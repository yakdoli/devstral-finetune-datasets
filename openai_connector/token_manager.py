#!/usr/bin/env python3
"""
토큰 관리자 모듈
토큰 사용량을 추적하고 최적화합니다.
"""

import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import re
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class TokenLimitType(Enum):
    """토큰 한도 유형"""
    CONTEXT = "context"
    REQUEST = "request"
    RATE_LIMIT = "rate_limit"


@dataclass
class TokenConfig:
    """토큰 관리 설정"""
    max_context_length: int = 128000
    max_request_tokens: int = 32000
    rate_limit_rpm: int = 60  # requests per minute
    rate_limit_tpm: int = 100000  # tokens per minute
    token_buffer: float = 0.9  # 90% 사용 시 경고
    enable_optimization: bool = True
    track_usage_history: bool = True
    history_size: int = 1000


class TokenEstimator:
    """토큰 예측기"""
    
    def __init__(self):
        """초기화"""
        # 간단한 토큰 예측을 위한 평균 문자당 토큰 비율
        self.char_to_token_ratio = {
            "english": 4.0,  # 영어 평균
            "korean": 2.5,   # 한국어 평균
            "code": 3.0,     # 코드 평균
            "mixed": 3.2     # 혼합 평균
        }
    
    def estimate_tokens(self, text: str, text_type: str = "mixed") -> int:
        """
        텍스트의 토큰 수를 예측합니다.
        
        Args:
            text: 예측할 텍스트
            text_type: 텍스트 유형 (english, korean, code, mixed)
            
        Returns:
            예측된 토큰 수
        """
        if not text:
            return 0
        
        # 텍스트 유형 결정
        if text_type == "auto":
            text_type = self._detect_text_type(text)
        
        # 기본 비율 설정
        ratio = self.char_to_token_ratio.get(text_type, 3.2)
        
        # 문자 수 계산
        char_count = len(text)
        
        # 특수 문자 보정
        special_chars = re.findall(r'[^\w\s]', text)
        if special_chars:
            ratio *= 1.1  # 특수 문자가 많으면 토큰 수 증가
        
        # 코드 라인 보정
        if text_type == "code":
            lines = text.split('\n')
            ratio *= 1.05  # 코드는 라인당 더 많은 토큰 사용
        
        # 예측된 토큰 수 계산
        estimated_tokens = int(char_count / ratio)
        
        # 최소/최대 값 보정
        estimated_tokens = max(1, min(estimated_tokens, 100000))
        
        return estimated_tokens
    
    def estimate_message_tokens(self, messages: List[Dict[str, str]]) -> int:
        """
        메시지 목록의 토큰 수를 예측합니다.
        
        Args:
            messages: 메시지 목록
            
        Returns:
            예측된 토큰 수
        """
        total_tokens = 0
        
        for message in messages:
            content = message.get('content', '')
            role = message.get('role', 'user')
            
            # 콘텐츠 토큰 수 예측
            content_tokens = self.estimate_tokens(content)
            
            # 역할 토큰 수 추가 (약 1-3 토큰)
            role_tokens = 2
            
            # 메시지 구조 토큰 수 추가 (약 3-4 토큰)
            structure_tokens = 4
            
            total_tokens += content_tokens + role_tokens + structure_tokens
        
        return total_tokens
    
    def _detect_text_type(self, text: str) -> str:
        """텍스트 유형을 감지합니다."""
        # 코드 감지
        code_patterns = [
            r'\b(def|class|function|var|let|const|if|else|for|while|return)\b',
            r'\b(int|string|bool|float|double|void)\b',
            r'[{}();\[\]]',
            r'//.*|/\*.*\*/'
        ]
        
        code_score = sum(1 for pattern in code_patterns if re.search(pattern, text))
        if code_score >= 2:
            return "code"
        
        # 한국어 감지
        korean_chars = len(re.findall(r'[가-힣]', text))
        total_chars = len(text)
        
        if korean_chars / total_chars > 0.3:
            return "korean"
        
        # 영어 감지
        english_chars = len(re.findall(r'[a-zA-Z]', text))
        if english_chars / total_chars > 0.5:
            return "english"
        
        return "mixed"


