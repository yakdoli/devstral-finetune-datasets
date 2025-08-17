#!/usr/bin/env python3
"""
유틸리티 모듈
공통 유틸리티 함수들을 제공합니다.
"""

import json
import logging
import hashlib
import uuid
import time
import asyncio
from typing import Dict, List, Any, Optional, Union
from pathlib import Path
from datetime import datetime
import re
from functools import wraps
import aiofiles


def setup_logging(level: str = "INFO", log_file: Optional[str] = None) -> logging.Logger:
    """
    로깅을 설정합니다.
    
    Args:
        level: 로그 레벨
        log_file: 로그 파일 경로 (선택적)
        
    Returns:
        설정된 로거
    """
    logger = logging.getLogger("openai_connector")
    logger.setLevel(getattr(logging, level.upper()))
    
    # 기본 핸들러
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # 콘솔 핸들러
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # 파일 핸들러
        if log_file:
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    
    return logger


def generate_conversation_id() -> str:
    """
    고유한 대화 ID를 생성합니다.
    
    Returns:
        생성된 대화 ID
    """
    return str(uuid.uuid4())


def extract_source_documents(documents: List[Dict[str, Any]]) -> List[str]:
    """
    문서에서 소스 정보를 추출합니다.
    
    Args:
        documents: 문서 목록
        
    Returns:
        소스 문서 ID 목록
    """
    source_ids = []
    
    for doc in documents:
        doc_id = doc.get('id', doc.get('title', str(hash(doc.get('content', '')))))
        source_ids.append(doc_id)
    
    return source_ids


def calculate_tokens_used(messages: List[Dict[str, str]]) -> int:
    """
    메시지의 토큰 사용량을 계산합니다.
    
    Args:
        messages: 메시지 목록
        
    Returns:
        사용된 토큰 수
    """
    total_chars = sum(len(msg.get('content', '')) for msg in messages)
    # 평균적으로 1토큰 = 4 characters
    return int(total_chars / 4)


def validate_conversation_format(conversation: Dict[str, Any]) -> bool:
    """
    대화 형식을 검증합니다.
    
    Args:
        conversation: 검증할 대화
        
    Returns:
        형식 유효 여부
    """
    required_fields = ['id', 'conversations', 'metadata']
    
    # 필드 존재 확인
    for field in required_fields:
        if field not in conversation:
            return False
    
    # 대화 내용 검증
    conversations = conversation.get('conversations', [])
    if not isinstance(conversations, list):
        return False
    
    for conv in conversations:
        if not isinstance(conv, dict):
            return False
        
        if 'from' not in conv or 'value' not in conv:
            return False
        
        if conv['from'] not in ['human', 'gpt']:
            return False
    
    # 메타데이터 검증
    metadata = conversation.get('metadata', {})
    if not isinstance(metadata, dict):
        return False
    
    return True


def save_conversations_to_json(
    conversations: List[Dict[str, Any]],
    output_path: Union[str, Path],
    indent: int = 2,
    ensure_ascii: bool = False
) -> bool:
    """
    대화를 JSON 파일로 저장합니다.
    
    Args:
        conversations: 저장할 대화 목록
        output_path: 출력 파일 경로
        indent: JSON 들여쓰기
        ensure_ascii: ASCII 문자 보장 여부
        
    Returns:
        저장 성공 여부
    """
    try:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 대화 데이터 변환
        data = []
        for conv in conversations:
            if isinstance(conv, dict):
                data.append(conv)
            else:
                # Conversation 객체인 경우
                data.append(conv.to_dict())
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)
        
        return True
        
    except Exception as e:
        logging.error(f"대화 저장 실패: {e}")
        return False


