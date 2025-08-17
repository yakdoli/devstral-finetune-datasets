#!/usr/bin/env python3
"""
로컬 LLM 클라이언트 모듈

로컬에서 실행되는 언어 모델과의 HTTP 통신을 담당합니다.
OpenAI 호환 API를 지원하면서 로컬 LLM 특성에 맞게 최적화되었습니다.
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
class LocalLLMClientConfig:
    """로컬 LLM 클라이언트 설정"""
    endpoint: str = "http://123.37.28.120:9997/v1"
    model: str = "qwen2.5-vl-instruct"
    api_key: str = "your-api-key"
    max_tokens: int = 128000
    temperature: float = 0.3
    top_p: float = 0.9
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    max_concurrent: int = 8
    batch_size: int = 16
    timeout: int = 300
    retry_attempts: int = 3
    retry_delay: float = 1.0
    rate_limit_rpm: int = 600  # requests per minute
    rate_limit_tpm: int = 1000000  # tokens per minute
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_tokens <= 0:
            raise ValueError("max_tokens는 양의 정수여야 합니다")
        if not (0.0 <= self.temperature <= 2.0):
            raise ValueError("temperature는 0.0과 2.0 사이여야 합니다")
        if not (0.0 <= self.top_p <= 1.0):
            raise ValueError("top_p는 0.0과 1.0 사이여야 합니다")
        if self.max_concurrent <= 0:
            raise ValueError("max_concurrent는 양의 정수여야 합니다")
        if self.batch_size <= 0:
            raise ValueError("batch_size는 양의 정수여야 합니다")


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
    
    def __init__(self, rpm: int = 600, tpm: int = 1000000):
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


class LocalLLMClient:
    """로컬 LLM 클라이언트"""
    
    def __init__(self, config: LocalLLMClientConfig):
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
        연결 테스트
        
        Returns:
            연결 테스트 결과
        """
        try:
            # 모델 목록 요청
            models_url = f"{self.config.endpoint}/models"
            
            async with self.session.get(models_url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # 모델 정보 확인
                    models = data.get("data", [])
                    model_found = any(model.get("id") == self.config.model for model in models)
                    
                    return {
                        "status": "success",
                        "message": "로컬 LLM 연결 성공",
                        "model_info": {
                            "model": self.config.model,
                            "available": model_found,
                            "total_models": len(models)
                        },
                        "endpoint": self.config.endpoint,
                        "timestamp": datetime.now().isoformat()
                    }
                else:
                    return {
                        "status": "error",
                        "message": f"HTTP 오류: {response.status}",
                        "endpoint": self.config.endpoint,
                        "timestamp": datetime.now().isoformat()
                    }
                    
        except Exception as e:
            logger.error(f"연결 테스트 실패: {str(e)}")
            return {
                "status": "error",
                "message": f"연결 실패: {str(e)}",
                "endpoint": self.config.endpoint,
                "timestamp": datetime.now().isoformat()
            }
    
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        stream: bool = False
    ) -> APIResponse:
        """
        채팅 완성 요청
        
        Args:
            messages: 메시지 목록
            max_tokens: 최대 토큰 수
            temperature: 생성 온도
            top_p: Top-p 샘플링
            stream: 스트리밍 여부
            
        Returns:
            API 응답
        """
        if not self.session:
            raise RuntimeError("세션이 초기화되지 않았습니다. async with 구문을 사용하세요.")
        
        # 설정 값 적용
        max_tokens = max_tokens or self.config.max_tokens
        temperature = temperature or self.config.temperature
        top_p = top_p or self.config.top_p
        
        # 레이트 리밋 확인
        estimated_tokens = self._estimate_tokens(messages)
        await self.rate_limiter.wait_if_needed(estimated_tokens)
        
        # 요청 데이터 구성
        request_data = {
            "model": self.config.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "stream": stream
        }
        
        # 재시도 로직
        for attempt in range(self.config.retry_attempts):
            try:
                self.total_requests += 1
                
                # 요청 전송
                url = f"{self.config.endpoint}/chat/completions"
                async with self.session.post(url, json=request_data) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # 응답 파싱
                        api_response = self._parse_chat_response(data)
                        
                        self.successful_requests += 1
                        return api_response
                    else:
                        error_text = await response.text()
                        logger.error(f"API 요청 실패 (시도 {attempt + 1}/{self.config.retry_attempts}): {response.status} - {error_text}")
                        
                        if attempt == self.config.retry_attempts - 1:
                            raise Exception(f"API 요청 실패: {response.status} - {error_text}")
                        
                        # 재시도 대기
                        await asyncio.sleep(self.config.retry_delay * (2 ** attempt))
                        
            except Exception as e:
                logger.error(f"채팅 완성 요청 실패 (시도 {attempt + 1}/{self.config.retry_attempts}): {str(e)}")
                
                if attempt == self.config.retry_attempts - 1:
                    self.failed_requests += 1
                    raise Exception(f"채팅 완성 요청 최종 실패: {str(e)}")
                
                # 재시도 대기
                await asyncio.sleep(self.config.retry_delay * (2 ** attempt))
        
        # 여기에 도달하지 않아야 함
        raise Exception("채팅 완성 요청 실패")
    
    async def chat_completion_batch(
        self,
        messages_list: List[List[Dict[str, str]]],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None
    ) -> List[APIResponse]:
        """
        배치 채팅 완성 요청
        
        Args:
            messages_list: 메시지 목록의 리스트
            max_tokens: 최대 토큰 수
            temperature: 생성 온도
            top_p: Top-p 샘플링
            
        Returns:
            API 응답 리스트
        """
        if not messages_list:
            return []
        
        # 배치 크기 계산
        batch_size = self.config.batch_size
        batches = [messages_list[i:i + batch_size] for i in range(0, len(messages_list), batch_size)]
        
        results = []
        
        for batch in batches:
            # 배치 처리
            batch_results = await self._process_batch(
                batch, max_tokens, temperature, top_p
            )
            results.extend(batch_results)
        
        return results
    
    async def _process_batch(
        self,
        messages_batch: List[List[Dict[str, str]]],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None
    ) -> List[APIResponse]:
        """
        배치 처리
        
        Args:
            messages_batch: 메시지 배치
            max_tokens: 최대 토큰 수
            temperature: 생성 온도
            top_p: Top-p 샘플링
            
        Returns:
            API 응답 리스트
        """
        tasks = []
        
        for messages in messages_batch:
            task = self.chat_completion(messages, max_tokens, temperature, top_p)
            tasks.append(task)
        
        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # 예외 처리
            valid_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    logger.error(f"Batch item {i} failed: {result}")
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
            
        except Exception as e:
            logger.error(f"배치 처리 실패: {str(e)}")
            # 빈 응답으로 대체
            return [
                APIResponse(
                    content="",
                    role="assistant",
                    finish_reason="error",
                    usage={},
                    timestamp=datetime.now(),
                    model=self.config.model
                )
                for _ in messages_batch
            ]
    
    def _parse_chat_response(self, data: Dict[str, Any]) -> APIResponse:
        """
        채팅 응답 파싱
        
        Args:
            data: API 응답 데이터
            
        Returns:
            파싱된 API 응답
        """
        try:
            choices = data.get("choices", [])
            if not choices:
                raise Exception("응답에 choices 필드가 없습니다")
            
            choice = choices[0]
            message = choice.get("message", {})
            
            content = message.get("content", "")
            role = message.get("role", "assistant")
            finish_reason = choice.get("finish_reason", "stop")
            
            # 사용량 정보
            usage = data.get("usage", {})
            
            return APIResponse(
                content=content,
                role=role,
                finish_reason=finish_reason,
                usage=usage,
                timestamp=datetime.now(),
                model=data.get("model", self.config.model),
                tokens_used=usage.get("total_tokens", 0)
            )
            
        except Exception as e:
            logger.error(f"채팅 응답 파싱 실패: {str(e)}")
            raise Exception(f"응답 파싱 실패: {str(e)}")
    
    def _estimate_tokens(self, messages: List[Dict[str, str]]) -> int:
        """
        메시지의 토큰 수를 예측
        
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
        클라이언트 통계 정보를 반환
        
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


def create_local_llm_client(config: LocalLLMClientConfig) -> LocalLLMClient:
    """
    로컬 LLM 클라이언트를 생성
    
    Args:
        config: 클라이언트 설정
        
    Returns:
        LocalLLMClient 인스턴스
    """
    return LocalLLMClient(config)


# 테스트 코드
async def test_client():
    """클라이언트 테스트"""
    config = LocalLLMClientConfig(
        endpoint="http://123.37.28.120:9997/v1",
        model="qwen2.5-vl-instruct",
        api_key="test-key",
        max_tokens=1000,
        temperature=0.3,
        max_concurrent=2
    )
    
    async with LocalLLMClient(config) as client:
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