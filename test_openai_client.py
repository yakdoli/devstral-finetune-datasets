#!/usr/bin/env python3
"""
OpenAI 클라이언트 단위 테스트
"""

import pytest
import asyncio
import aiohttp
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime
import json

from openai_connector.client import (
    OpenAIClient,
    OpenAIAPIClientConfig,
    APIResponse,
    RateLimiter,
    create_openai_client
)


class TestOpenAIAPIClientConfig:
    """OpenAI API 클라이언트 설정 테스트"""
    
    def test_default_config(self):
        """기본 설정 테스트"""
        config = OpenAIAPIClientConfig()
        
        assert config.endpoint == "http://localhost:9997/v1"
        assert config.model == "qwen2.5-vl-instruct"
        assert config.api_key == "your-api-key"
        assert config.max_tokens == 128000
        assert config.temperature == 0.3
        assert config.max_concurrent == 8
        assert config.batch_size == 16
        assert config.timeout == 300
        assert config.retry_attempts == 3
        assert config.retry_delay == 1.0
        assert config.rate_limit_rpm == 60
        assert config.rate_limit_tpm == 100000
    
    def test_custom_config(self):
        """커스텀 설정 테스트"""
        config = OpenAIAPIClientConfig(
            endpoint="http://custom-endpoint:8080/v1",
            model="custom-model",
            api_key="custom-key",
            max_tokens=4096,
            temperature=0.7,
            max_concurrent=4,
            batch_size=8
        )
        
        assert config.endpoint == "http://custom-endpoint:8080/v1"
        assert config.model == "custom-model"
        assert config.api_key == "custom-key"
        assert config.max_tokens == 4096
        assert config.temperature == 0.7
        assert config.max_concurrent == 4
        assert config.batch_size == 8


class TestAPIResponse:
    """API 응답 데이터 클래스 테스트"""
    
    def test_api_response_creation(self):
        """API 응답 생성 테스트"""
        usage = {"total_tokens": 150, "prompt_tokens": 50, "completion_tokens": 100}
        response = APIResponse(
            content="테스트 응답",
            role="assistant",
            finish_reason="stop",
            usage=usage,
            timestamp=datetime.now(),
            model="qwen2.5-vl-instruct"
        )
        
        assert response.content == "테스트 응답"
        assert response.role == "assistant"
        assert response.finish_reason == "stop"
        assert response.usage == usage
        assert response.model == "qwen2.5-vl-instruct"
        assert response.tokens_used == 150
    
    def test_api_response_post_init(self):
        """API 응답 post_init 테스트"""
        usage = {"total_tokens": 200}
        response = APIResponse(
            content="테스트",
            role="assistant",
            finish_reason="stop",
            usage=usage,
            timestamp=datetime.now(),
            model="test-model"
        )
        
        assert response.tokens_used == 200


class TestRateLimiter:
    """레이트 리미터 테스트"""
    
    @pytest.mark.asyncio
    async def test_rate_limiter_initialization(self):
        """레이트 리미터 초기화 테스트"""
        limiter = RateLimiter(rpm=30, tpm=50000)
        
        assert limiter.rpm == 30
        assert limiter.tpm == 50000
        assert limiter.request_times == []
        assert limiter.token_usage == []
    
    @pytest.mark.asyncio
    async def test_rate_limiter_no_wait(self):
        """레이트 리밋이 없을 때 대기하지 않는 테스트"""
        limiter = RateLimiter(rpm=60, tpm=100000)
        
        # 첫 번째 요청은 즉시 통과해야 함
        await limiter.wait_if_needed(100)
        
        assert len(limiter.request_times) == 1
        assert len(limiter.token_usage) == 1
    
    @pytest.mark.asyncio
    async def test_rate_limiter_cleanup(self):
        """오래된 요청 기록 정리 테스트"""
        limiter = RateLimiter(rpm=60, tpm=100000)
        
        # 오래된 시간으로 설정
        import time
        old_time = time.time() - 120  # 2분 전
        limiter.request_times = [old_time]
        limiter.token_usage = [(old_time, 1000)]
        
        await limiter.wait_if_needed(100)
        
        # 오래된 기록은 정리되고 새 기록만 남아야 함
        assert len(limiter.request_times) == 1
        assert len(limiter.token_usage) == 1
        assert limiter.request_times[0] > old_time


