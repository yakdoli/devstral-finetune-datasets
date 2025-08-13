#!/usr/bin/env python3
"""
MD 처리 모듈 유틸리티
공통 유틸리티 함수와 헬퍼 함수들을 제공합니다.
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Union, Tuple
from datetime import datetime
import hashlib
import unicodedata

logger = logging.getLogger(__name__)


def setup_logging(level: str = "INFO", log_file: Optional[str] = None) -> logging.Logger:
    """
    로깅 설정을 초기화합니다.
    
    Args:
        level: 로깅 레벨
        log_file: 로그 파일 경로 (선택적)
        
    Returns:
        설정된 로거
    """
    log_level = getattr(logging, level.upper(), logging.INFO)
    
    # 포매터 설정
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 핸들러 설정
    handlers = [logging.StreamHandler()]
    
    if log_file:
        # 로그 파일 디렉토리 생성
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file, encoding='utf-8'))
    
    # 로거 설정
    logging.basicConfig(
        level=log_level,
        handlers=handlers,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    return logging.getLogger(__name__)


def normalize_text(text: str) -> str:
    """
    텍스트를 정규화합니다.
    
    Args:
        text: 정규화할 텍스트
        
    Returns:
        정규화된 텍스트
    """
    if not text:
        return ""
    
    # 유니코드 정규화
    text = unicodedata.normalize('NFKC', text)
    
    # 여러 공백을 단일 공백으로 변경
    text = re.sub(r'\s+', ' ', text)
    
    # 줄바꿈 정리
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # 양 끝 공백 제거
    text = text.strip()
    
    return text


def clean_filename(filename: str) -> str:
    """
    파일명에서 특수 문자를 제거합니다.
    
    Args:
        filename: 정리할 파일명
        
    Returns:
        정리된 파일명
    """
    # 허용되지 않는 문자 제거
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    
    # 공백을 언더스코어로 변경
    filename = re.sub(r'\s+', '_', filename)
    
    # 점 여러 개는 하나로 변경
    filename = re.sub(r'\.+', '.', filename)
    
    # 양 끝 점 제거
    filename = filename.strip('.')
    
    # 빈 파일명 처리
    if not filename:
        filename = "unnamed"
    
    return filename


def generate_unique_id(content: str, prefix: str = "doc") -> str:
    """
    고유 ID를 생성합니다.
    
    Args:
        content: ID 생성에 사용할 콘텐츠
        prefix: ID 접두사
        
    Returns:
        고유 ID
    """
    content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()[:8]
    return f"{prefix}_{content_hash}"


def extract_metadata_from_content(content: str) -> Dict[str, Any]:
    """
    콘텐츠에서 메타데이터를 추출합니다.
    
    Args:
        content: 메타데이터를 추출할 콘텐츠
        
    Returns:
        추출된 메타데이터 딕셔너리
    """
    metadata = {}
    
    # YAML 프론트매터 추출
    yaml_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        try:
            # YAML 파싱 (간단한 버전만 처리)
            for line in yaml_content.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"\'')
                    metadata[key] = value
        except Exception as e:
            logger.warning(f"Failed to parse YAML frontmatter: {e}")
        
        # YAML 프론트매터 제거
        content = content[yaml_match.end():]
    
    # 제목 추출
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    # 키워드 추출
    keywords = []
    # 헤더에서 키워드 추출
    header_matches = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    keywords.extend([h.strip() for h in header_matches])
    
    # 코드 블록에서 언어 추출
    code_matches = re.findall(r'```(\w+)', content)
    keywords.extend(code_matches)
    
    if keywords:
        metadata['keywords'] = list(set(keywords))
    
    return metadata


def calculate_content_stats(content: str) -> Dict[str, Any]:
    """
    콘텐츠 통계를 계산합니다.
    
    Args:
        content: 통계를 계산할 콘텐츠
        
    Returns:
        콘텐츠 통계 딕셔너리
    """
    if not content:
        return {
            "character_count": 0,
            "word_count": 0,
            "line_count": 0,
            "paragraph_count": 0,
            "header_count": 0,
            "code_block_count": 0,
            "link_count": 0,
            "image_count": 0,
            "list_count": 0
        }
    
    stats = {
        "character_count": len(content),
        "word_count": len(re.findall(r'\b\w+\b', content)),
        "line_count": len(content.split('\n')),
        "paragraph_count": len([p for p in content.split('\n\n') if p.strip()]),
        "header_count": len(re.findall(r'^#+\s+', content, re.MULTILINE)),
        "code_block_count": len(re.findall(r'```', content)) // 2,
        "link_count": len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)),
        "image_count": len(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)),
        "list_count": len(re.findall(r'^\s*[-*+]\s+', content, re.MULTILINE)) +
                     len(re.findall(r'^\s*\d+\.\s+', content, re.MULTILINE))
    }
    
    return stats


def validate_document_structure(document: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    문서 구조를 검증합니다.
    
    Args:
        document: 검증할 문서 딕셔너리
        
    Returns:
        (유효성 여부, 오류 목록)
    """
    errors = []
    
    # 필수 필드 검증
    required_fields = ['id', 'title', 'content']
    for field in required_fields:
        if field not in document:
            errors.append(f"Missing required field: {field}")
    
    # ID 형식 검증
    if 'id' in document and not isinstance(document['id'], str):
        errors.append("ID must be a string")
    
    # 제목 형식 검증
    if 'title' in document and not isinstance(document['title'], str):
        errors.append("Title must be a string")
    
    # 콘텐츠 형식 검증
    if 'content' in document and not isinstance(document['content'], str):
        errors.append("Content must be a string")
    
    # 메타데이터 검증
    if 'metadata' in document and not isinstance(document['metadata'], dict):
        errors.append("Metadata must be a dictionary")
    
    # 품질 점수 검증
    if 'quality_score' in document:
        try:
            score = float(document['quality_score'])
            if not (0.0 <= score <= 1.0):
                errors.append("Quality score must be between 0.0 and 1.0")
        except (ValueError, TypeError):
            errors.append("Quality score must be a number")
    
    return len(errors) == 0, errors


