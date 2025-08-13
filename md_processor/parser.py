#!/usr/bin/env python3
"""
MD 파일 파서 모듈
MD 파일 내용과 JSON 메타데이터를 파싱하고 전처리합니다.
"""

import json
import re
import logging
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime
import markdown
from bs4 import BeautifulSoup
import hashlib

logger = logging.getLogger(__name__)


class DocumentMetadata:
    """문서 메타데이터 클래스"""
    
    def __init__(self, component: str = None, page: str = None, **kwargs):
        self.component = component
        self.page = page
        self.source_path = kwargs.get('source_path')
        self.file_size = kwargs.get('file_size')
        self.last_modified = kwargs.get('last_modified')
        self.additional_metadata = {k: v for k, v in kwargs.items() 
                                   if k not in ['component', 'page', 'source_path', 'file_size', 'last_modified']}
    
    def to_dict(self) -> Dict[str, Any]:
        """메타데이터를 딕셔너리로 변환"""
        result = {
            "component": self.component,
            "page": self.page,
            "source_path": self.source_path,
            "file_size": self.file_size,
            "last_modified": self.last_modified,
            "additional_metadata": self.additional_metadata
        }
        return result


class ContentPreprocessor:
    """콘텐츠 전처리기 클래스"""
    
    def __init__(self):
        self.md_converter = markdown.Markdown(extensions=['codehilite', 'fenced_code', 'tables'])
        
    def preprocess_content(self, content: str) -> str:
        """
        MD 콘텐츠를 전처리합니다.
        
        Args:
            content: 원본 MD 콘텐츠
            
        Returns:
            전처리된 콘텐츠
        """
        if not content or not content.strip():
            return ""
        
        # 정규화
        content = self._normalize_content(content)
        
        # 코드 블록 처리
        content = self._process_code_blocks(content)
        
        # 링크 정리
        content = self._process_links(content)
        
        # 이미지 처리
        content = self._process_images(content)
        
        # 헤더 정리
        content = self._process_headers(content)
        
        # 특수 문자 정리
        content = self._clean_special_characters(content)
        
        return content.strip()
    
    def _normalize_content(self, content: str) -> str:
        """콘텐츠 정규화"""
        # 불필요한 공백 제거
        content = re.sub(r'\r\n', '\n', content)  # Windows 줄바꿈 통일
        content = re.sub(r'\n{3,}', '\n\n', content)  # 여러 줄바꿈 통일
        content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)  # 행 끝 공백 제거
        return content
    
    def _process_code_blocks(self, content: str) -> str:
        """코드 블록 처리"""
        # 코드 블록 언어 지정 추가
        content = re.sub(r'```([^`\n]+)\n', r'```python\n', content, flags=re.IGNORECASE)
        
        # 코드 블록 내부 특수 문자 이스케이프
        def escape_code_block(match):
            code = match.group(1)
            # 코드 블록 내부의 특수 문자는 이스케이프하지 않음
            return f"```\n{code}\n```"
        
        content = re.sub(r'```(.*?)```', escape_code_block, content, flags=re.DOTALL)
        return content
    
    def _process_links(self, content: str) -> str:
        """링크 처리"""
        # 상대 경로 링크 절대 경로로 변환 (필요 시)
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', self._process_link, content)
        return content
    
    def _process_link(self, match: re.Match) -> str:
        """개별 링크 처리"""
        text = match.group(1)
        url = match.group(2)
        
        # 외부 링크는 그대로 유지
        if url.startswith(('http://', 'https://', 'ftp://', 'mailto:')):
            return f"[{text}]({url})"
        
        # 내부 링크는 정리
        if url.endswith('.md'):
            url = url.replace('.md', '')
        
        return f"[{text}]({url})"
    
    def _process_images(self, content: str) -> str:
        """이미지 처리"""
        # 로컬 이미지 경로 정리
        def process_image(match):
            alt_text = match.group(1)
            src = match.group(2)
            
            # 로컬 이미지 경로 정리
            if not src.startswith(('http://', 'https://')):
                src = src.replace('\\', '/')
            
            return f"![{alt_text}]({src})"
        
        content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', process_image, content)
        return content
    
    def _process_headers(self, content: str) -> str:
        """헤더 처리"""
        # 헤더 ID 제거
        content = re.sub(r'^#+\s+(.+?)\s*\{#[^\}]+\}', r'# \1', content, flags=re.MULTILINE)
        
        # 헤더 레벨 정리 (최대 6레벨)
        def clean_header(match):
            level = len(match.group(1))
            text = match.group(2).strip()
            new_level = min(level, 6)
            return '#' * new_level + f' {text}'
        
        content = re.sub(r'^(#+)\s*(.+)$', clean_header, content, flags=re.MULTILINE)
        return content
    
    def _clean_special_characters(self, content: str) -> str:
        """특수 문자 정리"""
        # 제어 문자 제거
        content = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', content)
        
        # 연속된 공백 단일 공백으로 변경
        content = re.sub(r'[ \t]+', ' ', content)
        
        # 연속된 개행 정리
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        return content


