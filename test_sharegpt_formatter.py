#!/usr/bin/env python3
"""
ShareGPT 포맷터 단위 테스트
"""

import unittest
import json
from datetime import datetime
from unsloth_dataset.formatters.sharegpt_formatter import ShareGPTFormatter, ShareGPTConfig


class TestShareGPTFormatter(unittest.TestCase):
    """ShareGPT 포맷터 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.formatter = ShareGPTFormatter()
        self.test_instruction = "Syncfusion WinForms DataGrid 사용법을 알려주세요."
        self.test_response = "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치"
        self.test_context = "WinForms 애플리케이션 개발"
    
    def test_format_conversation_basic(self):
        """기본 대화 포맷 테스트"""
        result = self.formatter.format_conversation(
            instruction=self.test_instruction,
            response=self.test_response
        )
        
        # 기본 구조 검증
        self.assertIn("conversations", result)
        self.assertIn("metadata", result)
        
        conversations = result["conversations"]
        self.assertIsInstance(conversations, list)
        self.assertGreaterEqual(len(conversations), 3)  # system + human + gpt
        
        # 시스템 메시지 검증
        self.assertEqual(conversations[0]["from"], "system")
        self.assertIn("Syncfusion", conversations[0]["value"])
        
        # 사용자 메시지 검증
        self.assertEqual(conversations[1]["from"], "human")
        self.assertIn("DataGrid", conversations[1]["value"])
        
        # GPT 응답 검증
        self.assertEqual(conversations[2]["from"], "gpt")
        self.assertIn("DataGrid", conversations[2]["value"])
    
    def test_format_conversation_with_context(self):
        """컨텍스트 포함 대화 포맷 테스트"""
        result = self.formatter.format_conversation(
            instruction=self.test_instruction,
            response=self.test_response,
            context=self.test_context
        )
        
        conversations = result["conversations"]
        self.assertGreaterEqual(len(conversations), 4)  # system + context + human + gpt
        
        # 컨텍스트 메시지 확인
        context_found = False
        for conv in conversations:
            if conv["from"] == "system" and "컨텍스트" in conv["value"]:
                context_found = True
                break
        self.assertTrue(context_found)
    
    def test_format_conversation_with_turns(self):
        """다중 턴 대화 포맷 테스트"""
        turns = [
            {"from": "human", "value": "추가 질문입니다."},
            {"from": "gpt", "value": "추가 답변입니다."}
        ]
        
        result = self.formatter.format_conversation(
            instruction=self.test_instruction,
            response=self.test_response,
            turns=turns
        )
        
        conversations = result["conversations"]
        self.assertGreaterEqual(len(conversations), 5)  # system + human + gpt + 2 turns
        
        # 추가 턴 검증
        self.assertEqual(conversations[-2]["from"], "human")
        self.assertEqual(conversations[-1]["from"], "gpt")
    
    def test_format_batch(self):
        """배치 포맷 테스트"""
        samples = [
            {
                "instruction": "첫 번째 질문",
                "response": "첫 번째 답변",
                "source": "test1"
            },
            {
                "instruction": "두 번째 질문",
                "response": "두 번째 답변",
                "context": "테스트 컨텍스트",
                "source": "test2"
            }
        ]
        
        results = self.formatter.format_batch(samples)
        
        self.assertEqual(len(results), 2)
        
        # 첫 번째 샘플 검증
        self.assertIn("conversations", results[0])
        self.assertIn("metadata", results[0])
        
        # 두 번째 샘플 검증 (컨텍스트 포함)
        conversations = results[1]["conversations"]
        context_found = any("컨텍스트" in conv["value"] for conv in conversations if conv["from"] == "system")
        self.assertTrue(context_found)
    
    def test_format_batch_with_invalid_samples(self):
        """잘못된 샘플이 포함된 배치 테스트"""
        samples = [
            {
                "instruction": "올바른 질문",
                "response": "올바른 답변"
            },
            {
                "instruction": "질문만 있음"
                # response 누락
            },
            {
                "response": "답변만 있음"
                # instruction 누락
            }
        ]
        
        results = self.formatter.format_batch(samples)
        
        # 올바른 샘플만 처리되어야 함
        self.assertEqual(len(results), 1)
        self.assertIn("올바른", results[0]["conversations"][1]["value"])
    
    def test_validate_format_valid(self):
        """유효한 포맷 검증 테스트"""
        valid_data = {
            "conversations": [
                {"from": "system", "value": "시스템 메시지"},
                {"from": "human", "value": "사용자 질문"},
                {"from": "gpt", "value": "GPT 응답"}
            ],
            "metadata": {"format": "sharegpt"}
        }
        
        self.assertTrue(self.formatter.validate_format(valid_data))
    
    def test_validate_format_invalid(self):
        """잘못된 포맷 검증 테스트"""
        # conversations 필드 누락
        invalid_data1 = {"metadata": {"format": "sharegpt"}}
        self.assertFalse(self.formatter.validate_format(invalid_data1))
        
        # 잘못된 역할
        invalid_data2 = {
            "conversations": [
                {"from": "invalid_role", "value": "메시지"}
            ]
        }
        self.assertFalse(self.formatter.validate_format(invalid_data2))
        
        # 필수 필드 누락
        invalid_data3 = {
            "conversations": [
                {"from": "human"}  # value 누락
            ]
        }
        self.assertFalse(self.formatter.validate_format(invalid_data3))
    
    def test_text_normalization(self):
        """텍스트 정규화 테스트"""
        config = ShareGPTConfig(
            normalize_whitespace=True,
            remove_special_chars=True
        )
        formatter = ShareGPTFormatter(config)
        
        # 여러 공백과 특수 문자가 포함된 텍스트
        messy_text = "  여러   공백과    특수문자★☆가   포함된   텍스트  "
        
        result = formatter.format_conversation(
            instruction=messy_text,
            response="정상 응답"
        )
        
        # 정규화된 텍스트 확인
        human_message = result["conversations"][1]["value"]
        self.assertNotIn("  ", human_message)  # 여러 공백 제거
        self.assertNotIn("★", human_message)   # 특수 문자 제거
    
    def test_eos_token_addition(self):
        """EOS 토큰 추가 테스트"""
        config = ShareGPTConfig(eos_token="</s>")
        formatter = ShareGPTFormatter(config)
        
        result = formatter.format_conversation(
            instruction="테스트 질문",
            response="테스트 응답"
        )
        
        conversations = result["conversations"]
        
        # human과 gpt 메시지에 EOS 토큰이 추가되었는지 확인
        for conv in conversations:
            if conv["from"] in ["human", "gpt"]:
                self.assertTrue(conv["value"].endswith("</s>"))
    
    def test_custom_config(self):
        """커스텀 설정 테스트"""
        config = ShareGPTConfig(
            system_prompt="커스텀 시스템 프롬프트",
            add_system_message=True,
            max_conversation_length=1000
        )
        formatter = ShareGPTFormatter(config)
        
        result = formatter.format_conversation(
            instruction="테스트 질문",
            response="테스트 응답"
        )
        
        # 커스텀 시스템 프롬프트 확인
        system_message = result["conversations"][0]["value"]
        self.assertEqual(system_message, "커스텀 시스템 프롬프트")
    
    def test_get_format_info(self):
        """포맷 정보 반환 테스트"""
        info = self.formatter.get_format_info()
        
        self.assertIn("name", info)
        self.assertIn("description", info)
        self.assertIn("required_fields", info)
        self.assertIn("features", info)
        
        self.assertEqual(info["name"], "ShareGPT")
        self.assertIn("instruction", info["required_fields"])
        self.assertIn("response", info["required_fields"])
    
    def test_metadata_generation(self):
        """메타데이터 생성 테스트"""
        result = self.formatter.format_conversation(
            instruction=self.test_instruction,
            response=self.test_response
        )
        
        metadata = result["metadata"]
        
        self.assertEqual(metadata["format"], "sharegpt")
        self.assertIn("created_at", metadata)
        self.assertIn("turns", metadata)
        self.assertIn("system_prompt", metadata)
        
        # 날짜 형식 검증
        created_at = metadata["created_at"]
        datetime.fromisoformat(created_at)  # 유효한 ISO 형식인지 확인


if __name__ == "__main__":
    unittest.main()