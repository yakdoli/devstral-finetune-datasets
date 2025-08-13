#!/usr/bin/env python3
"""
Alpaca 포맷터 단위 테스트
"""

import unittest
import json
from datetime import datetime
from unsloth_dataset.formatters.alpaca_formatter import AlpacaFormatter, AlpacaConfig


class TestAlpacaFormatter(unittest.TestCase):
    """Alpaca 포맷터 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.formatter = AlpacaFormatter()
        self.test_instruction = "Syncfusion WinForms DataGrid 사용법을 설명해주세요."
        self.test_input = "초보자도 이해할 수 있도록 단계별로 설명해주세요."
        self.test_output = "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치"
    
    def test_format_sample_basic(self):
        """기본 샘플 포맷 테스트"""
        result = self.formatter.format_sample(
            instruction=self.test_instruction,
            output=self.test_output
        )
        
        # 필수 필드 검증
        self.assertIn("instruction", result)
        self.assertIn("output", result)
        self.assertIn("metadata", result)
        
        # 내용 검증
        self.assertIn("DataGrid", result["instruction"])
        self.assertIn("DataGrid", result["output"])
        
        # 메타데이터 검증
        metadata = result["metadata"]
        self.assertEqual(metadata["format"], "alpaca")
        self.assertIn("created_at", metadata)
        self.assertIn("instruction_length", metadata)
        self.assertIn("output_length", metadata)
    
    def test_format_sample_with_input(self):
        """입력 텍스트 포함 샘플 포맷 테스트"""
        result = self.formatter.format_sample(
            instruction=self.test_instruction,
            output=self.test_output,
            input_text=self.test_input
        )
        
        # 입력 필드 검증
        self.assertIn("input", result)
        self.assertIn("초보자", result["input"])
        
        # 메타데이터에 입력 길이 포함 확인
        metadata = result["metadata"]
        self.assertGreater(metadata["input_length"], 0)
    
    def test_format_sample_without_input(self):
        """입력 텍스트 없는 샘플 포맷 테스트"""
        config = AlpacaConfig(include_empty_input=True)
        formatter = AlpacaFormatter(config)
        
        result = formatter.format_sample(
            instruction=self.test_instruction,
            output=self.test_output
        )
        
        # 빈 입력 필드 확인
        self.assertIn("input", result)
        self.assertEqual(result["input"], "")
    
    def test_format_sample_exclude_empty_input(self):
        """빈 입력 필드 제외 테스트"""
        config = AlpacaConfig(include_empty_input=False)
        formatter = AlpacaFormatter(config)
        
        result = formatter.format_sample(
            instruction=self.test_instruction,
            output=self.test_output
        )
        
        # 입력 필드가 없어야 함
        self.assertNotIn("input", result)
    
    def test_format_batch(self):
        """배치 포맷 테스트"""
        samples = [
            {
                "instruction": "첫 번째 지시문",
                "output": "첫 번째 응답",
                "input": "첫 번째 입력",
                "quality_score": 0.9
            },
            {
                "instruction": "두 번째 지시문",
                "output": "두 번째 응답",
                "quality_score": 0.8
            }
        ]
        
        results = self.formatter.format_batch(samples)
        
        self.assertEqual(len(results), 2)
        
        # 첫 번째 샘플 검증
        self.assertIn("input", results[0])
        self.assertEqual(results[0]["input"], "첫 번째 입력</s>")
        
        # 두 번째 샘플 검증 (입력 없음)
        self.assertIn("input", results[1])
        self.assertEqual(results[1]["input"], "")
    
    def test_format_batch_quality_filtering(self):
        """품질 점수 필터링 테스트"""
        config = AlpacaConfig(quality_threshold=0.7)
        formatter = AlpacaFormatter(config)
        
        samples = [
            {
                "instruction": "고품질 지시문",
                "output": "고품질 응답",
                "quality_score": 0.9
            },
            {
                "instruction": "저품질 지시문",
                "output": "저품질 응답",
                "quality_score": 0.5  # 임계값 미만
            }
        ]
        
        results = formatter.format_batch(samples)
        
        # 고품질 샘플만 처리되어야 함
        self.assertEqual(len(results), 1)
        self.assertIn("고품질", results[0]["instruction"])
    
    def test_format_batch_with_invalid_samples(self):
        """잘못된 샘플이 포함된 배치 테스트"""
        samples = [
            {
                "instruction": "올바른 지시문",
                "output": "올바른 응답"
            },
            {
                "instruction": "지시문만 있음"
                # output 누락
            },
            {
                "output": "응답만 있음"
                # instruction 누락
            }
        ]
        
        results = self.formatter.format_batch(samples)
        
        # 올바른 샘플만 처리되어야 함
        self.assertEqual(len(results), 1)
        self.assertIn("올바른", results[0]["instruction"])
    
    def test_format_from_conversation(self):
        """대화 형식에서 Alpaca 포맷 변환 테스트"""
        conversations = [
            {"from": "system", "value": "Syncfusion WinForms 전문가"},
            {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
            {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."},
            {"from": "human", "value": "데이터 바인딩은 어떻게 하나요?"},
            {"from": "gpt", "value": "데이터 바인딩 방법입니다..."}
        ]
        
        result = self.formatter.format_from_conversation(conversations)
        
        # 기본 구조 검증
        self.assertIn("instruction", result)
        self.assertIn("output", result)
        self.assertIn("input", result)
        
        # 지시문에 시스템 프롬프트와 첫 번째 사용자 메시지 포함
        self.assertIn("전문가", result["instruction"])
        self.assertIn("DataGrid", result["instruction"])
        
        # 응답은 마지막 GPT 메시지
        self.assertIn("데이터 바인딩 방법", result["output"])
        
        # 입력은 중간 대화 내용
        self.assertIn("human:", result["input"])
        self.assertIn("gpt:", result["input"])
    
    def test_format_from_empty_conversation(self):
        """빈 대화에서 변환 시 오류 테스트"""
        with self.assertRaises(ValueError):
            self.formatter.format_from_conversation([])
    
    def test_validate_format_valid(self):
        """유효한 포맷 검증 테스트"""
        valid_data = {
            "instruction": "테스트 지시문",
            "output": "테스트 응답",
            "input": "테스트 입력"
        }
        
        self.assertTrue(self.formatter.validate_format(valid_data))
    
    def test_validate_format_invalid(self):
        """잘못된 포맷 검증 테스트"""
        # instruction 필드 누락
        invalid_data1 = {"output": "응답만 있음"}
        self.assertFalse(self.formatter.validate_format(invalid_data1))
        
        # output 필드 누락
        invalid_data2 = {"instruction": "지시문만 있음"}
        self.assertFalse(self.formatter.validate_format(invalid_data2))
        
        # 잘못된 타입
        invalid_data3 = {
            "instruction": 123,  # 문자열이 아님
            "output": "응답"
        }
        self.assertFalse(self.formatter.validate_format(invalid_data3))
    
    def test_length_validation(self):
        """길이 제한 검증 테스트"""
        config = AlpacaConfig(
            max_instruction_length=10,
            max_input_length=10,
            max_output_length=10
        )
        formatter = AlpacaFormatter(config)
        
        long_text = "이것은 매우 긴 텍스트입니다. " * 10
        
        result = formatter.format_sample(
            instruction=long_text,
            output=long_text,
            input_text=long_text
        )
        
        # 길이 제한 확인
        self.assertLessEqual(len(result["instruction"]), 15)  # EOS 토큰 고려
        self.assertLessEqual(len(result["output"]), 15)
        self.assertLessEqual(len(result["input"]), 15)
    
    def test_text_normalization(self):
        """텍스트 정규화 테스트"""
        config = AlpacaConfig(
            normalize_whitespace=True,
            remove_special_chars=True
        )
        formatter = AlpacaFormatter(config)
        
        # 여러 공백과 특수 문자가 포함된 텍스트
        messy_text = "  여러   공백과    특수문자★☆가   포함된   텍스트  "
        
        result = formatter.format_sample(
            instruction=messy_text,
            output="정상 응답"
        )
        
        # 정규화된 텍스트 확인
        self.assertNotIn("  ", result["instruction"])  # 여러 공백 제거
        self.assertNotIn("★", result["instruction"])   # 특수 문자 제거
    
    def test_eos_token_addition(self):
        """EOS 토큰 추가 테스트"""
        config = AlpacaConfig(eos_token="</s>")
        formatter = AlpacaFormatter(config)
        
        result = formatter.format_sample(
            instruction="테스트 지시문",
            output="테스트 응답",
            input_text="테스트 입력"
        )
        
        # 모든 필드에 EOS 토큰이 추가되었는지 확인
        self.assertTrue(result["instruction"].endswith("</s>"))
        self.assertTrue(result["output"].endswith("</s>"))
        self.assertTrue(result["input"].endswith("</s>"))
    
    def test_custom_config(self):
        """커스텀 설정 테스트"""
        config = AlpacaConfig(
            instruction_prefix="커스텀 접두사:",
            quality_threshold=0.8,
            include_empty_input=False
        )
        formatter = AlpacaFormatter(config)
        
        # 설정 확인
        self.assertEqual(formatter.config.instruction_prefix, "커스텀 접두사:")
        self.assertEqual(formatter.config.quality_threshold, 0.8)
        self.assertFalse(formatter.config.include_empty_input)
    
    def test_get_format_info(self):
        """포맷 정보 반환 테스트"""
        info = self.formatter.get_format_info()
        
        self.assertIn("name", info)
        self.assertIn("description", info)
        self.assertIn("required_fields", info)
        self.assertIn("features", info)
        
        self.assertEqual(info["name"], "Alpaca")
        self.assertIn("instruction", info["required_fields"])
        self.assertIn("output", info["required_fields"])
    
    def test_metadata_generation(self):
        """메타데이터 생성 테스트"""
        result = self.formatter.format_sample(
            instruction=self.test_instruction,
            output=self.test_output,
            input_text=self.test_input
        )
        
        metadata = result["metadata"]
        
        self.assertEqual(metadata["format"], "alpaca")
        self.assertIn("created_at", metadata)
        self.assertIn("instruction_length", metadata)
        self.assertIn("input_length", metadata)
        self.assertIn("output_length", metadata)
        self.assertIn("total_tokens", metadata)
        
        # 날짜 형식 검증
        created_at = metadata["created_at"]
        datetime.fromisoformat(created_at)  # 유효한 ISO 형식인지 확인
        
        # 길이 검증
        self.assertGreater(metadata["instruction_length"], 0)
        self.assertGreater(metadata["input_length"], 0)
        self.assertGreater(metadata["output_length"], 0)
        self.assertGreater(metadata["total_tokens"], 0)


if __name__ == "__main__":
    unittest.main()