#!/usr/bin/env python3
"""
대화 생성기 디버그 테스트
"""

import asyncio
import logging
from openai_connector import (
    create_openai_client,
    create_prompt_engine,
    create_token_manager,
    create_conversation_generator,
    OpenAIAPIClientConfig,
    PromptEngineConfig,
    TokenConfig,
    ConversationConfig,
    GenerationMode
)

# 로깅 설정
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def test_conversation_generation():
    """대화 생성 디버그 테스트"""
    print("=== 대화 생성 디버그 테스트 ===\n")
    
    # 설정
    client_config = OpenAIAPIClientConfig(
        endpoint="http://localhost:9997/v1",
        model="qwen2.5-vl-instruct",
        api_key="test-key",
        max_tokens=100,
        temperature=0.3,
        timeout=30
    )
    
    conversation_config = ConversationConfig(
        generation_mode=GenerationMode.LLM_ASSISTED,
        target_count=1,
        max_turns=2,
        batch_size=1,
        max_concurrent=1
    )
    
    # 컴포넌트 생성
    client = create_openai_client(client_config)
    prompt_engine = create_prompt_engine()
    token_manager = create_token_manager(TokenConfig())
    conversation_generator = create_conversation_generator(
        client, prompt_engine, token_manager, conversation_config
    )
    
    # 테스트 문서
    test_document = {
        'id': 'test_doc_001',
        'component': 'GridControl',
        'title': 'GridControl 기본 사용법',
        'content': 'GridControl 사용법에 대한 설명',
        'quality_score': 0.8
    }
    
    try:
        async with client as api_client:
            print("1. API 연결 테스트...")
            health = await api_client.test_connection()
            print(f"연결 상태: {health}")
            
            if health["status"] == "success":
                print("\n2. 단일 대화 생성 테스트...")
                
                # 대화 생성기에 클라이언트 설정
                conversation_generator.client = api_client
                
                # 단일 대화 생성
                conversation = await conversation_generator._generate_single_conversation(test_document)
                
                if conversation:
                    print("✓ 대화 생성 성공")
                    print(f"  - ID: {conversation.id}")
                    print(f"  - 턴 수: {len(conversation.conversations)}")
                    print(f"  - 메타데이터: {conversation.metadata}")
                    
                    for i, turn in enumerate(conversation.conversations):
                        print(f"  - 턴 {i+1} [{turn['from']}]: {turn['value'][:100]}...")
                else:
                    print("✗ 대화 생성 실패")
                
                print("\n3. 배치 대화 생성 테스트...")
                conversations = await conversation_generator.generate_conversations([test_document])
                
                print(f"생성된 대화 수: {len(conversations)}")
                
                # 통계 출력
                stats = conversation_generator.get_stats()
                print(f"통계: {stats}")
            
    except Exception as e:
        print(f"오류 발생: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_conversation_generation())