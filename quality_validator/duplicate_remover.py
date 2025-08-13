#!/usr/bin/env python3
"""
중복 제거기 모듈
0.9 이상 유사도를 가진 중복 콘텐츠를 탐지하고 제거합니다.
"""

import hashlib
import logging
from typing import List, Dict, Any, Optional, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json
from pathlib import Path
import re
from collections import defaultdict
import difflib

# 선택적 임포트 (성능 향상을 위해)
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

__version__ = "1.0.0"
__author__ = "Duplicate Remover Team"


@dataclass
class DuplicateRemoverConfig:
    """중복 제거기 설정"""
    # 유사도 임계값
    similarity_threshold: float = 0.9
    
    # 중복 검사 방법 (exact, fuzzy, semantic)
    detection_method: str = "fuzzy"
    
    # 텍스트 정규화 활성화
    enable_text_normalization: bool = True
    
    # 해시 기반 빠른 검사 활성화
    enable_hash_check: bool = True
    
    # 의미적 유사도 검사 활성화 (sklearn 필요)
    enable_semantic_similarity: bool = SKLEARN_AVAILABLE
    
    # 배치 처리 크기
    batch_size: int = 1000
    
    # 메모리 효율 모드
    memory_efficient: bool = True
    
    # 중복 제거 전략 (remove_all, keep_first, keep_best)
    removal_strategy: str = "keep_first"
    
    # 로깅 레벨
    log_level: str = "INFO"


@dataclass
class DuplicateResult:
    """중복 검사 결과"""
    is_duplicate: bool
    similarity_score: float
    duplicate_of: Optional[str] = None
    status: str = "unique"  # unique, duplicate, similar
    matched_items: List[str] = field(default_factory=list)
    confidence_score: float = 0.0
    details: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class DuplicateGroup:
    """중복 그룹"""
    group_id: str
    items: List[str] = field(default_factory=list)
    similarity_scores: Dict[str, float] = field(default_factory=dict)
    representative_item: Optional[str] = None
    group_size: int = 0


