#!/usr/bin/env python3
"""
중복 제거 모듈
데이터셋에서 중복되는 아이템을 탐지하고 제거하는 기능을 제공합니다.
"""

import re
import hashlib
import logging
import math
from typing import List, Dict, Any, Optional, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class DuplicateRemoverConfig:
    """중복 제거기 설정"""
    # 유사도 임계값
    similarity_threshold: float = 0.9
    
    # 해시 기반 중복 제거 활성화
    hash_based_dedup: bool = True
    
    # 유사도 기반 중복 제거 활성화
    similarity_based_dedup: bool = True
    
    # 부분 중복 제거 활성화
    partial_dedup: bool = True
    
    # 최소 텍스트 길이
    min_text_length: int = 10
    
    # 최대 유사도 계산 대상 수
    max_similarity_candidates: int = 100
    
    # 해시 알고리즘
    hash_algorithm: str = "md5"


@dataclass
class DuplicateResult:
    """중복 제거 결과"""
    original_count: int = 0
    duplicate_count: int = 0
    unique_count: int = 0
    duplicate_pairs: List[Tuple[int, int]] = field(default_factory=list)
    similarity_scores: List[float] = field(default_factory=list)
    processing_time: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class DuplicateRemover:
    """중복 제거 클래스"""
    
    def __init__(self, config: Optional[DuplicateRemoverConfig] = None):
        """
        중복 제거기를 초기화합니다.
        
        Args:
            config: 중복 제거기 설정
        """
        self.config = config or DuplicateRemoverConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 처리된 아이템 캐시
        self._processed_items: Dict[str, Any] = {}
    
    def remove_duplicates(self, items: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], DuplicateResult]:
        """
        중복 아이템을 제거합니다.
        
        Args:
            items: 중복 제거할 아이템 목록
            
        Returns:
            중복이 제거된 아이템 목록과 결과
        """
        start_time = datetime.now()
        result = DuplicateResult()
        result.original_count = len(items)
        
        if not items:
            result.unique_count = 0
            result.processing_time = (datetime.now() - start_time).total_seconds()
            return [], result
        
        # 1단계: 해시 기반 중복 제거
        if self.config.hash_based_dedup:
            items, hash_result = self._hash_based_deduplication(items)
            result.duplicate_count += hash_result.duplicate_count
        
        # 2단계: 유사도 기반 중복 제거
        if self.config.similarity_based_dedup and len(items) > 1:
            items, similarity_result = self._similarity_based_deduplication(items)
            result.duplicate_count += similarity_result.duplicate_count
            result.duplicate_pairs.extend(similarity_result.duplicate_pairs)
            result.similarity_scores.extend(similarity_result.similarity_scores)
        
        # 3단계: 부분 중복 제거
        if self.config.partial_dedup:
            items, partial_result = self._partial_deduplication(items)
            result.duplicate_count += partial_result.duplicate_count
        
        result.unique_count = len(items)
        result.processing_time = (datetime.now() - start_time).total_seconds()
        
        self.logger.info(f"Deduplication completed: {result.original_count} -> {result.unique_count} "
                        f"({result.duplicate_count} duplicates removed)")
        
        return items, result
    
    def _hash_based_deduplication(self, items: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], DuplicateResult]:
        """해시 기반 중복 제거를 수행합니다."""
        result = DuplicateResult()
        seen_hashes = set()
        unique_items = []
        
        for item in items:
            item_hash = self._generate_item_hash(item)
            
            if item_hash in seen_hashes:
                result.duplicate_count += 1
                result.duplicate_pairs.append((len(unique_items), len(items)))
                continue
            
            seen_hashes.add(item_hash)
            unique_items.append(item)
        
        return unique_items, result
    
    def _similarity_based_deduplication(self, items: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], DuplicateResult]:
        """유사도 기반 중복 제거를 수행합니다."""
        result = DuplicateResult()
        
        # 텍스트 콘텐츠 추출
        texts = [self._extract_text_content(item) for item in items]
        
        # 텍스트 길이 필터링
        filtered_indices = []
        filtered_texts = []
        
        for i, text in enumerate(texts):
            if len(text.strip()) >= self.config.min_text_length:
                filtered_indices.append(i)
                filtered_texts.append(text)
        
        if len(filtered_texts) < 2:
            return items, result
        
        # 유사도 기반 중복 탐지
        to_remove = set()
        for i in range(len(filtered_texts)):
            if i in to_remove:
                continue
            
            for j in range(i + 1, len(filtered_texts)):
                if j in to_remove:
                    continue
                
                similarity = self._calculate_text_similarity(filtered_texts[i], filtered_texts[j])
                if similarity >= self.config.similarity_threshold:
                    to_remove.add(j)
                    result.duplicate_count += 1
                    result.duplicate_pairs.append((filtered_indices[i], filtered_indices[j]))
                    result.similarity_scores.append(similarity)
        
        # 중복 제거
        unique_indices = [idx for idx in filtered_indices if idx not in to_remove]
        unique_items = [items[idx] for idx in unique_indices]
        
        # 필터링되지 않은 아이템들도 포함
        for idx in range(len(items)):
            if idx not in filtered_indices:
                unique_items.append(items[idx])
        
        return unique_items, result
    
    def _partial_deduplication(self, items: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], DuplicateResult]:
        """부분 중복 제거를 수행합니다."""
        result = DuplicateResult()
        unique_items = []
        
        for i, item in enumerate(items):
            is_duplicate = False
            
            # 기존 아이템들과 비교
            for j, existing_item in enumerate(unique_items):
                similarity = self._calculate_partial_similarity(item, existing_item)
                
                if similarity >= self.config.similarity_threshold:
                    is_duplicate = True
                    result.duplicate_count += 1
                    result.duplicate_pairs.append((j, i))
                    break
            
            if not is_duplicate:
                unique_items.append(item)
        
        return unique_items, result
    
    def check_duplicates(self, items: List[Dict[str, Any]], threshold: float = 0.9) -> List[Dict[str, Any]]:
        """
        중복 아이템을 확인합니다.
        
        Args:
            items: 확인할 아이템 목록
            threshold: 유사도 임계값
            
        Returns:
            중복이 제거된 아이템 목록
        """
        unique_items = []
        seen_hashes = set()
        
        for item in items:
            # 해시 생성
            item_hash = self._generate_item_hash(item)
            
            # 해시 기반 중복 확인
            if item_hash in seen_hashes:
                continue
            
            # 유사도 기반 중복 확인
            is_duplicate = False
            for existing_item in unique_items:
                similarity = self._calculate_similarity(item, existing_item)
                if similarity >= threshold:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                unique_items.append(item)
                seen_hashes.add(item_hash)
        
        return unique_items
    
    def _generate_item_hash(self, item: Dict[str, Any]) -> str:
        """아이템의 해시를 생성합니다."""
        # 아이템의 텍스트 콘텐츠를 추출하여 해시 생성
        text_content = self._extract_text_content(item)
        return hashlib.md5(text_content.encode('utf-8')).hexdigest()
    
    def _extract_text_content(self, item: Dict[str, Any]) -> str:
        """아이템에서 텍스트 콘텐츠를 추출합니다."""
        if 'conversations' in item:
            # 대화 형식인 경우
            texts = []
            for conv in item['conversations']:
                if isinstance(conv, dict) and 'value' in conv:
                    texts.append(conv['value'])
            return ' '.join(texts)
        elif 'instruction' in item and 'response' in item:
            # 지시-응답 형식인 경우
            return f"{item['instruction']} {item['response']}"
        elif 'messages' in item:
            # 메시지 형식인 경우
            texts = []
            for msg in item['messages']:
                if isinstance(msg, dict) and 'content' in msg:
                    texts.append(msg['content'])
            return ' '.join(texts)
        else:
            # 기본적으로 모든 값을 합침
            text_parts = []
            for key, value in item.items():
                if isinstance(value, str):
                    text_parts.append(value)
            return ' '.join(text_parts)
    
    def _calculate_similarity(self, item1: Dict[str, Any], item2: Dict[str, Any]) -> float:
        """두 아이템 간의 유사도를 계산합니다."""
        text1 = self._extract_text_content(item1)
        text2 = self._extract_text_content(item2)
        
        if not text1 or not text2:
            return 0.0
        
        return self._calculate_text_similarity(text1, text2)
    
    def _calculate_text_similarity(self, text1: str, text2: str) -> float:
        """두 텍스트 간의 유사도를 계산합니다."""
        # 텍스트 정규화
        text1 = text1.lower().strip()
        text2 = text2.lower().strip()
        
        if text1 == text2:
            return 1.0
        
        if not text1 or not text2:
            return 0.0
        
        # 단어 기반 유사도 계산
        words1 = set(text1.split())
        words2 = set(text2.split())
        
        if not words1 or not words2:
            return 0.0
        
        # 자카드 유사도 계산
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        jaccard_similarity = len(intersection) / len(union)
        
        # 부분 문자열 유사도 추가
        substring_similarity = self._calculate_substring_similarity(text1, text2)
        
        # 가중 평균
        final_similarity = 0.7 * jaccard_similarity + 0.3 * substring_similarity
        
        return final_similarity
    
    def _calculate_substring_similarity(self, text1: str, text2: str) -> float:
        """두 텍스트 간의 부분 문자열 유사도를 계산합니다."""
        # 더 짧은 텍스트를 찾음
        shorter, longer = (text1, text2) if len(text1) < len(text2) else (text2, text1)
        
        if not shorter:
            return 0.0
        
        # 더 긴 텍스트에서 더 짧은 텍스트의 부분 문자열 찾기
        max_match = 0
        for i in range(len(longer) - len(shorter) + 1):
            substring = longer[i:i+len(shorter)]
            if substring == shorter:
                max_match = len(shorter)
                break
            else:
                # 부분 일치 길이 계산
                match_length = 0
                for j in range(len(shorter)):
                    if shorter[j] == longer[i+j]:
                        match_length += 1
                    else:
                        break
                max_match = max(max_match, match_length)
        
        # 일치 비율 계산
        return max_match / len(shorter) if shorter else 0.0
    
    def _calculate_partial_similarity(self, item1: Dict[str, Any], item2: Dict[str, Any]) -> float:
        """두 아이템 간의 부분 유사도를 계산합니다."""
        text1 = self._extract_text_content(item1)
        text2 = self._extract_text_content(item2)
        
        if not text1 or not text2:
            return 0.0
        
        # 공통 단어 비율 계산
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        # 자카드 유사도 계산
        jaccard_similarity = len(intersection) / len(union)
        
        return jaccard_similarity
    
    def get_deduplication_summary(self, result: DuplicateResult) -> Dict[str, Any]:
        """중복 제거 요약 정보를 생성합니다."""
        if result.original_count == 0:
            return {"total": 0, "unique": 0, "duplicates": 0, "rate": 0.0}
        
        return {
            "total": result.original_count,
            "unique": result.unique_count,
            "duplicates": result.duplicate_count,
            "removal_rate": result.duplicate_count / result.original_count,
            "processing_time": result.processing_time,
            "average_similarity": sum(result.similarity_scores) / len(result.similarity_scores) if result.similarity_scores else 0.0,
            "timestamp": result.timestamp
        }


