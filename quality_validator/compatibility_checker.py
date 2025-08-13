#!/usr/bin/env python3
"""
Unsloth 호환성 검증 모듈
Unsloth 프레임워크와의 호환성을 검증하는 기능을 제공합니다.
"""

import re
import json
import logging
from typing import List, Dict, Any, Optional, Set, Tuple, Union
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class CompatibilityCheckerConfig:
    """호환성 검증기 설정"""
    # 토큰 길이 검증 설정
    min_token_length: int = 50
    max_token_length: int = 4096
    strict_token_validation: bool = True
    
    # 시퀀스 구조 검증 설정
    required_conversation_structure: bool = True
    min_conversation_turns: int = 2
    max_conversation_turns: int = 20
    
    # EOS 토큰 검증 설정
    eos_token_validation: bool = True
    valid_eos_tokens: List[str] = field(default_factory=lambda: ["</s>", "<|im_end|>", "<|endoftext|>"])
    
    # 메모리 효율성 검증 설정
    memory_efficiency_check: bool = True
    max_memory_usage_mb: int = 8192
    optimization_level: str = "4bit"  # 4bit, 8bit, 16bit
    
    # 포맷 호환성 검증 설정
    format_validation: bool = True
    supported_formats: List[str] = field(default_factory=lambda: ["sharegpt", "alpaca", "openai"])
    
    # 성능 최적화 설정
    batch_size: int = 100
    max_workers: int = 4
    use_cache: bool = True


