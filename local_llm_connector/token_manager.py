#!/usr/bin/env python3
"""
토큰 관리자 모듈

로컬 LLM의 토큰 사용량을 관리하고 최적화합니다.
프롬프트 토큰 제한을 적용하고 효율적인 토큰 사용을 보장합니다.
"""

import logging
import re
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime
import math

logger = logging.getLogger(__name__)


@dataclass
class TokenConfig:
    """토큰 관리 설정"""
    # 토큰 제한
    max_prompt_tokens: int = 4000
    max_response_tokens: int = 2000
    total_token_limit: int = 8000
    
    # 토큰 계산
    enable_token_counting: bool = True
    tokens_per_character: float = 0.25  # 평균 토큰/문자 비율
    
    # 토큰 최적화
    enable_prompt_optimization: bool = True
    enable_context_compression: bool = True
    compression_ratio: float = 0.7
    
    # 토큰 예산 관리
    enable_token_budget: bool = True
    token_budget_safety_margin: float = 0.9  # 90% 사용 시 경고
    
    # 로깅
    enable_detailed_token_logging: bool = False
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_prompt_tokens <= 0:
            raise ValueError("max_prompt_tokens는 양의 정수여야 합니다")
        if self.max_response_tokens <= 0:
            raise ValueError("max_response_tokens는 양의 정수여야 합니다")
        if self.total_token_limit <= 0:
            raise ValueError("total_token_limit는 양의 정수여야 합니다")
        if self.max_prompt_tokens + self.max_response_tokens > self.total_token_limit:
            raise ValueError("max_prompt_tokens + max_response_tokens는 total_token_limit보다 작아야 합니다")
        if not (0.0 < self.compression_ratio <= 1.0):
            raise ValueError("compression_ratio는 0.0과 1.0 사이여야 합니다")
        if not (0.0 < self.token_budget_safety_margin <= 1.0):
            raise ValueError("token_budget_safety_margin는 0.0과 1.0 사이여야 합니다")


