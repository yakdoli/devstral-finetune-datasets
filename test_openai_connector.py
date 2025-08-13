#!/usr/bin/env python3
"""
OpenAI 연동 모듈 통합 테스트 스크립트
"""

import asyncio
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

# OpenAI 연동 모듈 임포트
from openai_connector import (
    create_openai_connector,
    create_openai_connector_from_env,
    OpenAIConnector
)
from openai_connector.client import OpenAIAPIClientConfig, OpenAIClient
from openai_connector.prompt_engine import PromptEngine, PromptConfig
from openai_connector.conversation_generator import ConversationGenerator, ConversationConfig
from openai_connector.token_manager import TokenManager, TokenConfig
from openai_connector.utils import setup_logging, save_conversations_to_json

# 로깅 설정
logger = setup_logging("INFO", "test_openai_connector.log")


def create_test_documents() -> List[Dict[str, Any]]:
    """테스트용 문서 데이터를 생성합니다."""
    return [
        {
            'id': 'doc_001',
            'component': 'GridControl',
            'title': 'GridControl 기본 사용법',
            'content': '''GridControl은 Syncfusion WinForms의 강력한 데이터 그리드 컴포넌트입니다.
주요 기능:
- 데이터 표시 및 편집
- 정렬 및 필터링
- 커스텀 컬럼 설정
- 테마 지원
- 가상 모드 지원

기본 사용법:
1. 네임스페이스 추가
2. 컴포넌트 생성
3. DataSource 설정
4. 컬럼 구성''',
            'code_example': '''var gridControl = new GridControl();
gridControl.DataSource = yourDataSource;
gridControl.Columns.Add(new GridColumn() { 
    MappingName = "ID", 
    HeaderText = "ID" 
});''',
            'quality_score': 0.9,
            'document_type': 'user_guide'
        },
        {
            'id': 'doc_002',
            'component': 'GridControl',
            'title': 'GridControl 고급 기능',
            'content': '''GridControl의 고급 기능들을 활용하면 더욱 강력한 애플리케이션을 개발할 수 있습니다.

고급 기능:
- 커스텀 렌더링
- 이벤트 처리
- 데이터 바인딩
- 성능 최적화
- 템플릿 컬럼

성능 최적화 팁:
- 가상 모드 사용
- 페이지네이션 적용
- 백그라운드 스레드 활용
- 캐싱 전략''',
            'code_example': '''// 가상 모드 설정
gridControl.VirtualMode = true;
gridControl.RowCount = 1000000;

// 커스텀 렌더러
gridControl.CellRenderers.Add(new CustomCellRenderer());''',
            'quality_score': 0.85,
            'document_type': 'advanced_guide'
        },
        {
            'id': 'doc_003',
            'component': 'GridControl',
            'title': 'GridControl 오류 해결',
            'content': '''GridControl 사용 시 발생할 수 있는 주요 문제들과 해결책입니다.

주요 오류 및 해결책:
1. 데이터 표시 안됨
   - DataSource 확인
   - AutoGenerateColumns 설정
   - 데이터 유효성 검사

2. 성능 저하
   - 가상 모드 활성화
   - 불필요한 이벤트 제거
   - 캐싱 적용

3. UI 반응성 문제
   - 백그라운드 작업 분리
   - Progress 표시
   - 비동기 처리''',
            'quality_score': 0.8,
            'document_type': 'troubleshooting'
        }
    ]


async def test_basic_functionality():
    """기본 기능 테스트"""
    print("\n=== 기본 기능 테스트 ===")
    
    try:
        # 테스트 문서 생성
        test_documents = create_test_documents()
        print(f"테스트 문서 수: {len(test_documents)}")
        
        # OpenAI 연동 모듈 생성
        connector = create_openai_connector(
            endpoint="http://123.37.28.120:9997/v1",
            model="qwen2.5-vl-instruct",
            api_key="test-key",
            max_tokens=1000,
            temperature=0.3,
            max_concurrent=2,
            batch_size=2
        )
        
        # 연결 테스트
        print("API 연결 테스트...")
        health = await connector.test_connection()
        print(f"연결 상태: {health['status']}")
        
        if health['status'] == 'success':
            # 대화 생성 테스트 (소규모)
            print("대화 생성 테스트...")
            conversations = await connector.generate_conversations(
                documents=test_documents,
                mode="llm_assisted",
                target_count=3,
                output_path="test_conversations.json"
            )
            
            print(f"생성된 대화 수: {len(conversations)}")
            
            # 생성된 대화 확인
            for i, conv in enumerate(conversations):
                print(f"\n대화 {i+1}:")
                print(f"ID: {conv.id}")
                print(f"턴 수: {len(conv.conversations)}")
                print(f"메타데이터: {conv.metadata}")
                
                # 대화 내용 간략히 표시
                for j, turn in enumerate(conv.conversations[:2]):  # 첫 2턴만 표시
                    print(f"  {turn['from']}: {turn['value'][:50]}...")
            
            # 통계 정보 출력
            stats = connector.conversation_generator.get_stats()
            print(f"\n통계 정보:")
            print(f"  - 성공률: {stats['success_rate']:.1f}%")
            print(f"  - 총 토큰 사용량: {stats['total_tokens_used']}")
            print(f"  - 생성된 대화 수: {stats['generated_count']}")
            print(f"  - 실패한 대화 수: {stats['failed_count']}")
            
            return True
        else:
            print(f"API 연결 실패: {health['error']}")
            return False
            
    except Exception as e:
        print(f"테스트 중 오류 발생: {e}")
        logger.error(f"기본 기능 테스트 실패: {e}")
        return False