class TokenTracker:
    """토큰 사용량 추적기"""
    
    def __init__(self, config: TokenConfig):
        """
        초기화
        
        Args:
            config: 토큰 설정
        """
        self.config = config
        self.usage_history: List[Dict[str, Any]] = []
        self.session_start = datetime.now()
        self.total_tokens_used = 0
        self.total_requests = 0
        self.tokens_by_type: Dict[str, int] = {
            "prompt": 0,
            "completion": 0,
            "total": 0
        }
    
    def record_token_usage(
        self,
        prompt_tokens: int,
        completion_tokens: int,
        request_tokens: int,
        timestamp: datetime = None
    ):
        """
        토큰 사용량을 기록합니다.
        
        Args:
            prompt_tokens: 프롬프트 토큰 수
            completion_tokens: 완성 토큰 수
            request_tokens: 요청 토큰 수
            timestamp: 타임스탬프
        """
        timestamp = timestamp or datetime.now()
        
        # 사용량 업데이트
        self.total_tokens_used += request_tokens
        self.total_requests += 1
        self.tokens_by_type["prompt"] += prompt_tokens
        self.tokens_by_type["completion"] += completion_tokens
        self.tokens_by_type["total"] += request_tokens
        
        # 기록 저장
        usage_record = {
            "timestamp": timestamp.isoformat(),
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "request_tokens": request_tokens,
            "session_duration": (timestamp - self.session_start).total_seconds()
        }
        
        self.usage_history.append(usage_record)
        
        # 기록 크기 제한
        if len(self.usage_history) > self.config.history_size:
            self.usage_history.pop(0)
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """사용량 통계를 반환합니다."""
        if not self.usage_history:
            return {
                "total_tokens": 0,
                "total_requests": 0,
                "avg_tokens_per_request": 0,
                "tokens_by_type": self.tokens_by_type,
                "session_duration": 0,
                "requests_per_minute": 0,
                "tokens_per_minute": 0
            }
        
        # 세션 시간 계산
        session_duration = (datetime.now() - self.session_start).total_seconds()
        session_duration_minutes = session_duration / 60.0
        
        # 분당 통계 계산
        requests_per_minute = self.total_requests / session_duration_minutes if session_duration_minutes > 0 else 0
        tokens_per_minute = self.total_tokens_used / session_duration_minutes if session_duration_minutes > 0 else 0
        
        # 평균 토큰 수 계산
        avg_tokens_per_request = self.total_tokens_used / self.total_requests if self.total_requests > 0 else 0
        
        return {
            "total_tokens": self.total_tokens_used,
            "total_requests": self.total_requests,
            "avg_tokens_per_request": avg_tokens_per_request,
            "tokens_by_type": self.tokens_by_type,
            "session_duration": session_duration,
            "requests_per_minute": requests_per_minute,
            "tokens_per_minute": tokens_per_minute,
            "usage_history_size": len(self.usage_history)
        }
    
    def get_recent_usage(self, minutes: int = 60) -> Dict[str, Any]:
        """최근 사용량을 반환합니다."""
        cutoff_time = datetime.now() - timedelta(minutes=minutes)
        
        recent_usage = [
            record for record in self.usage_history
            if datetime.fromisoformat(record["timestamp"]) >= cutoff_time
        ]
        
        if not recent_usage:
            return {
                "tokens_in_period": 0,
                "requests_in_period": 0,
                "avg_tokens_per_request": 0
            }
        
        total_tokens = sum(record["request_tokens"] for record in recent_usage)
        total_requests = len(recent_usage)
        avg_tokens_per_request = total_tokens / total_requests if total_requests > 0 else 0
        
        return {
            "tokens_in_period": total_tokens,
            "requests_in_period": total_requests,
            "avg_tokens_per_request": avg_tokens_per_request,
            "period_minutes": minutes
        }


