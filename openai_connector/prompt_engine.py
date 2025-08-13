#!/usr/bin/env python3
"""
OpenAI 프롬프트 엔진 모듈

Syncfusion WinForms 문서를 기반으로 고품질의 프롬프트를 생성합니다.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import logging


@dataclass
class PromptConfig:
    """프롬프트 설정"""
    # 시스템 프롬프트 템플릿
    system_prompt_template: str = "당신은 Syncfusion WinForms 전문가입니다. 사용자의 질문에 정확하고 도움이 되는 답변을 제공해주세요."
    
    # 생성 모드
    generation_mode: str = "balanced"  # "detailed", "concise", "balanced"
    
    # 최대 턴 수
    max_turns: int = 10
    
    # 최소 턴 수
    min_turns: int = 3
    
    # 최대 생성 시간 (초)
    max_generation_time: int = 300
    
    # 재시도 횟수
    max_retries: int = 3
    
    # 배치 크기
    batch_size: int = 10


@dataclass
class PromptEngineConfig:
    """프롬프트 엔진 설정"""
    # 시스템 프롬프트 템플릿
    system_prompt_template: str = "당신은 Syncfusion WinForms 전문가입니다. 사용자의 질문에 정확하고 도움이 되는 답변을 제공해주세요."
    
    # 생성 모드
    generation_mode: str = "balanced"  # "detailed", "concise", "balanced"
    
    # 최대 턴 수
    max_turns: int = 10
    
    # 최소 턴 수
    min_turns: int = 3
    
    # 최대 생성 시간 (초)
    max_generation_time: int = 300
    
    # 재시도 횟수
    max_retries: int = 3
    
    # 배치 크기
    batch_size: int = 10


class PromptEngine:
    """프롬프트 엔진 클래스"""
    
    def __init__(self, config: PromptEngineConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # 프롬프트 템플릿
        self.templates = {
            "system": self.config.system_prompt_template,
            "question_generation": "다음 Syncfusion WinForms 문서를 기반으로 자연스러운 질문을 생성해주세요: {content}",
            "answer_generation": "다음 문서 내용을 바탕으로 전문적인 답변을 생성해주세요: {content}",
            "code_example": "다음과 같은 코드 예시를 생성해주세요: {requirement}"
        }
    
    def generate_system_prompt(self) -> str:
        """시스템 프롬프트 생성"""
        return self.templates["system"]
    
    def generate_question_prompt(self, content: str) -> str:
        """질문 생성 프롬프트"""
        return self.templates["question_generation"].format(content=content)
    
    def generate_answer_prompt(self, content: str) -> str:
        """답변 생성 프롬프트"""
        return self.templates["answer_generation"].format(content=content)
    
    def generate_code_example_prompt(self, requirement: str) -> str:
        """코드 예시 생성 프롬프트"""
        return self.templates["code_example"].format(requirement=requirement)
    
    def generate_conversation_prompt(self, document: Dict[str, Any]) -> List[Dict[str, str]]:
        """대화 프롬프트 생성"""
        prompts = []
        
        # 시스템 프롬프트
        prompts.append({
            "role": "system",
            "content": self.generate_system_prompt()
        })
        
        # 문서 내용 기반 질문
        content = document.get('content', '')
        component = document.get('component', 'GridControl')
        
        # component가 None이거나 비어있는 경우 기본값 사용
        if not component or component == 'None':
            component = 'GridControl'
        
        # 항상 프롬프트 생성 (content가 비어있어도)
        prompts.append({
            "role": "user",
            "content": f"{component} 컴포넌트에 대해 자세히 알고 싶습니다."
        })
        
        prompts.append({
            "role": "assistant",
            "content": f"{component}는 Syncfusion WinForms의 강력한 컴포넌트입니다. 기본 사용법부터 고급 기능까지 다양한 방식으로 활용할 수 있습니다. 구체적으로 어떤 기능에 대해 알고 싶으신가요?"
        })
        
        return prompts
    
    def generate_conversation_examples(self, document: Dict[str, Any]) -> List[List[Dict[str, str]]]:
        """대화 예시 생성"""
        examples = []
        
        # 예시 1: 기본 사용법 질의응답
        examples.append([
            {
                "role": "user",
                "content": f"{document.get('component', 'GridControl')} 컴포넌트의 기본 사용법을 알려주세요."
            },
            {
                "role": "assistant",
                "content": f"{document.get('component', 'GridControl')}를 사용하려면 먼저 필요한 네임스페이스를 추가하고, 컴포넌트를 폼에 배치한 후 DataSource 속성을 설정해야 합니다. 기본적인 설정 코드는 다음과 같습니다: 네임스페이스 추가, 컴포넌트 생성, DataSource 설정, 컬럼 설정을 순서대로 진행합니다."
            }
        ])
        
        # 예시 2: 오류 해결
        examples.append([
            {
                "role": "user",
                "content": f"{document.get('component', 'GridControl')}에서 데이터가 표시되지 않는 문제가 발생합니다. 해결 방법을 알려주세요."
            },
            {
                "role": "assistant", 
                "content": "데이터가 표시되지 않는 문제는 여러 가지 원인으로 발생할 수 있습니다: DataSource 설정 확인, MappingName 설정, AutoGenerateColumns 설정, 데이터 소스 유효성 확인 등을 점검해야 합니다."
            }
        ])
        
        return examples
    
    def optimize_prompt(self, prompt: str, document: Dict[str, Any]) -> str:
        """프롬프트 최적화"""
        # 문서 정보 기반 프롬프트 개선
        component = document.get('component', 'GridControl')
        
        # 컴포넌트 특화 프롬프트
        if component:
            prompt = prompt.replace("GridControl", component)
        
        # 품질 향상을 위한 프롬프트 확장
        if self.config.generation_mode == "detailed":
            prompt += "\\n\\n답변은 구체적이고 상세하게 제공해주세요. 코드 예시를 포함하는 것이 좋습니다."
        elif self.config.generation_mode == "concise":
            prompt += "\\n\\n답변은 간결하고 핵심적인 내용만 포함해주세요."
        
        return prompt
    
    def create_batch_prompts(
        self,
        documents: List[Dict[str, Any]],
        target_turns: int = None,
        mode: str = "balanced"
    ) -> List[List[Dict[str, str]]]:
        """배치 프롬프트 생성"""
        batch_prompts = []
        
        for i in range(0, len(documents), self.config.batch_size):
            batch = documents[i:i + self.config.batch_size]
            batch_prompts.extend([self.generate_conversation_prompt(doc) for doc in batch])
        
        return batch_prompts


def create_prompt_engine(config: Optional[PromptEngineConfig] = None) -> PromptEngine:
    """프롬프트 엔진 생성"""
    if config is None:
        config = PromptEngineConfig()
    
    return PromptEngine(config)


# 테스트 코드
if __name__ == "__main__":
    config = PromptEngineConfig()
    engine = create_prompt_engine(config)
    
    # 테스트 문서
    test_document = {
        "component": "GridControl",
        "content": "Syncfusion WinForms GridControl 사용법",
        "metadata": {"category": "DataGrid", "difficulty": "Intermediate"}
    }
    
    # 프롬프트 생성 테스트
    prompts = engine.generate_conversation_prompt(test_document)
    print("생성된 프롬프트:")
    for prompt in prompts:
        print(f"{prompt['role']}: {prompt['content']}")