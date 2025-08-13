#!/usr/bin/env python3
"""
실제 API 연결 테스트
"""

import asyncio
from openai_connector.client import OpenAIClient, OpenAIAPIClientConfig


async def test_real_connection():
    """실제 API 연결 테스트"""
    config = OpenAIAPIClientConfig(
        endpoint="http://localhost:9997/v1",
        model="qwen2.5-vl-instruct",
        api_key="test-key",
        max_tokens=100,
        temperature=0.3,
        timeout=30
    )
    
    print("=== OpenAI 호환 API 연결 테스트 ===")
    print(f"엔드포인트: {config.endpoint}")
    print(f"모델: {config.model}")
    
    async with OpenAIClient(config) as client:
        try:
            # 1. 연결 테스트
            print("\n1. 연결 테스트 중...")
            health = await client.test_connection()
            print(f"연결 상태: {health}")
            
            if health["status"] == "success":
                # 2. 간단한 채팅 테스트
                print("\n2. 채팅 완성 테스트 중...")
                messages = [
                    {"role": "system", "content": "당신은 도움이 되는 AI 어시스턴트입니다."},
                    {"role": "user", "content": "안녕하세요! 간단한 인사말을 해주세요."}
                ]
                
                response = await client.chat_completion(messages, max_tokens=50)
                print(f"응답: {response.content}")
                print(f"사용된 토큰: {response.tokens_used}")
                print(f"완료 이유: {response.finish_reason}")
                
                # 3. Syncfusion 관련 테스트
                print("\n3. Syncfusion WinForms 관련 테스트 중...")
                syncfusion_messages = [
                    {"role": "system", "content": "당신은 Syncfusion WinForms 전문가입니다."},
                    {"role": "user", "content": "GridControl의 기본 사용법을 간단히 설명해주세요."}
                ]
                
                syncfusion_response = await client.chat_completion(syncfusion_messages, max_tokens=100)
                print(f"Syncfusion 응답: {syncfusion_response.content}")
                print(f"사용된 토큰: {syncfusion_response.tokens_used}")
                
                # 4. 통계 정보
                print("\n4. 클라이언트 통계:")
                stats = client.get_stats()
                print(f"총 요청 수: {stats['total_requests']}")
                print(f"성공한 요청 수: {stats['successful_requests']}")
                print(f"실패한 요청 수: {stats['failed_requests']}")
                print(f"성공률: {stats['success_rate']:.1f}%")
                
            else:
                print("API 연결에 실패했습니다.")
                
        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


if __name__ == "__main__":
    asyncio.run(test_real_connection())