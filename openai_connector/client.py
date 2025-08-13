#!/usr/bin/env python3
"""
OpenAI 호환 API 클라이언트 모듈
qwen2.5-vl-instruct 모델과의 통신을 담당합니다.
"""

import json
import asyncio
import aiohttp
import logging
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import time
from enum import Enum

logger = logging.getLogger(__name__)


class GenerationMode(Enum):
    """생성 모드 정의"""
    LLM_ASSISTED = "llm_assisted"
    RULE_BASED = "rule_based"


@dataclass
class OpenAIAPIClientConfig:
    """OpenAI API 클라이언트 설정"""
    endpoint: str = "http://123.37.28.120:9997/v1"
    model: str = "qwen2.5-vl-instruct"
    api_key: str = "your-api-key"
    max_tokens: int = 128000
    temperature: float = 0.3
    max_concurrent: int = 8
    batch_size: int = 16
    timeout: int = 300
    retry_attempts: int = 3
    retry_delay: float = 1.0
    rate_limit_rpm: int = 60  # requests per minute
    rate_limit_tpm: int = 100000  # tokens per minute


@dataclass
class APIResponse:
    """API 응답 데이터 클래스"""
    content: str
    role: str
    finish_reason: str
    usage: Dict[str, int]
    timestamp: datetime
    model: str
    tokens_used: int = 0
    
    def __post_init__(self):
        if self.tokens_used == 0 and self.usage:
            self.tokens_used = self.usage.get("total_tokens", 0)


class RateLimiter:
    """레이트 리미터 클래스"""
    
    def __init__(self, rpm: int = 60, tpm: int = 100000):
        self.rpm = rpm
        self.tpm = tpm
        self.request_times = []
        self.token_usage = []
        self.lock = asyncio.Lock()
    
    async def wait_if_needed(self, tokens_required: int = 1):
        """레이트 리밋을 확인하고 필요한 경우 대기합니다."""
        async with self.lock:
            now = time.time()
            
            # 오래된 요청 기록 정리 (1분 이전)
            self.request_times = [t for t in self.request_times if now - t < 60]
            self.token_usage = [t for t in self.token_usage if now - t[0] < 60]
            
            # RPM 확인
            if len(self.request_times) >= self.rpm:
                sleep_time = 60 - (now - self.request_times[0])
                if sleep_time > 0:
                    logger.info(f"Rate limit reached. Waiting {sleep_time:.2f} seconds...")
                    await asyncio.sleep(sleep_time)
            
            # TPM 확인
            total_tokens_in_window = sum(t[1] for t in self.token_usage)
            if total_tokens_in_window + tokens_required > self.tpm:
                # 가장 오래된 토큰 사용량 기준으로 대기 시간 계산
                if self.token_usage:
                    oldest_time, oldest_tokens = self.token_usage[0]
                    sleep_time = 60 - (now - oldest_time)
                    if sleep_time > 0:
                        logger.info(f"Token rate limit reached. Waiting {sleep_time:.2f} seconds...")
                        await asyncio.sleep(sleep_time)
            
            # 현재 요청 기록
            self.request_times.append(now)
            self.token_usage.append((now, tokens_required))