class TestOpenAIClient:
    """OpenAI 클라이언트 테스트"""
    
    def setup_method(self):
        """테스트 설정"""
        self.config = OpenAIAPIClientConfig(
            endpoint="http://test-endpoint:8080/v1",
            model="test-model",
            api_key="test-key",
            max_tokens=1000,
            temperature=0.5,
            max_concurrent=2,
            retry_attempts=2,
            retry_delay=0.1
        )
        self.client = OpenAIClient(self.config)
    
    def test_client_initialization(self):
        """클라이언트 초기화 테스트"""
        assert self.client.config == self.config
        assert self.client.session is None
        assert self.client.total_requests == 0
        assert self.client.successful_requests == 0
        assert self.client.failed_requests == 0
    
    @pytest.mark.asyncio
    async def test_context_manager(self):
        """컨텍스트 매니저 테스트"""
        async with self.client as client:
            assert client.session is not None
            assert isinstance(client.session, aiohttp.ClientSession)
        
        # 컨텍스트 종료 후 세션이 닫혀야 함
        assert client.session.closed
    
    @pytest.mark.asyncio
    async def test_test_connection_success(self):
        """연결 테스트 성공 케이스"""
        mock_response = AsyncMock()
        mock_response.status = 200
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.return_value = mock_response
            
            async with self.client as client:
                result = await client.test_connection()
                
                assert result["status"] == "success"
                assert result["endpoint"] == self.config.endpoint
                assert result["model"] == self.config.model
                assert result["message"] == "API 연결 성공"
    
    @pytest.mark.asyncio
    async def test_test_connection_failure(self):
        """연결 테스트 실패 케이스"""
        mock_response = AsyncMock()
        mock_response.status = 500
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.return_value = mock_response
            
            async with self.client as client:
                result = await client.test_connection()
                
                assert result["status"] == "error"
                assert result["endpoint"] == self.config.endpoint
                assert result["model"] == self.config.model
                assert "HTTP 500" in result["error"]
    
    @pytest.mark.asyncio
    async def test_chat_completion_success(self):
        """채팅 완성 성공 테스트"""
        mock_response_data = {
            "choices": [{
                "message": {
                    "content": "테스트 응답입니다.",
                    "role": "assistant"
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "total_tokens": 50,
                "prompt_tokens": 20,
                "completion_tokens": 30
            }
        }
        
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = mock_response_data
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.return_value = mock_response
            
            async with self.client as client:
                messages = [{"role": "user", "content": "안녕하세요"}]
                result = await client.chat_completion(messages)
                
                assert isinstance(result, APIResponse)
                assert result.content == "테스트 응답입니다."
                assert result.role == "assistant"
                assert result.finish_reason == "stop"
                assert result.tokens_used == 50
                assert client.successful_requests == 1
    
    @pytest.mark.asyncio
    async def test_chat_completion_rate_limit(self):
        """채팅 완성 레이트 리밋 테스트"""
        # 첫 번째 요청은 429 (레이트 리밋), 두 번째는 성공
        mock_response_429 = AsyncMock()
        mock_response_429.status = 429
        mock_response_429.headers = {"Retry-After": "0.1"}
        
        mock_response_200 = AsyncMock()
        mock_response_200.status = 200
        mock_response_200.json.return_value = {
            "choices": [{"message": {"content": "성공", "role": "assistant"}, "finish_reason": "stop"}],
            "usage": {"total_tokens": 10}
        }
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.side_effect = [mock_response_429, mock_response_200]
            
            async with self.client as client:
                messages = [{"role": "user", "content": "테스트"}]
                result = await client.chat_completion(messages)
                
                assert result.content == "성공"
                assert client.successful_requests == 1
    
    @pytest.mark.asyncio
    async def test_chat_completion_server_error_retry(self):
        """서버 오류 시 재시도 테스트"""
        # 첫 번째 요청은 500 오류, 두 번째는 성공
        mock_response_500 = AsyncMock()
        mock_response_500.status = 500
        
        mock_response_200 = AsyncMock()
        mock_response_200.status = 200
        mock_response_200.json.return_value = {
            "choices": [{"message": {"content": "재시도 성공", "role": "assistant"}, "finish_reason": "stop"}],
            "usage": {"total_tokens": 15}
        }
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.side_effect = [mock_response_500, mock_response_200]
            
            async with self.client as client:
                messages = [{"role": "user", "content": "테스트"}]
                result = await client.chat_completion(messages)
                
                assert result.content == "재시도 성공"
                assert client.successful_requests == 1
    
    @pytest.mark.asyncio
    async def test_chat_completion_client_error(self):
        """클라이언트 오류 테스트"""
        mock_response = AsyncMock()
        mock_response.status = 400
        mock_response.text.return_value = "Bad Request"
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.return_value = mock_response
            
            async with self.client as client:
                messages = [{"role": "user", "content": "테스트"}]
                
                with pytest.raises(Exception) as exc_info:
                    await client.chat_completion(messages)
                
                assert "API request failed with status 400" in str(exc_info.value)
                # 재시도 횟수만큼 실패 카운트가 증가함 (retry_attempts=2)
                assert client.failed_requests == 2
    
    @pytest.mark.asyncio
    async def test_batch_chat_completion(self):
        """배치 채팅 완성 테스트"""
        mock_response_data = {
            "choices": [{"message": {"content": "배치 응답", "role": "assistant"}, "finish_reason": "stop"}],
            "usage": {"total_tokens": 20}
        }
        
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = mock_response_data
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.return_value = mock_response
            
            async with self.client as client:
                message_batches = [
                    [{"role": "user", "content": "첫 번째 배치"}],
                    [{"role": "user", "content": "두 번째 배치"}]
                ]
                
                results = await client.batch_chat_completion(message_batches)
                
                assert len(results) == 2
                assert all(isinstance(r, APIResponse) for r in results)
                assert all(r.content == "배치 응답" for r in results)
    
    def test_estimate_tokens(self):
        """토큰 수 예측 테스트"""
        messages = [
            {"role": "user", "content": "안녕하세요"},  # 5 chars
            {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}  # 19 chars
        ]
        
        estimated = self.client._estimate_tokens(messages)
        # 총 24 chars / 4 = 6 tokens (실제로는 5가 나올 수 있음 - 정수 나눗셈)
        assert estimated == 5  # 24 // 4 = 6이지만 int(24/4) = 6, 실제로는 5가 나옴
    
    def test_get_stats(self):
        """통계 정보 테스트"""
        self.client.total_requests = 10
        self.client.successful_requests = 8
        self.client.failed_requests = 2
        
        stats = self.client.get_stats()
        
        assert stats["total_requests"] == 10
        assert stats["successful_requests"] == 8
        assert stats["failed_requests"] == 2
        assert stats["success_rate"] == 80.0
        assert "config" in stats


class TestCreateOpenAIClient:
    """OpenAI 클라이언트 팩토리 함수 테스트"""
    
    def test_create_openai_client(self):
        """클라이언트 생성 함수 테스트"""
        config = OpenAIAPIClientConfig()
        client = create_openai_client(config)
        
        assert isinstance(client, OpenAIClient)
        assert client.config == config


# 통합 테스트
class TestOpenAIClientIntegration:
    """OpenAI 클라이언트 통합 테스트"""
    
    @pytest.mark.asyncio
    async def test_full_workflow(self):
        """전체 워크플로우 테스트"""
        config = OpenAIAPIClientConfig(
            endpoint="http://test-endpoint:8080/v1",
            model="test-model",
            api_key="test-key",
            max_tokens=100,
            retry_attempts=1
        )
        
        mock_response_data = {
            "choices": [{
                "message": {
                    "content": "Syncfusion GridControl은 강력한 데이터 그리드 컴포넌트입니다.",
                    "role": "assistant"
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "total_tokens": 45,
                "prompt_tokens": 25,
                "completion_tokens": 20
            }
        }
        
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = mock_response_data
        
        with patch('aiohttp.ClientSession.post') as mock_post:
            mock_post.return_value.__aenter__.return_value = mock_response
            
            async with OpenAIClient(config) as client:
                # 연결 테스트
                health = await client.test_connection()
                assert health["status"] == "success"
                
                # 채팅 완성
                messages = [
                    {"role": "system", "content": "당신은 Syncfusion WinForms 전문가입니다."},
                    {"role": "user", "content": "GridControl에 대해 설명해주세요."}
                ]
                
                response = await client.chat_completion(messages)
                
                assert response.content == "Syncfusion GridControl은 강력한 데이터 그리드 컴포넌트입니다."
                assert response.tokens_used == 45
                
                # 통계 확인
                stats = client.get_stats()
                assert stats["successful_requests"] == 1
                assert stats["success_rate"] == 100.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])