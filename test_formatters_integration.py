#!/usr/bin/env python3
"""
포맷터 통합 테스트
모든 포맷터가 함께 작동하는지 확인합니다.
"""

import unittest
import json
from unsloth_dataset.formatters import (
    create_formatter, 
    get_supported_formats,
    ShareGPTFormatter,
    AlpacaFormatter, 
    OpenAIFormatter
)


class TestFormattersIntegration(unittest.TestCase):
    """포맷터 통합 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.test_data = {
            "instruction": "Syncfusion WinForms DataGrid 컴포넌트 사용법을 설명해주세요.",
            "response": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정",
            "context": "WinForms 애플리케이션 개발 가이드",
            "source": "documentation",
            "quality_score": 0.9
        }
        
        self.conversation_data = [
            {"from": "system", "value": "Syncfusion WinForms 전문가입니다."},
            {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
            {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."},
            {"from": "human", "value": "데이터 바인딩은 어떻게 하나요?"},
            {"from": "gpt", "value": "데이터 바인딩 방법입니다..."}
        ]
    
    def test_create_formatter_factory(self):
        """포맷터 팩토리 함수 테스트"""
        # 지원하는 모든 포맷에 대해 포맷터 생성
        for format_type in get_supported_formats():
            formatter = create_formatter(format_type)
            self.assertIsNotNone(formatter)
            
            # 포맷터 타입 확인
            if format_type == "sharegpt":
                self.assertIsInstance(formatter, ShareGPTFormatter)
            elif format_type == "alpaca":
                self.assertIsInstance(formatter, AlpacaFormatter)
            elif format_type == "openai":
                self.assertIsInstance(formatter, OpenAIFormatter)
    
    def test_create_formatter_invalid_type(self):
        """지원하지 않는 포맷 타입 테스트"""
        with self.assertRaises(ValueError):
            create_formatter("invalid_format")
    
    def test_all_formatters_basic_functionality(self):
        """모든 포맷터의 기본 기능 테스트"""
        formatters = {
            "sharegpt": create_formatter("sharegpt"),
            "alpaca": create_formatter("alpaca"),
            "openai": create_formatter("openai")
        }
        
        for format_name, formatter in formatters.items():
            with self.subTest(format=format_name):
                # 포맷 정보 확인
                info = formatter.get_format_info()
                self.assertIn("name", info)
                self.assertIn("description", info)
                self.assertIn("required_fields", info)
                
                # 기본 포맷 변환 테스트
                if format_name == "sharegpt":
                    result = formatter.format_conversation(
                        instruction=self.test_data["instruction"],
                        response=self.test_data["response"]
                    )
                    self.assertIn("conversations", result)
                    self.assertTrue(formatter.validate_format(result))
                    
                elif format_name == "alpaca":
                    result = formatter.format_sample(
                        instruction=self.test_data["instruction"],
                        output=self.test_data["response"]
                    )
                    self.assertIn("instruction", result)
                    self.assertIn("output", result)
                    self.assertTrue(formatter.validate_format(result))
                    
                elif format_name == "openai":
                    result = formatter.format_messages(
                        user_message=self.test_data["instruction"],
                        assistant_message=self.test_data["response"]
                    )
                    self.assertIn("messages", result)
                    self.assertTrue(formatter.validate_format(result))
    
    def test_conversation_to_all_formats(self):
        """대화 데이터를 모든 포맷으로 변환 테스트"""
        formatters = {
            "sharegpt": create_formatter("sharegpt"),
            "alpaca": create_formatter("alpaca"),
            "openai": create_formatter("openai")
        }
        
        results = {}
        
        for format_name, formatter in formatters.items():
            with self.subTest(format=format_name):
                if format_name == "sharegpt":
                    # ShareGPT는 대화 형식을 직접 처리
                    result = formatter.format_conversation(
                        instruction=self.conversation_data[1]["value"],
                        response=self.conversation_data[-1]["value"],
                        context="시스템: " + self.conversation_data[0]["value"]
                    )
                    
                elif format_name == "alpaca":
                    # Alpaca는 대화를 instruction-output 형식으로 변환
                    result = formatter.format_from_conversation(self.conversation_data)
                    
                elif format_name == "openai":
                    # OpenAI는 대화를 메시지 배열로 변환
                    result = formatter.format_from_conversation(self.conversation_data)
                
                results[format_name] = result
                
                # 유효성 검증
                self.assertTrue(formatter.validate_format(result))
        
        # 결과 확인
        self.assertEqual(len(results), 3)
        
        # ShareGPT 결과 확인
        sharegpt_result = results["sharegpt"]
        self.assertIn("conversations", sharegpt_result)
        self.assertGreater(len(sharegpt_result["conversations"]), 0)
        
        # Alpaca 결과 확인
        alpaca_result = results["alpaca"]
        self.assertIn("instruction", alpaca_result)
        self.assertIn("output", alpaca_result)
        
        # OpenAI 결과 확인
        openai_result = results["openai"]
        self.assertIn("messages", openai_result)
        self.assertGreater(len(openai_result["messages"]), 0)
    
    def test_batch_processing_all_formats(self):
        """모든 포맷터의 배치 처리 테스트"""
        # 테스트 샘플 데이터 준비
        samples = [
            {
                "instruction": "첫 번째 질문",
                "response": "첫 번째 답변",
                "user_message": "첫 번째 질문",
                "assistant_message": "첫 번째 답변",
                "output": "첫 번째 답변",
                "quality_score": 0.9
            },
            {
                "instruction": "두 번째 질문",
                "response": "두 번째 답변",
                "user_message": "두 번째 질문",
                "assistant_message": "두 번째 답변",
                "output": "두 번째 답변",
                "quality_score": 0.8
            }
        ]
        
        formatters = {
            "sharegpt": create_formatter("sharegpt"),
            "alpaca": create_formatter("alpaca"),
            "openai": create_formatter("openai")
        }
        
        for format_name, formatter in formatters.items():
            with self.subTest(format=format_name):
                results = formatter.format_batch(samples)
                
                # 결과 개수 확인
                self.assertEqual(len(results), 2)
                
                # 각 결과 유효성 검증
                for result in results:
                    self.assertTrue(formatter.validate_format(result))
    
    def test_format_consistency(self):
        """포맷 간 일관성 테스트"""
        # 동일한 입력 데이터로 모든 포맷 생성
        instruction = "Syncfusion Chart 컴포넌트 사용법"
        response = "Chart 컴포넌트 사용 방법을 설명합니다."
        
        # ShareGPT 포맷
        sharegpt_formatter = create_formatter("sharegpt")
        sharegpt_result = sharegpt_formatter.format_conversation(
            instruction=instruction,
            response=response
        )
        
        # Alpaca 포맷
        alpaca_formatter = create_formatter("alpaca")
        alpaca_result = alpaca_formatter.format_sample(
            instruction=instruction,
            output=response
        )
        
        # OpenAI 포맷
        openai_formatter = create_formatter("openai")
        openai_result = openai_formatter.format_messages(
            user_message=instruction,
            assistant_message=response
        )
        
        # 내용 일관성 확인
        # ShareGPT에서 사용자 메시지 추출
        sharegpt_user_msg = None
        sharegpt_gpt_msg = None
        for conv in sharegpt_result["conversations"]:
            if conv["from"] == "human":
                sharegpt_user_msg = conv["value"].replace("</s>", "")
            elif conv["from"] == "gpt":
                sharegpt_gpt_msg = conv["value"].replace("</s>", "")
        
        # Alpaca에서 내용 추출
        alpaca_instruction = alpaca_result["instruction"].replace("</s>", "")
        alpaca_output = alpaca_result["output"].replace("</s>", "")
        
        # OpenAI에서 내용 추출
        openai_user_msg = None
        openai_assistant_msg = None
        for msg in openai_result["messages"]:
            if msg["role"] == "user":
                openai_user_msg = msg["content"].replace("</s>", "")
            elif msg["role"] == "assistant":
                openai_assistant_msg = msg["content"].replace("</s>", "")
        
        # 일관성 검증
        self.assertEqual(sharegpt_user_msg, instruction)
        self.assertEqual(sharegpt_gpt_msg, response)
        self.assertIn(instruction, alpaca_instruction)  # Alpaca는 시스템 프롬프트가 포함될 수 있음
        self.assertEqual(alpaca_output, response)
        self.assertEqual(openai_user_msg, instruction)
        self.assertEqual(openai_assistant_msg, response)
    
    def test_error_handling_all_formats(self):
        """모든 포맷터의 오류 처리 테스트"""
        formatters = {
            "sharegpt": create_formatter("sharegpt"),
            "alpaca": create_formatter("alpaca"),
            "openai": create_formatter("openai")
        }
        
        # 잘못된 입력 데이터
        invalid_samples = [
            {"instruction": "질문만 있음"},  # response/output/assistant_message 누락
            {"response": "답변만 있음"},     # instruction/user_message 누락
            {}                              # 모든 필드 누락
        ]
        
        for format_name, formatter in formatters.items():
            with self.subTest(format=format_name):
                results = formatter.format_batch(invalid_samples)
                
                # 잘못된 샘플은 처리되지 않아야 함
                self.assertEqual(len(results), 0)
    
    def test_metadata_consistency(self):
        """메타데이터 일관성 테스트"""
        formatters = {
            "sharegpt": create_formatter("sharegpt"),
            "alpaca": create_formatter("alpaca"),
            "openai": create_formatter("openai")
        }
        
        for format_name, formatter in formatters.items():
            with self.subTest(format=format_name):
                if format_name == "sharegpt":
                    result = formatter.format_conversation(
                        instruction="테스트 질문",
                        response="테스트 답변"
                    )
                elif format_name == "alpaca":
                    result = formatter.format_sample(
                        instruction="테스트 질문",
                        output="테스트 답변"
                    )
                elif format_name == "openai":
                    result = formatter.format_messages(
                        user_message="테스트 질문",
                        assistant_message="테스트 답변"
                    )
                
                # 메타데이터 존재 확인
                self.assertIn("metadata", result)
                metadata = result["metadata"]
                
                # 공통 메타데이터 필드 확인
                self.assertIn("format", metadata)
                self.assertIn("created_at", metadata)
                self.assertEqual(metadata["format"], format_name)


if __name__ == "__main__":
    unittest.main()