def load_conversations_from_json(input_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    JSON 파일에서 대화를 불러옵니다.
    
    Args:
        input_path: 입력 파일 경로
        
    Returns:
        불러온 대화 목록
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return data
        
    except Exception as e:
        logging.error(f"대화 로드 실패: {e}")
        return []


def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exceptions: tuple = (Exception,)
):
    """
    백오프 전략을 사용한 재시도 데코레이터.
    
    Args:
        max_retries: 최대 재시도 횟수
        base_delay: 기본 지연 시간
        max_delay: 최대 지연 시간
        exceptions: 재시도할 예외 타입
        
    Returns:
        데코레이터 함수
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt < max_retries:
                        # 지수 백오프 계산
                        delay = min(base_delay * (2 ** attempt), max_delay)
                        logging.warning(f"Attempt {attempt + 1} failed. Retrying in {delay:.2f} seconds...")
                        await asyncio.sleep(delay)
                    else:
                        logging.error(f"All {max_retries} attempts failed")
                        raise last_exception
        
        return wrapper
    return decorator


def handle_rate_limit(
    max_retries: int = 5,
    base_delay: float = 1.0,
    max_delay: float = 300.0
):
    """
    레이트 리미트 처리 데코레이터.
    
    Args:
        max_retries: 최대 재시도 횟수
        base_delay: 기본 지연 시간
        max_delay: 최대 지연 시간
        
    Returns:
        데코레이터 함수
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    
                    # 레이트 리미트 오류 감지
                    if "rate limit" in str(e).lower() or "429" in str(e):
                        if attempt < max_retries:
                            # 지수 백오프 계산
                            delay = min(base_delay * (2 ** attempt), max_delay)
                            logging.warning(f"Rate limited. Retrying in {delay:.2f} seconds...")
                            await asyncio.sleep(delay)
                        else:
                            logging.error(f"Rate limit retries exhausted")
                            raise last_exception
                    else:
                        # 레이트 리미트 오류가 아닌 경우 즉시 재시도
                        if attempt < max_retries:
                            delay = base_delay
                            logging.warning(f"Request failed. Retrying in {delay:.2f} seconds...")
                            await asyncio.sleep(delay)
                        else:
                            raise last_exception
        
        return wrapper
    return decorator


def benchmark_generation_performance(
    func: callable,
    *args,
    **kwargs
) -> Dict[str, Any]:
    """
    생성 성능을 벤치마크합니다.
    
    Args:
        func: 벤치마크할 함수
        *args: 함수 인자
        **kwargs: 함수 키워드 인자
        
    Returns:
        벤치마크 결과
    """
    start_time = time.time()
    
    try:
        result = func(*args, **kwargs)
        success = True
    except Exception as e:
        result = str(e)
        success = False
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return {
        "execution_time": execution_time,
        "success": success,
        "result": result,
        "timestamp": datetime.now().isoformat()
    }


def clean_text(text: str) -> str:
    """
    텍스트를 정제합니다.
    
    Args:
        text: 정제할 텍스트
        
    Returns:
        정제된 텍스트
    """
    if not text:
        return ""
    
    # 불필요한 공백 제거
    text = re.sub(r'\s+', ' ', text)
    
    # 특수 문자 정리
    text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)\[\]\{\}\"\'\/\@\#\$\%\^\&\*\+\=\~\`]', '', text)
    
    # 줄바꿈 정리
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    return text.strip()


def extract_code_blocks(text: str) -> List[str]:
    """
    텍스트에서 코드 블록을 추출합니다.
    
    Args:
        text: 분석할 텍스트
        
    Returns:
        코드 블록 목록
    """
    code_blocks = []
    
    # 마크다운 코드 블록 추출
    markdown_pattern = r'```(?:[a-zA-Z0-9+]*)?\n(.*?)\n```'
    matches = re.findall(markdown_pattern, text, re.DOTALL)
    code_blocks.extend(matches)
    
    # 인라인 코드 추출
    inline_pattern = r'`([^`]+)`'
    inline_matches = re.findall(inline_pattern, text)
    code_blocks.extend(inline_matches)
    
    return code_blocks


def calculate_text_similarity(text1: str, text2: str) -> float:
    """
    두 텍스트의 유사도를 계산합니다.
    
    Args:
        text1: 첫 번째 텍스트
        text2: 두 번째 텍스트
        
    Returns:
        유사도 점수 (0.0 ~ 1.0)
    """
    if not text1 or not text2:
        return 0.0
    
    # 간단한 단어 기반 유사도 계산
    words1 = set(re.findall(r'\b\w+\b', text1.lower()))
    words2 = set(re.findall(r'\b\w+\b', text2.lower()))
    
    if not words1 or not words2:
        return 0.0
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    return len(intersection) / len(union) if union else 0.0


