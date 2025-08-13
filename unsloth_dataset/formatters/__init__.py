#!/usr/bin/env python3
"""
포맷터 모듈 초기화 파일
다양한 데이터셋 포맷을 생성하는 포맷터들을 제공합니다.
"""

from .sharegpt_formatter import ShareGPTFormatter, ShareGPTConfig
from .alpaca_formatter import AlpacaFormatter, AlpacaConfig
from .openai_formatter import OpenAIFormatter, OpenAIConfig

__version__ = "1.0.0"
__author__ = "Unsloth Dataset Formatter Team"
__email__ = "support@example.com"
__description__ = "Dataset Formatters for Unsloth Fine-tuning"

__all__ = [
    # ShareGPT Formatter
    'ShareGPTFormatter',
    'ShareGPTConfig',
    
    # Alpaca Formatter
    'AlpacaFormatter',
    'AlpacaConfig',
    
    # OpenAI Formatter
    'OpenAIFormatter',
    'OpenAIConfig',
    
    # Version info
    '__version__',
    '__author__',
    '__email__',
    '__description__'
]


# 모듈 로드 시 기본 로깅 설정
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


def create_formatter(format_type: str, **kwargs):
    """
    지정된 포맷 타입에 맞는 포맷터를 생성합니다.
    
    Args:
        format_type: 포맷 타입 ("sharegpt", "alpaca", "openai")
        **kwargs: 포맷터별 설정
        
    Returns:
        생성된 포맷터 인스턴스
        
    Raises:
        ValueError: 지원하지 않는 포맷 타입인 경우
    """
    format_type = format_type.lower()
    
    if format_type == "sharegpt":
        return ShareGPTFormatter(**kwargs)
    elif format_type == "alpaca":
        return AlpacaFormatter(**kwargs)
    elif format_type == "openai":
        return OpenAIFormatter(**kwargs)
    else:
        raise ValueError(f"지원하지 않는 포맷 타입: {format_type}. "
                        "지원하는 포맷: 'sharegpt', 'alpaca', 'openai'")


def get_supported_formats():
    """지원하는 포맷 목록을 반환합니다."""
    return ["sharegpt", "alpaca", "openai"]


def get_format_description(format_type: str) -> str:
    """지정된 포맷의 설명을 반환합니다."""
    descriptions = {
        "sharegpt": "다중 턴 대화 형식의 ShareGPT 포맷",
        "alpaca": "instruction/input/output 구조의 Alpaca 포맷", 
        "openai": "messages 배열 구조의 OpenAI 포맷"
    }
    return descriptions.get(format_type.lower(), "알 수 없는 포맷")


if __name__ == "__main__":
    print("=== Dataset Formatters Module ===")
    print(f"Supported formats: {get_supported_formats()}")
    
    for fmt in get_supported_formats():
        print(f"{fmt}: {get_format_description(fmt)}")
    
    print("\nUse create_formatter() to create formatters.")