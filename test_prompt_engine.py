#!/usr/bin/env python3
"""
프롬프트 엔진 단위 테스트
"""

import pytest
from openai_connector.prompt_engine import (
    PromptEngine,
    PromptConfig,
    PromptEngineConfig,
    create_prompt_engine
)


class TestPromptEngineConfig:
    """프롬프트 엔진 설정 테스트"""
    
    def test_default_config(self):
        """기본 설정 테스트"""
        config = PromptEngineConfig()
        
        assert "Syncfusion WinForms 전문가" in config.system_prompt_template
        assert config.generation_mode == "balanced"
        assert config.max_turns == 10
        assert config.min_turns == 3
        assert config.max_generation_time == 300
        assert config.max_retries == 3
        assert config.batch_size == 10
    
    def test_custom_config(self):
        """커스텀 설정 테스트"""
        config = PromptEngineConfig(
            system_prompt_template="커스텀 시스템 프롬프트",
            generation_mode="detailed",
            max_turns=5,
            min_turns=2,
            batch_size=5
        )
        
        assert config.system_prompt_template == "커스텀 시스템 프롬프트"
        assert config.generation_mode == "detailed"
        assert config.max_turns == 5
        assert config.min_turns == 2
        assert config.batch_size == 5


class TestPromptEngine:
    """프롬프트 엔진 테스트"""
    
    def setup_method(self):
        """테스트 설정"""
        self.config = PromptEngineConfig()
        self.engine = PromptEngine(self.config)
        
        self.test_document = {
            "component": "GridControl",
            "content": "Syncfusion WinForms GridControl은 강력한 데이터 그리드 컴포넌트입니다.",
            "difficulty": "Intermediate",
            "metadata": {"category": "DataGrid", "version": "20.4"}
        }
    
    def test_engine_initialization(self):
        """엔진 초기화 테스트"""
        assert self.engine.config == self.config
        assert "system" in self.engine.templates
        assert "system_detailed" in self.engine.templates
        assert "question_generation" in self.engine.templates
        assert "answer_generation" in self.engine.templates
        assert "code_example" in self.engine.templates
    
    def test_generate_system_prompt(self):
        """시스템 프롬프트 생성 테스트"""
        system_prompt = self.engine.generate_system_prompt()
        
        assert isinstance(system_prompt, str)
        assert len(system_prompt) > 0
        assert "Syncfusion WinForms" in system_prompt
    
    def test_generate_question_prompt(self):
        """질문 생성 프롬프트 테스트"""
        content = "GridControl 사용법"
        question_prompt = self.engine.generate_question_prompt(content)
        
        assert isinstance(question_prompt, str)
        assert content in question_prompt
        assert "질문" in question_prompt
    
    def test_generate_answer_prompt(self):
        """답변 생성 프롬프트 테스트"""
        content = "GridControl 설정 방법"
        answer_prompt = self.engine.generate_answer_prompt(content)
        
        assert isinstance(answer_prompt, str)
        assert content in answer_prompt
        assert "답변" in answer_prompt
    
    def test_generate_code_example_prompt(self):
        """코드 예시 생성 프롬프트 테스트"""
        requirement = "GridControl 초기화"
        code_prompt = self.engine.generate_code_example_prompt(requirement)
        
        assert isinstance(code_prompt, str)
        assert requirement in code_prompt
        assert "코드" in code_prompt
    
    def test_generate_conversation_prompt(self):
        """대화 프롬프트 생성 테스트"""
        prompts = self.engine.generate_conversation_prompt(self.test_document)
        
        assert isinstance(prompts, list)
        assert len(prompts) >= 2  # 최소 시스템 + 사용자 프롬프트
        
        # 첫 번째는 시스템 프롬프트여야 함
        assert prompts[0]["role"] == "system"
        assert "Syncfusion WinForms" in prompts[0]["content"]
        
        # 두 번째는 사용자 프롬프트여야 함
        assert prompts[1]["role"] == "user"
        assert "GridControl" in prompts[1]["content"]
    
    def test_generate_conversation_prompt_with_empty_component(self):
        """컴포넌트가 비어있는 경우 대화 프롬프트 생성 테스트"""
        document = {
            "component": None,
            "content": "테스트 내용"
        }
        
        prompts = self.engine.generate_conversation_prompt(document)
        
        assert isinstance(prompts, list)
        assert len(prompts) >= 2
        # 기본값으로 GridControl이 사용되어야 함
        assert "GridControl" in prompts[1]["content"]
    
    def test_generate_contextual_question(self):
        """컨텍스트 기반 질문 생성 테스트"""
        question_types = ["basic", "advanced", "troubleshooting", "performance", "integration"]
        
        for question_type in question_types:
            question = self.engine.generate_contextual_question(self.test_document, question_type)
            
            assert isinstance(question, str)
            assert len(question) > 0
            assert "GridControl" in question
    
    def test_generate_contextual_answer(self):
        """컨텍스트 기반 답변 생성 프롬프트 테스트"""
        question = "GridControl의 기본 사용법을 알려주세요."
        answer_prompt = self.engine.generate_contextual_answer(self.test_document, question, "basic")
        
        assert isinstance(answer_prompt, str)
        assert "GridControl" in answer_prompt
        assert "답변" in answer_prompt
    
    def test_generate_follow_up_question(self):
        """후속 질문 생성 테스트"""
        previous_qa = {
            "question": "GridControl의 기본 사용법을 알려주세요.",
            "answer": "GridControl을 사용하려면 먼저 DataSource를 설정해야 합니다."
        }
        
        follow_up = self.engine.generate_follow_up_question(previous_qa, self.test_document)
        
        assert isinstance(follow_up, str)
        assert "GridControl" in follow_up
    
    def test_create_multi_turn_conversation(self):
        """다중 턴 대화 생성 테스트"""
        conversation = self.engine.create_multi_turn_conversation(self.test_document, target_turns=6)
        
        assert isinstance(conversation, list)
        assert len(conversation) >= 3  # 시스템 + 최소 1턴 대화
        
        # 첫 번째는 시스템 프롬프트
        assert conversation[0]["role"] == "system"
        
        # 이후 user/assistant가 번갈아 나와야 함
        for i in range(1, len(conversation)):
            if i % 2 == 1:  # 홀수 인덱스는 user
                assert conversation[i]["role"] == "user"
            else:  # 짝수 인덱스는 assistant
                assert conversation[i]["role"] == "assistant"
    
    def test_create_batch_prompts(self):
        """배치 프롬프트 생성 테스트"""
        documents = [self.test_document] * 3
        batch_prompts = self.engine.create_batch_prompts(documents, mode="balanced")
        
        assert isinstance(batch_prompts, list)
        assert len(batch_prompts) == 3
        
        for prompts in batch_prompts:
            assert isinstance(prompts, list)
            assert len(prompts) >= 2
    
    def test_create_batch_prompts_multi_turn(self):
        """다중 턴 배치 프롬프트 생성 테스트"""
        documents = [self.test_document] * 2
        batch_prompts = self.engine.create_batch_prompts(documents, target_turns=4, mode="multi_turn")
        
        assert isinstance(batch_prompts, list)
        assert len(batch_prompts) == 2
        
        for prompts in batch_prompts:
            assert isinstance(prompts, list)
            assert len(prompts) >= 3  # 시스템 + 최소 1턴
    
    def test_get_component_specific_templates(self):
        """컴포넌트별 특화 템플릿 테스트"""
        components = ["GridControl", "ChartControl", "TreeViewAdv", "UnknownComponent"]
        
        for component in components:
            templates = self.engine.get_component_specific_templates(component)
            
            assert isinstance(templates, dict)
            assert "intro" in templates
            assert "key_features" in templates
            assert "common_issues" in templates
            
            # 알려진 컴포넌트는 특화된 내용이 있어야 함
            if component in ["GridControl", "ChartControl", "TreeViewAdv"]:
                assert component.lower() in templates["intro"].lower()
    
    def test_optimize_prompt(self):
        """프롬프트 최적화 테스트"""
        original_prompt = "GridControl에 대해 알려주세요."
        
        # balanced 모드
        self.engine.config.generation_mode = "balanced"
        optimized = self.engine.optimize_prompt(original_prompt, self.test_document)
        assert isinstance(optimized, str)
        
        # detailed 모드
        self.engine.config.generation_mode = "detailed"
        detailed = self.engine.optimize_prompt(original_prompt, self.test_document)
        assert "상세하게" in detailed or "코드 예시" in detailed
        
        # concise 모드
        self.engine.config.generation_mode = "concise"
        concise = self.engine.optimize_prompt(original_prompt, self.test_document)
        assert "간결하고" in concise or "핵심적인" in concise
    
    def test_validate_prompt_quality(self):
        """프롬프트 품질 검증 테스트"""
        # 고품질 프롬프트
        high_quality_prompt = "GridControl의 DataSource 속성을 설정하는 C# 코드 예시를 알려주세요."
        quality = self.engine.validate_prompt_quality(high_quality_prompt)
        
        assert isinstance(quality, dict)
        assert "score" in quality
        assert "is_high_quality" in quality
        assert quality["has_component"] is True
        assert quality["has_code_context"] is True
        assert quality["is_question_format"] is True
        
        # 저품질 프롬프트
        low_quality_prompt = "안녕"
        low_quality = self.engine.validate_prompt_quality(low_quality_prompt)
        
        assert low_quality["score"] < quality["score"]
        assert low_quality["is_high_quality"] is False


