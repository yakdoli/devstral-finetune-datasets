#!/usr/bin/env python3
"""
ShareGPT 포맷터 모듈
Unsloth 프레임워크와 호환되는 ShareGPT 포맷 데이터셋을 생성합니다.
"""

import json
import logging
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import re

logger = logging.getLogger(__name__)


@dataclass
class ShareGPTConfig:
    """ShareGPT 포맷터 설정"""
    system_prompt: str = "Syncfusion WinForms 기술 전문가입니다."
    min_turns: int = 1
    max_turns: int = 10
    add_system_message: bool = True
    eos_token: str = "</s>"
    normalize_whitespace: bool = True
    remove_special_chars: bool = True
    max_conversation_length: int = 4096


class ShareGPTFormatter:
    """ShareGPT 포맷 데이터셋 생성기"""
    
    def __init__(self, config: Optional[ShareGPTConfig] = None):
        """
        ShareGPT 포맷터를 초기화합니다.
        
        Args:
            config: ShareGPT 포맷터 설정
        """
        self.config = config or ShareGPTConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
    def format_conversation(
        self, 
        instruction: str, 
        response: str, 
        context: Optional[str] = None,
        turns: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        단일 대화를 ShareGPT 포맷으로 변환합니다.
        
        Args:
            instruction: 사용자 질문/지시
            response: AI 응답
            context: 추가 컨텍스트 (선택적)
            turns: 추가 대화 턴 (선택적)
            
        Returns:
            ShareGPT 포맷 딕셔너리
        """
        # 텍스트 정규화
        instruction = self._normalize_text(instruction)
        response = self._normalize_text(response)
        
        if context:
            context = self._normalize_text(context)
        
        conversations = []
        
        # 시스템 메시지 추가
        if self.config.add_system_message:
            conversations.append({
                "from": "system", 
                "value": self.config.system_prompt
            })
        
        # 컨텍스트가 있는 경우 추가
        if context:
            conversations.append({
                "from": "system",
                "value": f"컨텍스트: {context}"
            })
        
        # 첫 번째 대화 턴
        conversations.append({
            "from": "human",
            "value": instruction
        })
        
        conversations.append({
            "from": "gpt", 
            "value": response
        })
        
        # 추가 대화 턴이 있는 경우 처리
        if turns:
            for turn in turns:
                if "from" in turn and "value" in turn:
                    normalized_turn = {
                        "from": turn["from"],
                        "value": self._normalize_text(turn["value"])
                    }
                    conversations.append(normalized_turn)
        
        # EOS 토큰 추가
        for conv in conversations:
            if conv["from"] in ["human", "gpt"]:
                conv["value"] = self._add_eos_token(conv["value"])
        
        return {
            "conversations": conversations,
            "metadata": {
                "format": "sharegpt",
                "created_at": datetime.now().isoformat(),
                "turns": len(conversations),
                "system_prompt": self.config.system_prompt if self.config.add_system_message else None
            }
        }
    
    def format_batch(
        self, 
        samples: List[Dict[str, Any]], 
        include_metadata: bool = True
    ) -> List[Dict[str, Any]]:
        """
        샘플 배치를 ShareGPT 포맷으로 변환합니다.
        
        Args:
            samples: 샘플 데이터 목록
            include_metadata: 메타데이터 포함 여부
            
        Returns:
            ShareGPT 포맷 데이터 목록
        """
        formatted_samples = []
        
        for i, sample in enumerate(samples):
            try:
                # 필수 필드 확인
                if "instruction" not in sample or "response" not in sample:
                    self.logger.warning(f"Sample {i} 필수 필드 누락: {sample}")
                    continue
                
                # 단일 대화 형식으로 변환
                formatted = self.format_conversation(
                    instruction=sample["instruction"],
                    response=sample["response"],
                    context=sample.get("context"),
                    turns=sample.get("turns")
                )
                
                # 메타데이터 처리
                if include_metadata:
                    formatted["metadata"].update({
                        "sample_index": i,
                        "source": sample.get("source", "unknown"),
                        "quality_score": sample.get("quality_score", 1.0),
                        "token_count": self._calculate_total_tokens(formatted["conversations"])
                    })
                else:
                    del formatted["metadata"]
                
                formatted_samples.append(formatted)
                
            except Exception as e:
                self.logger.error(f"Sample {i} 처리 실패: {e}")
                continue
        
        return formatted_samples
    
    def validate_format(self, data: Dict[str, Any]) -> bool:
        """
        ShareGPT 포맷 유효성을 검증합니다.
        
        Args:
            data: 검증할 데이터
            
        Returns:
            유효성 검증 결과
        """
        if not isinstance(data, dict):
            return False
        
        if "conversations" not in data:
            return False
        
        conversations = data["conversations"]
        if not isinstance(conversations, list):
            return False
        
        # 대화 구조 검증
        valid_roles = {"system", "human", "gpt"}
        for i, conv in enumerate(conversations):
            if not isinstance(conv, dict):
                return False
            
            if "from" not in conv or "value" not in conv:
                return False
            
            if conv["from"] not in valid_roles:
                return False
            
            if not isinstance(conv["value"], str):
                return False
        
        # 토큰 수 검증
        total_tokens = self._calculate_total_tokens(conversations)
        if total_tokens > self.config.max_conversation_length:
            self.logger.warning(f"최대 대화 길이 초과: {total_tokens} > {self.config.max_conversation_length}")
        
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
    
    def _calculate_total_tokens(self, conversations: List[Dict[str, str]]) -> int:
        """대화의 총 토큰 수를 계산합니다."""
        # 간단한 토큰 계산 (실제 구현에서는 토크나이저 사용)
        total_chars = sum(len(conv["value"]) for conv in conversations)
        # 평균 토큰 길이를 4로 가정
        return total_chars // 4
    
    def get_format_info(self) -> Dict[str, Any]:
        """포맷 정보를 반환합니다."""
        return {
            "name": "ShareGPT",
            "description": "다중 턴 대화 형식의 ShareGPT 포맷",
            "required_fields": ["instruction", "response"],
            "optional_fields": ["context", "turns"],
            "features": [
                "다중 턴 대화 지원",
                "시스템 프롬프트 지원",
                "컨텍스트 정보 지원",
                "EOS 토큰 자동 추가",
                "메타데이터 포함"
            ],
            "max_conversation_length": self.config.max_conversation_length,
            "supported_roles": ["system", "human", "gpt"]
        }


def create_sharegpt_formatter(**kwargs) -> ShareGPTFormatter:
    """
    ShareGPT 포맷터를 생성합니다.
    
    Args:
        **kwargs: 포맷터 설정
        
    Returns:
        ShareGPTFormatter 인스턴스
    """
    config = ShareGPTConfig(**kwargs)
    return ShareGPTFormatter(config)


if __name__ == "__main__":
    # 테스트용 샘플 데이터
    test_samples = [
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 알려주세요.",
            "response": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용",
            "context": "WinForms 애플리케이션 개발",
            "source": "documentation"
        },
        {
            "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
            "response": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가",
            "source": "tutorial"
        }
    ]
    
    # 포맷터 생성 및 테스트
    formatter = create_sharegpt_formatter()
    
    print("=== ShareGPT Formatter Test ===")
    print(f"Format info: {formatter.get_format_info()}")
    
    # 단일 샘플 테스트
    single_result = formatter.format_conversation(
        instruction="테스트 질문",
        response="테스트 응답"
    )
    print(f"\nSingle conversation format: {json.dumps(single_result, indent=2, ensure_ascii=False)}")
    
    # 배치 테스트
    batch_result = formatter.format_batch(test_samples)
    print(f"\nBatch format result count: {len(batch_result)}")
    
    # 유효성 검증
    is_valid = formatter.validate_format(single_result)
    print(f"\nValidation result: {is_valid}")