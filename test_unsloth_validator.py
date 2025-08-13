#!/usr/bin/env python3
"""
Unsloth 호환성 검증기 단위 테스트
"""

import unittest
from unsloth_dataset.validator import UnslothValidator, ValidationResult


class TestUnslothValidator(unittest.TestCase):
    """Unsloth 검증기 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.validator = UnslothValidator()
        
        # 테스트 데이터
        self.valid_sharegpt_data = [
            {
                "conversations": [
                    {"from": "system", "value": "Syncfusion WinForms 전문가입니다."},
                    {"from": "human", "value": "DataGrid 사용법을 알려주세요.</s>"},
                    {"from": "gpt", "value": "DataGrid 컴포넌트 사용법은 다음과 같습니다...</s>"}
                ]
            }
        ]
        
        self.valid_alpaca_data = [
            {
                "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.</s>",
                "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치</s>",
                "input": "초보자도 이해할 수 있도록 단계별로 설명해주세요.</s>"
            }
        ]
        
        self.valid_openai_data = [
            {
                "messages": [
                    {"role": "system", "content": "Syncfusion WinForms 전문가입니다."},
                    {"role": "user", "content": "DataGrid 사용법을 알려주세요.</s>"},
                    {"role": "assistant", "content": "DataGrid 컴포넌트 사용법은 다음과 같습니다...</s>"}
                ]
            }
        ]
    
    def test_validation_result_basic(self):
        """ValidationResult 기본 기능 테스트"""
        result = ValidationResult()
        
        # 초기 상태 확인
        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.issues), 0)
        self.assertEqual(len(result.warnings), 0)
        self.assertEqual(len(result.recommendations), 0)
        
        # 이슈 추가
        result.add_issue("테스트 이슈")
        self.assertFalse(result.is_valid)
        self.assertEqual(len(result.issues), 1)
        self.assertIn("테스트 이슈", result.issues)
        
        # 경고 추가
        result.add_warning("테스트 경고")
        self.assertEqual(len(result.warnings), 1)
        self.assertIn("테스트 경고", result.warnings)
        
        # 권장사항 추가
        result.add_recommendation("테스트 권장사항")
        self.assertEqual(len(result.recommendations), 1)
        self.assertIn("테스트 권장사항", result.recommendations)
        
        # 딕셔너리 변환
        result_dict = result.to_dict()
        self.assertIn("is_valid", result_dict)
        self.assertIn("issues", result_dict)
        self.assertIn("warnings", result_dict)
        self.assertIn("recommendations", result_dict)
    
    def test_validate_sharegpt_format_valid(self):
        """유효한 ShareGPT 포맷 검증 테스트"""
        result = self.validator.validate_dataset_format("sharegpt", self.valid_sharegpt_data)
        
        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.issues), 0)
        self.assertIn("total_items", result.statistics)
        self.assertEqual(result.statistics["format_type"], "sharegpt")
    
    def test_validate_sharegpt_format_invalid(self):
        """잘못된 ShareGPT 포맷 검증 테스트"""
        # conversations 필드 누락
        invalid_data1 = [{"metadata": {"format": "sharegpt"}}]
        result1 = self.validator.validate_dataset_format("sharegpt", invalid_data1)
        self.assertFalse(result1.is_valid)
        self.assertGreater(len(result1.issues), 0)
        
        # 잘못된 역할
        invalid_data2 = [{
            "conversations": [
                {"from": "invalid_role", "value": "테스트 메시지"}
            ]
        }]
        result2 = self.validator.validate_dataset_format("sharegpt", invalid_data2)
        self.assertFalse(result2.is_valid)
        
        # 필수 필드 누락
        invalid_data3 = [{
            "conversations": [
                {"from": "human"}  # value 누락
            ]
        }]
        result3 = self.validator.validate_dataset_format("sharegpt", invalid_data3)
        self.assertFalse(result3.is_valid)
    
    def test_validate_alpaca_format_valid(self):
        """유효한 Alpaca 포맷 검증 테스트"""
        result = self.validator.validate_dataset_format("alpaca", self.valid_alpaca_data)
        
        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.issues), 0)
        self.assertIn("total_items", result.statistics)
        self.assertEqual(result.statistics["format_type"], "alpaca")
    
    def test_validate_alpaca_format_invalid(self):
        """잘못된 Alpaca 포맷 검증 테스트"""
        # instruction 필드 누락
        invalid_data1 = [{"output": "응답만 있음"}]
        result1 = self.validator.validate_dataset_format("alpaca", invalid_data1)
        self.assertFalse(result1.is_valid)
        self.assertGreater(len(result1.issues), 0)
        
        # output 필드 누락
        invalid_data2 = [{"instruction": "지시문만 있음"}]
        result2 = self.validator.validate_dataset_format("alpaca", invalid_data2)
        self.assertFalse(result2.is_valid)
        
        # 빈 필드
        invalid_data3 = [{"instruction": "", "output": ""}]
        result3 = self.validator.validate_dataset_format("alpaca", invalid_data3)
        self.assertFalse(result3.is_valid)
    
    def test_validate_openai_format_valid(self):
        """유효한 OpenAI 포맷 검증 테스트"""
        result = self.validator.validate_dataset_format("openai", self.valid_openai_data)
        
        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.issues), 0)
        self.assertIn("total_items", result.statistics)
        self.assertEqual(result.statistics["format_type"], "openai")
    
    def test_validate_openai_format_invalid(self):
        """잘못된 OpenAI 포맷 검증 테스트"""
        # messages 필드 누락
        invalid_data1 = [{"metadata": {"format": "openai"}}]
        result1 = self.validator.validate_dataset_format("openai", invalid_data1)
        self.assertFalse(result1.is_valid)
        self.assertGreater(len(result1.issues), 0)
        
        # 잘못된 역할
        invalid_data2 = [{
            "messages": [
                {"role": "invalid_role", "content": "테스트 메시지"}
            ]
        }]
        result2 = self.validator.validate_dataset_format("openai", invalid_data2)
        self.assertFalse(result2.is_valid)
        
        # 메시지 수 부족
        invalid_data3 = [{
            "messages": [
                {"role": "user", "content": "메시지 하나만"}
            ]
        }]
        result3 = self.validator.validate_dataset_format("openai", invalid_data3)
        self.assertFalse(result3.is_valid)
    
    def test_validate_message_order(self):
        """메시지 순서 검증 테스트"""
        # 올바른 순서
        valid_order_data = [{
            "messages": [
                {"role": "system", "content": "시스템 메시지"},
                {"role": "user", "content": "사용자 메시지"},
                {"role": "assistant", "content": "어시스턴트 메시지"}
            ]
        }]
        result1 = self.validator.validate_dataset_format("openai", valid_order_data)
        self.assertTrue(result1.is_valid)
        
        # 잘못된 순서
        invalid_order_data = [{
            "messages": [
                {"role": "user", "content": "사용자 메시지"},
                {"role": "user", "content": "사용자 메시지 연속"}  # 잘못된 순서
            ]
        }]
        result2 = self.validator.validate_dataset_format("openai", invalid_order_data)
        self.assertFalse(result2.is_valid)
    
    def test_validate_token_ranges(self):
        """토큰 범위 검증 테스트"""
        # 정상 범위
        result1 = self.validator.validate_token_ranges(self.valid_alpaca_data, 10, 1000)
        self.assertTrue(result1.is_valid)
        
        # 최소 토큰 수 미달
        result2 = self.validator.validate_token_ranges(self.valid_alpaca_data, 1000, 2000)
        self.assertFalse(result2.is_valid)
        self.assertGreater(len(result2.issues), 0)
        
        # 최대 토큰 수 초과
        result3 = self.validator.validate_token_ranges(self.valid_alpaca_data, 1, 10)
        self.assertFalse(result3.is_valid)
        self.assertGreater(len(result3.issues), 0)
    
    def test_validate_unsloth_compatibility(self):
        """Unsloth 호환성 검증 테스트"""
        datasets = {
            "sharegpt": self.valid_sharegpt_data,
            "alpaca": self.valid_alpaca_data,
            "openai": self.valid_openai_data
        }
        
        results = self.validator.validate_unsloth_compatibility(datasets)
        
        # 모든 포맷에 대한 결과 확인
        self.assertEqual(len(results), 3)
        self.assertIn("sharegpt", results)
        self.assertIn("alpaca", results)
        self.assertIn("openai", results)
        
        # 각 결과가 ValidationResult 인스턴스인지 확인
        for format_type, result in results.items():
            self.assertIsInstance(result, ValidationResult)
    
    def test_eos_token_validation(self):
        """EOS 토큰 검증 테스트"""
        # EOS 토큰이 없는 데이터
        no_eos_sharegpt = [{
            "conversations": [
                {"from": "human", "value": "EOS 토큰 없음"},
                {"from": "gpt", "value": "EOS 토큰 없음"}
            ]
        }]
        
        result = self.validator.validate_dataset_format("sharegpt", no_eos_sharegpt)
        # EOS 토큰 누락은 경고로 처리되므로 is_valid는 True일 수 있음
        # 하지만 경고가 있어야 함
        unsloth_result = self.validator._validate_unsloth_specific("sharegpt", no_eos_sharegpt)
        self.assertGreater(len(unsloth_result.warnings), 0)
    
    def test_content_quality_validation(self):
        """콘텐츠 품질 검증 테스트"""
        # 너무 짧은 내용
        short_content_data = [{
            "conversations": [
                {"from": "human", "value": "짧음</s>"},
                {"from": "gpt", "value": "짧음</s>"}
            ]
        }]
        
        unsloth_result = self.validator._validate_unsloth_specific("sharegpt", short_content_data)
        self.assertGreater(len(unsloth_result.warnings), 0)
        
        # 반복적인 내용 (10단어 이상으로 구성)
        repetitive_data = [{
            "instruction": "반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복</s>",
            "output": "반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복 반복</s>"
        }]
        
        unsloth_result2 = self.validator._validate_unsloth_specific("alpaca", repetitive_data)
        self.assertGreater(len(unsloth_result2.warnings), 0)
    
    def test_unsupported_format(self):
        """지원하지 않는 포맷 테스트"""
        # 빈 데이터가 아닌 더미 데이터로 테스트
        dummy_data = [{"test": "data"}]
        result = self.validator.validate_dataset_format("unsupported_format", dummy_data)
        self.assertFalse(result.is_valid)
        self.assertGreater(len(result.issues), 0)
        self.assertIn("지원하지 않는 포맷", result.issues[0])
    
    def test_empty_data(self):
        """빈 데이터 테스트"""
        result = self.validator.validate_dataset_format("sharegpt", [])
        self.assertFalse(result.is_valid)
        self.assertGreater(len(result.issues), 0)
        self.assertIn("데이터가 비어있습니다", result.issues[0])
    
    def test_validation_statistics(self):
        """검증 통계 생성 테스트"""
        # ShareGPT 통계
        result_sharegpt = self.validator.validate_dataset_format("sharegpt", self.valid_sharegpt_data)
        stats = result_sharegpt.statistics
        self.assertIn("total_items", stats)
        self.assertIn("average_turns_per_conversation", stats)
        self.assertEqual(stats["format_type"], "sharegpt")
        
        # Alpaca 통계
        result_alpaca = self.validator.validate_dataset_format("alpaca", self.valid_alpaca_data)
        stats = result_alpaca.statistics
        self.assertIn("average_instruction_length", stats)
        self.assertIn("average_output_length", stats)
        self.assertEqual(stats["format_type"], "alpaca")
        
        # OpenAI 통계
        result_openai = self.validator.validate_dataset_format("openai", self.valid_openai_data)
        stats = result_openai.statistics
        self.assertIn("average_messages_per_item", stats)
        self.assertEqual(stats["format_type"], "openai")
    
    def test_validation_summary(self):
        """검증 요약 생성 테스트"""
        datasets = {
            "sharegpt": self.valid_sharegpt_data,
            "alpaca": self.valid_alpaca_data,
            "openai": self.valid_openai_data
        }
        
        results = self.validator.validate_unsloth_compatibility(datasets)
        summary = self.validator.get_validation_summary(results)
        
        # 요약 구조 확인
        self.assertIn("total_formats", summary)
        self.assertIn("valid_formats", summary)
        self.assertIn("invalid_formats", summary)
        self.assertIn("total_issues", summary)
        self.assertIn("total_warnings", summary)
        self.assertIn("total_recommendations", summary)
        self.assertIn("format_details", summary)
        
        # 값 확인
        self.assertEqual(summary["total_formats"], 3)
        self.assertEqual(len(summary["format_details"]), 3)
        
        # 각 포맷 세부사항 확인
        for format_type in ["sharegpt", "alpaca", "openai"]:
            self.assertIn(format_type, summary["format_details"])
            detail = summary["format_details"][format_type]
            self.assertIn("is_valid", detail)
            self.assertIn("issues_count", detail)
            self.assertIn("warnings_count", detail)
            self.assertIn("recommendations_count", detail)
    
    def test_merge_validation_results(self):
        """검증 결과 병합 테스트"""
        result1 = ValidationResult()
        result1.add_issue("첫 번째 이슈")
        result1.add_warning("첫 번째 경고")
        
        result2 = ValidationResult()
        result2.add_issue("두 번째 이슈")
        result2.add_recommendation("첫 번째 권장사항")
        
        merged = self.validator._merge_validation_results(result1, result2)
        
        # 병합 결과 확인
        self.assertFalse(merged.is_valid)  # 이슈가 있으므로 False
        self.assertEqual(len(merged.issues), 2)
        self.assertEqual(len(merged.warnings), 1)
        self.assertEqual(len(merged.recommendations), 1)
        
        self.assertIn("첫 번째 이슈", merged.issues)
        self.assertIn("두 번째 이슈", merged.issues)
        self.assertIn("첫 번째 경고", merged.warnings)
        self.assertIn("첫 번째 권장사항", merged.recommendations)
    
    def test_token_calculation(self):
        """토큰 계산 테스트"""
        # ShareGPT 토큰 계산
        sharegpt_item = self.valid_sharegpt_data[0]
        tokens = self.validator._calculate_token_count(sharegpt_item)
        self.assertGreater(tokens, 0)
        
        # Alpaca 토큰 계산
        alpaca_item = self.valid_alpaca_data[0]
        tokens = self.validator._calculate_token_count(alpaca_item)
        self.assertGreater(tokens, 0)
        
        # OpenAI 토큰 계산
        openai_item = self.valid_openai_data[0]
        tokens = self.validator._calculate_token_count(openai_item)
        self.assertGreater(tokens, 0)
    
    def test_format_rules_access(self):
        """포맷 규칙 접근 테스트"""
        # 지원하는 모든 포맷에 대한 규칙이 있는지 확인
        supported_formats = ["sharegpt", "alpaca", "openai"]
        
        for format_type in supported_formats:
            self.assertIn(format_type, self.validator.format_rules)
            rules = self.validator.format_rules[format_type]
            self.assertIn("required_fields", rules)
            
            if format_type == "sharegpt":
                self.assertIn("conversation_structure", rules)
            elif format_type == "openai":
                self.assertIn("message_structure", rules)
    
    def test_auto_correct_sharegpt_item(self):
        """ShareGPT 아이템 자동 수정 테스트"""
        # EOS 토큰 누락 데이터
        no_eos_data = [{
            "conversations": [
                {"from": "human", "value": "EOS 토큰 없음"},
                {"from": "gpt", "value": "EOS 토큰 없음"}
            ]
        }]
        
        corrected_data, result = self.validator.auto_correct_dataset("sharegpt", no_eos_data)
        
        self.assertEqual(len(corrected_data), 1)
        self.assertGreater(len(result.warnings), 0)
        
        # EOS 토큰이 추가되었는지 확인
        conversations = corrected_data[0]["conversations"]
        for conv in conversations:
            if conv["from"] in ["human", "gpt"]:
                self.assertTrue(conv["value"].endswith("</s>"))
    
    def test_auto_correct_alpaca_item(self):
        """Alpaca 아이템 자동 수정 테스트"""
        # EOS 토큰 누락 데이터
        no_eos_data = [{
            "instruction": "EOS 토큰 없는 지시문",
            "output": "EOS 토큰 없는 응답",
            "input": "EOS 토큰 없는 입력"
        }]
        
        corrected_data, result = self.validator.auto_correct_dataset("alpaca", no_eos_data)
        
        self.assertEqual(len(corrected_data), 1)
        self.assertGreater(len(result.warnings), 0)
        
        # EOS 토큰이 추가되었는지 확인
        item = corrected_data[0]
        for field in ["instruction", "output", "input"]:
            if field in item and item[field]:
                self.assertTrue(item[field].endswith("</s>"))
    
    def test_auto_correct_openai_item(self):
        """OpenAI 아이템 자동 수정 테스트"""
        # 역할 수정 및 EOS 토큰 추가 테스트
        incorrect_data = [{
            "messages": [
                {"role": "human", "content": "사용자 메시지"},  # human -> user
                {"role": "gpt", "content": "GPT 응답"}        # gpt -> assistant
            ]
        }]
        
        corrected_data, result = self.validator.auto_correct_dataset("openai", incorrect_data)
        
        self.assertEqual(len(corrected_data), 1)
        self.assertGreater(len(result.warnings), 0)
        
        # 역할이 수정되었는지 확인
        messages = corrected_data[0]["messages"]
        self.assertEqual(messages[0]["role"], "user")
        self.assertEqual(messages[1]["role"], "assistant")
        
        # EOS 토큰이 추가되었는지 확인
        for msg in messages:
            if msg["role"] in ["user", "assistant"]:
                self.assertTrue(msg["content"].endswith("</s>"))
    
    def test_auto_correct_invalid_data(self):
        """수정 불가능한 데이터 테스트"""
        # 필수 필드 누락
        invalid_data = [{"metadata": "only"}]
        
        corrected_data, result = self.validator.auto_correct_dataset("sharegpt", invalid_data)
        
        # 수정 불가능한 데이터는 제거됨
        self.assertEqual(len(corrected_data), 0)
        self.assertGreater(len(result.issues), 0)
    
    def test_auto_correct_disabled(self):
        """자동 수정 비활성화 테스트"""
        validator_no_correction = UnslothValidator(enable_auto_correction=False)
        
        no_eos_data = [{
            "conversations": [
                {"from": "human", "value": "EOS 토큰 없음"},
                {"from": "gpt", "value": "EOS 토큰 없음"}
            ]
        }]
        
        corrected_data, result = validator_no_correction.auto_correct_dataset("sharegpt", no_eos_data)
        
        # 자동 수정이 비활성화되어 있으므로 원본 데이터 반환
        self.assertEqual(corrected_data, no_eos_data)
        self.assertEqual(len(result.issues), 0)
        self.assertEqual(len(result.warnings), 0)
    
    def test_validate_and_correct_dataset(self):
        """검증 및 자동 수정 통합 테스트"""
        # 수정이 필요한 데이터
        data_to_correct = [{
            "conversations": [
                {"from": "human", "value": "EOS 토큰 없음"},
                {"from": "gpt", "value": "EOS 토큰 없음"}
            ]
        }]
        
        corrected_data, result = self.validator.validate_and_correct_dataset("sharegpt", data_to_correct)
        
        # 수정된 데이터가 유효한지 확인
        self.assertEqual(len(corrected_data), 1)
        self.assertTrue(result.is_valid or len(result.issues) == 0)  # 수정 후 유효해야 함
        
        # 수정된 데이터 검증
        final_validation = self.validator.validate_dataset_format("sharegpt", corrected_data)
        self.assertTrue(final_validation.is_valid)
    
    def test_length_truncation(self):
        """길이 제한으로 인한 잘림 테스트"""
        # 매우 긴 텍스트
        very_long_text = "매우 긴 텍스트입니다. " * 1000  # 매우 긴 텍스트 생성
        
        long_data = [{
            "instruction": very_long_text,
            "output": very_long_text
        }]
        
        corrected_data, result = self.validator.auto_correct_dataset("alpaca", long_data)
        
        self.assertEqual(len(corrected_data), 1)
        self.assertGreater(len(result.warnings), 0)
        
        # 길이가 제한되었는지 확인 (EOS 토큰 추가를 고려)
        item = corrected_data[0]
        max_instruction_length = 512 * 4  # 설정된 최대 길이
        max_output_length = 8192 * 4
        
        self.assertLessEqual(len(item["instruction"]), max_instruction_length)
        self.assertLessEqual(len(item["output"]), max_output_length)
        
        # 여전히 EOS 토큰으로 끝나는지 확인
        self.assertTrue(item["instruction"].endswith("</s>"))
        self.assertTrue(item["output"].endswith("</s>"))


if __name__ == "__main__":
    unittest.main()