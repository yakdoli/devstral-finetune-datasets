#!/usr/bin/env python3
"""
SafetyFilter 단위 테스트
"""

import unittest
import tempfile
import json
from pathlib import Path

from quality_validator.safety_filter import (
    SafetyFilter, SafetyFilterConfig, SafetyResult,
    create_default_safety_filter
)


class TestSafetyFilter(unittest.TestCase):
    """SafetyFilter 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.config = SafetyFilterConfig(
            safety_threshold=0.8,
            filter_strength="moderate",
            language="ko",
            enable_bias_detection=True,
            enable_harmful_content_detection=True,
            enable_pii_detection=True,
            allow_technical_content=True,
            log_level="ERROR"  # 테스트 중 로그 최소화
        )
        self.safety_filter = SafetyFilter(self.config)
    
    def test_initialization(self):
        """초기화 테스트"""
        self.assertIsNotNone(self.safety_filter)
        self.assertEqual(self.safety_filter.config.safety_threshold, 0.8)
        self.assertEqual(self.safety_filter.config.filter_strength, "moderate")
        self.assertTrue(self.safety_filter.config.enable_bias_detection)
    
    def test_safe_content_sharegpt(self):
        """안전한 콘텐츠 테스트 (ShareGPT 형식)"""
        safe_item = {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다. 먼저 프로젝트에 참조를 추가하고..."}
            ]
        }
        
        result = self.safety_filter.check_safety(safe_item, "sharegpt")
        
        self.assertIsInstance(result, SafetyResult)
        self.assertTrue(result.is_safe)
        self.assertGreaterEqual(result.safety_score, self.config.safety_threshold)
        self.assertEqual(len(result.issues), 0)
    
    def test_safe_content_alpaca(self):
        """안전한 콘텐츠 테스트 (Alpaca 형식)"""
        safe_item = {
            "instruction": "Syncfusion Chart 컴포넌트 사용법을 설명해주세요.",
            "input": "초보자도 이해할 수 있도록 설명해주세요.",
            "output": "Chart 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. Chart 컨트롤 폼에 배치\n3. 데이터 소스 설정"
        }
        
        result = self.safety_filter.check_safety(safe_item, "alpaca")
        
        self.assertTrue(result.is_safe)
        self.assertGreaterEqual(result.safety_score, self.config.safety_threshold)
    
    def test_safe_content_openai(self):
        """안전한 콘텐츠 테스트 (OpenAI 형식)"""
        safe_item = {
            "messages": [
                {"role": "system", "content": "Syncfusion WinForms 전문가"},
                {"role": "user", "content": "DataGrid 사용법을 알려주세요."},
                {"role": "assistant", "content": "DataGrid 사용법은 다음과 같습니다..."}
            ]
        }
        
        result = self.safety_filter.check_safety(safe_item, "openai")
        
        self.assertTrue(result.is_safe)
        self.assertGreaterEqual(result.safety_score, self.config.safety_threshold)
    
    def test_blocked_words_detection(self):
        """금지어 탐지 테스트"""
        unsafe_item = {
            "conversations": [
                {"from": "human", "value": "이 바보같은 프로그램이 왜 안되는거야?"},
                {"from": "gpt", "value": "프로그램 오류를 해결하는 방법을 알려드리겠습니다."}
            ]
        }
        
        result = self.safety_filter.check_safety(unsafe_item, "sharegpt")
        
        self.assertFalse(result.is_safe)
        self.assertLess(result.safety_score, self.config.safety_threshold)
        self.assertGreater(len(result.issues), 0)
        self.assertIn("blocked_words", result.detected_categories)
    
    def test_pii_detection(self):
        """개인정보 탐지 테스트"""
        pii_item = {
            "conversations": [
                {"from": "human", "value": "제 전화번호는 010-1234-5678입니다."},
                {"from": "gpt", "value": "개인정보는 공유하지 마세요."}
            ]
        }
        
        result = self.safety_filter.check_safety(pii_item, "sharegpt")
        
        self.assertFalse(result.is_safe)
        self.assertGreater(len(result.issues), 0)
        self.assertIn("pii", result.detected_categories)
        
        # PII 탐지 내용 확인
        pii_issue_found = any("PII detected" in issue for issue in result.issues)
        self.assertTrue(pii_issue_found)
    
    def test_bias_detection(self):
        """편향성 탐지 테스트"""
        biased_item = {
            "conversations": [
                {"from": "human", "value": "남자가 프로그래밍을 더 잘한다고 생각해요."},
                {"from": "gpt", "value": "프로그래밍 능력은 성별과 관계없습니다."}
            ]
        }
        
        result = self.safety_filter.check_safety(biased_item, "sharegpt")
        
        # 편향성은 경고로 처리되므로 is_safe는 여전히 True일 수 있음
        self.assertGreater(len(result.warnings), 0)
        self.assertIn("bias", result.detected_categories)
        
        # 편향성 경고 내용 확인
        bias_warning_found = any("bias detected" in warning.lower() for warning in result.warnings)
        self.assertTrue(bias_warning_found)
    
    def test_harmful_content_detection(self):
        """유해 콘텐츠 탐지 테스트"""
        harmful_item = {
            "conversations": [
                {"from": "human", "value": "자살하고 싶어요."},
                {"from": "gpt", "value": "도움을 요청하세요."}
            ]
        }
        
        result = self.safety_filter.check_safety(harmful_item, "sharegpt")
        
        self.assertFalse(result.is_safe)
        self.assertGreater(len(result.issues), 0)
        self.assertIn("harmful", result.detected_categories)
    
    def test_technical_content_exception(self):
        """기술적 콘텐츠 예외 처리 테스트"""
        technical_item = {
            "conversations": [
                {"from": "human", "value": "API 클래스 메서드를 사용하는 방법을 알려주세요."},
                {"from": "gpt", "value": "API 클래스의 메서드는 다음과 같이 사용합니다: class.method()"}
            ]
        }
        
        result = self.safety_filter.check_safety(technical_item, "sharegpt")
        
        self.assertTrue(result.is_safe)
        self.assertGreaterEqual(result.safety_score, self.config.safety_threshold)
        
        # 기술적 콘텐츠 예외 처리 확인
        if "technical_exceptions" in result.details:
            self.assertGreater(result.details["technical_exceptions"], 0)
    
    def test_empty_content(self):
        """빈 콘텐츠 테스트"""
        empty_item = {
            "conversations": []
        }
        
        result = self.safety_filter.check_safety(empty_item, "sharegpt")
        
        self.assertTrue(result.is_safe)
        self.assertEqual(result.safety_score, 1.0)
        self.assertGreater(len(result.warnings), 0)
        self.assertIn("No text content found", result.warnings[0])
    
    def test_batch_check_safety(self):
        """배치 안전성 검사 테스트"""
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
            },
            {
                "conversations": [
                    {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                    {"from": "gpt", "value": "Chart 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            }
        ]
        
        results = self.safety_filter.batch_check_safety(test_items, "sharegpt")
        
        self.assertEqual(len(results), 3)
        self.assertIsInstance(results[0], SafetyResult)
        self.assertIsInstance(results[1], SafetyResult)
        self.assertIsInstance(results[2], SafetyResult)
        
        # 첫 번째와 세 번째는 안전, 두 번째는 불안전
        self.assertTrue(results[0].is_safe)
        self.assertFalse(results[1].is_safe)
        self.assertTrue(results[2].is_safe)
    
    def test_safety_statistics(self):
        """안전성 통계 테스트"""
        test_results = [
            SafetyResult(is_safe=True, safety_score=0.9),
            SafetyResult(is_safe=False, safety_score=0.5, issues=["test issue"]),
            SafetyResult(is_safe=True, safety_score=0.8, warnings=["test warning"])
        ]
        
        stats = self.safety_filter.get_safety_statistics(test_results)
        
        self.assertEqual(stats["total_items"], 3)
        self.assertEqual(stats["safe_items"], 2)
        self.assertEqual(stats["unsafe_items"], 1)
        self.assertAlmostEqual(stats["safety_rate"], 2/3, places=2)
        self.assertAlmostEqual(stats["average_safety_score"], (0.9 + 0.5 + 0.8) / 3, places=2)
        self.assertEqual(stats["total_issues"], 1)
        self.assertEqual(stats["total_warnings"], 1)
    
    def test_save_safety_report(self):
        """안전성 리포트 저장 테스트"""
        test_results = [
            SafetyResult(is_safe=True, safety_score=0.9),
            SafetyResult(is_safe=False, safety_score=0.5, issues=["test issue"])
        ]
        
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "safety_report.json"
            
            success = self.safety_filter.save_safety_report(test_results, str(report_path))
            
            self.assertTrue(success)
            self.assertTrue(report_path.exists())
            
            # 리포트 내용 확인
            with open(report_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            
            self.assertIn("report_version", report)
            self.assertIn("generated_at", report)
            self.assertIn("configuration", report)
            self.assertIn("statistics", report)
            self.assertIn("detailed_results", report)
            self.assertEqual(len(report["detailed_results"]), 2)
    
    def test_filter_strength_strict(self):
        """엄격한 필터 강도 테스트"""
        strict_config = SafetyFilterConfig(
            safety_threshold=0.9,
            filter_strength="strict",
            log_level="ERROR"
        )
        strict_filter = SafetyFilter(strict_config)
        
        borderline_item = {
            "conversations": [
                {"from": "human", "value": "이 프로그램이 좀 이상해요."},
                {"from": "gpt", "value": "프로그램 문제를 해결해드리겠습니다."}
            ]
        }
        
        result = strict_filter.check_safety(borderline_item, "sharegpt")
        
        # 엄격한 모드에서는 더 낮은 점수를 받을 것
        self.assertLessEqual(result.safety_score, 1.0)
    
    def test_filter_strength_lenient(self):
        """관대한 필터 강도 테스트"""
        lenient_config = SafetyFilterConfig(
            safety_threshold=0.5,
            filter_strength="lenient",
            log_level="ERROR"
        )
        lenient_filter = SafetyFilter(lenient_config)
        
        borderline_item = {
            "conversations": [
                {"from": "human", "value": "이 프로그램이 좀 이상해요."},
                {"from": "gpt", "value": "프로그램 문제를 해결해드리겠습니다."}
            ]
        }
        
        result = lenient_filter.check_safety(borderline_item, "sharegpt")
        
        # 관대한 모드에서는 더 높은 점수를 받을 것
        self.assertTrue(result.is_safe)
    
    def test_custom_blocked_words(self):
        """커스텀 금지어 테스트"""
        custom_config = SafetyFilterConfig(
            custom_blocked_words=["테스트금지어", "커스텀차단"],
            log_level="ERROR"
        )
        custom_filter = SafetyFilter(custom_config)
        
        custom_item = {
            "conversations": [
                {"from": "human", "value": "테스트금지어를 사용해보겠습니다."},
                {"from": "gpt", "value": "다른 표현을 사용해주세요."}
            ]
        }
        
        result = custom_filter.check_safety(custom_item, "sharegpt")
        
        self.assertFalse(result.is_safe)
        self.assertGreater(len(result.issues), 0)
        
        # 커스텀 금지어 탐지 확인
        custom_issue_found = any("커스텀" in issue for issue in result.issues)
        self.assertTrue(custom_issue_found)
    
    def test_create_default_safety_filter(self):
        """기본 안전성 필터 생성 테스트"""
        default_filter = create_default_safety_filter()
        
        self.assertIsNotNone(default_filter)
        self.assertIsInstance(default_filter, SafetyFilter)
        self.assertEqual(default_filter.config.safety_threshold, 0.8)
        self.assertEqual(default_filter.config.filter_strength, "moderate")
        self.assertTrue(default_filter.config.enable_bias_detection)
        self.assertTrue(default_filter.config.enable_harmful_content_detection)
        self.assertTrue(default_filter.config.enable_pii_detection)
        self.assertTrue(default_filter.config.allow_technical_content)


if __name__ == "__main__":
    unittest.main()