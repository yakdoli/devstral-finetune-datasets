#!/usr/bin/env python3
"""
로컬 LLM 커넥터 모듈

로컬에서 실행되는 언어 모델과의 통신을 담당합니다.
기존 OpenAI 호환 API를 지원하면서 로컬 LLM 특성에 맞게 최적화되었습니다.
"""

from .client import LocalLLMClient, LocalLLMClientConfig, APIResponse, RateLimiter, create_local_llm_client
from .conversation_generator import ConversationGenerator, ConversationConfig, Conversation, create_conversation_generator
from .prompt_engine import PromptEngine, PromptEngineConfig, create_prompt_engine
from .token_manager import TokenManager, TokenConfig, create_token_manager
from .hybrid_searcher import HybridSearcher, HybridSearchConfig, create_hybrid_searcher

__version__ = "1.0.0"
__author__ = "Devstral Team"
__email__ = "team@devstral.com"

__all__ = [
    # 클라이언트
    "LocalLLMClient",
    "LocalLLMClientConfig", 
    "APIResponse",
    "RateLimiter",
    "create_local_llm_client",
    
    # 대화 생성기
    "ConversationGenerator",
    "ConversationConfig",
    "Conversation",
    "create_conversation_generator",
    
    # 프롬프트 엔진
    "PromptEngine",
    "PromptEngineConfig",
    "create_prompt_engine",
    
    # 토큰 관리자
    "TokenManager",
    "TokenConfig",
    "create_token_manager",
    
    # 하이브리드 검색기
    "HybridSearcher",
    "HybridSearchConfig",
    "create_hybrid_searcher",
    
    # 버전 정보
    "__version__",
    "__author__",
    "__email__"
]


def create_local_llm_connector(config_dict: dict = None):
    """
    로컬 LLM 커넥터 팩토리 함수
    
    Args:
        config_dict: 설정 딕셔너리
        
    Returns:
        로컬 LLM 커넥터 인스턴스
    """
    try:
        from config.config import load_config
        
        # 설정 로드
        if config_dict:
            # 딕셔너리에서 설정 생성
            from config.config import LocalLLMConfig
            config = LocalLLMConfig(**config_dict)
        else:
            # YAML 파일에서 설정 로드
            config = load_config("config.yaml").local_llm
        
        # 클라이언트 생성
        client = create_local_llm_client(config)
        
        # 프롬프트 엔진 생성
        prompt_engine_config = PromptEngineConfig(
            temperature=config.temperature,
            max_prompt_length=config.max_tokens // 2
        )
        prompt_engine = create_prompt_engine(prompt_engine_config)
        
        # 토큰 관리자 생성
        token_config = TokenConfig(
            max_prompt_tokens=config.max_tokens // 2,
            max_response_tokens=config.max_tokens // 2,
            total_token_limit=config.max_tokens
        )
        token_manager = create_token_manager(token_config)
        
        # 하이브리드 검색기 생성
        hybrid_search_config = HybridSearchConfig(
            max_results=10,
            weights={"context7": 0.3, "local": 0.3, "qdrant": 0.4}
        )
        hybrid_searcher = create_hybrid_searcher(hybrid_search_config)
        
        # 대화 생성기 생성
        conversation_config = ConversationConfig(
            max_conversations_per_document=3,
            min_conversation_length=50,
            max_conversation_length=config.max_tokens // 4,
            enable_quality_filter=True,
            quality_threshold=0.7,
            enable_hybrid_search=True,
            hybrid_search_weight=0.3
        )
        
        conversation_generator = create_conversation_generator(
            client=client,
            prompt_engine=prompt_engine,
            token_manager=token_manager,
            config=conversation_config,
            hybrid_searcher=hybrid_searcher
        )
        
        return {
            "client": client,
            "prompt_engine": prompt_engine,
            "token_manager": token_manager,
            "hybrid_searcher": hybrid_searcher,
            "conversation_generator": conversation_generator,
            "config": config
        }
        
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"로컬 LLM 커넥터 생성 실패: {str(e)}")
        raise


def test_connection(config_dict: dict = None) -> dict:
    """
    로컬 LLM 연결 테스트
    
    Args:
        config_dict: 설정 딕셔너리
        
    Returns:
        연결 테스트 결과
    """
    try:
        # 설정 로드
        if config_dict:
            from config.config import LocalLLMConfig
            config = LocalLLMConfig(**config_dict)
        else:
            from config.config import load_config
            config = load_config("config.yaml").local_llm
        
        # 클라이언트 생성 및 연결 테스트
        client = create_local_llm_client(config)
        
        async def _test():
            async with client:
                return await client.test_connection()
        
        import asyncio
        result = asyncio.run(_test())
        
        return {
            "status": "success",
            "message": "로컬 LLM 연결 성공",
            "config": config,
            "result": result
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"로컬 LLM 연결 실패: {str(e)}",
            "config": config_dict or {},
            "result": None
        }


# 모듈 로드 시 기본 설정으로 테스트 실행
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    
    # 연결 테스트
    test_result = test_connection()
    print(f"연결 테스트 결과: {test_result}")