class DuplicateRemover:
    """중복 제거기 클래스"""
    
    def __init__(self, config: Optional[DuplicateRemoverConfig] = None):
        """
        중복 제거기를 초기화합니다.
        
        Args:
            config: 중복 제거기 설정
        """
        self.config = config or DuplicateRemoverConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 로깅 설정
        self._setup_logging()
        
        # 중복 검사 데이터 구조 초기화
        self._initialize_data_structures()
        
        # TF-IDF 벡터라이저 초기화 (의미적 유사도용)
        if self.config.enable_semantic_similarity and SKLEARN_AVAILABLE:
            self._initialize_vectorizer()
        
        self.logger.info("DuplicateRemover initialized successfully")
    
    def _setup_logging(self):
        """로깅을 설정합니다."""
        level = getattr(logging, self.config.log_level.upper(), logging.INFO)
        self.logger.setLevel(level)
    
    def _initialize_data_structures(self):
        """데이터 구조를 초기화합니다."""
        # 해시 기반 빠른 검사용
        self.exact_hashes = {}  # hash -> item_id
        self.fuzzy_hashes = {}  # normalized_hash -> item_id
        
        # 텍스트 콘텐츠 저장 (메모리 효율 모드가 아닌 경우)
        if not self.config.memory_efficient:
            self.text_contents = {}  # item_id -> text_content
        
        # 중복 그룹 관리
        self.duplicate_groups = {}  # group_id -> DuplicateGroup
        self.item_to_group = {}  # item_id -> group_id
        
        # 처리 통계
        self.processing_stats = {
            'total_processed': 0,
            'exact_duplicates': 0,
            'fuzzy_duplicates': 0,
            'semantic_duplicates': 0,
            'unique_items': 0
        }
    
    def _initialize_vectorizer(self):
        """TF-IDF 벡터라이저를 초기화합니다."""
        try:
            self.vectorizer = TfidfVectorizer(
                max_features=5000,
                stop_words=None,  # 한국어 불용어는 별도 처리
                ngram_range=(1, 2),
                min_df=1,
                max_df=0.95
            )
            self.document_vectors = None
            self.document_ids = []
            
            self.logger.info("TF-IDF vectorizer initialized for semantic similarity")
            
        except Exception as e:
            self.logger.error(f"Error initializing vectorizer: {e}")
            self.config.enable_semantic_similarity = False
    
    def check_duplicates(self, item: Dict[str, Any], format_type: str = "sharegpt") -> DuplicateResult:
        """
        아이템의 중복 여부를 검사합니다.
        
        Args:
            item: 검사할 아이템
            format_type: 데이터 포맷 타입
            
        Returns:
            중복 검사 결과
        """
        try:
            # 아이템 ID 생성
            item_id = self._generate_item_id(item)
            
            # 텍스트 콘텐츠 추출
            text_content = self._extract_text_content(item, format_type)
            
            if not text_content:
                return DuplicateResult(
                    is_duplicate=False,
                    similarity_score=0.0,
                    status="no_content"
                )
            
            # 중복 검사 수행
            duplicate_result = self._perform_duplicate_check(item_id, text_content)
            
            # 아이템 등록 (중복이 아닌 경우)
            if not duplicate_result.is_duplicate:
                self._register_item(item_id, text_content)
            
            # 통계 업데이트
            self._update_statistics(duplicate_result)
            
            self.logger.debug(f"Duplicate check completed for {item_id}: {duplicate_result.status}")
            
            return duplicate_result
            
        except Exception as e:
            self.logger.error(f"Error in duplicate check: {e}")
            return DuplicateResult(
                is_duplicate=False,
                similarity_score=0.0,
                status="error",
                details={"error": str(e)}
            )
    
    def _generate_item_id(self, item: Dict[str, Any]) -> str:
        """아이템 ID를 생성합니다."""
        # 아이템 내용을 기반으로 고유 ID 생성
        item_str = json.dumps(item, sort_keys=True, ensure_ascii=False)
        return hashlib.md5(item_str.encode('utf-8')).hexdigest()[:16]
    
    def _extract_text_content(self, item: Dict[str, Any], format_type: str) -> str:
        """아이템에서 텍스트 콘텐츠를 추출합니다."""
        text_parts = []
        
        try:
            if format_type == "sharegpt":
                conversations = item.get("conversations", [])
                for conv in conversations:
                    if isinstance(conv, dict) and "value" in conv:
                        text_parts.append(conv["value"])
            
            elif format_type == "alpaca":
                for key in ["instruction", "input", "output"]:
                    if key in item and item[key]:
                        text_parts.append(item[key])
            
            elif format_type == "openai":
                messages = item.get("messages", [])
                for msg in messages:
                    if isinstance(msg, dict) and "content" in msg:
                        text_parts.append(msg["content"])
            
            return " ".join(text_parts)
            
        except Exception as e:
            self.logger.error(f"Error extracting text content: {e}")
            return ""
    
    def _perform_duplicate_check(self, item_id: str, text_content: str) -> DuplicateResult:
        """중복 검사를 수행합니다."""
        # 1. 정확한 중복 검사 (해시 기반)
        if self.config.enable_hash_check:
            exact_result = self._check_exact_duplicate(item_id, text_content)
            if exact_result.is_duplicate:
                return exact_result
        
        # 2. 퍼지 중복 검사 (정규화된 텍스트 기반)
        if self.config.detection_method in ["fuzzy", "semantic"]:
            fuzzy_result = self._check_fuzzy_duplicate(item_id, text_content)
            if fuzzy_result.is_duplicate:
                return fuzzy_result
        
        # 3. 의미적 중복 검사 (TF-IDF 기반)
        if self.config.enable_semantic_similarity and self.config.detection_method == "semantic":
            semantic_result = self._check_semantic_duplicate(item_id, text_content)
            if semantic_result.is_duplicate:
                return semantic_result
        
        # 중복이 아님
        return DuplicateResult(
            is_duplicate=False,
            similarity_score=0.0,
            status="unique"
        )
    
    def _check_exact_duplicate(self, item_id: str, text_content: str) -> DuplicateResult:
        """정확한 중복을 검사합니다."""
        # 정확한 해시 계산
        exact_hash = hashlib.sha256(text_content.encode('utf-8')).hexdigest()
        
        if exact_hash in self.exact_hashes:
            duplicate_id = self.exact_hashes[exact_hash]
            return DuplicateResult(
                is_duplicate=True,
                similarity_score=1.0,
                duplicate_of=duplicate_id,
                status="exact_duplicate",
                confidence_score=1.0
            )
        
        # 해시 등록
        self.exact_hashes[exact_hash] = item_id
        
        return DuplicateResult(
            is_duplicate=False,
            similarity_score=0.0,
            status="unique"
        )
    
    def _check_fuzzy_duplicate(self, item_id: str, text_content: str) -> DuplicateResult:
        """퍼지 중복을 검사합니다."""
        # 텍스트 정규화
        normalized_text = self._normalize_text(text_content)
        
        # 정규화된 해시 계산
        fuzzy_hash = hashlib.sha256(normalized_text.encode('utf-8')).hexdigest()
        
        if fuzzy_hash in self.fuzzy_hashes:
            duplicate_id = self.fuzzy_hashes[fuzzy_hash]
            return DuplicateResult(
                is_duplicate=True,
                similarity_score=0.95,  # 퍼지 매칭이므로 약간 낮은 점수
                duplicate_of=duplicate_id,
                status="fuzzy_duplicate",
                confidence_score=0.9
            )
        
        # 기존 아이템들과 유사도 비교 (메모리 효율 모드가 아닌 경우)
        if not self.config.memory_efficient and hasattr(self, 'text_contents'):
            best_match = self._find_best_fuzzy_match(normalized_text)
            if best_match and best_match[1] >= self.config.similarity_threshold:
                return DuplicateResult(
                    is_duplicate=True,
                    similarity_score=best_match[1],
                    duplicate_of=best_match[0],
                    status="fuzzy_duplicate",
                    confidence_score=best_match[1]
                )
        
        # 해시 등록
        self.fuzzy_hashes[fuzzy_hash] = item_id
        
        return DuplicateResult(
            is_duplicate=False,
            similarity_score=0.0,
            status="unique"
        )
    
    def _check_semantic_duplicate(self, item_id: str, text_content: str) -> DuplicateResult:
        """의미적 중복을 검사합니다."""
        if not SKLEARN_AVAILABLE:
            return DuplicateResult(
                is_duplicate=False,
                similarity_score=0.0,
                status="semantic_check_unavailable"
            )
        
        try:
            # 기존 문서가 없으면 중복이 아님
            if not self.document_ids:
                return DuplicateResult(
                    is_duplicate=False,
                    similarity_score=0.0,
                    status="unique"
                )
            
            # 현재 문서를 벡터화
            all_texts = [self.text_contents.get(doc_id, "") for doc_id in self.document_ids] + [text_content]
            
            # TF-IDF 벡터 계산
            tfidf_matrix = self.vectorizer.fit_transform(all_texts)
            
            # 현재 문서와 기존 문서들 간의 코사인 유사도 계산
            current_vector = tfidf_matrix[-1]
            existing_vectors = tfidf_matrix[:-1]
            
            similarities = cosine_similarity(current_vector, existing_vectors).flatten()
            
            # 최고 유사도 찾기
            max_similarity_idx = np.argmax(similarities)
            max_similarity = similarities[max_similarity_idx]
            
            if max_similarity >= self.config.similarity_threshold:
                duplicate_id = self.document_ids[max_similarity_idx]
                return DuplicateResult(
                    is_duplicate=True,
                    similarity_score=float(max_similarity),
                    duplicate_of=duplicate_id,
                    status="semantic_duplicate",
                    confidence_score=float(max_similarity)
                )
            
            return DuplicateResult(
                is_duplicate=False,
                similarity_score=float(max_similarity) if similarities.size > 0 else 0.0,
                status="unique"
            )
            
        except Exception as e:
            self.logger.error(f"Error in semantic duplicate check: {e}")
            return DuplicateResult(
                is_duplicate=False,
                similarity_score=0.0,
                status="semantic_check_error",
                details={"error": str(e)}
            )
    
    def _normalize_text(self, text: str) -> str:
        """텍스트를 정규화합니다."""
        if not self.config.enable_text_normalization:
            return text
        
        # 소문자 변환
        normalized = text.lower()
        
        # 공백 정규화
        normalized = re.sub(r'\s+', ' ', normalized)
        
        # 특수문자 제거 (일부 유지)
        normalized = re.sub(r'[^\w\s가-힣]', '', normalized)
        
        # 앞뒤 공백 제거
        normalized = normalized.strip()
        
        return normalized
    
    def _find_best_fuzzy_match(self, normalized_text: str) -> Optional[Tuple[str, float]]:
        """가장 유사한 텍스트를 찾습니다."""
        best_match = None
        best_score = 0.0
        
        for item_id, stored_text in self.text_contents.items():
            stored_normalized = self._normalize_text(stored_text)
            
            # 문자열 유사도 계산 (difflib 사용)
            similarity = difflib.SequenceMatcher(None, normalized_text, stored_normalized).ratio()
            
            if similarity > best_score:
                best_score = similarity
                best_match = (item_id, similarity)
        
        return best_match if best_score >= self.config.similarity_threshold else None
    
    def _register_item(self, item_id: str, text_content: str):
        """아이템을 등록합니다."""
        # 텍스트 콘텐츠 저장 (메모리 효율 모드가 아닌 경우)
        if not self.config.memory_efficient:
            self.text_contents[item_id] = text_content
        
        # 의미적 유사도 검사용 문서 ID 추가
        if self.config.enable_semantic_similarity and hasattr(self, 'document_ids'):
            self.document_ids.append(item_id)
    
    def _update_statistics(self, result: DuplicateResult):
        """통계를 업데이트합니다."""
        self.processing_stats['total_processed'] += 1
        
        if result.status == "exact_duplicate":
            self.processing_stats['exact_duplicates'] += 1
        elif result.status == "fuzzy_duplicate":
            self.processing_stats['fuzzy_duplicates'] += 1
        elif result.status == "semantic_duplicate":
            self.processing_stats['semantic_duplicates'] += 1
        elif result.status == "unique":
            self.processing_stats['unique_items'] += 1
    
    def batch_check_duplicates(self, items: List[Dict[str, Any]], format_type: str = "sharegpt") -> List[DuplicateResult]:
        """
        여러 아이템의 중복을 배치로 검사합니다.
        
        Args:
            items: 검사할 아이템 목록
            format_type: 데이터 포맷 타입
            
        Returns:
            중복 검사 결과 목록
        """
        results = []
        
        for i, item in enumerate(items):
            try:
                result = self.check_duplicates(item, format_type)
                results.append(result)
                
                if (i + 1) % self.config.batch_size == 0:
                    self.logger.info(f"Processed {i + 1}/{len(items)} items for duplicate check")
                    
            except Exception as e:
                self.logger.error(f"Error checking duplicates for item {i}: {e}")
                results.append(DuplicateResult(
                    is_duplicate=False,
                    similarity_score=0.0,
                    status="error",
                    details={"error": str(e)}
                ))
        
        unique_count = sum(1 for r in results if not r.is_duplicate)
        duplicate_count = len(results) - unique_count
        
        self.logger.info(f"Duplicate check completed: {unique_count} unique, {duplicate_count} duplicates")
        
        return results
    
    def remove_duplicates(self, items: List[Dict[str, Any]], format_type: str = "sharegpt") -> Tuple[List[Dict[str, Any]], List[DuplicateResult]]:
        """
        중복을 제거하고 고유한 아이템만 반환합니다.
        
        Args:
            items: 원본 아이템 목록
            format_type: 데이터 포맷 타입
            
        Returns:
            (고유한 아이템 목록, 중복 검사 결과 목록)
        """
        results = self.batch_check_duplicates(items, format_type)
        
        # 중복 제거 전략에 따라 처리
        if self.config.removal_strategy == "remove_all":
            # 중복된 모든 아이템 제거
            unique_items = [items[i] for i, result in enumerate(results) if not result.is_duplicate]
        
        elif self.config.removal_strategy == "keep_first":
            # 첫 번째 아이템만 유지 (중복된 아이템은 제거)
            unique_items = []
            
            for i, result in enumerate(results):
                if not result.is_duplicate:
                    unique_items.append(items[i])
        
        elif self.config.removal_strategy == "keep_best":
            # 품질이 가장 좋은 아이템 유지 (현재는 첫 번째와 동일)
            unique_items = [items[i] for i, result in enumerate(results) if not result.is_duplicate]
        
        else:
            # 기본값: keep_first
            unique_items = [items[i] for i, result in enumerate(results) if not result.is_duplicate]
        
        self.logger.info(f"Removed {len(items) - len(unique_items)} duplicate items")
        
        return unique_items, results
    
    def get_duplicate_statistics(self, results: List[DuplicateResult]) -> Dict[str, Any]:
        """중복 검사 통계를 생성합니다."""
        if not results:
            return {}
        
        unique_count = sum(1 for r in results if not r.is_duplicate)
        duplicate_count = len(results) - unique_count
        
        # 중복 타입별 통계
        exact_duplicates = sum(1 for r in results if r.status == "exact_duplicate")
        fuzzy_duplicates = sum(1 for r in results if r.status == "fuzzy_duplicate")
        semantic_duplicates = sum(1 for r in results if r.status == "semantic_duplicate")
        
        # 유사도 점수 통계
        similarity_scores = [r.similarity_score for r in results if r.is_duplicate]
        avg_similarity = sum(similarity_scores) / len(similarity_scores) if similarity_scores else 0.0
        
        # 신뢰도 점수 통계
        confidence_scores = [r.confidence_score for r in results if r.is_duplicate]
        avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0.0
        
        return {
            "total_items": len(results),
            "unique_items": unique_count,
            "duplicate_items": duplicate_count,
            "duplication_rate": duplicate_count / len(results),
            "exact_duplicates": exact_duplicates,
            "fuzzy_duplicates": fuzzy_duplicates,
            "semantic_duplicates": semantic_duplicates,
            "average_similarity_score": avg_similarity,
            "average_confidence_score": avg_confidence,
            "detection_method": self.config.detection_method,
            "similarity_threshold": self.config.similarity_threshold,
            "processing_stats": self.processing_stats
        }
    
    def save_duplicate_report(self, results: List[DuplicateResult], output_path: str) -> bool:
        """중복 검사 리포트를 저장합니다."""
        try:
            report = {
                "report_version": "1.0.0",
                "generated_at": datetime.now().isoformat(),
                "configuration": {
                    "similarity_threshold": self.config.similarity_threshold,
                    "detection_method": self.config.detection_method,
                    "enable_text_normalization": self.config.enable_text_normalization,
                    "enable_hash_check": self.config.enable_hash_check,
                    "enable_semantic_similarity": self.config.enable_semantic_similarity,
                    "removal_strategy": self.config.removal_strategy,
                    "memory_efficient": self.config.memory_efficient
                },
                "statistics": self.get_duplicate_statistics(results),
                "detailed_results": [
                    {
                        "is_duplicate": r.is_duplicate,
                        "similarity_score": r.similarity_score,
                        "duplicate_of": r.duplicate_of,
                        "status": r.status,
                        "matched_items": r.matched_items,
                        "confidence_score": r.confidence_score,
                        "details": r.details,
                        "timestamp": r.timestamp
                    }
                    for r in results
                ]
            }
            
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"Duplicate report saved to {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving duplicate report: {e}")
            return False
    
    def clear_cache(self):
        """캐시를 정리합니다."""
        self.exact_hashes.clear()
        self.fuzzy_hashes.clear()
        
        if hasattr(self, 'text_contents'):
            self.text_contents.clear()
        
        if hasattr(self, 'document_ids'):
            self.document_ids.clear()
        self.duplicate_groups.clear()
        self.item_to_group.clear()
        
        # 통계 초기화
        self.processing_stats = {
            'total_processed': 0,
            'exact_duplicates': 0,
            'fuzzy_duplicates': 0,
            'semantic_duplicates': 0,
            'unique_items': 0
        }
        
        self.logger.info("Cache cleared")


