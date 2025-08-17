#!/usr/bin/env python3
"""
Hybrid Searcher
Qdrant 검색과 Context7 검색을 결합한 하이브리드 검색 기능을 제공합니다.
"""

import asyncio
import logging
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from .client import Context7Client, Context7Document
from .retriever import DocumentRetriever, LocalDocument

logger = logging.getLogger(__name__)

@dataclass
class SearchResult:
    """검색 결과"""
    title: str
    content: str
    source: str
    metadata: Dict[str, Any]
    relevance_score: float
    search_type: str  # 'qdrant', 'context7', 'local'
    hybrid_score: float = 0.0

class HybridSearcher:
    """하이브리드 검색기"""
    
    def __init__(self, 
                 context7_client: Context7Client = None,
                 document_retriever: DocumentRetriever = None,
                 qdrant_searcher = None,
                 context7_weight: float = 0.3,
                 local_weight: float = 0.3,
                 qdrant_weight: float = 0.4):
        self.context7_client = context7_client or Context7Client()
        self.document_retriever = document_retriever or DocumentRetriever()
        self.qdrant_searcher = qdrant_searcher
        self.context7_weight = context7_weight
        self.local_weight = local_weight
        self.qdrant_weight = qdrant_weight
        
        # 가중치 합이 1이 되도록 정규화
        total_weight = context7_weight + local_weight + qdrant_weight
        if total_weight > 0:
            self.context7_weight /= total_weight
            self.local_weight /= total_weight
            self.qdrant_weight /= total_weight
    
    async def initialize(self):
        """초기화"""
        await self.context7_client.connect()
        await self.document_retriever.initialize()
        
        if self.qdrant_searcher:
            await self.qdrant_searcher.initialize()
    
    async def search(self, query: str, max_results: int = 10) -> List[SearchResult]:
        """하이브리드 검색 수행"""
        if not self.context7_client.connected and not self.document_retriever.documents_indexed:
            logger.warning("Neither Context7 nor local documents are available")
            return []
        
        # 병렬로 검색 수행
        context7_results = []
        local_results = []
        qdrant_results = []
        
        tasks = []
        
        # Context7 검색
        if self.context7_client.connected:
            tasks.append(self._search_context7(query))
        
        # 로컬 문서 검색
        if self.document_retriever.documents_indexed:
            tasks.append(self._search_local(query))
        
        # Qdrant 검색
        if self.qdrant_searcher:
            tasks.append(self._search_qdrant(query))
        
        # 모든 검색 작업 병렬 실행
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    logger.error(f"Search task {i} failed: {result}")
                    continue
                
                if i == 0 and self.context7_client.connected:
                    context7_results = result
                elif i == 1 and self.document_retriever.documents_indexed:
                    local_results = result
                elif i == 2 and self.qdrant_searcher:
                    qdrant_results = result
        
        # 결과 통합
        hybrid_results = await self._combine_results(
            context7_results, local_results, qdrant_results, max_results
        )
        
        logger.info(f"Hybrid search completed: {len(hybrid_results)} results for query: {query}")
        return hybrid_results
    
    async def _search_context7(self, query: str) -> List[Context7Document]:
        """Context7 검색"""
        try:
            return await self.context7_client.search_documents(query, max_results=20)
        except Exception as e:
            logger.error(f"Context7 search failed: {e}")
            return []
    
    async def _search_local(self, query: str) -> List[LocalDocument]:
        """로컬 문서 검색"""
        try:
            return await self.document_retriever.search_documents(query, max_results=20)
        except Exception as e:
            logger.error(f"Local document search failed: {e}")
            return []
    
    async def _search_qdrant(self, query: str) -> List[Any]:
        """Qdrant 검색"""
        try:
            if hasattr(self.qdrant_searcher, 'search'):
                return await self.qdrant_searcher.search(query, max_results=20)
            else:
                return []
        except Exception as e:
            logger.error(f"Qdrant search failed: {e}")
            return []
    
    async def _combine_results(self, 
                              context7_results: List[Context7Document],
                              local_results: List[LocalDocument],
                              qdrant_results: List[Any],
                              max_results: int) -> List[SearchResult]:
        """검색 결과 통합"""
        combined_results = []
        
        # Context7 결과 변환
        for doc in context7_results:
            combined_results.append(SearchResult(
                title=doc.title,
                content=doc.content,
                source=doc.source,
                metadata=doc.metadata,
                relevance_score=doc.relevance_score,
                search_type='context7',
                hybrid_score=doc.relevance_score * self.context7_weight
            ))
        
        # 로컬 문서 결과 변환
        for doc in local_results:
            combined_results.append(SearchResult(
                title=doc.title,
                content=doc.content,
                source=doc.source,
                metadata=doc.metadata,
                relevance_score=doc.relevance_score,
                search_type='local',
                hybrid_score=doc.relevance_score * self.local_weight
            ))
        
        # Qdrant 결과 변환
        for doc in qdrant_results:
            if hasattr(doc, 'score'):
                score = doc.score
            else:
                score = 0.5  # 기본 점수
            
            combined_results.append(SearchResult(
                title=getattr(doc, 'title', str(doc)),
                content=getattr(doc, 'content', str(doc)),
                source=getattr(doc, 'source', 'qdrant'),
                metadata=getattr(doc, 'metadata', {}),
                relevance_score=score,
                search_type='qdrant',
                hybrid_score=score * self.qdrant_weight
            ))
        
        # 하이브리드 점수로 정렬
        combined_results.sort(key=lambda x: x.hybrid_score, reverse=True)
        
        # 최대 결과 수 제한
        return combined_results[:max_results]
    
    async def search_by_category(self, category: str, query: str = "", max_results: int = 10) -> List[SearchResult]:
        """카테고리별 검색"""
        # 로컬 문서에서 카테고리별 검색
        local_results = await self.document_retriever.get_category_documents(category, max_results=20)
        
        # 쿼리가 있으면 필터링
        if query:
            query_lower = query.lower()
            local_results = [
                doc for doc in local_results
                if query_lower in doc.title.lower() or query_lower in doc.content.lower()
            ]
        
        # 결과 변환
        results = []
        for doc in local_results:
            results.append(SearchResult(
                title=doc.title,
                content=doc.content,
                source=doc.source,
                metadata=doc.metadata,
                relevance_score=doc.relevance_score,
                search_type='local',
                hybrid_score=doc.relevance_score * self.local_weight
            ))
        
        # 하이브리드 점수로 정렬
        results.sort(key=lambda x: x.hybrid_score, reverse=True)
        
        return results[:max_results]
    
    async def get_similar_documents(self, document: SearchResult, max_results: int = 5) -> List[SearchResult]:
        """유사 문서 검색"""
        similar_results = []
        
        # 로컬 문서에서 유사 문서 찾기
        if document.search_type == 'local':
            local_doc = self.document_retriever.get_document_by_path(document.source)
            if local_doc:
                similar_local_docs = await self.document_retriever.get_similar_documents(local_doc, max_results)
                for doc in similar_local_docs:
                    similar_results.append(SearchResult(
                        title=doc.title,
                        content=doc.content,
                        source=doc.source,
                        metadata=doc.metadata,
                        relevance_score=doc.relevance_score,
                        search_type='local',
                        hybrid_score=doc.relevance_score * self.local_weight
                    ))
        
        # Context7에서 유사 문서 찾기
        if document.search_type == 'context7':
            similar_context7_docs = await self.context7_client.search_documents(document.title, max_results)
            for doc in similar_context7_docs:
                similar_results.append(SearchResult(
                    title=doc.title,
                    content=doc.content,
                    source=doc.source,
                    metadata=doc.metadata,
                    relevance_score=doc.relevance_score,
                    search_type='context7',
                    hybrid_score=doc.relevance_score * self.context7_weight
                ))
        
        # 하이브리드 점수로 정렬
        similar_results.sort(key=lambda x: x.hybrid_score, reverse=True)
        
        return similar_results[:max_results]
    
    def get_search_statistics(self) -> Dict[str, Any]:
        """검색 통계 정보"""
        stats = {
            'context7_connected': self.context7_client.connected,
            'context7_mock_mode': self.context7_client.mock_mode,
            'local_documents_indexed': len(self.document_retriever.documents_cache),
            'qdrant_available': self.qdrant_searcher is not None,
            'weights': {
                'context7': self.context7_weight,
                'local': self.local_weight,
                'qdrant': self.qdrant_weight
            }
        }
        
        # 로컬 문서 통계
        if self.document_retriever.documents_indexed:
            categories = self.document_retriever.get_all_categories()
            directories = self.document_retriever.get_all_directories()
            
            stats['local_documents_stats'] = {
                'categories': categories,
                'directories': directories,
                'total_categories': len(categories),
                'total_directories': len(directories)
            }
        
        return stats
    
    def update_weights(self, context7_weight: float = None, local_weight: float = None, qdrant_weight: float = None):
        """검색 가중치 업데이트"""
        if context7_weight is not None:
            self.context7_weight = context7_weight
        if local_weight is not None:
            self.local_weight = local_weight
        if qdrant_weight is not None:
            self.qdrant_weight = qdrant_weight
        
        # 가중치 합이 1이 되도록 정규화
        total_weight = self.context7_weight + self.local_weight + self.qdrant_weight
        if total_weight > 0:
            self.context7_weight /= total_weight
            self.local_weight /= total_weight
            self.qdrant_weight /= total_weight
        
        logger.info(f"Updated search weights: context7={self.context7_weight:.2f}, local={self.local_weight:.2f}, qdrant={self.qdrant_weight:.2f}")