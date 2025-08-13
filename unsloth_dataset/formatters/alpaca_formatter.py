#!/usr/bin/env python3
"""
Alpaca 포맷터 모듈
Unsloth 프레임워크와 호환되는 Alpaca 포맷 데이터셋을 생성합니다.
"""

import json
import logging
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import re

logger = logging.getLogger(__name__)


@dataclass
class AlpacaConfig:
    """Alpaca 포맷터 설정"""
    instruction_prefix: str = "다음은 작업 설명입니다. 요청을 적절히 완료하는 응답을 작성하세요."
    input_prefix: str = "입력:"
    output_prefix: str = "응답:"
    eos_token: str = "</s>"
    normalize_whitespace: bool = True
    remove_special_chars: bool = True
    max_instruction_length: int = 512
    max_input_length: int = 1024
    max_output_length: int = 8192
    include_empty_input: bool = True
    quality_threshold: float = 0.5


class AlpacaFormatter:
    """Alpaca 포맷 데이터셋 생성기"""
    
    def __init__(self, config: Optional[AlpacaConfig] = None):
        """
        Alpaca 포맷터를 초기화합니다.
        
        Args:
            config: Alpaca 포맷터 설정
        """
        self.config = config or AlpacaConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
    def format_sample(
        self, 
        instruction: str, 
        output: str, 
        input_text: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        단일 샘플을 Alpaca 포맷으로 변환합니다.
        
        Args:
            instruction: 지시문
            output: 응답
            input_text: 입력 텍스트 (선택적)
            metadata: 메타데이터 (선택적)
            
        Returns:
            Alpaca 포맷 딕셔너리
        """
        # 텍스트 정규화
        instruction = self._normalize_text(instruction)
        output = self._normalize_text(output)
        
        if input_text:
            input_text = self._normalize_text(input_text)
        
        # 길이 검증
        if len(instruction) > self.config.max_instruction_length:
            self.logger.warning(f"지시문 길이 초과: {len(instruction)} > {self.config.max_instruction_length}")
            instruction = instruction[:self.config.max_instruction_length]
        
        if input_text and len(input_text) > self.config.max_input_length:
            self.logger.warning(f"입력 텍스트 길이 초과: {len(input_text)} > {self.config.max_input_length}")
            input_text = input_text[:self.config.max_input_length]
        
        if len(output) > self.config.max_output_length:
            self.logger.warning(f"응답 길이 초과: {len(output)} > {self.config.max_output_length}")
            output = output[:self.config.max_output_length]
        
        # 필수 필드 구성
        alpaca_sample = {
            "instruction": instruction,
            "output": output
        }
        
        # 입력 텍스트 추가 (비어있지 않은 경우)
        if input_text or self.config.include_empty_input:
            alpaca_sample["input"] = input_text if input_text else ""
        
        # 메타데이터 추가
        if metadata:
            alpaca_sample["metadata"] = metadata
        else:
            alpaca_sample["metadata"] = {
                "format": "alpaca",
                "created_at": datetime.now().isoformat(),
                "instruction_length": len(instruction),
                "input_length": len(input_text) if input_text else 0,
                "output_length": len(output),
                "total_tokens": self._calculate_total_tokens(alpaca_sample)
            }
        
        # EOS 토큰 추가
        alpaca_sample["instruction"] = self._add_eos_token(alpaca_sample["instruction"])
        alpaca_sample["output"] = self._add_eos_token(alpaca_sample["output"])
        if "input" in alpaca_sample:
            alpaca_sample["input"] = self._add_eos_token(alpaca_sample["input"])
        
        return alpaca_sample
    
    def format_batch(
        self, 
        samples: List[Dict[str, Any]], 
        include_metadata: bool = True
    ) -> List[Dict[str, Any]]:
        """
        샘플 배치를 Alpaca 포맷으로 변환합니다.
        
        Args:
            samples: 샘플 데이터 목록
            include_metadata: 메타데이터 포함 여부
            
        Returns:
            Alpaca 포맷 데이터 목록
        """
        formatted_samples = []
        
        for i, sample in enumerate(samples):
            try:
                # 필수 필드 확인
                if "instruction" not in sample or "output" not in sample:
                    self.logger.warning(f"Sample {i} 필수 필드 누락: {sample}")
                    continue
                
                # 품질 점수 검증
                quality_score = sample.get("quality_score", 1.0)
                if quality_score < self.config.quality_threshold:
                    self.logger.warning(f"Sample {i} 품질 점수 낮음: {quality_score}")
                    continue
                
                # Alpaca 포맷으로 변환
                formatted = self.format_sample(
                    instruction=sample["instruction"],
                    output=sample["output"],
                    input_text=sample.get("input"),
                    metadata=sample.get("metadata")
                )
                
                # 메타데이터 처리
                if include_metadata:
                    formatted["metadata"].update({
                        "sample_index": i,
                        "source": sample.get("source", "unknown"),
                        "original_quality_score": quality_score,
                        "has_context": "context" in sample,
                        "has_turns": "turns" in sample
                    })
                else:
                    del formatted["metadata"]
                
                formatted_samples.append(formatted)
                
            except Exception as e:
                self.logger.error(f"Sample {i} 처리 실패: {e}")
                continue
        
        return formatted_samples
    
    def format_from_conversation(
        self, 
        conversations: List[Dict[str, str]], 
        system_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        대화 형식의 데이터를 Alpaca 포맷으로 변환합니다.
        
        Args:
            conversations: 대화 목록
            system_prompt: 시스템 프롬프트 (선택적)
            
        Returns:
            Alpaca 포맷 딕셔너리
        """
        if not conversations:
            raise ValueError("대화 데이터가 비어있습니다")
        
        # 지시문 생성
        instruction_parts = []
        
        # 시스템 프롬프트 추가
        if system_prompt:
            instruction_parts.append(system_prompt)
        
        # 사용자 메시지 추출
        human_messages = [conv["value"] for conv in conversations if conv["from"] == "human"]
        if human_messages:
            instruction_parts.append(human_messages[0])
        
        # 지시문 조합
        instruction = "\n".join(instruction_parts)
        
        # 응답 추출 (마지막 gpt 메시지)
        gpt_messages = [conv["value"] for conv in conversations if conv["from"] == "gpt"]
        output = gpt_messages[-1] if gpt_messages else ""
        
        # 입력 텍스트 생성 (중간 대화 내용)
        input_parts = []
        for conv in conversations[1:-1]:  # 첫 human과 마지막 gpt 제외
            if conv["from"] in ["human", "gpt"]:
                input_parts.append(f"{conv['from']}: {conv['value']}")
        
        input_text = "\n".join(input_parts) if input_parts else None
        
        return self.format_sample(
            instruction=instruction,
            output=output,
            input_text=input_text
        )
    
    def validate_format(self, data: Dict[str, Any]) -> bool:
        """
        Alpaca 포맷 유효성을 검증합니다.
        
        Args:
            data: 검증할 데이터
            
        Returns:
            유효성 검증 결과
        """
        if not isinstance(data, dict):
            return False
        
        # 필수 필드 확인
        required_fields = ["instruction", "output"]
        for field in required_fields:
            if field not in data:
                return False
            if not isinstance(data[field], str):
                return False
        
        # 선택 필드 확인
        if "input" in data and not isinstance(data["input"], str):
            return False
        
        # 길이 검증
        if len(data["instruction"]) > self.config.max_instruction_length:
            return False
        
        if "input" in data and len(data["input"]) > self.config.max_input_length:
            return False
        
        if len(data["output"]) > self.config.max_output_length:
            return False
        
        # 토큰 수 검증
        total_tokens = self._calculate_total_tokens(data)
        if total_tokens > 8192:  # Alpaca 최대 토큰 수
            self.logger.warning(f"최대 토큰 수 초과: {total_tokens} > 4096")
        
        return True
    
    def _normalize_text(self, text: str) -> str:
        """텍스트를 정규화합니다."""
        if not text:
            return ""
        
        text = text.strip()
        
        if self.config.normalize_whitespace:
            # 여러 공백을 단일 공백으로
            text = re.sub(r'\s+', ' ', text)
        
        if self.config.remove_special_chars:
            # 특수 문자 제거 (필요한 기호는 유지)
            text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)\[\]\{\}\"\'\/\@\#\$\%\^\&\*\+\=\~\`]', '', text)
        
        return text
    
    def _add_eos_token(self, text: str) -> str:
        """EOS 토큰을 추가합니다."""
        if not text.endswith(self.config.eos_token):
            return text + self.config.eos_token
        return text
    
    def _calculate_total_tokens(self, sample: Dict[str, str]) -> int:
        """샘플의 총 토큰 수를 계산합니다."""
        # 간단한 토큰 계산 (실제 구현에서는 토크나이저 사용)
        total_chars = (
            len(sample.get("instruction", "")) +
            len(sample.get("input", "")) +
            len(sample.get("output", ""))
        )
        # 평균 토큰 길이를 4로 가정
        return total_chars // 4
    
    def get_format_info(self) -> Dict[str, Any]:
        """포맷 정보를 반환합니다."""
        return {
            "name": "Alpaca",
            "description": "instruction/input/output 구조의 Alpaca 포맷",
            "required_fields": ["instruction", "output"],
            "optional_fields": ["input"],
            "features": [
                "간결한 instruction 구조",
                "선택적 input 지원",
                "명확한 output 형식",
                "EOS 토큰 자동 추가",
                "길이 제한 검증"
            ],
            "max_instruction_length": self.config.max_instruction_length,
            "max_input_length": self.config.max_input_length,
            "max_output_length": self.config.max_output_length,
            "max_total_tokens": 4096
        }