def create_default_duplicate_remover() -> DuplicateRemover:
    """기본 설정으로 중복 제거기를 생성합니다."""
    config = DuplicateRemoverConfig(
        similarity_threshold=0.9,
        detection_method="fuzzy",
        enable_text_normalization=True,
        enable_hash_check=True,
        enable_semantic_similarity=SKLEARN_AVAILABLE,
        batch_size=1000,
        memory_efficient=True,
        removal_strategy="keep_first",
        log_level="INFO"
    )
    
    return DuplicateRemover(config)


if __name__ == "__main__":
    # 모듈 테스트
    print(f"Duplicate Remover Module v{__version__}")
    print(f"Author: {__author__}")
    print(f"Sklearn available: {SKLEARN_AVAILABLE}")
    
    # 샘플 테스트
    duplicate_remover = create_default_duplicate_remover()
    
    # 테스트 데이터
    test_items = [
        {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        },
        {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},  # 중복
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        },
        {
            "conversations": [
                {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                {"from": "gpt", "value": "Chart 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        },
        {
            "conversations": [
                {"from": "human", "value": "syncfusion datagrid 사용법을 알려주세요."},  # 퍼지 중복
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        }
    ]
    
    # 중복 검사 및 제거
    unique_items, results = duplicate_remover.remove_duplicates(test_items)
    
    print(f"\nOriginal items: {len(test_items)}")
    print(f"Unique items: {len(unique_items)}")
    
    for i, result in enumerate(results):
        print(f"\nItem {i+1}:")
        print(f"  Duplicate: {result.is_duplicate}")
        print(f"  Status: {result.status}")
        print(f"  Similarity: {result.similarity_score:.3f}")
        if result.duplicate_of:
            print(f"  Duplicate of: {result.duplicate_of}")
    
    # 통계 출력
    stats = duplicate_remover.get_duplicate_statistics(results)
    print(f"\nStatistics:")
    print(f"  Duplication rate: {stats['duplication_rate']:.3f}")
    print(f"  Exact duplicates: {stats['exact_duplicates']}")
    print(f"  Fuzzy duplicates: {stats['fuzzy_duplicates']}")
    print(f"  Semantic duplicates: {stats['semantic_duplicates']}")