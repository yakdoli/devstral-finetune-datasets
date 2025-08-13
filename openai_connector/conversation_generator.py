#!/usr/bin/env python3
"""
대화 생성기 모듈
ShareGPT 포맷의 다중 턴 대화를 생성합니다.
"""

import json
import asyncio
import logging
import uuid
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
import random
from pathlib import Path

from .client import OpenAIClient, OpenAIAPIClientConfig, APIResponse
from .prompt_engine import PromptEngine, PromptConfig
from .token_manager import TokenManager, TokenConfig

logger = logging.getLogger(__name__)


class GenerationMode(Enum):
    """생성 모드 정의"""
    LLM_ASSISTED = "llm_assisted"
    RULE_BASED = "rule_based"


@dataclass
class ConversationConfig:
    """대화 생성 설정"""
    generation_mode: GenerationMode = GenerationMode.LLM_ASSISTED
    target_count: int = 1000
    max_turns: int = 4
    batch_size: int = 16
    max_concurrent: int = 8
    temperature: float = 0.3
    include_metadata: bool = True
    save_intermediate: bool = True
    intermediate_interval: int = 100
    output_format: str = "sharegpt"  # sharegpt, alpaca, unsloth


@dataclass
class Conversation:
    """대화 데이터 클래스"""
    id: str
    conversations: List[Dict[str, str]]
    metadata: Dict[str, Any]
    created_at: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환"""
        return {
            "id": self.id,
            "conversations": self.conversations,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Conversation':
        """딕셔너리에서 생성"""
        return cls(
            id=data["id"],
            conversations=data["conversations"],
            metadata=data["metadata"],
            created_at=datetime.fromisoformat(data["created_at"]) if "created_at" in data else datetime.now()
        )


class ConversationGenerator:
    """대화 생성기 클래스"""
    
    def __init__(
        self,
        client: OpenAIClient,
        prompt_engine: PromptEngine,
        token_manager: TokenManager,
        config: ConversationConfig
    ):
        """
        초기화
        
        Args:
            client: OpenAI 클라이언트
            prompt_engine: 프롬프트 엔진
            token_manager: 토큰 관리자
            config: 대화 생성 설정
        """
        self.client = client
        self.prompt_engine = prompt_engine
        self.token_manager = token_manager
        self.config = config
        
        self.generated_count = 0
        self.failed_count = 0
        self.total_tokens_used = 0
        self.start_time = None
        
    async def generate_conversations(
        self,
        documents: List[Dict[str, Any]],
        target_count: int = None
    ) -> List[Conversation]:
        """
        대화 데이터셋을 생성합니다.
        
        Args:
            documents: 입력 문서 목록
            target_count: 목표 대화 수
            
        Returns:
            생성된 대화 목록
        """
        target_count = target_count or self.config.target_count
        self.start_time = datetime.now()
        
        logger.info(f"대화 생성 시작: 목표 {target_count}개, 문서 {len(documents)}개")
        
        conversations = []
        
        # 문서를 배치로 처리
        for i in range(0, len(documents), self.config.batch_size):
            batch_documents = documents[i:i + self.config.batch_size]
            logger.info(f"배치 처리: {i+1}-{min(i+len(batch_documents), len(documents))}/{len(documents)}")
            
            # 배치 대화 생성
            batch_conversations = await self._generate_batch_conversations(batch_documents)
            conversations.extend(batch_conversations)
            
            # 중간 결과 저장
            if self.config.save_intermediate and len(conversations) % self.config.intermediate_interval == 0:
                await self._save_intermediate_results(conversations)
            
            # 목표 도달 확인
            if len(conversations) >= target_count:
                break
        
        # 최종 결과 정리
        final_conversations = conversations[:target_count]
        
        # 통계 정보 업데이트
        self._update_stats(final_conversations)
        
        logger.info(f"대화 생성 완료: {len(final_conversations)}개 생성")
        logger.info(f"성공률: {(len(final_conversations) / (len(final_conversations) + self.failed_count) * 100):.1f}%")
        
        return final_conversations
    
    async def _generate_batch_conversations(self, documents: List[Dict[str, Any]]) -> List[Conversation]:
        """배치 단위로 대화를 생성합니다."""
        batch_conversations = []
        
        # 동시 요청 처리
        semaphore_value = self.config.max_concurrent
        semaphore = asyncio.Semaphore(semaphore_value)
        
        async def generate_conversation_for_document(doc_index, document):
            async with semaphore:
                try:
                    conversation = await self._generate_single_conversation(document)
                    if conversation:
                        batch_conversations.append(conversation)
                        self.generated_count += 1
                        logger.debug(f"대화 생성 완료: {self.generated_count}")
                    return conversation
                except Exception as e:
                    self.failed_count += 1
                    logger.error(f"대화 생성 실패 (문서 {doc_index}): {e}")
                    return None
        
        # 모든 문서에 대해 대화 생성
        tasks = []
        for doc_index, document in enumerate(documents):
            task = generate_conversation_for_document(doc_index, document)
            tasks.append(task)
        
        # 모든 작업 완료 대기
        await asyncio.gather(*tasks, return_exceptions=True)
        
        return batch_conversations
    
    async def _generate_single_conversation(
        self,
        document: Dict[str, Any]
    ) -> Optional[Conversation]:
        """단일 대화를 생성합니다."""
        try:
            # 간단한 프롬프트 생성 - API가 기대하는 형식
            user_question = f"{document.get('title', '문서')}에 대해 자세히 알고 싶습니다."
            
            messages = [
                {"role": "user", "content": user_question}
            ]
            
            logger.debug(f"문서 {document.get('id', 'unknown')} 프롬프트: {messages}")
            
            # 토큰 관리
            estimated_tokens = self.token_manager.estimate_tokens(messages)
            if not self.token_manager.check_token_limit(estimated_tokens):
                logger.warning("토큰 한도 초과")
                return None
            
            # API 호출
            response = await self.client.chat_completion(
                messages=messages,
                max_tokens=4096,  # 임시 고정값
                temperature=self.config.temperature
            )
            
            # 응답 토큰 수 업데이트
            tokens_used = response.tokens_used
            self.total_tokens_used += tokens_used
            self.token_manager.update_token_usage(0, tokens_used)  # prompt_tokens=0, completion_tokens=tokens_used
            
            # 대화 구조화
            conversation = self._structure_conversation(document, messages, response)
            
            return conversation
            
        except Exception as e:
            logger.error(f"단일 대화 생성 실패: {e}")
            return None
    
    def _structure_conversation(
        self,
        document: Dict[str, Any],
        prompt: List[Dict[str, str]],
        response: APIResponse
    ) -> Conversation:
        """대화를 ShareGPT 포맷으로 구조화합니다."""
        # 대화 ID 생성
        conversation_id = str(uuid.uuid4())
        
        # 대화 내용 구성
        conversations = []
        
        # 시스템 메시지 제외 (ShareGPT 형식에 포함되지 않음)
        for msg in prompt:
            if msg["role"] != "system":
                conversations.append({
                    "from": "human" if msg["role"] == "user" else "gpt",
                    "value": msg["content"]
                })
        
        # 응답 추가
        conversations.append({
            "from": "gpt",
            "value": response.content
        })
        
        # 메타데이터 구성
        metadata = {
            "source_documents": [document.get('id', str(document.get('title', '')))],
            "model": self.client.config.model,
            "tokens_used": response.tokens_used,
            "generation_mode": self.config.generation_mode.value,
            "document_info": {
                "component": document.get('component', ''),
                "title": document.get('title', ''),
                "quality_score": document.get('quality_score', 0.0)
            }
        }
        
        if self.config.include_metadata:
            metadata.update({
                "created_at": datetime.now().isoformat(),
                "generator_version": "1.0.0",
                "prompt_tokens": self.token_manager.get_prompt_tokens(),
                "completion_tokens": response.tokens_used,
                "total_tokens": self.token_manager.get_total_tokens()
            })
        
        return Conversation(
            id=conversation_id,
            conversations=conversations,
            metadata=metadata
        )
    
    async def _save_intermediate_results(self, conversations: List[Conversation]):
        """중간 결과를 저장합니다."""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"intermediate_conversations_{timestamp}_{len(conversations)}.json"
            
            # JSON 형식으로 저장
            data = [conv.to_dict() for conv in conversations]
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"중간 결과 저장: {filename} ({len(conversations)}개 대화)")
            
        except Exception as e:
            logger.error(f"중간 결과 저장 실패: {e}")
    
    def _update_stats(self, conversations: List[Conversation]):
        """통계 정보를 업데이트합니다."""
        if conversations:
            # 평균 토큰 사용량 계산
            avg_tokens = sum(conv.metadata.get('tokens_used', 0) for conv in conversations) / len(conversations)
            
            # 처리 시간 계산
            if self.start_time:
                processing_time = (datetime.now() - self.start_time).total_seconds()
                conversations_per_second = len(conversations) / processing_time
                
                logger.info(f"처리 통계:")
                logger.info(f"  - 총 대화 수: {len(conversations)}")
                logger.info(f"  - 실패 수: {self.failed_count}")
                logger.info(f"  - 성공률: {(len(conversations) / (len(conversations) + self.failed_count) * 100):.1f}%")
                logger.info(f"  - 평균 토큰 사용량: {avg_tokens:.1f}")
                logger.info(f"  - 총 토큰 사용량: {self.total_tokens_used}")
                logger.info(f"  - 처리 시간: {processing_time:.1f}초")
                logger.info(f"  - 처리 속도: {conversations_per_second:.1f} 대화/초")
    
    def get_stats(self) -> Dict[str, Any]:
        """통계 정보를 반환합니다."""
        return {
            "generated_count": self.generated_count,
            "failed_count": self.failed_count,
            "total_tokens_used": self.total_tokens_used,
            "success_rate": (self.generated_count / (self.generated_count + self.failed_count) * 100) if (self.generated_count + self.failed_count) > 0 else 0,
            "config": asdict(self.config)
        }


def create_conversation_generator(
    client: OpenAIClient,
    prompt_engine: PromptEngine,
    token_manager: TokenManager,
    config: ConversationConfig = None
) -> ConversationGenerator:
    """
    대화 생성기를 생성합니다.
    
    Args:
        client: OpenAI 클라이언트
        prompt_engine: 프롬프트 엔진
        token_manager: 토큰 관리자
        config: 대화 생성 설정
        
    Returns:
        ConversationGenerator 인스턴스
    """
    config = config or ConversationConfig()
    return ConversationGenerator(client, prompt_engine, token_manager, config)


# 테스트 코드
async def test_conversation_generator():
    """대화 생성기 테스트"""
    # 설정 생성
    client_config = OpenAIAPIClientConfig(
        endpoint="http://123.37.28.120:9997/v1",
        model="qwen2.5-vl-instruct",
        api_key="test-key",
        max_tokens=4096,
        temperature=0.3,
        max_concurrent=8
    )
    
    prompt_config = PromptConfig(
        max_turns=3,
        include_examples=True,
        example_count=1
    )
    
    token_config = TokenConfig(max_context_length=128000)
    
    conversation_config = ConversationConfig(
        generation_mode=GenerationMode.LLM_ASSISTED,
        target_count=5,
        max_turns=3,
        batch_size=2,
        max_concurrent=2
    )
    
    # 컴포넌트 생성
    client = OpenAIClient(client_config)
    prompt_engine = PromptEngine(prompt_config)
    token_manager = TokenManager(token_config)
    
    # 대화 생성기 생성
    generator = create_conversation_generator(client, prompt_engine, token_manager, conversation_config)
    
    # 테스트 문서
    test_documents = [
        {
            'id': 'doc1',
            'component': 'GridControl',
            'title': 'GridControl 기본 사용법',
            'content': 'GridControl은 Syncfusion WinForms의 강력한 데이터 그리드 컴포넌트입니다...',
            'quality_score': 0.8
        },
        {
            'id': 'doc2',
            'component': 'GridControl',
            'title': 'GridControl 고급 기능',
            'content': 'GridControl의 고급 기능에는 가상 모드, 커스텀 렌더링 등이 있습니다...',
            'quality_score': 0.9
        }
    ]
    
    # 대화 생성
    async with client:
        conversations = await generator.generate_conversations(test_documents)
        
        print(f"생성된 대화 수: {len(conversations)}")
        for i, conv in enumerate(conversations):
            print(f"\n대화 {i+1}:")
            print(f"ID: {conv.id}")
            print(f"턴 수: {len(conv.conversations)}")
            print(f"메타데이터: {conv.metadata}")


if __name__ == "__main__":
    asyncio.run(test_conversation_generator())