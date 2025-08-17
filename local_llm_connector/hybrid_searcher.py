#!/usr/bin/env python3
"""
하이브리드 검색기 모듈

Context7, 로컬 검색, Qdrant 벡터 검색을 결합한 하이브리드 검색을 제공합니다.
로컬 LLM과의 통합을 최적화합니다.
"""

import logging
import asyncio
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime
import json

logger = logging.getLogger(__name__)


@dataclass
class HybridSearchConfig:
    """하이브리드 검색 설정"""
    # 검색 옵션
    max_results: int = 10
    timeout: int = 30
    
    # 가중치 설정
    weights: Dict[str, float] = field(default_factory=lambda: {
        "context7": 0.3,
        "local": 0.3,
        "qdrant": 0.4
    })
    
    # 검색 옵션
    enable_context7: bool = True
    enable_local_search: bool = True
    enable_qdrant_search: bool = True
    
    # 결과 처리
    enable_reranking: bool = True
    enable_deduplication: bool = True
    similarity_threshold: float = 0.7
    
    # 캐싱
    enable_caching: bool = True
    cache_ttl: int = 300  # 5분
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_results <= 0:
            raise ValueError("max_results는 양의 정수여야 합니다")
        if self.timeout <= 0:
            raise ValueError("timeout은 양의 정수여야 합니다")
        if not all(0.0 <= weight <= 1.0 for weight in self.weights.values()):
            raise ValueError("모든 가중치는 0.0과 1.0 사이여야 합니다")
        
        # 가중치 합이 1이 되도록 정규화
        total_weight = sum(self.weights.values())
        if total_weight > 0:
            self.weights = {k: v / total_weight for k, v in self.weights.items()}


