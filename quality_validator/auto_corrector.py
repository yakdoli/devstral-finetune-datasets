#!/usr/bin/env python3
"""
자동 수정 모듈
품질 문제를 자동으로 해결하는 기능을 제공합니다.
"""

import re
import json
import logging
from typing import List, Dict, Any, Optional, Set, Tuple, Union
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter

logger = logging.getLogger(__name__)


@dataclass
class AutoCorrectorConfig:
    """자동 수정기 설정"""
    # 텍스트 수정 설정
    text_correction_enabled: bool = True
    fix_grammar: bool = True
    fix_spelling: bool = True
    fix_formatting: bool = True
    fix_whitespace: bool = True
    
    # 구조 수정 설정
    structural_correction_enabled: bool = True
    fix_conversation_structure: bool = True
    fix_missing_fields: bool = True
    fix_sequence_order: bool = True
    
    # 토큰 관련 수정 설정
    token_correction_enabled: bool = True
    fix_token_length: bool = True
    max_token_length: int = 4096
    min_token_length: int = 50
    truncate_method: str = "smart"  # smart, simple, none
    
    # EOS 토큰 수정 설정
    eos_correction_enabled: bool = True
    add_missing_eos: bool = True
    remove_duplicate_eos: bool = True
    preferred_eos_token: str = "</s>"
    
    # 메타데이터 수정 설정
    metadata_correction_enabled: bool = True
    add_missing_metadata: bool = True
    standardize_metadata: bool = True
    
    # 수정 강도 설정
    correction_strength: float = 0.8  # 0.0-1.0
    preserve_original_content: bool = True
    create_backup: bool = True
    
    # 성능 최적화 설정
    batch_size: int = 100
    max_workers: int = 4
    use_cache: bool = True


@dataclass
class CorrectionResult:
    """수정 결과"""
    original_item: Dict[str, Any] = field(default_factory=dict)
    corrected_item: Dict[str, Any] = field(default_factory=dict)
    corrections_applied: List[str] = field(default_factory=list)
    issues_fixed: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    correction_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    confidence_score: float = 0.0
    changes_made: bool = False


