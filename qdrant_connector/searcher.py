#!/usr/bin/env python3
"""
Qdrant 문서 검색기 모듈
Qdrant 벡터 데이터베이스에서 문서를 검색합니다.
"""

import logging
from typing import List, Dict, Any, Optional, Union, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from qdrant_client import QdrantClient, models
from qdrant_client.http import models as http_models
from qdrant_client.http.exceptions import UnexpectedResponse

from .client import QdrantConnectionManager, QdrantClientConfig

logger = logging.getLogger(__name__)


@dataclass
class SearchQuery:
    """검색 쿼리 데이터 클래스"""
    text: str
    limit: int = 10
    score_threshold: float = 0.5
    filter: Optional[Dict[str, Any]] = None
    vector: Optional[List[float]] = None
    search_type: str = "semantic"  # "semantic", "keyword", "hybrid"
    metadata_filter: Optional[Dict[str, Any]] = None


@dataclass
class SearchResult:
    """검색 결과 데이터 클래스"""
    id: str
    score: float
    payload: Optional[Dict[str, Any]] = None
    vector: Optional[List[float]] = None
    shard_id: Optional[int] = None
    version: Optional[int] = None


@dataclass
class BatchSearchResult:
    """배치 검색 결과 데이터 클래스"""
    results: List[SearchResult]
    query: str
    total_count: int
    execution_time: float
    has_more: bool = False


