#!/usr/bin/env python3
"""
OpenAI 호환 API 연동 모듈 초기화 파일
qwen2.5-vl-instruct 모델을 통한 LLM 기반 데이터셋 생성 기능을 제공합니다.
"""

from typing import List, Dict, Any, Optional
from pathlib import Path
from .client import (
    OpenAIAPIClientConfig,
    OpenAIClient,
    create_openai_client
)
from .prompt_engine import (
    PromptEngine,
    PromptConfig,
    PromptEngineConfig,
    create_prompt_engine
)
from .conversation_generator import (
    ConversationGenerator,
    ConversationConfig,
    GenerationMode,
    Conversation,
    create_conversation_generator
)
from .token_manager import (
    TokenManager,
    TokenConfig,
    TokenLimitType,
    create_token_manager
)
from .utils import (
    setup_logging,
    generate_conversation_id,
    extract_source_documents,
    calculate_tokens_used,
    validate_conversation_format,
    save_conversations_to_json,
    load_conversations_from_json,
    retry_with_backoff,
    handle_rate_limit,
    benchmark_generation_performance
)

__version__ = "1.0.0"
__author__ = "OpenAI Connector Team"
__email__ = "support@example.com"
__description__ = "OpenAI Compatible API Connector for LLM-based Dataset Generation"

__all__ = [
    # Client
    'OpenAIAPIClientConfig',
    'OpenAIClient',
    'create_openai_client',
    
    # Prompt Engine
    'PromptEngine',
    'PromptConfig',
    'PromptEngineConfig',
    'create_prompt_engine',
    
    # Conversation Generator
    'ConversationGenerator',
    'ConversationConfig',
    'GenerationMode',
    'Conversation',
    'create_conversation_generator',
    
    # Token Manager
    'TokenManager',
    'TokenConfig',
    'TokenLimitType',
    'create_token_manager',
    
    # Utils
    'setup_logging',
    'generate_conversation_id',
    'extract_source_documents',
    'calculate_tokens_used',
    'validate_conversation_format',
    'save_conversations_to_json',
    'load_conversations_from_json',
    'retry_with_backoff',
    'handle_rate_limit',
    'benchmark_generation_performance',
    
    # Version info
    '__version__',
    '__author__',
    '__email__',
    '__description__'
]


class OpenAIConnector:
    """OpenAI 연동 모듈 메인 클래스"""
    
    def __init__(
        self,
        endpoint: str = "http://123.37.28.120:9997/v1",
        model: str = "qwen2.5-vl-instruct",
        api_key: str = "your-api-key",
        max_tokens: int = 128000,
        temperature: float = 0.3,
        max_concurrent: int = 8,
        batch_size: int = 16
    ):
        """
        OpenAI 연동 모듈을 초기화합니다.
        
        Args:
            endpoint: API 엔드포인트
            model: 사용할 모델 이름
            api_key: API 키
            max_tokens: 최대 토큰 수
            temperature: 생성 온도
            max_concurrent: 최대 동시 요청 수
            batch_size: 배치 크기
        """
        self.client_config = OpenAIAPIClientConfig(
            endpoint=endpoint,
            model=model,
            api_key=api_key,
            max_tokens=max_tokens,
            temperature=temperature,
            max_concurrent=max_concurrent,
            batch_size=batch_size
        )
        
        self.prompt_config = PromptConfig()
        self.conversation_config = ConversationConfig(
            generation_mode=GenerationMode.LLM_ASSISTED,
            target_count=1000,
            max_turns=6
        )
        self.token_config = TokenConfig(max_context_length=max_tokens)
        
        # 컴포넌트 초기화
        self.client = create_openai_client(self.client_config)
        self.prompt_engine = create_prompt_engine(self.prompt_config)
        self.token_manager = create_token_manager(self.token_config)
        self.conversation_generator = create_conversation_generator(
            self.client,
            self.prompt_engine,
            self.token_manager,
            self.conversation_config
        )
    
    async def generate_conversations(
        self,
        documents: List[Dict[str, Any]],
        mode: str = "llm_assisted",
        target_count: int = 1000,
        output_path: Optional[Path] = None
    ) -> List[Dict[str, Any]]:
        """
        문서 기반 대화 데이터셋을 생성합니다.
        
        Args:
            documents: 입력 문서 목록
            mode: 생성 모드 (llm_assisted 또는 rule_based)
            target_count: 목표 대화 수
            output_path: 출력 파일 경로 (선택적)
            
        Returns:
            생성된 대화 목록
        """
        # 생성 모드 설정
        generation_mode = GenerationMode.LLM_ASSISTED if mode == "llm_assisted" else GenerationMode.RULE_BASED
        self.conversation_config.generation_mode = generation_mode
        self.conversation_config.target_count = target_count
        
        # 대화 생성
        conversations = await self.conversation_generator.generate_conversations(
            documents=documents,
            target_count=target_count
        )
        
        # 결과 저장
        if output_path:
            save_conversations_to_json(conversations, output_path)
        
        return conversations
    
    async def test_connection(self) -> Dict[str, Any]:
        """
        API 연결을 테스트합니다.
        
        Returns:
            연결 상태 정보
        """
        try:
            await self.client.test_connection()
            return {
                "status": "success",
                "endpoint": self.client_config.endpoint,
                "model": self.client_config.model,
                "message": "API 연결 성공"
            }
        except Exception as e:
            return {
                "status": "error",
                "endpoint": self.client_config.endpoint,
                "model": self.client_config.model,
                "error": str(e),
                "message": "API 연결 실패"
            }