class MetadataExtractor:
    """메타데이터 추출기 클래스"""
    
    def extract_from_json(self, json_path: Path) -> Optional[DocumentMetadata]:
        """
        JSON 파일에서 메타데이터를 추출합니다.
        
        Args:
            json_path: JSON 파일 경로
            
        Returns:
            DocumentMetadata 객체 또는 None
        """
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 기본 메타데이터 추출
            component = data.get('document_name') or data.get('component') or data.get('product')
            page = data.get('page_number') or data.get('page') or data.get('title')
            
            # 파일 정보 추가
            metadata_dict = {
                'source_path': str(json_path),
                'file_size': json_path.stat().st_size,
                'last_modified': datetime.fromtimestamp(json_path.stat().st_mtime).isoformat()
            }
            
            # 추가 메타데이터 병합
            metadata_dict.update({k: v for k, v in data.items() 
                                if k not in ['document_name', 'component', 'product', 'page_number', 'page', 'title']})
            
            return DocumentMetadata(component=component, page=page, **metadata_dict)
            
        except Exception as e:
            logger.error(f"Failed to extract metadata from {json_path}: {e}")
            return None
    
    def extract_from_path(self, file_path: Path) -> DocumentMetadata:
        """
        파일 경로에서 메타데이터를 추출합니다.
        
        Args:
            file_path: 파일 경로
            
        Returns:
            DocumentMetadata 객체
        """
        # 경로에서 컴포넌트와 페이지 정보 추출
        component = None
        page = None
        
        if 'output' in str(file_path):
            # 컴포넌트 단위 파일: ./output/{컴포넌트}.md
            component = file_path.stem
        elif 'md_staging' in str(file_path):
            # 페이지 단위 파일: ./md_staging/{컴포넌트}/{페이지}.md
            parts = file_path.parts
            try:
                component_idx = parts.index('md_staging') + 1
                if component_idx < len(parts):
                    component = parts[component_idx]
                
                # page_로 시작하는 파일에서 페이지 번호 추출
                if file_path.stem.startswith('page_'):
                    page = file_path.stem
            except ValueError:
                pass
        
        metadata_dict = {
            'source_path': str(file_path),
            'file_size': file_path.stat().st_size,
            'last_modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
        }
        
        return DocumentMetadata(component=component, page=page, **metadata_dict)


