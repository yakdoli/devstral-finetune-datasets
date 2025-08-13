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
        
        # Syncfusion WinForms 전용 프롬프트 템플릿
        self.templates = {
            "system": self.config.system_prompt_template,
            "system_detailed": """당신은 Syncfusion WinForms 전문가입니다. 다음 지침을 따라 답변해주세요:
1. 정확하고 실용적인 정보를 제공하세요
2. 코드 예시는 C# WinForms 기반으로 작성하세요
3. 단계별 설명을 포함하세요
4. 일반적인 문제와 해결책을 언급하세요
5. 최신 버전의 Syncfusion 기능을 반영하세요""",
            
            "question_generation": """다음 Syncfusion WinForms 문서를 기반으로 실제 개발자가 궁금해할 만한 자연스러운 질문을 생성해주세요:

문서 내용: {content}
컴포넌트: {component}

질문은 다음 유형 중 하나여야 합니다:
- 기본 사용법 문의
- 고급 기능 활용법
- 문제 해결 방법
- 성능 최적화
- 커스터마이징 방법""",
            
            "answer_generation": """다음 Syncfusion WinForms 문서 내용을 바탕으로 전문적이고 실용적인 답변을 생성해주세요:

문서 내용: {content}
컴포넌트: {component}
질문 유형: {question_type}

답변에 포함할 요소:
1. 명확한 설명
2. C# 코드 예시 (가능한 경우)
3. 주의사항 또는 팁
4. 관련 속성이나 메서드 언급""",
            
            "code_example": """다음 요구사항에 맞는 Syncfusion WinForms C# 코드 예시를 생성해주세요:

요구사항: {requirement}
컴포넌트: {component}

코드는 다음을 포함해야 합니다:
1. 필요한 using 문
2. 컴포넌트 초기화
3. 주요 속성 설정
4. 이벤트 핸들러 (필요한 경우)
5. 주석으로 설명""",
            
            "conversation_starter": """다음 Syncfusion WinForms 컴포넌트에 대한 대화를 시작하는 자연스러운 질문을 생성해주세요:

컴포넌트: {component}
문서 내용: {content}
난이도: {difficulty}

질문은 실제 개발 상황에서 나올 법한 것이어야 합니다.""",
            
            "follow_up": """이전 대화를 바탕으로 자연스러운 후속 질문을 생성해주세요:

이전 질문: {previous_question}
이전 답변: {previous_answer}
컴포넌트: {component}

후속 질문은 다음 중 하나여야 합니다:
- 더 구체적인 사용법 문의
- 관련 기능에 대한 질문
- 실제 구현 시 발생할 수 있는 문제
- 성능이나 최적화 관련 질문"""
        }
    
    def generate_system_prompt(self) -> str:
        """시스템 프롬프트 생성"""
        return self.templates["system"]
    
    def generate_question_prompt(self, content: str, component: str = "GridControl") -> str:
        """질문 생성 프롬프트"""
        return self.templates["question_generation"].format(content=content, component=component)
    
    def generate_answer_prompt(self, content: str, component: str = "GridControl") -> str:
        """답변 생성 프롬프트"""
        return self.templates["answer_generation"].format(
            content=content, 
            component=component, 
            question_type="basic"
        )
    
    def generate_code_example_prompt(self, requirement: str, component: str = "GridControl") -> str:
        """코드 예시 생성 프롬프트"""
        return self.templates["code_example"].format(requirement=requirement, component=component)
    
    def generate_conversation_prompt(self, document: Dict[str, Any]) -> List[Dict[str, str]]:
        """대화 프롬프트 생성"""
        prompts = []
        
        # 시스템 프롬프트 (상세 버전 사용)
        prompts.append({
            "role": "system",
            "content": self.templates["system_detailed"]
        })
        
        # 문서 정보 추출
        content = document.get('content', '')
        component = document.get('component', 'GridControl')
        difficulty = document.get('difficulty', 'Intermediate')
        
        # component가 None이거나 비어있는 경우 기본값 사용
        if not component or component == 'None':
            component = 'GridControl'
        
        # 컨텍스트 기반 동적 질문 생성
        starter_prompt = self.templates["conversation_starter"].format(
            component=component,
            content=content[:500] if content else f"{component} 컴포넌트 사용법",
            difficulty=difficulty
        )
        
        # 첫 번째 질문 생성을 위한 프롬프트
        prompts.append({
            "role": "user",
            "content": f"{component} 컴포넌트를 처음 사용하는데, 기본적인 설정 방법과 주요 속성들에 대해 알고 싶습니다."
        })
        
        return prompts
    
    def generate_contextual_question(self, document: Dict[str, Any], question_type: str = "basic") -> str:
        """컨텍스트 기반 질문 생성"""
        component = document.get('component', 'GridControl')
        content = document.get('content', '')
        
        question_templates = {
            "basic": f"{component}의 기본 사용법과 초기 설정 방법을 알려주세요.",
            "advanced": f"{component}의 고급 기능과 커스터마이징 옵션에 대해 설명해주세요.",
            "troubleshooting": f"{component} 사용 중 자주 발생하는 문제와 해결 방법을 알려주세요.",
            "performance": f"{component}의 성능을 최적화하는 방법과 모범 사례를 알려주세요.",
            "integration": f"{component}를 다른 컴포넌트와 함께 사용할 때 주의사항이 있나요?"
        }
        
        return question_templates.get(question_type, question_templates["basic"])
    
    def generate_contextual_answer(self, document: Dict[str, Any], question: str, question_type: str = "basic") -> str:
        """컨텍스트 기반 답변 생성 프롬프트"""
        component = document.get('component', 'GridControl')
        content = document.get('content', '')
        
        return self.templates["answer_generation"].format(
            content=content[:1000] if content else f"{component} 관련 정보",
            component=component,
            question_type=question_type
        )
    
    def generate_follow_up_question(self, previous_qa: Dict[str, str], document: Dict[str, Any]) -> str:
        """후속 질문 생성"""
        component = document.get('component', 'GridControl')
        
        return self.templates["follow_up"].format(
            previous_question=previous_qa.get('question', ''),
            previous_answer=previous_qa.get('answer', '')[:500],  # 답변 길이 제한
            component=component
        )
    
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
    
    def create_multi_turn_conversation(
        self,
        document: Dict[str, Any],
        target_turns: int = None
    ) -> List[Dict[str, str]]:
        """다중 턴 대화 생성"""
        if target_turns is None:
            target_turns = self.config.max_turns
        
        conversation = []
        component = document.get('component', 'GridControl')
        
        # 시스템 프롬프트
        conversation.append({
            "role": "system",
            "content": self.templates["system_detailed"]
        })
        
        # 질문 유형들을 순환하며 대화 생성
        question_types = ["basic", "advanced", "troubleshooting", "performance", "integration"]
        
        for i in range(min(target_turns // 2, len(question_types))):
            question_type = question_types[i % len(question_types)]
            
            # 사용자 질문
            question = self.generate_contextual_question(document, question_type)
            conversation.append({
                "role": "user",
                "content": question
            })
            
            # 어시스턴트 답변을 위한 프롬프트 (실제 답변은 LLM이 생성)
            answer_prompt = self.generate_contextual_answer(document, question, question_type)
            conversation.append({
                "role": "assistant",
                "content": f"{component}에 대한 {question_type} 질문에 대한 전문적인 답변을 제공하겠습니다."
            })
        
        return conversation
    
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
            
            for doc in batch:
                if mode == "multi_turn":
                    prompts = self.create_multi_turn_conversation(doc, target_turns)
                else:
                    prompts = self.generate_conversation_prompt(doc)
                batch_prompts.append(prompts)
        
        return batch_prompts
    
    def get_component_specific_templates(self, component: str) -> Dict[str, str]:
        """컴포넌트별 특화 템플릿 반환"""
        component_templates = {
            "GridControl": {
                "intro": "GridControl은 Syncfusion WinForms의 강력한 데이터 그리드 컴포넌트입니다.",
                "key_features": "데이터 바인딩, 정렬, 필터링, 그룹화, 편집 기능을 제공합니다.",
                "common_issues": "DataSource 설정, 컬럼 매핑, 성능 최적화가 주요 고려사항입니다."
            },
            "ChartControl": {
                "intro": "ChartControl은 다양한 차트 유형을 지원하는 시각화 컴포넌트입니다.",
                "key_features": "2D/3D 차트, 실시간 업데이트, 인터랙티브 기능을 제공합니다.",
                "common_issues": "데이터 시리즈 설정, 축 구성, 성능 최적화가 중요합니다."
            },
            "TreeViewAdv": {
                "intro": "TreeViewAdv는 계층적 데이터를 표시하는 고급 트리뷰 컴포넌트입니다.",
                "key_features": "체크박스, 이미지, 커스텀 노드, 드래그앤드롭을 지원합니다.",
                "common_issues": "노드 관리, 이벤트 처리, 성능 최적화가 핵심입니다."
            }
        }
        
        return component_templates.get(component, component_templates["GridControl"])
    
    def validate_prompt_quality(self, prompt: str) -> Dict[str, Any]:
        """프롬프트 품질 검증"""
        quality_metrics = {
            "length": len(prompt),
            "has_component": any(comp in prompt for comp in ["GridControl", "ChartControl", "TreeViewAdv"]),
            "has_code_context": "C#" in prompt or "코드" in prompt,
            "has_specific_terms": any(term in prompt for term in ["속성", "메서드", "이벤트", "설정"]),
            "is_question_format": "?" in prompt or "알려주세요" in prompt or "설명해주세요" in prompt
        }
        
        # 품질 점수 계산 (0-100)
        score = 0
        if 50 <= quality_metrics["length"] <= 500:
            score += 20
        if quality_metrics["has_component"]:
            score += 25
        if quality_metrics["has_code_context"]:
            score += 20
        if quality_metrics["has_specific_terms"]:
            score += 20
        if quality_metrics["is_question_format"]:
            score += 15
        
        quality_metrics["score"] = score
        quality_metrics["is_high_quality"] = score >= 70
        
        return quality_metrics


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