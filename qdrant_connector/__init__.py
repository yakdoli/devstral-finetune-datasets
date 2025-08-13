#!/usr/bin/env python3
"""
Qdrant 연동 모듈 초기화 파일
Qdrant 벡터 데이터베이스와의 연동을 위한 핵심 모듈을 제공합니다.
"""

from typing import Optional, Dict, Any, List, Union
from pathlib import Path
from .client import (
    QdrantClientConfig,
    QdrantConnectionManager,
    QdrantClientFactory,
    create_qdrant_client,
    get_global_client_manager,
    set_global_client_manager
)
from .searcher import (
    SearchQuery,
    SearchResult,
    BatchSearchResult,
    QdrantDocumentSearcher
)
from .transformer import (
    DocumentTransformConfig,
    QdrantDataTransformer,
    create_transformer
)
from .utils import (
    setup_logging,
    normalize_text,
    clean_filename,
    generate_unique_id,
    extract_keywords_from_text,
    calculate_content_quality,
    merge_document_sources,
    save_documents_to_json,
    load_documents_from_json,
    create_qdrant_filter_from_dict,
    validate_qdrant_connection_config,
    get_environment_config,
    benchmark_search_performance
)
from .integration import (
    IntegratedDocumentProcessor,
    create_integrated_processor,
    create_integrated_processor_from_env
)

__version__ = "1.0.0"
__author__ = "Qdrant Connector Team"
__email__ = "support@example.com"
__description__ = "Qdrant Vector Database Connector for Syncfusion WinForms Documentation"

__all__ = [
    # Client
    'QdrantClientConfig',
    'QdrantConnectionManager',
    'QdrantClientFactory',
    'create_qdrant_client',
    'get_global_client_manager',
    'set_global_client_manager',
    
    # Searcher
    'SearchQuery',
    'SearchResult',
    'BatchSearchResult',
    'QdrantDocumentSearcher',
    
    # Transformer
    'DocumentTransformConfig',
    'QdrantDataTransformer',
    'create_transformer',
    
    # Integration
    'IntegratedDocumentProcessor',
    'create_integrated_processor',
    'create_integrated_processor_from_env',
    
    # Utils
    'setup_logging',
    'normalize_text',
    'clean_filename',
    'generate_unique_id',
    'extract_keywords_from_text',
    'calculate_content_quality',
    'merge_document_sources',
    'save_documents_to_json',
    'load_documents_from_json',
    'create_qdrant_filter_from_dict',
    'validate_qdrant_connection_config',
    'get_environment_config',
    'benchmark_search_performance',
    
    # Version info
    '__version__',
    '__author__',
    '__email__',
    '__description__'
]