def create_alpaca_formatter(**kwargs) -> AlpacaFormatter:
    """
    Alpaca 포맷터를 생성합니다.
    
    Args:
        **kwargs: 포맷터 설정
        
    Returns:
        AlpacaFormatter 인스턴스
    """
    config = AlpacaConfig(**kwargs)
    return AlpacaFormatter(config)


if __name__ == "__main__":
    # 테스트용 샘플 데이터
    test_samples = [
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
            "input": "초보자도 이해할 수 있도록 단계별로 설명해주세요.",
            "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용",
            "source": "documentation",
            "quality_score": 0.9
        },
        {
            "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
            "output": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가",
            "source": "tutorial",
            "quality_score": 0.8
        }
    ]
    
    # 대화 형식 테스트 데이터
    test_conversation = [
        {"from": "system", "value": "Syncfusion WinForms 전문가"},
        {"from": "human", "value": "DataGrid 사용법 설명"},
        {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."},
        {"from": "human", "value": "데이터 바인딩은 어떻게 하나요?"},
        {"from": "gpt", "value": "데이터 바인딩은..."}
    ]
    
    # 포맷터 생성 및 테스트
    formatter = create_alpaca_formatter()
    
    print("=== Alpaca Formatter Test ===")
    print(f"Format info: {formatter.get_format_info()}")
    
    # 단일 샘플 테스트
    single_result = formatter.format_sample(
        instruction="테스트 지시문",
        output="테스트 응답",
        input_text="테스트 입력"
    )
    print(f"\nSingle sample format: {json.dumps(single_result, indent=2, ensure_ascii=False)}")
    
    # 배치 테스트
    batch_result = formatter.format_batch(test_samples)
    print(f"\nBatch format result count: {len(batch_result)}")
    
    # 대화 형식 테스트
    conversation_result = formatter.format_from_conversation(test_conversation)
    print(f"\nConversation format: {json.dumps(conversation_result, indent=2, ensure_ascii=False)}")
    
    # 유효성 검증
    is_valid = formatter.validate_format(single_result)
    print(f"\nValidation result: {is_valid}")