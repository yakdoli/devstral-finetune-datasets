#!/usr/bin/env python3
"""
유틸리티 함수 모듈
공통 유틸리티 함수를 제공합니다.
"""

import json
import logging
import asyncio
import time
import hashlib
import os
from typing import Dict, Any, List, Optional, Union
from pathlib import Path
from datetime import datetime
import aiohttp

logger = logging.getLogger(__name__)


def setup_logging(
    level: str = "INFO",
    format_string: Optional[str] = None,
    log_file: Optional[str] = None,
    enable_console: bool = True,
    enable_file: bool = True
) -> logging.Logger:
    """
    로깅 설정을 초기화합니다.
    
    Args:
        level: 로그 레벨
        format_string: 로그 형식 문자열
        log_file: 로그 파일 경로
        enable_console: 콘솔 출력 여부
        enable_file: 파일 출력 여부
        
    Returns:
        설정된 로거
    """
    # 로거 생성
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level.upper()))
    
    # 포맷터 설정
    format_string = format_string or "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(format_string)
    
    # 핸들러 초기화
    handlers = []
    
    # 콘솔 핸들러
    if enable_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        handlers.append(console_handler)
    
    # 파일 핸들러
    if enable_file and log_file:
        # 디렉토리 생성
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)
    
    # 핸들러 설정
    logger.handlers.clear()
    for handler in handlers:
        logger.addHandler(handler)
    
    return logger


def generate_conversation_id() -> str:
    """
    고유한 대화 ID를 생성합니다.
    
    Returns:
        생성된 대화 ID
    """
    return hashlib.md5(str(time.time()).encode()).hexdigest()[:16]