def merge_documents(documents: List[Dict[str, Any]], merge_strategy: str = "append") -> Dict[str, Any]:
    """
    여러 문서를 병합합니다.
    
    Args:
        documents: 병합할 문서 목록
        merge_strategy: 병합 전략 ("append", "interleave")
        
    Returns:
        병합된 문서
    """
    if not documents:
        return {}
    
    if len(documents) == 1:
        return documents[0]
    
    # 기본 정보 가져오기
    base_doc = documents[0].copy()
    
    # 콘텐츠 병합
    contents = [doc.get('content', '') for doc in documents]
    
    if merge_strategy == "append":
        merged_content = '\n\n'.join(filter(None, contents))
    elif merge_strategy == "interleave":
        # 간단한 인터리빙 (실제 구현은 더 복잡할 수 있음)
        merged_content = '\n\n'.join(filter(None, contents))
    else:
        merged_content = '\n\n'.join(filter(None, contents))
    
    # 병합된 문서 생성
    merged_doc = {
        'id': generate_unique_id(merged_content, 'merged'),
        'title': f"Merged: {', '.join(doc.get('title', 'Unknown') for doc in documents)}",
        'component': documents[0].get('component'),
        'page': documents[0].get('page'),
        'content': merged_content,
        'metadata': {
            'merge_strategy': merge_strategy,
            'source_count': len(documents),
            'source_ids': [doc.get('id') for doc in documents],
            'merge_time': datetime.now().isoformat()
        },
        'quality_score': min(doc.get('quality_score', 1.0) for doc in documents)
    }
    
    return merged_doc


def save_documents_to_json(documents: List[Dict[str, Any]], output_path: Path, 
                          indent: int = 2, ensure_ascii: bool = False):
    """
    문서를 JSON 파일로 저장합니다.
    
    Args:
        documents: 저장할 문서 목록
        output_path: 출력 파일 경로
        indent: JSON 들여쓰기
        ensure_ascii: ASCII 문자 보장 여부
    """
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(documents, f, indent=indent, ensure_ascii=ensure_ascii)
        
        logger.info(f"Saved {len(documents)} documents to {output_path}")
        
    except Exception as e:
        logger.error(f"Failed to save documents to {output_path}: {e}")
        raise