class HybridSearcher:
    """하이브리드 검색기"""
    
    def __init__(self, config: HybridSearchConfig = None):
        """
        초기화
        
        Args:
            config: 하이브리드 검색 설정
        """
        self.config = config or HybridSearchConfig()
        
        # 검색 엔진 초기화 (실제 구현에서는 각 엔진을 초기화)
        self.context7_searcher = None
        self.local_searcher = None
        self.qdrant_searcher = None
        
        # 캐시
        self.search_cache = {}
        self.cache_timestamps = {}
        
        # 통계 정보
        self.stats = {
            "total_searches": 0,
            "successful_searches": 0,
            "failed_searches": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "average_response_time": 0.0,
            "start_time": None
        }
    
    async def initialize(self):
        """검색기 초기화"""
        logger.info("하이브리드 검색기 초기화 중...")
        
        try:
            # Context7 검색기 초기화
            if self.config.enable_context7:
                self.context7_searcher = await self._initialize_context7_searcher()
            
            # 로컬 검색기 초기화
            if self.config.enable_local_search:
                self.local_searcher = await self._initialize_local_searcher()
            
            # Qdrant 검색기 초기화
            if self.config.enable_qdrant_search:
                self.qdrant_searcher = await self._initialize_qdrant_searcher()
            
            logger.info("하이브리드 검색기 초기화 완료")
            
        except Exception as e:
            logger.error(f"하이브리드 검색기 초기화 실패: {str(e)}")
            raise
    
    async def search(
        self,
        query: str,
        limit: Optional[int] = None,
        weights: Optional[Dict[str, float]] = None,
        filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        하이브리드 검색 수행
        
        Args:
            query: 검색 쿼리
            limit: 결과 제한 수
            weights: 검색 가중치
            filters: 필터 조건
            
        Returns:
            검색 결과
        """
        if not self.stats["start_time"]:
            self.stats["start_time"] = datetime.now()
        
        start_time = datetime.now()
        self.stats["total_searches"] += 1
        
        try:
            # 캐시 확인
            if self.config.enable_caching:
                cache_key = self._generate_cache_key(query, limit, weights, filters)
                cached_result = self._get_from_cache(cache_key)
                
                if cached_result:
                    self.stats["cache_hits"] += 1
                    response_time = (datetime.now() - start_time).total_seconds()
                    self._update_average_response_time(response_time)
                    return cached_result
            
            # 검색 수행
            search_results = await self._perform_hybrid_search(
                query, limit or self.config.max_results, weights or self.config.weights, filters
            )
            
            # 결과 후처리
            processed_results = await self._post_process_results(search_results)
            
            # 캐시 저장
            if self.config.enable_caching:
                self._save_to_cache(cache_key, processed_results)
            
            # 통계 업데이트
            self.stats["successful_searches"] += 1
            response_time = (datetime.now() - start_time).total_seconds()
            self._update_average_response_time(response_time)
            
            return processed_results
            
        except Exception as e:
            self.stats["failed_searches"] += 1
            logger.error(f"하이브리드 검색 실패: {str(e)}")
            return {
                "status": "error",
                "message": str(e),
                "results": [],
                "weights": weights or self.config.weights
            }
    
    async def _perform_hybrid_search(
        self,
        query: str,
        limit: int,
        weights: Dict[str, float],
        filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        실제 하이브리드 검색 수행
        
        Args:
            query: 검색 쿼리
            limit: 결과 제한 수
            weights: 가중치
            filters: 필터 조건
            
        Returns:
            검색 결과
        """
        search_tasks = []
        
        # Context7 검색
        if self.config.enable_context7 and self.context7_searcher:
            context7_task = self._search_context7(query, limit, filters)
            search_tasks.append(("context7", context7_task))
        
        # 로컬 검색
        if self.config.enable_local_search and self.local_searcher:
            local_task = self._search_local(query, limit, filters)
            search_tasks.append(("local", local_task))
        
        # Qdrant 검색
        if self.config.enable_qdrant_search and self.qdrant_searcher:
            qdrant_task = self._search_qdrant(query, limit, filters)
            search_tasks.append(("qdrant", qdrant_task))
        
        # 병렬 검색 수행
        results = {}
        for source_name, task in search_tasks:
            try:
                result = await task
                results[source_name] = result
            except Exception as e:
                logger.error(f"{source_name} 검색 실패: {str(e)}")
                results[source_name] = {"results": [], "error": str(e)}
        
        # 결과 결합
        combined_results = self._combine_results(results, weights, limit)
        
        return combined_results
    
    async def _search_context7(
        self,
        query: str,
        limit: int,
        filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Context7 검색 수행"""
        try:
            # Context7 검색 로직 (실제 구현에서는 Context7 MCP를 사용)
            # 여기서는 모의 구현
            mock_results = [
                {
                    "title": f"Context7 Result {i}",
                    "content": f"Context7 검색 결과 {i}: {query}",
                    "score": 0.9 - (i * 0.1),
                    "source": "context7",
                    "metadata": {"doc_id": f"context7_doc_{i}"}
                }
                for i in range(min(limit, 5))
            ]
            
            return {
                "results": mock_results,
                "total": len(mock_results),
                "source": "context7"
            }
            
        except Exception as e:
            logger.error(f"Context7 검색 실패: {str(e)}")
            raise
    
    async def _search_local(
        self,
        query: str,
        limit: int,
        filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """로컬 검색 수행"""
        try:
            # 로컬 검색 로직 (실제 구현에서는 로컬 문서 검색)
            # 여기서는 모의 구현
            mock_results = [
                {
                    "title": f"Local Result {i}",
                    "content": f"로컬 검색 결과 {i}: {query}",
                    "score": 0.8 - (i * 0.1),
                    "source": "local",
                    "metadata": {"doc_id": f"local_doc_{i}"}
                }
                for i in range(min(limit, 3))
            ]
            
            return {
                "results": mock_results,
                "total": len(mock_results),
                "source": "local"
            }
            
        except Exception as e:
            logger.error(f"로컬 검색 실패: {str(e)}")
            raise
    
    async def _search_qdrant(
        self,
        query: str,
        limit: int,
        filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Qdrant 검색 수행"""
        try:
            # Qdrant 검색 로직 (실제 구현에서는 Qdrant 벡터 검색)
            # 여기서는 모의 구현
            mock_results = [
                {
                    "title": f"Qdrant Result {i}",
                    "content": f"Qdrant 벡터 검색 결과 {i}: {query}",
                    "score": 0.85 - (i * 0.1),
                    "source": "qdrant",
                    "metadata": {"doc_id": f"qdrant_doc_{i}"}
                }
                for i in range(min(limit, 4))
            ]
            
            return {
                "results": mock_results,
                "total": len(mock_results),
                "source": "qdrant"
            }
            
        except Exception as e:
            logger.error(f"Qdrant 검색 실패: {str(e)}")
            raise
    
    def _combine_results(
        self,
        results: Dict[str, Dict[str, Any]],
        weights: Dict[str, float],
        limit: int
    ) -> Dict[str, Any]:
        """
        검색 결과 결합
        
        Args:
            results: 검색 결과 딕셔너리
            weights: 가중치
            limit: 결과 제한 수
            
        Returns:
            결합된 검색 결과
        """
        try:
            all_results = []
            
            # 모든 결과를 하나의 리스트로 결합
            for source_name, source_results in results.items():
                if source_results.get("results"):
                    for result in source_results["results"]:
                        # 가중치 적용
                        weight = weights.get(source_name, 0.0)
                        result["weighted_score"] = result.get("score", 0.0) * weight
                        result["source"] = source_name
                        all_results.append(result)
            
            # 점수 기준 정렬
            all_results.sort(key=lambda x: x.get("weighted_score", 0.0), reverse=True)
            
            # 상위 결과 선택
            top_results = all_results[:limit]
            
            # 재랭킹 (선택적)
            if self.config.enable_reranking:
                top_results = self._rerank_results(top_results)
            
            # 중복 제거 (선택적)
            if self.config.enable_deduplication:
                top_results = self._deduplicate_results(top_results)
            
            return {
                "results": top_results,
                "total": len(top_results),
                "sources": list(results.keys()),
                "weights": weights
            }
            
        except Exception as e:
            logger.error(f"결과 결합 실패: {str(e)}")
            return {"results": [], "total": 0, "sources": [], "weights": weights}
    
    def _rerank_results(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """결과 재랭킹"""
        # 간단한 재랭킹 로직 (실제 구현에서는 더 복잡한 알고리즘 사용)
        return sorted(results, key=lambda x: x.get("weighted_score", 0.0), reverse=True)
    
    def _deduplicate_results(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """결과 중복 제거"""
        try:
            unique_results = []
            seen_titles = set()
            
            for result in results:
                title = result.get("title", "")
                if title not in seen_titles:
                    unique_results.append(result)
                    seen_titles.add(title)
                elif result.get("weighted_score", 0.0) > 0.8:  # 높은 점수 결과는 유지
                    unique_results.append(result)
            
            return unique_results
            
        except Exception as e:
            logger.error(f"중복 제거 실패: {str(e)}")
            return results
    
    async def _post_process_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """결과 후처리"""
        try:
            # 결과 포맷팅
            processed_results = {
                "results": results.get("results", []),
                "total": results.get("total", 0),
                "sources": results.get("sources", []),
                "weights": results.get("weights", {}),
                "timestamp": datetime.now().isoformat(),
                "status": "success"
            }
            
            # 유사도 임계값 적용
            if self.config.similarity_threshold > 0:
                filtered_results = [
                    result for result in processed_results["results"]
                    if result.get("weighted_score", 0.0) >= self.config.similarity_threshold
                ]
                processed_results["results"] = filtered_results
                processed_results["total"] = len(filtered_results)
            
            return processed_results
            
        except Exception as e:
            logger.error(f"결과 후처리 실패: {str(e)}")
            return {
                "results": [],
                "total": 0,
                "sources": [],
                "weights": {},
                "timestamp": datetime.now().isoformat(),
                "status": "error",
                "message": str(e)
            }
    
    def _generate_cache_key(
        self,
        query: str,
        limit: Optional[int],
        weights: Optional[Dict[str, float]],
        filters: Optional[Dict[str, Any]]
    ) -> str:
        """캐시 키 생성"""
        import hashlib
        
        key_data = {
            "query": query,
            "limit": limit,
            "weights": weights or self.config.weights,
            "filters": filters or {}
        }
        
        key_string = json.dumps(key_data, sort_keys=True)
        return hashlib.md5(key_string.encode()).hexdigest()
    
    def _get_from_cache(self, cache_key: str) -> Optional[Dict[str, Any]]:
        """캐시에서 결과 가져오기"""
        try:
            if cache_key in self.search_cache:
                # 캐시 만료 확인
                timestamp = self.cache_timestamps.get(cache_key, 0)
                if (datetime.now().timestamp() - timestamp) < self.config.cache_ttl:
                    self.stats["cache_hits"] += 1
                    return self.search_cache[cache_key]
                else:
                    # 만료된 캐시 삭제
                    del self.search_cache[cache_key]
                    del self.cache_timestamps[cache_key]
            
            self.stats["cache_misses"] += 1
            return None
            
        except Exception as e:
            logger.error(f"캐시 조회 실패: {str(e)}")
            return None
    
    def _save_to_cache(self, cache_key: str, result: Dict[str, Any]):
        """캐시에 결과 저장"""
        try:
            self.search_cache[cache_key] = result
            self.cache_timestamps[cache_key] = datetime.now().timestamp()
            
            # 캐시 크기 제한 (선택적)
            if len(self.search_cache) > 100:
                # 가장 오래된 캐시 삭제
                oldest_key = min(self.cache_timestamps.keys(), key=lambda k: self.cache_timestamps[k])
                del self.search_cache[oldest_key]
                del self.cache_timestamps[oldest_key]
                
        except Exception as e:
            logger.error(f"캐시 저장 실패: {str(e)}")
    
    def _update_average_response_time(self, response_time: float):
        """평균 응답 시간 업데이트"""
        if self.stats["total_searches"] > 0:
            current_avg = self.stats["average_response_time"]
            self.stats["average_response_time"] = (
                (current_avg * (self.stats["total_searches"] - 1) + response_time) 
                / self.stats["total_searches"]
            )
    
    async def _initialize_context7_searcher(self):
        """Context7 검색기 초기화"""
        # 실제 구현에서는 Context7 MCP를 초기화
        return True
    
    async def _initialize_local_searcher(self):
        """로컬 검색기 초기화"""
        # 실제 구현에서는 로컬 문서 검색기를 초기화
        return True
    
    async def _initialize_qdrant_searcher(self):
        """Qdrant 검색기 초기화"""
        # 실제 구현에서는 Qdrant 클라이언트를 초기화
        return True
    
    def get_stats(self) -> Dict[str, Any]:
        """통계 정보 반환"""
        if self.stats["start_time"]:
            elapsed_time = (datetime.now() - self.stats["start_time"]).total_seconds()
        else:
            elapsed_time = 0
        
        cache_hit_rate = (
            self.stats["cache_hits"] / (self.stats["cache_hits"] + self.stats["cache_misses"]) * 100
            if (self.stats["cache_hits"] + self.stats["cache_misses"]) > 0 else 0
        )
        
        success_rate = (
            self.stats["successful_searches"] / self.stats["total_searches"] * 100
            if self.stats["total_searches"] > 0 else 0
        )
        
        return {
            **self.stats,
            "elapsed_time": elapsed_time,
            "cache_hit_rate": cache_hit_rate,
            "success_rate": success_rate,
            "config": {
                "max_results": self.config.max_results,
                "timeout": self.config.timeout,
                "weights": self.config.weights,
                "enable_context7": self.config.enable_context7,
                "enable_local_search": self.config.enable_local_search,
                "enable_qdrant_search": self.config.enable_qdrant_search,
                "enable_caching": self.config.enable_caching
            }
        }


def create_hybrid_searcher(config: HybridSearchConfig = None) -> HybridSearcher:
    """
    하이브리드 검색기 생성
    
    Args:
        config: 하이브리드 검색 설정
        
    Returns:
        HybridSearcher 인스턴스
    """
    config = config or HybridSearchConfig()
    searcher = HybridSearcher(config)
    
    # 비동기 초기화
    asyncio.create_task(searcher.initialize())
    
    return searcher