def extract_source_documents(conversation: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    대화에서 소스 문서를 추출합니다.
    
    Args:
        conversation: 대화 데이터
        
    Returns:
        소스 문서 목록
    """
    source_docs = []
    
    # 메타데이터에서 소스 문서 정보 추출
    metadata = conversation.get("metadata", {})
    if "source_documents" in metadata:
        source_docs.extend(metadata["source_documents"])
    
    # 대화 내용에서 문서 참조 추출
    for message in conversation.get("conversations", []):
        content = message.get("content", "")
        if "document:" in content.lower():
            # 간단한 문서 참조 추출
            doc_ref = content.lower().split("document:")[1].split()[0]
            source_docs.append({"id": doc_ref, "title": f"Document {doc_ref}"})
    
    return source_docs


def calculate_tokens_used(text: str) -> int:
    """
    텍스트의 토큰 사용량을 계산합니다.
    
    Args:
        text: 계산할 텍스트
        
    Returns:
        토큰 수
    """
    # 간단한 토큰 계산 (실제로는 tiktoken 사용이 좋음)
    return len(text) // 4


def validate_conversation_format(conversation: Dict[str, Any]) -> Dict[str, Any]:
    """
    대화 형식을 검증합니다.
    
    Args:
        conversation: 검증할 대화
        
    Returns:
        검증 결과
    """
    result = {
        "valid": True,
        "errors": [],
        "warnings": []
    }
    
    # 필수 필드 확인
    required_fields = ["id", "conversations"]
    for field in required_fields:
        if field not in conversation:
            result["valid"] = False
            result["errors"].append(f"필수 필드 누락: {field}")
    
    # 대화 형식 확인
    if "conversations" in conversation:
        conversations = conversation["conversations"]
        if not isinstance(conversations, list):
            result["valid"] = False
            result["errors"].append("conversations는 리스트여야 합니다")
        else:
            for i, msg in enumerate(conversations):
                if not isinstance(msg, dict):
                    result["valid"] = False
                    result["errors"].append(f"메시지 {i}는 딕셔너리여야 합니다")
                    continue
                
                if "role" not in msg or "content" not in msg:
                    result["valid"] = False
                    result["errors"].append(f"메시지 {i}에는 role과 content 필드가 필요합니다")
                
                # 역할 유효성 확인
                valid_roles = ["user", "assistant", "system"]
                if msg.get("role") not in valid_roles:
                    result["warnings"].append(f"메시지 {i}의 역할이 유효하지 않음: {msg.get('role')}")
    
    return result


def save_conversations_to_json(
    conversations: List[Dict[str, Any]],
    output_path: Union[str, Path],
    indent: int = 2
) -> bool:
    """
    대화 목록을 JSON 파일로 저장합니다.
    
    Args:
        conversations: 저장할 대화 목록
        output_path: 출력 파일 경로
        indent: JSON 들여쓰기
        
    Returns:
        저장 성공 여부
    """
    try:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, indent=indent, ensure_ascii=False)
        
        logger.info(f"대화 데이터 저장 완료: {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"대화 데이터 저장 실패: {e}")
        return False


def load_conversations_from_json(input_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    JSON 파일에서 대화 목록을 로드합니다.
    
    Args:
        input_path: 입력 파일 경로
        
    Returns:
        로드된 대화 목록
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            conversations = json.load(f)
        
        logger.info(f"대화 데이터 로드 완료: {len(conversations)}개")
        return conversations
        
    except Exception as e:
        logger.error(f"대화 데이터 로드 실패: {e}")
        return []


async def retry_with_backoff(
    func,
    max_attempts: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (Exception,)
):
    """
    백오프와 함께 재시도를 수행합니다.
    
    Args:
        func: 실행할 함수
        max_attempts: 최대 시도 횟수
        base_delay: 기본 지연 시간 (초)
        max_delay: 최대 지연 시간 (초)
        backoff_factor: 백오프 배수
        exceptions: 재시도할 예외 타입
        
    Returns:
        함수 실행 결과
        
    Raises:
        마지막 예외
    """
    last_exception = None
    
    for attempt in range(max_attempts):
        try:
            return await func()
        except exceptions as e:
            last_exception = e
            if attempt < max_attempts - 1:
                delay = min(base_delay * (backoff_factor ** attempt), max_delay)
                logger.warning(f"Attempt {attempt + 1} failed. Retrying in {delay:.2f} seconds...")
                await asyncio.sleep(delay)
            else:
                logger.error(f"All {max_attempts} attempts failed")
    
    raise last_exception


async def handle_rate_limit(
    response: aiohttp.ClientResponse,
    max_retries: int = 3,
    base_delay: float = 1.0
) -> bool:
    """
    레이트 리미트 오류를 처리합니다.
    
    Args:
        response: HTTP 응답
        max_retries: 최대 재시도 횟수
        base_delay: 기본 지연 시간
        
    Returns:
        처리 성공 여부
    """
    if response.status == 429:
        retry_after = int(response.headers.get("Retry-After", base_delay))
        logger.warning(f"Rate limited. Retrying after {retry_after} seconds...")
        await asyncio.sleep(retry_after)
        return True
    
    return False


async def benchmark_generation_performance(
    func,
    *args,
    **kwargs
) -> Dict[str, Any]:
    """
    생성 성능을 벤치마크합니다.
    
    Args:
        func: 벤치마크할 함수
        *args: 함수 인자
        **kwargs: 키워드 인자
        
    Returns:
        벤치마크 결과
    """
    start_time = time.time()
    
    try:
        result = await func(*args, **kwargs)
        success = True
    except Exception as e:
        result = str(e)
        success = False
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return {
        "success": success,
        "execution_time": execution_time,
        "start_time": datetime.fromtimestamp(start_time).isoformat(),
        "end_time": datetime.fromtimestamp(end_time).isoformat(),
        "result": result
    }


def get_environment_variables() -> Dict[str, str]:
    """
    관련 환경 변수를 가져옵니다.
    
    Returns:
        환경 변수 딕셔너리
    """
    env_vars = {}
    
    # OpenAI 관련 환경 변수
    env_vars.update({
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "OPENAI_ENDPOINT": os.getenv("OPENAI_ENDPOINT", "http://123.37.28.120:9997/v1"),
        "OPENAI_MODEL": os.getenv("OPENAI_MODEL", "qwen2.5-vl-instruct"),
        "OPENAI_MAX_TOKENS": os.getenv("OPENAI_MAX_TOKENS", "128000"),
        "OPENAI_TEMPERATURE": os.getenv("OPENAI_TEMPERATURE", "0.3"),
    })
    
    # 로컬 LLM 관련 환경 변수
    env_vars.update({
        "LOCAL_LLM_ENDPOINT": os.getenv("LOCAL_LLM_ENDPOINT", "http://123.37.28.120:9997/v1"),
        "LOCAL_LLM_MODEL": os.getenv("LOCAL_LLM_MODEL", "qwen2.5-vl-instruct"),
        "LOCAL_LLM_API_KEY": os.getenv("LOCAL_LLM_API_KEY", "your-api-key"),
        "LOCAL_LLM_MAX_TOKENS": os.getenv("LOCAL_LLM_MAX_TOKENS", "128000"),
        "LOCAL_LLM_TEMPERATURE": os.getenv("LOCAL_LLM_TEMPERATURE", "0.3"),
    })
    
    return env_vars


def validate_configuration(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    설정 유효성을 검증합니다.
    
    Args:
        config: 검증할 설정
        
    Returns:
        검증 결과
    """
    result = {
        "valid": True,
        "errors": [],
        "warnings": []
    }
    
    # 필수 설정 확인
    required_settings = ["endpoint", "model", "max_tokens", "temperature"]
    for setting in required_settings:
        if setting not in config:
            result["valid"] = False
            result["errors"].append(f"필수 설정 누락: {setting}")
    
    # 값 유효성 확인
    if "max_tokens" in config:
        try:
            max_tokens = int(config["max_tokens"])
            if max_tokens <= 0:
                result["valid"] = False
                result["errors"].append("max_tokens는 양의 정수여야 합니다")
        except ValueError:
            result["valid"] = False
            result["errors"].append("max_tokens는 정수여야 합니다")
    
    if "temperature" in config:
        try:
            temperature = float(config["temperature"])
            if not (0.0 <= temperature <= 2.0):
                result["warnings"].append("temperature는 0.0과 2.0 사이가 권장됩니다")
        except ValueError:
            result["valid"] = False
            result["errors"].append("temperature는 숫자여야 합니다")
    
    return result


def create_directory_structure(base_path: Union[str, Path]) -> bool:
    """
    디렉토리 구조를 생성합니다.
    
    Args:
        base_path: 기본 경로
        
    Returns:
        생성 성공 여부
    """
    try:
        base_path = Path(base_path)
        
        # 필요한 디렉토리 목록
        directories = [
            base_path,
            base_path / "output",
            base_path / "temp",
            base_path / "cache",
            base_path / "logs",
            base_path / "templates"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"디렉토리 구조 생성 완료: {base_path}")
        return True
        
    except Exception as e:
        logger.error(f"디렉토리 구조 생성 실패: {e}")
        return False


if __name__ == "__main__":
    # 테스트 코드
    print("유틸리티 함수 테스트")
    
    # 로깅 테스트
    logger = setup_logging(level="DEBUG", log_file="test.log")
    logger.info("로깅 테스트")
    
    # ID 생성 테스트
    conversation_id = generate_conversation_id()
    print(f"생성된 대화 ID: {conversation_id}")
    
    # 토큰 계산 테스트
    text = "This is a test text for token calculation."
    tokens = calculate_tokens_used(text)
    print(f"토큰 수: {tokens}")
    
    # 환경 변수 테스트
    env_vars = get_environment_variables()
    print(f"환경 변수: {env_vars}")