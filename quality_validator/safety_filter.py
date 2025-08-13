#!/usr/bin/env python3
"""
안전성 필터 모듈
부적절한 콘텐츠, 편향성, 유해 콘텐츠를 탐지하고 필터링합니다.
"""

import re
import logging
from typing import List, Dict, Any, Optional, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json
from pathlib import Path

__version__ = "1.0.0"
__author__ = "Safety Filter Team"


@dataclass
class SafetyFilterConfig:
    """안전성 필터 설정"""
    # 안전성 임계값
    safety_threshold: float = 0.8
    
    # 필터링 강도 (strict, moderate, lenient)
    filter_strength: str = "moderate"
    
    # 언어별 설정
    language: str = "ko"  # 한국어
    
    # 커스텀 금지어 목록
    custom_blocked_words: List[str] = field(default_factory=list)
    
    # 편향성 검사 활성화
    enable_bias_detection: bool = True
    
    # 유해 콘텐츠 검사 활성화
    enable_harmful_content_detection: bool = True
    
    # 개인정보 검사 활성화
    enable_pii_detection: bool = True
    
    # 기술적 콘텐츠 허용 (코드, API 등)
    allow_technical_content: bool = True
    
    # 로깅 레벨
    log_level: str = "INFO"


@dataclass
class SafetyResult:
    """안전성 검사 결과"""
    is_safe: bool
    safety_score: float
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    detected_categories: List[str] = field(default_factory=list)
    confidence_score: float = 0.0
    details: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


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
        
        # 로깅 설정
        self._setup_logging()
        
        # 필터링 규칙 초기화
        self._initialize_filters()
        
        self.logger.info("SafetyFilter initialized successfully")
    
    def _setup_logging(self):
        """로깅을 설정합니다."""
        level = getattr(logging, self.config.log_level.upper(), logging.INFO)
        self.logger.setLevel(level)
    
    def _initialize_filters(self):
        """필터링 규칙을 초기화합니다."""
        # 기본 금지어 목록 (한국어)
        self.blocked_words = {
            # 욕설 및 비속어
            "욕설": [
                "바보", "멍청이", "병신", "미친", "개새끼", "씨발", "좆", "존나",
                "개놈", "년", "놈", "새끼", "지랄", "빡친", "엿", "좇"
            ],
            
            # 차별적 표현
            "차별": [
                "장애인", "정신병자", "미개한", "후진국", "3류", "저급한",
                "열등한", "무식한", "촌스러운"
            ],
            
            # 정치적 편향
            "정치": [
                "좌파", "우파", "빨갱이", "수구", "진보충", "보수충",
                "문빠", "박빠", "윤빠"
            ],
            
            # 성적 콘텐츠
            "성적": [
                "섹스", "성관계", "야동", "포르노", "음란", "변태",
                "성기", "자위", "오르가즘"
            ],
            
            # 폭력적 콘텐츠
            "폭력": [
                "죽이", "살인", "자살", "폭행", "테러", "폭탄",
                "총", "칼", "무기", "살해"
            ]
        }
        
        # 커스텀 금지어 추가
        if self.config.custom_blocked_words:
            self.blocked_words["커스텀"] = self.config.custom_blocked_words
        
        # 개인정보 패턴
        self.pii_patterns = {
            "전화번호": re.compile(r'0\d{1,2}-\d{3,4}-\d{4}'),
            "이메일": re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'),
            "주민등록번호": re.compile(r'\d{6}-\d{7}'),
            "신용카드": re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}'),
            "계좌번호": re.compile(r'\d{3}-\d{2}-\d{6}')
        }
        
        # 편향성 키워드
        self.bias_keywords = {
            "성별": ["남자가", "여자가", "남성은", "여성은", "남자답게", "여자답게"],
            "연령": ["젊은이들은", "노인들은", "어른들은", "애들은"],
            "지역": ["서울사람", "지방사람", "촌놈", "깡촌"],
            "직업": ["의사는", "변호사는", "공무원은", "노동자는"],
            "학력": ["대졸자는", "고졸은", "명문대", "지잡대"]
        }
        
        # 기술적 콘텐츠 허용 패턴
        self.technical_patterns = [
            re.compile(r'\b(class|function|method|property|event)\b', re.IGNORECASE),
            re.compile(r'\b(API|SDK|DLL|EXE|COM)\b', re.IGNORECASE),
            re.compile(r'\b(Syncfusion|WinForms|DataGrid|Chart)\b', re.IGNORECASE),
            re.compile(r'\b(C#|VB\.NET|Visual Studio)\b', re.IGNORECASE),
            re.compile(r'\b(namespace|using|import|include)\b', re.IGNORECASE)
        ]
        
        self.logger.info(f"Initialized {len(self.blocked_words)} blocked word categories")
        self.logger.info(f"Initialized {len(self.pii_patterns)} PII patterns")
        self.logger.info(f"Initialized {len(self.bias_keywords)} bias categories")
    
    def check_safety(self, item: Dict[str, Any], format_type: str = "sharegpt") -> SafetyResult:
        """
        아이템의 안전성을 검사합니다.
        
        Args:
            item: 검사할 아이템
            format_type: 데이터 포맷 타입
            
        Returns:
            안전성 검사 결과
        """
        try:
            # 텍스트 추출
            text_content = self._extract_text_content(item, format_type)
            
            if not text_content:
                return SafetyResult(
                    is_safe=True,
                    safety_score=1.0,
                    warnings=["No text content found for safety check"]
                )
            
            # 안전성 검사 수행
            safety_result = self._perform_safety_checks(text_content)
            
            # 기술적 콘텐츠 예외 처리
            if self.config.allow_technical_content:
                safety_result = self._apply_technical_content_exceptions(safety_result, text_content)
            
            # 최종 안전성 점수 계산
            safety_result.safety_score = self._calculate_safety_score(safety_result)
            safety_result.is_safe = safety_result.safety_score >= self.config.safety_threshold
            
            # 상세 정보 추가
            safety_result.details = {
                "text_length": len(text_content),
                "format_type": format_type,
                "filter_strength": self.config.filter_strength,
                "technical_content_allowed": self.config.allow_technical_content
            }
            
            self.logger.debug(f"Safety check completed: score={safety_result.safety_score:.3f}, safe={safety_result.is_safe}")
            
            return safety_result
            
        except Exception as e:
            self.logger.error(f"Error in safety check: {e}")
            return SafetyResult(
                is_safe=False,
                safety_score=0.0,
                issues=[f"Safety check error: {str(e)}"]
            )
    
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
            
            # 메타데이터에서도 텍스트 추출
            metadata = item.get("metadata", {})
            if isinstance(metadata, dict):
                for key, value in metadata.items():
                    if isinstance(value, str) and len(value) > 10:
                        text_parts.append(value)
            
            return " ".join(text_parts)
            
        except Exception as e:
            self.logger.error(f"Error extracting text content: {e}")
            return ""
    
    def _perform_safety_checks(self, text: str) -> SafetyResult:
        """안전성 검사를 수행합니다."""
        result = SafetyResult(is_safe=True, safety_score=1.0)
        
        # 1. 금지어 검사
        blocked_word_issues = self._check_blocked_words(text)
        if blocked_word_issues:
            result.issues.extend(blocked_word_issues)
            result.detected_categories.append("blocked_words")
        
        # 2. 개인정보 검사
        if self.config.enable_pii_detection:
            pii_issues = self._check_pii(text)
            if pii_issues:
                result.issues.extend(pii_issues)
                result.detected_categories.append("pii")
        
        # 3. 편향성 검사
        if self.config.enable_bias_detection:
            bias_issues = self._check_bias(text)
            if bias_issues:
                result.warnings.extend(bias_issues)
                result.detected_categories.append("bias")
        
        # 4. 유해 콘텐츠 검사
        if self.config.enable_harmful_content_detection:
            harmful_issues = self._check_harmful_content(text)
            if harmful_issues:
                result.issues.extend(harmful_issues)
                result.detected_categories.append("harmful")
        
        # 5. 콘텐츠 품질 검사
        quality_issues = self._check_content_quality(text)
        if quality_issues:
            result.warnings.extend(quality_issues)
            result.detected_categories.append("quality")
        
        return result
    
    def _check_blocked_words(self, text: str) -> List[str]:
        """금지어를 검사합니다."""
        issues = []
        text_lower = text.lower()
        
        for category, words in self.blocked_words.items():
            found_words = []
            for word in words:
                if word.lower() in text_lower:
                    found_words.append(word)
            
            if found_words:
                issues.append(f"Blocked words detected in {category}: {', '.join(found_words)}")
        
        return issues
    
    def _check_pii(self, text: str) -> List[str]:
        """개인정보를 검사합니다."""
        issues = []
        
        for pii_type, pattern in self.pii_patterns.items():
            matches = pattern.findall(text)
            if matches:
                issues.append(f"PII detected ({pii_type}): {len(matches)} instances")
        
        return issues
    
    def _check_bias(self, text: str) -> List[str]:
        """편향성을 검사합니다."""
        warnings = []
        text_lower = text.lower()
        
        for category, keywords in self.bias_keywords.items():
            found_keywords = []
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    found_keywords.append(keyword)
            
            if found_keywords:
                warnings.append(f"Potential bias detected in {category}: {', '.join(found_keywords)}")
        
        return warnings
    
    def _check_harmful_content(self, text: str) -> List[str]:
        """유해 콘텐츠를 검사합니다."""
        issues = []
        text_lower = text.lower()
        
        # 자해/자살 관련 콘텐츠
        self_harm_keywords = ["자살", "자해", "죽고싶", "목매", "투신", "음독"]
        found_self_harm = [kw for kw in self_harm_keywords if kw in text_lower]
        if found_self_harm:
            issues.append(f"Self-harm content detected: {', '.join(found_self_harm)}")
        
        # 불법 활동 관련
        illegal_keywords = ["마약", "대마초", "해킹", "크랙", "불법복제", "저작권침해"]
        found_illegal = [kw for kw in illegal_keywords if kw in text_lower]
        if found_illegal:
            issues.append(f"Illegal activity content detected: {', '.join(found_illegal)}")
        
        # 혐오 표현
        hate_keywords = ["혐오", "차별", "배척", "추방", "박멸"]
        found_hate = [kw for kw in hate_keywords if kw in text_lower]
        if found_hate:
            issues.append(f"Hate speech detected: {', '.join(found_hate)}")
        
        return issues
    
    def _check_content_quality(self, text: str) -> List[str]:
        """콘텐츠 품질을 검사합니다."""
        warnings = []
        
        # 텍스트 길이 검사
        if len(text) < 10:
            warnings.append("Content too short")
        elif len(text) > 10000:
            warnings.append("Content too long")
        
        # 반복 패턴 검사
        words = text.split()
        if len(words) > 10:
            word_counts = {}
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
            
            # 단어 반복률 검사
            max_repetition = max(word_counts.values()) if word_counts else 0
            if max_repetition > len(words) * 0.3:
                warnings.append("High word repetition detected")
        
        # 특수문자 과다 사용 검사
        special_char_count = len(re.findall(r'[!@#$%^&*()_+={}\[\]|\\:";\'<>?,./]', text))
        if special_char_count > len(text) * 0.1:
            warnings.append("Excessive special characters")
        
        # 대문자 과다 사용 검사
        upper_count = sum(1 for c in text if c.isupper())
        if upper_count > len(text) * 0.3:
            warnings.append("Excessive uppercase letters")
        
        return warnings
    
    def _apply_technical_content_exceptions(self, result: SafetyResult, text: str) -> SafetyResult:
        """기술적 콘텐츠에 대한 예외를 적용합니다."""
        # 기술적 콘텐츠 패턴 검사
        is_technical = any(pattern.search(text) for pattern in self.technical_patterns)
        
        if is_technical:
            # 기술적 콘텐츠로 판단되면 일부 이슈를 경고로 변경
            technical_exceptions = []
            remaining_issues = []
            
            for issue in result.issues:
                # 기술 용어로 인한 오탐 제거
                if any(tech_term in issue.lower() for tech_term in ["api", "class", "method", "property"]):
                    technical_exceptions.append(f"Technical content exception: {issue}")
                else:
                    remaining_issues.append(issue)
            
            result.issues = remaining_issues
            result.warnings.extend(technical_exceptions)
            
            if technical_exceptions:
                result.details["technical_exceptions"] = len(technical_exceptions)
        
        return result
    
    def _calculate_safety_score(self, result: SafetyResult) -> float:
        """안전성 점수를 계산합니다."""
        base_score = 1.0
        
        # 이슈에 따른 점수 차감
        issue_penalty = len(result.issues) * 0.2
        warning_penalty = len(result.warnings) * 0.05
        
        # 카테고리별 가중치
        category_weights = {
            "blocked_words": 0.3,
            "pii": 0.4,
            "harmful": 0.5,
            "bias": 0.1,
            "quality": 0.05
        }
        
        category_penalty = 0.0
        for category in result.detected_categories:
            category_penalty += category_weights.get(category, 0.1)
        
        # 필터 강도에 따른 조정
        strength_multiplier = {
            "strict": 1.5,
            "moderate": 1.0,
            "lenient": 0.7
        }.get(self.config.filter_strength, 1.0)
        
        # 최종 점수 계산
        final_score = base_score - (issue_penalty + warning_penalty + category_penalty) * strength_multiplier
        
        # 점수 범위 제한 (0.0 ~ 1.0)
        return max(0.0, min(1.0, final_score))
    
    def batch_check_safety(self, items: List[Dict[str, Any]], format_type: str = "sharegpt") -> List[SafetyResult]:
        """
        여러 아이템의 안전성을 배치로 검사합니다.
        
        Args:
            items: 검사할 아이템 목록
            format_type: 데이터 포맷 타입
            
        Returns:
            안전성 검사 결과 목록
        """
        results = []
        
        for i, item in enumerate(items):
            try:
                result = self.check_safety(item, format_type)
                results.append(result)
                
                if (i + 1) % 100 == 0:
                    self.logger.info(f"Processed {i + 1}/{len(items)} items for safety check")
                    
            except Exception as e:
                self.logger.error(f"Error checking safety for item {i}: {e}")
                results.append(SafetyResult(
                    is_safe=False,
                    safety_score=0.0,
                    issues=[f"Safety check error: {str(e)}"]
                ))
        
        safe_count = sum(1 for r in results if r.is_safe)
        self.logger.info(f"Safety check completed: {safe_count}/{len(results)} items are safe")
        
        return results
    
    def get_safety_statistics(self, results: List[SafetyResult]) -> Dict[str, Any]:
        """안전성 검사 통계를 생성합니다."""
        if not results:
            return {}
        
        safe_count = sum(1 for r in results if r.is_safe)
        unsafe_count = len(results) - safe_count
        
        # 점수 통계
        scores = [r.safety_score for r in results]
        avg_score = sum(scores) / len(scores)
        min_score = min(scores)
        max_score = max(scores)
        
        # 카테고리별 통계
        category_counts = {}
        for result in results:
            for category in result.detected_categories:
                category_counts[category] = category_counts.get(category, 0) + 1
        
        # 이슈 통계
        total_issues = sum(len(r.issues) for r in results)
        total_warnings = sum(len(r.warnings) for r in results)
        
        return {
            "total_items": len(results),
            "safe_items": safe_count,
            "unsafe_items": unsafe_count,
            "safety_rate": safe_count / len(results),
            "average_safety_score": avg_score,
            "min_safety_score": min_score,
            "max_safety_score": max_score,
            "total_issues": total_issues,
            "total_warnings": total_warnings,
            "category_distribution": category_counts,
            "issues_per_item": total_issues / len(results),
            "warnings_per_item": total_warnings / len(results)
        }
    
    def save_safety_report(self, results: List[SafetyResult], output_path: str) -> bool:
        """안전성 검사 리포트를 저장합니다."""
        try:
            report = {
                "report_version": "1.0.0",
                "generated_at": datetime.now().isoformat(),
                "configuration": {
                    "safety_threshold": self.config.safety_threshold,
                    "filter_strength": self.config.filter_strength,
                    "language": self.config.language,
                    "enable_bias_detection": self.config.enable_bias_detection,
                    "enable_harmful_content_detection": self.config.enable_harmful_content_detection,
                    "enable_pii_detection": self.config.enable_pii_detection,
                    "allow_technical_content": self.config.allow_technical_content
                },
                "statistics": self.get_safety_statistics(results),
                "detailed_results": [
                    {
                        "is_safe": r.is_safe,
                        "safety_score": r.safety_score,
                        "issues": r.issues,
                        "warnings": r.warnings,
                        "detected_categories": r.detected_categories,
                        "confidence_score": r.confidence_score,
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
            
            self.logger.info(f"Safety report saved to {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving safety report: {e}")
            return False


def create_default_safety_filter() -> SafetyFilter:
    """기본 설정으로 안전성 필터를 생성합니다."""
    config = SafetyFilterConfig(
        safety_threshold=0.8,
        filter_strength="moderate",
        language="ko",
        enable_bias_detection=True,
        enable_harmful_content_detection=True,
        enable_pii_detection=True,
        allow_technical_content=True,
        log_level="INFO"
    )
    
    return SafetyFilter(config)


if __name__ == "__main__":
    # 모듈 테스트
    print(f"Safety Filter Module v{__version__}")
    print(f"Author: {__author__}")
    
    # 샘플 테스트
    safety_filter = create_default_safety_filter()
    
    # 테스트 데이터
    test_items = [
        {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        },
        {
            "conversations": [
                {"from": "human", "value": "이 바보같은 프로그램이 왜 안되는거야?"},
                {"from": "gpt", "value": "프로그램 오류를 해결하는 방법을 알려드리겠습니다."}
            ]
        }
    ]
    
    # 안전성 검사
    results = safety_filter.batch_check_safety(test_items)
    
    for i, result in enumerate(results):
        print(f"\nItem {i+1}:")
        print(f"  Safe: {result.is_safe}")
        print(f"  Score: {result.safety_score:.3f}")
        print(f"  Issues: {result.issues}")
        print(f"  Warnings: {result.warnings}")
    
    # 통계 출력
    stats = safety_filter.get_safety_statistics(results)
    print(f"\nStatistics:")
    print(f"  Safety rate: {stats['safety_rate']:.3f}")
    print(f"  Average score: {stats['average_safety_score']:.3f}")
    print(f"  Total issues: {stats['total_issues']}")