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
        score_threshold: float = 0.7,  # 요구사항에 따라 기본값을 0.7로 변경
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
                # 벡터 기반 의미적 검색
                search_result = self.client.search(
                    collection_name=self.collection_name,
                    query_vector=query.vector,
                    limit=query.limit,
                    score_threshold=query.score_threshold,
                    query_filter=filter_condition,
                    with_payload=True,
                    with_vectors=False
                )
            elif query.search_type == "semantic" and query.text:
                # 텍스트 기반 의미적 검색 (임베딩 생성 후 검색)
                try:
                    # 실제 구현에서는 sentence-transformers를 사용하여 임베딩 생성
                    # 여기서는 간단한 텍스트 검색으로 대체
                    search_result = self._search_by_text_similarity(query)
                except Exception as e:
                    logger.warning(f"의미적 검색 실패, 키워드 검색으로 대체: {e}")
                    search_result = self._search_by_keywords(query, filter_condition)
            elif query.search_type == "metadata":
                # 메타데이터 기반 검색
                search_result = self._search_by_metadata_only(query, filter_condition)
            else:
                # 키워드 기반 검색
                search_result = self._search_by_keywords(query, filter_condition)
            
            # 결과 변환
            results = []
            for hit in search_result:
                result = SearchResult(
                    id=str(hit.id),
                    score=getattr(hit, 'score', 1.0),  # scroll 결과에는 score가 없을 수 있음
                    payload=hit.payload,
                    vector=getattr(hit, 'vector', None),
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
        limit: int = 10,
        score_threshold: float = 0.0  # 메타데이터 검색에서는 낮은 임계값 사용
    ) -> List[Dict[str, Any]]:
        """
        메타데이터 기반으로 문서를 검색합니다.
        
        Args:
            metadata_filter: 메타데이터 필터
            limit: 반환할 결과 수
            score_threshold: 점수 임계값
            
        Returns:
            검색된 문서 목록
        """
        return self.search_documents(
            query="",
            limit=limit,
            score_threshold=score_threshold,
            metadata_filter=metadata_filter,
            search_type="metadata"
        )
    
    def search_by_component(
        self,
        component_name: str,
        limit: int = 10,
        additional_filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        컴포넌트 이름으로 문서를 검색합니다.
        
        Args:
            component_name: 컴포넌트 이름
            limit: 반환할 결과 수
            additional_filters: 추가 필터
            
        Returns:
            검색된 문서 목록
        """
        metadata_filter = {"component": component_name}
        if additional_filters:
            metadata_filter.update(additional_filters)
        
        return self.search_by_metadata(metadata_filter, limit)
    
    def search_by_page_range(
        self,
        start_page: int,
        end_page: int,
        component_name: Optional[str] = None,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        페이지 범위로 문서를 검색합니다.
        
        Args:
            start_page: 시작 페이지
            end_page: 끝 페이지
            component_name: 컴포넌트 이름 (선택적)
            limit: 반환할 결과 수
            
        Returns:
            검색된 문서 목록
        """
        metadata_filter = {
            "page": {
                "gte": start_page,
                "lte": end_page
            }
        }
        
        if component_name:
            metadata_filter["component"] = component_name
        
        return self.search_by_metadata(metadata_filter, limit)
    
    def search_similar_documents(
        self,
        document_id: str,
        limit: int = 10,
        score_threshold: float = 0.7  # 요구사항에 따라 기본값을 0.7로 변경
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
        score_threshold: float = 0.7,  # 요구사항에 따라 기본값을 0.7로 변경
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
            
            # 병렬 처리를 위한 배치 검색 최적화
            try:
                batch_search_results = self._execute_batch_search(
                    batch_queries, limit, score_threshold, metadata_filter
                )
                
                for query_results in batch_search_results:
                    batch_result.results.extend(query_results)
                    batch_result.total_count += len(query_results)
                    
            except Exception as e:
                logger.error(f"배치 검색 실패: {e}")
                # 개별 검색으로 대체
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
    
    def _execute_batch_search(
        self,
        queries: List[str],
        limit: int,
        score_threshold: float,
        metadata_filter: Optional[Dict[str, Any]]
    ) -> List[List[Dict[str, Any]]]:
        """
        배치 검색을 실행합니다.
        
        Args:
            queries: 검색 쿼리 목록
            limit: 각 쿼리당 반환할 결과 수
            score_threshold: 점수 임계값
            metadata_filter: 메타데이터 필터
            
        Returns:
            각 쿼리별 검색 결과 목록
        """
        batch_results = []
        
        try:
            # 의미적 검색을 위한 벡터 생성 (가능한 경우)
            if hasattr(self, '_embedding_model') or self._try_load_embedding_model():
                query_vectors = self._embedding_model.encode(queries).tolist()
                
                # 벡터 기반 배치 검색
                for i, (query, vector) in enumerate(zip(queries, query_vectors)):
                    try:
                        search_result = self.client.search(
                            collection_name=self.collection_name,
                            query_vector=vector,
                            limit=limit,
                            score_threshold=score_threshold,
                            query_filter=self._build_filter(None, metadata_filter),
                            with_payload=True,
                            with_vectors=False
                        )
                        
                        # 결과 변환
                        results = []
                        for hit in search_result:
                            result = SearchResult(
                                id=str(hit.id),
                                score=getattr(hit, 'score', 1.0),
                                payload=hit.payload,
                                vector=getattr(hit, 'vector', None),
                                shard_id=getattr(hit, 'shard_id', None),
                                version=getattr(hit, 'version', None)
                            )
                            results.append(result)
                        
                        transformed_results = self._transform_search_results(results)
                        batch_results.append(transformed_results)
                        
                    except Exception as e:
                        logger.error(f"배치 검색 중 쿼리 '{query}' 실패: {e}")
                        batch_results.append([])
            else:
                # 키워드 기반 배치 검색
                for query in queries:
                    try:
                        results = self.search_documents(
                            query=query,
                            limit=limit,
                            score_threshold=score_threshold,
                            metadata_filter=metadata_filter,
                            search_type="keyword"
                        )
                        batch_results.append(results)
                        
                    except Exception as e:
                        logger.error(f"배치 검색 중 쿼리 '{query}' 실패: {e}")
                        batch_results.append([])
                        
        except Exception as e:
            logger.error(f"배치 검색 실행 실패: {e}")
            raise
        
        return batch_results
    
    def _try_load_embedding_model(self) -> bool:
        """
        임베딩 모델 로드를 시도합니다.
        
        Returns:
            로드 성공 여부
        """
        try:
            from sentence_transformers import SentenceTransformer
            self._embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            return True
        except ImportError:
            logger.warning("sentence-transformers가 설치되지 않음")
            return False
        except Exception as e:
            logger.error(f"임베딩 모델 로드 실패: {e}")
            return False
    
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
    
    def _search_by_text_similarity(self, query: SearchQuery) -> List:
        """
        텍스트 유사도 기반 의미적 검색을 수행합니다.
        
        Args:
            query: 검색 쿼리
            
        Returns:
            검색 결과 목록
        """
        try:
            # 실제 구현에서는 sentence-transformers를 사용하여 임베딩 생성
            # 여기서는 간단한 구현으로 대체
            from sentence_transformers import SentenceTransformer
            
            # 모델 로드 (캐시됨)
            if not hasattr(self, '_embedding_model'):
                self._embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            
            # 쿼리 텍스트를 벡터로 변환
            query_vector = self._embedding_model.encode(query.text).tolist()
            
            # 벡터 검색 수행
            search_result = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=query.limit,
                score_threshold=query.score_threshold,
                query_filter=query.filter,
                with_payload=True,
                with_vectors=False
            )
            
            return search_result
            
        except ImportError:
            logger.warning("sentence-transformers가 설치되지 않음. 키워드 검색으로 대체")
            return self._search_by_keywords(query, query.filter)
        except Exception as e:
            logger.error(f"의미적 검색 실패: {e}")
            return self._search_by_keywords(query, query.filter)
    
    def _search_by_keywords(self, query: SearchQuery, filter_condition) -> List:
        """
        키워드 기반 검색을 수행합니다.
        
        Args:
            query: 검색 쿼리
            filter_condition: 필터 조건
            
        Returns:
            검색 결과 목록
        """
        try:
            # 스크롤을 사용한 키워드 검색
            search_result, _ = self.client.scroll(
                collection_name=self.collection_name,
                limit=query.limit,
                scroll_filter=filter_condition,
                with_payload=True,
                with_vectors=False
            )
            
            # 텍스트 매칭 점수 계산 (간단한 구현)
            if query.text:
                scored_results = []
                for hit in search_result:
                    content = hit.payload.get('content', '') if hit.payload else ''
                    title = hit.payload.get('title', '') if hit.payload else ''
                    
                    # 간단한 텍스트 매칭 점수 계산
                    score = self._calculate_text_similarity(query.text, content + ' ' + title)
                    
                    if score >= query.score_threshold:
                        # score 속성 추가
                        hit.score = score
                        scored_results.append(hit)
                
                # 점수 기준으로 정렬
                scored_results.sort(key=lambda x: x.score, reverse=True)
                return scored_results[:query.limit]
            
            return search_result
            
        except Exception as e:
            logger.error(f"키워드 검색 실패: {e}")
            return []
    
    def _search_by_metadata_only(self, query: SearchQuery, filter_condition) -> List:
        """
        메타데이터만을 기반으로 검색을 수행합니다.
        
        Args:
            query: 검색 쿼리
            filter_condition: 필터 조건
            
        Returns:
            검색 결과 목록
        """
        try:
            search_result, _ = self.client.scroll(
                collection_name=self.collection_name,
                limit=query.limit,
                scroll_filter=filter_condition,
                with_payload=True,
                with_vectors=False
            )
            
            # 메타데이터 검색에서는 모든 결과에 동일한 점수 부여
            for hit in search_result:
                hit.score = 1.0
            
            return search_result
            
        except Exception as e:
            logger.error(f"메타데이터 검색 실패: {e}")
            return []
    
    def _calculate_text_similarity(self, query_text: str, content: str) -> float:
        """
        간단한 텍스트 유사도를 계산합니다.
        
        Args:
            query_text: 쿼리 텍스트
            content: 비교할 콘텐츠
            
        Returns:
            유사도 점수 (0.0-1.0)
        """
        if not query_text or not content:
            return 0.0
        
        # 간단한 키워드 매칭 기반 점수 계산
        query_words = set(query_text.lower().split())
        content_words = set(content.lower().split())
        
        if not query_words:
            return 0.0
        
        # Jaccard 유사도 계산
        intersection = len(query_words.intersection(content_words))
        union = len(query_words.union(content_words))
        
        if union == 0:
            return 0.0
        
        return intersection / union


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