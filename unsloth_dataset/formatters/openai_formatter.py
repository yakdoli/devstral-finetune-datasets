#!/usr/bin/env python3
"""
OpenAI 포맷터 모듈
Unsloth 프레임워크와 호환되는 OpenAI 포맷 데이터셋을 생성합니다.
"""

import json
import logging
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, asdict
from datetime import datetime
import re

logger = logging.getLogger(__name__)


@dataclass
class OpenAIConfig:
    """OpenAI 포맷터 설정"""
    system_role: str = "system"
    user_role: str = "user"
    assistant_role: str = "assistant"
    default_system_prompt: str = "Syncfusion WinForms 전문가"
    eos_token: str = "</s>"
    normalize_whitespace: bool = True
    remove_special_chars: bool = True
    max_message_length: int = 2048
    include_system_message: bool = True
    validate_message_order: bool = True
    quality_threshold: float = 0.5


class OpenAIFormatter:
    """OpenAI 포맷 데이터셋 생성기"""
    
    def __init__(self, config: Optional[OpenAIConfig] = None):
        """
        OpenAI 포맷터를 초기화합니다.
        
        Args:
            config: OpenAI 포맷터 설정
        """
        self.config = config or OpenAIConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
    def format_messages(
        self,
        user_message: str,
        assistant_message: str,
        system_prompt: Optional[str] = None,
        context_messages: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        메시지 배열을 OpenAI 포맷으로 변환합니다.
        
        Args:
            system_prompt: 시스템 프롬프트 (선택적)
            user_message: 사용자 메시지
            assistant_message: 어시스턴트 메시지
            context_messages: 컨텍스트 메시지 목록 (선택적)
            
        Returns:
            OpenAI 포맷 딕셔너리
        """
        # 텍스트 정규화
        user_message = self._normalize_text(user_message)
        assistant_message = self._normalize_text(assistant_message)
        
        messages = []
        
        # 시스템 메시지 추가
        if self.config.include_system_message:
            final_system_prompt = system_prompt or self.config.default_system_prompt
            messages.append({
                "role": self.config.system_role,
                "content": self._normalize_text(final_system_prompt)
            })
        
        # 컨텍스트 메시지 추가
        if context_messages:
            for msg in context_messages:
                if "role" in msg and "content" in msg:
                    normalized_msg = {
                        "role": msg["role"],
                        "content": self._normalize_text(msg["content"])
                    }
                    messages.append(normalized_msg)
        
        # 사용자 메시지 추가
        messages.append({
            "role": self.config.user_role,
            "content": user_message
        })
        
        # 어시스턴트 메시지 추가
        messages.append({
            "role": self.config.assistant_role,
            "content": assistant_message
        })
        
        # EOS 토큰 추가
        for msg in messages:
            if msg["role"] in [self.config.user_role, self.config.assistant_role]:
                msg["content"] = self._add_eos_token(msg["content"])
        
        return {
            "messages": messages,
            "metadata": {
                "format": "openai",
                "created_at": datetime.now().isoformat(),
                "message_count": len(messages),
                "system_prompt": system_prompt or self.config.default_system_prompt if self.config.include_system_message else None,
                "total_tokens": self._calculate_total_tokens(messages)
            }
        }
    
    def format_batch(
        self, 
        samples: List[Dict[str, Any]], 
        include_metadata: bool = True
    ) -> List[Dict[str, Any]]:
        """
        샘플 배치를 OpenAI 포맷으로 변환합니다.
        
        Args:
            samples: 샘플 데이터 목록
            include_metadata: 메타데이터 포함 여부
            
        Returns:
            OpenAI 포맷 데이터 목록
        """
        formatted_samples = []
        
        for i, sample in enumerate(samples):
            try:
                # 필수 필드 확인
                if "user_message" not in sample or "assistant_message" not in sample:
                    self.logger.warning(f"Sample {i} 필수 필드 누락: {sample}")
                    continue
                
                # 품질 점수 검증
                quality_score = sample.get("quality_score", 1.0)
                if quality_score < self.config.quality_threshold:
                    self.logger.warning(f"Sample {i} 품질 점수 낮음: {quality_score}")
                    continue
                
                # OpenAI 포맷으로 변환
                formatted = self.format_messages(
                    system_prompt=sample.get("system_prompt"),
                    user_message=sample["user_message"],
                    assistant_message=sample["assistant_message"],
                    context_messages=sample.get("context_messages")
                )
                
                # 메타데이터 처리
                if include_metadata:
                    formatted["metadata"].update({
                        "sample_index": i,
                        "source": sample.get("source", "unknown"),
                        "original_quality_score": quality_score,
                        "has_context": "context_messages" in sample,
                        "instruction": sample.get("instruction"),
                        "input": sample.get("input")
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
        conversations: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """
        대화 형식의 데이터를 OpenAI 포맷으로 변환합니다.
        
        Args:
            conversations: 대화 목록
            
        Returns:
            OpenAI 포맷 딕셔너리
        """
        if not conversations:
            raise ValueError("대화 데이터가 비어있습니다")
        
        # 메시지 역할 매핑
        role_mapping = {
            "system": self.config.system_role,
            "human": self.config.user_role,
            "gpt": self.config.assistant_role
        }
        
        messages = []
        system_prompt = None
        
        # 대화 메시지 변환
        for conv in conversations:
            if "from" not in conv or "value" not in conv:
                continue
            
            original_role = conv["from"]
            if original_role in role_mapping:
                new_role = role_mapping[original_role]
                content = conv["value"]
                
                # 시스템 프롬프트 분리
                if new_role == self.config.system_role:
                    system_prompt = content
                else:
                    messages.append({
                        "role": new_role,
                        "content": content
                    })
        
        # 마지막 어시스턴트 메시지 분리
        user_message = ""
        assistant_message = ""
        
        if len(messages) >= 2:
            # 마지막 두 메시지 추출
            last_two = messages[-2:]
            if len(last_two) == 2:
                user_message = last_two[0]["content"] if last_two[0]["role"] == self.config.user_role else ""
                assistant_message = last_two[1]["content"] if last_two[1]["role"] == self.config.assistant_role else ""
        
        # 이전 메시지를 컨텍스트로 사용
        context_messages = messages[:-2] if len(messages) > 2 else None
        
        return self.format_messages(
            system_prompt=system_prompt,
            user_message=user_message,
            assistant_message=assistant_message,
            context_messages=context_messages
        )
    
    def validate_format(self, data: Dict[str, Any]) -> bool:
        """
        OpenAI 포맷 유효성을 검증합니다.
        
        Args:
            data: 검증할 데이터
            
        Returns:
            유효성 검증 결과
        """
        if not isinstance(data, dict):
            return False
        
        if "messages" not in data:
            return False
        
        messages = data["messages"]
        if not isinstance(messages, list):
            return False
        
        # 메시지 구조 검증
        valid_roles = {self.config.system_role, self.config.user_role, self.config.assistant_role}
        for i, msg in enumerate(messages):
            if not isinstance(msg, dict):
                return False
            
            if "role" not in msg or "content" not in msg:
                return False
            
            if msg["role"] not in valid_roles:
                return False
            
            if not isinstance(msg["content"], str):
                return False
            
            # 길이 검증
            if len(msg["content"]) > self.config.max_message_length:
                return False
        
        # 메시지 순서 검증
        if self.config.validate_message_order:
            if not self._validate_message_order(messages):
                return False
        
        # 최소 메시지 수 검증
        if len(messages) < 2:  # 최소 user + assistant
            return False
        
        # 토큰 수 검증
        total_tokens = self._calculate_total_tokens(messages)
        if total_tokens > 4096:
            self.logger.warning(f"최대 토큰 수 초과: {total_tokens} > 4096")
        
        return True
    
    def _validate_message_order(self, messages: List[Dict[str, str]]) -> bool:
        """메시지 순서 유효성을 검증합니다."""
        if not messages:
            return False
        
        # 첫 번째 메시지가 시스템인지 확인
        if messages[0]["role"] == self.config.system_role:
            remaining = messages[1:]
        else:
            remaining = messages
        
        # user/assistant 순서 검증
        expected_role = self.config.user_role
        for msg in remaining:
            if msg["role"] != expected_role:
                return False
            expected_role = self.config.assistant_role if expected_role == self.config.user_role else self.config.user_role
        
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
    
    def _calculate_total_tokens(self, messages: List[Dict[str, str]]) -> int:
        """메시지의 총 토큰 수를 계산합니다."""
        # 간단한 토큰 계산 (실제 구현에서는 토크나이저 사용)
        total_chars = sum(len(msg["content"]) for msg in messages)
        # 평균 토큰 길이를 4로 가정
        return total_chars // 4
    
    def get_format_info(self) -> Dict[str, Any]:
        """포맷 정보를 반환합니다."""
        return {
            "name": "OpenAI",
            "description": "messages 배열 구조의 OpenAI 포맷",
            "required_fields": ["user_message", "assistant_message"],
            "optional_fields": ["system_prompt", "context_messages"],
            "features": [
                "유연한 메시지 배열 구조",
                "시스템 프롬프트 지원",
                "컨텍스트 메시지 지원",
                "역할 기반 메시지 구조",
                "EOS 토큰 자동 추가",
                "메시지 순서 검증"
            ],
            "max_message_length": self.config.max_message_length,
            "max_total_tokens": 4096,
            "supported_roles": [self.config.system_role, self.config.user_role, self.config.assistant_role]
        }


def create_openai_formatter(**kwargs) -> OpenAIFormatter:
    """
    OpenAI 포맷터를 생성합니다.
    
    Args:
        **kwargs: 포맷터 설정
        
    Returns:
        OpenAIFormatter 인스턴스
    """
    config = OpenAIConfig(**kwargs)
    return OpenAIFormatter(config)


if __name__ == "__main__":
    # 테스트용 샘플 데이터
    test_samples = [
        {
            "user_message": "Syncfusion WinForms DataGrid 사용법을 알려주세요.",
            "assistant_message": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용",
            "system_prompt": "Syncfusion WinForms 기술 전문가",
            "source": "documentation",
            "quality_score": 0.9
        },
        {
            "user_message": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
            "assistant_message": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가",
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
    formatter = create_openai_formatter()
    
    print("=== OpenAI Formatter Test ===")
    print(f"Format info: {formatter.get_format_info()}")
    
    # 단일 샘플 테스트
    single_result = formatter.format_messages(
        user_message="테스트 사용자 메시지",
        assistant_message="테스트 어시스턴트 메시지",
        system_prompt="테스트 시스템 프롬프트"
    )
    print(f"\nSingle messages format: {json.dumps(single_result, indent=2, ensure_ascii=False)}")
    
    # 배치 테스트
    batch_result = formatter.format_batch(test_samples)
    print(f"\nBatch format result count: {len(batch_result)}")
    
    # 대화 형식 테스트
    conversation_result = formatter.format_from_conversation(test_conversation)
    print(f"\nConversation format: {json.dumps(conversation_result, indent=2, ensure_ascii=False)}")
    
    # 유효성 검증
    is_valid = formatter.validate_format(single_result)
    print(f"\nValidation result: {is_valid}")