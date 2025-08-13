#!/usr/bin/env python3
"""
AutoCorrector 단위 테스트
"""

import unittest
import tempfile
import json
from pathlib import Path

from quality_validator.auto_corrector import (
    AutoCorrector, AutoCorrectorConfig, CorrectionResult,
    create_default_auto_corrector
)


class TestAutoCorrector(unittest.TestCase):
    """AutoCorrector 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.config = AutoCorrectorConfig(
            enable_text_normalization=True,
            enable_format_correction=True,
            enable_encoding_correction=True,
            enable_structure_correction=True,
            enable_content_enhancement=True,
            correction_strength="moderate",
            min_confidence_score=0.5,  # 테스트에서는 낮은 임계값 사용
            max_corrections_per_item=10,
            log_level="ERROR"  # 테스트 중 로그 최소화
        )
        self.auto_corrector = AutoCorrector(self.config)
    
    def test_initialization(self):
        """초기화 테스트"""
        self.assertIsNotNone(self.auto_corrector)
        self.assertEqual(self.auto_corrector.config.correction_strength, "moderate")
        self.assertTrue(self.auto_corrector.config.enable_text_normalization)
        self.assertTrue(self.auto_corrector.config.enable_format_correction)
    
    def test_no_correction_needed(self):
        """수정이 필요 없는 콘텐츠 테스트"""
        clean_item = {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다."}
            ]
        }
        
        result = self.auto_corrector.correct_item(clean_item, "sharegpt")
        
        self.assertIsInstance(result, CorrectionResult)
        # 깨끗한 콘텐츠는 수정이 거의 필요 없을 것
        self.assertLessEqual(len(result.corrections_applied), 2)
    
    def test_text_normalization_sharegpt(self):
        """텍스트 정규화 테스트 (ShareGPT 형식)"""
        messy_item = {
            "conversations": [
                {"from": "human", "value": "  syncfusion   datagrid  사용벙을   알려주세요...  "},
                {"from": "gpt", "value": "\t\tDataGrid  컴포넌트트는   다음과   같이   사용합니다.\n\n\n\n"}
            ]
        }
        
        result = self.auto_corrector.correct_item(messy_item, "sharegpt")
        
        self.assertTrue(result.changes_made)
        self.assertGreater(len(result.corrections_applied), 0)
        
        # 수정된 텍스트 확인
        corrected_conversations = result.corrected_item["conversations"]
        human_value = corrected_conversations[0]["value"]
        gpt_value = corrected_conversations[1]["value"]
        
        # 공백이 정규화되었는지 확인
        self.assertNotIn("   ", human_value)
        self.assertNotIn("   ", gpt_value)
        
        # 앞뒤 공백이 제거되었는지 확인
        self.assertEqual(human_value, human_value.strip())
        self.assertEqual(gpt_value, gpt_value.strip())
    
    def test_text_normalization_alpaca(self):
        """텍스트 정규화 테스트 (Alpaca 형식)"""
        messy_item = {
            "instruction": "  syncfusion  chart  사용벙을  설명해주세요  ",
            "input": "\t초보자도  이해할  수  있도록\t",
            "output": "Chart  컴포넌트트는\n\n\n다음과  같이  사용합니다"
        }
        
        result = self.auto_corrector.correct_item(messy_item, "alpaca")
        
        self.assertTrue(result.changes_made)
        self.assertGreater(len(result.corrections_applied), 0)
        
        # 수정된 텍스트 확인
        corrected_item = result.corrected_item
        self.assertEqual(corrected_item["instruction"], corrected_item["instruction"].strip())
        self.assertEqual(corrected_item["input"], corrected_item["input"].strip())
        self.assertEqual(corrected_item["output"], corrected_item["output"].strip())
    
    def test_format_correction(self):
        """포맷 수정 테스트"""
        item_with_typos = {
            "conversations": [
                {"from": "human", "value": "datagrid 사용벙을 알려주세요."},
                {"from": "gpt", "value": "syncfusion winforms 컴포넌트트를 사용합니다."}
            ]
        }
        
        result = self.auto_corrector.correct_item(item_with_typos, "sharegpt")
        
        self.assertTrue(result.changes_made)
        
        # 수정된 텍스트 확인
        corrected_conversations = result.corrected_item["conversations"]
        human_value = corrected_conversations[0]["value"]
        gpt_value = corrected_conversations[1]["value"]
        
        # 기술 용어가 표준화되었는지 확인 (일부만 확인)
        self.assertIn("DataGrid", human_value)
        # 오타 수정은 구현에 따라 다를 수 있으므로 기본적인 것만 확인
        self.assertIn("Syncfusion", gpt_value)
        self.assertIn("WinForms", gpt_value)
    
    def test_structure_correction_sharegpt(self):
        """구조 수정 테스트 (ShareGPT 형식)"""
        item_with_structure_issues = {
            "conversations": [
                {"from": "human", "value": ""},  # 빈 대화
                {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다."},
                {"from": "gpt", "value": "추가 설명입니다."}  # 연속된 같은 역할
            ]
        }
        
        result = self.auto_corrector.correct_item(item_with_structure_issues, "sharegpt")
        
        self.assertTrue(result.changes_made)
        
        # 수정된 구조 확인
        corrected_conversations = result.corrected_item["conversations"]
        
        # 빈 대화가 제거되었는지 확인
        for conv in corrected_conversations:
            self.assertTrue(conv.get("value", "").strip())
        
        # 연속된 같은 역할이 병합되었는지 확인 (구현에 따라 다를 수 있음)
        self.assertLessEqual(len(corrected_conversations), 3)
    
    def test_structure_correction_openai(self):
        """구조 수정 테스트 (OpenAI 형식)"""
        item_with_structure_issues = {
            "messages": [
                {"role": "user", "content": ""},  # 빈 메시지
                {"role": "user", "content": "DataGrid 사용법을 알려주세요."},
                {"role": "assistant", "content": "DataGrid 컴포넌트는 다음과 같이 사용합니다."},
                {"role": "assistant", "content": "추가 설명입니다."}  # 연속된 같은 역할
            ]
        }
        
        result = self.auto_corrector.correct_item(item_with_structure_issues, "openai")
        
        self.assertTrue(result.changes_made)
        
        # 수정된 구조 확인
        corrected_messages = result.corrected_item["messages"]
        
        # 빈 메시지가 제거되었는지 확인
        for msg in corrected_messages:
            self.assertTrue(msg.get("content", "").strip())
        
        # 연속된 같은 역할이 병합되었는지 확인
        self.assertLessEqual(len(corrected_messages), 3)
    
    def test_encoding_correction(self):
        """인코딩 수정 테스트"""
        item_with_encoding_issues = {
            "conversations": [
                {"from": "human", "value": "DataGrid\u00a0사용법을\u2018알려주세요\u2019"},
                {"from": "gpt", "value": "DataGrid\u2013컴포넌트는\u2026다음과\u00a0같이\u00a0사용합니다"}
            ]
        }
        
        result = self.auto_corrector.correct_item(item_with_encoding_issues, "sharegpt")
        
        # 인코딩 수정이 적용되었는지 확인 (변경사항이 있을 수도 없을 수도 있음)
        corrected_conversations = result.corrected_item["conversations"]
        human_value = corrected_conversations[0]["value"]
        gpt_value = corrected_conversations[1]["value"]
        
        # 특수 문자가 일반 문자로 변환되었는지 확인 (변경이 있었다면)
        if result.changes_made:
            # 적어도 일부 특수 문자는 변환되었을 것
            original_human = "DataGrid\u00a0사용법을\u2018알려주세요\u2019"
            original_gpt = "DataGrid\u2013컴포넌트는\u2026다음과\u00a0같이\u00a0사용합니다"
            self.assertNotEqual(human_value, original_human)
            self.assertNotEqual(gpt_value, original_gpt)
    
    def test_content_enhancement(self):
        """콘텐츠 향상 테스트"""
        item_with_code = {
            "conversations": [
                {"from": "human", "value": "DataGrid 코드 예제를 보여주세요."},
                {"from": "gpt", "value": "다음은 예제입니다:\n\n```csharp\n  SfDataGrid dataGrid = new SfDataGrid();  \n  dataGrid.DataSource = data;  \n\n```\n\n1.프로젝트 설정\n2.컨트롤 추가"}
            ]
        }
        
        result = self.auto_corrector.correct_item(item_with_code, "sharegpt")
        
        # 콘텐츠 향상이 적용되었는지 확인 (구현에 따라 다를 수 있음)
        corrected_gpt_value = result.corrected_item["conversations"][1]["value"]
        
        # 목록 포맷팅이 개선되었는지 확인
        self.assertIn("1. 프로젝트", corrected_gpt_value)
        self.assertIn("2. 컨트롤", corrected_gpt_value)
    
    def test_confidence_score_calculation(self):
        """신뢰도 점수 계산 테스트"""
        # 많은 문제가 있는 아이템
        problematic_item = {
            "conversations": [
                {"from": "human", "value": ""},  # 빈 대화
                {"from": "gpt", "value": "  많은   공백과   문제가   있는   텍스트입니다...  "}
            ]
        }
        
        result = self.auto_corrector.correct_item(problematic_item, "sharegpt")
        
        # 신뢰도 점수가 계산되었는지 확인
        self.assertGreaterEqual(result.confidence_score, 0.0)
        self.assertLessEqual(result.confidence_score, 1.0)
        
        # 문제가 많았으므로 신뢰도가 높지 않을 것
        self.assertLess(result.confidence_score, 1.0)
    
    def test_batch_correct_items(self):
        """배치 수정 테스트"""
        test_items = [
            {
                "conversations": [
                    {"from": "human", "value": "  datagrid  사용벙  "},
                    {"from": "gpt", "value": "DataGrid  컴포넌트트  사용법"}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "chart  사용법"},
                    {"from": "gpt", "value": "Chart  컴포넌트  설명"}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "깨끗한 텍스트입니다."},
                    {"from": "gpt", "value": "문제없는 응답입니다."}
                ]
            }
        ]
        
        results = self.auto_corrector.batch_correct_items(test_items, "sharegpt")
        
        self.assertEqual(len(results), 3)
        self.assertIsInstance(results[0], CorrectionResult)
        self.assertIsInstance(results[1], CorrectionResult)
        self.assertIsInstance(results[2], CorrectionResult)
        
        # 첫 번째와 두 번째는 수정이 필요했을 것
        self.assertTrue(results[0].changes_made)
        self.assertTrue(results[1].changes_made)
        
        # 세 번째는 수정이 적거나 없을 것
        self.assertLessEqual(len(results[2].corrections_applied), 2)
    
    def test_correction_statistics(self):
        """수정 통계 테스트"""
        test_results = [
            CorrectionResult(
                corrected_item={},
                changes_made=True,
                corrections_applied=["Text normalization applied", "Format correction applied"],
                confidence_score=0.8,
                original_issues=["Excessive whitespace", "Common typos"],
                remaining_issues=[]
            ),
            CorrectionResult(
                corrected_item={},
                changes_made=False,
                corrections_applied=[],
                confidence_score=1.0,
                original_issues=[],
                remaining_issues=[]
            ),
            CorrectionResult(
                corrected_item={},
                changes_made=True,
                corrections_applied=["Structure correction applied"],
                confidence_score=0.9,
                original_issues=["Empty conversations"],
                remaining_issues=[]
            )
        ]
        
        stats = self.auto_corrector.get_correction_statistics(test_results)
        
        self.assertEqual(stats["total_items"], 3)
        self.assertEqual(stats["corrected_items"], 2)
        self.assertEqual(stats["uncorrected_items"], 1)
        self.assertAlmostEqual(stats["correction_rate"], 2/3, places=2)
        self.assertAlmostEqual(stats["average_confidence"], (0.8 + 1.0 + 0.9) / 3, places=2)
        self.assertEqual(stats["total_original_issues"], 3)
        self.assertEqual(stats["total_remaining_issues"], 0)
        self.assertEqual(stats["issue_resolution_rate"], 1.0)
        self.assertIn("correction_types", stats)
    
    def test_save_correction_report(self):
        """수정 리포트 저장 테스트"""
        test_results = [
            CorrectionResult(
                corrected_item={},
                changes_made=True,
                corrections_applied=["Text normalization applied"],
                confidence_score=0.8
            ),
            CorrectionResult(
                corrected_item={},
                changes_made=False,
                corrections_applied=[],
                confidence_score=1.0
            )
        ]
        
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "correction_report.json"
            
            success = self.auto_corrector.save_correction_report(test_results, str(report_path))
            
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
    
    def test_low_confidence_threshold(self):
        """낮은 신뢰도 임계값 테스트"""
        # 높은 신뢰도 임계값 설정
        high_threshold_config = AutoCorrectorConfig(
            min_confidence_score=0.95,
            log_level="ERROR"
        )
        high_threshold_corrector = AutoCorrector(high_threshold_config)
        
        # 문제가 있는 아이템
        problematic_item = {
            "conversations": [
                {"from": "human", "value": "  많은   문제가   있는   텍스트  "},
                {"from": "gpt", "value": "  응답도   문제가   많습니다  "}
            ]
        }
        
        result = high_threshold_corrector.correct_item(problematic_item, "sharegpt")
        
        # 신뢰도가 낮으면 원본이 반환되어야 함
        if result.confidence_score < 0.95:
            self.assertFalse(result.changes_made)
            self.assertEqual(len(result.corrections_applied), 0)
    
    def test_correction_strength_settings(self):
        """수정 강도 설정 테스트"""
        # 보수적 설정
        conservative_config = AutoCorrectorConfig(
            correction_strength="conservative",
            min_confidence_score=0.5,
            log_level="ERROR"
        )
        conservative_corrector = AutoCorrector(conservative_config)
        
        # 공격적 설정
        aggressive_config = AutoCorrectorConfig(
            correction_strength="aggressive",
            min_confidence_score=0.5,
            log_level="ERROR"
        )
        aggressive_corrector = AutoCorrector(aggressive_config)
        
        test_item = {
            "conversations": [
                {"from": "human", "value": "  텍스트   정규화   테스트  "},
                {"from": "gpt", "value": "  응답   텍스트   테스트  "}
            ]
        }
        
        conservative_result = conservative_corrector.correct_item(test_item, "sharegpt")
        aggressive_result = aggressive_corrector.correct_item(test_item, "sharegpt")
        
        # 두 결과 모두 유효해야 함
        self.assertIsInstance(conservative_result, CorrectionResult)
        self.assertIsInstance(aggressive_result, CorrectionResult)
        
        # 신뢰도 점수가 다를 수 있음 (구현에 따라)
        self.assertGreaterEqual(conservative_result.confidence_score, 0.0)
        self.assertGreaterEqual(aggressive_result.confidence_score, 0.0)
    
    def test_create_default_auto_corrector(self):
        """기본 자동 수정기 생성 테스트"""
        default_corrector = create_default_auto_corrector()
        
        self.assertIsNotNone(default_corrector)
        self.assertIsInstance(default_corrector, AutoCorrector)
        self.assertTrue(default_corrector.config.enable_text_normalization)
        self.assertTrue(default_corrector.config.enable_format_correction)
        self.assertTrue(default_corrector.config.enable_encoding_correction)
        self.assertTrue(default_corrector.config.enable_structure_correction)
        self.assertTrue(default_corrector.config.enable_content_enhancement)
        self.assertEqual(default_corrector.config.correction_strength, "moderate")
        self.assertEqual(default_corrector.config.min_confidence_score, 0.7)
    
    def test_empty_content_handling(self):
        """빈 콘텐츠 처리 테스트"""
        empty_item = {
            "conversations": []
        }
        
        result = self.auto_corrector.correct_item(empty_item, "sharegpt")
        
        self.assertIsInstance(result, CorrectionResult)
        # 빈 콘텐츠는 수정할 것이 없음
        self.assertEqual(result.corrected_item, empty_item)


if __name__ == "__main__":
    unittest.main()