def create_openai_connector(
    endpoint: str = "http://123.37.28.120:9997/v1",
    model: str = "qwen2.5-vl-instruct",
    api_key: str = "your-api-key",
    max_tokens: int = 128000,
    temperature: float = 0.3,
    max_concurrent: int = 8,
    batch_size: int = 16
) -> OpenAIConnector:
    """
    OpenAI 연동 모듈을 생성합니다.
    
    Args:
        endpoint: API 엔드포인트
        model: 사용할 모델 이름
        api_key: API 키
        max_tokens: 최대 토큰 수
        temperature: 생성 온도
        max_concurrent: 최대 동시 요청 수
        batch_size: 배치 크기
        
    Returns:
        OpenAIConnector 인스턴스
    """
    return OpenAIConnector(
        endpoint=endpoint,
        model=model,
        api_key=api_key,
        max_tokens=max_tokens,
        temperature=temperature,
        max_concurrent=max_concurrent,
        batch_size=batch_size
    )


def create_openai_connector_from_env() -> OpenAIConnector:
    """
    환경변수에서 설정을 읽어 OpenAI 연동 모듈을 생성합니다.
    
    Returns:
        OpenAIConnector 인스턴스
    """
    import os
    
    endpoint = os.getenv("OPENAI_ENDPOINT", "http://123.37.28.120:9997/v1")
    model = os.getenv("OPENAI_MODEL", "qwen2.5-vl-instruct")
    api_key = os.getenv("OPENAI_API_KEY", "your-api-key")
    max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", "128000"))
    temperature = float(os.getenv("OPENAI_TEMPERATURE", "0.3"))
    max_concurrent = int(os.getenv("OPENAI_MAX_CONCURRENT", "8"))
    batch_size = int(os.getenv("OPENAI_BATCH_SIZE", "16"))
    
    return create_openai_connector(
        endpoint=endpoint,
        model=model,
        api_key=api_key,
        max_tokens=max_tokens,
        temperature=temperature,
        max_concurrent=max_concurrent,
        batch_size=batch_size
    )


# 모듈 로드 시 기본 로깅 설정
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


# 모듈 정보 출력
def print_module_info():
    """모듈 정보를 출력합니다."""
    print(f"OpenAI Connector Module v{__version__}")
    print(f"Author: {__author__}")
    print(f"Description: {__description__}")
    print(f"Available components:")
    print(f"  - Client: OpenAI compatible API connection")
    print(f"  - Prompt Engine: Template management")
    print(f"  - Conversation Generator: ShareGPT format generation")
    print(f"  - Token Manager: Token optimization")
    print(f"  - Utils: Common utility functions")

