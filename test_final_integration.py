#!/usr/bin/env python3
"""
최종 통합 테스트
OpenAI 커넥터 모듈의 모든 기능을 종합적으로 테스트
"""

import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path

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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def test_complete_workflow():
    """완전한 워크플로우 테스트"""
    print("=== OpenAI 커넥터 최종 통합 테스트 ===\n")
    
    # 1. 설정 및 초기화
    logger.info("1. 시스템 초기화 중...")
    
    client_config = OpenAIAPIClientConfig(
        endpoint="http://localhost:9997/v1",
        model="qwen2.5-vl-instruct",
        api_key="integration-test-key",
        max_tokens=150,
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
        max_request_tokens=2000,
        enable_optimization=True,
        track_usage_history=True
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
    
    # 컴포넌트 생성
    client = create_openai_client(client_config)
    prompt_engine = create_prompt_engine(prompt_config)
    token_manager = create_token_manager(token_config)
    conversation_generator = create_conversation_generator(
        client, prompt_engine, token_manager, conversation_config
    )
    
    logger.info("✓ 시스템 초기화 완료")
    
    # 2. 테스트 데이터 준비
    logger.info("2. 테스트 데이터 준비 중...")
    
    test_documents = [
        {
            'id': 'sf_grid_001',
            'component': 'GridControl',
            'title': 'GridControl 데이터 바인딩',
            'content': 'Syncfusion GridControl의 데이터 바인딩 기능을 사용하여 데이터베이스나 컬렉션의 데이터를 그리드에 표시할 수 있습니다.',
            'quality_score': 0.85,
            'difficulty': 'Intermediate',
            'category': 'DataBinding'
        },
        {
            'id': 'sf_chart_001',
            'component': 'ChartControl',
            'title': 'ChartControl 실시간 차트',
            'content': 'ChartControl을 사용하여 실시간으로 업데이트되는 차트를 생성하고 다양한 시각화 옵션을 적용할 수 있습니다.',
            'quality_score': 0.90,
            'difficulty': 'Advanced',
            'category': 'Visualization'
        },
        {
            'id': 'sf_tree_001',
            'component': 'TreeViewAdv',
            'title': 'TreeViewAdv 노드 관리',
            'content': 'TreeViewAdv에서 동적으로 노드를 추가, 삭제, 수정하고 체크박스 및 이미지를 활용하는 방법을 설명합니다.',
            'quality_score': 0.88,
            'difficulty': 'Beginner',
            'category': 'Navigation'
        }
    ]
    
    logger.info(f"✓ {len(test_documents)}개 테스트 문서 준비 완료")
    
    # 3. API 연결 및 기본 기능 테스트
    logger.info("3. API 연결 테스트 중...")
    
    async with client as api_client:
        try:
            # 연결 테스트
            health = await api_client.test_connection()
            
            if health["status"] != "success":
                logger.error(f"API 연결 실패: {health}")
                return False
            
            logger.info(f"✓ API 연결 성공 - {health['model']}")
            
            # 4. 프롬프트 엔진 테스트
            logger.info("4. 프롬프트 엔진 테스트 중...")
            
            prompt_test_results = []
            for doc in test_documents:
                # 프롬프트 생성
                prompts = prompt_engine.generate_conversation_prompt(doc)
                
                # 품질 검증
                if len(prompts) > 1:
                    user_prompt = prompts[1]['content']
                    quality = prompt_engine.validate_prompt_quality(user_prompt)
                    
                    prompt_test_results.append({
                        'component': doc['component'],
                        'prompt_count': len(prompts),
                        'quality_score': quality['score'],
                        'is_high_quality': quality['is_high_quality']
                    })
            
            avg_quality = sum(r['quality_score'] for r in prompt_test_results) / len(prompt_test_results)
            high_quality_count = sum(1 for r in prompt_test_results if r['is_high_quality'])
            
            logger.info(f"✓ 프롬프트 엔진 테스트 완료")
            logger.info(f"  - 평균 품질 점수: {avg_quality:.1f}/100")
            logger.info(f"  - 고품질 프롬프트: {high_quality_count}/{len(prompt_test_results)}")
            
            # 5. 토큰 관리자 테스트
            logger.info("5. 토큰 관리자 테스트 중...")
            
            token_test_results = []
            for doc in test_documents:
                prompts = prompt_engine.generate_conversation_prompt(doc)
                estimated_tokens = token_manager.estimate_tokens(prompts)
                can_process = token_manager.check_token_limit(estimated_tokens)
                
                token_test_results.append({
                    'component': doc['component'],
                    'estimated_tokens': estimated_tokens,
                    'can_process': can_process
                })
            
            total_estimated_tokens = sum(r['estimated_tokens'] for r in token_test_results)
            processable_count = sum(1 for r in token_test_results if r['can_process'])
            
            logger.info(f"✓ 토큰 관리자 테스트 완료")
            logger.info(f"  - 총 예상 토큰: {total_estimated_tokens}")
            logger.info(f"  - 처리 가능한 문서: {processable_count}/{len(token_test_results)}")
            
            # 6. 대화 생성 테스트
            logger.info("6. 대화 생성 테스트 중...")
            
            start_time = datetime.now()
            conversations = await conversation_generator.generate_conversations(
                test_documents,
                target_count=3
            )
            end_time = datetime.now()
            
            processing_time = (end_time - start_time).total_seconds()
            
            if conversations:
                logger.info(f"✓ 대화 생성 성공")
                logger.info(f"  - 생성된 대화 수: {len(conversations)}")
                logger.info(f"  - 처리 시간: {processing_time:.2f}초")
                logger.info(f"  - 처리 속도: {len(conversations) / processing_time:.2f} 대화/초")
                
                # 대화 품질 분석
                total_turns = sum(len(conv.conversations) for conv in conversations)
                total_tokens = sum(conv.metadata.get('tokens_used', 0) for conv in conversations)
                avg_tokens_per_conversation = total_tokens / len(conversations)
                avg_turns_per_conversation = total_turns / len(conversations)
                
                logger.info(f"  - 평균 턴 수: {avg_turns_per_conversation:.1f}")
                logger.info(f"  - 평균 토큰 사용량: {avg_tokens_per_conversation:.1f}")
                
                # 7. 결과 검증
                logger.info("7. 결과 검증 중...")
                
                validation_results = {
                    'valid_conversations': 0,
                    'valid_sharegpt_format': 0,
                    'valid_metadata': 0,
                    'component_coverage': set()
                }
                
                for conv in conversations:
                    # 기본 구조 검증
                    if hasattr(conv, 'id') and hasattr(conv, 'conversations') and hasattr(conv, 'metadata'):
                        validation_results['valid_conversations'] += 1
                    
                    # ShareGPT 포맷 검증
                    if all('from' in turn and 'value' in turn for turn in conv.conversations):
                        validation_results['valid_sharegpt_format'] += 1
                    
                    # 메타데이터 검증
                    required_metadata = ['source_documents', 'model', 'tokens_used', 'generation_mode']
                    if all(key in conv.metadata for key in required_metadata):
                        validation_results['valid_metadata'] += 1
                    
                    # 컴포넌트 커버리지
                    doc_info = conv.metadata.get('document_info', {})
                    component = doc_info.get('component')
                    if component:
                        validation_results['component_coverage'].add(component)
                
                logger.info(f"✓ 결과 검증 완료")
                logger.info(f"  - 유효한 대화: {validation_results['valid_conversations']}/{len(conversations)}")
                logger.info(f"  - ShareGPT 포맷 준수: {validation_results['valid_sharegpt_format']}/{len(conversations)}")
                logger.info(f"  - 메타데이터 완성도: {validation_results['valid_metadata']}/{len(conversations)}")
                logger.info(f"  - 컴포넌트 커버리지: {len(validation_results['component_coverage'])}/3")
                
                # 8. 결과 저장
                logger.info("8. 결과 저장 중...")
                
                output_data = {
                    'test_info': {
                        'timestamp': datetime.now().isoformat(),
                        'test_type': 'final_integration_test',
                        'total_documents': len(test_documents),
                        'target_conversations': 3,
                        'processing_time_seconds': processing_time
                    },
                    'conversations': [conv.to_dict() for conv in conversations],
                    'statistics': {
                        'prompt_engine': {
                            'avg_quality_score': avg_quality,
                            'high_quality_count': high_quality_count
                        },
                        'token_manager': {
                            'total_estimated_tokens': total_estimated_tokens,
                            'processable_documents': processable_count
                        },
                        'conversation_generator': {
                            **conversation_generator.get_stats(),
                            'config': {
                                **conversation_generator.get_stats()['config'],
                                'generation_mode': conversation_generator.get_stats()['config']['generation_mode'].value
                            }
                        },
                        'validation': validation_results
                    }
                }
                
                # 컴포넌트 커버리지를 리스트로 변환 (JSON 직렬화를 위해)
                output_data['statistics']['validation']['component_coverage'] = list(validation_results['component_coverage'])
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_file = f"final_integration_test_{timestamp}.json"
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(output_data, f, indent=2, ensure_ascii=False)
                
                logger.info(f"✓ 결과 저장 완료: {output_file}")
                logger.info(f"  - 파일 크기: {Path(output_file).stat().st_size} bytes")
                
                # 9. 최종 통계
                logger.info("9. 최종 통계 요약...")
                
                client_stats = api_client.get_stats()
                token_stats = token_manager.get_stats()
                
                logger.info(f"✓ 최종 통계:")
                logger.info(f"  API 클라이언트:")
                logger.info(f"    - 총 요청: {client_stats['total_requests']}")
                logger.info(f"    - 성공률: {client_stats['success_rate']:.1f}%")
                logger.info(f"  토큰 관리:")
                logger.info(f"    - 총 토큰 사용량: {token_stats['usage_stats']['total_tokens']}")
                logger.info(f"    - 평균 요청당 토큰: {token_stats['usage_stats']['avg_tokens_per_request']:.1f}")
                logger.info(f"  대화 생성:")
                logger.info(f"    - 성공률: {conversation_generator.get_stats()['success_rate']:.1f}%")
                logger.info(f"    - 총 토큰 사용량: {conversation_generator.get_stats()['total_tokens_used']}")
                
                return True
                
            else:
                logger.error("✗ 대화 생성 실패")
                return False
                
        except Exception as e:
            logger.error(f"테스트 실행 중 오류 발생: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False


async def main():
    """메인 함수"""
    print("OpenAI 커넥터 최종 통합 테스트를 시작합니다...\n")
    
    success = await test_complete_workflow()
    
    if success:
        print("\n🎉 모든 테스트가 성공적으로 완료되었습니다!")
        print("OpenAI 호환 API 연동 모듈이 정상적으로 구현되었습니다.")
    else:
        print("\n❌ 테스트 실행 중 문제가 발생했습니다.")
        print("로그를 확인하여 문제를 해결해주세요.")
    
    print("\n=== 테스트 완료 ===")


if __name__ == "__main__":
    asyncio.run(main())