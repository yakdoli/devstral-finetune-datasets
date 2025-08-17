#!/usr/bin/env python3
"""
대화 생성기 모듈

로컬 LLM을 사용하여 고품질의 대화 데이터를 생성합니다.
Context7 하이브리드 검색과 통합하여 정확한 정보를 제공합니다.
"""

import logging
import asyncio
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime
import json
import re
from enum import Enum

from .client import LocalLLMClient, APIResponse
from .prompt_engine import PromptEngine
from .token_manager import TokenManager
from .hybrid_searcher import HybridSearcher

logger = logging.getLogger(__name__)


class GenerationMode(Enum):
    """생성 모드 정의"""
    LLM_ASSISTED = "llm_assisted"
    RULE_BASED = "rule_based"


@dataclass
class ConversationConfig:
    """대화 생성 설정"""
    # 생성 옵션
    max_conversations_per_document: int = 3
    min_conversation_length: int = 50
    max_conversation_length: int = 2000
    
    # 품질 설정
    enable_quality_filter: bool = True
    quality_threshold: float = 0.7
    
    # 하이브리드 검색 설정
    enable_hybrid_search: bool = True
    hybrid_search_weight: float = 0.3
    
    # 다양성 설정
    enable_diversity: bool = True
    diversity_temperature: float = 0.8
    
    # 재시도 설정
    max_retry_attempts: int = 3
    retry_on_error: bool = True
    
    # 로깅 설정
    enable_detailed_logging: bool = False
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_conversations_per_document <= 0:
            raise ValueError("max_conversations_per_document는 양의 정수여야 합니다")
        if self.min_conversation_length <= 0:
            raise ValueError("min_conversation_length는 양의 정수여야 합니다")
        if self.max_conversation_length <= self.min_conversation_length:
            raise ValueError("max_conversation_length는 min_conversation_length보다 커야 합니다")
        if not (0.0 <= self.quality_threshold <= 1.0):
            raise ValueError("quality_threshold는 0.0과 1.0 사이여야 합니다")
        if not (0.0 <= self.hybrid_search_weight <= 1.0):
            raise ValueError("hybrid_search_weight는 0.0과 1.0 사이여야 합니다")
        if not (0.0 <= self.diversity_temperature <= 2.0):
            raise ValueError("diversity_temperature는 0.0과 2.0 사이여야 합니다")


