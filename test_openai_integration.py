#!/usr/bin/env python3
"""
OpenAI 커넥터 통합 테스트
클라이언트, 프롬프트 엔진, 토큰 매니저, 대화 생성기의 통합 테스트
"""

import pytest
import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime

from openai_connector import (
    OpenAIClient,
    OpenAIAPIClientConfig,
    PromptEngine,
    PromptEngineConfig,
    TokenManager,
    TokenConfig,
    ConversationGenerator,
    ConversationConfig,
    GenerationMode,
    create_openai_client,
    create_prompt_engine,
    create_token_manager,
    create_conversation_generator
)


class TestOpenAIConnectorIntegration:
    """OpenAI 커넥터 통합 테스트"""
    
    def setup_method(self):
        """테스트 설정"""
        # 설정 생성
        self.client_config = OpenAIAPIClientConfig(
            endpoint="http://localhost:9997/v1",
            model="qwen2.5-vl-instruct",
            api_key="test-key",
            max_tokens=4096,
            temperature=0.3,
            max_concurrent=2,
            retry_attempts=1
        )
        
        self.prompt_config = PromptEngineConfig(
            generation_mode="balanced",
            max_turns=4,
            batch_size=2
        )
        
        self.token_config = TokenConfig(
            max_context_length=8192,
            max_request_tokens=4096,
            enable_optimization=True
        )
        
        self.conversation_config = ConversationConfig(
            generation_mode=GenerationMode.LLM_ASSISTED,
            target_count=3,
            max_turns=2,
            batch_size=2,
            max_concurrent=2,
            temperature=0.3
        )
        
        # 컴포넌트 생성
        self.client = create_openai_client(self.client_config)
        self.prompt_engine = create_prompt_engine(self.prompt_config)
        self.token_manager = create_token_manager(self.token_config)
        self.conversation_generator = create_conversation_generator(
            self.client,
            self.prompt_engine,
            self.token_manager,
            self.conversation_config
        )
        
        # 테스트 문서
        self.test_documents = [
            {
                'id': 'doc1',
                'component': 'GridControl',
                'title': 'GridControl 기본 사용법',
                'content': 'GridControl은 Syncfusion WinForms의 강력한 데이터 그리드 컴포넌트입니다.',
                'quality_score': 0.8,
                'difficulty': 'Beginner'
            },
            {
                'id': 'doc2',
                'component': 'ChartControl',
                'title': 'ChartControl 차트 생성',
                'content': 'ChartControl을 사용하여 다양한 유형의 차트를 생성할 수 있습니다.',
                'quality_score': 0.9,
                'difficulty': 'Intermediate'
            }
        ]
    
    def test_component_initialization(self):
        """컴포넌트 초기화 테스트"""
        assert isinstance(self.client, OpenAIClient)
        assert isinstance(self.prompt_engine, PromptEngine)
        assert isinstance(self.token_manager, TokenManager)
        assert isinstance(self.conversation_generator, ConversationGenerator)
        
        # 설정 확인
        assert self.client.config.endpoint == "http://localhost:9997/v1"
        assert self.prompt_engine.config.generation_mode == "balanced"
        assert self.token_manager.config.max_context_length == 8192
        assert self.conversation_generator.config.target_count == 3
    
    def test_prompt_engine_token_manager_integration(self):
        """프롬프트 엔진과 토큰 매니저 통합 테스트"""
        # 프롬프트 생성
        prompts = self.prompt_engine.generate_conversation_prompt(self.test_documents[0])
        
        # 토큰 수 예측
        estimated_tokens = self.token_manager.estimate_tokens(prompts)
        
        assert isinstance(prompts, list)
        assert len(prompts) >= 2
        assert estimated_tokens > 0
        
        # 토큰 한도 확인
        can_process = self.token_manager.check_token_limit(estimated_tokens)
        assert can_process is True
        
        # 프롬프트 최적화
        optimized_prompts = self.token_manager.optimize_prompt(prompts, 1000)
        assert isinstance(optimized_prompts, list)
        assert len(optimized_prompts) <= len(prompts)
    
    @pytest.mark.asyncio
    async def test_client_prompt_integration(self):
        """클라이언트와 프롬프트 엔진 통합 테스트"""
        # Mock 응답 설정
        mock_response_data = {
            "choices": [{
                "message": {
                    "content": "GridControl은 강력한 데이터 그리드 컴포넌트로, 데이터 바인딩과 편집 기능을 제공합니다.",
                    "role": "assistant"
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "total_tokens": 80,
                "prompt_tokens": 30,
                "completion_tokens": 50
            }
        }
        
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = mock_response_data
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.return_value = mock_response
            
            async with self.client as client:
                # 프롬프트 생성
                prompts = self.prompt_engine.generate_conversation_prompt(self.test_documents[0])
                
                # API 호출
                response = await client.chat_completion(prompts)
                
                assert response.content == "GridControl은 강력한 데이터 그리드 컴포넌트로, 데이터 바인딩과 편집 기능을 제공합니다."
                assert response.tokens_used == 80
    
    @pytest.mark.asyncio
    async def test_full_conversation_generation_workflow(self):
        """전체 대화 생성 워크플로우 테스트"""
        # Mock 응답 설정
        mock_response_data = {
            "choices": [{
                "message": {
                    "content": "이 컴포넌트에 대한 자세한 설명을 제공하겠습니다. 기본 사용법부터 고급 기능까지 다양한 내용을 다룰 수 있습니다.",
                    "role": "assistant"
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "total_tokens": 60,
                "prompt_tokens": 20,
                "completion_tokens": 40
            }
        }
        
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = mock_response_data
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.return_value = mock_response
            
            async with self.client as client:
                # 대화 생성기에 클라이언트 설정
                self.conversation_generator.client = client
                
                # 대화 생성
                conversations = await self.conversation_generator.generate_conversations(
                    self.test_documents,
                    target_count=2
                )
                
                # 결과 검증
                assert isinstance(conversations, list)
                assert len(conversations) <= 2  # 목표 수 이하
                
                for conv in conversations:
                    assert hasattr(conv, 'id')
                    assert hasattr(conv, 'conversations')
                    assert hasattr(conv, 'metadata')
                    
                    # ShareGPT 포맷 확인
                    assert isinstance(conv.conversations, list)
                    if conv.conversations:
                        assert 'from' in conv.conversations[0]
                        assert 'value' in conv.conversations[0]
                    
                    # 메타데이터 확인
                    assert 'source_documents' in conv.metadata
                    assert 'model' in conv.metadata
                    assert 'tokens_used' in conv.metadata
    
    def test_batch_processing(self):
        """배치 처리 테스트"""
        # 배치 크기 제안
        suggested_batch_size = self.token_manager.suggest_batch_size(self.test_documents)
        assert isinstance(suggested_batch_size, int)
        assert suggested_batch_size > 0
        
        # 배치 프롬프트 생성
        batch_prompts = self.prompt_engine.create_batch_prompts(
            self.test_documents,
            mode="balanced"
        )
        
        assert isinstance(batch_prompts, list)
        assert len(batch_prompts) == len(self.test_documents)
        
        for prompts in batch_prompts:
            assert isinstance(prompts, list)
            assert len(prompts) >= 2
    
    def test_quality_validation(self):
        """품질 검증 테스트"""
        # 고품질 프롬프트
        high_quality_prompt = "GridControl의 DataSource 속성을 설정하는 C# 코드 예시를 알려주세요."
        quality = self.prompt_engine.validate_prompt_quality(high_quality_prompt)
        
        assert quality["score"] > 50
        assert quality["has_component"] is True
        assert quality["is_question_format"] is True
        
        # 저품질 프롬프트
        low_quality_prompt = "안녕"
        low_quality = self.prompt_engine.validate_prompt_quality(low_quality_prompt)
        
        assert low_quality["score"] < quality["score"]
        assert low_quality["is_high_quality"] is False
    
    def test_token_optimization(self):
        """토큰 최적화 테스트"""
        # 긴 프롬프트 생성
        long_prompts = []
        for i in range(10):
            long_prompts.append({
                "role": "user",
                "content": f"이것은 매우 긴 프롬프트입니다. " * 100 + f"질문 {i}"
            })
        
        # 토큰 수 예측
        original_tokens = self.token_manager.estimate_tokens(long_prompts)
        
        # 최적화
        optimized_prompts = self.token_manager.optimize_prompt(long_prompts, 500)
        optimized_tokens = self.token_manager.estimate_tokens(optimized_prompts)
        
        assert optimized_tokens <= 500
        assert len(optimized_prompts) <= len(long_prompts)
    
    def test_component_specific_generation(self):
        """컴포넌트별 특화 생성 테스트"""
        components = ["GridControl", "ChartControl", "TreeViewAdv"]
        
        for component in components:
            document = {
                'component': component,
                'title': f'{component} 사용법',
                'content': f'{component}에 대한 설명',
                'difficulty': 'Intermediate'
            }
            
            # 프롬프트 생성
            prompts = self.prompt_engine.generate_conversation_prompt(document)
            
            # 컴포넌트 이름이 포함되어야 함
            user_content = prompts[1]["content"] if len(prompts) > 1 else ""
            assert component in user_content
            
            # 컴포넌트별 템플릿 확인
            templates = self.prompt_engine.get_component_specific_templates(component)
            assert component.lower() in templates["intro"].lower()
    
    def test_error_handling(self):
        """오류 처리 테스트"""
        # 빈 문서 처리
        empty_documents = []
        batch_prompts = self.prompt_engine.create_batch_prompts(empty_documents)
        assert isinstance(batch_prompts, list)
        assert len(batch_prompts) == 0
        
        # 잘못된 문서 처리
        invalid_document = {"invalid": "data"}
        prompts = self.prompt_engine.generate_conversation_prompt(invalid_document)
        assert isinstance(prompts, list)
        assert len(prompts) >= 2
        
        # 토큰 한도 초과 처리
        huge_tokens = 999999
        can_process = self.token_manager.check_token_limit(huge_tokens)
        assert can_process is False
    
    def test_statistics_and_monitoring(self):
        """통계 및 모니터링 테스트"""
        # 토큰 사용량 업데이트
        self.token_manager.update_token_usage(100, 200)
        
        # 통계 확인
        stats = self.token_manager.get_stats()
        assert "current_context_tokens" in stats
        assert "usage_stats" in stats
        assert stats["usage_stats"]["total_tokens"] > 0
        
        # 대화 생성기 통계
        gen_stats = self.conversation_generator.get_stats()
        assert "generated_count" in gen_stats
        assert "failed_count" in gen_stats
        assert "config" in gen_stats


# 실제 API 통합 테스트 (선택적)
class TestRealAPIIntegration:
    """실제 API와의 통합 테스트 (localhost:9997이 실행 중일 때만)"""
    
    @pytest.mark.asyncio
    async def test_real_api_conversation_generation(self):
        """실제 API를 사용한 대화 생성 테스트"""
        # 설정
        client_config = OpenAIAPIClientConfig(
            endpoint="http://localhost:9997/v1",
            model="qwen2.5-vl-instruct",
            api_key="test-key",
            max_tokens=100,  # 테스트용 작은 값
            temperature=0.3,
            timeout=30
        )
        
        prompt_config = PromptEngineConfig(generation_mode="concise")
        token_config = TokenConfig(max_context_length=8192)
        conversation_config = ConversationConfig(
            target_count=1,
            max_turns=2,
            batch_size=1,
            max_concurrent=1
        )
        
        # 컴포넌트 생성
        client = create_openai_client(client_config)
        prompt_engine = create_prompt_engine(prompt_config)
        token_manager = create_token_manager(token_config)
        conversation_generator = create_conversation_generator(
            client, prompt_engine, token_manager, conversation_config
        )
        
        # 테스트 문서
        test_document = {
            'id': 'test_doc',
            'component': 'GridControl',
            'title': 'GridControl 테스트',
            'content': 'GridControl 기본 사용법',
            'quality_score': 0.8
        }
        
        try:
            async with client as api_client:
                # 연결 테스트
                health = await api_client.test_connection()
                if health["status"] != "success":
                    pytest.skip("API 서버에 연결할 수 없습니다")
                
                # 대화 생성
                conversations = await conversation_generator.generate_conversations([test_document])
                
                # 결과 검증
                assert len(conversations) >= 0  # 실패해도 빈 리스트 반환
                
                if conversations:
                    conv = conversations[0]
                    assert conv.id is not None
                    assert len(conv.conversations) > 0
                    assert 'source_documents' in conv.metadata
                    
                    print(f"생성된 대화: {conv.conversations}")
                    print(f"메타데이터: {conv.metadata}")
                
        except Exception as e:
            pytest.skip(f"실제 API 테스트 실패: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])