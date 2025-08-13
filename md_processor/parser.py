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
        pass
        
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
        
        # YAML 프론트매터 제거
        content = self._remove_frontmatter(content)
        
        # 코드 블록 처리 (보존)
        content, code_blocks = self._preserve_code_blocks(content)
        
        # 링크 정리
        content = self._process_links(content)
        
        # 이미지 처리
        content = self._process_images(content)
        
        # 헤더 정리
        content = self._process_headers(content)
        
        # 테이블 정리
        content = self._process_tables(content)
        
        # 리스트 정리
        content = self._process_lists(content)
        
        # 특수 문자 정리
        content = self._clean_special_characters(content)
        
        # 코드 블록 복원
        content = self._restore_code_blocks(content, code_blocks)
        
        # 최종 정리
        content = self._final_cleanup(content)
        
        return content.strip()
    
    def _remove_frontmatter(self, content: str) -> str:
        """YAML 프론트매터 제거"""
        # YAML 프론트매터 패턴: ---로 시작하고 끝남
        frontmatter_pattern = r'^---\s*\n.*?\n---\s*\n?'
        content = re.sub(frontmatter_pattern, '', content, flags=re.DOTALL | re.MULTILINE)
        return content
    
    def _preserve_code_blocks(self, content: str) -> Tuple[str, Dict[str, str]]:
        """코드 블록을 임시로 보존"""
        code_blocks = {}
        counter = 0
        
        def replace_code_block(match):
            nonlocal counter
            placeholder = f"__CODE_BLOCK_{counter}__"
            code_blocks[placeholder] = match.group(0)
            counter += 1
            return placeholder
        
        # ``` 코드 블록 보존
        content = re.sub(r'```.*?```', replace_code_block, content, flags=re.DOTALL)
        
        # 인라인 코드 보존
        def replace_inline_code(match):
            nonlocal counter
            placeholder = f"__INLINE_CODE_{counter}__"
            code_blocks[placeholder] = match.group(0)
            counter += 1
            return placeholder
        
        content = re.sub(r'`[^`\n]+`', replace_inline_code, content)
        
        return content, code_blocks
    
    def _restore_code_blocks(self, content: str, code_blocks: Dict[str, str]) -> str:
        """보존된 코드 블록 복원"""
        for placeholder, original in code_blocks.items():
            content = content.replace(placeholder, original)
        return content
    
    def _process_tables(self, content: str) -> str:
        """테이블 처리"""
        # 테이블 정렬 정리
        lines = content.split('\n')
        processed_lines = []
        
        for line in lines:
            if '|' in line and line.strip().startswith('|') and line.strip().endswith('|'):
                # 테이블 행 정리
                cells = [cell.strip() for cell in line.split('|')[1:-1]]
                processed_line = '| ' + ' | '.join(cells) + ' |'
                processed_lines.append(processed_line)
            else:
                processed_lines.append(line)
        
        return '\n'.join(processed_lines)
    
    def _process_lists(self, content: str) -> str:
        """리스트 처리"""
        lines = content.split('\n')
        processed_lines = []
        
        for line in lines:
            # 순서 없는 리스트 정리
            if re.match(r'^\s*[-*+]\s+', line):
                # 들여쓰기 정규화
                indent_match = re.match(r'^(\s*)', line)
                indent = indent_match.group(1) if indent_match else ''
                content_part = re.sub(r'^\s*[-*+]\s+', '', line)
                processed_line = f"{indent}- {content_part}"
                processed_lines.append(processed_line)
            # 순서 있는 리스트 정리
            elif re.match(r'^\s*\d+\.\s+', line):
                indent_match = re.match(r'^(\s*)', line)
                indent = indent_match.group(1) if indent_match else ''
                number_match = re.match(r'^\s*(\d+)\.\s+', line)
                number = number_match.group(1) if number_match else '1'
                content_part = re.sub(r'^\s*\d+\.\s+', '', line)
                processed_line = f"{indent}{number}. {content_part}"
                processed_lines.append(processed_line)
            else:
                processed_lines.append(line)
        
        return '\n'.join(processed_lines)
    
    def _final_cleanup(self, content: str) -> str:
        """최종 정리"""
        # 연속된 빈 줄을 최대 2개로 제한
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        # 줄 끝 공백 제거
        lines = [line.rstrip() for line in content.split('\n')]
        content = '\n'.join(lines)
        
        # 문서 시작과 끝의 불필요한 공백 제거
        content = content.strip()
        
        return content
    
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