class MDParser:
    """MD 파일 파서 메인 클래스"""
    
    def __init__(self):
        self.preprocessor = ContentPreprocessor()
        self.metadata_extractor = MetadataExtractor()
    
    def parse_file(self, md_path: Path, json_path: Optional[Path] = None) -> Dict[str, Any]:
        """
        MD 파일을 파싱합니다.
        
        Args:
            md_path: MD 파일 경로
            json_path: JSON 메타데이터 파일 경로 (선택적)
            
        Returns:
            파싱된 문서 딕셔너리
        """
        try:
            # MD 파일 읽기
            with open(md_path, 'r', encoding='utf-8') as f:
                raw_content = f.read()
            
            # 콘텐츠 전처리
            processed_content = self.preprocessor.preprocess_content(raw_content)
            
            # 메타데이터 추출
            if json_path and json_path.exists():
                metadata = self.metadata_extractor.extract_from_json(json_path)
            else:
                metadata = self.metadata_extractor.extract_from_path(md_path)
            
            # 고유 ID 생성
            doc_id = self._generate_document_id(md_path, metadata)
            
            # 품질 점수 계산
            quality_score = self._calculate_quality_score(processed_content, metadata)
            
            # 결과 구성
            result = {
                "id": doc_id,
                "title": self._generate_title(metadata),
                "component": metadata.component,
                "page": metadata.page,
                "content": processed_content,
                "metadata": metadata.to_dict(),
                "quality_score": quality_score
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Failed to parse {md_path}: {e}")
            return {
                "id": f"error_{hashlib.md5(str(md_path).encode()).hexdigest()[:8]}",
                "title": f"Error parsing {md_path.name}",
                "component": None,
                "page": None,
                "content": "",
                "metadata": {"error": str(e)},
                "quality_score": 0.0
            }
    
    def _generate_document_id(self, file_path: Path, metadata: DocumentMetadata) -> str:
        """고유 문서 ID 생성"""
        # 파일 경로와 메타데이터를 기반으로 해시 생성
        id_string = f"{file_path}:{metadata.component}:{metadata.page}"
        return hashlib.md5(id_string.encode()).hexdigest()
    
    def _generate_title(self, metadata: DocumentMetadata) -> str:
        """문서 제목 생성"""
        if metadata.component and metadata.page:
            return f"{metadata.component}/{metadata.page}"
        elif metadata.component:
            return str(metadata.component)
        elif metadata.page:
            return str(metadata.page)
        else:
            return "Untitled Document"
    
    def _calculate_quality_score(self, content: str, metadata: DocumentMetadata) -> float:
        """품질 점수 계산 (0.0-1.0)"""
        if not content:
            return 0.0
        
        score = 0.0
        
        # 길이 점수 (0-0.3)
        content_length = len(content)
        if content_length > 1000:
            score += 0.3
        elif content_length > 500:
            score += 0.2
        elif content_length > 100:
            score += 0.1
        
        # 메타데이터 완성도 점수 (0-0.3)
        if metadata.component:
            score += 0.15
        if metadata.page:
            score += 0.15
        
        # 구조적 품질 점수 (0-0.4)
        # 헤더가 있는지
        if re.search(r'^#+\s+', content, re.MULTILINE):
            score += 0.1
        
        # 코드 블록이 있는지
        if '```' in content:
            score += 0.1
        
        # 링크가 있는지
        if '](' in content:
            score += 0.1
        
        # 리스트가 있는지
        if re.search(r'^\s*[-*+]\s+', content, re.MULTILINE):
            score += 0.1
        
        return min(score, 1.0)


def create_parser() -> MDParser:
    """
    MD 파서를 생성합니다.
    
    Returns:
        MDParser 인스턴스
    """
    return MDParser()


if __name__ == "__main__":
    # 테스트 코드
    logging.basicConfig(level=logging.INFO)
    
    parser = create_parser()
    
    # 테스트 파일 경로
    test_md_path = Path("md_staging/grid/page_020.md")
    test_json_path = Path("md_staging/grid/page_020.json")
    
    if test_md_path.exists():
        print("=== MD 파일 파싱 테스트 ===")
        result = parser.parse_file(test_md_path, test_json_path if test_json_path.exists() else None)
        
        print(f"ID: {result['id']}")
        print(f"Title: {result['title']}")
        print(f"Component: {result['component']}")
        print(f"Page: {result['page']}")
        print(f"Content length: {len(result['content'])}")
        print(f"Quality score: {result['quality_score']}")
        print(f"Metadata: {result['metadata']}")
        
        # 내용 미리보기
        if result['content']:
            print(f"\nContent preview:\n{result['content'][:200]}...")
    else:
        print("테스트 파일을 찾을 수 없습니다.")