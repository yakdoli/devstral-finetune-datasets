#!/usr/bin/env python3
"""
Qdrant 데이터 변환기 모듈
Qdrant에서 가져온 데이터를 표준 형식으로 변환합니다.
"""

import logging
from typing import List, Dict, Any, Optional, Union, Generator
from dataclasses import dataclass
from datetime import datetime
import json
import re
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class DocumentTransformConfig:
    """문서 변환 설정 클래스"""
    
    def __init__(
        self,
        include_original_payload: bool = True,
        include_vector: bool = False,
        max_content_length: int = 50000,
        min_quality_score: float = 0.1,
        normalize_content: bool = True,
        extract_metadata: bool = True,
        generate_missing_fields: bool = True
    ):
        """
        문서 변환 설정을 초기화합니다.
        
        Args:
            include_original_payload: 원본 페이로드 포함 여부
            include_vector: 벡터 데이터 포함 여부
            max_content_length: 최대 콘텐츠 길이
            min_quality_score: 최소 품질 점수
            normalize_content: 콘텐츠 정규화 여부
            extract_metadata: 메타데이터 추출 여부
            generate_missing_fields: 누락된 필드 생성 여부
        """
        self.include_original_payload = include_original_payload
        self.include_vector = include_vector
        self.max_content_length = max_content_length
        self.min_quality_score = min_quality_score
        self.normalize_content = normalize_content
        self.extract_metadata = extract_metadata
        self.generate_missing_fields = generate_missing_fields


