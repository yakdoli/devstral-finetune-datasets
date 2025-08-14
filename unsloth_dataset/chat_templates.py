#!/usr/bin/env python3
"""
Unsloth 호환 채팅 템플릿 매핑 시스템
Unsloth의 get_chat_template 기능을 참조하여 구현
"""

import logging
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class ChatTemplateType(Enum):
    """지원되는 채팅 템플릿 타입"""
    CHATML = "chatml"
    ZEPHYR = "zephyr"
    MISTRAL = "mistral"
    LLAMA = "llama"
    ALPACA = "alpaca"
    VICUNA = "vicuna"
    VICUNA_OLD = "vicuna_old"
    UNSLOTH = "unsloth"
    SHAREGPT = "sharegpt"
    OPENAI = "openai"


@dataclass
class ChatTemplateConfig:
    """채팅 템플릿 설정"""
    template_type: Union[str, ChatTemplateType]
    mapping: Optional[Dict[str, str]] = None
    map_eos_token: bool = True
    add_generation_prompt: bool = False
    system_message: Optional[str] = None
    custom_template: Optional[str] = None
    eos_token: str = "</s>"


class UnslothChatTemplateManager:
    """Unsloth 스타일 채팅 템플릿 관리자"""
    
    def __init__(self):
        self.templates = self._initialize_templates()
        self.default_mappings = self._initialize_default_mappings()
    
    def _initialize_templates(self) -> Dict[str, str]:
        """기본 채팅 템플릿들 초기화"""
        return {
            ChatTemplateType.CHATML.value: (
                "{% if messages[0]['role'] == 'system' %}"
                "{% set system_message = messages[0]['content'] %}"
                "{% set messages = messages[1:] %}"
                "{% else %}"
                "{% set system_message = 'You are a helpful assistant.' %}"
                "{% endif %}"
                "{% for message in messages %}"
                "{% if message['role'] == 'user' %}"
                "<|im_start|>user\n{{ message['content'] }}<|im_end|>\n"
                "{% elif message['role'] == 'assistant' %}"
                "<|im_start|>assistant\n{{ message['content'] }}<|im_end|>\n"
                "{% endif %}"
                "{% endfor %}"
                "{% if add_generation_prompt %}"
                "<|im_start|>assistant\n"
                "{% endif %}"
            ),
            
            ChatTemplateType.ZEPHYR.value: (
                "{% for message in messages %}"
                "{% if message['role'] == 'user' %}"
                "<|user|>\n{{ message['content'] }}</s>\n"
                "{% elif message['role'] == 'assistant' %}"
                "<|assistant|>\n{{ message['content'] }}</s>\n"
                "{% elif message['role'] == 'system' %}"
                "<|system|>\n{{ message['content'] }}</s>\n"
                "{% endif %}"
                "{% endfor %}"
                "{% if add_generation_prompt %}"
                "<|assistant|>\n"
                "{% endif %}"
            ),
            
            ChatTemplateType.LLAMA.value: (
                "{% if messages[0]['role'] == 'system' %}"
                "{% set system_message = messages[0]['content'] %}"
                "{% set messages = messages[1:] %}"
                "{% else %}"
                "{% set system_message = 'You are a helpful assistant.' %}"
                "{% endif %}"
                "{% for message in messages %}"
                "{% if message['role'] == 'user' %}"
                "[INST] {{ message['content'] }} [/INST]"
                "{% elif message['role'] == 'assistant' %}"
                "{{ message['content'] }}</s>"
                "{% endif %}"
                "{% endfor %}"
                "{% if add_generation_prompt %}"
                "[INST] "
                "{% endif %}"
            ),
            
            ChatTemplateType.ALPACA.value: (
                "{% for message in messages %}"
                "{% if message['role'] == 'user' %}"
                "### Instruction:\n{{ message['content'] }}\n\n"
                "{% elif message['role'] == 'assistant' %}"
                "### Response:\n{{ message['content'] }}\n\n"
                "{% elif message['role'] == 'system' %}"
                "{{ message['content'] }}\n\n"
                "{% endif %}"
                "{% endfor %}"
                "{% if add_generation_prompt %}"
                "### Response:\n"
                "{% endif %}"
            ),
            
            ChatTemplateType.VICUNA.value: (
                "{% if messages[0]['role'] == 'system' %}"
                "{{ messages[0]['content'] }}\n\n"
                "{% set messages = messages[1:] %}"
                "{% endif %}"
                "{% for message in messages %}"
                "{% if message['role'] == 'user' %}"
                "USER: {{ message['content'] }}\n"
                "{% elif message['role'] == 'assistant' %}"
                "ASSISTANT: {{ message['content'] }}</s>\n"
                "{% endif %}"
                "{% endfor %}"
                "{% if add_generation_prompt %}"
                "ASSISTANT: "
                "{% endif %}"
            ),
            
            ChatTemplateType.UNSLOTH.value: (
                "{{ bos_token }}"
                "{{ 'You are a helpful assistant to the user\\n' }}"
                "{% for message in messages %}"
                "{% if message['role'] == 'user' %}"
                "{{ '>>> User: ' + message['content'] + '\\n' }}"
                "{% elif message['role'] == 'assistant' %}"
                "{{ '>>> Assistant: ' + message['content'] + eos_token + '\\n' }}"
                "{% endif %}"
                "{% endfor %}"
                "{% if add_generation_prompt %}"
                "{{ '>>> Assistant: ' }}"
                "{% endif %}"
            ),
            
            ChatTemplateType.SHAREGPT.value: (
                "{% for message in messages %}"
                "{% if message['role'] == 'system' %}"
                "{{ message['content'] }}\n\n"
                "{% elif message['role'] == 'human' or message['role'] == 'user' %}"
                "Human: {{ message['content'] }}\n\n"
                "{% elif message['role'] == 'gpt' or message['role'] == 'assistant' %}"
                "Assistant: {{ message['content'] }}\n\n"
                "{% endif %}"
                "{% endfor %}"
                "{% if add_generation_prompt %}"
                "Assistant: "
                "{% endif %}"
            ),
            
            ChatTemplateType.OPENAI.value: (
                "{% for message in messages %}"
                "{% if message['role'] == 'system' %}"
                "System: {{ message['content'] }}\n\n"
                "{% elif message['role'] == 'user' %}"
                "User: {{ message['content'] }}\n\n"
                "{% elif message['role'] == 'assistant' %}"
                "Assistant: {{ message['content'] }}\n\n"
                "{% endif %}"
                "{% endfor %}"
                "{% if add_generation_prompt %}"
                "Assistant: "
                "{% endif %}"
            )
        }
    
    def _initialize_default_mappings(self) -> Dict[str, Dict[str, str]]:
        """기본 필드 매핑들 초기화"""
        return {
            "sharegpt": {
                "role": "from",
                "content": "value",
                "user": "human",
                "assistant": "gpt"
            },
            "openai": {
                "role": "role",
                "content": "content",
                "user": "user",
                "assistant": "assistant"
            },
            "alpaca": {
                "instruction": "instruction",
                "input": "input",
                "output": "output"
            }
        }
    
    def get_chat_template(
        self,
        template_type: Union[str, ChatTemplateType],
        mapping: Optional[Dict[str, str]] = None,
        map_eos_token: bool = True,
        custom_template: Optional[Union[str, Tuple[str, str]]] = None
    ) -> Tuple[str, Dict[str, str]]:
        """
        Unsloth 스타일 채팅 템플릿 가져오기
        
        Args:
            template_type: 템플릿 타입
            mapping: 필드 매핑 딕셔너리
            map_eos_token: EOS 토큰 매핑 여부
            custom_template: 커스텀 템플릿 (템플릿 문자열 또는 (템플릿, EOS토큰) 튜플)
            
        Returns:
            (템플릿 문자열, 매핑 딕셔너리) 튜플
        """
        if isinstance(template_type, ChatTemplateType):
            template_type = template_type.value
        
        # 커스텀 템플릿 처리
        if custom_template:
            if isinstance(custom_template, tuple):
                template_str, eos_token = custom_template
            else:
                template_str = custom_template
                eos_token = "</s>"
        else:
            # 기본 템플릿 사용
            if template_type not in self.templates:
                raise ValueError(f"지원되지 않는 템플릿 타입: {template_type}")
            
            template_str = self.templates[template_type]
            eos_token = "</s>"
        
        # 매핑 설정
        if mapping is None:
            mapping = self.default_mappings.get(template_type, {})
        
        # EOS 토큰 매핑
        if map_eos_token:
            mapping["eos_token"] = eos_token
        
        return template_str, mapping
    
    def apply_chat_template(
        self,
        conversations: List[Dict[str, Any]],
        template_type: Union[str, ChatTemplateType],
        mapping: Optional[Dict[str, str]] = None,
        add_generation_prompt: bool = False,
        tokenize: bool = False
    ) -> Union[str, List[str]]:
        """
        대화에 채팅 템플릿 적용
        
        Args:
            conversations: 대화 데이터 리스트
            template_type: 템플릿 타입
            mapping: 필드 매핑
            add_generation_prompt: 생성 프롬프트 추가 여부
            tokenize: 토큰화 여부 (현재는 문자열만 반환)
            
        Returns:
            포맷된 텍스트 또는 텍스트 리스트
        """
        template_str, field_mapping = self.get_chat_template(
            template_type=template_type,
            mapping=mapping
        )
        
        if isinstance(conversations[0], list):
            # 여러 대화 처리
            results = []
            for conv in conversations:
                formatted = self._format_single_conversation(
                    conv, template_str, field_mapping, add_generation_prompt
                )
                results.append(formatted)
            return results
        else:
            # 단일 대화 처리
            return self._format_single_conversation(
                conversations, template_str, field_mapping, add_generation_prompt
            )
    
    def _format_single_conversation(
        self,
        conversation: List[Dict[str, Any]],
        template: str,
        mapping: Dict[str, str],
        add_generation_prompt: bool = False
    ) -> str:
        """단일 대화 포맷팅"""
        # 필드 매핑 적용
        mapped_messages = []
        for message in conversation:
            mapped_message = {}
            
            # 역할 매핑
            if "role" in mapping and mapping["role"] in message:
                role = message[mapping["role"]]
                # 역할 값 매핑
                if "user" in mapping and role == mapping["user"]:
                    mapped_message["role"] = "user"
                elif "assistant" in mapping and role == mapping["assistant"]:
                    mapped_message["role"] = "assistant"
                else:
                    mapped_message["role"] = role
            elif "role" in message:
                mapped_message["role"] = message["role"]
            
            # 콘텐츠 매핑
            if "content" in mapping and mapping["content"] in message:
                mapped_message["content"] = message[mapping["content"]]
            elif "content" in message:
                mapped_message["content"] = message["content"]
            
            mapped_messages.append(mapped_message)
        
        # 간단한 템플릿 렌더링 (실제 Jinja2 대신 기본 문자열 처리)
        return self._render_template(template, mapped_messages, add_generation_prompt)
    
    def _render_template(
        self,
        template: str,
        messages: List[Dict[str, Any]],
        add_generation_prompt: bool = False
    ) -> str:
        """간단한 템플릿 렌더링"""
        # 시스템 메시지 처리
        system_message = None
        if messages and messages[0].get("role") == "system":
            system_message = messages[0]["content"]
            messages = messages[1:]
        
        result = ""
        
        # 메시지 처리
        for message in messages:
            role = message.get("role", "")
            content = message.get("content", "")
            
            if role == "user":
                if "chatml" in template.lower():
                    result += f"<|im_start|>user\n{content}<|im_end|>\n"
                elif "zephyr" in template.lower():
                    result += f"<|user|>\n{content}</s>\n"
                elif "llama" in template.lower():
                    result += f"[INST] {content} [/INST]"
                elif "alpaca" in template.lower():
                    result += f"### Instruction:\n{content}\n\n"
                elif "vicuna" in template.lower():
                    result += f"USER: {content}\n"
                elif "unsloth" in template.lower():
                    result += f">>> User: {content}\n"
                elif "sharegpt" in template.lower():
                    result += f"Human: {content}\n\n"
                elif "openai" in template.lower():
                    result += f"User: {content}\n\n"
                else:
                    result += f"User: {content}\n"
            
            elif role == "assistant":
                if "chatml" in template.lower():
                    result += f"<|im_start|>assistant\n{content}<|im_end|>\n"
                elif "zephyr" in template.lower():
                    result += f"<|assistant|>\n{content}</s>\n"
                elif "llama" in template.lower():
                    result += f"{content}</s>"
                elif "alpaca" in template.lower():
                    result += f"### Response:\n{content}\n\n"
                elif "vicuna" in template.lower():
                    result += f"ASSISTANT: {content}</s>\n"
                elif "unsloth" in template.lower():
                    result += f">>> Assistant: {content}</s>\n"
                elif "sharegpt" in template.lower():
                    result += f"Assistant: {content}\n\n"
                elif "openai" in template.lower():
                    result += f"Assistant: {content}\n\n"
                else:
                    result += f"Assistant: {content}\n"
        
        # 생성 프롬프트 추가
        if add_generation_prompt:
            if "chatml" in template.lower():
                result += "<|im_start|>assistant\n"
            elif "zephyr" in template.lower():
                result += "<|assistant|>\n"
            elif "llama" in template.lower():
                result += "[INST] "
            elif "alpaca" in template.lower():
                result += "### Response:\n"
            elif "vicuna" in template.lower():
                result += "ASSISTANT: "
            elif "unsloth" in template.lower():
                result += ">>> Assistant: "
            elif "sharegpt" in template.lower():
                result += "Assistant: "
            elif "openai" in template.lower():
                result += "Assistant: "
            else:
                result += "Assistant: "
        
        return result.strip()
    
    def format_for_training(
        self,
        dataset: List[Dict[str, Any]],
        template_type: Union[str, ChatTemplateType],
        mapping: Optional[Dict[str, str]] = None,
        text_field: str = "text"
    ) -> List[Dict[str, Any]]:
        """
        훈련용 데이터셋 포맷팅
        
        Args:
            dataset: 원본 데이터셋
            template_type: 템플릿 타입
            mapping: 필드 매핑
            text_field: 텍스트 필드명
            
        Returns:
            포맷된 데이터셋
        """
        formatted_dataset = []
        
        for item in dataset:
            if "conversations" in item:
                # 대화 형식 데이터
                formatted_text = self.apply_chat_template(
                    conversations=item["conversations"],
                    template_type=template_type,
                    mapping=mapping,
                    add_generation_prompt=False
                )
                
                formatted_item = {
                    text_field: formatted_text,
                    **{k: v for k, v in item.items() if k != "conversations"}
                }
                formatted_dataset.append(formatted_item)
            
            elif "instruction" in item and "output" in item:
                # Alpaca 형식 데이터를 대화 형식으로 변환
                conversations = [
                    {"role": "user", "content": item["instruction"]},
                    {"role": "assistant", "content": item["output"]}
                ]
                
                if item.get("input", "").strip():
                    conversations[0]["content"] = f"{item['instruction']}\n\n{item['input']}"
                
                formatted_text = self.apply_chat_template(
                    conversations=conversations,
                    template_type=template_type,
                    mapping=mapping,
                    add_generation_prompt=False
                )
                
                formatted_item = {
                    text_field: formatted_text,
                    **{k: v for k, v in item.items() if k not in ["instruction", "input", "output"]}
                }
                formatted_dataset.append(formatted_item)
        
        return formatted_dataset