@dataclass
class Conversation:
    """대화 데이터 클래스"""
    id: str
    document_id: str
    document_title: str
    document_content: str
    conversations: List[Dict[str, str]]
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    quality_score: float = 0.0
    source_info: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환"""
        return {
            "id": self.id,
            "document_id": self.document_id,
            "document_title": self.document_title,
            "document_content": self.document_content,
            "conversations": self.conversations,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "quality_score": self.quality_score,
            "source_info": self.source_info
        }


class ConversationGenerator:
    """대화 생성기"""
    
    def __init__(
        self,
        client: LocalLLMClient,
        prompt_engine: PromptEngine,
        token_manager: TokenManager,
        config: ConversationConfig = None,
        hybrid_searcher: HybridSearcher = None
    ):
        """
        초기화
        
        Args:
            client: 로컬 LLM 클라이언트
            prompt_engine: 프롬프트 엔진
            token_manager: 토큰 관리자
            config: 대화 생성 설정
            hybrid_searcher: 하이브리드 검색기
        """
        self.client = client
        self.prompt_engine = prompt_engine
        self.token_manager = token_manager
        self.config = config or ConversationConfig()
        self.hybrid_searcher = hybrid_searcher
        
        # 통계 정보
        self.stats = {
            "total_documents": 0,
            "total_conversations": 0,
            "successful_conversations": 0,
            "failed_conversations": 0,
            "total_tokens_used": 0,
            "average_quality_score": 0.0,
            "start_time": None
        }
    
    async def generate_conversations(
        self,
        documents: List[Dict[str, Any]],
        target_count: int = 1,
        mode: str = "llm_assisted"
    ) -> List[Dict[str, Any]]:
        """
        대화 생성
        
        Args:
            documents: 문서 목록
            target_count: 생성할 대화 수
            mode: 생성 모드
            
        Returns:
            생성된 대화 목록
        """
        if not documents:
            logger.warning("생성할 문서가 없습니다")
            return []
        
        self.stats["start_time"] = datetime.now()
        self.stats["total_documents"] = len(documents)
        
        try:
            # 대화 생성
            conversations = []
            
            for document in documents:
                # 문서별 대화 생성
                document_conversations = await self._generate_conversations_for_document(
                    document, target_count, mode
                )
                
                conversations.extend(document_conversations)
                
                # 통계 업데이트
                self.stats["total_conversations"] += len(document_conversations)
                self.stats["successful_conversations"] += len(document_conversations)
            
            # 품질 필터링
            if self.config.enable_quality_filter:
                conversations = self._filter_conversations_by_quality(conversations)
            
            # 다양성 보장
            if self.config.enable_diversity and len(conversations) > target_count:
                conversations = self._ensure_diversity(conversations, target_count)
            
            # 최종 통계 업데이트
            if conversations:
                self.stats["average_quality_score"] = sum(
                    conv.get("quality_score", 0.0) for conv in conversations
                ) / len(conversations)
            
            logger.info(f"대화 생성 완료: {len(conversations)}개 대화 생성")
            return conversations
            
        except Exception as e:
            logger.error(f"대화 생성 실패: {str(e)}")
            self.stats["failed_conversations"] += 1
            return []
    
    async def _generate_conversations_for_document(
        self,
        document: Dict[str, Any],
        target_count: int,
        mode: str
    ) -> List[Dict[str, Any]]:
        """
        단일 문서에 대한 대화 생성
        
        Args:
            document: 문서 데이터
            target_count: 생성할 대화 수
            mode: 생성 모드
            
        Returns:
            생성된 대화 목록
        """
        document_id = document.get("id", f"doc_{hash(document.get('content', ''))}")
        document_title = document.get("title", "Unknown Document")
        document_content = document.get("content", "")
        
        # 하이브리드 검색 수행
        context_info = {}
        if self.config.enable_hybrid_search and self.hybrid_searcher:
            try:
                search_results = await self.hybrid_searcher.search(
                    query=document_content,
                    limit=5,
                    weights={"context7": 0.3, "local": 0.3, "qdrant": 0.4}
                )
                context_info = search_results
            except Exception as e:
                logger.warning(f"하이브리드 검색 실패: {str(e)}")
        
        # 프롬프트 생성
        prompt = self.prompt_engine.create_conversation_prompt(
            document=document,
            context_info=context_info,
            target_count=target_count,
            mode=mode
        )
        
        # 토큰 관리
        token_limit = self.token_manager.get_token_limit()
        if len(prompt) > token_limit:
            prompt = self.token_manager.truncate_prompt(prompt, token_limit)
        
        # 대화 생성
        conversations = []
        for i in range(min(target_count, self.config.max_conversations_per_document)):
            try:
                # LLM 호출
                response = await self.client.chat_completion(
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=self.config.max_conversation_length,
                    temperature=self.config.diversity_temperature
                )
                
                # 응답 파싱
                conversation_data = self._parse_conversation_response(
                    response.content, document_id, document_title, document_content
                )
                
                if conversation_data:
                    # 품질 평가
                    quality_score = self._evaluate_conversation_quality(conversation_data)
                    conversation_data["quality_score"] = quality_score
                    conversation_data["source_info"] = {
                        "context_info": context_info,
                        "generation_mode": mode,
                        "generation_index": i
                    }
                    
                    conversations.append(conversation_data)
                    
                    # 통계 업데이트
                    self.stats["total_tokens_used"] += response.tokens_used
                
            except Exception as e:
                logger.error(f"대화 생성 실패 (문서: {document_id}, 인덱스: {i}): {str(e)}")
                
                if self.config.retry_on_error and i < self.config.max_retry_attempts - 1:
                    continue
                else:
                    break
        
        return conversations
    
    def _parse_conversation_response(
        self,
        response_content: str,
        document_id: str,
        document_title: str,
        document_content: str
    ) -> Optional[Dict[str, Any]]:
        """
        LLM 응답을 대화 데이터로 파싱
        
        Args:
            response_content: LLM 응답 내용
            document_id: 문서 ID
            document_title: 문서 제목
            document_content: 문서 내용
            
        Returns:
            파싱된 대화 데이터
        """
        try:
            # JSON 형식인지 확인
            if response_content.strip().startswith("{"):
                data = json.loads(response_content)
            else:
                # 텍스트 형식인 경우 파싱
                data = self._parse_text_response(response_content)
            
            # 필수 필드 확인
            if not data.get("conversations"):
                logger.warning("대화 데이터에 conversations 필드가 없습니다")
                return None
            
            # 대화 형식 검증
            conversations = data["conversations"]
            if not isinstance(conversations, list):
                logger.warning("conversations는 리스트여야 합니다")
                return None
            
            # 대화 내용 검증
            for conv in conversations:
                if not isinstance(conv, dict):
                    logger.warning("대화 항목은 딕셔너리여야 합니다")
                    return None
                
                if "from" not in conv or "value" not in conv:
                    logger.warning("대화 항목에 'from'과 'value' 필드가 필요합니다")
                    return None
            
            # 대화 생성
            conversation = Conversation(
                id=f"conv_{document_id}_{hash(response_content)}",
                document_id=document_id,
                document_title=document_title,
                document_content=document_content,
                conversations=conversations,
                metadata={
                    "source_document": document_id,
                    "source_title": document_title,
                    "generation_timestamp": datetime.now().isoformat()
                }
            )
            
            return conversation.to_dict()
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON 파싱 실패: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"대화 응답 파싱 실패: {str(e)}")
            return None
    
    def _parse_text_response(self, response_content: str) -> Dict[str, Any]:
        """
        텍스트 형식의 응답을 파싱
        
        Args:
            response_content: 텍스트 응답
            
        Returns:
            파싱된 데이터
        """
        # 간단한 텍스트 파싱 로직
        # 실제 구현에서는 더 복잡한 파싱 로직이 필요할 수 있습니다
        
        # 대화 형식 추출
        conversations = []
        
        # 질문-답변 쌍 추출
        qa_pattern = r'Q: (.*?)\n+A: (.*?)(?=\n\n|$)'
        matches = re.findall(qa_pattern, response_content, re.DOTALL)
        
        for question, answer in matches:
            conversations.append({
                "from": "human",
                "value": question.strip()
            })
            conversations.append({
                "from": "gpt",
                "value": answer.strip()
            })
        
        if not conversations:
            # 기본 형식으로 대화 생성
            conversations = [
                {
                    "from": "human",
                    "value": "이 문서에 대해 자세히 알려주세요."
                },
                {
                    "from": "gpt",
                    "value": response_content[:500]  # 응답의 일부를 사용
                }
            ]
        
        return {
            "conversations": conversations
        }
    
    def _evaluate_conversation_quality(self, conversation: Dict[str, Any]) -> float:
        """
        대화 품질 평가
        
        Args:
            conversation: 대화 데이터
            
        Returns:
            품질 점수 (0.0 ~ 1.0)
        """
        try:
            score = 1.0
            
            # 대화 길이 평가
            conversations = conversation.get("conversations", [])
            total_length = sum(len(conv.get("value", "")) for conv in conversations)
            
            if total_length < self.config.min_conversation_length:
                score *= 0.5
            elif total_length > self.config.max_conversation_length:
                score *= 0.8
            
            # 대화 구조 평가
            if len(conversations) < 2:
                score *= 0.7
            
            # 내용 관련성 평가 (간단한 구현)
            document_content = conversation.get("document_content", "")
            if document_content:
                # 문서 내용과의 관련성 검사
                content_similarity = self._calculate_content_similarity(
                    conversations, document_content
                )
                score *= (0.5 + 0.5 * content_similarity)
            
            # 품질 점수 범위 제한
            return max(0.0, min(1.0, score))
            
        except Exception as e:
            logger.error(f"품질 평가 실패: {str(e)}")
            return 0.5
    
    def _calculate_content_similarity(
        self,
        conversations: List[Dict[str, str]],
        document_content: str
    ) -> float:
        """
        대화 내용과 문서 내용의 유사도 계산
        
        Args:
            conversations: 대화 목록
            document_content: 문서 내용
            
        Returns:
            유사도 점수 (0.0 ~ 1.0)
        """
        try:
            # 간단한 유사도 계산
            conversation_text = " ".join(conv.get("value", "") for conv in conversations)
            
            # 키워드 기반 유사도
            doc_keywords = set(document_content.lower().split())
            conv_keywords = set(conversation_text.lower().split())
            
            if not doc_keywords:
                return 0.0
            
            intersection = doc_keywords.intersection(conv_keywords)
            similarity = len(intersection) / len(doc_keywords)
            
            return similarity
            
        except Exception as e:
            logger.error(f"유사도 계산 실패: {str(e)}")
            return 0.5
    
    def _filter_conversations_by_quality(self, conversations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        품질 점수로 대화 필터링
        
        Args:
            conversations: 대화 목록
            
        Returns:
            필터링된 대화 목록
        """
        filtered = [
            conv for conv in conversations
            if conv.get("quality_score", 0.0) >= self.config.quality_threshold
        ]
        
        logger.info(f"품질 필터링: {len(conversations)} -> {len(filtered)}")
        return filtered
    
    def _ensure_diversity(self, conversations: List[Dict[str, Any]], target_count: int) -> List[Dict[str, Any]]:
        """
        대화의 다양성 보장
        
        Args:
            conversations: 대화 목록
            target_count: 목표 대화 수
            
        Returns:
            다양성이 보장된 대화 목록
        """
        if len(conversations) <= target_count:
            return conversations
        
        # 간단한 다양성 보장: 품질 점수 기준 상위 N개 선택
        sorted_conversations = sorted(
            conversations,
            key=lambda x: x.get("quality_score", 0.0),
            reverse=True
        )
        
        return sorted_conversations[:target_count]
    
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
                "max_conversations_per_document": self.config.max_conversations_per_document,
                "quality_threshold": self.config.quality_threshold,
                "enable_hybrid_search": self.config.enable_hybrid_search,
                "enable_diversity": self.config.enable_diversity
            }
        }


def create_conversation_generator(
    client: LocalLLMClient,
    prompt_engine: PromptEngine,
    token_manager: TokenManager,
    config: ConversationConfig = None,
    hybrid_searcher: HybridSearcher = None
) -> ConversationGenerator:
    """
    대화 생성기 생성
    
    Args:
        client: 로컬 LLM 클라이언트
        prompt_engine: 프롬프트 엔진
        token_manager: 토큰 관리자
        config: 대화 생성 설정
        hybrid_searcher: 하이브리드 검색기
        
    Returns:
        ConversationGenerator 인스턴스
    """
    config = config or ConversationConfig()
    return ConversationGenerator(client, prompt_engine, token_manager, config, hybrid_searcher)