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
    system_prompt_template: str = "You are a Syncfusion WinForms expert. Please provide accurate and helpful answers to user questions."
    
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
    system_prompt_template: str = "You are a Syncfusion WinForms expert. Please provide accurate and helpful answers to user questions."
    
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
            "system_detailed": """You are a Syncfusion WinForms expert. Please follow these guidelines when answering:
1. Provide accurate and practical information
2. Write code examples based on C# WinForms
3. Include step-by-step explanations
4. Mention common problems and solutions
5. Reflect the latest Syncfusion features""",
            
            "question_generation": """Based on the following Syncfusion WinForms documentation, please generate natural questions that actual developers would be curious about:

Document content: {content}
Component: {component}

The question should be one of the following types:
- Basic usage inquiry
- Advanced feature utilization
- Problem solving methods
- Performance optimization
- Customization methods""",
            
            "answer_generation": """Based on the following Syncfusion WinForms documentation content, please generate professional and practical answers:

Document content: {content}
Component: {component}
Question type: {question_type}

Elements to include in the answer:
1. Clear explanation
2. C# code examples (when possible)
3. Precautions or tips
4. Mention related properties or methods""",
            
            "code_example": """Please generate a Syncfusion WinForms C# code example that meets the following requirements:

Requirements: {requirement}
Component: {component}

The code should include:
1. Required using statements
2. Component initialization
3. Key property settings
4. Event handlers (if needed)
5. Explanatory comments""",
            
            "conversation_starter": """Please generate a natural question to start a conversation about the following Syncfusion WinForms component:

Component: {component}
Document content: {content}
Difficulty: {difficulty}

The question should be something that would come up in actual development situations.""",
            
            "follow_up": """Based on the previous conversation, please generate a natural follow-up question:

Previous question: {previous_question}
Previous answer: {previous_answer}
Component: {component}

The follow-up question should be one of the following:
- More specific usage inquiry
- Questions about related features
- Problems that may occur during actual implementation
- Performance or optimization related questions"""
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
            "content": f"I'm using the {component} component for the first time. I'd like to know about basic setup methods and key properties."
        })
        
        return prompts
    
    def generate_contextual_question(self, document: Dict[str, Any], question_type: str = "basic") -> str:
        """컨텍스트 기반 질문 생성"""
        component = document.get('component', 'GridControl')
        content = document.get('content', '')
        
        question_templates = {
            "basic": f"Please tell me about the basic usage and initial setup methods for {component}.",
            "advanced": f"Please explain the advanced features and customization options of {component}.",
            "troubleshooting": f"Please tell me about common problems and solutions when using {component}.",
            "performance": f"Please tell me about methods and best practices for optimizing {component} performance.",
            "integration": f"Are there any precautions when using {component} with other components?"
        }
        
        return question_templates.get(question_type, question_templates["basic"])
    
    def generate_contextual_answer(self, document: Dict[str, Any], question: str, question_type: str = "basic") -> str:
        """컨텍스트 기반 답변 생성 프롬프트"""
        component = document.get('component', 'GridControl')
        content = document.get('content', '')
        
        return self.templates["answer_generation"].format(
            content=content[:1000] if content else f"{component} related information",
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
                "content": f"Please tell me about the basic usage of the {document.get('component', 'GridControl')} component."
            },
            {
                "role": "assistant",
                "content": f"To use {document.get('component', 'GridControl')}, you first need to add the necessary namespaces, place the component on the form, and then set the DataSource property. The basic setup code follows this order: add namespaces, create component, set DataSource, and configure columns."
            }
        ])
        
        # 예시 2: 오류 해결
        examples.append([
            {
                "role": "user",
                "content": f"I'm having an issue where data is not displaying in {document.get('component', 'GridControl')}. Please tell me how to solve this."
            },
            {
                "role": "assistant", 
                "content": "The issue of data not displaying can occur due to several reasons: you need to check DataSource settings, MappingName settings, AutoGenerateColumns settings, and data source validity."
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
            prompt += "\\n\\nPlease provide specific and detailed answers. It's good to include code examples."
        elif self.config.generation_mode == "concise":
            prompt += "\\n\\nPlease provide concise answers with only essential content."
        
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
                "content": f"I will provide a professional answer to the {question_type} question about {component}."
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
            "has_specific_terms": any(term in prompt for term in ["property", "method", "event", "setting", "속성", "메서드", "이벤트", "설정"]),
            "is_question_format": "?" in prompt or "please" in prompt.lower() or "how" in prompt.lower() or "알려주세요" in prompt or "설명해주세요" in prompt
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