def generate_hash(content: str) -> str:
    """
    콘텐츠의 해시를 생성합니다.
    
    Args:
        content: 해시할 콘텐츠
        
    Returns:
        생성된 해시
    """
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def merge_metadata(metadata_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    메타데이터 목록을 병합합니다.
    
    Args:
        metadata_list: 메타데이터 목록
        
    Returns:
        병합된 메타데이터
    """
    merged = {}
    
    for metadata in metadata_list:
        if not isinstance(metadata, dict):
            continue
        
        for key, value in metadata.items():
            if key in merged:
                # 리스트인 경우 병합
                if isinstance(merged[key], list) and isinstance(value, list):
                    merged[key].extend(value)
                # 숫자인 경우 합산
                elif isinstance(merged[key], (int, float)) and isinstance(value, (int, float)):
                    merged[key] += value
                # 문자열인 경우 연결
                elif isinstance(merged[key], str) and isinstance(value, str):
                    merged[key] += " | " + value
                # 그 외의 경우 덮어쓰기
                else:
                    merged[key] = value
            else:
                merged[key] = value
    
    return merged


def format_file_size(size_bytes: int) -> str:
    """
    파일 크기를 읽기 쉬운 형식으로 포맷합니다.
    
    Args:
        size_bytes: 바이트 크기
        
    Returns:
        포맷된 파일 크기
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"


async def async_file_exists(file_path: Union[str, Path]) -> bool:
    """
    파일 존재 여부를 비동기로 확인합니다.
    
    Args:
        file_path: 파일 경로
        
    Returns:
        파일 존재 여부
    """
    try:
        async with aiofiles.open(file_path, 'r'):
            return True
    except (FileNotFoundError, IOError):
        return False


def get_file_info(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    파일 정보를 가져옵니다.
    
    Args:
        file_path: 파일 경로
        
    Returns:
        파일 정보 딕셔너리
    """
    path = Path(file_path)
    
    if not path.exists():
        return {"exists": False}
    
    stat = path.stat()
    
    return {
        "exists": True,
        "size": stat.st_size,
        "size_formatted": format_file_size(stat.st_size),
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
        "extension": path.suffix,
        "name": path.name,
        "stem": path.stem,
        "parent": str(path.parent)
    }


# 테스트 코드
def test_utils():
    """유틸리티 함수 테스트"""
    # 로깅 테스트
    logger = setup_logging("DEBUG")
    logger.info("로깅 테스트")
    
    # 대화 ID 생성 테스트
    conv_id = generate_conversation_id()
    print(f"생성된 대화 ID: {conv_id}")
    
    # 토큰 계산 테스트
    messages = [
        {"role": "user", "content": "안녕하세요. GridControl 사용법을 알려주세요."},
        {"role": "assistant", "content": "GridControl은 Syncfusion의 강력한 컴포넌트입니다..."}
    ]
    tokens = calculate_tokens_used(messages)
    print(f"계산된 토큰 수: {tokens}")
    
    # 텍스트 정제 테스트
    dirty_text = "  이것은    테스트  텍스트입니다.  \n\n  여러  줄입니다.  "
    clean_text_result = clean_text(dirty_text)
    print(f"정제된 텍스트: '{clean_text_result}'")
    
    # 코드 블록 추출 테스트
    text_with_code = "여기에 코드가 있습니다: ```csharp var x = 1; ``` 그리고 `inline code`도 있습니다."
    code_blocks = extract_code_blocks(text_with_code)
    print(f"추출된 코드 블록: {code_blocks}")
    
    # 유사도 계산 테스트
    similarity = calculate_text_similarity("안녕하세요", "안녕하세요 반갑습니다")
    print(f"텍스트 유사도: {similarity:.2f}")
    
    # 해시 생성 테스트
    content_hash = generate_hash("테스트 콘텐츠")
    print(f"생성된 해시: {content_hash}")
    
    # 파일 정보 테스트
    file_info = get_file_info(__file__)
    print(f"파일 정보: {file_info}")


if __name__ == "__main__":
    test_utils()