class TokenManager:
    """토큰 관리자"""
    
    def __init__(self, config: TokenConfig = None):
        """
        초기화
        
        Args:
            config: 토큰 관리 설정
        """
        self.config = config or TokenConfig()
        
        # 토큰 사용량 추적
        self.token_usage = {
            "total_tokens": 0,
            "prompt_tokens": 0,
            "response_tokens": 0,
            "session_tokens": 0,
            "session_start_time": None
        }
        
        # 통계 정보
        self.stats = {
            "total_prompts_processed": 0,
            "total_tokens_used": 0,
            "average_tokens_per_prompt": 0.0,
            "compression_applied": 0,
            "optimization_applied": 0,
            "start_time": None
        }
    
    def count_tokens(self, text: str) -> int:
        """
        텍스트의 토큰 수를 계산
        
        Args:
            text: 토큰을 계산할 텍스트
            
        Returns:
            토큰 수
        """
        if not self.config.enable_token_counting:
            return 0
        
        try:
            # 간단한 토큰 계산 (실제로는 tiktoken 사용이 좋음)
            # 평균적으로 1토큰 = 4 characters
            token_count = int(len(text) * self.config.tokens_per_character)
            
            # 통계 업데이트
            self.token_usage["total_tokens"] += token_count
            
            return token_count
            
        except Exception as e:
            logger.error(f"토큰 계산 실패: {str(e)}")
            return 0
    
    def validate_token_budget(self, prompt_tokens: int, response_tokens: int) -> bool:
        """
        토큰 예산 검증
        
        Args:
            prompt_tokens: 프롬프트 토큰 수
            response_tokens: 응답 토큰 수
            
        Returns:
            예산 내인 경우 True
        """
        total_tokens = prompt_tokens + response_tokens
        
        # 전체 토큰 제한 검사
        if total_tokens > self.config.total_token_limit:
            logger.warning(f"토큰 제한 초과: {total_tokens} > {self.config.total_token_limit}")
            return False
        
        # 프롬프트 토큰 제한 검사
        if prompt_tokens > self.config.max_prompt_tokens:
            logger.warning(f"프롬프트 토큰 제한 초과: {prompt_tokens} > {self.config.max_prompt_tokens}")
            return False
        
        # 응답 토큰 제한 검사
        if response_tokens > self.config.max_response_tokens:
            logger.warning(f"응답 토큰 제한 초과: {response_tokens} > {self.config.max_response_tokens}")
            return False
        
        # 예산 안전 마진 검사
        if self.config.enable_token_budget:
            safety_threshold = self.config.total_token_limit * self.config.token_budget_safety_margin
            if total_tokens > safety_threshold:
                logger.warning(f"토큰 예산 안전 마진 초과: {total_tokens} > {safety_threshold}")
        
        return True
    
    def truncate_prompt(self, prompt: str, max_tokens: int) -> str:
        """
        프롬프트 토큰 제한에 맞게 자르기
        
        Args:
            prompt: 원본 프롬프트
            max_tokens: 최대 토큰 수
            
        Returns:
            자른 프롬프트
        """
        if not self.config.enable_token_counting:
            return prompt
        
        try:
            current_tokens = self.count_tokens(prompt)
            
            if current_tokens <= max_tokens:
                return prompt
            
            # 프롬프트를 의미 있는 단위로 자르기
            truncated_prompt = self._truncate_by_sentences(prompt, max_tokens)
            
            # 통계 업데이트
            self.stats["optimization_applied"] += 1
            
            if self.config.enable_detailed_token_logging:
                original_tokens = current_tokens
                final_tokens = self.count_tokens(truncated_prompt)
                logger.info(f"프롬프트 자르기 적용: {original_tokens} -> {final_tokens} 토큰")
            
            return truncated_prompt
            
        except Exception as e:
            logger.error(f"프롬프트 자르기 실패: {str(e)}")
            return prompt[:max_tokens * 4]  # 간단한 자르기
    
    def _truncate_by_sentences(self, text: str, max_tokens: int) -> str:
        """
        문장 단위로 프롬프트 자르기
        
        Args:
            text: 원본 텍스트
            max_tokens: 최대 토큰 수
            
        Returns:
            자른 텍스트
        """
        try:
            # 문장 분리
            sentences = re.split(r'(?<=[.!?])\s+', text)
            
            if not sentences:
                return text[:max_tokens * 4]
            
            result = []
            current_tokens = 0
            
            for sentence in sentences:
                sentence_tokens = self.count_tokens(sentence)
                
                if current_tokens + sentence_tokens <= max_tokens:
                    result.append(sentence)
                    current_tokens += sentence_tokens
                else:
                    break
            
            return ' '.join(result)
            
        except Exception as e:
            logger.error(f"문장 단위 자르기 실패: {str(e)}")
            return text[:max_tokens * 4]
    
    def compress_context(self, context: str, max_tokens: int) -> str:
        """
        컨텍스트 압축
        
        Args:
            context: 원본 컨텍스트
            max_tokens: 최대 토큰 수
            
        Returns:
            압축된 컨텍스트
        """
        if not self.config.enable_context_compression:
            return context
        
        try:
            current_tokens = self.count_tokens(context)
            
            if current_tokens <= max_tokens:
                return context
            
            # 압축 비율 계산
            target_tokens = int(max_tokens * self.config.compression_ratio)
            
            # 컨텍스트 압축
            compressed_context = self._compress_text(context, target_tokens)
            
            # 통계 업데이트
            self.stats["compression_applied"] += 1
            
            if self.config.enable_detailed_token_logging:
                original_tokens = current_tokens
                final_tokens = self.count_tokens(compressed_context)
                compression_ratio = final_tokens / original_tokens
                logger.info(f"컨텍스트 압축 적용: {original_tokens} -> {final_tokens} 토큰 (비율: {compression_ratio:.2f})")
            
            return compressed_context
            
        except Exception as e:
            logger.error(f"컨텍스트 압축 실패: {str(e)}")
            return self.truncate_prompt(context, max_tokens)
    
    def _compress_text(self, text: str, target_tokens: int) -> str:
        """
        텍스트 압축
        
        Args:
            text: 원본 텍스트
            target_tokens: 목표 토큰 수
            
        Returns:
            압축된 텍스트
        """
        try:
            # 간단한 압축: 중요한 문장 유지
            sentences = re.split(r'(?<=[.!?])\s+', text)
            
            if len(sentences) <= 2:
                return self.truncate_prompt(text, target_tokens)
            
            # 문장 중요도 평가 (간단한 구현)
            important_sentences = []
            for sentence in sentences:
                # 중요한 키워드 포함 여부 확인
                important_keywords = ['important', 'key', 'main', 'essential', 'critical', 'important']
                if any(keyword in sentence.lower() for keyword in important_keywords):
                    important_sentences.append(sentence)
                elif len(important_sentences) < len(sentences) * 0.3:  # 30%는 유지
                    important_sentences.append(sentence)
            
            # 중요 문장으로 구성
            compressed_text = ' '.join(important_sentences)
            
            # 토큰 제한 초과 시 추가로 자르기
            if self.count_tokens(compressed_text) > target_tokens:
                compressed_text = self.truncate_prompt(compressed_text, target_tokens)
            
            return compressed_text
            
        except Exception as e:
            logger.error(f"텍스트 압축 실패: {str(e)}")
            return self.truncate_prompt(text, target_tokens)
    
    def optimize_prompt(self, prompt: str) -> str:
        """
        프롬프트 최적화
        
        Args:
            prompt: 원본 프롬프트
            
        Returns:
            최적화된 프롬프트
        """
        if not self.config.enable_prompt_optimization:
            return prompt
        
        try:
            optimized_prompt = prompt
            
            # 중복 제거
            optimized_prompt = self._remove_duplicates(optimized_prompt)
            
            # 불필요한 공백 제거
            optimized_prompt = ' '.join(optimized_prompt.split())
            
            # 통계 업데이트
            self.stats["optimization_applied"] += 1
            
            return optimized_prompt
            
        except Exception as e:
            logger.error(f"프롬프트 최적화 실패: {str(e)}")
            return prompt
    
    def _remove_duplicates(self, text: str) -> str:
        """
        중복된 문장 제거
        
        Args:
            text: 원본 텍스트
            
        Returns:
            중복 제거된 텍스트
        """
        try:
            sentences = re.split(r'(?<=[.!?])\s+', text)
            
            if len(sentences) <= 1:
                return text
            
            # 중복 제거
            unique_sentences = []
            seen_sentences = set()
            
            for sentence in sentences:
                normalized_sentence = sentence.strip().lower()
                if normalized_sentence not in seen_sentences:
                    unique_sentences.append(sentence)
                    seen_sentences.add(normalized_sentence)
            
            return ' '.join(unique_sentences)
            
        except Exception as e:
            logger.error(f"중복 제거 실패: {str(e)}")
            return text
    
    def get_token_limit(self) -> int:
        """
        토큰 제한 반환
        
        Returns:
            토큰 제한
        """
        return self.config.max_prompt_tokens
    
    def get_token_usage(self) -> Dict[str, int]:
        """
        토큰 사용량 정보 반환
        
        Returns:
            토큰 사용량 정보
        """
        return self.token_usage.copy()
    
    def reset_session_tokens(self):
        """세션 토큰 사용량 초기화"""
        self.token_usage["session_tokens"] = 0
        self.token_usage["session_start_time"] = datetime.now()
    
    def start_session(self):
        """세션 시작"""
        self.token_usage["session_tokens"] = 0
        self.token_usage["session_start_time"] = datetime.now()
    
    def end_session(self) -> Dict[str, Any]:
        """
        세션 종료 및 통계 반환
        
        Returns:
            세션 통계 정보
        """
        session_stats = {
            "session_tokens": self.token_usage["session_tokens"],
            "session_duration": (datetime.now() - self.token_usage["session_start_time"]).total_seconds() if self.token_usage["session_start_time"] else 0,
            "average_tokens_per_second": self.token_usage["session_tokens"] / ((datetime.now() - self.token_usage["session_start_time"]).total_seconds() if self.token_usage["session_start_time"] and (datetime.now() - self.token_usage["session_start_time"]).total_seconds() > 0 else 1)
        }
        
        # 세션 초기화
        self.reset_session_tokens()
        
        return session_stats
    
    def update_prompt_stats(self, prompt_tokens: int, response_tokens: int):
        """
        프롬프트 통계 업데이트
        
        Args:
            prompt_tokens: 프롬프트 토큰 수
            response_tokens: 응답 토큰 수
        """
        self.stats["total_prompts_processed"] += 1
        self.stats["total_tokens_used"] += prompt_tokens + response_tokens
        self.token_usage["prompt_tokens"] += prompt_tokens
        self.token_usage["response_tokens"] += response_tokens
        self.token_usage["session_tokens"] += prompt_tokens + response_tokens
        
        # 평균 토큰 수 계산
        if self.stats["total_prompts_processed"] > 0:
            self.stats["average_tokens_per_prompt"] = self.stats["total_tokens_used"] / self.stats["total_prompts_processed"]
    
    def get_stats(self) -> Dict[str, Any]:
        """통계 정보 반환"""
        if self.stats["start_time"]:
            elapsed_time = (datetime.now() - self.stats["start_time"]).total_seconds()
        else:
            elapsed_time = 0
        
        return {
            **self.stats,
            **self.token_usage,
            "elapsed_time": elapsed_time,
            "config": {
                "max_prompt_tokens": self.config.max_prompt_tokens,
                "max_response_tokens": self.config.max_response_tokens,
                "total_token_limit": self.config.total_token_limit,
                "enable_token_counting": self.config.enable_token_counting,
                "enable_prompt_optimization": self.config.enable_prompt_optimization,
                "enable_context_compression": self.config.enable_context_compression
            }
        }


def create_token_manager(config: TokenConfig = None) -> TokenManager:
    """
    토큰 관리자 생성
    
    Args:
        config: 토큰 관리 설정
        
    Returns:
        TokenManager 인스턴스
    """
    config = config or TokenConfig()
    return TokenManager(config)