@dataclass
class CompatibilityResult:
    """호환성 검증 결과"""
    is_compatible: bool = True
    compatibility_score: float = 1.0
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    detailed_checks: Dict[str, Any] = field(default_factory=dict)
    validation_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class CompatibilityChecker:
    """Unsloth 호환성 검증기 클래스"""
    
    def __init__(self, config: Optional[CompatibilityCheckerConfig] = None):
        """
        호환성 검증기를 초기화합니다.
        
        Args:
            config: 호환성 검증기 설정
        """
        self.config = config or CompatibilityCheckerConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 토큰화 설정
        self._setup_tokenization()
        
        # 포맷 검증 패턴
        self._setup_format_patterns()
        
        # 최적화 설정
        self._setup_optimization_settings()
    
    def _setup_tokenization(self):
        """토큰화 설정을 초기화합니다."""
        # 간단한 토큰화 패턴 (실제 토크나이저 대체용)
        self.token_patterns = {
            'words': re.compile(r'\b\w+\b'),
            'punctuation': re.compile(r'[^\w\s]'),
            'whitespace': re.compile(r'\s+'),
            'sentences': re.compile(r'[.!?]+')
        }
    
    def _setup_format_patterns(self):
        """포맷 검증 패턴을 설정합니다."""
        # ShareGPT 포맷 검증 패턴
        self.sharegpt_patterns = {
            'required_fields': ['conversations'],
            'conversation_structure': [
                {'from': 'system', 'value': r'.*'},
                {'from': 'human', 'value': r'.*'},
                {'from': 'gpt', 'value': r'.*'}
            ]
        }
        
        # Alpaca 포맷 검증 패턴
        self.alpaca_patterns = {
            'required_fields': ['instruction', 'input', 'output'],
            'instruction_length': {'min': 10, 'max': 1000},
            'output_length': {'min': 10, 'max': 2000}
        }
        
        # OpenAI 포맷 검증 패턴
        self.openai_patterns = {
            'required_fields': ['messages'],
            'message_structure': [
                {'role': 'system', 'content': r'.*'},
                {'role': 'user', 'content': r'.*'},
                {'role': 'assistant', 'content': r'.*'}
            ]
        }
    
    def _setup_optimization_settings(self):
        """최적화 설정을 초기화합니다."""
        # 4-bit 양자화 설정
        self.quantization_settings = {
            '4bit': {
                'memory_efficiency': 'high',
                'performance_impact': 'low',
                'supported_precision': ['int4', 'nf4']
            },
            '8bit': {
                'memory_efficiency': 'medium',
                'performance_impact': 'medium',
                'supported_precision': ['int8']
            },
            '16bit': {
                'memory_efficiency': 'low',
                'performance_impact': 'high',
                'supported_precision': ['float16', 'bfloat16']
            }
        }
    
    def check_compatibility(self, item: Dict[str, Any], item_format: str) -> CompatibilityResult:
        """
        아이템의 Unsloth 호환성을 검증합니다.
        
        Args:
            item: 호환성 검증할 아이템
            item_format: 아이템 포맷 (sharegpt, alpaca, openai)
            
        Returns:
            호환성 검증 결과
        """
        result = CompatibilityResult()
        
        if not item:
            result.is_compatible = False
            result.issues.append("빈 아이템")
            result.compatibility_score = 0.0
            return result
        
        # 포맷 검증
        if self.config.format_validation:
            format_result = self._validate_format(item, item_format)
            if not format_result.is_compatible:
                result.is_compatible = False
                result.compatibility_score = format_result.compatibility_score
                result.issues.extend(format_result.issues)
                result.warnings.extend(format_result.warnings)
                result.detailed_checks['format_validation'] = format_result.detailed_checks
        
        # 토큰 길이 검증
        token_result = self._validate_token_length(item, item_format)
        result.detailed_checks['token_length'] = token_result.detailed_checks
        
        if not token_result.is_compatible:
            result.is_compatible = False
            result.compatibility_score *= token_result.compatibility_score
            result.issues.extend(token_result.issues)
            result.warnings.extend(token_result.warnings)
        
        # 시퀀스 구조 검증
        structure_result = self._validate_sequence_structure(item, item_format)
        result.detailed_checks['sequence_structure'] = structure_result.detailed_checks
        
        if not structure_result.is_compatible:
            result.is_compatible = False
            result.compatibility_score *= structure_result.compatibility_score
            result.issues.extend(structure_result.issues)
            result.warnings.extend(structure_result.warnings)
        
        # EOS 토큰 검증
        if self.config.eos_token_validation:
            eos_result = self._validate_eos_token(item, item_format)
            result.detailed_checks['eos_token'] = eos_result.detailed_checks
            
            if not eos_result.is_compatible:
                result.is_compatible = False
                result.compatibility_score *= eos_result.compatibility_score
                result.issues.extend(eos_result.issues)
                result.warnings.extend(eos_result.warnings)
        
        # 메모리 효율성 검증
        if self.config.memory_efficiency_check:
            memory_result = self._validate_memory_efficiency(item, item_format)
            result.detailed_checks['memory_efficiency'] = memory_result.detailed_checks
            
            if not memory_result.is_compatible:
                result.is_compatible = False
                result.compatibility_score *= memory_result.compatibility_score
                result.issues.extend(memory_result.issues)
                result.warnings.extend(memory_result.warnings)
        
        # 최종 호환성 점수 계산
        result.compatibility_score = max(0.0, min(1.0, result.compatibility_score))
        
        # 권장사항 생성
        self._generate_recommendations(result)
        
        return result
    
    def _validate_format(self, item: Dict[str, Any], item_format: str) -> CompatibilityResult:
        """포맷을 검증합니다."""
        result = CompatibilityResult()
        
        if item_format not in self.config.supported_formats:
            result.is_compatible = False
            result.issues.append(f"지원되지 않는 포맷: {item_format}")
            result.compatibility_score = 0.0
            return result
        
        # 포맷별 필드 검증
        if item_format == "sharegpt":
            return self._validate_sharegpt_format(item)
        elif item_format == "alpaca":
            return self._validate_alpaca_format(item)
        elif item_format == "openai":
            return self._validate_openai_format(item)
        else:
            result.is_compatible = False
            result.issues.append(f"알 수 없는 포맷: {item_format}")
            result.compatibility_score = 0.0
            return result
    
    def _validate_sharegpt_format(self, item: Dict[str, Any]) -> CompatibilityResult:
        """ShareGPT 포맷을 검증합니다."""
        result = CompatibilityResult()
        
        # 필수 필드 검증
        if 'conversations' not in item:
            result.is_compatible = False
            result.issues.append("필수 필드 'conversations'가 없습니다")
            result.compatibility_score = 0.0
            return result
        
        conversations = item['conversations']
        
        if not isinstance(conversations, list):
            result.is_compatible = False
            result.issues.append("'conversations'는 리스트 형식이어야 합니다")
            result.compatibility_score = 0.0
            return result
        
        # 대화 턴 수 검증
        if len(conversations) < self.config.min_conversation_turns:
            result.is_compatible = False
            result.issues.append(f"대화 턴 수가 너무 적음: {len(conversations)} < {self.config.min_conversation_turns}")
            result.compatibility_score = 0.5
        
        if len(conversations) > self.config.max_conversation_turns:
            result.warnings.append(f"대화 턴 수가 많음: {len(conversations)} > {self.config.max_conversation_turns}")
            result.compatibility_score *= 0.9
        
        # 각 대화 턴 검증
        for i, conv in enumerate(conversations):
            if not isinstance(conv, dict):
                result.is_compatible = False
                result.issues.append(f"대화 턴 {i}: 딕셔너리 형식이 아님")
                result.compatibility_score *= 0.8
                continue
            
            if 'from' not in conv or 'value' not in conv:
                result.is_compatible = False
                result.issues.append(f"대화 턴 {i}: 'from' 또는 'value' 필드가 없음")
                result.compatibility_score *= 0.8
                continue
            
            # 역할 검증
            role = conv['from']
            if role not in ['system', 'human', 'gpt']:
                result.warnings.append(f"대화 턴 {i}: 알 수 없는 역할: {role}")
                result.compatibility_score *= 0.95
            
            # 값 검증
            value = conv['value']
            if not isinstance(value, str) or not value.strip():
                result.is_compatible = False
                result.issues.append(f"대화 턴 {i}: 비어있거나 유효하지 않은 값")
                result.compatibility_score *= 0.8
        
        result.detailed_checks = {
            'conversation_count': len(conversations),
            'valid_turns': sum(1 for conv in conversations if isinstance(conv, dict) and 'from' in conv and 'value' in conv)
        }
        
        return result
    
    def _validate_alpaca_format(self, item: Dict[str, Any]) -> CompatibilityResult:
        """Alpaca 포맷을 검증합니다."""
        result = CompatibilityResult()
        
        # 필수 필드 검증
        required_fields = ['instruction', 'input', 'output']
        for field in required_fields:
            if field not in item:
                result.is_compatible = False
                result.issues.append(f"필수 필드 '{field}'가 없습니다")
                result.compatibility_score *= 0.5
        
        # 필드 값 검증
        if 'instruction' in item:
            instruction = str(item['instruction'])
            if len(instruction) < self.alpaca_patterns['instruction_length']['min']:
                result.warnings.append("지시문이 너무 짧음")
                result.compatibility_score *= 0.9
            elif len(instruction) > self.alpaca_patterns['instruction_length']['max']:
                result.warnings.append("지시문이 너김")
                result.compatibility_score *= 0.9
        
        if 'output' in item:
            output = str(item['output'])
            if len(output) < self.alpaca_patterns['output_length']['min']:
                result.warnings.append("출력이 너무 짧음")
                result.compatibility_score *= 0.9
            elif len(output) > self.alpaca_patterns['output_length']['max']:
                result.warnings.append("출력이 너김")
                result.compatibility_score *= 0.9
        
        result.detailed_checks = {
            'instruction_length': len(str(item.get('instruction', ''))),
            'input_length': len(str(item.get('input', ''))),
            'output_length': len(str(item.get('output', '')))
        }
        
        return result
    
    def _validate_openai_format(self, item: Dict[str, Any]) -> CompatibilityResult:
        """OpenAI 포맷을 검증합니다."""
        result = CompatibilityResult()
        
        # 필수 필드 검증
        if 'messages' not in item:
            result.is_compatible = False
            result.issues.append("필수 필드 'messages'가 없습니다")
            result.compatibility_score = 0.0
            return result
        
        messages = item['messages']
        
        if not isinstance(messages, list):
            result.is_compatible = False
            result.issues.append("'messages'는 리스트 형식이어야 합니다")
            result.compatibility_score = 0.0
            return result
        
        # 메시지 수 검증
        if len(messages) < self.config.min_conversation_turns:
            result.is_compatible = False
            result.issues.append(f"메시지 수가 너무 적음: {len(messages)} < {self.config.min_conversation_turns}")
            result.compatibility_score = 0.5
        
        if len(messages) > self.config.max_conversation_turns:
            result.warnings.append(f"메시지 수가 많음: {len(messages)} > {self.config.max_conversation_turns}")
            result.compatibility_score *= 0.9
        
        # 각 메시지 검증
        for i, msg in enumerate(messages):
            if not isinstance(msg, dict):
                result.is_compatible = False
                result.issues.append(f"메시지 {i}: 딕셔너리 형식이 아님")
                result.compatibility_score *= 0.8
                continue
            
            if 'role' not in msg or 'content' not in msg:
                result.is_compatible = False
                result.issues.append(f"메시지 {i}: 'role' 또는 'content' 필드가 없음")
                result.compatibility_score *= 0.8
                continue
            
            # 역할 검증
            role = msg['role']
            if role not in ['system', 'user', 'assistant']:
                result.warnings.append(f"메시지 {i}: 알 수 없는 역할: {role}")
                result.compatibility_score *= 0.95
            
            # 값 검증
            content = msg['content']
            if not isinstance(content, str) or not content.strip():
                result.is_compatible = False
                result.issues.append(f"메시지 {i}: 비어있거나 유효하지 않은 내용")
                result.compatibility_score *= 0.8
        
        result.detailed_checks = {
            'message_count': len(messages),
            'valid_messages': sum(1 for msg in messages if isinstance(msg, dict) and 'role' in msg and 'content' in msg)
        }
        
        return result
    
    def _validate_token_length(self, item: Dict[str, Any], item_format: str) -> CompatibilityResult:
        """토큰 길이를 검증합니다."""
        result = CompatibilityResult()
        
        # 텍스트 추출
        text = self._extract_text_for_tokenization(item, item_format)
        
        if not text:
            result.is_compatible = False
            result.issues.append("토큰화할 텍스트가 없음")
            result.compatibility_score = 0.0
            return result
        
        # 토큰 수 계산 (간소화된 방식)
        token_count = self._estimate_token_count(text)
        
        result.detailed_checks = {
            'token_count': token_count,
            'text_length': len(text)
        }
        
        # 토큰 길이 검증
        if token_count < self.config.min_token_length:
            result.is_compatible = False
            result.issues.append(f"토큰 수가 너무 적음: {token_count} < {self.config.min_token_length}")
            result.compatibility_score = 0.3
        
        if token_count > self.config.max_token_length:
            if self.config.strict_token_validation:
                result.is_compatible = False
                result.issues.append(f"토큰 수가 너김: {token_count} > {self.config.max_token_length}")
                result.compatibility_score = 0.0
            else:
                result.warnings.append(f"토큰 수가 너김: {token_count} > {self.config.max_token_length}")
                result.compatibility_score *= 0.7
        
        # 적절한 토큰 길이 범위 확인
        if self.config.min_token_length <= token_count <= self.config.max_token_length:
            result.compatibility_score = 1.0
        elif token_count < self.config.min_token_length:
            # 최소 토큰 수에 비례하여 점수 조정
            ratio = token_count / self.config.min_token_length
            result.compatibility_score = max(0.3, ratio)
        
        return result
    
    def _validate_sequence_structure(self, item: Dict[str, Any], item_format: str) -> CompatibilityResult:
        """시퀀스 구조를 검증합니다."""
        result = CompatibilityResult()
        
        if item_format == "sharegpt":
            return self._validate_sharegpt_sequence(item)
        elif item_format == "alpaca":
            return self._validate_alpaca_sequence(item)
        elif item_format == "openai":
            return self._validate_openai_sequence(item)
        else:
            result.is_compatible = False
            result.issues.append(f"알 수 없는 포맷: {item_format}")
            result.compatibility_score = 0.0
            return result
    
    def _validate_sharegpt_sequence(self, item: Dict[str, Any]) -> CompatibilityResult:
        """ShareGPT 시퀀스 구조를 검증합니다."""
        result = CompatibilityResult()
        
        conversations = item.get('conversations', [])
        
        # 시퀀스 순서 검증
        expected_sequence = ['system', 'human', 'gpt']
        actual_sequence = [conv.get('from', '') for conv in conversations]
        
        # 기본 시퀀스 검증
        if len(actual_sequence) >= 3:
            for i in range(min(3, len(actual_sequence))):
                if actual_sequence[i] != expected_sequence[i]:
                    result.warnings.append(f"시퀀스 순서 불일치: 기대 {expected_sequence[i]}, 실제 {actual_sequence[i]}")
                    result.compatibility_score *= 0.95
        
        # 연속된 역할 검증
        for i in range(1, len(actual_sequence)):
            if actual_sequence[i] == actual_sequence[i-1]:
                result.warnings.append(f"연속된 동일 역할: {actual_sequence[i]}")
                result.compatibility_score *= 0.9
        
        result.detailed_checks = {
            'sequence': actual_sequence,
            'has_system': 'system' in actual_sequence,
            'has_human': 'human' in actual_sequence,
            'has_gpt': 'gpt' in actual_sequence
        }
        
        return result
    
    def _validate_alpaca_sequence(self, item: Dict[str, Any]) -> CompatibilityResult:
        """Alpaca 시퀀스 구조를 검증합니다."""
        result = CompatibilityResult()
        
        # Alpaca는 특정 시퀀스 구조를 요구하지 않음
        # 대신 필드 존재 여부만 검증
        result.detailed_checks = {
            'has_instruction': 'instruction' in item,
            'has_input': 'input' in item,
            'has_output': 'output' in item
        }
        
        return result
    
    def _validate_openai_sequence(self, item: Dict[str, Any]) -> CompatibilityResult:
        """OpenAI 시퀀스 구조를 검증합니다."""
        result = CompatibilityResult()
        
        messages = item.get('messages', [])
        
        # 시퀀스 순서 검증
        expected_sequence = ['system', 'user', 'assistant']
        actual_sequence = [msg.get('role', '') for msg in messages]
        
        # 기본 시퀀스 검증
        if len(actual_sequence) >= 3:
            for i in range(min(3, len(actual_sequence))):
                if actual_sequence[i] != expected_sequence[i]:
                    result.warnings.append(f"시퀀스 순서 불일치: 기대 {expected_sequence[i]}, 실제 {actual_sequence[i]}")
                    result.compatibility_score *= 0.95
        
        # 연속된 역할 검증
        for i in range(1, len(actual_sequence)):
            if actual_sequence[i] == actual_sequence[i-1]:
                result.warnings.append(f"연속된 동일 역할: {actual_sequence[i]}")
                result.compatibility_score *= 0.9
        
        result.detailed_checks = {
            'sequence': actual_sequence,
            'has_system': 'system' in actual_sequence,
            'has_user': 'user' in actual_sequence,
            'has_assistant': 'assistant' in actual_sequence
        }
        
        return result
    
    def _validate_eos_token(self, item: Dict[str, Any], item_format: str) -> CompatibilityResult:
        """EOS 토큰을 검증합니다."""
        result = CompatibilityResult()
        
        # 텍스트 추출
        text = self._extract_text_for_tokenization(item, item_format)
        
        if not text:
            result.is_compatible = False
            result.issues.append("EOS 토큰 검증을 위한 텍스트가 없음")
            result.compatibility_score = 0.0
            return result
        
        # EOS 토큰 검증
        found_eos_tokens = []
        for eos_token in self.config.valid_eos_tokens:
            if eos_token in text:
                found_eos_tokens.append(eos_token)
        
        result.detailed_checks = {
            'found_eos_tokens': found_eos_tokens,
            'total_eos_tokens': len(found_eos_tokens)
        }
        
        if not found_eos_tokens:
            result.warnings.append(f"유효한 EOS 토큰을 찾을 수 없음: {self.config.valid_eos_tokens}")
            result.compatibility_score = 0.8
        else:
            result.compatibility_score = 1.0
        
        return result
    
    def _validate_memory_efficiency(self, item: Dict[str, Any], item_format: str) -> CompatibilityResult:
        """메모리 효율성을 검증합니다."""
        result = CompatibilityResult()
        
        # 텍스트 추출
        text = self._extract_text_for_tokenization(item, item_format)
        
        if not text:
            result.is_compatible = False
            result.issues.append("메모리 효율성 검증을 위한 텍스트가 없음")
            result.compatibility_score = 0.0
            return result
        
        # 메모리 사용량 추정
        estimated_memory_mb = self._estimate_memory_usage(text, item_format)
        
        result.detailed_checks = {
            'estimated_memory_mb': estimated_memory_mb,
            'text_length': len(text),
            'token_count': self._estimate_token_count(text)
        }
        
        # 메모리 사용량 검증
        if estimated_memory_mb > self.config.max_memory_usage_mb:
            result.warnings.append(f"예상 메모리 사용량이 높음: {estimated_memory_mb:.2f}MB > {self.config.max_memory_usage_mb}MB")
            result.compatibility_score *= 0.8
        
        # 최적화 수준별 검증
        optimization_settings = self.quantization_settings.get(self.config.optimization_level, {})
        if optimization_settings:
            efficiency_score = optimization_settings.get('memory_efficiency', 'medium')
            
            if efficiency_score == 'high':
                result.compatibility_score *= 1.0
            elif efficiency_score == 'medium':
                result.compatibility_score *= 0.9
            else:
                result.compatibility_score *= 0.8
        
        return result
    
    def _extract_text_for_tokenization(self, item: Dict[str, Any], item_format: str) -> str:
        """토큰화를 위한 텍스트를 추출합니다."""
        if item_format == "sharegpt":
            text_parts = []
            for conv in item.get('conversations', []):
                text_parts.append(str(conv.get('value', '')))
            return ' '.join(text_parts)
        
        elif item_format == "alpaca":
            text_parts = [
                str(item.get('instruction', '')),
                str(item.get('input', '')),
                str(item.get('output', ''))
            ]
            return ' '.join(text_parts)
        
        elif item_format == "openai":
            text_parts = []
            for msg in item.get('messages', []):
                text_parts.append(str(msg.get('content', '')))
            return ' '.join(text_parts)
        
        else:
            return str(item)
    
    def _estimate_token_count(self, text: str) -> int:
        """토큰 수를 추정합니다."""
        # 간단한 토큰 수 추정 (실제 토크나이저 대체용)
        words = self.token_patterns['words'].findall(text)
        return len(words)
    
    def _estimate_memory_usage(self, text: str, item_format: str) -> float:
        """메모리 사용량을 추정합니다."""
        # 텍스트 길이를 기반으로 메모리 사용량 추정
        text_length = len(text)
        token_count = self._estimate_token_count(text)
        
        # 기본 메모리 사용량 계산
        base_memory_mb = (text_length * 0.001) + (token_count * 0.004)
        
        # 포맷별 추가 메모리 요구사항
        format_multiplier = {
            'sharegpt': 1.2,
            'alpaca': 1.0,
            'openai': 1.1
        }
        
        multiplier = format_multiplier.get(item_format, 1.0)
        
        return base_memory_mb * multiplier
    
    def _generate_recommendations(self, result: CompatibilityResult):
        """권장사항을 생성합니다."""
        recommendations = []
        
        # 호환성 점수 기반 권장사항
        if result.compatibility_score < 0.5:
            recommendations.append("아이템을 수정하거나 제거하는 것을 권장합니다")
        elif result.compatibility_score < 0.8:
            recommendations.append("아이템을 개선하는 것을 권장합니다")
        
        # 이슈 기반 권장사항
        if any('토큰 수' in issue for issue in result.issues):
            recommendations.append("토큰 수를 조절하기 위해 텍스트를 압축하거나 요약하세요")
        
        if any('시퀀스' in issue for issue in result.issues):
            recommendations.append("대화 시퀀스를 올바른 순서로 재구성하세요")
        
        if any('EOS 토큰' in issue for issue in result.warnings):
            recommendations.append(f"EOS 토큰을 추가하세요: {self.config.valid_eos_tokens}")
        
        if any('메모리' in issue for issue in result.warnings):
            recommendations.append("메모리 효율성을 위해 4-bit 양자화를 사용하세요")
        
        result.recommendations = recommendations
    
    def batch_check_compatibility(self, items: List[Dict[str, Any]], item_format: str) -> List[CompatibilityResult]:
        """
        배치로 호환성을 검증합니다.
        
        Args:
            items: 호환성 검증할 아이템 목록
            item_format: 아이템 포맷
            
        Returns:
            호환성 검증 결과 목록
        """
        results = []
        
        for i, item in enumerate(items):
            try:
                result = self.check_compatibility(item, item_format)
                results.append(result)
                
                # 진행률 로깅
                if (i + 1) % 100 == 0:
                    self.logger.info(f"Processed {i + 1}/{len(items)} items")
                    
            except Exception as e:
                self.logger.error(f"Error checking compatibility for item {i}: {e}")
                # 오류 발생 시 기본 결과 반환
                error_result = CompatibilityResult()
                error_result.is_compatible = False
                error_result.compatibility_score = 0.0
                error_result.issues.append(f"처리 오류: {str(e)}")
                results.append(error_result)
        
        return results
    
    def get_compatibility_summary(self, results: List[CompatibilityResult]) -> Dict[str, Any]:
        """호환성 요약 정보를 생성합니다."""
        if not results:
            return {"total": 0, "compatible": 0, "incompatible": 0}
        
        total = len(results)
        compatible_count = sum(1 for r in results if r.is_compatible)
        incompatible_count = total - compatible_count
        
        # 평균 호환성 점수
        average_score = sum(r.compatibility_score for r in results) / total
        
        # 호환성 등급별 통계
        compatibility_grades = {
            "excellent": sum(1 for r in results if r.compatibility_score >= 0.9),
            "good": sum(1 for r in results if 0.7 <= r.compatibility_score < 0.9),
            "fair": sum(1 for r in results if 0.5 <= r.compatibility_score < 0.7),
            "poor": sum(1 for r in results if r.compatibility_score < 0.5)
        }
        
        # 이슈 통계
        issues_count = sum(len(r.issues) for r in results)
        warnings_count = sum(len(r.warnings) for r in results)
        recommendations_count = sum(len(r.recommendations) for r in results)
        
        return {
            "total": total,
            "compatible": compatible_count,
            "incompatible": incompatible_count,
            "compatibility_rate": compatible_count / total,
            "average_score": average_score,
            "compatibility_grades": compatibility_grades,
            "issues_count": issues_count,
            "warnings_count": warnings_count,
            "recommendations_count": recommendations_count,
            "timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    # 테스트 데이터
    test_items = [
        {
            "conversations": [
                {"from": "system", "value": "Syncfusion WinForms 전문가"},
                {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."}
            ]
        },
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
            "input": "초보자도 이해할 수 있도록 설명해주세요.",
            "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용"
        },
        {
            "messages": [
                {"role": "system", "content": "Syncfusion WinForms 전문가"},
                {"role": "user", "content": "Chart 컴포넌트 사용법을 알려주세요."},
                {"role": "assistant", "content": "Chart 컴포넌트 사용법은 다음과 같습니다..."}
            ]
        }
    ]
    
    test_formats = ["sharegpt", "alpaca", "openai"]
    
    # 호환성 검증기 생성
    compatibility_checker = CompatibilityChecker()
    
    print("=== Compatibility Checker Test ===")
    
    # 포맷별 호환성 검증 테스트
    for i, (item, item_format) in enumerate(zip(test_items, test_formats)):
        print(f"\nItem {i + 1} ({item_format} format):")
        result = compatibility_checker.check_compatibility(item, item_format)
        print(f"  Compatible: {result.is_compatible}")
        print(f"  Compatibility Score: {result.compatibility_score:.2f}")
        print(f"  Issues: {result.issues}")
        print(f"  Warnings: {result.warnings}")
        print(f"  Recommendations: {result.recommendations}")
        print(f"  Detailed Checks: {result.detailed_checks}")
    
    # 배치 호환성 검증 테스트
    print(f"\n=== Batch Compatibility Check Test ===")
    batch_results = []
    for item_format in test_formats:
        format_items = [test_items[i] for i, fmt in enumerate(test_formats) if fmt == item_format]
        if format_items:
            format_results = compatibility_checker.batch_check_compatibility(format_items, item_format)
            batch_results.extend(format_results)
    
    summary = compatibility_checker.get_compatibility_summary(batch_results)
    
    print(f"Total Items: {summary['total']}")
    print(f"Compatible: {summary['compatible']}")
    print(f"Incompatible: {summary['incompatible']}")
    print(f"Compatibility Rate: {summary['compatibility_rate']:.2%}")
    print(f"Average Score: {summary['average_score']:.2f}")
    print(f"Excellent: {summary['compatibility_grades']['excellent']}")
    print(f"Good: {summary['compatibility_grades']['good']}")
    print(f"Fair: {summary['compatibility_grades']['fair']}")
    print(f"Poor: {summary['compatibility_grades']['poor']}")
    print(f"Issues: {summary['issues_count']}")
    print(f"Warnings: {summary['warnings_count']}")
    print(f"Recommendations: {summary['recommendations_count']}")