class QdrantConnector:
    """Qdrant 연동 모듈 메인 클래스"""
    
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6333,
        api_key: Optional[str] = None,
        collection_name: str = "ws-7491d651ae044c78",
        config: Optional[QdrantClientConfig] = None
    ):
        """
        Qdrant 연동 모듈을 초기화합니다.
        
        Args:
            host: Qdrant 호스트 주소
            port: Qdrant 포트
            api_key: API 키
            collection_name: 컬렉션 이름
            config: Qdrant 클라이언트 설정 (선택적)
        """
        if config:
            self.config = config
        else:
            self.config = QdrantClientConfig(
                host=host,
                port=port,
                api_key=api_key,
                collection_name=collection_name
            )
        
        self.connection_manager = QdrantConnectionManager(self.config)
        self.searcher = None
        self.transformer = None
        
        # 기본 변환기 생성
        self.transformer_config = DocumentTransformConfig()
        self.transformer = QdrantDataTransformer(self.transformer_config)
    
    def connect(self) -> bool:
        """
        Qdrant 서버에 연결합니다.
        
        Returns:
            연결 성공 여부
        """
        success = self.connection_manager.connect()
        if success:
            self.searcher = QdrantDocumentSearcher(self.connection_manager)
        return success
    
    def disconnect(self):
        """Qdrant 연결을 종료합니다."""
        self.connection_manager.disconnect()
        self.searcher = None
    
    def search_documents(
        self,
        query: str,
        limit: int = 10,
        score_threshold: float = 0.5,
        metadata_filter: Optional[Dict[str, Any]] = None,
        search_type: str = "semantic",
        vector: Optional[List[float]] = None,
        transform: bool = True
    ) -> Union[List[Dict[str, Any]], List[SearchResult]]:
        """
        문서를 검색합니다.
        
        Args:
            query: 검색 쿼리
            limit: 반환할 결과 수
            score_threshold: 점수 임계값
            metadata_filter: 메타데이터 필터
            search_type: 검색 유형
            vector: 직접 제공된 벡터
            transform: 결과 변환 여부
            
        Returns:
            검색된 문서 목록 또는 원본 검색 결과
        """
        if not self.searcher:
            raise ConnectionError("Qdrant 연결이 필요합니다")
        
        raw_results = self.searcher.search_documents(
            query=query,
            limit=limit,
            score_threshold=score_threshold,
            metadata_filter=metadata_filter,
            search_type=search_type,
            vector=vector
        )
        
        if transform:
            return self.transformer.transform_documents(raw_results)
        else:
            return raw_results
    
    def search_by_metadata(
        self,
        metadata_filter: Dict[str, Any],
        limit: int = 10,
        transform: bool = True
    ) -> Union[List[Dict[str, Any]], List[SearchResult]]:
        """
        메타데이터 기반으로 문서를 검색합니다.
        
        Args:
            metadata_filter: 메타데이터 필터
            limit: 반환할 결과 수
            transform: 결과 변환 여부
            
        Returns:
            검색된 문서 목록 또는 원본 검색 결과
        """
        if not self.searcher:
            raise ConnectionError("Qdrant 연결이 필요합니다")
        
        raw_results = self.searcher.search_by_metadata(
            metadata_filter=metadata_filter,
            limit=limit
        )
        
        if transform:
            return self.transformer.transform_documents(raw_results)
        else:
            return raw_results
    
    def search_similar_documents(
        self,
        document_id: str,
        limit: int = 10,
        score_threshold: float = 0.5,
        transform: bool = True
    ) -> Union[List[Dict[str, Any]], List[SearchResult]]:
        """
        특정 문서와 유사한 문서를 검색합니다.
        
        Args:
            document_id: 기준 문서 ID
            limit: 반환할 결과 수
            score_threshold: 점수 임계값
            transform: 결과 변환 여부
            
        Returns:
            검색된 문서 목록 또는 원본 검색 결과
        """
        if not self.searcher:
            raise ConnectionError("Qdrant 연결이 필요합니다")
        
        raw_results = self.searcher.search_similar_documents(
            document_id=document_id,
            limit=limit,
            score_threshold=score_threshold
        )
        
        if transform:
            return self.transformer.transform_documents(raw_results)
        else:
            return raw_results
    
    def batch_search(
        self,
        queries: List[str],
        limit: int = 10,
        score_threshold: float = 0.5,
        metadata_filter: Optional[Dict[str, Any]] = None,
        batch_size: int = 10
    ) -> List[BatchSearchResult]:
        """
        여러 쿼리를 배치로 검색합니다.
        
        Args:
            queries: 검색 쿼리 목록
            limit: 각 쿼리당 반환할 결과 수
            score_threshold: 점수 임계값
            metadata_filter: 메타데이터 필터
            batch_size: 배치 크기
            
        Returns:
            배치 검색 결과 목록
        """
        if not self.searcher:
            raise ConnectionError("Qdrant 연결이 필요합니다")
        
        return self.searcher.batch_search(
            queries=queries,
            limit=limit,
            score_threshold=score_threshold,
            metadata_filter=metadata_filter,
            batch_size=batch_size
        )
    
    def get_document_count(self) -> int:
        """
        컬렉션의 문서 수를 가져옵니다.
        
        Returns:
            문서 수
        """
        if not self.searcher:
            raise ConnectionError("Qdrant 연결이 필요합니다")
        
        return self.searcher.get_document_count()
    
    def get_available_metadata_fields(self) -> List[str]:
        """
        사용 가능한 메타데이터 필드 목록을 가져옵니다.
        
        Returns:
            메타데이터 필드 목록
        """
        if not self.searcher:
            raise ConnectionError("Qdrant 연결이 필요합니다")
        
        return self.searcher.get_available_metadata_fields()
    
    def get_collection_info(self) -> Optional[Dict[str, Any]]:
        """
        컬렉션 정보를 가져옵니다.
        
        Returns:
            컬렉션 정보 딕셔너리
        """
        return self.connection_manager.get_collection_info()
    
    def health_check(self) -> Dict[str, Any]:
        """
        Qdrant 서버 상태를 확인합니다.
        
        Returns:
            상태 정보 딕셔너리
        """
        return self.connection_manager.health_check()
    
    def transform_documents(
        self,
        documents: List[Dict[str, Any]],
        source_metadata: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        문서를 변환합니다.
        
        Args:
            documents: 변환할 문서 목록
            source_metadata: 소스별 메타데이터
            
        Returns:
            변환된 문서 목록
        """
        return self.transformer.transform_documents(documents, source_metadata)
    
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
        return self.transformer.merge_with_local_documents(
            qdrant_documents, local_documents
        )
    
    def save_documents(
        self,
        documents: List[Dict[str, Any]],
        output_path: Union[str, Path],
        indent: int = 2,
        ensure_ascii: bool = False
    ) -> bool:
        """
        문서를 JSON 파일로 저장합니다.
        
        Args:
            documents: 저장할 문서 목록
            output_path: 출력 파일 경로
            indent: JSON 들여쓰기
            ensure_ascii: ASCII 문자 보장 여부
            
        Returns:
            저장 성공 여부
        """
        return save_documents_to_json(
            documents, output_path, indent, ensure_ascii
        )
    
    def load_documents(self, input_path: Union[str, Path]) -> List[Dict[str, Any]]:
        """
        JSON 파일에서 문서를 불러옵니다.
        
        Args:
            input_path: 입력 파일 경로
            
        Returns:
            불러온 문서 목록
        """
        return load_documents_from_json(input_path)


def create_qdrant_connector(
    host: str = "localhost",
    port: int = 6333,
    api_key: Optional[str] = None,
    collection_name: str = "ws-7491d651ae044c78"
) -> QdrantConnector:
    """
    Qdrant 연동 모듈을 생성합니다.
    
    Args:
        host: Qdrant 호스트 주소
        port: Qdrant 포트
        api_key: API 키
        collection_name: 컬렉션 이름
        
    Returns:
        QdrantConnector 인스턴스
    """
    return QdrantConnector(
        host=host,
        port=port,
        api_key=api_key,
        collection_name=collection_name
    )


def create_qdrant_connector_from_env() -> QdrantConnector:
    """
    환경변수에서 설정을 읽어 Qdrant 연동 모듈을 생성합니다.
    
    Returns:
        QdrantConnector 인스턴스
    """
    config = get_environment_config()
    return QdrantConnector(
        host=config["host"],
        port=config["port"],
        api_key=config["api_key"],
        collection_name=config["collection_name"]
    )


# 모듈 로드 시 기본 로깅 설정
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


# 모듈 정보 출력
def print_module_info():
    """모듈 정보를 출력합니다."""
    print(f"Qdrant Connector Module v{__version__}")
    print(f"Author: {__author__}")
    print(f"Description: {__description__}")
    print(f"Available components:")
    print(f"  - Client: Qdrant connection management")
    print(f"  - Searcher: Document search functionality")
    print(f"  - Transformer: Data transformation utilities")
    print(f"  - Utils: Common utility functions")


if __name__ == "__main__":
    # 모듈 정보 출력
    print_module_info()
    
    # 기본 연동 모듈 생성 테스트
    print("\n=== Qdrant Connector Test ===")
    try:
        connector = create_qdrant_connector()
        
        # 연결 테스트
        if connector.connect():
            print("Qdrant 연결 성공!")
            
            # 상태 확인
            health = connector.health_check()
            print(f"상태: {health['status']}")
            
            # 문서 수 확인
            count = connector.get_document_count()
            print(f"총 문서 수: {count}")
            
            # 메타데이터 필드 확인
            fields = connector.get_available_metadata_fields()
            print(f"사용 가능한 메타데이터 필드: {fields}")
            
            connector.disconnect()
        else:
            print(f"Qdrant 연결 실패")
            
    except Exception as e:
        print(f"테스트 중 오류 발생: {e}")
    
    print("\n=== Module Ready ===")
    print("Use create_qdrant_connector() to start using Qdrant connector.")