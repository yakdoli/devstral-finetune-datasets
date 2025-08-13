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
        
        # Syncfusion 컴포넌트 키워드 매핑
        component_keywords = {
            "grid": ["grid", "datatable", "table", "spreadsheet"],
            "chart": ["chart", "graph", "plot", "visualization"],
            "diagram": ["diagram", "flowchart", "workflow"],
            "pdf": ["pdf", "document", "report"],
            "excel": ["excel", "xls", "spreadsheet", "workbook"],
            "word": ["word", "doc", "document", "text"],
            "powerpoint": ["powerpoint", "ppt", "presentation"],
            "schedule": ["schedule", "calendar", "appointment"],
            "gauge": ["gauge", "meter", "indicator"],
            "pivot": ["pivot", "olap", "cube"],
            "edit": ["edit", "editor", "rich text"],
            "html": ["html", "web", "browser"],
            "qtp": ["qtp", "test", "automation"],
            "tools": ["tools", "utility", "helper"],
            "calculate": ["calculate", "formula", "calculation"],
            "common": ["common", "shared", "base"],
            "dicom": ["dicom", "medical", "image"],
            "docio": ["docio", "document", "report"],
            "olap": ["olap", "cube", "analysis"],
            "projio": ["projio", "project", "management"],
            "viewer": ["viewer", "preview", "display"]
        }
        
        for component, keywords in component_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                return component
        
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