async def test_component_isolation():
    """컴포넌트 분리 테스트"""
    print("\n=== 컴포넌트 분리 테스트 ===")
    
    try:
        # 개별 컴포넌트 생성 및 테스트
        client_config = OpenAIAPIClientConfig(
            endpoint="http://123.37.28.120:9997/v1",
            model="qwen2.5-vl-instruct",
            api_key="test-key",
            max_tokens=1000
        )
        
        prompt_config = PromptConfig(
            max_turns=3,
            include_examples=True,
            example_count=1
        )
        
        token_config = TokenConfig(max_context_length=128000)
        
        conversation_config = ConversationConfig(
            generation_mode="llm_assisted",
            target_count=2,
            max_turns=3,
            batch_size=1
        )
        
        # 컴포넌트 생성
        client = OpenAIClient(client_config)
        prompt_engine = PromptEngine(prompt_config)
        token_manager = TokenManager(token_config)
        
        print("컴포넌트 생성 완료")
        
        # 프롬프트 엔진 테스트
        print("프롬프트 엔진 테스트...")
        test_document = {
            'component': 'GridControl',
            'title': '테스트 문서',
            'content': '테스트 콘텐츠'
        }
        
        prompt = prompt_engine.create_conversation_prompt(test_document, target_turns=2)
        print(f"생성된 프롬프트 턴 수: {len(prompt)}")
        
        # 토큰 관리자 테스트
        print("토큰 관리자 테스트...")
        estimated_tokens = token_manager.estimate_tokens(prompt)
        print(f"예측된 토큰 수: {estimated_tokens}")
        
        can_process = token_manager.check_token_limit(estimated_tokens)
        print(f"처리 가능 여부: {can_process}")
        
        return True
        
    except Exception as e:
        print(f"컴포넌트 분리 테스트 중 오류 발생: {e}")
        logger.error(f"컴포넌트 분리 테스트 실패: {e}")
        return False


async def test_error_handling():
    """오류 처리 테스트"""
    print("\n=== 오류 처리 테스트 ===")
    
    try:
        # 잘못된 설정으로 테스트
        connector = create_openai_connector(
            endpoint="http://invalid-endpoint:9997/v1",
            model="invalid-model",
            api_key="invalid-key"
        )
        
        # 연결 테스트 (예상된 오류)
        health = await connector.test_connection()
        print(f"예상된 연결 실패: {health['status']}")
        
        # 잘못된 형식의 문서로 테스트
        invalid_documents = [
            {
                'id': 'invalid_doc',
                'title': '잘못된 문서',
                # 필드 누락
            }
        ]
        
        # 대화 생성 시도 (예상된 오류)
        conversations = await connector.generate_conversations(
            documents=invalid_documents,
            mode="llm_assisted",
            target_count=1
        )
        
        print(f"오류 처리 결과: {len(conversations)}개 대화 생성")
        
        return True
        
    except Exception as e:
        print(f"오류 처리 테스트 중 예상치 못한 오류 발생: {e}")
        logger.error(f"오류 처리 테스트 실패: {e}")
        return False