class APISignatureExtractor:
    """API 시그니처 추출기 클래스"""
    
    def __init__(self):
        # C# API 패턴들
        self.csharp_patterns = [
            # 메서드 패턴: public/private/protected ReturnType MethodName(parameters)
            r'(?:public|private|protected|internal)?\s*(?:static\s+)?(?:virtual\s+)?(?:override\s+)?(\w+(?:<[^>]+>)?)\s+(\w+)\s*\([^)]*\)',
            # 프로퍼티 패턴: public Type PropertyName { get; set; }
            r'(?:public|private|protected|internal)?\s*(\w+(?:<[^>]+>)?)\s+(\w+)\s*\{\s*(?:get;?\s*)?(?:set;?\s*)?\}',
            # 이벤트 패턴: public event EventHandler EventName
            r'(?:public|private|protected|internal)?\s*event\s+(\w+(?:<[^>]+>)?)\s+(\w+)',
            # 클래스/인터페이스 패턴: public class/interface ClassName
            r'(?:public|private|protected|internal)?\s*(?:abstract\s+)?(?:sealed\s+)?(class|interface|struct|enum)\s+(\w+(?:<[^>]+>)?)',
        ]
        
        # JavaScript/TypeScript API 패턴들
        self.js_patterns = [
            # 함수 패턴: function functionName(parameters)
            r'function\s+(\w+)\s*\([^)]*\)',
            # 메서드 패턴: methodName(parameters) { 또는 methodName: function(parameters)
            r'(\w+)\s*[:=]\s*function\s*\([^)]*\)|(\w+)\s*\([^)]*\)\s*\{',
            # 클래스 패턴: class ClassName
            r'class\s+(\w+)',
            # 변수/상수 패턴: var/let/const variableName
            r'(?:var|let|const)\s+(\w+)',
        ]
    
    def extract_api_signatures(self, content: str) -> List[Dict[str, Any]]:
        """
        콘텐츠에서 API 시그니처를 추출합니다.
        
        Args:
            content: 분석할 콘텐츠
            
        Returns:
            API 시그니처 목록
        """
        signatures = []
        
        # 코드 블록에서 API 추출
        code_blocks = self._extract_code_blocks(content)
        for code_block in code_blocks:
            language = code_block.get('language', '').lower()
            code = code_block.get('code', '')
            
            if language in ['csharp', 'c#', 'cs']:
                signatures.extend(self._extract_csharp_apis(code))
            elif language in ['javascript', 'js', 'typescript', 'ts']:
                signatures.extend(self._extract_js_apis(code))
            else:
                # 언어가 명시되지 않은 경우 휴리스틱으로 판단
                signatures.extend(self._extract_generic_apis(code))
        
        # 인라인 코드에서도 API 추출
        inline_codes = self._extract_inline_codes(content)
        for inline_code in inline_codes:
            signatures.extend(self._extract_generic_apis(inline_code))
        
        # 중복 제거 및 정리
        unique_signatures = self._deduplicate_signatures(signatures)
        
        return unique_signatures
    
    def _extract_code_blocks(self, content: str) -> List[Dict[str, str]]:
        """코드 블록 추출"""
        code_blocks = []
        
        # ``` 코드 블록 패턴
        pattern = r'```(\w*)\n(.*?)\n```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for language, code in matches:
            code_blocks.append({
                'language': language.strip(),
                'code': code.strip()
            })
        
        return code_blocks
    
    def _extract_inline_codes(self, content: str) -> List[str]:
        """인라인 코드 추출"""
        # `code` 패턴
        pattern = r'`([^`]+)`'
        matches = re.findall(pattern, content)
        return [match.strip() for match in matches if len(match.strip()) > 3]
    
    def _extract_csharp_apis(self, code: str) -> List[Dict[str, Any]]:
        """C# API 추출"""
        apis = []
        
        for pattern in self.csharp_patterns:
            matches = re.finditer(pattern, code, re.MULTILINE | re.IGNORECASE)
            for match in matches:
                groups = match.groups()
                if len(groups) >= 2:
                    api_type = self._determine_csharp_api_type(match.group(0))
                    apis.append({
                        'signature': match.group(0).strip(),
                        'type': api_type,
                        'language': 'csharp',
                        'return_type': groups[0] if groups[0] else None,
                        'name': groups[1] if len(groups) > 1 and groups[1] else None
                    })
        
        return apis
    
    def _extract_js_apis(self, code: str) -> List[Dict[str, Any]]:
        """JavaScript/TypeScript API 추출"""
        apis = []
        
        for pattern in self.js_patterns:
            matches = re.finditer(pattern, code, re.MULTILINE | re.IGNORECASE)
            for match in matches:
                groups = match.groups()
                name = next((g for g in groups if g), None)
                if name:
                    api_type = self._determine_js_api_type(match.group(0))
                    apis.append({
                        'signature': match.group(0).strip(),
                        'type': api_type,
                        'language': 'javascript',
                        'name': name
                    })
        
        return apis
    
    def _extract_generic_apis(self, code: str) -> List[Dict[str, Any]]:
        """일반적인 API 패턴 추출"""
        apis = []
        
        # 함수 호출 패턴: functionName(parameters)
        function_pattern = r'(\w+)\s*\([^)]*\)'
        matches = re.finditer(function_pattern, code)
        
        for match in matches:
            function_name = match.group(1)
            # 일반적인 키워드는 제외
            if function_name.lower() not in ['if', 'for', 'while', 'switch', 'return', 'new', 'var', 'let', 'const']:
                apis.append({
                    'signature': match.group(0).strip(),
                    'type': 'function_call',
                    'language': 'generic',
                    'name': function_name
                })
        
        return apis
    
    def _determine_csharp_api_type(self, signature: str) -> str:
        """C# API 타입 결정"""
        signature_lower = signature.lower()
        
        if 'class ' in signature_lower:
            return 'class'
        elif 'interface ' in signature_lower:
            return 'interface'
        elif 'struct ' in signature_lower:
            return 'struct'
        elif 'enum ' in signature_lower:
            return 'enum'
        elif 'event ' in signature_lower:
            return 'event'
        elif '{ get' in signature_lower or '{ set' in signature_lower:
            return 'property'
        else:
            return 'method'
    
    def _determine_js_api_type(self, signature: str) -> str:
        """JavaScript API 타입 결정"""
        signature_lower = signature.lower()
        
        if 'class ' in signature_lower:
            return 'class'
        elif 'function ' in signature_lower:
            return 'function'
        elif 'var ' in signature_lower or 'let ' in signature_lower or 'const ' in signature_lower:
            return 'variable'
        else:
            return 'method'
    
    def _deduplicate_signatures(self, signatures: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """시그니처 중복 제거"""
        seen = set()
        unique_signatures = []
        
        for sig in signatures:
            # 시그니처와 이름을 기준으로 중복 확인
            key = (sig.get('signature', ''), sig.get('name', ''))
            if key not in seen:
                seen.add(key)
                unique_signatures.append(sig)
        
        return unique_signatures


class MetadataExtractor:
    """메타데이터 추출기 클래스"""
    
    def __init__(self):
        self.api_extractor = APISignatureExtractor()
    
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
    
    def extract_api_signatures_from_content(self, content: str) -> List[Dict[str, Any]]:
        """
        콘텐츠에서 API 시그니처를 추출합니다.
        
        Args:
            content: 분석할 콘텐츠
            
        Returns:
            API 시그니처 목록
        """
        return self.api_extractor.extract_api_signatures(content)


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
            
            # API 시그니처 추출
            api_signatures = self.metadata_extractor.extract_api_signatures_from_content(raw_content)
            
            # 고유 ID 생성
            doc_id = self._generate_document_id(md_path, metadata)
            
            # 품질 점수 계산
            quality_score = self._calculate_quality_score(processed_content, metadata, api_signatures)
            
            # 콘텐츠 구조 분석
            content_structure = self._analyze_content_structure(processed_content)
            
            # 결과 구성
            result = {
                "id": doc_id,
                "title": self._generate_title(metadata),
                "component": metadata.component,
                "page": metadata.page,
                "content": processed_content,
                "raw_content": raw_content,
                "api_signatures": api_signatures,
                "content_structure": content_structure,
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
                "raw_content": "",
                "api_signatures": [],
                "content_structure": {},
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
    
    def _calculate_quality_score(self, content: str, metadata: DocumentMetadata, api_signatures: List[Dict[str, Any]] = None) -> float:
        """품질 점수 계산 (0.0-1.0)"""
        if not content:
            return 0.0
        
        score = 0.0
        api_signatures = api_signatures or []
        
        # 길이 점수 (0-0.25)
        content_length = len(content)
        if content_length > 2000:
            score += 0.25
        elif content_length > 1000:
            score += 0.2
        elif content_length > 500:
            score += 0.15
        elif content_length > 100:
            score += 0.1
        
        # 메타데이터 완성도 점수 (0-0.2)
        if metadata.component:
            score += 0.1
        if metadata.page:
            score += 0.1
        
        # 구조적 품질 점수 (0-0.35)
        # 헤더가 있는지
        if re.search(r'^#+\s+', content, re.MULTILINE):
            score += 0.1
        
        # 코드 블록이 있는지
        if '```' in content:
            score += 0.1
        
        # 링크가 있는지
        if '](' in content:
            score += 0.05
        
        # 리스트가 있는지
        if re.search(r'^\s*[-*+]\s+', content, re.MULTILINE):
            score += 0.05
        
        # 테이블이 있는지
        if '|' in content and re.search(r'\|.*\|', content):
            score += 0.05
        
        # API 시그니처 점수 (0-0.2)
        if api_signatures:
            api_count = len(api_signatures)
            if api_count >= 5:
                score += 0.2
            elif api_count >= 3:
                score += 0.15
            elif api_count >= 1:
                score += 0.1
        
        return min(score, 1.0)
    
    def _analyze_content_structure(self, content: str) -> Dict[str, Any]:
        """콘텐츠 구조 분석"""
        structure = {
            "word_count": len(content.split()),
            "character_count": len(content),
            "line_count": len(content.split('\n')),
            "paragraph_count": len([p for p in content.split('\n\n') if p.strip()]),
            "header_count": len(re.findall(r'^#+\s+', content, re.MULTILINE)),
            "code_block_count": content.count('```') // 2,
            "inline_code_count": len(re.findall(r'`[^`]+`', content)),
            "link_count": len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)),
            "image_count": len(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)),
            "list_item_count": len(re.findall(r'^\s*[-*+]\s+', content, re.MULTILINE)) + 
                              len(re.findall(r'^\s*\d+\.\s+', content, re.MULTILINE)),
            "table_count": len(re.findall(r'\|.*\|', content)),
            "headers": self._extract_headers(content),
            "complexity_score": self._calculate_complexity_score(content)
        }
        
        return structure
    
    def _extract_headers(self, content: str) -> List[Dict[str, Any]]:
        """헤더 추출"""
        headers = []
        header_pattern = r'^(#+)\s+(.+)$'
        
        for match in re.finditer(header_pattern, content, re.MULTILINE):
            level = len(match.group(1))
            text = match.group(2).strip()
            headers.append({
                "level": level,
                "text": text,
                "anchor": re.sub(r'[^\w\s-]', '', text).strip().replace(' ', '-').lower()
            })
        
        return headers
    
    def _calculate_complexity_score(self, content: str) -> float:
        """콘텐츠 복잡도 점수 계산 (0.0-1.0)"""
        score = 0.0
        
        # 기본 요소들
        if re.search(r'^#+\s+', content, re.MULTILINE):
            score += 0.1  # 헤더
        if '```' in content:
            score += 0.2  # 코드 블록
        if re.search(r'\[([^\]]+)\]\(([^)]+)\)', content):
            score += 0.1  # 링크
        if re.search(r'!\[([^\]]*)\]\(([^)]+)\)', content):
            score += 0.1  # 이미지
        if '|' in content and re.search(r'\|.*\|', content):
            score += 0.15  # 테이블
        if re.search(r'^\s*[-*+]\s+', content, re.MULTILINE):
            score += 0.1  # 리스트
        
        # 고급 요소들
        if re.search(r'```\w+', content):  # 언어 지정된 코드 블록
            score += 0.1
        if re.search(r'>\s+', content, re.MULTILINE):  # 인용문
            score += 0.05
        if re.search(r'\*\*[^*]+\*\*|\__[^_]+\__', content):  # 강조
            score += 0.05
        if re.search(r'\*[^*]+\*|\_[^_]+\_', content):  # 기울임
            score += 0.05
        
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