class QdrantDocumentSearcher:
    """Qdrant 문서 검색기 클래스"""
    
    def __init__(self, connection_manager: QdrantConnectionManager):
        """
        Qdrant 문서 검색기를 초기화합니다.
        
        Args:
            connection_manager: Qdrant 연결 관리자
        """
        self.connection_manager = connection_manager
        self.client = connection_manager.get_client()
        self.collection_name = connection_manager.config.collection_name
    
    def search_documents(
        self,
        query: str,
        limit: int = 10,
        score_threshold: float = 0.5,
        metadata_filter: Optional[Dict[str, Any]] = None,
        search_type: str = "semantic",
        vector: Optional[List[float]] = None,
        batch_size: int = 100
    ) -> List[Dict[str, Any]]:
        """
        문서를 검색합니다.
        
        Args:
            query: 검색 쿼리 텍스트
            limit: 반환할 결과 수
            score_threshold: 점수 임계값
            metadata_filter: 메타데이터 필터
            search_type: 검색 유형 ("semantic", "keyword", "hybrid")
            vector: 직접 제공된 벡터 (선택적)
            batch_size: 배치 크기
            
        Returns:
            검색된 문서 목록
        """
        if not self.connection_manager.ensure_connection():
            raise ConnectionError("Qdrant 연결 실패")
        
        try:
            # 검색 쿼리 생성
            search_query = SearchQuery(
                text=query,
                limit=limit,
                score_threshold=score_threshold,
                filter=metadata_filter,
                vector=vector,
                search_type=search_type,
                metadata_filter=metadata_filter
            )
            
            # 검색 수행
            results = self._execute_search(search_query)
            
            # 결과 변환
            return self._transform_search_results(results)
            
        except Exception as e:
            logger.error(f"문서 검색 실패: {e}")
            raise
    
    def _execute_search(self, query: SearchQuery) -> List[SearchResult]:
        """
        실제 검색을 수행합니다.
        
        Args:
            query: 검색 쿼리
            
        Returns:
            검색 결과 목록
        """
        start_time = datetime.now()
        
        try:
            # 필터 생성
            filter_condition = self._build_filter(query.filter, query.metadata_filter)
            
            # 검색 방식에 따라 다른 쿼리 생성
            if query.search_type == "semantic" and query.vector:
                # 벡터 기반 검색
                search_request = models.SearchRequest(
                    vector=query.vector,
                    limit=query.limit,
                    score_threshold=query.score_threshold,
                    filter=filter_condition,
                    with_payload=True,
                    with_vector=False
                )
            elif query.search_type == "keyword":
                # 키워드 기반 검색
                search_request = models.SearchRequest(
                    query=models.Query(
                        must=[
                            models.FieldCondition(
                                key="content",
                                match=models.MatchText(
                                    text=query.text
                                )
                            )
                        ]
                    ),
                    limit=query.limit,
                    filter=filter_condition,
                    with_payload=True,
                    with_vector=False
                )
            else:
                # 하이브리드 검색 (기본적으로 시맨틱 검색)
                search_request = models.SearchRequest(
                    query=models.Query(
                        must=[
                            models.FieldCondition(
                                key="content",
                                match=models.MatchText(
                                    text=query.text
                                )
                            )
                        ]
                    ),
                    limit=query.limit,
                    score_threshold=query.score_threshold,
                    filter=filter_condition,
                    with_payload=True,
                    with_vector=False
                )
            
            # 검색 실행
            search_result = self.client.search(
                collection_name=self.collection_name,
                search_request=search_request
            )
            
            # 결과 변환
            results = []
            for hit in search_result:
                result = SearchResult(
                    id=str(hit.id),
                    score=hit.score,
                    payload=hit.payload,
                    vector=hit.vector if hasattr(hit, 'vector') else None,
                    shard_id=getattr(hit, 'shard_id', None),
                    version=getattr(hit, 'version', None)
                )
                results.append(result)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            logger.info(f"검색 완료: {len(results)}개 결과, 실행 시간: {execution_time:.2f}초")
            
            return results
            
        except Exception as e:
            logger.error(f"검색 실행 실패: {e}")
            raise
    
    def _build_filter(
        self,
        filter_dict: Optional[Dict[str, Any]],
        metadata_filter: Optional[Dict[str, Any]]
    ) -> Optional[models.Filter]:
        """
        필터 조건을 Qdrant Filter 형식으로 변환합니다.
        
        Args:
            filter_dict: 필터 딕셔너리
            metadata_filter: 메타데이터 필터
            
        Returns:
            Qdrant Filter 객체
        """
        if not filter_dict and not metadata_filter:
            return None
        
        # 필터 병합
        combined_filter = {}
        if filter_dict:
            combined_filter.update(filter_dict)
        if metadata_filter:
            combined_filter.update(metadata_filter)
        
        # Qdrant Filter 형식으로 변환
        must_conditions = []
        
        for key, value in combined_filter.items():
            if isinstance(value, str):
                # 문자열 매칭
                must_conditions.append(
                    models.FieldCondition(
                        key=key,
                        match=models.MatchText(text=value)
                    )
                )
            elif isinstance(value, list):
                # 리스트 매칭
                must_conditions.append(
                    models.FieldCondition(
                        key=key,
                        match=models.MatchAny(any=value)
                    )
                )
            elif isinstance(value, (int, float)):
                # 숫자 범위
                must_conditions.append(
                    models.FieldCondition(
                        key=key,
                        range=models.Range(
                            gte=value if isinstance(value, (int, float)) else None
                        )
                    )
                )
            elif isinstance(value, dict):
                # 복잡한 조건
                if "gte" in value or "lte" in value:
                    range_params = {}
                    if "gte" in value:
                        range_params["gte"] = value["gte"]
                    if "lte" in value:
                        range_params["lte"] = value["lte"]
                    
                    must_conditions.append(
                        models.FieldCondition(
                            key=key,
                            range=models.Range(**range_params)
                        )
                    )
                elif "match" in value:
                    must_conditions.append(
                        models.FieldCondition(
                            key=key,
                            match=models.MatchText(text=value["match"])
                        )
                    )
        
        if must_conditions:
            return models.Filter(must=must_conditions)
        return None
    
    def _transform_search_results(self, results: List[SearchResult]) -> List[Dict[str, Any]]:
        """
        검색 결과를 표준 형식으로 변환합니다.
        
        Args:
            results: 원본 검색 결과
            
        Returns:
            변환된 검색 결과
        """
        transformed_results = []
        
        for result in results:
            # 페이로드에서 기본 정보 추출
            payload = result.payload or {}
            
            # 문서 구조 생성
            document = {
                "id": result.id,
                "title": payload.get("title", f"Document {result.id}"),
                "component": payload.get("component", "unknown"),
                "page": payload.get("page", "unknown"),
                "content": payload.get("content", ""),
                "metadata": {
                    "source": "qdrant",
                    "collection": self.collection_name,
                    "vector_score": result.score,
                    "original_payload": payload,
                    "shard_id": result.shard_id,
                    "version": result.version
                },
                "quality_score": min(result.score, 1.0)  # 품질 점수로 변환
            }
            
            # 추가 메타데이터 병합
            if "metadata" in payload:
                document["metadata"].update(payload["metadata"])
            
            transformed_results.append(document)
        
        return transformed_results
    
    def search_by_metadata(
        self,
        metadata_filter: Dict[str, Any],
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        메타데이터 기반으로 문서를 검색합니다.
        
        Args:
            metadata_filter: 메타데이터 필터
            limit: 반환할 결과 수
            
        Returns:
            검색된 문서 목록
        """
        return self.search_documents(
            query="",
            limit=limit,
            metadata_filter=metadata_filter,
            search_type="keyword"
        )
    
    def search_similar_documents(
        self,
        document_id: str,
        limit: int = 10,
        score_threshold: float = 0.5
    ) -> List[Dict[str, Any]]:
        """
        특정 문서와 유사한 문서를 검색합니다.
        
        Args:
            document_id: 기준 문서 ID
            limit: 반환할 결과 수
            score_threshold: 점수 임계값
            
        Returns:
            유사 문서 목록
        """
        if not self.connection_manager.ensure_connection():
            raise ConnectionError("Qdrant 연결 실패")
        
        try:
            # 특정 문서의 벡터 정보 가져오기
            vector_info = self.client.retrieve(
                collection_name=self.collection_name,
                ids=[document_id],
                with_vector=True
            )
            
            if not vector_info:
                raise ValueError(f"문서 {document_id}를 찾을 수 없습니다")
            
            # 벡터 정보 추출
            vector = vector_info[0].vector if hasattr(vector_info[0], 'vector') else None
            
            if not vector:
                raise ValueError(f"문서 {document_id}에 벡터 정보가 없습니다")
            
            # 유사 문서 검색
            return self.search_documents(
                query="",
                limit=limit,
                score_threshold=score_threshold,
                vector=vector,
                search_type="semantic"
            )
            
        except Exception as e:
            logger.error(f"유사 문서 검색 실패: {e}")
            raise
    
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
        batch_results = []
        
        for i in range(0, len(queries), batch_size):
            batch_queries = queries[i:i + batch_size]
            batch_start_time = datetime.now()
            
            batch_result = BatchSearchResult(
                results=[],
                query=", ".join(batch_queries),
                total_count=0,
                execution_time=0.0
            )
            
            for query in batch_queries:
                try:
                    results = self.search_documents(
                        query=query,
                        limit=limit,
                        score_threshold=score_threshold,
                        metadata_filter=metadata_filter
                    )
                    batch_result.results.extend(results)
                    batch_result.total_count += len(results)
                    
                except Exception as e:
                    logger.error(f"쿼리 '{query}' 검색 실패: {e}")
                    continue
            
            batch_result.execution_time = (datetime.now() - batch_start_time).total_seconds()
            batch_results.append(batch_result)
        
        return batch_results
    
    def get_document_count(self) -> int:
        """
        컬렉션의 문서 수를 가져옵니다.
        
        Returns:
            문서 수
        """
        if not self.connection_manager.ensure_connection():
            raise ConnectionError("Qdrant 연결 실패")
        
        try:
            collection_info = self.connection_manager.get_collection_info()
            return collection_info["vectors_count"] if collection_info else 0
        except Exception as e:
            logger.error(f"문서 수 조회 실패: {e}")
            return 0
    
    def get_available_metadata_fields(self) -> List[str]:
        """
        사용 가능한 메타데이터 필드 목록을 가져옵니다.
        
        Returns:
            메타데이터 필드 목록
        """
        if not self.connection_manager.ensure_connection():
            raise ConnectionError("Qdrant 연결 실패")
        
        try:
            # 샘플 문서에서 메타데이터 필드 추출
            sample_results = self.search_documents(
                query="",
                limit=1,
                score_threshold=0.0
            )
            
            if not sample_results:
                return []
            
            # 첫 번째 결과에서 메타데이터 필드 추출
            metadata_fields = set()
            for doc in sample_results:
                if doc.get("metadata"):
                    metadata_fields.update(doc["metadata"].keys())
            
            return list(metadata_fields)
            
        except Exception as e:
            logger.error(f"메타데이터 필드 조회 실패: {e}")
            return []


if __name__ == "__main__":
    # 테스트 코드
    logging.basicConfig(level=logging.INFO)
    
    # 클라이언트 생성
    from .client import create_qdrant_client
    client_manager = create_qdrant_client()
    
    # 검색기 생성
    searcher = QdrantDocumentSearcher(client_manager)
    
    # 연결 테스트
    if client_manager.connect():
        print("Qdrant 연결 성공!")
        
        # 문서 수 확인
        count = searcher.get_document_count()
        print(f"총 문서 수: {count}")
        
        # 메타데이터 필드 확인
        fields = searcher.get_available_metadata_fields()
        print(f"사용 가능한 메타데이터 필드: {fields}")
        
        # 문서 검색 테스트
        if count > 0:
            results = searcher.search_documents("syncfusion", limit=5)
            print(f"검색 결과: {len(results)}개 문서")
            
            for doc in results[:2]:
                print(f"- {doc['title']} (점수: {doc['quality_score']:.2f})")
        
        client_manager.disconnect()
    else:
        print(f"Qdrant 연결 실패: {client_manager.connection_error}")