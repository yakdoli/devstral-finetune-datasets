#!/usr/bin/env python3
"""
안전성 필터링 모듈
부적절한 콘텐츠 및 개인정보를 탐지하고 제거하는 안전성 필터링 기능을 제공합니다.
"""

import re
import logging
import hashlib
from typing import List, Dict, Any, Optional, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class SafetyFilterConfig:
    """안전성 필터 설정"""
    # 욕설 필터링 설정
    profanity_threshold: float = 0.8
    custom_profanity_words: Optional[Set[str]] = None
    
    # 개인정보 필터링 설정
    pii_detection_enabled: bool = True
    pii_patterns: Dict[str, str] = field(default_factory=dict)
    
    # 저작권 위반 검사 설정
    copyright_check_enabled: bool = True
    min_code_length: int = 50
    code_patterns: List[str] = field(default_factory=list)
    
    # 콘텐츠 길이 제한
    min_content_length: int = 10
    max_content_length: int = 50000
    
    # 필터링 모드
    strict_mode: bool = True
    auto_correction: bool = True


@dataclass
class SafetyResult:
    """안전성 검사 결과"""
    is_safe: bool = True
    safety_score: float = 1.0
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    pii_detected: Dict[str, List[str]] = field(default_factory=dict)
    profanity_score: float = 0.0
    copyright_issues: List[str] = field(default_factory=list)
    corrected_content: Optional[str] = None
    detection_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class SafetyFilter:
    """안전성 필터 클래스"""
    
    def __init__(self, config: Optional[SafetyFilterConfig] = None):
        """
        안전성 필터를 초기화합니다.
        
        Args:
            config: 안전성 필터 설정
        """
        self.config = config or SafetyFilterConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 기본 욕설 패턴
        self._setup_default_profanity_patterns()
        
        # 기본 PII 패턴
        self._setup_default_pii_patterns()
        
        # 기본 코드 패턴
        self._setup_default_code_patterns()
        
        # 커스텀 욕설 단어 추가
        if self.config.custom_profanity_words:
            self.profanity_patterns.extend(self.config.custom_profanity_words)
    
    def _setup_default_profanity_patterns(self):
        """기본 욕설 패턴을 설정합니다."""
        # 한국어 욕설 패턴 (간소화된 버전)
        self.profanity_patterns = [
            r'씨발', r'병신', r'ㅅㅂ', r'ㅂㅅ', r'ㅄ', r'ㅅㅂㄹㅇ',
            r'개새끼', r'새끼', r'ㅂㅅㅂㅅ', r'ㅅㅂㅅㅂ',
            r'존나', r'존나게', r'존나게쌉', r'존나게씨발',
            r'ㅅㅂㄹㅇㅁㅊ', r'ㅅㅂㄹㅇㅄ', r'ㅅㅂㄹㅇㄹㅇ',
            r'ㅄ', r'ㅁㅊ', r'ㅅㅂㄹㅇ', r'ㅅㅂㅂㅅ',
            # 영어 욕설
            r'fuck', r'shit', r'bitch', r'asshole', r'bastard',
            r'damn', r'crap', r'whore', r'slut', r'idiot',
            r'motherfucker', r'fucker', r'piss', r'dick', r'cock'
        ]
    
    def _setup_default_pii_patterns(self):
        """기본 PII 패턴을 설정합니다."""
        self.config.pii_patterns = {
            # 이메일 주소
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            # 전화번호 (한국형)
            'phone_kr': r'\b(?:\+82\s?1[0-9]\s?[0-9]{3,4}\s?[0-9]{4})\b',
            # 전화번호 (국제형)
            'phone_int': r'\b(?:\+\d{1,3}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b',
            # 주민등록번호 (한국)
            'resident_id_kr': r'\b(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12][0-9]|3[01])-[1-4][0-9]{6})\b',
            # 주민등록번호 (간소화)
            'resident_id_simple': r'\b\d{6}-[1-4]\d{6}\b',
            # 신용카드 번호
            'credit_card': r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
            # IP 주소
            'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
            # URL
            'url': r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?',
            # 사용자 이름 (간단한 형식)
            'username': r'@[A-Za-z0-9_]+',
            # 파일 경로
            'file_path': r'[A-Za-z]:\\[^\\]+(?:\\[^\\]+)*\.[A-Za-z]{2,4}',
            # 웹사이트 도메인
            'domain': r'\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b'
        }
    
    def _setup_default_code_patterns(self):
        """기본 코드 패턴을 설정합니다."""
        self.config.code_patterns = [
            # 클래스 정의
            r'class\s+\w+',
            # 함수 정의
            r'def\s+\w+\s*\([^)]*\)',
            # import 문
            r'import\s+\w+',
            # from import 문
            r'from\s+\w+\s+import\s+',
            # try-except 블록
            r'try:.*?except',
            # if-else 블록
            r'if\s+.*?:.*?else:',
            # for 루프
            r'for\s+.*?in\s+.*?:',
            # while 루프
            r'while\s+.*?:',
            # 주석
            r'#.*?$',
            # 문자열 리터럴 (코드 스니펫)
            r'["\'].*?["\']',
            # 숫자 리터럴
            r'\b\d+\.\d+\b|\b\d+\b'
        ]
    
    def filter_content(self, content: str, content_type: str = "text") -> SafetyResult:
        """
        콘텐츠의 안전성을 검사하고 필터링합니다.
        
        Args:
            content: 검사할 콘텐츠
            content_type: 콘텐츠 타입 (text, code, conversation)
            
        Returns:
            안전성 검사 결과
        """
        result = SafetyResult()
        
        if not content or not content.strip():
            result.is_safe = False
            result.issues.append("빈 콘텐츠")
            return result
        
        # 길이 검사
        length_result = self._check_content_length(content)
        if not length_result.is_safe:
            result.is_safe = False
            result.issues.extend(length_result.issues)
        
        # 욕설 검사
        profanity_result = self._check_profanity(content)
        result.profanity_score = profanity_result.profanity_score
        if profanity_result.profanity_score > self.config.profanity_threshold:
            result.is_safe = False
            result.issues.append(f"욕설 감지 (점수: {profanity_result.profanity_score:.2f})")
        
        # PII 검사
        if self.config.pii_detection_enabled:
            pii_result = self._check_pii(content)
            result.pii_detected = pii_result.pii_detected
            if pii_result.pii_detected:
                result.is_safe = False
                result.issues.append(f"개인정보 감지: {list(pii_result.pii_detected.keys())}")
        
        # 저작권 위반 검사
        if self.config.copyright_check_enabled:
            copyright_result = self._check_copyright_violation(content, content_type)
            result.copyright_issues = copyright_result.copyright_issues
            if copyright_result.copyright_issues:
                result.is_safe = False
                result.issues.extend(copyright_result.copyright_issues)
        
        # 안전 점수 계산
        result.safety_score = self._calculate_safety_score(result)
        
        # 자동 수정
        if self.config.auto_correction and not result.is_safe:
            corrected_content = self._auto_correct_content(content, result)
            if corrected_content:
                result.corrected_content = corrected_content
        
        return result
    
    def filter_conversation(self, conversation: List[Dict[str, Any]]) -> SafetyResult:
        """
        대화의 안전성을 검사합니다.
        
        Args:
            conversation: 대화 데이터 (from, value 형식)
            
        Returns:
            안전성 검사 결과
        """
        result = SafetyResult()
        
        if not conversation:
            result.is_safe = False
            result.issues.append("빈 대화")
            return result
        
        # 각 대화 턴별로 검사
        for i, turn in enumerate(conversation):
            if not isinstance(turn, dict) or 'from' not in turn or 'value' not in turn:
                result.is_safe = False
                result.issues.append(f"대화 턴 {i}: 잘못된 형식")
                continue
            
            speaker = turn['from']
            content = turn['value']
            
            # 발화자별 검사
            turn_result = self.filter_content(content, "conversation")
            
            # 결과 병합
            if not turn_result.is_safe:
                result.is_safe = False
                result.issues.extend([f"{speaker}: {issue}" for issue in turn_result.issues])
                result.warnings.extend([f"{speaker}: {warning}" for warning in turn_result.warnings])
            
            result.pii_detected.update(turn_result.pii_detected)
            result.copyright_issues.extend(turn_result.copyright_issues)
            
            # 욕설 점수 누적
            result.profanity_score = max(result.profanity_score, turn_result.profanity_score)
        
        # 최종 안전 점수 계산
        result.safety_score = self._calculate_safety_score(result)
        
        return result
    
    def _check_content_length(self, content: str) -> SafetyResult:
        """콘텐츠 길이를 검사합니다."""
        result = SafetyResult()
        
        content_length = len(content.strip())
        
        if content_length < self.config.min_content_length:
            result.is_safe = False
            result.issues.append(f"콘텐츠가 너무 짧음 ({content_length} < {self.config.min_content_length})")
        
        if content_length > self.config.max_content_length:
            result.is_safe = False
            result.issues.append(f"콘텐츠가 너무 김 ({content_length} > {self.config.max_content_length})")
        
        return result
    
    def _check_profanity(self, content: str) -> SafetyResult:
        """욕설을 검사합니다."""
        result = SafetyResult()
        
        # 텍스트 정규화
        normalized_content = content.lower()
        
        # 욕설 패턴 매칭
        profanity_count = 0
        matched_patterns = []
        
        for pattern in self.profanity_patterns:
            matches = re.findall(pattern, normalized_content)
            if matches:
                profanity_count += len(matches)
                matched_patterns.append(pattern)
        
        # 욕설 점수 계산 (총 문자 수 대비 욕설 비율)
        total_chars = len(normalized_content)
        if total_chars > 0:
            result.profanity_score = min(1.0, profanity_count / (total_chars / 10))
        else:
            result.profanity_score = 0.0
        
        # 경고 추가
        if result.profanity_score > 0.3:
            result.warnings.append(f"욕설 패턴 감지: {matched_patterns}")
        
        return result
    
    def _check_pii(self, content: str) -> SafetyResult:
        """개인정보를 검사합니다."""
        result = SafetyResult()
        
        detected_pii = {}
        
        for pii_type, pattern in self.config.pii_patterns.items():
            matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE)
            if matches:
                detected_pii[pii_type] = matches
        
        result.pii_detected = detected_pii
        
        # 경고 추가
        if detected_pii:
            result.warnings.append(f"PII 감지: {list(detected_pii.keys())}")
        
        return result
    
    def _check_copyright_violation(self, content: str, content_type: str) -> SafetyResult:
        """저작권 위반을 검사합니다."""
        result = SafetyResult()
        
        # 코드 콘텐츠인 경우
        if content_type == "code":
            if len(content) > self.config.min_code_length:
                # 코드 패턴 확인
                code_pattern_count = 0
                for pattern in self.config.code_patterns:
                    if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                        code_pattern_count += 1
                
                # 코드 패턴이 너무 많으면 저작권 위반 의심
                if code_pattern_count > len(self.config.code_patterns) * 0.7:
                    result.copyright_issues.append("코드 구조가 저작권이 있는 코드와 유사합니다")
        
        # 일반 텍스트인 경우
        else:
            # 특정 키워드로 저작권 위반 의심
            copyright_keywords = [
                'copyright', '©', 'all rights reserved', 'patent', 'trademark',
                'licensed under', 'copyleft', 'public domain'
            ]
            
            for keyword in copyright_keywords:
                if keyword.lower() in content.lower():
                    result.copyright_issues.append(f"저작권 관련 키워드 발견: {keyword}")
                    break
        
        return result
    
    def _calculate_safety_score(self, result: SafetyResult) -> float:
        """안전 점수를 계산합니다."""
        base_score = 1.0
        
        # 욕설 점수 차감
        base_score -= result.profanity_score * 0.5
        
        # PII 감지 시 큰 점수 차감
        if result.pii_detected:
            base_score -= 0.4
        
        # 저작권 문제 시 점수 차감
        if result.copyright_issues:
            base_score -= 0.3
        
        # 이슈가 있을 경우 추가 차감
        if result.issues:
            base_score -= len(result.issues) * 0.1
        
        # 경고는 작은 점수 차감
        if result.warnings:
            base_score -= len(result.warnings) * 0.05
        
        # 점수 범위 제한
        return max(0.0, min(1.0, base_score))
    
    def _auto_correct_content(self, content: str, result: SafetyResult) -> Optional[str]:
        """콘텐츠를 자동으로 수정합니다."""
        if not self.config.auto_correction:
            return None
        
        corrected_content = content
        
        # 욕설 마스킹
        for pattern in self.profanity_patterns:
            corrected_content = re.sub(
                pattern, 
                '*' * len(pattern), 
                corrected_content, 
                flags=re.IGNORECASE
            )
        
        # PII 마스킹
        for pii_type, matches in result.pii_detected.items():
            for match in matches:
                if pii_type == 'email':
                    corrected_content = corrected_content.replace(match, '[EMAIL]')
                elif pii_type in ['phone_kr', 'phone_int']:
                    corrected_content = corrected_content.replace(match, '[PHONE]')
                elif pii_type in ['resident_id_kr', 'resident_id_simple']:
                    corrected_content = corrected_content.replace(match, '[ID]')
                elif pii_type == 'credit_card':
                    corrected_content = corrected_content.replace(match, '[CARD]')
                else:
                    corrected_content = corrected_content.replace(match, '[PII]')
        
        return corrected_content if corrected_content != content else None
    
    def batch_filter(self, contents: List[str], content_type: str = "text") -> List[SafetyResult]:
        """
        여러 콘텐츠를 배치로 필터링합니다.
        
        Args:
            contents: 필터링할 콘텐츠 목록
            content_type: 콘텐츠 타입
            
        Returns:
            필터링 결과 목록
        """
        results = []
        
        for i, content in enumerate(contents):
            try:
                if content_type == "conversation":
                    # 대화 형식인 경우
                    result = self.filter_conversation(content)
                else:
                    # 텍스트 형식인 경우
                    result = self.filter_content(content, content_type)
                
                results.append(result)
                
                # 진행률 로깅
                if (i + 1) % 100 == 0:
                    self.logger.info(f"Processed {i + 1}/{len(contents)} contents")
                    
            except Exception as e:
                self.logger.error(f"Error filtering content {i}: {e}")
                # 오류 발생 시 기본 결과 반환
                error_result = SafetyResult()
                error_result.is_safe = False
                error_result.issues.append(f"처리 오류: {str(e)}")
                results.append(error_result)
        
        return results
    
    def get_filter_summary(self, results: List[SafetyResult]) -> Dict[str, Any]:
        """필터링 요약 정보를 생성합니다."""
        if not results:
            return {"total": 0, "safe": 0, "unsafe": 0}
        
        total = len(results)
        safe_count = sum(1 for r in results if r.is_safe)
        unsafe_count = total - safe_count
        
        # 평균 안전 점수
        avg_safety_score = sum(r.safety_score for r in results) / total
        
        # PII 통계
        pii_detected_count = sum(1 for r in results if r.pii_detected)
        
        # 욕설 통계
        high_profanity_count = sum(1 for r in results if r.profanity_score > 0.5)
        
        return {
            "total": total,
            "safe": safe_count,
            "unsafe": unsafe_count,
            "safety_rate": safe_count / total,
            "average_safety_score": avg_safety_score,
            "pii_detected_count": pii_detected_count,
            "high_profanity_count": high_profanity_count,
            "timestamp": datetime.now().isoformat()
        }
    
    def check_safety(self, item: Dict[str, Any], item_type: str = "text") -> SafetyResult:
        """
        아이템의 안전성을 검사합니다.
        
        Args:
            item: 검사할 아이템
            item_type: 아이템 타입 (text, conversation, code)
            
        Returns:
            안전성 검사 결과
        """
        if item_type == "conversation":
            # 대화 형식인 경우
            conversation = item.get("conversations", [])
            return self.filter_conversation(conversation)
        else:
            # 텍스트 형식인 경우
            text = self._extract_text_from_item(item, item_type)
            if text:
                return self.filter_content(text, item_type)
            else:
                result = SafetyResult()
                result.is_safe = False
                result.issues.append("텍스트 추출 실패")
                return result
    
    def _extract_text_from_item(self, item: Dict[str, Any], item_type: str) -> str:
        """아이템에서 텍스트를 추출합니다."""
        if item_type == "text":
            return item.get("text", "")
        elif item_type == "instruction":
            return item.get("instruction", "") + " " + item.get("input", "") + " " + item.get("response", "")
        elif "conversations" in item:
            # 대화 형식인 경우 모든 턴의 텍스트를 합침
            texts = []
            for conv in item.get("conversations", []):
                texts.append(conv.get("value", ""))
            return " ".join(texts)
        else:
            # 기본적으로 모든 값을 합침
            text_parts = []
            for key, value in item.items():
                if isinstance(value, str):
                    text_parts.append(value)
            return " ".join(text_parts)


