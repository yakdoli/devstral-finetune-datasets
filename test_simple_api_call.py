#!/usr/bin/env python3
"""
간단한 API 호출 테스트
"""

import asyncio
from openai_connector import create_openai_client, OpenAIAPIClientConfig


async def test_simple_api_call():
    """간단한 API 호출 테스트"""
    config = OpenAIAPIClientConfig(
        endpoint="http://localhost:9997/v1",
        model="qwen2.5-vl-instruct",
        api_key="test-key",
        max_tokens=50,
        temperature=0.3,
        timeout=30
    )
    
    async with create_openai_client(config) as client:
        try:
            # 연결 테스트
            health = await client.test_connection()
            print(f"연결 상태: {health}")
            
            if health["status"] == "success":
                # 간단한 채팅 테스트
                messages = [
                    {"role": "user", "content": "안녕하세요"}
                ]
                
                print("API 호출 중...")
                response = await client.chat_completion(messages)
                print(f"응답: {response.content}")
                print(f"토큰 사용량: {response.tokens_used}")
                print(f"완료 이유: {response.finish_reason}")
                
        except Exception as e:
            print(f"오류 발생: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_simple_api_call())