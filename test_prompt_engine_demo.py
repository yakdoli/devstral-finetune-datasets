#!/usr/bin/env python3
"""
프롬프트 엔진 데모 및 실제 동작 테스트
"""

from openai_connector.prompt_engine import create_prompt_engine, PromptEngineConfig


def test_prompt_engine_demo():
    """프롬프트 엔진 데모"""
    print("=== Syncfusion WinForms 프롬프트 엔진 데모 ===\n")
    
    # 프롬프트 엔진 생성
    config = PromptEngineConfig(
        generation_mode="balanced",
        max_turns=6,
        batch_size=3
    )
    engine = create_prompt_engine(config)
    
    # 테스트 문서들
    test_documents = [
        {
            "component": "GridControl",
            "content": "Syncfusion WinForms GridControl은 강력한 데이터 그리드 컴포넌트로, 데이터 바인딩, 정렬, 필터링, 그룹화 기능을 제공합니다.",
            "difficulty": "Intermediate",
            "metadata": {"category": "DataGrid", "version": "20.4"}
        },
        {
            "component": "ChartControl",
            "content": "ChartControl은 2D/3D 차트를 생성할 수 있는 시각화 컴포넌트로, 다양한 차트 유형과 실시간 업데이트를 지원합니다.",
            "difficulty": "Advanced",
            "metadata": {"category": "Visualization", "version": "20.4"}
        },
        {
            "component": "TreeViewAdv",
            "content": "TreeViewAdv는 계층적 데이터를 표시하는 고급 트리뷰 컴포넌트로, 체크박스, 이미지, 드래그앤드롭을 지원합니다.",
            "difficulty": "Beginner",
            "metadata": {"category": "Navigation", "version": "20.4"}
        }
    ]
    
    print("1. 기본 대화 프롬프트 생성")
    print("-" * 50)
    
    for i, doc in enumerate(test_documents, 1):
        print(f"\n{i}. {doc['component']} 컴포넌트:")
        prompts = engine.generate_conversation_prompt(doc)
        
        for j, prompt in enumerate(prompts):
            print(f"  [{prompt['role']}]: {prompt['content'][:100]}...")
            if j >= 1:  # 처음 2개만 출력
                break
    
    print("\n\n2. 컨텍스트 기반 질문 생성")
    print("-" * 50)
    
    question_types = ["basic", "advanced", "troubleshooting", "performance"]
    
    for doc in test_documents[:2]:  # 처음 2개 문서만
        print(f"\n{doc['component']} 컴포넌트:")
        for q_type in question_types:
            question = engine.generate_contextual_question(doc, q_type)
            print(f"  [{q_type}]: {question}")
    
    print("\n\n3. 다중 턴 대화 생성")
    print("-" * 50)
    
    multi_turn = engine.create_multi_turn_conversation(test_documents[0], target_turns=4)
    print(f"\n{test_documents[0]['component']} 다중 턴 대화 ({len(multi_turn)}턴):")
    
    for i, turn in enumerate(multi_turn):
        print(f"  턴 {i+1} [{turn['role']}]: {turn['content'][:80]}...")
    
    print("\n\n4. 컴포넌트별 특화 템플릿")
    print("-" * 50)
    
    for doc in test_documents:
        component = doc['component']
        templates = engine.get_component_specific_templates(component)
        print(f"\n{component}:")
        print(f"  소개: {templates['intro']}")
        print(f"  주요 기능: {templates['key_features']}")
        print(f"  주의사항: {templates['common_issues']}")
    
    print("\n\n5. 프롬프트 품질 검증")
    print("-" * 50)
    
    test_prompts = [
        "GridControl의 DataSource 속성을 설정하는 C# 코드 예시를 알려주세요.",
        "ChartControl 사용법",
        "안녕하세요",
        "TreeViewAdv에서 노드를 동적으로 추가하고 삭제하는 방법과 관련 이벤트 처리에 대해 자세히 설명해주세요."
    ]
    
    for prompt in test_prompts:
        quality = engine.validate_prompt_quality(prompt)
        print(f"\n프롬프트: {prompt[:50]}...")
        print(f"  품질 점수: {quality['score']}/100")
        print(f"  고품질 여부: {quality['is_high_quality']}")
        print(f"  컴포넌트 포함: {quality['has_component']}")
        print(f"  코드 컨텍스트: {quality['has_code_context']}")
        print(f"  질문 형식: {quality['is_question_format']}")
    
    print("\n\n6. 배치 프롬프트 생성")
    print("-" * 50)
    
    batch_prompts = engine.create_batch_prompts(test_documents, mode="balanced")
    print(f"\n생성된 배치 프롬프트 수: {len(batch_prompts)}")
    
    for i, prompts in enumerate(batch_prompts):
        print(f"  배치 {i+1}: {len(prompts)}개 프롬프트")
        if prompts:
            user_prompt = next((p for p in prompts if p['role'] == 'user'), None)
            if user_prompt:
                print(f"    사용자 질문: {user_prompt['content'][:60]}...")
    
    print("\n\n7. 프롬프트 최적화")
    print("-" * 50)
    
    original_prompt = "GridControl에 대해 알려주세요."
    modes = ["balanced", "detailed", "concise"]
    
    for mode in modes:
        engine.config.generation_mode = mode
        optimized = engine.optimize_prompt(original_prompt, test_documents[0])
        print(f"\n[{mode} 모드]:")
        print(f"  원본: {original_prompt}")
        print(f"  최적화: {optimized[:100]}...")
    
    print("\n\n=== 데모 완료 ===")


if __name__ == "__main__":
    test_prompt_engine_demo()