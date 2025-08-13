#!/usr/bin/env python3
"""
Unsloth 호환성 검증기 모듈
Unsloth 프레임워크와의 호환성을 검증하는 검증기 모듈입니다.
"""

import json
import logging
from typing import List, Dict, Any, Optional, Union, Tuple
from dataclasses import dataclass, asdict, field
from datetime import datetime
import re

logger = logging.getLogger(__name__)


@dataclass
class ValidationResult:
    """검증 결과"""
    is_valid: bool = True
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    format_specific: Dict[str, Any] = field(default_factory=dict)
    statistics: Dict[str, Any] = field(default_factory=dict)
    
    def add_issue(self, issue: str):
        """이슈를 추가합니다."""
        self.issues.append(issue)
        self.is_valid = False
    
    def add_warning(self, warning: str):
        """경고를 추가합니다."""
        self.warnings.append(warning)
    
    def add_recommendation(self, recommendation: str):
        """권장사항을 추가합니다."""
        self.recommendations.append(recommendation)
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환합니다."""
        return asdict(self)


class UnslothValidator:
    """Unsloth 호환성 검증기"""
    
    def __init__(self):
        """검증기를 초기화합니다."""
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 지원하는 포맷별 검증 규칙
        self.format_rules = {
            "sharegpt": {
                "required_fields": ["conversations"],
                "conversation_structure": {
                    "valid_roles": ["system", "human", "gpt"],
                    "min_turns": 1,
                    "max_turns": 20
                },
                "token_limits": {
                    "min_total_tokens": 50,
                    "max_total_tokens": 8192,
                    "max_conversation_length": 8192
                }
            },
            "alpaca": {
                "required_fields": ["instruction", "output"],
                "optional_fields": ["input"],
                "token_limits": {
                    "min_instruction_tokens": 10,
                    "max_instruction_tokens": 512,
                    "max_input_tokens": 1024,
                    "max_output_tokens": 8192,
                    "max_total_tokens": 8192
                }
            },
            "openai": {
                "required_fields": ["messages"],
                "message_structure": {
                    "valid_roles": ["system", "user", "assistant"],
                    "min_messages": 2,
                    "max_messages": 50
                },
                "token_limits": {
                    "min_total_tokens": 50,
                    "max_total_tokens": 8192,
                    "max_message_length": 8192
                }
            }
        }
    
    def validate_dataset_format(
        self, 
        format_type: str, 
        data: List[Dict[str, Any]]
    ) -> ValidationResult:
        """
        데이터셋 포맷 유효성을 검증합니다.
        
        Args:
            format_type: 포맷 타입
            data: 검증할 데이터 목록
            
        Returns:
            검증 결과
        """
        result = ValidationResult()
        
        if not data:
            result.add_issue("데이터가 비어있습니다")
            return result
        
        format_type = format_type.lower()
        if format_type not in self.format_rules:
            result.add_issue(f"지원하지 않는 포맷 타입: {format_type}")
            return result
        
        rules = self.format_rules[format_type]
        
        # 기본 구조 검증
        self._validate_basic_structure(result, format_type, data, rules)
        
        # 데이터 개별 검증
        for i, item in enumerate(data):
            try:
                if format_type == "sharegpt":
                    self._validate_sharegpt_item(result, item, i)
                elif format_type == "alpaca":
                    self._validate_alpaca_item(result, item, i)
                elif format_type == "openai":
                    self._validate_openai_item(result, item, i)
            except Exception as e:
                result.add_issue(f"Item {i} 검증 중 오류: {str(e)}")
        
        # 통계 생성
        result.statistics = self._generate_validation_statistics(data, format_type)
        
        return result
    
    def validate_token_ranges(
        self, 
        data: List[Dict[str, Any]], 
        min_tokens: int, 
        max_tokens: int
    ) -> ValidationResult:
        """
        토큰 범위 유효성을 검증합니다.
        
        Args:
            data: 검증할 데이터 목록
            min_tokens: 최소 토큰 수
            max_tokens: 최대 토큰 수
            
        Returns:
            검증 결과
        """
        result = ValidationResult()
        
        for i, item in enumerate(data):
            try:
                token_count = self._calculate_token_count(item)
                
                if token_count < min_tokens:
                    result.add_issue(f"Item {i}: 토큰 수 부족 ({token_count} < {min_tokens})")
                elif token_count > max_tokens:
                    result.add_issue(f"Item {i}: 토큰 수 초과 ({token_count} > {max_tokens})")
                    
            except Exception as e:
                result.add_issue(f"Item {i} 토큰 계산 중 오류: {str(e)}")
        
        return result
    
    def validate_unsloth_compatibility(
        self, 
        datasets: Dict[str, List[Dict[str, Any]]]
    ) -> Dict[str, ValidationResult]:
        """
        전체 데이터셋의 Unsloth 호환성을 검증합니다.
        
        Args:
            datasets: 포맷별 데이터셋
            
        Returns:
            포맷별 검증 결과
        """
        results = {}
        
        for format_type, data in datasets.items():
            self.logger.info(f"Validating {format_type} format compatibility")
            
            # 포맷 유효성 검증
            format_result = self.validate_dataset_format(format_type, data)
            
            # 토큰 범위 검증 (기본값 사용)
            token_result = self.validate_token_ranges(data, 50, 4096)
            
            # 결과 병합
            combined_result = self._merge_validation_results(format_result, token_result)
            
            # Unsloth 특화 검증
            unsloth_result = self._validate_unsloth_specific(format_type, data)
            combined_result = self._merge_validation_results(combined_result, unsloth_result)
            
            results[format_type] = combined_result
        
        return results
    
    def _validate_basic_structure(
        self, 
        result: ValidationResult, 
        format_type: str, 
        data: List[Dict[str, Any]], 
        rules: Dict[str, Any]
    ):
        """기본 구조를 검증합니다."""
        # 필수 필드 확인
        required_fields = rules.get("required_fields", [])
        for field in required_fields:
            if not all(field in item for item in data):
                result.add_issue(f"필수 필드 누락: {field}")
        
        # 데이터 타입 검증
        for item in data:
            if not isinstance(item, dict):
                result.add_issue(f"데이터 타입 오류: dict이어야 함")
                break
    
    def _validate_sharegpt_item(self, result: ValidationResult, item: Dict[str, Any], index: int):
        """ShareGPT 아이템을 검증합니다."""
        if "conversations" not in item:
            result.add_issue(f"Item {index}: conversations 필드 누락")
            return
        
        conversations = item["conversations"]
        if not isinstance(conversations, list):
            result.add_issue(f"Item {index}: conversations는 리스트여야 함")
            return
        
        rules = self.format_rules["sharegpt"]["conversation_structure"]
        valid_roles = rules["valid_roles"]
        
        # 대화 구조 검증
        for i, conv in enumerate(conversations):
            if not isinstance(conv, dict):
                result.add_issue(f"Item {index} Conversation {i}: dict이어야 함")
                continue
            
            if "from" not in conv or "value" not in conv:
                result.add_issue(f"Item {index} Conversation {i}: from 또는 value 필드 누락")
                continue
            
            if conv["from"] not in valid_roles:
                result.add_issue(f"Item {index} Conversation {i}: 유효하지 않은 역할 - {conv['from']}")
            
            if not isinstance(conv["value"], str) or not conv["value"].strip():
                result.add_issue(f"Item {index} Conversation {i}: 비어있는 값")
        
        # 턴 수 검증
        turn_count = len(conversations)
        if turn_count < rules["min_turns"]:
            result.add_issue(f"Item {index}: 턴 수 부족 ({turn_count} < {rules['min_turns']})")
        elif turn_count > rules["max_turns"]:
            result.add_warning(f"Item {index}: 턴 수 많음 ({turn_count} > {rules['max_turns']})")
    
    def _validate_alpaca_item(self, result: ValidationResult, item: Dict[str, Any], index: int):
        """Alpaca 아이템을 검증합니다."""
        # 필수 필드 검증
        required_fields = ["instruction", "output"]
        for field in required_fields:
            if field not in item:
                result.add_issue(f"Item {index}: 필수 필드 누락 - {field}")
            elif not isinstance(item[field], str) or not item[field].strip():
                result.add_issue(f"Item {index}: {field} 필드가 비어있음")
        
        # 선택 필드 검증
        if "input" in item and item["input"]:
            if not isinstance(item["input"], str):
                result.add_issue(f"Item {index}: input 필드는 문자열이어야 함")
        
        # 길이 검증
        rules = self.format_rules["alpaca"]["token_limits"]
        instruction_len = len(item.get("instruction", ""))
        output_len = len(item.get("output", ""))
        input_len = len(item.get("input", ""))
        
        if instruction_len > rules["max_instruction_tokens"] * 4:  # 문자열 길이로 추정
            result.add_warning(f"Item {index}: instruction 길이가 깜 ({instruction_len} chars)")
        
        if input_len > rules["max_input_tokens"] * 4:
            result.add_warning(f"Item {index}: input 길이가 깜 ({input_len} chars)")
        
        if output_len > rules["max_output_tokens"] * 4:
            result.add_warning(f"Item {index}: output 길이가 깜 ({output_len} chars)")
    
    def _validate_openai_item(self, result: ValidationResult, item: Dict[str, Any], index: int):
        """OpenAI 아이템을 검증합니다."""
        if "messages" not in item:
            result.add_issue(f"Item {index}: messages 필드 누락")
            return
        
        messages = item["messages"]
        if not isinstance(messages, list):
            result.add_issue(f"Item {index}: messages는 리스트여야 함")
            return
        
        rules = self.format_rules["openai"]["message_structure"]
        valid_roles = rules["valid_roles"]
        
        # 메시지 구조 검증
        for i, msg in enumerate(messages):
            if not isinstance(msg, dict):
                result.add_issue(f"Item {index} Message {i}: dict이어야 함")
                continue
            
            if "role" not in msg or "content" not in msg:
                result.add_issue(f"Item {index} Message {i}: role 또는 content 필드 누락")
                continue
            
            if msg["role"] not in valid_roles:
                result.add_issue(f"Item {index} Message {i}: 유효하지 않은 역할 - {msg['role']}")
            
            if not isinstance(msg["content"], str) or not msg["content"].strip():
                result.add_issue(f"Item {index} Message {i}: 비어있는 content")
        
        # 메시지 수 검증
        message_count = len(messages)
        if message_count < rules["min_messages"]:
            result.add_issue(f"Item {index}: 메시지 수 부족 ({message_count} < {rules['min_messages']})")
        elif message_count > rules["max_messages"]:
            result.add_warning(f"Item {index}: 메시지 수 많음 ({message_count} > {rules['max_messages']})")
        
        # 메시지 순서 검증
        self._validate_message_order(result, item, index)
    
    def _validate_message_order(self, result: ValidationResult, item: Dict[str, Any], index: int):
        """메시지 순서를 검증합니다."""
        messages = item["messages"]
        if not messages:
            return
        
        # 첫 번째 메시지가 system인지 확인
        if messages[0]["role"] == "system":
            remaining = messages[1:]
        else:
            remaining = messages
        
        # user/assistant 순서 검증
        expected_role = "user"
        for msg in remaining:
            if msg["role"] != expected_role:
                result.add_issue(f"Item {index}: 메시지 순서 오류 - 기대: {expected_role}, 실제: {msg['role']}")
                break
            expected_role = "assistant" if expected_role == "user" else "user"
    
    def _validate_unsloth_specific(self, format_type: str, data: List[Dict[str, Any]]) -> ValidationResult:
        """Unsloth 특화 검증을 수행합니다."""
        result = ValidationResult()
        
        # EOS 토큰 검증
        eos_token = "</s>"
        for i, item in enumerate(data):
            try:
                if format_type == "sharegpt":
                    for conv in item.get("conversations", []):
                        if conv["from"] in ["human", "gpt"]:
                            if not conv["value"].endswith(eos_token):
                                result.add_warning(f"Item {i}: EOS 토큰 누락 - {conv['from']}")
                
                elif format_type == "alpaca":
                    for field in ["instruction", "output", "input"]:
                        if field in item and item[field]:
                            if not item[field].endswith(eos_token):
                                result.add_warning(f"Item {i}: EOS 토큰 누락 - {field}")
                
                elif format_type == "openai":
                    for msg in item.get("messages", []):
                        if msg["role"] in ["user", "assistant"]:
                            if not msg["content"].endswith(eos_token):
                                result.add_warning(f"Item {i}: EOS 토큰 누락 - {msg['role']}")
            
            except Exception as e:
                result.add_issue(f"Item {i} EOS 토큰 검증 중 오류: {str(e)}")
        
        # 품질 검증
        quality_issues = 0
        for i, item in enumerate(data):
            # 너무 짧은 내용 검증
            if self._is_content_too_short(item, format_type):
                result.add_warning(f"Item {i}: 내용이 너무 짧음")
                quality_issues += 1
            
            # 반복 패턴 검증
            if self._has_repetitive_content(item, format_type):
                result.add_warning(f"Item {i}: 반복적인 내용 감지")
                quality_issues += 1
        
        # 품질 이슈가 많은 경우 권장사항 추가
        if quality_issues > len(data) * 0.1:  # 10% 이상
            result.add_recommendation("품질 개선을 위해 데이터 필터링을 강화하세요")
        
        return result
    
    def _is_content_too_short(self, item: Dict[str, Any], format_type: str) -> bool:
        """내용이 너무 짧은지 확인합니다."""
        min_length = 20
        
        if format_type == "sharegpt":
            for conv in item.get("conversations", []):
                if len(conv.get("value", "")) < min_length:
                    return True
        
        elif format_type == "alpaca":
            for field in ["instruction", "output", "input"]:
                if field in item and len(item.get(field, "")) < min_length:
                    return True
        
        elif format_type == "openai":
            for msg in item.get("messages", []):
                if len(msg.get("content", "")) < min_length:
                    return True
        
        return False
    
    def _has_repetitive_content(self, item: Dict[str, Any], format_type: str) -> bool:
        """반복적인 내용이 있는지 확인합니다."""
        # 간단한 반복 패턴 검증
        text_parts = []
        
        if format_type == "sharegpt":
            text_parts = [conv.get("value", "") for conv in item.get("conversations", [])]
        elif format_type == "alpaca":
            text_parts = [item.get(field, "") for field in ["instruction", "output", "input"] if field in item]
        elif format_type == "openai":
            text_parts = [msg.get("content", "") for msg in item.get("messages", [])]
        
        # 반복 단어 검증
        for text in text_parts:
            words = text.lower().split()
            if len(words) > 10:  # 10단어 이상인 경우만 검증
                unique_words = set(words)
                if len(unique_words) / len(words) < 0.3:  # 30% 미만의 고유 단어
                    return True
        
        return False
    
    def _calculate_token_count(self, item: Dict[str, Any]) -> int:
        """아이템의 토큰 수를 계산합니다."""
        # 간단한 문자 기반 토큰 계산
        total_chars = 0
        
        if "conversations" in item:
            for conv in item["conversations"]:
                total_chars += len(conv.get("value", ""))
        
        elif "instruction" in item:
            total_chars += len(item.get("instruction", ""))
            total_chars += len(item.get("output", ""))
            total_chars += len(item.get("input", ""))
        
        elif "messages" in item:
            for msg in item["messages"]:
                total_chars += len(msg.get("content", ""))
        
        # 평균 토큰 길이를 4로 가정
        return total_chars // 4
    
    def _generate_validation_statistics(self, data: List[Dict[str, Any]], format_type: str) -> Dict[str, Any]:
        """검증 통계를 생성합니다."""
        stats = {
            "total_items": len(data),
            "format_type": format_type,
            "validation_time": datetime.now().isoformat()
        }
        
        # 포맷별 통계
        if format_type == "sharegpt":
            total_turns = sum(len(item.get("conversations", [])) for item in data)
            stats["average_turns_per_conversation"] = total_turns / len(data) if data else 0
        
        elif format_type == "alpaca":
            instruction_lengths = [len(item.get("instruction", "")) for item in data]
            output_lengths = [len(item.get("output", "")) for item in data]
            
            stats["average_instruction_length"] = sum(instruction_lengths) / len(data) if data else 0
            stats["average_output_length"] = sum(output_lengths) / len(data) if data else 0
        
        elif format_type == "openai":
            total_messages = sum(len(item.get("messages", [])) for item in data)
            stats["average_messages_per_item"] = total_messages / len(data) if data else 0
        
        return stats
    
    def _merge_validation_results(self, *results: ValidationResult) -> ValidationResult:
        """여러 검증 결과를 병합합니다."""
        merged = ValidationResult()
        
        for result in results:
            merged.issues.extend(result.issues)
            merged.warnings.extend(result.warnings)
            merged.recommendations.extend(result.recommendations)
            merged.format_specific.update(result.format_specific)
            merged.statistics.update(result.statistics)
            
            if not result.is_valid:
                merged.is_valid = False
        
        return merged
    
    def get_validation_summary(self, validation_results: Dict[str, ValidationResult]) -> Dict[str, Any]:
        """검증 요약을 생성합니다."""
        summary = {
            "total_formats": len(validation_results),
            "valid_formats": 0,
            "invalid_formats": 0,
            "total_issues": 0,
            "total_warnings": 0,
            "total_recommendations": 0,
            "format_details": {}
        }
        
        for format_type, result in validation_results.items():
            detail = {
                "is_valid": result.is_valid,
                "issues_count": len(result.issues),
                "warnings_count": len(result.warnings),
                "recommendations_count": len(result.recommendations),
                "issues": result.issues,
                "warnings": result.warnings,
                "recommendations": result.recommendations
            }
            
            summary["format_details"][format_type] = detail
            summary["total_issues"] += len(result.issues)
            summary["total_warnings"] += len(result.warnings)
            summary["total_recommendations"] += len(result.recommendations)
            
            if result.is_valid:
                summary["valid_formats"] += 1
            else:
                summary["invalid_formats"] += 1
        
        return summary


if __name__ == "__main__":
    # 테스트 데이터
    test_data = {
        "sharegpt": [
            {
                "conversations": [
                    {"from": "system", "value": "테스트 시스템"},
                    {"from": "human", "value": "테스트 질문"},
                    {"from": "gpt", "value": "테스트 응답"}
                ]
            }
        ],
        "alpaca": [
            {
                "instruction": "테스트 지시문",
                "output": "테스트 응답",
                "input": "테스트 입력"
            }
        ],
        "openai": [
            {
                "messages": [
                    {"role": "system", "content": "테스트 시스템"},
                    {"role": "user", "content": "테스트 질문"},
                    {"role": "assistant", "content": "테스트 응답"}
                ]
            }
        ]
    }
    
    # 검증기 생성
    validator = UnslothValidator()
    
    print("=== Unsloth Validator Test ===")
    
    # 포맷별 검증
    for format_type, data in test_data.items():
        print(f"\n{format_type.upper()} Format Validation:")
        result = validator.validate_dataset_format(format_type, data)
        print(f"  Valid: {result.is_valid}")
        print(f"  Issues: {len(result.issues)}")
        print(f"  Warnings: {len(result.warnings)}")
        print(f"  Recommendations: {len(result.recommendations)}")
        
        if result.issues:
            print(f"  Issue examples: {result.issues[:2]}")
    
    # 전체 호환성 검증
    print(f"\n=== Overall Compatibility Validation ===")
    results = validator.validate_unsloth_compatibility(test_data)
    summary = validator.get_validation_summary(results)
    
    print(f"Total formats: {summary['total_formats']}")
    print(f"Valid formats: {summary['valid_formats']}")
    print(f"Invalid formats: {summary['invalid_formats']}")
    print(f"Total issues: {summary['total_issues']}")
    print(f"Total warnings: {summary['total_warnings']}")