def create_chat_template_manager() -> UnslothChatTemplateManager:
    """채팅 템플릿 관리자 생성"""
    return UnslothChatTemplateManager()


# Unsloth 스타일 편의 함수들
def get_chat_template(
    template_type: Union[str, ChatTemplateType],
    mapping: Optional[Dict[str, str]] = None,
    map_eos_token: bool = True,
    custom_template: Optional[Union[str, Tuple[str, str]]] = None
) -> Tuple[str, Dict[str, str]]:
    """Unsloth 스타일 get_chat_template 함수"""
    manager = create_chat_template_manager()
    return manager.get_chat_template(
        template_type=template_type,
        mapping=mapping,
        map_eos_token=map_eos_token,
        custom_template=custom_template
    )


def format_conversations_for_training(
    dataset: List[Dict[str, Any]],
    template_type: Union[str, ChatTemplateType] = ChatTemplateType.CHATML,
    mapping: Optional[Dict[str, str]] = None,
    text_field: str = "text"
) -> List[Dict[str, Any]]:
    """대화 데이터를 훈련용으로 포맷팅"""
    manager = create_chat_template_manager()
    return manager.format_for_training(
        dataset=dataset,
        template_type=template_type,
        mapping=mapping,
        text_field=text_field
    )


if __name__ == "__main__":
    # 테스트 코드
    manager = create_chat_template_manager()
    
    # 테스트 데이터
    test_conversations = [
        {"from": "human", "value": "Hello, how are you?"},
        {"from": "gpt", "value": "I'm doing well, thank you! How can I help you today?"}
    ]
    
    # ShareGPT 스타일 매핑으로 ChatML 템플릿 적용
    formatted = manager.apply_chat_template(
        conversations=test_conversations,
        template_type=ChatTemplateType.CHATML,
        mapping={"role": "from", "content": "value", "user": "human", "assistant": "gpt"}
    )
    
    print("=== ChatML 포맷 결과 ===")
    print(formatted)
    
    # Alpaca 스타일 테스트
    alpaca_formatted = manager.apply_chat_template(
        conversations=test_conversations,
        template_type=ChatTemplateType.ALPACA,
        mapping={"role": "from", "content": "value", "user": "human", "assistant": "gpt"}
    )
    
    print("\n=== Alpaca 포맷 결과 ===")
    print(alpaca_formatted)