if __name__ == "__main__":
    # 테스트 데이터
    test_contents = [
        "이것은 일반적인 텍스트입니다.",
        "씨발 이런 내용은 욕설이 포함되어 있습니다.",
        "test@example.com 이메일 주소가 포함된 텍스트입니다.",
        "010-1234-5678 전화번호가 포함된 텍스트입니다.",
        "class MyClass:\n    def __init__(self):\n        pass\n    def method(self):\n        return 'test'",
        "이것은 저작권이 있는 코드와 유사한 내용입니다."
    ]
    
    # 안전성 필터 생성
    safety_filter = SafetyFilter()
    
    print("=== Safety Filter Test ===")
    
    # 개별 콘텐츠 필터링 테스트
    for i, content in enumerate(test_contents):
        print(f"\nContent {i + 1}: {content[:50]}...")
        result = safety_filter.filter_content(content)
        print(f"  Safe: {result.is_safe}")
        print(f"  Safety Score: {result.safety_score:.2f}")
        print(f"  Issues: {result.issues}")
        print(f"  Warnings: {result.warnings}")
        if result.pii_detected:
            print(f"  PII Detected: {result.pii_detected}")
        if result.corrected_content:
            print(f"  Corrected: {result.corrected_content[:50]}...")
    
    # 배치 필터링 테스트
    print(f"\n=== Batch Filtering Test ===")
    batch_results = safety_filter.batch_filter(test_contents)
    summary = safety_filter.get_filter_summary(batch_results)
    
    print(f"Total: {summary['total']}")
    print(f"Safe: {summary['safe']}")
    print(f"Unsafe: {summary['unsafe']}")
    print(f"Safety Rate: {summary['safety_rate']:.2%}")
    print(f"Average Safety Score: {summary['average_safety_score']:.2f}")
    print(f"PII Detected: {summary['pii_detected_count']}")
    print(f"High Profanity: {summary['high_profanity_count']}")