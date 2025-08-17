#!/usr/bin/env python3
"""
프롬프트 엔진 모듈

로컬 LLM을 위한 최적화된 프롬프트를 생성합니다.
Context7 정보와 결합하여 정확한 응답을 생성합니다.
"""

import logging
import json
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime
import re

logger = logging.getLogger(__name__)


@dataclass
class PromptEngineConfig:
    """프롬프트 엔진 설정"""
    # 기본 설정
    system_prompt: str = "You are a helpful assistant specialized in technical documentation."
    max_prompt_length: int = 4000
    temperature: float = 0.3
    
    # 프롬프트 템플릿
    conversation_prompt_template: str = """
You are an expert assistant specializing in technical documentation and Q&A generation.

Based on the following document content, generate high-quality conversational Q&A pairs.

Document Information:
- Title: {document_title}
- Content: {document_content}

Additional Context:
{context_info}

Requirements:
1. Generate {target_count} diverse and informative Q&A pairs
2. Questions should be clear and specific
3. Answers should be comprehensive and accurate
4. Focus on technical concepts, usage examples, and best practices
5. Include code examples where appropriate
6. Ensure the conversation flows naturally

Format your response as JSON:
{
  "conversations": [
    {
      "from": "human",
      "value": "Your question here"
    },
    {
      "from": "gpt", 
      "value": "Your detailed answer here"
    }
  ]
}

Please generate the Q&A pairs now:
"""
    
    # 프롬프트 변형 옵션
    enable_context_enhancement: bool = True
    enable_few_shot_examples: bool = True
    few_shot_examples: List[Dict[str, Any]] = field(default_factory=lambda: [
        {
            "document": {"title": "Example Document", "content": "Sample content about technical topic."},
            "conversations": [
                {"from": "human", "value": "What is the main concept?"},
                {"from": "gpt", "value": "The main concept is..."}
            ]
        }
    ])
    
    # 다양성 설정
    diversity_prompts: List[str] = field(default_factory=lambda: [
        "Generate questions about basic usage and setup.",
        "Generate questions about advanced features and best practices.",
        "Generate questions about troubleshooting and common issues.",
        "Generate questions about performance optimization.",
        "Generate questions about integration with other systems."
    ])
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_prompt_length <= 0:
            raise ValueError("max_prompt_length는 양의 정수여야 합니다")
        if not (0.0 <= self.temperature <= 2.0):
            raise ValueError("temperature는 0.0과 2.0 사이여야 합니다)


class PromptEngine:
    """프롬프트 엔진"""
    
    def __init__(self, config: PromptEngineConfig = None):
        """
        초기화
        
        Args:
            config: 프롬프트 엔진 설정
        """
        self.config = config or PromptEngineConfig()
        
        # 통계 정보
        self.stats = {
            "total_prompts_generated": 0,
            "total_tokens_used": 0,
            "average_prompt_length": 0.0,
            "start_time": None
        }
    
    def create_conversation_prompt(
        self,
        document: Dict[str, Any],
        context_info: Dict[str, Any] = None,
        target_count: int = 1,
        mode: str = "llm_assisted"
    ) -> str:
        """
        대화 생성용 프롬프트 생성
        
        Args:
            document: 문서 데이터
            context_info: 추가 컨텍스트 정보
            target_count: 생성할 대화 수
            mode: 생성 모드
            
        Returns:
            생성된 프롬프트
        """
        self.stats["start_time"] = datetime.now()
        
        try:
            # 문서 정보 추출
            document_title = document.get("title", "Unknown Document")
            document_content = document.get("content", "")
            
            # 프롬프트 템플릿에 데이터 채우기
            prompt_data = {
                "document_title": document_title,
                "document_content": document_content,
                "context_info": self._format_context_info(context_info) if context_info else "",
                "target_count": target_count,
                "mode": mode
            }
            
            # 기본 프롬프트 생성
            prompt = self.config.conversation_prompt_template.format(**prompt_data)
            
            # 컨텍스트 향상
            if self.config.enable_context_enhancement:
                prompt = self._enhance_with_context(prompt, context_info)
            
            # Few-shot 예제 추가
            if self.config.enable_few_shot_examples:
                prompt = self._add_few_shot_examples(prompt)
            
            # 다양성 프롬프트 추가
            if target_count > 1:
                prompt = self._add_diversity_prompts(prompt, target_count)
            
            # 프롬프트 길이 제한
            if len(prompt) > self.config.max_prompt_length:
                prompt = self._truncate_prompt(prompt, self.config.max_prompt_length)
            
            # 통계 업데이트
            self.stats["total_prompts_generated"] += 1
            self.stats["total_tokens_used"] += len(prompt) // 4  # 간단한 토큰 추정
            self.stats["average_prompt_length"] = (
                (self.stats["average_prompt_length"] * (self.stats["total_prompts_generated"] - 1) + len(prompt)) 
                / self.stats["total_prompts_generated"]
            )
            
            return prompt
            
        except Exception as e:
            logger.error(f"프롬프트 생성 실패: {str(e)}")
            return self._create_fallback_prompt(document, target_count)
    
    def _format_context_info(self, context_info: Dict[str, Any]) -> str:
        """
        컨텍스트 정보 포맷팅
        
        Args:
            context_info: 컨텍스트 정보
            
        Returns:
            포맷팅된 컨텍스트 텍스트
        """
        try:
            formatted_parts = []
            
            # Context7 정보
            if "context7" in context_info:
                context7_data = context_info["context7"]
                if context7_data.get("results"):
                    formatted_parts.append("Context7 Documentation References:")
                    for result in context7_data["results"][:3]:  # 상위 3개만 표시
                        formatted_parts.append(f"- {result.get('title', 'No title')}: {result.get('content', 'No content')[:200]}...")
            
            # 로컬 검색 정보
            if "local" in context_info:
                local_data = context_info["local"]
                if local_data.get("results"):
                    formatted_parts.append("Local Search Results:")
                    for result in local_data["results"][:2]:
                        formatted_parts.append(f"- {result.get('title', 'No title')}: {result.get('content', 'No content')[:150]}...")
            
            # Qdrant 정보
            if "qdrant" in context_info:
                qdrant_data = context_info["qdrant"]
                if qdrant_data.get("results"):
                    formatted_parts.append("Vector Search Results:")
                    for result in qdrant_data["results"][:2]:
                        formatted_parts.append(f"- {result.get('title', 'No title')}: {result.get('content', 'No content')[:150]}...")
            
            return "\n".join(formatted_parts)
            
        except Exception as e:
            logger.error(f"컨텍스트 정보 포맷팅 실패: {str(e)}")
            return ""
    
    def _enhance_with_context(self, prompt: str, context_info: Dict[str, Any]) -> str:
        """
        컨텍스트 정보로 프롬프트 향상
        
        Args:
            prompt: 기본 프롬프트
            context_info: 컨텍스트 정보
            
        Returns:
            향상된 프롬프트
        """
        if not context_info:
            return prompt
        
        try:
            # 컨텍스트 정보를 프롬프트에 추가
            context_section = "\n\nRelevant Additional Context:\n"
            context_section += self._format_context_info(context_info)
            
            # 프롬프트에 컨텍스트 섹션 추가
            if "Additional Context:" in prompt:
                prompt = prompt.replace("Additional Context:", context_section)
            else:
                prompt += context_section
            
            return prompt
            
        except Exception as e:
            logger.error(f"프롬프트 컨텍스트 향상 실패: {str(e)}")
            return prompt
    
    def _add_few_shot_examples(self, prompt: str) -> str:
        """
        Few-shot 예제 추가
        
        Args:
            prompt: 기본 프롬프트
            
        Returns:
            Few-shot 예제가 추가된 프롬프트
        """
        try:
            examples_text = "\n\nExamples:\n"
            
            for i, example in enumerate(self.config.few_shot_examples[:2]):  # 최대 2개 예제
                examples_text += f"\nExample {i+1}:\n"
                examples_text += f"Document: {example['document']['title']}\n"
                
                for conv in example['conversations']:
                    examples_text += f"{conv['from'].upper()}: {conv['value']}\n"
            
            # 프롬프트에 예제 추가
            if "Please generate the Q&A pairs now:" in prompt:
                prompt = prompt.replace("Please generate the Q&A pairs now:", examples_text + "\n\nPlease generate the Q&A pairs now:")
            else:
                prompt += examples_text
            
            return prompt
            
        except Exception as e:
            logger.error(f"Few-shot 예제 추가 실패: {str(e)}")
            return prompt
    
    def _add_diversity_prompts(self, prompt: str, target_count: int) -> str:
        """
        다양성 프롬프트 추가
        
        Args:
            prompt: 기본 프롬프트
            target_count: 목표 대화 수
            
        Returns:
            다양성 프롬프트가 추가된 프롬프트
        """
        try:
            diversity_text = "\n\nFocus Areas for Diversity:\n"
            
            # 다양성 프롬프트 선택
            selected_prompts = self.config.diversity_prompts[:min(target_count, len(self.config.diversity_prompts))]
            
            for i, diversity_prompt in enumerate(selected_prompts):
                diversity_text += f"{i+1}. {diversity_prompt}\n"
            
            # 프롬프트에 다양성 정보 추가
            if "Requirements:" in prompt:
                prompt = prompt.replace("Requirements:", diversity_text + "\n\nRequirements:")
            else:
                prompt += diversity_text
            
            return prompt
            
        except Exception as e:
            logger.error(f"다양성 프롬프트 추가 실패: {str(e)}")
            return prompt
    
    def _truncate_prompt(self, prompt: str, max_length: int) -> str:
        """
        프롬프트 자르기
        
        Args:
            prompt: 원본 프롬프트
            max_length: 최대 길이
            
        Returns:
            자른 프롬프트
        """
        try:
            # 프롬프트를 의미 있는 단위로 자르기
            if len(prompt) <= max_length:
                return prompt
            
            # JSON 부분은 유지하고 설명 부분만 자르기
            json_start = prompt.find("{")
            if json_start != -1:
                json_part = prompt[json_start:]
                text_part = prompt[:json_start]
                
                # 텍스트 부분 자르기
                available_length = max_length - len(json_part)
                if available_length > 0:
                    truncated_text = text_part[:available_length]
                    return truncated_text + json_part
                else:
                    return json_part
            
            # JSON 부분이 없으면 전체를 자르기
            return prompt[:max_length]
            
        except Exception as e:
            logger.error(f"프롬프트 자르기 실패: {str(e)}")
            return prompt[:max_length]
    
    def _create_fallback_prompt(self, document: Dict[str, Any], target_count: int) -> str:
        """
        대체 프롬프트 생성
        
        Args:
            document: 문서 데이터
            target_count: 생성할 대화 수
            
        Returns:
            대체 프롬프트
        """
        try:
            document_title = document.get("title", "Unknown Document")
            document_content = document.get("content", "")
            
            # 간단한 대체 프롬프트
            fallback_prompt = f"""
Generate {target_count} Q&A pairs based on the following document:

Title: {document_title}
Content: {document_content[:1000]}...

Format as JSON with "conversations" array containing "from" and "value" fields.
"""
            return fallback_prompt
            
        except Exception as e:
            logger.error(f"대체 프롬프트 생성 실패: {str(e)}")
            return "Generate a Q&A pair."
    
    def create_system_prompt(self, role: str = "technical_assistant") -> str:
        """
        시스템 프롬프트 생성
        
        Args:
            role: 역할 유형
            
        Returns:
            시스템 프롬프트
        """
        role_prompts = {
            "technical_assistant": "You are a helpful technical assistant specializing in documentation and Q&A generation.",
            "code_reviewer": "You are an expert code reviewer providing detailed feedback on code quality and best practices.",
            "tutor": "You are an educational tutor explaining complex concepts in simple terms.",
            "analyst": "You are a data analyst providing insights and recommendations based on technical information."
        }
        
        return role_prompts.get(role, self.config.system_prompt)
    
    def create_refinement_prompt(self, original_response: str, feedback: str) -> str:
        """
        응답 개선용 프롬프트 생성
        
        Args:
            original_response: 원본 응답
            feedback: 피드백
            
        Returns:
            개선용 프롬프트
        """
        refinement_prompt = f"""
Please improve the following response based on the feedback provided:

Original Response:
{original_response}

Feedback:
{feedback}

Please provide an improved response that addresses the feedback while maintaining the core information.
"""
        return refinement_prompt
    
    def get_stats(self) -> Dict[str, Any]:
        """통계 정보 반환"""
        if self.stats["start_time"]:
            elapsed_time = (datetime.now() - self.stats["start_time"]).total_seconds()
        else:
            elapsed_time = 0
        
        return {
            **self.stats,
            "elapsed_time": elapsed_time,
            "config": {
                "max_prompt_length": self.config.max_prompt_length,
                "temperature": self.config.temperature,
                "enable_context_enhancement": self.config.enable_context_enhancement,
                "enable_few_shot_examples": self.config.enable_few_shot_examples
            }
        }


def create_prompt_engine(config: PromptEngineConfig = None) -> PromptEngine:
    """
    프롬프트 엔진 생성
    
    Args:
        config: 프롬프트 엔진 설정
        
    Returns:
        PromptEngine 인스턴스
    """
    config = config or PromptEngineConfig()
    return PromptEngine(config)