#!/usr/bin/env python3
"""
Context7 MCP Connector for Syncfusion WinForms
Context7 MCP 도구를 사용하여 Syncfusion WinForms API 정보를 추출합니다.
"""

import json
import asyncio
import logging
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

@dataclass
class CodeSnippet:
    """코드 스니펫 정보"""
    title: str
    description: str
    code: str
    language: str
    source: str

class Context7Connector:
    """Context7 MCP 커넥터"""
    
    def __init__(self, library_id: str = "/yakdoli/syncfusion-v11-winform"):
        self.library_id = library_id
        self.connected = False
        
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
            
        except Exception as e:
            logger.warning(f"Context7 MCP connection failed: {e}")
            self.connected = False
    
    async def disconnect(self):
        """Context7 연결 해제"""
        self.connected = False
        logger.info("Context7 MCP disconnected")
    
    async def get_component_snippets(self, component_name: str, max_snippets: int = 100) -> List[CodeSnippet]:
        """특정 컴포넌트의 코드 스니펫 가져오기"""
        if not self.connected:
            logger.warning("Context7 not connected")
            return []
        
        try:
            from context7 import get_library_docs
            
            # 라이브러리 문서 가져오기
            docs = await get_library_docs(
                context7CompatibleLibraryID=self.library_id,
                tokens=20000  # 더 많은 토큰으로 확장
            )
            
            # 컴포넌트 관련 스니펫 필터링
            component_snippets = []
            
            if 'code_snippets' in docs:
                for snippet in docs['code_snippets']:
                    # 컴포넌트 이름이 포함된 스니펫만 필터링
                    if (component_name.lower() in snippet.get('title', '').lower() or
                        component_name.lower() in snippet.get('description', '').lower() or
                        component_name.lower() in snippet.get('code', '').lower()):
                        
                        component_snippets.append(CodeSnippet(
                            title=snippet.get('title', ''),
                            description=snippet.get('description', ''),
                            code=snippet.get('code', ''),
                            language=snippet.get('language', 'csharp'),
                            source=snippet.get('source', '')
                        ))
                        
                        if len(component_snippets) >= max_snippets:
                            break
            
            logger.info(f"Found {len(component_snippets)} snippets for {component_name}")
            return component_snippets
            
        except Exception as e:
            logger.error(f"Error getting component snippets: {e}")
            return []
    
    async def get_all_snippets(self, max_snippets: int = 1000) -> List[CodeSnippet]:
        """모든 코드 스니펫 가져오기"""
        if not self.connected:
            logger.warning("Context7 not connected")
            return []
        
        try:
            from context7 import get_library_docs
            
            # 라이브러리 문서 가져오기
            docs = await get_library_docs(
                context7CompatibleLibraryID=self.library_id,
                tokens=50000  # 모든 스니펫을 가져오기 위한 큰 토큰 수
            )
            
            all_snippets = []
            
            if 'code_snippets' in docs:
                for snippet in docs['code_snippets']:
                    all_snippets.append(CodeSnippet(
                        title=snippet.get('title', ''),
                        description=snippet.get('description', ''),
                        code=snippet.get('code', ''),
                        language=snippet.get('language', 'csharp'),
                        source=snippet.get('source', '')
                    ))
                    
                    if len(all_snippets) >= max_snippets:
                        break
            
            logger.info(f"Found {len(all_snippets)} total snippets")
            return all_snippets
            
        except Exception as e:
            logger.error(f"Error getting all snippets: {e}")
            return []
    
    async def search_snippets(self, query: str, max_snippets: int = 50) -> List[CodeSnippet]:
        """쿼리로 코드 스니펫 검색"""
        if not self.connected:
            logger.warning("Context7 not connected")
            return []
        
        try:
            from context7 import get_library_docs
            
            # 라이브러리 문서 가져오기
            docs = await get_library_docs(
                context7CompatibleLibraryID=self.library_id,
                tokens=30000
            )
            
            matching_snippets = []
            
            if 'code_snippets' in docs:
                for snippet in docs['code_snippets']:
                    # 쿼리가 제목, 설명, 코드에 포함되어 있는지 확인
                    if (query.lower() in snippet.get('title', '').lower() or
                        query.lower() in snippet.get('description', '').lower() or
                        query.lower() in snippet.get('code', '').lower()):
                        
                        matching_snippets.append(CodeSnippet(
                            title=snippet.get('title', ''),
                            description=snippet.get('description', ''),
                            code=snippet.get('code', ''),
                            language=snippet.get('language', 'csharp'),
                            source=snippet.get('source', '')
                        ))
                        
                        if len(matching_snippets) >= max_snippets:
                            break
            
            logger.info(f"Found {len(matching_snippets)} snippets matching query: {query}")
            return matching_snippets
            
        except Exception as e:
            logger.error(f"Error searching snippets: {e}")
            return []

# Mock 구현 (Context7 MCP가 없을 경우)
class MockContext7Connector:
    """Mock Context7 커넥터 (테스트용)"""
    
    def __init__(self, library_id: str = "/yakdoli/syncfusion-v11-winform"):
        self.library_id = library_id
        self.connected = False
        
    async def connect(self):
        """Mock 연결"""
        self.connected = True
        logger.info("Mock Context7 MCP connected")
        
    async def disconnect(self):
        """Mock 연결 해제"""
        self.connected = False
        logger.info("Mock Context7 MCP disconnected")
    
    async def get_component_snippets(self, component_name: str, max_snippets: int = 100) -> List[CodeSnippet]:
        """Mock 컴포넌트 스니펫"""
        if not self.connected:
            return []
        
        # Mock 데이터 생성
        mock_snippets = [
            CodeSnippet(
                title=f"{component_name} Control Example",
                description=f"Example of using {component_name} control",
                code=f"// {component_name} initialization code\nvar {component_name.lower()} = new {component_name}();",
                language="csharp",
                source="mock://example.com"
            ),
            CodeSnippet(
                title=f"{component_name} Configuration",
                description=f"Configuration example for {component_name}",
                code=f"// {component_name} configuration\n{component_name.lower()}.Property = value;",
                language="csharp",
                source="mock://example.com"
            )
        ]
        
        return mock_snippets[:max_snippets]
    
    async def get_all_snippets(self, max_snippets: int = 1000) -> List[CodeSnippet]:
        """Mock 모든 스니펫"""
        return []
    
    async def search_snippets(self, query: str, max_snippets: int = 50) -> List[CodeSnippet]:
        """Mock 검색"""
        return []

# 커넥터 선택
def get_context7_connector(use_mock: bool = False) -> Context7Connector:
    """Context7 커넥터 가져오기"""
    if use_mock:
        return MockContext7Connector()
    else:
        return Context7Connector()