class AutoCorrector:
    """자동 수정기 클래스"""
    
    def __init__(self, config: Optional[AutoCorrectorConfig] = None):
        """
        자동 수정기를 초기화합니다.
        
        Args:
            config: 자동 수정기 설정
        """
        self.config = config or AutoCorrectorConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 텍스트 수정 패턴
        self._setup_correction_patterns()
        
        # 구조 수정 규칙
        self._setup_structure_rules()
        
        # 토큰 관련 설정
        self._setup_token_settings()
    
    def _setup_correction_patterns(self):
        """수정 패턴을 설정합니다."""
        # 문법 수정 패턴
        self.grammar_patterns = {
            'double_punctuation': re.compile(r'([.!?]){2,}'),
            'extra_whitespace': re.compile(r'\s{2,}'),
            'missing_space': re.compile(r'([,.!?])([a-zA-Z])'),
            'extra_space': re.compile(r'\s+([,.!?])'),
            'capitalization': re.compile(r'\b[a-z](?=\s+[a-z]+\b)'),
            'sentence_end': re.compile(r'[^.!?]\s*$')
        }
        
        # 맞춤법 수정 패턴
        self.spelling_corrections = {
            'teh': 'the',
            'adn': 'and',
            'thier': 'their',
            'recieve': 'receive',
            'seperate': 'separate',
            'definately': 'definitely',
            'occured': 'occurred',
            'untill': 'until',
            'alot': 'a lot',
            'becuase': 'because',
            'wich': 'which',
            'couldnt': "couldn't",
            'wouldnt': "wouldn't",
            'shouldnt': "shouldn't",
            'dont': "don't",
            'doesnt': "doesn't",
            'isnt': "isn't",
            'arent': "aren't",
            'wasnt': "wasn't",
            'werent': "weren't"
        }
        
        # 형식 수정 패턴
        self.formatting_patterns = {
            'code_blocks': re.compile(r'```([^`]+)```'),
            'inline_code': re.compile(r'`([^`]+)`'),
            'markdown_links': re.compile(r'\[([^\]]+)\]\(([^)]+)\)'),
            'html_tags': re.compile(r'<[^>]+>')
        }
    
    def _setup_structure_rules(self):
        """구조 수정 규칙을 설정합니다."""
        # ShareGPT 구조 규칙
        self.sharegpt_rules = {
            'required_fields': ['conversations'],
            'required_roles': ['system', 'human', 'gpt'],
            'min_turns': 2,
            'max_turns': 20,
            'sequence_order': ['system', 'human', 'gpt']
        }
        
        # Alpaca 구조 규칙
        self.alpaca_rules = {
            'required_fields': ['instruction', 'input', 'output'],
            'min_instruction_length': 10,
            'max_instruction_length': 1000,
            'min_output_length': 10,
            'max_output_length': 2000
        }
        
        # OpenAI 구조 규칙
        self.openai_rules = {
            'required_fields': ['messages'],
            'required_roles': ['system', 'user', 'assistant'],
            'min_turns': 2,
            'max_turns': 20,
            'sequence_order': ['system', 'user', 'assistant']
        }
    
    def _setup_token_settings(self):
        """토큰 관련 설정을 초기화합니다."""
        # 토큰 추정 설정
        self.token_settings = {
            'words_per_token': 0.75,  # 평균 단어당 토큰 수
            'chars_per_token': 4.0,   # 평균 문자당 토큰 수
            'max_tokens_for_truncation': 100
        }
    
    def correct_item(self, item: Dict[str, Any], item_format: str, issues: List[str] = None) -> CorrectionResult:
        """
        아이템을 자동으로 수정합니다.
        
        Args:
            item: 수정할 아이템
            item_format: 아이템 포맷
            issues: 수정할 이슈 목록
            
        Returns:
            수정 결과
        """
        result = CorrectionResult()
        result.original_item = item.copy()
        result.corrected_item = item.copy()
        result.corrections_applied = []
        result.issues_fixed = []
        
        if not item:
            result.warnings.append("빈 아이템")
            return result
        
        # 제공된 이슈가 없으면 자동으로 감지
        if issues is None:
            issues = self._detect_issues(item, item_format)
        
        # 텍스트 수정
        if self.config.text_correction_enabled:
            text_result = self._correct_text(result.corrected_item, item_format, issues)
            result.corrections_applied.extend(text_result['corrections'])
            result.issues_fixed.extend(text_result['issues_fixed'])
        
        # 구조 수정
        if self.config.structural_correction_enabled:
            structure_result = self._correct_structure(result.corrected_item, item_format, issues)
            result.corrections_applied.extend(structure_result['corrections'])
            result.issues_fixed.extend(structure_result['issues_fixed'])
        
        # 토큰 관련 수정
        if self.config.token_correction_enabled:
            token_result = self._correct_tokens(result.corrected_item, item_format, issues)
            result.corrections_applied.extend(token_result['corrections'])
            result.issues_fixed.extend(token_result['issues_fixed'])
        
        # EOS 토큰 수정
        if self.config.eos_correction_enabled:
            eos_result = self._correct_eos_tokens(result.corrected_item, item_format, issues)
            result.corrections_applied.extend(eos_result['corrections'])
            result.issues_fixed.extend(eos_result['issues_fixed'])
        
        # 메타데이터 수정
        if self.config.metadata_correction_enabled:
            metadata_result = self._correct_metadata(result.corrected_item, item_format, issues)
            result.corrections_applied.extend(metadata_result['corrections'])
            result.issues_fixed.extend(metadata_result['issues_fixed'])
        
        # 변경 여부 확인
        result.changes_made = result.corrected_item != result.original_item
        
        # 신뢰도 점수 계산
        result.confidence_score = self._calculate_confidence_score(result)
        
        return result
    
    def _detect_issues(self, item: Dict[str, Any], item_format: str) -> List[str]:
        """아이템의 이슈를 감지합니다."""
        issues = []
        
        # 텍스트 관련 이슈 감지
        text = self._extract_text_for_correction(item, item_format)
        
        # 문법 이슈
        if self.config.fix_grammar:
            if self.grammar_patterns['double_punctuation'].search(text):
                issues.append("duplicate_punctuation")
            if self.grammar_patterns['extra_whitespace'].search(text):
                issues.append("extra_whitespace")
            if self.grammar_patterns['missing_space'].search(text):
                issues.append("missing_space")
            if self.grammar_patterns['extra_space'].search(text):
                issues.append("extra_space")
            if not self.grammar_patterns['sentence_end'].search(text):
                issues.append("missing_sentence_end")
        
        # 맞춤법 이슈
        if self.config.fix_spelling:
            for misspelling, correction in self.spelling_corrections.items():
                if misspelling in text.lower():
                    issues.append(f"spelling_error_{misspelling}")
        
        # 구조 이슈
        if item_format == "sharegpt":
            if "conversations" not in item:
                issues.append("missing_conversations")
            else:
                conversations = item["conversations"]
                if len(conversations) < self.sharegpt_rules['min_turns']:
                    issues.append("too_few_turns")
                if len(conversations) > self.sharegpt_rules['max_turns']:
                    issues.append("too_many_turns")
                
                # 역할 검사
                roles = [conv.get("from", "") for conv in conversations]
                for required_role in self.sharegpt_rules['required_roles']:
                    if required_role not in roles:
                        issues.append(f"missing_role_{required_role}")
        
        elif item_format == "alpaca":
            for field in self.alpaca_rules['required_fields']:
                if field not in item:
                    issues.append(f"missing_field_{field}")
            
            if "instruction" in item:
                instruction = str(item["instruction"])
                if len(instruction) < self.alpaca_rules['min_instruction_length']:
                    issues.append("instruction_too_short")
                if len(instruction) > self.alpaca_rules['max_instruction_length']:
                    issues.append("instruction_too_long")
            
            if "output" in item:
                output = str(item["output"])
                if len(output) < self.alpaca_rules['min_output_length']:
                    issues.append("output_too_short")
                if len(output) > self.alpaca_rules['max_output_length']:
                    issues.append("output_too_long")
        
        elif item_format == "openai":
            if "messages" not in item:
                issues.append("missing_messages")
            else:
                messages = item["messages"]
                if len(messages) < self.openai_rules['min_turns']:
                    issues.append("too_few_turns")
                if len(messages) > self.openai_rules['max_turns']:
                    issues.append("too_many_turns")
                
                # 역할 검사
                roles = [msg.get("role", "") for msg in messages]
                for required_role in self.openai_rules['required_roles']:
                    if required_role not in roles:
                        issues.append(f"missing_role_{required_role}")
        
        # 토큰 이슈
        if self.config.token_correction_enabled:
            token_count = self._estimate_token_count(text)
            if token_count > self.config.max_token_length:
                issues.append("tokens_too_long")
            elif token_count < self.config.min_token_length:
                issues.append("tokens_too_short")
        
        # EOS 토큰 이슈
        if self.config.eos_correction_enabled:
            if not any(eos_token in text for eos_token in [self.config.preferred_eos_token, "</s>", "<|im_end|>"]):
                issues.append("missing_eos_token")
        
        return issues
    
    def _correct_text(self, item: Dict[str, Any], item_format: str, issues: List[str]) -> Dict[str, Any]:
        """텍스트를 수정합니다."""
        corrections = []
        issues_fixed = []
        
        # 텍스트 추출
        text_parts = self._extract_text_parts_for_correction(item, item_format)
        corrected_parts = []
        
        for part in text_parts:
            corrected_part = part
            
            # 문법 수정
            if self.config.fix_grammar:
                # 연속된 구두문 수정
                corrected_part = self.grammar_patterns['double_punctuation'].sub(r'\1', corrected_part)
                if corrected_part != part:
                    corrections.append("fixed_duplicate_punctuation")
                    issues_fixed.append("duplicate_punctuation")
                
                # 불필요한 공백 수정
                corrected_part = self.grammar_patterns['extra_whitespace'].sub(' ', corrected_part)
                if corrected_part != part:
                    corrections.append("fixed_extra_whitespace")
                    issues_fixed.append("extra_whitespace")
                
                # 공백 부족 수정
                corrected_part = self.grammar_patterns['missing_space'].sub(r'\1 \2', corrected_part)
                if corrected_part != part:
                    corrections.append("fixed_missing_space")
                    issues_fixed.append("missing_space")
                
                # 불필요한 공백 수정
                corrected_part = self.grammar_patterns['extra_space'].sub(r'\1', corrected_part)
                if corrected_part != part:
                    corrections.append("fixed_extra_space")
                    issues_fixed.append("extra_space")
                
                # 문장 끝 수정
                if not corrected_part.strip().endswith(('.', '!', '?')):
                    corrected_part = corrected_part.strip() + '.'
                    corrections.append("fixed_missing_sentence_end")
                    issues_fixed.append("missing_sentence_end")
            
            # 맞춤법 수정
            if self.config.fix_spelling:
                for misspelling, correction in self.spelling_corrections.items():
                    if misspelling in corrected_part.lower():
                        pattern = re.compile(r'\b' + re.escape(misspelling) + r'\b', re.IGNORECASE)
                        corrected_part = pattern.sub(correction, corrected_part)
                        corrections.append(f"fixed_spelling_{misspelling}")
                        issues_fixed.append(f"spelling_error_{misspelling}")
            
            # 형식 수정
            if self.config.fix_formatting:
                # 코드 블록 형식화
                code_blocks = self.formatting_patterns['code_blocks'].findall(corrected_part)
                for code in code_blocks:
                    formatted_code = code.strip()
                    corrected_part = corrected_part.replace(f'```{code}```', f'```\n{formatted_code}\n```')
                
                # 인라인 코드 형식화
                inline_codes = self.formatting_patterns['inline_code'].findall(corrected_part)
                for code in inline_codes:
                    formatted_code = code.strip()
                    corrected_part = corrected_part.replace(f'`{code}`', f'`{formatted_code}`')
            
            corrected_parts.append(corrected_part)
        
        # 수정된 텍스트 다시 아이템에 적용
        self._apply_corrected_text(item, item_format, corrected_parts)
        
        return {"corrections": corrections, "issues_fixed": issues_fixed}
    
    def _correct_structure(self, item: Dict[str, Any], item_format: str, issues: List[str]) -> Dict[str, Any]:
        """구조를 수정합니다."""
        corrections = []
        issues_fixed = []
        
        if item_format == "sharegpt":
            # 필수 필드 추가
            if "conversations" not in item:
                item["conversations"] = []
                corrections.append("added_conversations_field")
                issues_fixed.append("missing_conversations")
            
            conversations = item["conversations"]
            
            # 대화 턴 수 조절
            if len(conversations) < self.sharegpt_rules['min_turns']:
                # 부족한 턴 추가
                while len(conversations) < self.sharegpt_rules['min_turns']:
                    conversations.append({
                        "from": "gpt",
                        "value": "추가 정보를 제공합니다."
                    })
                corrections.append("added_missing_turns")
                issues_fixed.append("too_few_turns")
            
            elif len(conversations) > self.sharegpt_rules['max_turns']:
                # 너무 많은 턴 제거
                conversations = conversations[:self.sharegpt_rules['max_turns']]
                item["conversations"] = conversations
                corrections.append("truncated_excess_turns")
                issues_fixed.append("too_many_turns")
            
            # 역할 순서 수정
            if "sequence_order" in issues:
                corrected_conversations = self._fix_conversation_sequence(conversations)
                if corrected_conversations != conversations:
                    item["conversations"] = corrected_conversations
                    corrections.append("fixed_conversation_sequence")
                    issues_fixed.append("sequence_order")
            
            # 필수 역할 추가
            for required_role in self.sharegpt_rules['required_roles']:
                if f"missing_role_{required_role}" in issues:
                    # 해당 역할이 없으면 추가
                    role_found = False
                    for conv in conversations:
                        if conv.get("from") == required_role:
                            role_found = True
                            break
                    
                    if not role_found:
                        # 적절한 위치에 역할 추가
                        if required_role == "system" and not any(conv.get("from") == "system" for conv in conversations):
                            conversations.insert(0, {"from": "system", "value": "전문가입니다."})
                        elif required_role == "human" and not any(conv.get("from") == "human" for conv in conversations):
                            conversations.append({"from": "human", "value": "질문입니다."})
                        elif required_role == "gpt" and not any(conv.get("from") == "gpt" for conv in conversations):
                            conversations.append({"from": "gpt", "value": "답변입니다."})
                        
                        corrections.append(f"added_missing_role_{required_role}")
                        issues_fixed.append(f"missing_role_{required_role}")
        
        elif item_format == "alpaca":
            # 필수 필드 추가
            for field in self.alpaca_rules['required_fields']:
                if field not in item:
                    item[field] = ""
                    corrections.append(f"added_missing_field_{field}")
                    issues_fixed.append(f"missing_field_{field}")
            
            # 필드 길이 조절
            if "instruction_too_short" in issues:
                instruction = item.get("instruction", "")
                if len(instruction) < self.alpaca_rules['min_instruction_length']:
                    item["instruction"] = instruction + " " * (self.alpaca_rules['min_instruction_length'] - len(instruction))
                    corrections.append("extended_instruction")
                    issues_fixed.append("instruction_too_short")
            
            if "instruction_too_long" in issues:
                instruction = item.get("instruction", "")
                if len(instruction) > self.alpaca_rules['max_instruction_length']:
                    item["instruction"] = instruction[:self.alpaca_rules['max_instruction_length']]
                    corrections.append("truncated_instruction")
                    issues_fixed.append("instruction_too_long")
            
            if "output_too_short" in issues:
                output = item.get("output", "")
                if len(output) < self.alpaca_rules['min_output_length']:
                    item["output"] = output + " " * (self.alpaca_rules['min_output_length'] - len(output))
                    corrections.append("extended_output")
                    issues_fixed.append("output_too_short")
            
            if "output_too_long" in issues:
                output = item.get("output", "")
                if len(output) > self.alpaca_rules['max_output_length']:
                    item["output"] = output[:self.alpaca_rules['max_output_length']]
                    corrections.append("truncated_output")
                    issues_fixed.append("output_too_long")
        
        elif item_format == "openai":
            # 필수 필드 추가
            if "messages" not in item:
                item["messages"] = []
                corrections.append("added_messages_field")
                issues_fixed.append("missing_messages")
            
            messages = item["messages"]
            
            # 메시지 턴 수 조절
            if len(messages) < self.openai_rules['min_turns']:
                # 부족한 턴 추가
                while len(messages) < self.openai_rules['min_turns']:
                    messages.append({
                        "role": "assistant",
                        "content": "추가 정보를 제공합니다."
                    })
                corrections.append("added_missing_turns")
                issues_fixed.append("too_few_turns")
            
            elif len(messages) > self.openai_rules['max_turns']:
                # 너무 많은 턴 제거
                messages = messages[:self.openai_rules['max_turns']]
                item["messages"] = messages
                corrections.append("truncated_excess_turns")
                issues_fixed.append("too_many_turns")
            
            # 역할 순서 수정
            if "sequence_order" in issues:
                corrected_messages = self._fix_message_sequence(messages)
                if corrected_messages != messages:
                    item["messages"] = corrected_messages
                    corrections.append("fixed_message_sequence")
                    issues_fixed.append("sequence_order")
            
            # 필수 역할 추가
            for required_role in self.openai_rules['required_roles']:
                if f"missing_role_{required_role}" in issues:
                    # 해당 역할이 없으면 추가
                    role_found = False
                    for msg in messages:
                        if msg.get("role") == required_role:
                            role_found = True
                            break
                    
                    if not role_found:
                        # 적절한 위치에 역할 추가
                        if required_role == "system" and not any(msg.get("role") == "system" for msg in messages):
                            messages.insert(0, {"role": "system", "content": "전문가입니다."})
                        elif required_role == "user" and not any(msg.get("role") == "user" for msg in messages):
                            messages.append({"role": "user", "content": "질문입니다."})
                        elif required_role == "assistant" and not any(msg.get("role") == "assistant" for msg in messages):
                            messages.append({"role": "assistant", "content": "답변입니다."})
                        
                        corrections.append(f"added_missing_role_{required_role}")
                        issues_fixed.append(f"missing_role_{required_role}")
        
        return {"corrections": corrections, "issues_fixed": issues_fixed}
    
    def _correct_tokens(self, item: Dict[str, Any], item_format: str, issues: List[str]) -> Dict[str, Any]:
        """토큰을 수정합니다."""
        corrections = []
        issues_fixed = []
        
        if "tokens_too_long" in issues or "tokens_too_short" in issues:
            # 텍스트 추출
            text = self._extract_text_for_correction(item, item_format)
            token_count = self._estimate_token_count(text)
            
            if token_count > self.config.max_token_length and "tokens_too_long" in issues:
                # 토큰 수 줄이기
                if self.config.truncate_method == "smart":
                    truncated_text = self._smart_truncate(text, self.config.max_token_length)
                elif self.config.truncate_method == "simple":
                    truncated_text = self._simple_truncate(text, self.config.max_token_length)
                else:
                    truncated_text = text
                
                # 수정된 텍스트 다시 적용
                self._apply_corrected_text(item, item_format, [truncated_text])
                
                corrections.append("truncated_tokens")
                issues_fixed.append("tokens_too_long")
            
            elif token_count < self.config.min_token_length and "tokens_too_short" in issues:
                # 토큰 수 늘리기
                extended_text = text + " " * (self.config.min_token_length - int(token_count * self.token_settings['chars_per_token']))
                
                # 수정된 텍스트 다시 적용
                self._apply_corrected_text(item, item_format, [extended_text])
                
                corrections.append("extended_tokens")
                issues_fixed.append("tokens_too_short")
        
        return {"corrections": corrections, "issues_fixed": issues_fixed}
    
    def _correct_eos_tokens(self, item: Dict[str, Any], item_format: str, issues: List[str]) -> Dict[str, Any]:
        """EOS 토큰을 수정합니다."""
        corrections = []
        issues_fixed = []
        
        if "missing_eos_token" in issues:
            # 텍스트 추출
            text_parts = self._extract_text_parts_for_correction(item, item_format)
            
            # EOS 토큰 추가
            corrected_parts = []
            for part in text_parts:
                if not part.strip().endswith(('.', '!', '?', self.config.preferred_eos_token, '</s>', '<|im_end|>')):
                    part = part.strip() + self.config.preferred_eos_token
                corrected_parts.append(part)
            
            # 수정된 텍스트 다시 적용
            self._apply_corrected_text(item, item_format, corrected_parts)
            
            corrections.append("added_eos_token")
            issues_fixed.append("missing_eos_token")
        
        return {"corrections": corrections, "issues_fixed": issues_fixed}
    
    def _correct_metadata(self, item: Dict[str, Any], item_format: str, issues: List[str]) -> Dict[str, Any]:
        """메타데이터를 수정합니다."""
        corrections = []
        issues_fixed = []
        
        # 메타데이터 필드 추가
        if "metadata" not in item:
            item["metadata"] = {}
            corrections.append("added_metadata_field")
        
        metadata = item["metadata"]
        
        # 표준화된 메타데이터 추가
        if self.config.standardize_metadata:
            standard_metadata = {
                "format": item_format,
                "corrected_at": datetime.now().isoformat(),
                "correction_version": "1.0",
                "quality_score": self._estimate_quality_score(item)
            }
            
            for key, value in standard_metadata.items():
                if key not in metadata:
                    metadata[key] = value
                    corrections.append(f"added_metadata_{key}")
        
        return {"corrections": corrections, "issues_fixed": issues_fixed}
    
    def _extract_text_for_correction(self, item: Dict[str, Any], item_format: str) -> str:
        """수정을 위한 텍스트를 추출합니다."""
        if item_format == "sharegpt":
            text_parts = []
            for conv in item.get("conversations", []):
                text_parts.append(conv.get("value", ""))
            return " ".join(text_parts)
        
        elif item_format == "alpaca":
            text_parts = [
                item.get("instruction", ""),
                item.get("input", ""),
                item.get("output", "")
            ]
            return " ".join(text_parts)
        
        elif item_format == "openai":
            text_parts = []
            for msg in item.get("messages", []):
                text_parts.append(msg.get("content", ""))
            return " ".join(text_parts)
        
        else:
            return str(item)
    
    def _extract_text_parts_for_correction(self, item: Dict[str, Any], item_format: str) -> List[str]:
        """수정을 위한 텍스트 부분을 추출합니다."""
        if item_format == "sharegpt":
            return [conv.get("value", "") for conv in item.get("conversations", [])]
        
        elif item_format == "alpaca":
            return [
                item.get("instruction", ""),
                item.get("input", ""),
                item.get("output", "")
            ]
        
        elif item_format == "openai":
            return [msg.get("content", "") for msg in item.get("messages", [])]
        
        else:
            return [str(item)]
    
    def _apply_corrected_text(self, item: Dict[str, Any], item_format: str, text_parts: List[str]):
        """수정된 텍스트를 아이템에 적용합니다."""
        if item_format == "sharegpt":
            conversations = item.get("conversations", [])
            for i, text in enumerate(text_parts):
                if i < len(conversations):
                    conversations[i]["value"] = text
                else:
                    conversations.append({"from": "gpt", "value": text})
        
        elif item_format == "alpaca":
            if len(text_parts) > 0:
                item["instruction"] = text_parts[0]
            if len(text_parts) > 1:
                item["input"] = text_parts[1]
            if len(text_parts) > 2:
                item["output"] = text_parts[2]
        
        elif item_format == "openai":
            messages = item.get("messages", [])
            for i, text in enumerate(text_parts):
                if i < len(messages):
                    messages[i]["content"] = text
                else:
                    messages.append({"role": "assistant", "content": text})
    
    def _estimate_token_count(self, text: str) -> int:
        """토큰 수를 추정합니다."""
        # 간단한 토큰 수 추정
        words = len(text.split())
        return int(words * self.token_settings['words_per_token'])
    
    def _smart_truncate(self, text: str, max_tokens: int) -> str:
        """스마트 트렁케이션을 수행합니다."""
        # 문단 단위로 트렁케이션
        paragraphs = text.split('\n\n')
        result = []
        current_tokens = 0
        
        for paragraph in paragraphs:
            paragraph_tokens = self._estimate_token_count(paragraph)
            if current_tokens + paragraph_tokens <= max_tokens:
                result.append(paragraph)
                current_tokens += paragraph_tokens
            else:
                # 문단 내에서 문장 단위로 트렁케이션
                sentences = paragraph.split('.')
                for sentence in sentences:
                    sentence_tokens = self._estimate_token_count(sentence)
                    if current_tokens + sentence_tokens <= max_tokens:
                        result.append(sentence)
                        current_tokens += sentence_tokens
                    else:
                        break
                break
        
        return '\n\n'.join(result)
    
    def _simple_truncate(self, text: str, max_tokens: int) -> str:
        """단순 트렁케이션을 수행합니다."""
        # 문자 수 기반 트렁케이션
        max_chars = int(max_tokens * self.token_settings['chars_per_token'])
        return text[:max_chars]
    
    def _fix_conversation_sequence(self, conversations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """대화 시퀀스를 수정합니다."""
        if not conversations:
            return conversations
        
        # 기대되는 시퀀스
        expected_sequence = ['system', 'human', 'gpt']
        
        # 시퀀스 재구성
        corrected_conversations = []
        current_role_index = 0
        
        for conv in conversations:
            role = conv.get("from", "")
            
            # 올바른 역할 찾기
            if role in expected_sequence:
                role_index = expected_sequence.index(role)
                if role_index >= current_role_index:
                    corrected_conversations.append(conv)
                    current_role_index = role_index + 1
                else:
                    # 순서가 잘못된 경우, 다음 기대 역할로 변경
                    if current_role_index < len(expected_sequence):
                        conv["from"] = expected_sequence[current_role_index]
                        corrected_conversations.append(conv)
                        current_role_index += 1
            else:
                # 알 수 없는 역할인 경우, 다음 기대 역할로 변경
                if current_role_index < len(expected_sequence):
                    conv["from"] = expected_sequence[current_role_index]
                    corrected_conversations.append(conv)
                    current_role_index += 1
        
        return corrected_conversations
    
    def _fix_message_sequence(self, messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """메시지 시퀀스를 수정합니다."""
        if not messages:
            return messages
        
        # 기대되는 시퀀스
        expected_sequence = ['system', 'user', 'assistant']
        
        # 시퀀스 재구성
        corrected_messages = []
        current_role_index = 0
        
        for msg in messages:
            role = msg.get("role", "")
            
            # 올바른 역할 찾기
            if role in expected_sequence:
                role_index = expected_sequence.index(role)
                if role_index >= current_role_index:
                    corrected_messages.append(msg)
                    current_role_index = role_index + 1
                else:
                    # 순서가 잘못된 경우, 다음 기대 역할로 변경
                    if current_role_index < len(expected_sequence):
                        msg["role"] = expected_sequence[current_role_index]
                        corrected_messages.append(msg)
                        current_role_index += 1
            else:
                # 알 수 없는 역할인 경우, 다음 기대 역할로 변경
                if current_role_index < len(expected_sequence):
                    msg["role"] = expected_sequence[current_role_index]
                    corrected_messages.append(msg)
                    current_role_index += 1
        
        return corrected_messages
    
    def _estimate_quality_score(self, item: Dict[str, Any]) -> float:
        """품질 점수를 추정합니다."""
        # 간단한 품질 점수 추정
        text = self._extract_text_for_correction(item, "text")
        
        if not text:
            return 0.0
        
        # 길이 점수
        length_score = min(1.0, len(text) / 1000)
        
        # 구조 점수
        structure_score = 0.0
        if "conversations" in item and len(item["conversations"]) >= 2:
            structure_score = 1.0
        elif "instruction" in item and "output" in item:
            structure_score = 0.8
        elif "messages" in item and len(item["messages"]) >= 2:
            structure_score = 0.8
        
        # 종합 점수
        quality_score = (length_score + structure_score) / 2
        
        return max(0.0, min(1.0, quality_score))
    
    def _calculate_confidence_score(self, result: CorrectionResult) -> float:
        """신뢰도 점수를 계산합니다."""
        if not result.corrections_applied:
            return 0.0
        
        # 수정된 이슈 수와 전체 이슈 수 비율
        confidence = len(result.issues_fixed) / max(1, len(result.issues_fixed) + len(result.warnings))
        
        # 수정 강도 적용
        confidence *= self.config.correction_strength
        
        return max(0.0, min(1.0, confidence))
    
    def batch_correct_items(self, items: List[Dict[str, Any]], item_format: str, issues_list: List[List[str]] = None) -> List[CorrectionResult]:
        """
        배치로 아이템을 수정합니다.
        
        Args:
            items: 수정할 아이템 목록
            item_format: 아이템 포맷
            issues_list: 수정할 이슈 목록 목록
            
        Returns:
            수정 결과 목록
        """
        results = []
        
        if issues_list is None:
            issues_list = [None] * len(items)
        
        for i, (item, issues) in enumerate(zip(items, issues_list)):
            try:
                result = self.correct_item(item, item_format, issues)
                results.append(result)
                
                # 진행률 로깅
                if (i + 1) % 100 == 0:
                    self.logger.info(f"Processed {i + 1}/{len(items)} items")
                    
            except Exception as e:
                self.logger.error(f"Error correcting item {i}: {e}")
                # 오류 발생 시 기본 결과 반환
                error_result = CorrectionResult()
                error_result.original_item = item.copy()
                error_result.corrected_item = item.copy()
                error_result.warnings.append(f"수정 오류: {str(e)}")
                results.append(error_result)
        
        return results
    
    def get_correction_summary(self, results: List[CorrectionResult]) -> Dict[str, Any]:
        """수정 요약 정보를 생성합니다."""
        if not results:
            return {"total": 0, "corrected": 0, "failed": 0}
        
        total = len(results)
        corrected_count = sum(1 for r in results if r.changes_made)
        failed_count = sum(1 for r in results if r.warnings)
        
        # 수정 유형별 통계
        correction_types = Counter()
        for result in results:
            for correction in result.corrections_applied:
                correction_types[correction] += 1
        
        # 이슈별 수정 통계
        issues_fixed = Counter()
        for result in results:
            for issue in result.issues_fixed:
                issues_fixed[issue] += 1
        
        # 평균 신뢰도 점수
        avg_confidence = sum(r.confidence_score for r in results) / total
        
        return {
            "total": total,
            "corrected": corrected_count,
            "failed": failed_count,
            "correction_rate": corrected_count / total,
            "average_confidence": avg_confidence,
            "correction_types": dict(correction_types),
            "issues_fixed": dict(issues_fixed),
            "timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    # 테스트 데이터
    test_items = [
        {
            "conversations": [
                {"from": "system", "value": "Syncfusion WinForms 전문가"},
                {"from": "human", "value": "DataGrid 사용법을 알려주세요.."},  # 중복 구두점
                {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."}  # 중복 구두점
            ]
        },
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요",  # 문장 끝에 마침표 없음
            "input": "초보자도 이해할 수 있도록 설명해주세요",
            "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용"
        },
        {
            "messages": [
                {"role": "system", "content": "Syncfusion WinForms 전문가"},
                {"role": "user", "content": "Chart 컴포넌트 사용법을 알려주세요"},
                {"role": "assistant", "content": "Chart 컴포넌트 사용법은 다음과 같습니다..."}  # 중복 구두점
            ]
        }
    ]
    
    test_formats = ["sharegpt", "alpaca", "openai"]
    
    # 자동 수정기 생성
    auto_corrector = AutoCorrector()
    
    print("=== Auto Corrector Test ===")
    
    # 개별 아이템 수정 테스트
    for i, (item, item_format) in enumerate(zip(test_items, test_formats)):
        print(f"\nItem {i + 1} ({item_format} format):")
        result = auto_corrector.correct_item(item, item_format)
        
        print(f"  Changes Made: {result.changes_made}")
        print(f"  Confidence Score: {result.confidence_score:.2f}")
        print(f"  Corrections Applied: {result.corrections_applied}")
        print(f"  Issues Fixed: {result.issues_fixed}")
        print(f"  Warnings: {result.warnings}")
        
        # 수정된 아이템 비교
        if result.changes_made:
            print(f"  Original: {result.original_item}")
            print(f"  Corrected: {result.corrected_item}")
    
    # 배치 수정 테스트
    print(f"\n=== Batch Correction Test ===")
    batch_results = auto_corrector.batch_correct_items(test_items, "sharegpt")
    summary = auto_corrector.get_correction_summary(batch_results)
    
    print(f"Total Items: {summary['total']}")
    print(f"Corrected: {summary['corrected']}")
    print(f"Failed: {summary['failed']}")
    print(f"Correction Rate: {summary['correction_rate']:.2%}")
    print(f"Average Confidence: {summary['average_confidence']:.2f}")
    print(f"Correction Types: {summary['correction_types']}")
    print(f"Issues Fixed: {summary['issues_fixed']}")