class OpenAIClient:
    """OpenAI 호환 API 클라이언트"""
    
    def __init__(self, config: OpenAIAPIClientConfig):
        """
        초기화
        
        Args:
            config: 클라이언트 설정
        """
        self.config = config
        self.session: Optional[aiohttp.ClientSession] = None
        self.rate_limiter = RateLimiter(config.rate_limit_rpm, config.rate_limit_tpm)
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        
    async def __aenter__(self):
        """비동기 컨텍스트 매니저 진입"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.config.timeout),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.api_key}"
            }
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """비동기 컨텍스트 매니저 종료"""
        if self.session:
            await self.session.close()
    
    async def test_connection(self) -> Dict[str, Any]:
        """
        API 연결을 테스트합니다.
        
        Returns:
            연결 상태 정보
        """
        try:
            test_payload = {
                "model": self.config.model,
                "messages": [
                    {"role": "user", "content": "test"}
                ],
                "max_tokens": 10
            }
            
            async with self.session.post(
                f"{self.config.endpoint}/chat/completions",
                json=test_payload
            ) as response:
                if response.status == 200:
                    return {
                        "status": "success",
                        "endpoint": self.config.endpoint,
                        "model": self.config.model,
                        "message": "API 연결 성공"
                    }
                else:
                    return {
                        "status": "error",
                        "endpoint": self.config.endpoint,
                        "model": self.config.model,
                        "error": f"HTTP {response.status}",
                        "message": "API 연결 실패"
                    }
                    
        except Exception as e:
            return {
                "status": "error",
                "endpoint": self.config.endpoint,
                "model": self.config.model,
                "error": str(e),
                "message": "API 연결 실패"
            }
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        stream: bool = False
    ) -> APIResponse:
        """
        채팅 완성 요청을 보냅니다.
        
        Args:
            messages: 메시지 목록
            max_tokens: 최대 토큰 수
            temperature: 생성 온도
            stream: 스트리밍 여부
            
        Returns:
            API 응답
        """
        self.total_requests += 1
        
        # 설정값 사용
        max_tokens = max_tokens or self.config.max_tokens
        temperature = temperature or self.config.temperature
        
        # 토큰 수 예측 (간단한 예측)
        estimated_tokens = self._estimate_tokens(messages) + max_tokens
        
        # 레이트 리밋 확인
        await self.rate_limiter.wait_if_needed(estimated_tokens)
        
        payload = {
            "model": self.config.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": stream
        }
        
        # 재시도 로직
        for attempt in range(self.config.retry_attempts):
            try:
                logger.debug(f"Sending request (attempt {attempt + 1}): {payload}")
                
                async with self.session.post(
                    f"{self.config.endpoint}/chat/completions",
                    json=payload
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        self.successful_requests += 1
                        
                        # 응답 파싱
                        choice = result.get("choices", [{}])[0]
                        message = choice.get("message", {})
                        
                        api_response = APIResponse(
                            content=message.get("content", ""),
                            role=message.get("role", "assistant"),
                            finish_reason=choice.get("finish_reason", "stop"),
                            usage=result.get("usage", {}),
                            timestamp=datetime.now(),
                            model=self.config.model,
                            tokens_used=result.get("usage", {}).get("total_tokens", 0)
                        )
                        
                        logger.debug(f"Response received: {api_response.tokens_used} tokens used")
                        return api_response
                        
                    elif response.status == 429:
                        # 레이트 리밋 오류
                        retry_after = int(response.headers.get("Retry-After", 5))
                        logger.warning(f"Rate limited. Retrying after {retry_after} seconds...")
                        await asyncio.sleep(retry_after)
                        continue
                        
                    elif response.status >= 500:
                        # 서버 오류
                        logger.warning(f"Server error {response.status}. Retrying...")
                        await asyncio.sleep(self.config.retry_delay * (2 ** attempt))
                        continue
                        
                    else:
                        # 클라이언트 오류
                        error_text = await response.text()
                        logger.error(f"Client error {response.status}: {error_text}")
                        self.failed_requests += 1
                        raise Exception(f"API request failed with status {response.status}: {error_text}")
                        
            except Exception as e:
                self.failed_requests += 1
                if attempt == self.config.retry_attempts - 1:
                    raise Exception(f"All retry attempts failed: {e}")
                await asyncio.sleep(self.config.retry_delay * (2 ** attempt))
        
        raise Exception("Unexpected error in chat completion")
    
    async def batch_chat_completion(
        self,
        message_batches: List[List[Dict[str, str]]],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        semaphore_value: int = None
    ) -> List[APIResponse]:
        """
        배치 채팅 완성 요청을 보냅니다.
        
        Args:
            message_batches: 메시지 배치 목록
            max_tokens: 최대 토큰 수
            temperature: 생성 온도
            semaphore_value: 동시 요청 제한 값
            
        Returns:
            API 응답 목록
        """
        semaphore_value = semaphore_value or self.config.max_concurrent
        semaphore = asyncio.Semaphore(semaphore_value)
        
        async def process_batch(batch_messages):
            async with semaphore:
                return await self.chat_completion(batch_messages, max_tokens, temperature)
        
        tasks = [process_batch(batch) for batch in message_batches]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # 예외 처리
        valid_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                logger.error(f"Batch {i} failed: {result}")
                # 빈 응답으로 대체
                valid_results.append(APIResponse(
                    content="",
                    role="assistant",
                    finish_reason="error",
                    usage={},
                    timestamp=datetime.now(),
                    model=self.config.model
                ))
            else:
                valid_results.append(result)
        
        return valid_results
    
    def _estimate_tokens(self, messages: List[Dict[str, str]]) -> int:
        """
        메시지의 토큰 수를 예측합니다.
        
        Args:
            messages: 메시지 목록
            
        Returns:
            예측된 토큰 수
        """
        # 간단한 토큰 예측 (실제로는 tiktoken 사용이 좋음)
        total_chars = sum(len(msg.get("content", "")) for msg in messages)
        # 평균적으로 1토큰 = 4 characters
        return int(total_chars / 4)
    
    def get_stats(self) -> Dict[str, Any]:
        """
        클라이언트 통계 정보를 반환합니다.
        
        Returns:
            통계 정보
        """
        return {
            "total_requests": self.total_requests,
            "successful_requests": self.successful_requests,
            "failed_requests": self.failed_requests,
            "success_rate": (self.successful_requests / self.total_requests * 100) if self.total_requests > 0 else 0,
            "config": asdict(self.config)
        }


def create_openai_client(config: OpenAIAPIClientConfig) -> OpenAIClient:
    """
    OpenAI 클라이언트를 생성합니다.
    
    Args:
        config: 클라이언트 설정
        
    Returns:
        OpenAIClient 인스턴스
    """
    return OpenAIClient(config)


# 테스트 코드
async def test_client():
    """클라이언트 테스트"""
    config = OpenAIAPIClientConfig(
        endpoint="http://123.37.28.120:9997/v1",
        model="qwen2.5-vl-instruct",
        api_key="test-key",
        max_tokens=1000,
        temperature=0.3,
        max_concurrent=2
    )
    
    async with OpenAIClient(config) as client:
        # 연결 테스트
        health = await client.test_connection()
        print(f"연결 상태: {health}")
        
        # 간단한 채팅 테스트
        if health["status"] == "success":
            messages = [
                {"role": "system", "content": "당신은 Syncfusion WinForms 전문가입니다."},
                {"role": "user", "content": "GridControl의 기본 사용법을 알려주세요."}
            ]
            
            try:
                response = await client.chat_completion(messages)
                print(f"응답: {response.content[:200]}...")
                print(f"사용된 토큰: {response.tokens_used}")
            except Exception as e:
                print(f"채팅 테스트 실패: {e}")


if __name__ == "__main__":
    asyncio.run(test_client())