class QdrantDataTransformer:
    """Qdrant 데이터 변환기 클래스"""
    
    def __init__(self, config: DocumentTransformConfig):
        """
        Qdrant 데이터 변환기를 초기화합니다.
        
        Args:
            config: 문서 변환 설정
        """
        self.config = config
    
    def transform_document(
        self,
        qdrant_document: Dict[str, Any],
        source_metadata: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        단일 문서를 변환합니다.
        
        Args:
            qdrant_document: Qdrant 문서 데이터
            source_metadata: 소스별 메타데이터
            
        Returns:
            변환된 문서 또는 None (품질 점수가 낮은 경우)
        """
        try:
            # 품질 점수 확인
            quality_score = qdrant_document.get("quality_score", 1.0)
            if quality_score < self.config.min_quality_score:
                logger.debug(f"품질 점수가 낮아 문서를 건너뜁니다: {quality_score}")
                return None
            
            # 기본 필드 추출
            doc_id = qdrant_document.get("id")
            if not doc_id:
                logger.warning("문서 ID가 없습니다")
                return None
            
            # 페이로드에서 정보 추출
            payload = qdrant_document.get("metadata", {}).get("original_payload", {})
            
            # 제목 추출
            title = self._extract_title(qdrant_document, payload)
            
            # 컴포넌트 추출
            component = self._extract_component(qdrant_document, payload)
            
            # 페이지 추출
            page = self._extract_page(qdrant_document, payload)
            
            # 콘텐츠 추출 및 정규화
            content = self._extract_and_normalize_content(qdrant_document, payload)
            
            if not content or len(content.strip()) == 0:
                logger.warning(f"콘텐츠가 없는 문서: {doc_id}")
                return None
            
            # 표준 문서 구조 생성
            transformed_doc = {
                "id": doc_id,
                "title": title,
                "component": component,
                "page": page,
                "content": content,
                "metadata": self._build_metadata(qdrant_document, payload, source_metadata),
                "quality_score": quality_score
            }
            
            # 누락된 필드 생성
            if self.config.generate_missing_fields:
                transformed_doc = self._generate_missing_fields(transformed_doc)
            
            # 벡터 데이터 포함
            if self.config.include_vector:
                vector = qdrant_document.get("metadata", {}).get("vector")
                if vector:
                    transformed_doc["metadata"]["vector"] = vector
            
            # 원본 페이로드 포함
            if self.config.include_original_payload:
                transformed_doc["metadata"]["original_payload"] = payload
            
            return transformed_doc
            
        except Exception as e:
            logger.error(f"문서 변환 실패: {e}")
            return None
    
    def transform_documents(
        self,
        qdrant_documents: List[Dict[str, Any]],
        source_metadata: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        여러 문서를 변환합니다.
        
        Args:
            qdrant_documents: Qdrant 문서 목록
            source_metadata: 소스별 메타데이터
            
        Returns:
            변환된 문서 목록
        """
        transformed_docs = []
        
        for doc in qdrant_documents:
            try:
                transformed_doc = self.transform_document(doc, source_metadata)
                if transformed_doc:
                    transformed_docs.append(transformed_doc)
            except Exception as e:
                logger.error(f"문서 변환 중 오류 발생: {e}")
                continue
        
        logger.info(f"문서 변환 완료: {len(transformed_docs)}/{len(qdrant_documents)}")
        return transformed_docs
    
    def transform_documents_generator(
        self,
        qdrant_documents: List[Dict[str, Any]],
        source_metadata: Optional[Dict[str, Any]] = None,
        batch_size: int = 100
    ) -> Generator[List[Dict[str, Any]], None, None]:
        """
        문서를 배치 단위로 변환하는 제너레이터
        
        Args:
            qdrant_documents: Qdrant 문서 목록
            source_metadata: 소스별 메타데이터
            batch_size: 배치 크기
            
        Yields:
            변환된 문서 배치
        """
        for i in range(0, len(qdrant_documents), batch_size):
            batch = qdrant_documents[i:i + batch_size]
            yield self.transform_documents(batch, source_metadata)
    
    def _extract_title(
        self,
        qdrant_document: Dict[str, Any],
        payload: Dict[str, Any]
    ) -> str:
        """제목을 추출합니다."""
        # 우선순위: qdrant_document > payload > 기본값
        title = (
            qdrant_document.get("title") or
            payload.get("title") or
            payload.get("document_title") or
            payload.get("filename") or
            f"Document {qdrant_document.get('id', 'unknown')}"
        )
        
        # 제목 정규화
        if isinstance(title, str):
            title = title.strip()
            if len(title) > 100:
                title = title[:97] + "..."
        
        return title or "Untitled"
    
    def _extract_component(
        self,
        qdrant_document: Dict[str, Any],
        payload: Dict[str, Any]
    ) -> str:
        """컴포넌트를 추출합니다."""
        # 우선순위: qdrant_document > payload > 메타데이터 추출
        component = (
            qdrant_document.get("component") or
            payload.get("component") or
            payload.get("category") or
            self._infer_component_from_content(payload.get("content", "")) or
            "unknown"
        )
        
        return component or "unknown"
    
    def _extract_page(
        self,
        qdrant_document: Dict[str, Any],
        payload: Dict[str, Any]
    ) -> str:
        """페이지를 추출합니다."""
        # 우선순위: qdrant_document > payload > 기본값
        page = (
            qdrant_document.get("page") or
            payload.get("page") or
            payload.get("source_page") or
            payload.get("filename") or
            "unknown"
        )
        
        return page or "unknown"
    
    def _extract_and_normalize_content(
        self,
        qdrant_document: Dict[str, Any],
        payload: Dict[str, Any]
    ) -> str:
        """콘텐츠를 추출하고 정규화합니다."""
        # 콘텐츠 추출 (우선순위: qdrant_document > payload)
        content = (
            qdrant_document.get("content") or
            payload.get("content") or
            payload.get("text") or
            payload.get("document_content") or
            ""
        )
        
        if not content:
            return ""
        
        # 콘텐츠 길이 제한
        if len(content) > self.config.max_content_length:
            content = content[:self.config.max_content_length - 3] + "..."
        
        # 콘텐츠 정규화
        if self.config.normalize_content:
            content = self._normalize_content(content)
        
        return content
    
    def _normalize_content(self, content: str) -> str:
        """콘텐츠를 정규화합니다."""
        import unicodedata
        import re
        
        # 유니코드 정규화
        content = unicodedata.normalize('NFKC', content)
        
        # 여러 공백을 단일 공백으로 변경
        content = re.sub(r'\s+', ' ', content)
        
        # 줄바꿈 정리
        content = re.sub(r'\n\s*\n', '\n\n', content)
        
        # 특수 문자 정리
        content = re.sub(r'[^\w\s\-_.(),;:!?\'"[\]{}@#$%^&*+=|\\/<>~`]', '', content)
        
        # 양 끝 공백 제거
        content = content.strip()
        
        return content
    
    def _infer_component_from_content(self, content: str) -> Optional[str]:
        """콘텐츠에서 컴포넌트를 추론합니다."""
        if not content:
            return None
        
        # 간단한 키워드 기반 추론
        content_lower = content.lower()
        
        # Syncfusion 컴포넌트 키워드 매핑 (우선순위 순서)
        component_keywords = {
            "grid": ["grid", "data table", "datatable", "table", "spreadsheet", "data grid"],
            "chart": ["chart", "graph", "plot", "visualization", "series"],
            "diagram": ["diagram", "flowchart", "workflow", "node", "connector"],
            "pdf": ["pdf", "document viewer", "pdf viewer"],
            "excel": ["excel", "xls", "xlsx", "spreadsheet", "workbook"],
            "word": ["word", "doc", "docx", "document", "text editor"],
            "powerpoint": ["powerpoint", "ppt", "pptx", "presentation"],
            "schedule": ["schedule", "calendar", "appointment", "scheduler"],
            "gauge": ["gauge", "meter", "indicator", "circular gauge"],
            "pivot": ["pivot", "olap", "cube", "pivot grid"],
            "edit": ["edit", "editor", "rich text", "text editor"],
            "html": ["html", "web", "browser", "html viewer"],
            "qtp": ["qtp", "test", "automation", "testing"],
            "tools": ["tools", "utility", "helper", "common tools"],
            "calculate": ["calculate", "formula", "calculation", "math"],
            "common": ["common", "shared", "base", "utility"],
            "dicom": ["dicom", "medical", "image", "medical imaging"],
            "docio": ["docio", "document io", "document processing"],
            "olap": ["olap", "cube", "analysis", "multidimensional"],
            "projio": ["projio", "project", "management", "project io"],
            "viewer": ["viewer", "preview", "display", "document viewer"]
        }
        
        # 점수 기반 매칭 (더 정확한 추론)
        component_scores = {}
        
        for component, keywords in component_keywords.items():
            score = 0
            for keyword in keywords:
                if keyword in content_lower:
                    # 키워드 길이에 따른 가중치 (긴 키워드가 더 정확)
                    score += len(keyword.split())
            
            if score > 0:
                component_scores[component] = score
        
        # 가장 높은 점수의 컴포넌트 반환
        if component_scores:
            return max(component_scores, key=component_scores.get)
        
        return None
    
    def _build_metadata(
        self,
        qdrant_document: Dict[str, Any],
        payload: Dict[str, Any],
        source_metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """메타데이터를 구축합니다."""
        metadata = {
            "source": "qdrant",
            "collection": qdrant_document.get("metadata", {}).get("collection", "unknown"),
            "vector_score": qdrant_document.get("metadata", {}).get("vector_score", 0.0),
            "qdrant_id": qdrant_document.get("id"),
            "extracted_at": datetime.now().isoformat()
        }
        
        # 기존 메타데이터 병합
        existing_metadata = qdrant_document.get("metadata", {})
        if existing_metadata:
            # 기존 메타데이터에서 중복되지 않는 필드만 추가
            for key, value in existing_metadata.items():
                if key not in ["source", "collection", "vector_score", "original_payload"]:
                    metadata[key] = value
        
        # 페이로드에서 추가 메타데이터 추출
        if self.config.extract_metadata:
            extracted_metadata = self._extract_metadata_from_payload(payload)
            metadata.update(extracted_metadata)
        
        # 소스별 메타데이터 추가
        if source_metadata:
            metadata.update(source_metadata)
        
        return metadata
    
    def _extract_metadata_from_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """페이로드에서 메타데이터를 추출합니다."""
        metadata = {}
        
        # 일반적인 메타데이터 필드
        common_fields = [
            "author", "created_at", "updated_at", "version", "tags",
            "category", "subcategory", "language", "format", "size"
        ]
        
        for field in common_fields:
            if field in payload:
                metadata[field] = payload[field]
        
        # 커스텀 메타데이터 필드 (metadata 키 아래)
        if "metadata" in payload and isinstance(payload["metadata"], dict):
            metadata.update(payload["metadata"])
        
        return metadata
    
    def _generate_missing_fields(self, document: Dict[str, Any]) -> Dict[str, Any]:
        """누락된 필드를 생성합니다."""
        # ID가 없는 경우 생성
        if not document.get("id"):
            import hashlib
            content_hash = hashlib.md5(document.get("content", "").encode()).hexdigest()[:8]
            document["id"] = f"qdrant_{content_hash}"
        
        # 품질 점수가 없는 경우 생성
        if "quality_score" not in document:
            document["quality_score"] = 1.0
        
        # 메타데이터가 없는 경우 생성
        if "metadata" not in document:
            document["metadata"] = {}
        
        return document
    
    def merge_with_local_documents(
        self,
        qdrant_documents: List[Dict[str, Any]],
        local_documents: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Qdrant 문서와 로컬 문서를 병합합니다.
        
        Args:
            qdrant_documents: Qdrant 문서 목록
            local_documents: 로컬 문서 목록
            
        Returns:
            병합된 문서 목록
        """
        # ID를 기준으로 문서 매핑
        qdrant_docs_map = {doc["id"]: doc for doc in qdrant_documents}
        local_docs_map = {doc["id"]: doc for doc in local_documents}
        
        merged_docs = []
        
        # 모든 고유 ID 수집
        all_ids = set(qdrant_docs_map.keys()).union(set(local_docs_map.keys()))
        
        for doc_id in all_ids:
            qdrant_doc = qdrant_docs_map.get(doc_id)
            local_doc = local_docs_map.get(doc_id)
            
            if qdrant_doc and local_doc:
                # 양쪽에 모두 있는 경우 - 우선순위: 로컬 > Qdrant
                merged_doc = local_doc.copy()
                merged_doc["metadata"]["qdrant_equivalent"] = {
                    "title": qdrant_doc.get("title"),
                    "component": qdrant_doc.get("component"),
                    "quality_score": qdrant_doc.get("quality_score"),
                    "vector_score": qdrant_doc.get("metadata", {}).get("vector_score")
                }
            elif qdrant_doc:
                # Qdrant에만 있는 경우
                merged_doc = qdrant_doc.copy()
                merged_doc["metadata"]["source_type"] = "qdrant_only"
            elif local_doc:
                # 로컬에만 있는 경우
                merged_doc = local_doc.copy()
                merged_doc["metadata"]["source_type"] = "local_only"
            else:
                continue
            
            merged_docs.append(merged_doc)
        
        logger.info(f"문서 병합 완료: {len(merged_docs)}개 문서")
        return merged_docs
    
    def format_context_for_generation(
        self,
        documents: List[Dict[str, Any]],
        max_context_length: int = 8000,
        include_metadata: bool = True,
        context_template: Optional[str] = None
    ) -> str:
        """
        문서들을 대화 생성용 컨텍스트로 포맷팅합니다.
        
        Args:
            documents: 포맷팅할 문서 목록
            max_context_length: 최대 컨텍스트 길이
            include_metadata: 메타데이터 포함 여부
            context_template: 커스텀 컨텍스트 템플릿
            
        Returns:
            포맷팅된 컨텍스트 문자열
        """
        if not documents:
            return ""
        
        # 기본 템플릿
        if context_template is None:
            context_template = """
## {title}
**Component:** {component} | **Page:** {page} | **Quality:** {quality_score:.2f}

{content}

---
"""
        
        formatted_contexts = []
        current_length = 0
        
        for doc in documents:
            # 문서 정보 추출
            title = doc.get("title", "Untitled")
            component = doc.get("component", "unknown")
            page = doc.get("page", "unknown")
            content = doc.get("content", "")
            quality_score = doc.get("quality_score", 0.0)
            
            # 메타데이터 추가
            metadata_str = ""
            if include_metadata and doc.get("metadata"):
                metadata = doc["metadata"]
                vector_score = metadata.get("vector_score", 0.0)
                source = metadata.get("source", "unknown")
                metadata_str = f" | **Source:** {source} | **Vector Score:** {vector_score:.2f}"
            
            # 컨텍스트 포맷팅
            formatted_context = context_template.format(
                title=title,
                component=component,
                page=page,
                content=content,
                quality_score=quality_score,
                metadata=metadata_str
            )
            
            # 길이 확인
            if current_length + len(formatted_context) > max_context_length:
                if not formatted_contexts:
                    # 첫 번째 문서가 너무 긴 경우 잘라서 포함
                    truncated_content = content[:max_context_length - 500] + "..."
                    formatted_context = context_template.format(
                        title=title,
                        component=component,
                        page=page,
                        content=truncated_content,
                        quality_score=quality_score,
                        metadata=metadata_str
                    )
                    formatted_contexts.append(formatted_context)
                break
            
            formatted_contexts.append(formatted_context)
            current_length += len(formatted_context)
        
        return "\n".join(formatted_contexts)
    
    def create_conversation_context(
        self,
        documents: List[Dict[str, Any]],
        query: Optional[str] = None,
        context_type: str = "general"
    ) -> Dict[str, Any]:
        """
        대화 생성을 위한 컨텍스트를 생성합니다.
        
        Args:
            documents: 컨텍스트로 사용할 문서 목록
            query: 사용자 쿼리 (선택적)
            context_type: 컨텍스트 유형 ("general", "api", "tutorial", "troubleshooting")
            
        Returns:
            컨텍스트 딕셔너리
        """
        # 컨텍스트 유형별 템플릿
        templates = {
            "general": """
## {title}
**Component:** {component} | **Page:** {page}

{content}

---
""",
            "api": """
## API Reference: {title}
**Component:** {component} | **Page:** {page}

{content}

**Usage Examples and Parameters:**
{api_examples}

---
""",
            "tutorial": """
## Tutorial: {title}
**Component:** {component} | **Step:** {page}

{content}

**Key Points:**
{key_points}

---
""",
            "troubleshooting": """
## Issue: {title}
**Component:** {component} | **Reference:** {page}

**Problem Description:**
{content}

**Solution Steps:**
{solution_steps}

---
"""
        }
        
        template = templates.get(context_type, templates["general"])
        
        # 문서별 추가 정보 추출
        enhanced_docs = []
        for doc in documents:
            enhanced_doc = doc.copy()
            
            # API 예제 추출
            if context_type == "api":
                enhanced_doc["api_examples"] = self._extract_api_examples(doc.get("content", ""))
            else:
                enhanced_doc["api_examples"] = ""
            
            # 핵심 포인트 추출
            if context_type == "tutorial":
                enhanced_doc["key_points"] = self._extract_key_points(doc.get("content", ""))
            else:
                enhanced_doc["key_points"] = ""
            
            # 해결 단계 추출
            if context_type == "troubleshooting":
                enhanced_doc["solution_steps"] = self._extract_solution_steps(doc.get("content", ""))
            else:
                enhanced_doc["solution_steps"] = ""
            
            enhanced_docs.append(enhanced_doc)
        
        # 컨텍스트 포맷팅
        formatted_context = self.format_context_for_generation(
            enhanced_docs,
            context_template=template
        )
        
        # 컨텍스트 메타데이터 생성
        context_metadata = {
            "document_count": len(documents),
            "context_type": context_type,
            "query": query,
            "components": list(set(doc.get("component", "unknown") for doc in documents)),
            "pages": list(set(doc.get("page", "unknown") for doc in documents)),
            "avg_quality_score": sum(doc.get("quality_score", 0.0) for doc in documents) / len(documents) if documents else 0.0,
            "total_content_length": sum(len(doc.get("content", "")) for doc in documents),
            "context_length": len(formatted_context)
        }
        
        return {
            "formatted_context": formatted_context,
            "metadata": context_metadata,
            "source_documents": documents
        }
    
    def _extract_api_examples(self, content: str) -> str:
        """콘텐츠에서 API 예제를 추출합니다."""
        import re
        
        # 코드 블록 패턴 (더 유연하게)
        code_blocks = re.findall(r'```[^`]*?```', content, re.DOTALL)
        
        # 메서드 호출 패턴
        method_calls = re.findall(r'(\w+\.\w+\([^)]*\))', content)
        
        examples = []
        
        # 코드 블록에서 라인별로 추출
        for block in code_blocks[:2]:  # 최대 2개 코드 블록
            # 코드 블록 내용만 추출 (``` 제거)
            block_content = re.sub(r'```[\w]*\n?', '', block)
            block_content = re.sub(r'\n?```', '', block_content)
            
            # 각 라인을 개별 예제로 처리
            lines = [line.strip() for line in block_content.split('\n') if line.strip()]
            examples.extend(lines[:3])  # 블록당 최대 3라인
        
        # 메서드 호출 추가
        if method_calls:
            examples.extend(method_calls[:3])  # 최대 3개 메서드 호출
        
        return "\n".join(f"- {example.strip()}" for example in examples[:5] if example.strip())
    
    def _extract_key_points(self, content: str) -> str:
        """콘텐츠에서 핵심 포인트를 추출합니다."""
        import re
        
        # 불릿 포인트 패턴
        bullet_points = re.findall(r'[•\-\*]\s*(.+)', content)
        
        # 번호 목록 패턴
        numbered_points = re.findall(r'\d+\.\s*(.+)', content)
        
        # 중요 표시 패턴
        important_points = re.findall(r'\*\*(.*?)\*\*', content)
        
        points = []
        if bullet_points:
            points.extend(bullet_points[:3])
        if numbered_points:
            points.extend(numbered_points[:3])
        if important_points:
            points.extend(important_points[:3])
        
        return "\n".join(f"- {point.strip()}" for point in points[:5])
    
    def _extract_solution_steps(self, content: str) -> str:
        """콘텐츠에서 해결 단계를 추출합니다."""
        import re
        
        # 단계별 패턴
        step_patterns = [
            r'Step\s*\d+[:\.]?\s*(.+)',
            r'\d+\.\s*(.+)',
            r'First[,\s]+(.+)',
            r'Then[,\s]+(.+)',
            r'Finally[,\s]+(.+)'
        ]
        
        steps = []
        for pattern in step_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            steps.extend(matches)
        
        return "\n".join(f"{i+1}. {step.strip()}" for i, step in enumerate(steps[:5]))


# 유틸리티 함수
def create_transformer(
    include_original_payload: bool = True,
    include_vector: bool = False,
    max_content_length: int = 50000,
    min_quality_score: float = 0.1
) -> QdrantDataTransformer:
    """
    데이터 변환기를 생성합니다.
    
    Args:
        include_original_payload: 원본 페이로드 포함 여부
        include_vector: 벡터 데이터 포함 여부
        max_content_length: 최대 콘텐츠 길이
        min_quality_score: 최소 품질 점수
        
    Returns:
        QdrantDataTransformer 인스턴스
    """
    config = DocumentTransformConfig(
        include_original_payload=include_original_payload,
        include_vector=include_vector,
        max_content_length=max_content_length,
        min_quality_score=min_quality_score
    )
    return QdrantDataTransformer(config)


if __name__ == "__main__":
    # 테스트 코드
    logging.basicConfig(level=logging.INFO)
    
    # 변환기 생성
    transformer = create_transformer()
    
    # 테스트 데이터
    test_qdrant_doc = {
        "id": "test_doc_001",
        "title": "Test Document",
        "component": "grid",
        "page": "page_001",
        "content": "This is a test document content for Qdrant transformation.",
        "metadata": {
            "source": "qdrant",
            "collection": "ws-7491d651ae044c78",
            "vector_score": 0.85,
            "original_payload": {
                "content": "This is a test document content for Qdrant transformation.",
                "filename": "test.md",
                "author": "test_user"
            }
        },
        "quality_score": 0.85
    }
    
    # 문서 변환 테스트
    transformed_doc = transformer.transform_document(test_qdrant_doc)
    print("변환된 문서:")
    print(json.dumps(transformed_doc, indent=2, ensure_ascii=False))