class TestCreatePromptEngine:
    """프롬프트 엔진 팩토리 함수 테스트"""
    
    def test_create_prompt_engine_default(self):
        """기본 설정으로 프롬프트 엔진 생성 테스트"""
        engine = create_prompt_engine()
        
        assert isinstance(engine, PromptEngine)
        assert isinstance(engine.config, PromptEngineConfig)
    
    def test_create_prompt_engine_custom(self):
        """커스텀 설정으로 프롬프트 엔진 생성 테스트"""
        config = PromptEngineConfig(generation_mode="detailed", max_turns=5)
        engine = create_prompt_engine(config)
        
        assert isinstance(engine, PromptEngine)
        assert engine.config == config
        assert engine.config.generation_mode == "detailed"
        assert engine.config.max_turns == 5


# 통합 테스트
class TestPromptEngineIntegration:
    """프롬프트 엔진 통합 테스트"""
    
    def test_full_workflow(self):
        """전체 워크플로우 테스트"""
        config = PromptEngineConfig(
            generation_mode="balanced",
            max_turns=4,
            batch_size=2
        )
        engine = create_prompt_engine(config)
        
        # 테스트 문서들
        documents = [
            {
                "component": "GridControl",
                "content": "GridControl 기본 사용법",
                "difficulty": "Beginner"
            },
            {
                "component": "ChartControl", 
                "content": "ChartControl 차트 생성",
                "difficulty": "Intermediate"
            }
        ]
        
        # 배치 프롬프트 생성
        batch_prompts = engine.create_batch_prompts(documents, mode="balanced")
        
        assert len(batch_prompts) == 2
        
        # 각 프롬프트 품질 검증
        for prompts in batch_prompts:
            assert len(prompts) >= 2
            
            # 시스템 프롬프트 검증
            system_prompt = prompts[0]
            assert system_prompt["role"] == "system"
            assert "Syncfusion WinForms" in system_prompt["content"]
            
            # 사용자 프롬프트 검증
            user_prompt = prompts[1]
            assert user_prompt["role"] == "user"
            
            # 품질 검증
            quality = engine.validate_prompt_quality(user_prompt["content"])
            assert quality["score"] > 0
    
    def test_component_specific_generation(self):
        """컴포넌트별 특화 생성 테스트"""
        engine = create_prompt_engine()
        
        components = ["GridControl", "ChartControl", "TreeViewAdv"]
        
        for component in components:
            document = {
                "component": component,
                "content": f"{component} 사용법",
                "difficulty": "Intermediate"
            }
            
            # 대화 프롬프트 생성
            prompts = engine.generate_conversation_prompt(document)
            
            # 컴포넌트 이름이 포함되어야 함
            user_content = prompts[1]["content"]
            assert component in user_content
            
            # 컴포넌트별 템플릿 확인
            templates = engine.get_component_specific_templates(component)
            assert component.lower() in templates["intro"].lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])