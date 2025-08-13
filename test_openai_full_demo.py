#!/usr/bin/env python3
"""
OpenAI 커넥터 전체 데모
실제 API를 사용한 완전한 대화 생성 데모
"""

import asyncio
import json
from pathlib import Path
from datetime import datetime

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


async def demo_openai_connector():
    """OpenAI 커넥터 전체 데모"""
    print("=== OpenAI 커넥터 전체 데모 ===\n")
    
    # 1. 설정 생성
    print("1. 컴포넌트 설정 중...")
    
    client_config = OpenAIAPIClientConfig(
        endpoint="http://localhost:9997/v1",
        model="qwen2.5-vl-instruct",
        api_key="demo-key",
        max_tokens=200,  # 데모용 작은 값
        temperature=0.3,
        max_concurrent=2,
        timeout=30
    )
    
    prompt_config = PromptEngineConfig(
        generation_mode="balanced",
        max_turns=3,
        batch_size=2
    )
    
    token_config = TokenConfig(
        max_context_length=8192,
        max_request_tokens=1000,
        enable_optimization=True
    )
    
    conversation_config = ConversationConfig(
        generation_mode=GenerationMode.LLM_ASSISTED,
        target_count=3,
        max_turns=2,
        batch_size=2,
        max_concurrent=2,
        temperature=0.3,
        include_metadata=True
    )
    
    print("✓ 설정 완료")
    
    # 2. 컴포넌트 생성
    print("\n2. 컴포넌트 생성 중...")
    
    client = create_openai_client(client_config)
    prompt_engine = create_prompt_engine(prompt_config)
    token_manager = create_token_manager(token_config)
    conversation_generator = create_conversation_generator(
        client, prompt_engine, token_manager, conversation_config
    )
    
    print("✓ 컴포넌트 생성 완료")
    
    # 3. 테스트 문서 준비
    print("\n3. 테스트 문서 준비 중...")
    
    test_documents = [
        {
            'id': 'doc_grid_001',
            'component': 'GridControl',
            'title': 'GridControl 기본 사용법',
            'content': 'Syncfusion WinForms GridControl은 강력한 데이터 그리드 컴포넌트로, 데이터 바인딩, 정렬, 필터링 기능을 제공합니다.',
            'quality_score': 0.85,
            'difficulty': 'Beginner',
            'category': 'DataGrid'
        },
        {
            'id': 'doc_chart_001',
            'component': 'ChartControl',
            'title': 'ChartControl 차트 생성',
            'content': 'ChartControl을 사용하여 2D/3D 차트를 생성하고 실시간 데이터 업데이트를 구현할 수 있습니다.',
            'quality_score': 0.90,
            'difficulty': 'Intermediate',
            'category': 'Visualization'
        },
        {
            'id': 'doc_tree_001',
            'component': 'TreeViewAdv',
            'title': 'TreeViewAdv 고급 기능',
            'content': 'TreeViewAdv는 계층적 데이터 표시, 체크박스, 드래그앤드롭 등의 고급 기능을 지원합니다.',
            'quality_score': 0.88,
            'difficulty': 'Advanced',
            'category': 'Navigation'
        }
    ]
    
    print(f"✓ {len(test_documents)}개 문서 준비 완료")
    
    # 4. API 연결 테스트
    print("\n4. API 연결 테스트 중...")
    
    try:
        async with client as api_client:
            health = await api_client.test_connection()
            
            if health["status"] == "success":
                print("✓ API 연결 성공")
                print(f"  - 엔드포인트: {health['endpoint']}")
                print(f"  - 모델: {health['model']}")
            else:
                print("✗ API 연결 실패")
                print(f"  - 오류: {health.get('error', 'Unknown error')}")
                return
            
            # 5. 프롬프트 생성 및 품질 검증
            print("\n5. 프롬프트 생성 및 품질 검증...")
            
            for i, doc in enumerate(test_documents, 1):
                print(f"\n  문서 {i}: {doc['component']}")
                
                # 프롬프트 생성
                prompts = prompt_engine.generate_conversation_prompt(doc)
                print(f"    - 생성된 프롬프트 수: {len(prompts)}")
                
                # 토큰 수 예측
                estimated_tokens = token_manager.estimate_tokens(prompts)
                print(f"    - 예상 토큰 수: {estimated_tokens}")
                
                # 품질 검증
                if len(prompts) > 1:
                    user_prompt = prompts[1]['content']
                    quality = prompt_engine.validate_prompt_quality(user_prompt)
                    print(f"    - 품질 점수: {quality['score']}/100")
                    print(f"    - 고품질 여부: {quality['is_high_quality']}")
            
            # 6. 대화 생성
            print("\n6. 대화 생성 중...")
            
            start_time = datetime.now()
            conversations = await conversation_generator.generate_conversations(
                test_documents,
                target_count=2  # 데모용 작은 값
            )
            end_time = datetime.now()
            
            processing_time = (end_time - start_time).total_seconds()
            
            print(f"✓ 대화 생성 완료")
            print(f"  - 생성된 대화 수: {len(conversations)}")
            print(f"  - 처리 시간: {processing_time:.2f}초")
            
            # 7. 결과 분석
            print("\n7. 결과 분석...")
            
            if conversations:
                total_tokens = sum(conv.metadata.get('tokens_used', 0) for conv in conversations)
                avg_tokens = total_tokens / len(conversations)
                
                print(f"  - 총 토큰 사용량: {total_tokens}")
                print(f"  - 평균 토큰 사용량: {avg_tokens:.1f}")
                print(f"  - 처리 속도: {len(conversations) / processing_time:.2f} 대화/초")
                
                # 첫 번째 대화 상세 정보
                first_conv = conversations[0]
                print(f"\n  첫 번째 대화 상세:")
                print(f"    - ID: {first_conv.id}")
                print(f"    - 턴 수: {len(first_conv.conversations)}")
                print(f"    - 소스 문서: {first_conv.metadata.get('source_documents', [])}")
                
                # 대화 내용 출력
                for j, turn in enumerate(first_conv.conversations):
                    role = "사용자" if turn['from'] == 'human' else "어시스턴트"
                    content = turn['value'][:100] + "..." if len(turn['value']) > 100 else turn['value']
                    print(f"    - 턴 {j+1} [{role}]: {content}")
            
            # 8. 통계 정보
            print("\n8. 통계 정보...")
            
            # 클라이언트 통계
            client_stats = api_client.get_stats()
            print(f"  클라이언트:")
            print(f"    - 총 요청 수: {client_stats['total_requests']}")
            print(f"    - 성공한 요청 수: {client_stats['successful_requests']}")
            print(f"    - 성공률: {client_stats['success_rate']:.1f}%")
            
            # 토큰 매니저 통계
            token_stats = token_manager.get_stats()
            print(f"  토큰 매니저:")
            print(f"    - 현재 컨텍스트 토큰: {token_stats['current_context_tokens']}")
            print(f"    - 총 토큰 사용량: {token_stats['usage_stats']['total_tokens']}")
            
            # 대화 생성기 통계
            gen_stats = conversation_generator.get_stats()
            print(f"  대화 생성기:")
            print(f"    - 생성된 대화 수: {gen_stats['generated_count']}")
            print(f"    - 실패한 대화 수: {gen_stats['failed_count']}")
            print(f"    - 성공률: {gen_stats['success_rate']:.1f}%")
            
            # 9. 결과 저장
            print("\n9. 결과 저장 중...")
            
            if conversations:
                # ShareGPT 포맷으로 저장
                output_data = []
                for conv in conversations:
                    output_data.append({
                        "id": conv.id,
                        "conversations": conv.conversations,
                        "metadata": conv.metadata
                    })
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_file = f"demo_conversations_{timestamp}.json"
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(output_data, f, indent=2, ensure_ascii=False)
                
                print(f"✓ 결과 저장 완료: {output_file}")
                print(f"  - 파일 크기: {Path(output_file).stat().st_size} bytes")
            
            print("\n=== 데모 완료 ===")
            
    except Exception as e:
        print(f"✗ 데모 실행 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()


async def demo_component_features():
    """개별 컴포넌트 기능 데모"""
    print("\n=== 개별 컴포넌트 기능 데모 ===\n")
    
    # 프롬프트 엔진 데모
    print("1. 프롬프트 엔진 기능:")
    prompt_engine = create_prompt_engine()
    
    test_doc = {
        'component': 'GridControl',
        'content': 'GridControl 사용법',
        'difficulty': 'Intermediate'
    }
    
    # 다양한 질문 유형 생성
    question_types = ["basic", "advanced", "troubleshooting"]
    for q_type in question_types:
        question = prompt_engine.generate_contextual_question(test_doc, q_type)
        print(f"  [{q_type}]: {question}")
    
    # 토큰 매니저 데모
    print("\n2. 토큰 매니저 기능:")
    token_manager = create_token_manager(TokenConfig())
    
    test_messages = [
        {"role": "user", "content": "GridControl의 기본 사용법을 알려주세요."}
    ]
    
    estimated = token_manager.estimate_tokens(test_messages)
    can_process = token_manager.check_token_limit(estimated)
    remaining = token_manager.get_remaining_tokens()
    
    print(f"  - 예상 토큰 수: {estimated}")
    print(f"  - 처리 가능 여부: {can_process}")
    print(f"  - 남은 토큰 수: {remaining}")
    
    print("\n=== 컴포넌트 데모 완료 ===")


if __name__ == "__main__":
    # 전체 데모 실행
    asyncio.run(demo_openai_connector())
    
    # 개별 컴포넌트 데모 실행
    asyncio.run(demo_component_features())