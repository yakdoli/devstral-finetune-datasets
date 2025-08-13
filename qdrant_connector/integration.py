#!/usr/bin/env python3
"""
Qdrant 연동 모듈 통합 인터페이스
기존 md_processor 모듈과의 통합을 제공합니다.
"""

import logging
from typing import List, Dict, Any, Optional, Union
from pathlib import Path
import json

from .client import QdrantConnectionManager, QdrantClientConfig
from .searcher import QdrantDocumentSearcher
from .transformer import QdrantDataTransformer, DocumentTransformConfig
from .utils import (
    merge_document_sources,
    save_documents_to_json,
    load_documents_from_json,
    setup_logging
)

logger = logging.getLogger(__name__)


class IntegratedDocumentProcessor:
    """통합 문서 프로세서 클래스"""
    
    def __init__(
        self,
        qdrant_config: Optional[QdrantClientConfig] = None,
        md_processor_config: Optional[Dict[str, Any]] = None
    ):
        """
        통합 문서 프로세서를 초기화합니다.
        
        Args:
            qdrant_config: Qdrant 클라이언트 설정
            md_processor_config: MD 프로세서 설정
        """
        self.qdrant_config = qdrant_config or QdrantClientConfig()
        self.md_processor_config = md_processor_config or {}
        
        # Qdrant 연결 관리자
        self.qdrant_manager = QdrantConnectionManager(self.qdrant_config)
        
        # 검색기와 변환기
        self.qdrant_searcher = None
        self.qdrant_transformer = QdrantDataTransformer(DocumentTransformConfig())
        
        # MD 프로세서 (지연 로딩)
        self.md_processor = None
        
        # 통합 설정
        self.auto_merge = self.md_processor_config.get("auto_merge", True)
        self.merge_strategy = self.md_processor_config.get("merge_strategy", "append")
        self.save_merged = self.md_processor_config.get("save_merged", False)
        self.merged_output_path = self.md_processor_config.get("merged_output_path", "merged_documents.json")
    
    def _load_md_processor(self):
        """MD 프로세서를 지연 로딩합니다."""
        if self.md_processor is None:
            try:
                from md_processor import create_processor
                self.md_processor = create_processor()
                logger.info("MD 프로세서가 성공적으로 로드되었습니다.")
            except ImportError as e:
                logger.warning(f"MD 프로세서를 로드할 수 없습니다: {e}")
                self.md_processor = None
    
    def connect_qdrant(self) -> bool:
        """
        Qdrant 서버에 연결합니다.
        
        Returns:
            연결 성공 여부
        """
        success = self.qdrant_manager.connect()
        if success:
            self.qdrant_searcher = QdrantDocumentSearcher(self.qdrant_manager)
            logger.info("Qdrant 연결이 성공적으로 설정되었습니다.")
        else:
            logger.error(f"Qdrant 연결 실패: {self.qdrant_manager.connection_error}")
        return success
    
    def process_local_documents(
        self,
        base_paths: Optional[List[str]] = None,
        output_path: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        로컬 문서를 처리합니다.
        
        Args:
            base_paths: 스캔할 기본 경로 목록
            output_path: 출력 파일 경로
            
        Returns:
            처리된 로컬 문서 목록
        """
        self._load_md_processor()
        
        if not self.md_processor:
            logger.error("MD 프로세서를 사용할 수 없습니다.")
            return []
        
        try:
            # 기본 경로 설정
            if base_paths is None:
                base_paths = ['./output', './md_staging']
            
            # 문서 처리
            processed_docs = self.md_processor.process_documents(base_paths)
            
            # 결과 저장
            if output_path:
                save_documents_to_json(processed_docs, output_path)
                logger.info(f"로컬 문서가 {output_path}에 저장되었습니다.")
            
            logger.info(f"로컬 문서 처리 완료: {len(processed_docs)}개 문서")
            return processed_docs
            
        except Exception as e:
            logger.error(f"로컬 문서 처리 실패: {e}")
            return []
    
    def search_qdrant_documents(
        self,
        query: str,
        limit: int = 10,
        score_threshold: float = 0.5,
        metadata_filter: Optional[Dict[str, Any]] = None,
        search_type: str = "semantic"
    ) -> List[Dict[str, Any]]:
        """
        Qdrant에서 문서를 검색합니다.
        
        Args:
            query: 검색 쿼리
            limit: 반환할 결과 수
            score_threshold: 점수 임계값
            metadata_filter: 메타데이터 필터
            search_type: 검색 유형
            
        Returns:
            검색된 Qdrant 문서 목록
        """
        if not self.qdrant_searcher:
            logger.error("Qdrant 연결이 필요합니다.")
            return []
        
        try:
            # 문서 검색
            raw_results = self.qdrant_searcher.search_documents(
                query=query,
                limit=limit,
                score_threshold=score_threshold,
                metadata_filter=metadata_filter,
                search_type=search_type
            )
            
            # 결과 변환
            transformed_results = self.qdrant_transformer.transform_documents(raw_results)
            
            logger.info(f"Qdrant 문서 검색 완료: {len(transformed_results)}개 문서")
            return transformed_results
            
        except Exception as e:
            logger.error(f"Qdrant 문서 검색 실패: {e}")
            return []
    
    def get_all_qdrant_documents(
        self,
        limit: int = 1000,
        batch_size: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Qdrant의 모든 문서를 가져옵니다.
        
        Args:
            limit: 가져올 최대 문서 수
            batch_size: 배치 크기
            
        Returns:
            모든 Qdrant 문서 목록
        """
        if not self.qdrant_searcher:
            logger.error("Qdrant 연결이 필요합니다.")
            return []
        
        try:
            # 빈 쿼리로 모든 문서 검색
            all_docs = []
            offset = 0
            
            while len(all_docs) < limit:
                batch = self.qdrant_searcher.search_documents(
                    query="",
                    limit=min(batch_size, limit - len(all_docs)),
                    score_threshold=0.0
                )
                
                if not batch:
                    break
                
                transformed_batch = self.qdrant_transformer.transform_documents(batch)
                all_docs.extend(transformed_batch)
                offset += len(batch)
                
                logger.info(f"Qdrant 문서 배치 로드: {len(batch)}개 (총 {len(all_docs)}개)")
            
            logger.info(f"Qdrant 모든 문서 로드 완료: {len(all_docs)}개 문서")
            return all_docs[:limit]
            
        except Exception as e:
            logger.error(f"Qdrant 모든 문서 로드 실패: {e}")
            return []
    
    def merge_document_sources(
        self,
        local_documents: List[Dict[str, Any]],
        qdrant_documents: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        로컬 문서와 Qdrant 문서를 병합합니다.
        
        Args:
            local_documents: 로컬 문서 목록
            qdrant_documents: Qdrant 문서 목록
            
        Returns:
            병합된 문서 목록
        """
        try:
            merged_docs = merge_document_sources(
                local_documents,
                qdrant_documents,
                strategy=self.merge_strategy
            )
            
            # 병합된 결과 저장
            if self.save_merged:
                save_documents_to_json(merged_docs, self.merged_output_path)
                logger.info(f"병합된 문서가 {self.merged_output_path}에 저장되었습니다.")
            
            logger.info(f"문서 병합 완료: {len(merged_docs)}개 문서")
            return merged_docs
            
        except Exception as e:
            logger.error(f"문서 병합 실패: {e}")
            return []
    
    def create_conversation_context(
        self,
        query: str,
        context_type: str = "general",
        max_documents: int = 5,
        score_threshold: float = 0.7,
        metadata_filter: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        대화 생성을 위한 컨텍스트를 생성합니다.
        
        Args:
            query: 검색 쿼리
            context_type: 컨텍스트 유형
            max_documents: 최대 문서 수
            score_threshold: 점수 임계값
            metadata_filter: 메타데이터 필터
            
        Returns:
            컨텍스트 딕셔너리
        """
        if not self.qdrant_searcher:
            logger.error("Qdrant 연결이 필요합니다.")
            return {"formatted_context": "", "metadata": {}, "source_documents": []}
        
        try:
            # 관련 문서 검색
            relevant_docs = self.search_qdrant_documents(
                query=query,
                limit=max_documents,
                score_threshold=score_threshold,
                metadata_filter=metadata_filter,
                search_type="semantic"
            )
            
            if not relevant_docs:
                logger.warning(f"쿼리 '{query}'에 대한 관련 문서를 찾을 수 없습니다.")
                return {"formatted_context": "", "metadata": {}, "source_documents": []}
            
            # 컨텍스트 생성
            context = self.qdrant_transformer.create_conversation_context(
                documents=relevant_docs,
                query=query,
                context_type=context_type
            )
            
            logger.info(f"컨텍스트 생성 완료: {len(relevant_docs)}개 문서, {context['metadata']['context_length']}자")
            return context
            
        except Exception as e:
            logger.error(f"컨텍스트 생성 실패: {e}")
            return {"formatted_context": "", "metadata": {}, "source_documents": []}
    
    def batch_create_contexts(
        self,
        queries: List[str],
        context_type: str = "general",
        max_documents: int = 5,
        score_threshold: float = 0.7
    ) -> List[Dict[str, Any]]:
        """
        여러 쿼리에 대한 컨텍스트를 배치로 생성합니다.
        
        Args:
            queries: 검색 쿼리 목록
            context_type: 컨텍스트 유형
            max_documents: 최대 문서 수
            score_threshold: 점수 임계값
            
        Returns:
            컨텍스트 목록
        """
        contexts = []
        
        for query in queries:
            try:
                context = self.create_conversation_context(
                    query=query,
                    context_type=context_type,
                    max_documents=max_documents,
                    score_threshold=score_threshold
                )
                contexts.append(context)
                
            except Exception as e:
                logger.error(f"쿼리 '{query}' 컨텍스트 생성 실패: {e}")
                contexts.append({"formatted_context": "", "metadata": {}, "source_documents": []})
        
        logger.info(f"배치 컨텍스트 생성 완료: {len(contexts)}개 컨텍스트")
        return contexts
    
    def get_component_specific_context(
        self,
        component_name: str,
        context_type: str = "general",
        max_documents: int = 10
    ) -> Dict[str, Any]:
        """
        특정 컴포넌트에 대한 컨텍스트를 생성합니다.
        
        Args:
            component_name: 컴포넌트 이름
            context_type: 컨텍스트 유형
            max_documents: 최대 문서 수
            
        Returns:
            컴포넌트별 컨텍스트
        """
        if not self.qdrant_searcher:
            logger.error("Qdrant 연결이 필요합니다.")
            return {"formatted_context": "", "metadata": {}, "source_documents": []}
        
        try:
            # 컴포넌트별 문서 검색
            component_docs = self.qdrant_searcher.search_by_component(
                component_name=component_name,
                limit=max_documents
            )
            
            if not component_docs:
                logger.warning(f"컴포넌트 '{component_name}'에 대한 문서를 찾을 수 없습니다.")
                return {"formatted_context": "", "metadata": {}, "source_documents": []}
            
            # 컨텍스트 생성
            context = self.qdrant_transformer.create_conversation_context(
                documents=component_docs,
                query=f"{component_name} component documentation",
                context_type=context_type
            )
            
            logger.info(f"컴포넌트 '{component_name}' 컨텍스트 생성 완료: {len(component_docs)}개 문서")
            return context
            
        except Exception as e:
            logger.error(f"컴포넌트 '{component_name}' 컨텍스트 생성 실패: {e}")
            return {"formatted_context": "", "metadata": {}, "source_documents": []}
    
    def process_and_merge(
        self,
        query: Optional[str] = None,
        local_base_paths: Optional[List[str]] = None,
        qdrant_limit: int = 10,
        qdrant_score_threshold: float = 0.5,
        qdrant_metadata_filter: Optional[Dict[str, Any]] = None,
        output_path: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        로컬 문서와 Qdrant 문서를 처리하고 병합합니다.
        
        Args:
            query: Qdrant 검색 쿼리 (None이면 모든 Qdrant 문서 사용)
            local_base_paths: 로컬 문서 경로
            qdrant_limit: Qdrant 검색 결과 수
            qdrant_score_threshold: Qdrant 점수 임계값
            qdrant_metadata_filter: Qdrant 메타데이터 필터
            output_path: 결과 저장 경로
            
        Returns:
            병합된 문서 목록
        """
        try:
            # 로컬 문서 처리
            logger.info("로컬 문서 처리를 시작합니다...")
            local_docs = self.process_local_documents(local_base_paths)
            
            # Qdrant 문서 검색
            logger.info("Qdrant 문서 검색을 시작합니다...")
            if query:
                qdrant_docs = self.search_qdrant_documents(
                    query=query,
                    limit=qdrant_limit,
                    score_threshold=qdrant_score_threshold,
                    metadata_filter=qdrant_metadata_filter
                )
            else:
                qdrant_docs = self.get_all_qdrant_documents(limit=qdrant_limit)
            
            # 문서 병합
            if self.auto_merge and local_docs and qdrant_docs:
                logger.info("문서 병합을 시작합니다...")
                merged_docs = self.merge_document_sources(local_docs, qdrant_docs)
            else:
                merged_docs = local_docs + qdrant_docs
                logger.info(f"문서 병합 없이 단순 결합: {len(merged_docs)}개 문서")
            
            # 결과 저장
            if output_path:
                save_documents_to_json(merged_docs, output_path)
                logger.info(f"최종 결과가 {output_path}에 저장되었습니다.")
            
            logger.info(f"통합 처리 완료: {len(merged_docs)}개 문서")
            return merged_docs
            
        except Exception as e:
            logger.error(f"통합 처리 실패: {e}")
            return []
    
    def get_qdrant_collection_info(self) -> Optional[Dict[str, Any]]:
        """
        Qdrant 컬렉션 정보를 가져옵니다.
        
        Returns:
            컬렉션 정보 딕셔너리
        """
        return self.qdrant_manager.get_collection_info()
    
    def health_check(self) -> Dict[str, Any]:
        """
        시스템 상태를 확인합니다.
        
        Returns:
            상태 정보 딕셔너리
        """
        status = {
            "qdrant": self.qdrant_manager.health_check(),
            "md_processor": self.md_processor is not None,
            "auto_merge": self.auto_merge,
            "merge_strategy": self.merge_strategy
        }
        
        return status
    
    def disconnect(self):
        """Qdrant 연결을 종료합니다."""
        if self.qdrant_manager:
            self.qdrant_manager.disconnect()
            logger.info("Qdrant 연결이 종료되었습니다.")


def create_integrated_processor(
    qdrant_host: str = "100.100.88.88",
    qdrant_port: int = 6333,
    qdrant_api_key: Optional[str] = None,
    qdrant_collection: str = "ws-7491d651ae044c78",
    auto_merge: bool = True,
    merge_strategy: str = "append",
    save_merged: bool = False,
    merged_output_path: str = "merged_documents.json"
) -> IntegratedDocumentProcessor:
    """
    통합 문서 프로세서를 생성합니다.
    
    Args:
        qdrant_host: Qdrant 호스트 주소
        qdrant_port: Qdrant 포트
        qdrant_api_key: Qdrant API 키
        qdrant_collection: Qdrant 컬렉션 이름
        auto_merge: 자동 병합 여부
        merge_strategy: 병합 전략
        save_merged: 병합 결과 저장 여부
        merged_output_path: 병합 결과 저장 경로
        
    Returns:
        IntegratedDocumentProcessor 인스턴스
    """
    # Qdrant 설정
    qdrant_config = QdrantClientConfig(
        host=qdrant_host,
        port=qdrant_port,
        api_key=qdrant_api_key,
        collection_name=qdrant_collection
    )
    
    # MD 프로세서 설정
    md_processor_config = {
        "auto_merge": auto_merge,
        "merge_strategy": merge_strategy,
        "save_merged": save_merged,
        "merged_output_path": merged_output_path
    }
    
    return IntegratedDocumentProcessor(
        qdrant_config=qdrant_config,
        md_processor_config=md_processor_config
    )


def create_integrated_processor_from_env() -> IntegratedDocumentProcessor:
    """
    환경변수에서 설정을 읽어 통합 문서 프로세서를 생성합니다.
    
    Returns:
        IntegratedDocumentProcessor 인스턴스
    """
    from .utils import get_environment_config
    
    env_config = get_environment_config()
    
    return create_integrated_processor(
        qdrant_host=env_config["host"],
        qdrant_port=env_config["port"],
        qdrant_api_key=env_config["api_key"],
        qdrant_collection=env_config["collection_name"],
        auto_merge=True,
        merge_strategy="append",
        save_merged=True
    )


# 예제 사용법
def example_usage():
    """통합 프로세서 사용 예제"""
    logging.basicConfig(level=logging.INFO)
    
    # 통합 프로세서 생성
    processor = create_integrated_processor()
    
    # Qdrant 연결
    if processor.connect_qdrant():
        print("Qdrant 연결 성공!")
        
        # 상태 확인
        health = processor.health_check()
        print(f"시스템 상태: {health}")
        
        # 컬렉션 정보 확인
        collection_info = processor.get_qdrant_collection_info()
        if collection_info:
            print(f"컬렉션 정보: {collection_info}")
        
        # 통합 처리 실행
        merged_docs = processor.process_and_merge(
            query="syncfusion",
            local_base_paths=["./output", "./md_staging"],
            qdrant_limit=20,
            output_path="final_merged_documents.json"
        )
        
        print(f"최종 결과: {len(merged_docs)}개 문서")
        
        # 연결 종료
        processor.disconnect()
    else:
        print("Qdrant 연결 실패")


if __name__ == "__main__":
    example_usage()