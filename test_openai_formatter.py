#!/usr/bin/env python3
"""
OpenAI 포맷터 단위 테스트
"""

import unittest
import json
from datetime import datetime
from unsloth_dataset.formatters.openai_formatter import OpenAIFormatter, OpenAIConfig


class TestOpenAIFormatter(unittest.TestCase):
    """OpenAI 포맷터 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.formatter = OpenAIFormatter()
        self.test_user_message = "Syncfusion WinForms DataGrid 사용법을 알려주세요."
        self.test_assistant_message = "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치"
        self.test_system_prompt = "Syncfusion WinForms 기술 전문가"
    
    def test_format_messages_basic(self):
        """기본 메시지 포맷 테스트"""
        result = self.formatter.format_messages(
            user_message=self.test_user_message,
            assistant_message=self.test_assistant_message
        )
        
        # 기본 구조 검증
        self.assertIn("messages", result)
        self.assertIn("metadata", result)
        
        messages = result["messages"]
        self.assertIsInstance(messages, list)
        self.assertGreaterEqual(len(messages), 3)  # system + user + assistant
        
        # 시스템 메시지 검증
        self.assertEqual(messages[0]["role"], "system")
        self.assertIn("Syncfusion", messages[0]["content"])
        
        # 사용자 메시지 검증
        self.assertEqual(messages[1]["role"], "user")
        self.assertIn("DataGrid", messages[1]["content"])
        
        # 어시스턴트 메시지 검증
        self.assertEqual(messages[2]["role"], "assistant")
        self.assertIn("DataGrid", messages[2]["content"])
    
    def test_format_messages_with_custom_system_prompt(self):
        """커스텀 시스템 프롬프트 포함 메시지 포맷 테스트"""
        result = self.formatter.format_messages(
            user_message=self.test_user_message,
            assistant_message=self.test_assistant_message,
            system_prompt=self.test_system_prompt
        )
        
        messages = result["messages"]
        
        # 커스텀 시스템 프롬프트 확인
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[0]["content"], self.test_system_prompt)
    
    def test_format_messages_with_context(self):
        """컨텍스트 메시지 포함 포맷 테스트"""
        context_messages = [
            {"role": "user", "content": "이전 질문입니다."},
            {"role": "assistant", "content": "이전 답변입니다."}
        ]
        
        result = self.formatter.format_messages(
            user_message=self.test_user_message,
            assistant_message=self.test_assistant_message,
            context_messages=context_messages
        )
        
        messages = result["messages"]
        self.assertGreaterEqual(len(messages), 5)  # system + 2 context + user + assistant
        
        # 컨텍스트 메시지 확인
        self.assertEqual(messages[1]["role"], "user")
        self.assertIn("이전 질문", messages[1]["content"])
        self.assertEqual(messages[2]["role"], "assistant")
        self.assertIn("이전 답변", messages[2]["content"])
    
    def test_format_messages_without_system(self):
        """시스템 메시지 없는 포맷 테스트"""
        config = OpenAIConfig(include_system_message=False)
        formatter = OpenAIFormatter(config)
        
        result = formatter.format_messages(
            user_message=self.test_user_message,
            assistant_message=self.test_assistant_message
        )
        
        messages = result["messages"]
        self.assertEqual(len(messages), 2)  # user + assistant only
        
        # 첫 번째 메시지가 사용자 메시지여야 함
        self.assertEqual(messages[0]["role"], "user")
        self.assertEqual(messages[1]["role"], "assistant")
    
    def test_format_batch(self):
        """배치 포맷 테스트"""
        samples = [
            {
                "user_message": "첫 번째 사용자 메시지",
                "assistant_message": "첫 번째 어시스턴트 메시지",
                "system_prompt": "첫 번째 시스템 프롬프트",
                "quality_score": 0.9
            },
            {
                "user_message": "두 번째 사용자 메시지",
                "assistant_message": "두 번째 어시스턴트 메시지",
                "quality_score": 0.8
            }
        ]
        
        results = self.formatter.format_batch(samples)
        
        self.assertEqual(len(results), 2)
        
        # 첫 번째 샘플 검증
        messages1 = results[0]["messages"]
        self.assertEqual(messages1[0]["content"], "첫 번째 시스템 프롬프트")
        
        # 두 번째 샘플 검증 (기본 시스템 프롬프트)
        messages2 = results[1]["messages"]
        self.assertIn("Syncfusion", messages2[0]["content"])
    
    def test_format_batch_quality_filtering(self):
        """품질 점수 필터링 테스트"""
        config = OpenAIConfig(quality_threshold=0.7)
        formatter = OpenAIFormatter(config)
        
        samples = [
            {
                "user_message": "고품질 사용자 메시지",
                "assistant_message": "고품질 어시스턴트 메시지",
                "quality_score": 0.9
            },
            {
                "user_message": "저품질 사용자 메시지",
                "assistant_message": "저품질 어시스턴트 메시지",
                "quality_score": 0.5  # 임계값 미만
            }
        ]
        
        results = formatter.format_batch(samples)
        
        # 고품질 샘플만 처리되어야 함
        self.assertEqual(len(results), 1)
        self.assertIn("고품질", results[0]["messages"][1]["content"])
    
    def test_format_batch_with_invalid_samples(self):
        """잘못된 샘플이 포함된 배치 테스트"""
        samples = [
            {
                "user_message": "올바른 사용자 메시지",
                "assistant_message": "올바른 어시스턴트 메시지"
            },
            {
                "user_message": "사용자 메시지만 있음"
                # assistant_message 누락
            },
            {
                "assistant_message": "어시스턴트 메시지만 있음"
                # user_message 누락
            }
        ]
        
        results = self.formatter.format_batch(samples)
        
        # 올바른 샘플만 처리되어야 함
        self.assertEqual(len(results), 1)
        self.assertIn("올바른", results[0]["messages"][1]["content"])
    
    def test_format_from_conversation(self):
        """대화 형식에서 OpenAI 포맷 변환 테스트"""
        conversations = [
            {"from": "system", "value": "Syncfusion WinForms 전문가"},
            {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
            {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."},
            {"from": "human", "value": "데이터 바인딩은 어떻게 하나요?"},
            {"from": "gpt", "value": "데이터 바인딩 방법입니다..."}
        ]
        
        result = self.formatter.format_from_conversation(conversations)
        
        # 기본 구조 검증
        self.assertIn("messages", result)
        messages = result["messages"]
        
        # 시스템 메시지 확인
        self.assertEqual(messages[0]["role"], "system")
        self.assertIn("전문가", messages[0]["content"])
        
        # 마지막 사용자-어시스턴트 쌍 확인
        self.assertEqual(messages[-2]["role"], "user")
        self.assertIn("데이터 바인딩", messages[-2]["content"])
        self.assertEqual(messages[-1]["role"], "assistant")
        self.assertIn("데이터 바인딩 방법", messages[-1]["content"])
    
    def test_format_from_empty_conversation(self):
        """빈 대화에서 변환 시 오류 테스트"""
        with self.assertRaises(ValueError):
            self.formatter.format_from_conversation([])
    
    def test_validate_format_valid(self):
        """유효한 포맷 검증 테스트"""
        valid_data = {
            "messages": [
                {"role": "system", "content": "시스템 메시지"},
                {"role": "user", "content": "사용자 메시지"},
                {"role": "assistant", "content": "어시스턴트 메시지"}
            ]
        }
        
        self.assertTrue(self.formatter.validate_format(valid_data))
    
    def test_validate_format_invalid(self):
        """잘못된 포맷 검증 테스트"""
        # messages 필드 누락
        invalid_data1 = {"metadata": {"format": "openai"}}
        self.assertFalse(self.formatter.validate_format(invalid_data1))
        
        # 잘못된 역할
        invalid_data2 = {
            "messages": [
                {"role": "invalid_role", "content": "메시지"}
            ]
        }
        self.assertFalse(self.formatter.validate_format(invalid_data2))
        
        # 필수 필드 누락
        invalid_data3 = {
            "messages": [
                {"role": "user"}  # content 누락
            ]
        }
        self.assertFalse(self.formatter.validate_format(invalid_data3))
        
        # 최소 메시지 수 미달
        invalid_data4 = {
            "messages": [
                {"role": "user", "content": "메시지 하나만"}
            ]
        }
        self.assertFalse(self.formatter.validate_format(invalid_data4))
    
    def test_validate_message_order(self):
        """메시지 순서 검증 테스트"""
        config = OpenAIConfig(validate_message_order=True)
        formatter = OpenAIFormatter(config)
        
        # 올바른 순서
        valid_data = {
            "messages": [
                {"role": "system", "content": "시스템"},
                {"role": "user", "content": "사용자"},
                {"role": "assistant", "content": "어시스턴트"}
            ]
        }
        self.assertTrue(formatter.validate_format(valid_data))
        
        # 잘못된 순서
        invalid_data = {
            "messages": [
                {"role": "user", "content": "사용자"},
                {"role": "user", "content": "사용자 연속"}  # 잘못된 순서
            ]
        }
        self.assertFalse(formatter.validate_format(invalid_data))
    
    def test_message_length_validation(self):
        """메시지 길이 검증 테스트"""
        config = OpenAIConfig(max_message_length=10)
        formatter = OpenAIFormatter(config)
        
        long_message = "이것은 매우 긴 메시지입니다. " * 10
        
        invalid_data = {
            "messages": [
                {"role": "user", "content": long_message},
                {"role": "assistant", "content": "짧은 응답"}
            ]
        }
        
        self.assertFalse(formatter.validate_format(invalid_data))
    
    def test_text_normalization(self):
        """텍스트 정규화 테스트"""
        config = OpenAIConfig(
            normalize_whitespace=True,
            remove_special_chars=True
        )
        formatter = OpenAIFormatter(config)
        
        # 여러 공백과 특수 문자가 포함된 텍스트
        messy_text = "  여러   공백과    특수문자★☆가   포함된   텍스트  "
        
        result = formatter.format_messages(
            user_message=messy_text,
            assistant_message="정상 응답"
        )
        
        # 정규화된 텍스트 확인
        user_message = result["messages"][1]["content"]
        self.assertNotIn("  ", user_message)  # 여러 공백 제거
        self.assertNotIn("★", user_message)   # 특수 문자 제거
    
    def test_eos_token_addition(self):
        """EOS 토큰 추가 테스트"""
        config = OpenAIConfig(eos_token="</s>")
        formatter = OpenAIFormatter(config)
        
        result = formatter.format_messages(
            user_message="테스트 사용자 메시지",
            assistant_message="테스트 어시스턴트 메시지"
        )
        
        messages = result["messages"]
        
        # user와 assistant 메시지에 EOS 토큰이 추가되었는지 확인
        for msg in messages:
            if msg["role"] in ["user", "assistant"]:
                self.assertTrue(msg["content"].endswith("</s>"))
    
    def test_custom_roles(self):
        """커스텀 역할 설정 테스트"""
        config = OpenAIConfig(
            system_role="system",
            user_role="human",
            assistant_role="ai"
        )
        formatter = OpenAIFormatter(config)
        
        result = formatter.format_messages(
            user_message="테스트 메시지",
            assistant_message="테스트 응답"
        )
        
        messages = result["messages"]
        
        # 커스텀 역할 확인
        self.assertEqual(messages[1]["role"], "human")
        self.assertEqual(messages[2]["role"], "ai")
    
    def test_get_format_info(self):
        """포맷 정보 반환 테스트"""
        info = self.formatter.get_format_info()
        
        self.assertIn("name", info)
        self.assertIn("description", info)
        self.assertIn("required_fields", info)
        self.assertIn("features", info)
        
        self.assertEqual(info["name"], "OpenAI")
        self.assertIn("user_message", info["required_fields"])
        self.assertIn("assistant_message", info["required_fields"])
    
    def test_metadata_generation(self):
        """메타데이터 생성 테스트"""
        result = self.formatter.format_messages(
            user_message=self.test_user_message,
            assistant_message=self.test_assistant_message,
            system_prompt=self.test_system_prompt
        )
        
        metadata = result["metadata"]
        
        self.assertEqual(metadata["format"], "openai")
        self.assertIn("created_at", metadata)
        self.assertIn("message_count", metadata)
        self.assertIn("system_prompt", metadata)
        self.assertIn("total_tokens", metadata)
        
        # 날짜 형식 검증
        created_at = metadata["created_at"]
        datetime.fromisoformat(created_at)  # 유효한 ISO 형식인지 확인
        
        # 메시지 수 검증
        self.assertGreater(metadata["message_count"], 0)
        self.assertGreater(metadata["total_tokens"], 0)
    
    def test_token_calculation(self):
        """토큰 계산 테스트"""
        result = self.formatter.format_messages(
            user_message="짧은 메시지",
            assistant_message="조금 더 긴 응답 메시지입니다."
        )
        
        metadata = result["metadata"]
        total_tokens = metadata["total_tokens"]
        
        # 토큰 수가 합리적인 범위인지 확인
        self.assertGreater(total_tokens, 0)
        self.assertLess(total_tokens, 1000)  # 짧은 메시지이므로


if __name__ == "__main__":
    unittest.main()