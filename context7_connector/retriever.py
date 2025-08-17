#!/usr/bin/env python3
"""
Document Retriever
로컬 MD 문서셋에서 관련 정보를 추출합니다.
"""

import asyncio
import logging
import re
from typing import List, Dict, Any, Optional
from pathlib import Path
from dataclasses import dataclass
from .client import Context7Document

logger = logging.getLogger(__name__)

@dataclass
class LocalDocument:
    """로컬 문서 정보"""
    title: str
    content: str
    source: str
    metadata: Dict[str, Any]
    relevance_score: float = 0.0

class DocumentRetriever:
    """로컬 문서 검색기"""
    
    def __init__(self, md_staging_path: str = "md_staging"):
        self.md_staging_path = Path(md_staging_path)
        self.documents_cache: Dict[str, LocalDocument] = {}
        self.documents_indexed = False
        
    async def initialize(self):
        """문서 인덱싱"""
        if not self.md_staging_path.exists():
            logger.warning(f"MD staging path does not exist: {self.md_staging_path}")
            return
        
        await self._index_documents()
        self.documents_indexed = True
        logger.info(f"Indexed {len(self.documents_cache)} documents from {self.md_staging_path}")
    
    async def _index_documents(self):
        """MD 문서 인덱싱"""
        self.documents_cache.clear()
        
        # 모든 MD 파일 찾기
        md_files = list(self.md_staging_path.rglob("*.md"))
        
        for md_file in md_files:
            try:
                # 파일 읽기
                content = await self._read_md_file(md_file)
                
                # 메타데이터 추출
                metadata = await self._extract_metadata(md_file, content)
                
                # 제목 추출
                title = await self._extract_title(md_file, content)
                
                # 문서 객체 생성
                document = LocalDocument(
                    title=title,
                    content=content,
                    source=str(md_file),
                    metadata=metadata
                )
                
                # 캐시에 저장
                self.documents_cache[str(md_file)] = document
                
            except Exception as e:
                logger.error(f"Error indexing document {md_file}: {e}")
    
    async def _read_md_file(self, file_path: Path) -> str:
        """MD 파일 읽기"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
            return ""
    
    async def _extract_metadata(self, file_path: Path, content: str) -> Dict[str, Any]:
        """메타데이터 추출"""
        metadata = {
            'file_path': str(file_path),
            'file_size': len(content),
            'directory': file_path.parent.name,
            'language': 'markdown',
            'tags': [],
            'category': 'general'
        }
        
        # 디렉토리 이름을 카테고리로 사용
        if file_path.parent.name in ['common', 'calculate', 'chart', 'diagram', 'edit', 'grid', 'schedule', 'tools']:
            metadata['category'] = file_path.parent.name
        
        # JSON 파일이 같은 디렉토리에 있는지 확인
        json_file = file_path.with_suffix('.json')
        if json_file.exists():
            try:
                import json
                with open(json_file, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                    metadata.update(json_data)
            except Exception as e:
                logger.error(f"Error reading JSON metadata {json_file}: {e}")
        
        return metadata
    
    async def _extract_title(self, file_path: Path, content: str) -> str:
        """제목 추출"""
        # 첫 번째 H1 헤더 찾기
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip()
        
        # 파일 이름을 제목으로 사용
        return file_path.stem
    
    async def search_documents(self, query: str, max_results: int = 10) -> List[LocalDocument]:
        """로컬 문서 검색"""
        if not self.documents_indexed:
            await self.initialize()
        
        if not self.documents_cache:
            logger.warning("No documents indexed")
            return []
        
        matching_documents = []
        query_lower = query.lower()
        
        for document in self.documents_cache.values():
            # 관련성 점수 계산
            relevance_score = self._calculate_relevance(query_lower, document)
            
            if relevance_score > 0:
                document.relevance_score = relevance_score
                matching_documents.append(document)
        
        # 관련성 점수로 정렬
        matching_documents.sort(key=lambda x: x.relevance_score, reverse=True)
        
        # 최대 결과 수 제한
        return matching_documents[:max_results]
    
    def _calculate_relevance(self, query: str, document: LocalDocument) -> float:
        """관련성 점수 계산"""
        score = 0.0
        content_lower = document.content.lower()
        title_lower = document.title.lower()
        
        # 제목에 매칭되면 높은 점수
        if query in title_lower:
            score += 0.5
        
        # 내용에 매칭되면 중간 점수
        if query in content_lower:
            score += 0.3
        
        # 메타데이터에 매칭되면 낮은 점수
        metadata_text = ' '.join(str(v).lower() for v in document.metadata.values())
        if query in metadata_text:
            score += 0.2
        
        # 단어별 점수 계산
        query_words = query.split()
        for word in query_words:
            if word in title_lower:
                score += 0.1
            if word in content_lower:
                score += 0.05
        
        return min(score, 1.0)  # 최대 점수는 1.0
    
    async def get_category_documents(self, category: str, max_results: int = 20) -> List[LocalDocument]:
        """특정 카테고리의 문서 가져오기"""
        if not self.documents_indexed:
            await self.initialize()
        
        category_documents = []
        
        for document in self.documents_cache.values():
            if document.metadata.get('category') == category:
                category_documents.append(document)
        
        # 관련성 점수로 정렬
        category_documents.sort(key=lambda x: x.relevance_score, reverse=True)
        
        return category_documents[:max_results]
    
    async def get_directory_documents(self, directory: str, max_results: int = 20) -> List[LocalDocument]:
        """특정 디렉토리의 문서 가져오기"""
        if not self.documents_indexed:
            await self.initialize()
        
        directory_documents = []
        
        for document in self.documents_cache.values():
            if document.metadata.get('directory') == directory:
                directory_documents.append(document)
        
        return directory_documents[:max_results]
    
    async def get_similar_documents(self, document: LocalDocument, max_results: int = 5) -> List[LocalDocument]:
        """유사 문서 찾기"""
        if not self.documents_indexed:
            await self.initialize()
        
        similar_documents = []
        document_text = document.content.lower()
        
        for other_document in self.documents_cache.values():
            if other_document.source == document.source:
                continue
            
            # 간단한 유사도 계산
            other_text = other_document.content.lower()
            common_words = set(document_text.split()) & set(other_text.split())
            similarity = len(common_words) / max(len(document_text.split()), len(other_text.split()))
            
            if similarity > 0.1:  # 유사도 임계값
                other_document.relevance_score = similarity
                similar_documents.append(other_document)
        
        # 유사도로 정렬
        similar_documents.sort(key=lambda x: x.relevance_score, reverse=True)
        
        return similar_documents[:max_results]
    
    def get_document_by_path(self, path: str) -> Optional[LocalDocument]:
        """경로로 문서 가져오기"""
        return self.documents_cache.get(path)
    
    def get_all_categories(self) -> List[str]:
        """모든 카테고리 목록 가져오기"""
        if not self.documents_indexed:
            asyncio.create_task(self.initialize())
        
        categories = set()
        for document in self.documents_cache.values():
            category = document.metadata.get('category', 'general')
            categories.add(category)
        
        return sorted(list(categories))
    
    def get_all_directories(self) -> List[str]:
        """모든 디렉토리 목록 가져오기"""
        if not self.documents_indexed:
            asyncio.create_task(self.initialize())
        
        directories = set()
        for document in self.documents_cache.values():
            directory = document.metadata.get('directory', 'unknown')
            directories.add(directory)
        
        return sorted(list(directories))