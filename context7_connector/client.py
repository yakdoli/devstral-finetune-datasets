#!/usr/bin/env python3
"""
Context7 MCP Client
Context7 MCP 도구를 사용하여 로컬 MD 문서셋에서 관련 정보를 추출합니다.
"""

import json
import asyncio
import logging
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

@dataclass
class Context7Document:
    """Context7 문서 정보"""
    title: str
    content: str
    source: str
    metadata: Dict[str, Any]
    relevance_score: float = 0.0

class Context7Client:
    """Context7 MCP 클라이언트"""
    
    def __init__(self, library_id: str = "/yakdoli/syncfusion-v11-winform", 
                 endpoint: str = None, timeout: int = 30):
        self.library_id = library_id
        self.endpoint = endpoint
        self.timeout = timeout
        self.connected = False
        self.mock_mode = False
        
    async def connect(self):
        """Context7에 연결"""
        try:
            # Context7 라이브러리 정보 확인
            from context7 import resolve_library_id, get_library_docs
            
            # 라이브러리 ID 확인
            result = await resolve_library_id("syncfusion v11 winform")
            if result:
                self.library_id = result
                logger.info(f"Using Context7 library: {self.library_id}")
            
            self.connected = True
            logger.info("Context7 MCP connected successfully")
            
        except ImportError:
            logger.warning("Context7 MCP not available, using mock mode")
            self.mock_mode = True
            self.connected = True
        except Exception as e:
            logger.warning(f"Context7 MCP connection failed: {e}")
            self.connected = False
    
    async def disconnect(self):
        """Context7 연결 해제"""
        self.connected = False
        logger.info("Context7 MCP disconnected")
    
    async def search_documents(self, query: str, max_results: int = 10) -> List[Context7Document]:
        """Context7에서 문서 검색"""
        if not self.connected:
            logger.warning("Context7 not connected")
            return []
        
        if self.mock_mode:
            return await self._mock_search_documents(query, max_results)
        
        try:
            from context7 import get_library_docs
            
            # 라이브러리 문서 가져오기
            docs = await get_library_docs(
                context7CompatibleLibraryID=self.library_id,
                tokens=30000,
                topic=query
            )
            
            matching_documents = []
            
            if 'code_snippets' in docs:
                for snippet in docs['code_snippets']:
                    # 쿼리가 제목, 설명, 코드에 포함되어 있는지 확인
                    if (query.lower() in snippet.get('title', '').lower() or
                        query.lower() in snippet.get('description', '').lower() or
                        query.lower() in snippet.get('code', '').lower()):
                        
                        # 관련성 점수 계산
                        relevance_score = self._calculate_relevance(query, snippet)
                        
                        matching_documents.append(Context7Document(
                            title=snippet.get('title', ''),
                            content=snippet.get('description', '') + '\n' + snippet.get('code', ''),
                            source=snippet.get('source', ''),
                            metadata={
                                'language': snippet.get('language', 'csharp'),
                                'tags': snippet.get('tags', []),
                                'category': snippet.get('category', 'general')
                            },
                            relevance_score=relevance_score
                        ))
                        
                        if len(matching_documents) >= max_results:
                            break
            
            # 관련성 점수로 정렬
            matching_documents.sort(key=lambda x: x.relevance_score, reverse=True)
            
            logger.info(f"Found {len(matching_documents)} documents matching query: {query}")
            return matching_documents
            
        except Exception as e:
            logger.error(f"Error searching documents: {e}")
            return []
    
    async def get_component_documents(self, component_name: str, max_results: int = 20) -> List[Context7Document]:
        """특정 컴포넌트의 문서 가져오기"""
        if not self.connected:
            logger.warning("Context7 not connected")
            return []
        
        if self.mock_mode:
            return await self._mock_get_component_documents(component_name, max_results)
        
        try:
            from context7 import get_library_docs
            
            # 라이브러리 문서 가져오기
            docs = await get_library_docs(
                context7CompatibleLibraryID=self.library_id,
                tokens=50000
            )
            
            component_documents = []
            
            if 'code_snippets' in docs:
                for snippet in docs['code_snippets']:
                    # 컴포넌트 이름이 포함된 스니펫만 필터링
                    if (component_name.lower() in snippet.get('title', '').lower() or
                        component_name.lower() in snippet.get('description', '').lower() or
                        component_name.lower() in snippet.get('code', '').lower()):
                        
                        # 관련성 점수 계산
                        relevance_score = self._calculate_relevance(component_name, snippet)
                        
                        component_documents.append(Context7Document(
                            title=snippet.get('title', ''),
                            content=snippet.get('description', '') + '\n' + snippet.get('code', ''),
                            source=snippet.get('source', ''),
                            metadata={
                                'language': snippet.get('language', 'csharp'),
                                'tags': snippet.get('tags', []),
                                'category': snippet.get('category', 'general')
                            },
                            relevance_score=relevance_score
                        ))
                        
                        if len(component_documents) >= max_results:
                            break
            
            # 관련성 점수로 정렬
            component_documents.sort(key=lambda x: x.relevance_score, reverse=True)
            
            logger.info(f"Found {len(component_documents)} documents for component: {component_name}")
            return component_documents
            
        except Exception as e:
            logger.error(f"Error getting component documents: {e}")
            return []
    
    def _calculate_relevance(self, query: str, snippet: Dict[str, Any]) -> float:
        """관련성 점수 계산"""
        query_lower = query.lower()
        title = snippet.get('title', '').lower()
        description = snippet.get('description', '').lower()
        code = snippet.get('code', '').lower()
        
        score = 0.0
        
        # 제목에 매칭되면 높은 점수
        if query_lower in title:
            score += 0.5
        
        # 설명에 매칭되면 중간 점수
        if query_lower in description:
            score += 0.3
        
        # 코드에 매칭되면 낮은 점수
        if query_lower in code:
            score += 0.2
        
        return score
    
    async def _mock_search_documents(self, query: str, max_results: int) -> List[Context7Document]:
        """Mock 문서 검색"""
        mock_documents = [
            Context7Document(
                title=f"{query} Example",
                content=f"Example of using {query} in Syncfusion WinForms",
                source="mock://example.com",
                metadata={
                    'language': 'csharp',
                    'tags': ['example', 'syncfusion'],
                    'category': 'general'
                },
                relevance_score=0.8
            ),
            Context7Document(
                title=f"{query} Configuration",
                content=f"Configuration example for {query} control",
                source="mock://example.com",
                metadata={
                    'language': 'csharp',
                    'tags': ['configuration', 'syncfusion'],
                    'category': 'general'
                },
                relevance_score=0.6
            )
        ]
        
        return mock_documents[:max_results]
    
    async def _mock_get_component_documents(self, component_name: str, max_results: int) -> List[Context7Document]:
        """Mock 컴포넌트 문서"""
        mock_documents = [
            Context7Document(
                title=f"{component_name} Control Example",
                content=f"Example of using {component_name} control in WinForms",
                source="mock://example.com",
                metadata={
                    'language': 'csharp',
                    'tags': ['control', 'winforms', 'syncfusion'],
                    'category': 'control'
                },
                relevance_score=0.9
            ),
            Context7Document(
                title=f"{component_name} Properties",
                content=f"Properties and methods for {component_name} control",
                source="mock://example.com",
                metadata={
                    'language': 'csharp',
                    'tags': ['properties', 'methods', 'syncfusion'],
                    'category': 'reference'
                },
                relevance_score=0.7
            )
        ]
        
        return mock_documents[:max_results]