if __name__ == "__main__":
    # 테스트 데이터
    test_items = [
        {
            "instruction": "Python 기초 문법을 설명해주세요.",
            "response": "Python은 간단하고 읽기 쉬운 프로그래밍 언어입니다."
        },
        {
            "instruction": "Python 기초 문법을 설명해주세요.",
            "response": "Python은 간단하고 읽기 쉬운 프로그래밍 언어입니다."  # 완전 중복
        },
        {
            "instruction": "Python 기초 문법을 설명해주세요.",
            "response": "파이썬은 쉽고 배우기 좋은 프로그래밍 언어입니다."  # 유사 중복
        },
        {
            "instruction": "자바스크립트란 무엇인가요?",
            "response": "자바스크립트는 웹 개발에 사용되는 프로그래밍 언어입니다."
        },
        {
            "instruction": "자바스크립트란 무엇인가요?",
            "response": "JS는 웹 브라우저에서 실행되는 스크립트 언어입니다."  # 유사 중복
        }
    ]
    
    # 중복 제거기 생성
    duplicate_remover = DuplicateRemover()
    
    print("=== Duplicate Remover Test ===")
    
    # 중복 제거 테스트
    unique_items, result = duplicate_remover.remove_duplicates(test_items)
    
    print(f"Original count: {result.original_count}")
    print(f"Unique count: {result.unique_count}")
    print(f"Duplicate count: {result.duplicate_count}")
    print(f"Processing time: {result.processing_time:.4f} seconds")
    print(f"Duplicate pairs: {result.duplicate_pairs}")
    
    # 요약 정보
    summary = duplicate_remover.get_deduplication_summary(result)
    print(f"\nSummary: {summary}")
    
    # 개별 확인 테스트
    print(f"\n=== Check Duplicates Test ===")
    test_check = [
        {"instruction": "Hello", "response": "Hi there"},
        {"instruction": "Hello", "response": "Hi there"},  # 중복
        {"instruction": "Hi", "response": "Hello world"}   # 다름
    ]
    
    unique_check = duplicate_remover.check_duplicates(test_check)
    print(f"Check duplicates: {len(test_check)} -> {len(unique_check)}")