class TokenOptimizer:
    """토큰 최적화기"""
    
    def __init__(self, config: TokenConfig):
        """
        초기화
        
        Args:
            config: 토큰 설정
        """
        self.config = config
        self.estimator = TokenEstimator()
    
    def optimize_prompt(self, prompt: List[Dict[str, str]], max_tokens: int) -> List[Dict[str, str]]:
        """
        프롬프트를 최적화합니다.
        
        Args:
            prompt: 최적화할 프롬프트
            max_tokens: 최대 토큰 수
            
        Returns:
            최적화된 프롬프트
        """
        if not self.config.enable_optimization:
            return prompt
        
        # 현재 토큰 수 계산
        current_tokens = self.estimator.estimate_message_tokens(prompt)
        
        if current_tokens <= max_tokens:
            return prompt
        
        # 최적화 시작
        optimized_prompt = []
        remaining_tokens = max_tokens
        
        # 메시지를 중요도 순으로 정렬 (시스템 > 사용자 > 어시스턴트)
        message_order = ["system", "user", "assistant"]
        sorted_messages = sorted(
            prompt,
            key=lambda x: message_order.index(x.get("role", "user"))
        )
        
        for message in sorted_messages:
            content = message.get("content", "")
            role = message.get("role", "user")
            
            # 메시지 토큰 수 예측
            message_tokens = self.estimator.estimate_tokens(content)
            
            # 최소 토큰 수 보장
            min_tokens = 10 if role == "system" else 5
            
            if message_tokens <= remaining_tokens - min_tokens:
                # 메시지 전체 추가
                optimized_prompt.append(message)
                remaining_tokens -= message_tokens
            else:
                # 메시지 일부 추가
                if remaining_tokens > min_tokens:
                    # 토큰 수에 맞게 내용 자르기
                    optimized_content = self._truncate_content(content, remaining_tokens - min_tokens)
                    optimized_prompt.append({
                        "role": role,
                        "content": optimized_content
                    })
                    remaining_tokens -= min_tokens
                else:
                    # 공간 부족 - 메시지 생략
                    continue
        
        return optimized_prompt
    
    def _truncate_content(self, content: str, max_tokens: int) -> str:
        """콘텐츠를 토큰 수에 맞게 자릅니다."""
        if not content:
            return ""
        
        # 단위로 자르기 (문장, 단락 등)
        sentences = re.split(r'(?<=[.!?])\s+', content)
        truncated_content = ""
        current_tokens = 0
        
        for sentence in sentences:
            sentence_tokens = self.estimator.estimate_tokens(sentence)
            
            if current_tokens + sentence_tokens <= max_tokens:
                truncated_content += sentence + " "
                current_tokens += sentence_tokens
            else:
                break
        
        return truncated_content.strip()
    
    def suggest_batch_size(self, documents: List[Dict[str, str]], max_tokens: int) -> int:
        """
        배치 크기를 제안합니다.
        
        Args:
            documents: 문서 목록
            max_tokens: 최대 토큰 수
            
        Returns:
            제안된 배치 크기
        """
        if not documents:
            return 1
        
        # 평균 문서 크기 계산
        avg_content_length = sum(len(doc.get('content', '')) for doc in documents) / len(documents)
        avg_tokens = self.estimator.estimate_tokens(avg_content_length)
        
        # 프롬프트 오버헤드 고려 (약 100 토큰)
        prompt_overhead = 100
        available_tokens = max_tokens - prompt_overhead
        
        # 배치 크기 계산
        if avg_tokens > 0:
            suggested_batch_size = max(1, int(available_tokens / avg_tokens))
        else:
            suggested_batch_size = 1
        
        # 최대/최소 값 보정
        suggested_batch_size = max(1, min(suggested_batch_size, len(documents)))
        
        return suggested_batch_size


