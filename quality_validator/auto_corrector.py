#!/usr/bin/env python3
"""
자동 수정기 모듈
일반적인 포맷 문제를 자동으로 수정합니다.
"""

import re
import logging
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json
from pathlib import Path

__version__ = "1.0.0"
__author__ = "Auto Corrector Team"


@dataclass
class AutoCorrectorConfig:
    """자동 수정기 설정"""
    # 수정 활성화 옵션
    enable_text_normalization: bool = True
    enable_format_correction: bool = True
    enable_encoding_correction: bool = True
    enable_structure_correction: bool = True
    enable_content_enhancement: bool = True
    
    # 수정 강도 (conservative, moderate, aggressive)
    correction_strength: str = "moderate"
    
    # 최소 신뢰도 점수 (이 점수 이상일 때만 수정 적용)
    min_confidence_score: float = 0.7
    
    # 최대 수정 횟수
    max_corrections_per_item: int = 10
    
    # 언어 설정
    language: str = "ko"
    
    # 로깅 레벨
    log_level: str = "INFO"


@dataclass
class CorrectionResult:
    """수정 결과"""
    corrected_item: Dict[str, Any]
    changes_made: bool
    corrections_applied: List[str] = field(default_factory=list)
    confidence_score: float = 0.0
    original_issues: List[str] = field(default_factory=list)
    remaining_issues: List[str] = field(default_factory=list)
    details: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


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
        
        # 로깅 설정
        self._setup_logging()
        
        # 수정 규칙 초기화
        self._initialize_correction_rules()
        
        self.logger.info("AutoCorrector initialized successfully")
    
    def _setup_logging(self):
        """로깅을 설정합니다."""
        level = getattr(logging, self.config.log_level.upper(), logging.INFO)
        self.logger.setLevel(level)
    
    def _initialize_correction_rules(self):
        """수정 규칙을 초기화합니다."""
        # 텍스트 정규화 규칙
        self.text_normalization_rules = [
            # 공백 정규화
            (re.compile(r'\s+'), ' '),
            # 연속된 줄바꿈 정규화
            (re.compile(r'\n\s*\n\s*\n+'), '\n\n'),
            # 앞뒤 공백 제거
            (re.compile(r'^\s+|\s+$'), ''),
            # 탭을 공백으로 변환
            (re.compile(r'\t'), ' '),
        ]
        
        # 포맷 수정 규칙
        self.format_correction_rules = {
            # 일반적인 오타 수정
            "common_typos": [
                (r'\b사용벙\b', '사용법'),
                (r'\b컴포넌트트\b', '컴포넌트'),
                (r'\b데이터그리드\b', 'DataGrid'),
                (r'\b차트트\b', 'Chart'),
                (r'\b윈폼스\b', 'WinForms'),
                (r'\b싱크퓨전\b', 'Syncfusion'),
            ],
            
            # 기술 용어 표준화
            "technical_terms": [
                (r'\bdatagrid\b', 'DataGrid'),
                (r'\bchart\b', 'Chart'),
                (r'\bwinforms\b', 'WinForms'),
                (r'\bsyncfusion\b', 'Syncfusion'),
                (r'\bc#\b', 'C#'),
                (r'\bvb\.net\b', 'VB.NET'),
            ],
            
            # 구두점 수정
            "punctuation": [
                (r'([.!?])\s*([.!?])+', r'\1'),  # 연속된 구두점 제거
                (r'([가-힣])\s*([.!?])', r'\1\2'),  # 한글과 구두점 사이 공백 제거
                (r'([.!?])\s*([가-힣A-Za-z])', r'\1 \2'),  # 구두점 후 공백 추가
            ]
        }
        
        # 구조 수정 규칙
        self.structure_correction_rules = {
            # 대화 구조 수정
            "conversation_structure": [
                # 빈 대화 제거
                lambda conversations: [c for c in conversations if c.get("value", "").strip()],
                # 연속된 같은 역할 대화 병합
                self._merge_consecutive_same_role,
                # 시스템 메시지 정규화
                self._normalize_system_messages,
            ],
            
            # 메타데이터 구조 수정
            "metadata_structure": [
                # 빈 메타데이터 제거
                lambda metadata: {k: v for k, v in metadata.items() if v is not None and v != ""},
                # 표준 메타데이터 키 정규화
                self._normalize_metadata_keys,
            ]
        }
        
        # 콘텐츠 향상 규칙
        self.content_enhancement_rules = {
            # 코드 블록 포맷팅
            "code_formatting": [
                (r'```(\w+)?\s*\n(.*?)\n```', self._format_code_block),
                (r'`([^`]+)`', r'`\1`'),  # 인라인 코드 정규화
            ],
            
            # 목록 포맷팅
            "list_formatting": [
                (r'^(\d+)\.\s*(.+)$', r'\1. \2'),  # 번호 목록 정규화
                (r'^[-*]\s*(.+)$', r'- \1'),  # 불릿 목록 정규화
            ]
        }
        
        self.logger.info("Correction rules initialized")
    
    def correct_item(self, item: Dict[str, Any], format_type: str = "sharegpt") -> CorrectionResult:
        """
        아이템을 자동으로 수정합니다.
        
        Args:
            item: 수정할 아이템
            format_type: 데이터 포맷 타입
            
        Returns:
            수정 결과
        """
        try:
            # 원본 아이템 복사
            corrected_item = self._deep_copy_item(item)
            corrections_applied = []
            
            # 원본 이슈 분석
            original_issues = self._analyze_issues(item, format_type)
            
            # 수정 적용
            if self.config.enable_text_normalization:
                corrected_item, text_corrections = self._apply_text_normalization(corrected_item, format_type)
                corrections_applied.extend(text_corrections)
            
            if self.config.enable_format_correction:
                corrected_item, format_corrections = self._apply_format_correction(corrected_item, format_type)
                corrections_applied.extend(format_corrections)
            
            if self.config.enable_encoding_correction:
                corrected_item, encoding_corrections = self._apply_encoding_correction(corrected_item, format_type)
                corrections_applied.extend(encoding_corrections)
            
            if self.config.enable_structure_correction:
                corrected_item, structure_corrections = self._apply_structure_correction(corrected_item, format_type)
                corrections_applied.extend(structure_corrections)
            
            if self.config.enable_content_enhancement:
                corrected_item, enhancement_corrections = self._apply_content_enhancement(corrected_item, format_type)
                corrections_applied.extend(enhancement_corrections)
            
            # 수정 후 이슈 분석
            remaining_issues = self._analyze_issues(corrected_item, format_type)
            
            # 신뢰도 점수 계산
            confidence_score = self._calculate_confidence_score(
                original_issues, remaining_issues, corrections_applied
            )
            
            # 신뢰도가 낮으면 원본 반환
            if confidence_score < self.config.min_confidence_score:
                self.logger.warning(f"Low confidence score ({confidence_score:.3f}), returning original item")
                corrected_item = item
                corrections_applied = []
            
            result = CorrectionResult(
                corrected_item=corrected_item,
                changes_made=len(corrections_applied) > 0,
                corrections_applied=corrections_applied,
                confidence_score=confidence_score,
                original_issues=original_issues,
                remaining_issues=remaining_issues,
                details={
                    "format_type": format_type,
                    "correction_strength": self.config.correction_strength,
                    "total_corrections": len(corrections_applied)
                }
            )
            
            self.logger.debug(f"Correction completed: {len(corrections_applied)} corrections applied")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error in auto correction: {e}")
            return CorrectionResult(
                corrected_item=item,
                changes_made=False,
                original_issues=[f"Correction error: {str(e)}"]
            )
    
    def _deep_copy_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """아이템을 깊은 복사합니다."""
        return json.loads(json.dumps(item))
    
    def _analyze_issues(self, item: Dict[str, Any], format_type: str) -> List[str]:
        """아이템의 이슈를 분석합니다."""
        issues = []
        
        # 텍스트 콘텐츠 추출
        text_content = self._extract_text_content(item, format_type)
        
        # 공백 관련 이슈
        if re.search(r'\s{3,}', text_content):
            issues.append("Excessive whitespace")
        
        if re.search(r'\n\s*\n\s*\n+', text_content):
            issues.append("Excessive line breaks")
        
        # 구두점 이슈
        if re.search(r'[.!?]{2,}', text_content):
            issues.append("Repeated punctuation")
        
        # 인코딩 이슈
        if re.search(r'[^\x00-\x7F가-힣ㄱ-ㅎㅏ-ㅣ]', text_content):
            issues.append("Unusual characters")
        
        # 구조적 이슈
        if format_type == "sharegpt":
            conversations = item.get("conversations", [])
            if not conversations:
                issues.append("Empty conversations")
            
            # 빈 대화 확인
            empty_conversations = [c for c in conversations if not c.get("value", "").strip()]
            if empty_conversations:
                issues.append("Empty conversation entries")
        
        elif format_type == "alpaca":
            if not item.get("instruction", "").strip():
                issues.append("Empty instruction")
            if not item.get("output", "").strip():
                issues.append("Empty output")
        
        elif format_type == "openai":
            messages = item.get("messages", [])
            if not messages:
                issues.append("Empty messages")
            
            empty_messages = [m for m in messages if not m.get("content", "").strip()]
            if empty_messages:
                issues.append("Empty message entries")
        
        return issues
    
    def _extract_text_content(self, item: Dict[str, Any], format_type: str) -> str:
        """아이템에서 텍스트 콘텐츠를 추출합니다."""
        text_parts = []
        
        try:
            if format_type == "sharegpt":
                conversations = item.get("conversations", [])
                for conv in conversations:
                    if isinstance(conv, dict) and "value" in conv:
                        text_parts.append(conv["value"])
            
            elif format_type == "alpaca":
                for key in ["instruction", "input", "output"]:
                    if key in item and item[key]:
                        text_parts.append(item[key])
            
            elif format_type == "openai":
                messages = item.get("messages", [])
                for msg in messages:
                    if isinstance(msg, dict) and "content" in msg:
                        text_parts.append(msg["content"])
            
            return " ".join(text_parts)
            
        except Exception as e:
            self.logger.error(f"Error extracting text content: {e}")
            return ""
    
    def _apply_text_normalization(self, item: Dict[str, Any], format_type: str) -> Tuple[Dict[str, Any], List[str]]:
        """텍스트 정규화를 적용합니다."""
        corrections = []
        
        def normalize_text(text: str) -> str:
            if not text:
                return text
            
            original_text = text
            
            # 정규화 규칙 적용
            for pattern, replacement in self.text_normalization_rules:
                text = pattern.sub(replacement, text)
            
            if text != original_text:
                corrections.append("Text normalization applied")
            
            return text.strip()
        
        # 포맷별 텍스트 정규화
        if format_type == "sharegpt":
            conversations = item.get("conversations", [])
            for conv in conversations:
                if "value" in conv:
                    conv["value"] = normalize_text(conv["value"])
        
        elif format_type == "alpaca":
            for key in ["instruction", "input", "output"]:
                if key in item and item[key]:
                    item[key] = normalize_text(item[key])
        
        elif format_type == "openai":
            messages = item.get("messages", [])
            for msg in messages:
                if "content" in msg:
                    msg["content"] = normalize_text(msg["content"])
        
        return item, corrections
    
    def _apply_format_correction(self, item: Dict[str, Any], format_type: str) -> Tuple[Dict[str, Any], List[str]]:
        """포맷 수정을 적용합니다."""
        corrections = []
        
        def correct_text_format(text: str) -> str:
            if not text:
                return text
            
            original_text = text
            
            # 각 카테고리별 수정 규칙 적용
            for category, rules in self.format_correction_rules.items():
                for pattern, replacement in rules:
                    if isinstance(pattern, str):
                        pattern = re.compile(pattern, re.IGNORECASE)
                    text = pattern.sub(replacement, text)
            
            if text != original_text:
                corrections.append(f"Format correction applied")
            
            return text
        
        # 포맷별 텍스트 수정
        if format_type == "sharegpt":
            conversations = item.get("conversations", [])
            for conv in conversations:
                if "value" in conv:
                    conv["value"] = correct_text_format(conv["value"])
        
        elif format_type == "alpaca":
            for key in ["instruction", "input", "output"]:
                if key in item and item[key]:
                    item[key] = correct_text_format(item[key])
        
        elif format_type == "openai":
            messages = item.get("messages", [])
            for msg in messages:
                if "content" in msg:
                    msg["content"] = correct_text_format(msg["content"])
        
        return item, corrections
    
    def _apply_encoding_correction(self, item: Dict[str, Any], format_type: str) -> Tuple[Dict[str, Any], List[str]]:
        """인코딩 수정을 적용합니다."""
        corrections = []
        
        def correct_encoding(text: str) -> str:
            if not text:
                return text
            
            original_text = text
            
            # 일반적인 인코딩 문제 수정
            encoding_fixes = [
                ('\u00a0', ' '),  # Non-breaking space
                ('\u2018', "'"),  # Left single quotation mark
                ('\u2019', "'"),  # Right single quotation mark
                ('\u201c', '"'),  # Left double quotation mark
                ('\u201d', '"'),  # Right double quotation mark
                ('\u2013', '-'),  # En dash
                ('\u2014', '-'),  # Em dash
                ('\u2026', '...'),  # Horizontal ellipsis
            ]
            
            for old_char, new_char in encoding_fixes:
                text = text.replace(old_char, new_char)
            
            # 제어 문자 제거 (탭과 줄바꿈 제외)
            text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
            
            if text != original_text:
                corrections.append("Encoding correction applied")
            
            return text
        
        # 포맷별 인코딩 수정
        if format_type == "sharegpt":
            conversations = item.get("conversations", [])
            for conv in conversations:
                if "value" in conv:
                    conv["value"] = correct_encoding(conv["value"])
        
        elif format_type == "alpaca":
            for key in ["instruction", "input", "output"]:
                if key in item and item[key]:
                    item[key] = correct_encoding(item[key])
        
        elif format_type == "openai":
            messages = item.get("messages", [])
            for msg in messages:
                if "content" in msg:
                    msg["content"] = correct_encoding(msg["content"])
        
        return item, corrections
    
    def _apply_structure_correction(self, item: Dict[str, Any], format_type: str) -> Tuple[Dict[str, Any], List[str]]:
        """구조 수정을 적용합니다."""
        corrections = []
        
        if format_type == "sharegpt":
            conversations = item.get("conversations", [])
            original_count = len(conversations)
            
            # 구조 수정 규칙 적용
            for rule in self.structure_correction_rules["conversation_structure"]:
                if callable(rule):
                    conversations = rule(conversations)
            
            item["conversations"] = conversations
            
            if len(conversations) != original_count:
                corrections.append("Conversation structure corrected")
        
        elif format_type == "openai":
            messages = item.get("messages", [])
            original_count = len(messages)
            
            # 빈 메시지 제거
            messages = [m for m in messages if m.get("content", "").strip()]
            
            # 연속된 같은 역할 메시지 병합
            merged_messages = []
            for msg in messages:
                if merged_messages and merged_messages[-1].get("role") == msg.get("role"):
                    merged_messages[-1]["content"] += " " + msg.get("content", "")
                else:
                    merged_messages.append(msg)
            
            item["messages"] = merged_messages
            
            if len(merged_messages) != original_count:
                corrections.append("Message structure corrected")
        
        # 메타데이터 구조 수정
        if "metadata" in item:
            original_metadata = item["metadata"].copy()
            
            for rule in self.structure_correction_rules["metadata_structure"]:
                if callable(rule):
                    item["metadata"] = rule(item["metadata"])
            
            if item["metadata"] != original_metadata:
                corrections.append("Metadata structure corrected")
        
        return item, corrections
    
    def _apply_content_enhancement(self, item: Dict[str, Any], format_type: str) -> Tuple[Dict[str, Any], List[str]]:
        """콘텐츠 향상을 적용합니다."""
        corrections = []
        
        def enhance_content(text: str) -> str:
            if not text:
                return text
            
            original_text = text
            
            # 코드 블록 포맷팅
            for pattern, replacement in self.content_enhancement_rules["code_formatting"]:
                if callable(replacement):
                    text = re.sub(pattern, replacement, text, flags=re.DOTALL)
                else:
                    text = re.sub(pattern, replacement, text, flags=re.MULTILINE)
            
            # 목록 포맷팅
            lines = text.split('\n')
            enhanced_lines = []
            
            for line in lines:
                for pattern, replacement in self.content_enhancement_rules["list_formatting"]:
                    line = re.sub(pattern, replacement, line)
                enhanced_lines.append(line)
            
            text = '\n'.join(enhanced_lines)
            
            if text != original_text:
                corrections.append("Content enhancement applied")
            
            return text
        
        # 포맷별 콘텐츠 향상
        if format_type == "sharegpt":
            conversations = item.get("conversations", [])
            for conv in conversations:
                if "value" in conv:
                    conv["value"] = enhance_content(conv["value"])
        
        elif format_type == "alpaca":
            for key in ["instruction", "input", "output"]:
                if key in item and item[key]:
                    item[key] = enhance_content(item[key])
        
        elif format_type == "openai":
            messages = item.get("messages", [])
            for msg in messages:
                if "content" in msg:
                    msg["content"] = enhance_content(msg["content"])
        
        return item, corrections
    
    def _merge_consecutive_same_role(self, conversations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """연속된 같은 역할의 대화를 병합합니다."""
        if not conversations:
            return conversations
        
        merged = []
        for conv in conversations:
            if merged and merged[-1].get("from") == conv.get("from"):
                # 같은 역할이면 내용 병합
                merged[-1]["value"] += " " + conv.get("value", "")
            else:
                merged.append(conv)
        
        return merged
    
    def _normalize_system_messages(self, conversations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """시스템 메시지를 정규화합니다."""
        for conv in conversations:
            if conv.get("from") == "system":
                # 시스템 메시지 표준화
                value = conv.get("value", "")
                if "전문가" not in value and "assistant" not in value.lower():
                    conv["value"] = "Syncfusion WinForms 전문가"
        
        return conversations
    
    def _normalize_metadata_keys(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """메타데이터 키를 정규화합니다."""
        key_mappings = {
            "timestamp": "generation_timestamp",
            "created_at": "generation_timestamp",
            "source": "source_documents",
            "quality": "quality_score"
        }
        
        normalized = {}
        for key, value in metadata.items():
            normalized_key = key_mappings.get(key, key)
            normalized[normalized_key] = value
        
        return normalized
    
    def _format_code_block(self, match) -> str:
        """코드 블록을 포맷팅합니다."""
        language = match.group(1) or ""
        code = match.group(2).strip()
        
        # 기본 코드 정리
        lines = code.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # 앞뒤 공백 정리
            cleaned_line = line.rstrip()
            cleaned_lines.append(cleaned_line)
        
        # 빈 줄 제거 (시작과 끝)
        while cleaned_lines and not cleaned_lines[0]:
            cleaned_lines.pop(0)
        while cleaned_lines and not cleaned_lines[-1]:
            cleaned_lines.pop()
        
        cleaned_code = '\n'.join(cleaned_lines)
        
        return f"```{language}\n{cleaned_code}\n```"
    
    def _calculate_confidence_score(self, original_issues: List[str], remaining_issues: List[str], corrections: List[str]) -> float:
        """신뢰도 점수를 계산합니다."""
        if not original_issues and not corrections:
            return 1.0  # 원래 문제가 없고 수정도 없으면 완벽
        
        if not original_issues:
            return 0.8  # 원래 문제가 없었는데 수정했으면 약간 낮은 신뢰도
        
        # 해결된 이슈 비율
        resolved_issues = len(original_issues) - len(remaining_issues)
        resolution_rate = resolved_issues / len(original_issues) if original_issues else 0
        
        # 수정 횟수에 따른 신뢰도 조정
        correction_penalty = min(len(corrections) * 0.05, 0.3)
        
        # 수정 강도에 따른 조정
        strength_multiplier = {
            "conservative": 0.9,
            "moderate": 1.0,
            "aggressive": 1.1
        }.get(self.config.correction_strength, 1.0)
        
        confidence = (resolution_rate * strength_multiplier) - correction_penalty
        
        return max(0.0, min(confidence, 1.0))
    
    def batch_correct_items(self, items: List[Dict[str, Any]], format_type: str = "sharegpt") -> List[CorrectionResult]:
        """
        여러 아이템을 배치로 수정합니다.
        
        Args:
            items: 수정할 아이템 목록
            format_type: 데이터 포맷 타입
            
        Returns:
            수정 결과 목록
        """
        results = []
        
        for i, item in enumerate(items):
            try:
                result = self.correct_item(item, format_type)
                results.append(result)
                
                if (i + 1) % 100 == 0:
                    self.logger.info(f"Processed {i + 1}/{len(items)} items for auto correction")
                    
            except Exception as e:
                self.logger.error(f"Error correcting item {i}: {e}")
                results.append(CorrectionResult(
                    corrected_item=item,
                    changes_made=False,
                    original_issues=[f"Correction error: {str(e)}"]
                ))
        
        corrected_count = sum(1 for r in results if r.changes_made)
        self.logger.info(f"Auto correction completed: {corrected_count}/{len(results)} items corrected")
        
        return results
    
    def get_correction_statistics(self, results: List[CorrectionResult]) -> Dict[str, Any]:
        """수정 통계를 생성합니다."""
        if not results:
            return {}
        
        corrected_count = sum(1 for r in results if r.changes_made)
        
        # 수정 타입별 통계
        correction_types = {}
        for result in results:
            for correction in result.corrections_applied:
                correction_types[correction] = correction_types.get(correction, 0) + 1
        
        # 신뢰도 통계
        confidence_scores = [r.confidence_score for r in results]
        avg_confidence = sum(confidence_scores) / len(confidence_scores)
        
        # 이슈 해결 통계
        total_original_issues = sum(len(r.original_issues) for r in results)
        total_remaining_issues = sum(len(r.remaining_issues) for r in results)
        resolution_rate = (total_original_issues - total_remaining_issues) / total_original_issues if total_original_issues > 0 else 0
        
        return {
            "total_items": len(results),
            "corrected_items": corrected_count,
            "uncorrected_items": len(results) - corrected_count,
            "correction_rate": corrected_count / len(results),
            "average_confidence": avg_confidence,
            "min_confidence": min(confidence_scores),
            "max_confidence": max(confidence_scores),
            "correction_types": correction_types,
            "total_original_issues": total_original_issues,
            "total_remaining_issues": total_remaining_issues,
            "issue_resolution_rate": resolution_rate,
            "average_corrections_per_item": sum(len(r.corrections_applied) for r in results) / len(results)
        }
    
    def save_correction_report(self, results: List[CorrectionResult], output_path: str) -> bool:
        """수정 리포트를 저장합니다."""
        try:
            report = {
                "report_version": "1.0.0",
                "generated_at": datetime.now().isoformat(),
                "configuration": {
                    "enable_text_normalization": self.config.enable_text_normalization,
                    "enable_format_correction": self.config.enable_format_correction,
                    "enable_encoding_correction": self.config.enable_encoding_correction,
                    "enable_structure_correction": self.config.enable_structure_correction,
                    "enable_content_enhancement": self.config.enable_content_enhancement,
                    "correction_strength": self.config.correction_strength,
                    "min_confidence_score": self.config.min_confidence_score,
                    "max_corrections_per_item": self.config.max_corrections_per_item
                },
                "statistics": self.get_correction_statistics(results),
                "detailed_results": [
                    {
                        "changes_made": r.changes_made,
                        "corrections_applied": r.corrections_applied,
                        "confidence_score": r.confidence_score,
                        "original_issues": r.original_issues,
                        "remaining_issues": r.remaining_issues,
                        "details": r.details,
                        "timestamp": r.timestamp
                    }
                    for r in results
                ]
            }
            
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"Correction report saved to {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving correction report: {e}")
            return False


def create_default_auto_corrector() -> AutoCorrector:
    """기본 설정으로 자동 수정기를 생성합니다."""
    config = AutoCorrectorConfig(
        enable_text_normalization=True,
        enable_format_correction=True,
        enable_encoding_correction=True,
        enable_structure_correction=True,
        enable_content_enhancement=True,
        correction_strength="moderate",
        min_confidence_score=0.7,
        max_corrections_per_item=10,
        language="ko",
        log_level="INFO"
    )
    
    return AutoCorrector(config)


if __name__ == "__main__":
    # 모듈 테스트
    print(f"Auto Corrector Module v{__version__}")
    print(f"Author: {__author__}")
    
    # 샘플 테스트
    auto_corrector = create_default_auto_corrector()
    
    # 테스트 데이터 (문제가 있는 데이터)
    test_items = [
        {
            "conversations": [
                {"from": "human", "value": "syncfusion   datagrid  사용벙을   알려주세요..."},
                {"from": "gpt", "value": "  DataGrid  컴포넌트트는   다음과   같이   사용합니다.\n\n\n\n1. 프로젝트에 참조 추가\n2. 컨트롤 배치  "}
            ]
        },
        {
            "conversations": [
                {"from": "human", "value": ""},  # 빈 대화
                {"from": "gpt", "value": "chart 컴포넌트 사용법을 설명드리겠습니다."},
                {"from": "gpt", "value": "추가 설명입니다."}  # 연속된 같은 역할
            ]
        }
    ]
    
    # 자동 수정
    results = auto_corrector.batch_correct_items(test_items)
    
    for i, result in enumerate(results):
        print(f"\nItem {i+1}:")
        print(f"  Changes made: {result.changes_made}")
        print(f"  Corrections: {result.corrections_applied}")
        print(f"  Confidence: {result.confidence_score:.3f}")
        print(f"  Original issues: {result.original_issues}")
        print(f"  Remaining issues: {result.remaining_issues}")
    
    # 통계 출력
    stats = auto_corrector.get_correction_statistics(results)
    print(f"\nStatistics:")
    print(f"  Correction rate: {stats['correction_rate']:.3f}")
    print(f"  Average confidence: {stats['average_confidence']:.3f}")
    print(f"  Issue resolution rate: {stats['issue_resolution_rate']:.3f}")