async def test_performance():
    """성능 테스트"""
    print("\n=== 성능 테스트 ===")
    
    try:
        # 대량 문서 생성
        large_documents = []
        for i in range(10):
            large_documents.append({
                'id': f'perf_doc_{i:03d}',
                'component': 'GridControl',
                'title': f'성능 테스트 문서 {i+1}',
                'content': f'이것은 성능 테스트용 문서입니다. 문서 번호: {i+1}\n' * 50,
                'quality_score': 0.8
            })
        
        print(f"성능 테스트용 문서 수: {len(large_documents)}")
        
        # 성능 측정용 커넥터 생성
        connector = create_openai_connector(
            endpoint="http://123.37.28.120:9997/v1",
            model="qwen2.5-vl-instruct",
            api_key="test-key",
            max_tokens=1000,
            temperature=0.3,
            max_concurrent=4,
            batch_size=4
        )
        
        # 대화 생성 성능 측정
        import time
        start_time = time.time()
        
        conversations = await connector.generate_conversations(
            documents=large_documents,
            mode="llm_assisted",
            target_count=10
        )
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        print(f"성능 테스트 결과:")
        print(f"  - 처리 시간: {processing_time:.2f}초")
        print(f"  - 생성된 대화 수: {len(conversations)}")
        print(f"  - 처리 속도: {len(conversations) / processing_time:.1f} 대화/초")
        
        # 통계 정보 확인
        stats = connector.conversation_generator.get_stats()
        print(f"  - 성공률: {stats['success_rate']:.1f}%")
        print(f"  - 총 토큰 사용량: {stats['total_tokens_used']}")
        
        return True
        
    except Exception as e:
        print(f"성능 테스트 중 오류 발생: {e}")
        logger.error(f"성능 테스트 실패: {e}")
        return False


async def test_integration_with_existing_modules():
    """기존 모듈과의 연동 테스트"""
    print("\n=== 기존 모듈과의 연동 테스트 ===")
    
    try:
        # 기존 MD 처리 모듈과의 연동 테스트 (가상)
        print("MD 처리 모듈 연동 테스트...")
        
        # 가상의 MD 처리 결과
        md_documents = [
            {
                'id': 'md_doc_001',
                'component': 'GridControl',
                'title': 'MD 처리된 문서',
                'content': 'MD 처리된 콘텐츠...',
                'source_file': 'test.md',
                'processed_at': '2024-01-01T00:00:00'
            }
        ]
        
        # 가상의 Qdrant 연동 모듈과의 연동 테스트
        print("Qdrant 연동 모듈 연동 테스트...")
        
        # 가상의 검색 결과
        qdrant_results = [
            {
                'id': 'qdrant_doc_001',
                'component': 'GridControl',
                'title': 'Qdrant 검색된 문서',
                'content': 'Qdrant 검색된 콘텐츠...',
                'score': 0.95,
                'metadata': {'source': 'qdrant'}
            }
        ]
        
        # 통합 문서 생성
        integrated_documents = md_documents + qdrant_results
        print(f"통합 문서 수: {len(integrated_documents)}")
        
        # OpenAI 연동 모듈로 대화 생성
        connector = create_openai_connector()
        
        conversations = await connector.generate_conversations(
            documents=integrated_documents,
            mode="llm_assisted",
            target_count=5
        )
        
        print(f"통합 대화 생성 결과: {len(conversations)}개 대화")
        
        # 결과 저장
        save_conversations_to_json(conversations, "integrated_test_conversations.json")
        
        return True
        
    except Exception as e:
        print(f"연동 테스트 중 오류 발생: {e}")
        logger.error(f"연동 테스트 실패: {e}")
        return False


async def main():
    """메인 테스트 함수"""
    print("OpenAI 연동 모듈 통합 테스트 시작")
    print("=" * 50)
    
    # 테스트 결과 저장
    test_results = {}
    
    # 기본 기능 테스트
    test_results['basic_functionality'] = await test_basic_functionality()
    
    # 컴포넌트 분리 테스트
    test_results['component_isolation'] = await test_component_isolation()
    
    # 오류 처리 테스트
    test_results['error_handling'] = await test_error_handling()
    
    # 성능 테스트
    test_results['performance'] = await test_performance()
    
    # 연동 테스트
    test_results['integration'] = await test_integration_with_existing_modules()
    
    # 최종 결과 요약
    print("\n" + "=" * 50)
    print("테스트 결과 요약")
    print("=" * 50)
    
    passed_tests = 0
    total_tests = len(test_results)
    
    for test_name, result in test_results.items():
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed_tests += 1
    
    print(f"\n전체 결과: {passed_tests}/{total_tests} 테스트 통과")
    print(f"통과율: {(passed_tests / total_tests * 100):.1f}%")
    
    # 테스트 결과 저장
    with open("test_results.json", "w", encoding="utf-8") as f:
        json.dump(test_results, f, indent=2, ensure_ascii=False)
    
    print("\n테스트 결과가 test_results.json 파일에 저장되었습니다.")
    
    # 성공 여부 반환
    return passed_tests == total_tests


if __name__ == "__main__":
    # 테스트 실행
    success = asyncio.run(main())
    
    if success:
        print("\n모든 테스트를 성공적으로 완료했습니다!")
        exit(0)
    else:
        print("\n일부 테스트가 실패했습니다.")
        exit(1)