def load_documents_from_json(input_path: Path) -> List[Dict[str, Any]]:
    """
    JSON 파일에서 문서를 불러옵니다.
    
    Args:
        input_path: 입력 파일 경로
        
    Returns:
        불러온 문서 목록
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            documents = json.load(f)
        
        # 단일 문서인 경우 리스트로 변환
        if isinstance(documents, dict):
            documents = [documents]
        
        logger.info(f"Loaded {len(documents)} documents from {input_path}")
        return documents
        
    except Exception as e:
        logger.error(f"Failed to load documents from {input_path}: {e}")
        return []


def create_directory_structure(base_path: Union[str, Path]) -> Path:
    """
    디렉토리 구조를 생성합니다.
    
    Args:
        base_path: 기본 경로
        
    Returns:
        생성된 기본 경로
    """
    base_path = Path(base_path)
    
    # 필요한 디렉토리들
    directories = [
        base_path,
        base_path / "output",
        base_path / "processed",
        base_path / "logs",
        base_path / "temp"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    
    return base_path


def get_file_info(file_path: Path) -> Dict[str, Any]:
    """
    파일 정보를 가져옵니다.
    
    Args:
        file_path: 파일 경로
        
    Returns:
        파일 정보 딕셔너리
    """
    if not file_path.exists():
        return {"error": "File not found"}
    
    stat = file_path.stat()
    
    return {
        "path": str(file_path),
        "name": file_path.name,
        "size": stat.st_size,
        "size_human": format_file_size(stat.st_size),
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
        "extension": file_path.suffix,
        "is_file": file_path.is_file(),
        "is_dir": file_path.is_dir()
    }


def format_file_size(size_bytes: int) -> str:
    """
    파일 크기를 사람이 읽기 쉬운 형식으로 변환합니다.
    
    Args:
        size_bytes: 바이트 크기
        
    Returns:
        포맷된 파일 크기 문자열
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"


def is_valid_md_file(file_path: Path) -> bool:
    """
    유효한 MD 파일인지 확인합니다.
    
    Args:
        file_path: 파일 경로
        
    Returns:
        유효성 여부
    """
    if not file_path.is_file():
        return False
    
    if file_path.suffix.lower() not in {'.md', '.markdown'}:
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # 최소한의 콘텐츠가 있는지 확인
            return len(content.strip()) > 0
    except Exception:
        return False


def batch_process(items: List[Any], batch_size: int, process_func, *args, **kwargs) -> List[Any]:
    """
    배치 처리를 수행합니다.
    
    Args:
        items: 처리할 항목 목록
        batch_size: 배치 크기
        process_func: 처리 함수
        *args: 처리 함수에 전달할 추가 인자
        **kwargs: 처리 함수에 전달할 추가 키워드 인자
        
    Returns:
        처리 결과 목록
    """
    results = []
    
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        logger.info(f"Processing batch {i//batch_size + 1}: {len(batch)} items")
        
        batch_results = process_func(batch, *args, **kwargs)
        results.extend(batch_results)
    
    return results


if __name__ == "__main__":
    # 테스트 코드
    setup_logging("INFO")
    
    # 텍스트 정규화 테스트
    test_text = "  Hello   World  \n\n  Test  \n"
    normalized = normalize_text(test_text)
    print(f"정규화된 텍스트: '{normalized}'")
    
    # 파일명 정리 테스트
    test_filename = "test<>file:name?*with*special|chars.md"
    cleaned = clean_filename(test_filename)
    print(f"정리된 파일명: '{cleaned}'")
    
    # 고유 ID 생성 테스트
    test_content = "This is a test content for ID generation"
    unique_id = generate_unique_id(test_content)
    print(f"생성된 고유 ID: {unique_id}")
    
    # 콘텐츠 통계 테스트
    test_content = """
# Test Document

This is a test document with some content.

## Section 1
- Item 1
- Item 2

## Section 2
Some code here:

```python
def test_function():
    return "Hello, World!"
```

And a link [here](https://example.com).
"""
    stats = calculate_content_stats(test_content)
    print("콘텐츠 통계:")
    for key, value in stats.items():
        print(f"  {key}: {value}")