class TokenManager:
    """토큰 관리자 메인 클래스"""
    
    def __init__(self, config: TokenConfig):
        """
        초기화
        
        Args:
            config: 토큰 설정
        """
        self.config = config
        self.estimator = TokenEstimator()
        self.tracker = TokenTracker(config)
        self.optimizer = TokenOptimizer(config)
        
        # 현재 상태
        self.current_context_tokens = 0
        self.current_request_tokens = 0
        self.rate_limit_tokens = 0
        self.last_request_time = None
    
    def estimate_tokens(self, messages: List[Dict[str, str]]) -> int:
        """
        메시지의 토큰 수를 예측합니다.
        
        Args:
            messages: 메시지 목록
            
        Returns:
            예측된 토큰 수
        """
        return self.estimator.estimate_message_tokens(messages)
    
    def check_token_limit(self, tokens_required: int, limit_type: TokenLimitType = TokenLimitType.CONTEXT) -> bool:
        """
        토큰 한도를 확인합니다.
        
        Args:
            tokens_required: 필요한 토큰 수
            limit_type: 한도 유형
            
        Returns:
            한도 내 가능 여부
        """
        if limit_type == TokenLimitType.CONTEXT:
            return self.current_context_tokens + tokens_required <= self.config.max_context_length
        elif limit_type == TokenLimitType.REQUEST:
            return tokens_required <= self.config.max_request_tokens
        elif limit_type == TokenLimitType.RATE_LIMIT:
            return self.rate_limit_tokens + tokens_required <= self.config.rate_limit_tpm
        
        return False
    
    def get_remaining_tokens(self, limit_type: TokenLimitType = TokenLimitType.CONTEXT) -> int:
        """
        남은 토큰 수를 반환합니다.
        
        Args:
            limit_type: 한도 유형
            
        Returns:
            남은 토큰 수
        """
        try:
            if limit_type == TokenLimitType.CONTEXT:
                return max(0, self.config.max_context_length - self.current_context_tokens)
            elif limit_type == TokenLimitType.REQUEST:
                return max(0, self.config.max_request_tokens - self.current_request_tokens)
            elif limit_type == TokenLimitType.RATE_LIMIT:
                return max(0, self.config.rate_limit_tpm - self.rate_limit_tokens)
        except Exception as e:
            logger.warning(f"토큰 계산 오류: {e}")
            return 0
        
        return 0
    
    def update_token_usage(self, prompt_tokens: int, completion_tokens: int):
        """
        토큰 사용량을 업데이트합니다.
        
        Args:
            prompt_tokens: 프롬프트 토큰 수
            completion_tokens: 완성 토큰 수
        """
        try:
            request_tokens = prompt_tokens + completion_tokens
            
            # 추적기 업데이트
            self.tracker.record_token_usage(prompt_tokens, completion_tokens, request_tokens)
            
            # 현재 상태 업데이트
            self.current_context_tokens += prompt_tokens
            self.current_request_tokens = request_tokens
            self.rate_limit_tokens += request_tokens
            
            # 레이트 리밋 리셋 (1분 주기)
            if self.last_request_time:
                time_diff = (datetime.now() - self.last_request_time).total_seconds()
                if time_diff >= 60:
                    self.rate_limit_tokens = 0
            
            self.last_request_time = datetime.now()
        except Exception as e:
            logger.warning(f"토큰 사용량 업데이트 오류: {e}")
    
    def optimize_prompt(self, prompt: List[Dict[str, str]], max_tokens: int = None) -> List[Dict[str, str]]:
        """
        프롬프트를 최적화합니다.
        
        Args:
            prompt: 최적화할 프롬프트
            max_tokens: 최대 토큰 수
            
        Returns:
            최적화된 프롬프트
        """
        max_tokens = max_tokens or self.config.max_request_tokens
        return self.optimizer.optimize_prompt(prompt, max_tokens)
    
    def suggest_batch_size(self, documents: List[Dict[str, str]]) -> int:
        """
        배치 크기를 제안합니다.
        
        Args:
            documents: 문서 목록
            
        Returns:
            제안된 배치 크기
        """
        return self.optimizer.suggest_batch_size(documents, self.config.max_request_tokens)
    
    def get_stats(self) -> Dict[str, Any]:
        """통계 정보를 반환합니다."""
        return {
            "current_context_tokens": self.current_context_tokens,
            "current_request_tokens": self.current_request_tokens,
            "rate_limit_tokens": self.rate_limit_tokens,
            "usage_stats": self.tracker.get_usage_stats(),
            "config": self.config.__dict__
        }
    
    def get_prompt_tokens(self) -> int:
        """프롬프트 토큰 수를 반환합니다."""
        return self.tracker.tokens_by_type.get("prompt", 0)
    
    def get_completion_tokens(self) -> int:
        """완성 토큰 수를 반환합니다."""
        return self.tracker.tokens_by_type.get("completion", 0)
    
    def get_total_tokens(self) -> int:
        """총 토큰 수를 반환합니다."""
        return self.tracker.tokens_by_type.get("total", 0)


def create_token_manager(config: TokenConfig) -> TokenManager:
    """
    토큰 관리자를 생성합니다.
    
    Args:
        config: 토큰 설정
        
    Returns:
        TokenManager 인스턴스
    """
    return TokenManager(config)


# 테스트 코드
def test_token_manager():
    """토큰 관리자 테스트"""
    config = TokenConfig(
        max_context_length=128000,
        max_request_tokens=32000,
        rate_limit_rpm=60,
        rate_limit_tpm=100000,
        token_buffer=0.9,
        enable_optimization=True,
        track_usage_history=True,
        history_size=100
    )
    
    manager = create_token_manager(config)
    
    # 테스트 메시지
    test_messages = [
        {"role": "system", "content": "당신은 Syncfusion WinForms 전문가입니다."},
        {"role": "user", "content": "GridControl의 기본 사용법을 알려주세요."},
        {"role": "assistant", "content": "GridControl 사용법에 대한 자세한 설명입니다..."}
    ]
    
    # 토큰 예측
    estimated_tokens = manager.estimate_tokens(test_messages)
    print(f"예측된 토큰 수: {estimated_tokens}")
    
    # 한도 확인
    can_process = manager.check_token_limit(estimated_tokens)
    print(f"처리 가능 여부: {can_process}")
    
    # 프롬프트 최적화
    optimized_prompt = manager.optimize_prompt(test_messages, 1000)
    print(f"최적화된 프롬프트 길이: {len(optimized_prompt)}")
    
    # 통계 정보
    stats = manager.get_stats()
    print(f"통계 정보: {stats}")


if __name__ == "__main__":
    test_token_manager()