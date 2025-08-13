#!/usr/bin/env python3
"""
통계 분석 모듈
데이터셋의 통계적 특성을 분석하고 검증하는 기능을 제공합니다.
"""

import re
import json
import logging
import math
import numpy as np
from typing import List, Dict, Any, Optional, Set, Tuple, Union
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from collections import Counter, defaultdict
import statistics

logger = logging.getLogger(__name__)


@dataclass
class StatisticsAnalyzerConfig:
    """통계 분석기 설정"""
    # 다양성 분석 설정
    diversity_analysis_enabled: bool = True
    min_vocabulary_size: int = 100
    min_topic_diversity: float = 0.7
    length_diversity_threshold: float = 0.5
    
    # 균형성 검증 설정
    balance_analysis_enabled: bool = True
    min_balance_ratio: float = 0.8
    component_balance_threshold: float = 0.7
    topic_balance_threshold: float = 0.6
    
    # 분포 분석 설정
    distribution_analysis_enabled: bool = True
    quality_distribution_bins: List[float] = field(default_factory=lambda: [0.0, 0.3, 0.5, 0.7, 0.9, 1.0])
    length_distribution_bins: List[int] = field(default_factory=lambda: [0, 100, 500, 1000, 2000, 5000])
    turn_distribution_bins: List[int] = field(default_factory=lambda: [0, 2, 5, 10, 15, 20])
    
    # 이상값 탐지 설정
    outlier_detection_enabled: bool = True
    outlier_method: str = "iqr"  # iqr, zscore, isolation
    outlier_threshold: float = 1.5
    min_samples_for_outlier: int = 10
    
    # 성능 최적화 설정
    batch_size: int = 1000
    max_workers: int = 4
    use_sampling: bool = False
    sample_size: int = 10000


@dataclass
class StatisticsResult:
    """통계 분석 결과"""
    total_samples: int = 0
    analysis_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    # 다양성 지표
    vocabulary_diversity: float = 0.0
    topic_diversity: float = 0.0
    length_diversity: float = 0.0
    
    # 균형성 지표
    component_balance: float = 0.0
    topic_balance: float = 0.0
    format_balance: float = 0.0
    
    # 분포 분석
    quality_distribution: Dict[str, int] = field(default_factory=dict)
    length_distribution: Dict[str, int] = field(default_factory=dict)
    turn_distribution: Dict[str, int] = field(default_factory=dict)
    
    # 이상값 분석
    outliers: Dict[str, List[int]] = field(default_factory=dict)
    outlier_statistics: Dict[str, Any] = field(default_factory=dict)
    
    # 상세 통계
    detailed_statistics: Dict[str, Any] = field(default_factory=dict)
    
    # 검증 결과
    validation_passed: bool = True
    validation_issues: List[str] = field(default_factory=list)
    validation_warnings: List[str] = field(default_factory=list)


class StatisticsAnalyzer:
    """통계 분석기 클래스"""
    
    def __init__(self, config: Optional[StatisticsAnalyzerConfig] = None):
        """
        통계 분석기를 초기화합니다.
        
        Args:
            config: 통계 분석기 설정
        """
        self.config = config or StatisticsAnalyzerConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 분석 설정
        self._setup_analysis_settings()
        
        # 주요 분류 사전
        self._setup_category_dictionaries()
    
    def _setup_analysis_settings(self):
        """분석 설정을 초기화합니다."""
        # 텍스트 분석 패턴
        self.text_patterns = {
            'words': re.compile(r'\b\w+\b'),
            'sentences': re.compile(r'[.!?]+'),
            'paragraphs': re.compile(r'\n\s*\n'),
            'code_blocks': re.compile(r'```[\s\S]*?```'),
            'urls': re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
            'emails': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        }
        
        # 통계 계산 설정
        self.statistical_methods = {
            'diversity': 'shannon_entropy',
            'balance': 'gini_coefficient',
            'outlier': 'iqr'
        }
    
    def _setup_category_dictionaries(self):
        """주요 분류 사전을 설정합니다."""
        # Syncfusion 주요 주제 분류
        self.syncfusion_topics = {
            'grid': ['datagrid', 'grid', 'pivotgrid', 'grouping'],
            'chart': ['chart', 'gauge', 'diagram'],
            'document': ['docio', 'xlsio', 'pdf', 'presentation'],
            'ui': ['winforms', 'wpf', 'blazor', 'maui', 'xamarin'],
            'data': ['olap', 'qtp', 'calculate', 'schedule'],
            'tools': ['tools', 'edit', 'htmlui', 'projio'],
            'viewer': ['pdfviewer', 'viewer']
        }
        
        # 품질 등급 분류
        self.quality_grades = {
            'excellent': (0.9, 1.0),
            'good': (0.7, 0.9),
            'fair': (0.5, 0.7),
            'poor': (0.0, 0.5)
        }
    
    def analyze_dataset(self, datasets: Dict[str, List[Dict[str, Any]]]) -> StatisticsResult:
        """
        전체 데이터셋을 분석합니다.
        
        Args:
            datasets: 포맷별 데이터셋
            
        Returns:
            통계 분석 결과
        """
        result = StatisticsResult()
        result.total_samples = sum(len(data) for data in datasets.values())
        
        if result.total_samples == 0:
            result.validation_passed = False
            result.validation_issues.append("데이터셋이 비어있음")
            return result
        
        # 다양성 분석
        if self.config.diversity_analysis_enabled:
            diversity_result = self._analyze_diversity(datasets)
            result.vocabulary_diversity = diversity_result['vocabulary']
            result.topic_diversity = diversity_result['topics']
            result.length_diversity = diversity_result['length']
            result.detailed_statistics['diversity'] = diversity_result
        
        # 균형성 분석
        if self.config.balance_analysis_enabled:
            balance_result = self._analyze_balance(datasets)
            result.component_balance = balance_result['component']
            result.topic_balance = balance_result['topic']
            result.format_balance = balance_result['format']
            result.detailed_statistics['balance'] = balance_result
        
        # 분포 분석
        if self.config.distribution_analysis_enabled:
            distribution_result = self._analyze_distributions(datasets)
            result.quality_distribution = distribution_result['quality']
            result.length_distribution = distribution_result['length']
            result.turn_distribution = distribution_result['turns']
            result.detailed_statistics['distributions'] = distribution_result
        
        # 이상값 탐지
        if self.config.outlier_detection_enabled:
            outlier_result = self._detect_outliers(datasets)
            result.outliers = outlier_result['outliers']
            result.outlier_statistics = outlier_result['statistics']
            result.detailed_statistics['outliers'] = outlier_result
        
        # 검증 수행
        self._validate_statistics(result)
        
        return result
    
    def _analyze_diversity(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """다양성을 분석합니다."""
        diversity_result = {}
        
        # 전체 텍스트 추출
        all_texts = []
        all_topics = []
        all_lengths = []
        
        for format_type, data in datasets.items():
            for item in data:
                # 텍스트 추출
                text = self._extract_text_for_analysis(item)
                if text:
                    all_texts.append(text)
                    all_lengths.append(len(text))
                    
                    # 주제 추출
                    topics = self._extract_topics(text)
                    all_topics.extend(topics)
        
        # 어휘 다양성
        if all_texts:
            vocabulary_diversity = self._calculate_vocabulary_diversity(all_texts)
            diversity_result['vocabulary'] = vocabulary_diversity
        
        # 주제 다양성
        if all_topics:
            topic_diversity = self._calculate_topic_diversity(all_topics)
            diversity_result['topics'] = topic_diversity
        
        # 길이 다양성
        if all_lengths:
            length_diversity = self._calculate_length_diversity(all_lengths)
            diversity_result['length'] = length_diversity
        
        return diversity_result
    
    def _analyze_balance(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """균형성을 분석합니다."""
        balance_result = {}
        
        # 컴포넌트별 균형성
        component_balance = self._analyze_component_balance(datasets)
        balance_result['component'] = component_balance
        
        # 주제별 균형성
        topic_balance = self._analyze_topic_balance(datasets)
        balance_result['topic'] = topic_balance
        
        # 포맷별 균형성
        format_balance = self._analyze_format_balance(datasets)
        balance_result['format'] = format_balance
        
        return balance_result
    
    def _analyze_distributions(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """분포를 분석합니다."""
        distribution_result = {}
        
        # 품질 점수 분포
        quality_scores = []
        for format_type, data in datasets.items():
            for item in data:
                # 간단한 품질 점수 추정
                score = self._estimate_quality_score(item)
                quality_scores.append(score)
        
        if quality_scores:
            quality_distribution = self._create_distribution(quality_scores, self.config.quality_distribution_bins)
            distribution_result['quality'] = quality_distribution
        
        # 길이 분포
        lengths = []
        for format_type, data in datasets.items():
            for item in data:
                text = self._extract_text_for_analysis(item)
                if text:
                    lengths.append(len(text))
        
        if lengths:
            length_distribution = self._create_distribution(lengths, self.config.length_distribution_bins)
            distribution_result['length'] = length_distribution
        
        # 턴 수 분포
        turn_counts = []
        for format_type, data in datasets.items():
            for item in data:
                turn_count = self._count_turns(item)
                turn_counts.append(turn_count)
        
        if turn_counts:
            turn_distribution = self._create_distribution(turn_counts, self.config.turn_distribution_bins)
            distribution_result['turns'] = turn_distribution
        
        return distribution_result
    
    def _detect_outliers(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """이상값을 탐지합니다."""
        outlier_result = {'outliers': {}, 'statistics': {}}
        
        # 길이 이상값 탐지
        lengths = []
        item_indices = []
        
        for format_type, data in datasets.items():
            for i, item in enumerate(data):
                text = self._extract_text_for_analysis(item)
                if text:
                    lengths.append(len(text))
                    item_indices.append((format_type, i))
        
        if len(lengths) >= self.config.min_samples_for_outlier:
            length_outliers = self._detect_outliers_by_length(lengths, item_indices)
            outlier_result['outliers']['length'] = length_outliers
            outlier_result['statistics']['length'] = {
                'mean': np.mean(lengths),
                'median': np.median(lengths),
                'std': np.std(lengths),
                'min': np.min(lengths),
                'max': np.max(lengths)
            }
        
        # 품질 점수 이상값 탐지
        quality_scores = []
        quality_indices = []
        
        for format_type, data in datasets.items():
            for i, item in enumerate(data):
                score = self._estimate_quality_score(item)
                quality_scores.append(score)
                quality_indices.append((format_type, i))
        
        if len(quality_scores) >= self.config.min_samples_for_outlier:
            quality_outliers = self._detect_outliers_by_quality(quality_scores, quality_indices)
            outlier_result['outliers']['quality'] = quality_outliers
            outlier_result['statistics']['quality'] = {
                'mean': np.mean(quality_scores),
                'median': np.median(quality_scores),
                'std': np.std(quality_scores),
                'min': np.min(quality_scores),
                'max': np.max(quality_scores)
            }
        
        return outlier_result
    
    def _extract_text_for_analysis(self, item: Dict[str, Any]) -> str:
        """분석을 위한 텍스트를 추출합니다."""
        text_parts = []
        
        # 포맷별 텍스트 추출
        if "conversations" in item:
            for conv in item["conversations"]:
                text_parts.append(conv.get("value", ""))
        elif "instruction" in item and "output" in item:
            text_parts.append(item.get("instruction", ""))
            text_parts.append(item.get("output", ""))
        elif "messages" in item:
            for msg in item["messages"]:
                text_parts.append(msg.get("content", ""))
        else:
            # 일반 필드에서 텍스트 추출
            for field in ["instruction", "response", "input", "output", "content", "text"]:
                if field in item:
                    text_parts.append(str(item[field]))
        
        return " ".join(text_parts)
    
    def _extract_topics(self, text: str) -> List[str]:
        """텍스트에서 주제를 추출합니다."""
        topics = []
        text_lower = text.lower()
        
        # Syncfusion 주제 분류 기반 주제 추출
        for topic_name, keywords in self.syncfusion_topics.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    topics.append(topic_name)
                    break
        
        return topics
    
    def _calculate_vocabulary_diversity(self, texts: List[str]) -> float:
        """어휘 다양성을 계산합니다."""
        if not texts:
            return 0.0
        
        # 전체 단어 추출
        all_words = []
        for text in texts:
            words = self.text_patterns['words'].findall(text.lower())
            all_words.extend(words)
        
        if not all_words:
            return 0.0
        
        # 고유 단어 비율 계산
        unique_words = set(all_words)
        vocabulary_ratio = len(unique_words) / len(all_words)
        
        # 샤넌 엔트로피 계산
        word_counts = Counter(all_words)
        total_words = len(all_words)
        
        entropy = 0.0
        for count in word_counts.values():
            probability = count / total_words
            if probability > 0:
                entropy -= probability * math.log2(probability)
        
        # 정규화된 다양성 점수
        max_entropy = math.log2(len(unique_words)) if len(unique_words) > 1 else 1.0
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0.0
        
        # 종합 다양성 점수
        diversity_score = (vocabulary_ratio + normalized_entropy) / 2
        
        return min(1.0, diversity_score)
    
    def _calculate_topic_diversity(self, topics: List[str]) -> float:
        """주제 다양성을 계산합니다."""
        if not topics:
            return 0.0
        
        # 주제 분포 계산
        topic_counts = Counter(topics)
        total_topics = len(topics)
        
        # 샤넌 엔트로피 계산
        entropy = 0.0
        for count in topic_counts.values():
            probability = count / total_topics
            if probability > 0:
                entropy -= probability * math.log2(probability)
        
        # 정규화된 주제 다양성
        max_entropy = math.log2(len(topic_counts)) if len(topic_counts) > 1 else 1.0
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0.0
        
        return min(1.0, normalized_entropy)
    
    def _calculate_length_diversity(self, lengths: List[int]) -> float:
        """길이 다양성을 계산합니다."""
        if not lengths:
            return 0.0
        
        # 길이 범위 계산
        min_length = min(lengths)
        max_length = max(lengths)
        
        if min_length == max_length:
            return 0.0
        
        # 표준편차 계산
        std_dev = statistics.stdev(lengths) if len(lengths) > 1 else 0.0
        
        # 변동 계수 계산
        mean_length = statistics.mean(lengths)
        coefficient_of_variation = std_dev / mean_length if mean_length > 0 else 0.0
        
        # 정규화된 길이 다양성
        diversity_score = min(1.0, coefficient_of_variation * 2)
        
        return diversity_score
    
    def _analyze_component_balance(self, datasets: Dict[str, List[Dict[str, Any]]]) -> float:
        """컴포넌트별 균형성을 분석합니다."""
        component_counts = defaultdict(int)
        
        for format_type, data in datasets.items():
            for item in data:
                topics = self._extract_topics(self._extract_text_for_analysis(item))
                for topic in topics:
                    component_counts[topic] += 1
        
        if not component_counts:
            return 1.0
        
        # 지니 계수 계산
        total = sum(component_counts.values())
        if total == 0:
            return 1.0
        
        # 비율 계산
        proportions = [count / total for count in component_counts.values()]
        
        # 지니 계수 계산
        n = len(proportions)
        gini = 0.0
        for i in range(n):
            for j in range(n):
                gini += abs(proportions[i] - proportions[j])
        
        gini = gini / (2 * n * n)
        
        # 균형성 점수 (지니 계수가 낮을수록 균형이 좋음)
        balance_score = 1.0 - gini
        
        return max(0.0, min(1.0, balance_score))
    
    def _analyze_topic_balance(self, datasets: Dict[str, List[Dict[str, Any]]]) -> float:
        """주제별 균형성을 분석합니다."""
        # 컴포넌트 균형성과 동일한 방식으로 계산
        return self._analyze_component_balance(datasets)
    
    def _analyze_format_balance(self, datasets: Dict[str, List[Dict[str, Any]]]) -> float:
        """포맷별 균형성을 분석합니다."""
        format_counts = {format_type: len(data) for format_type, data in datasets.items()}
        
        if not format_counts:
            return 1.0
        
        total = sum(format_counts.values())
        if total == 0:
            return 1.0
        
        # 비율 계산
        proportions = [count / total for count in format_counts.values()]
        
        # 지니 계수 계산
        n = len(proportions)
        gini = 0.0
        for i in range(n):
            for j in range(n):
                gini += abs(proportions[i] - proportions[j])
        
        gini = gini / (2 * n * n)
        
        # 균형성 점수
        balance_score = 1.0 - gini
        
        return max(0.0, min(1.0, balance_score))
    
    def _create_distribution(self, values: List[Union[int, float]], bins: List[Union[int, float]]) -> Dict[str, int]:
        """분포를 생성합니다."""
        if not values:
            return {}
        
        # 히스토그램 계산
        hist, bin_edges = np.histogram(values, bins=bins)
        
        # 분포 딕셔너리 생성
        distribution = {}
        for i in range(len(hist)):
            bin_start = bin_edges[i]
            bin_end = bin_edges[i + 1]
            bin_key = f"{bin_start}-{bin_end}"
            distribution[bin_key] = int(hist[i])
        
        return distribution
    
    def _count_turns(self, item: Dict[str, Any]) -> int:
        """대화 턴 수를 계산합니다."""
        if "conversations" in item:
            return len(item["conversations"])
        elif "messages" in item:
            return len(item["messages"])
        else:
            return 1
    
    def _estimate_quality_score(self, item: Dict[str, Any]) -> float:
        """품질 점수를 추정합니다."""
        # 간단한 품질 점수 추정
        text = self._extract_text_for_analysis(item)
        
        if not text:
            return 0.0
        
        # 길이 점수
        length_score = min(1.0, len(text) / 1000)
        
        # 구조 점수
        structure_score = 0.0
        if "conversations" in item and len(item["conversations"]) >= 2:
            structure_score = 1.0
        elif "instruction" in item and "output" in item:
            structure_score = 0.8
        elif "messages" in item and len(item["messages"]) >= 2:
            structure_score = 0.8
        
        # 종합 점수
        quality_score = (length_score + structure_score) / 2
        
        return max(0.0, min(1.0, quality_score))
    
    def _detect_outliers_by_length(self, lengths: List[int], item_indices: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
        """길이 기반 이상값을 탐지합니다."""
        outliers = []
        
        # IQR 방법 사용
        if self.config.outlier_method == "iqr":
            q1 = np.percentile(lengths, 25)
            q3 = np.percentile(lengths, 75)
            iqr = q3 - q1
            
            lower_bound = q1 - self.config.outlier_threshold * iqr
            upper_bound = q3 + self.config.outlier_threshold * iqr
            
            for i, length in enumerate(lengths):
                if length < lower_bound or length > upper_bound:
                    format_type, item_idx = item_indices[i]
                    outliers.append((format_type, item_idx))
        
        # Z-score 방법 사용
        elif self.config.outlier_method == "zscore":
            mean = np.mean(lengths)
            std = np.std(lengths)
            
            if std > 0:
                for i, length in enumerate(lengths):
                    z_score = abs((length - mean) / std)
                    if z_score > self.config.outlier_threshold:
                        format_type, item_idx = item_indices[i]
                        outliers.append((format_type, item_idx))
        
        return outliers
    
    def _detect_outliers_by_quality(self, quality_scores: List[float], item_indices: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
        """품질 점수 기반 이상값을 탐지합니다."""
        outliers = []
        
        # IQR 방법 사용
        if self.config.outlier_method == "iqr":
            q1 = np.percentile(quality_scores, 25)
            q3 = np.percentile(quality_scores, 75)
            iqr = q3 - q1
            
            lower_bound = q1 - self.config.outlier_threshold * iqr
            upper_bound = q3 + self.config.outlier_threshold * iqr
            
            for i, score in enumerate(quality_scores):
                if score < lower_bound or score > upper_bound:
                    format_type, item_idx = item_indices[i]
                    outliers.append((format_type, item_idx))
        
        # Z-score 방법 사용
        elif self.config.outlier_method == "zscore":
            mean = np.mean(quality_scores)
            std = np.std(quality_scores)
            
            if std > 0:
                for i, score in enumerate(quality_scores):
                    z_score = abs((score - mean) / std)
                    if z_score > self.config.outlier_threshold:
                        format_type, item_idx = item_indices[i]
                        outliers.append((format_type, item_idx))
        
        return outliers
    
    def _validate_statistics(self, result: StatisticsResult):
        """통계 결과를 검증합니다."""
        validation_issues = []
        validation_warnings = []
        
        # 다양성 검증
        if result.vocabulary_diversity < 0.5:
            validation_warnings.append("어휘 다양성이 낮음")
        
        if result.topic_diversity < self.config.min_topic_diversity:
            validation_warnings.append("주제 다양성이 기준 미달")
        
        if result.length_diversity < self.config.length_diversity_threshold:
            validation_warnings.append("길이 다양성이 낮음")
        
        # 균형성 검증
        if result.component_balance < self.config.component_balance_threshold:
            validation_warnings.append("컴포넌트 균형성이 낮음")
        
        if result.topic_balance < self.config.topic_balance_threshold:
            validation_warnings.append("주제 균형성이 낮음")
        
        if result.format_balance < self.config.min_balance_ratio:
            validation_warnings.append("포맷 균형성이 낮음")
        
        # 이상값 검증
        total_outliers = sum(len(outliers) for outliers in result.outliers.values())
        if total_outliers > result.total_samples * 0.1:  # 10% 이상 이상값
            validation_warnings.append(f"이상값 비율이 높음: {total_outliers}/{result.total_samples}")
        
        # 결과 업데이트
        result.validation_issues = validation_issues
        result.validation_warnings = validation_warnings
        result.validation_passed = len(validation_issues) == 0
    
    def batch_analyze_datasets(self, dataset_batches: List[Dict[str, List[Dict[str, Any]]]]) -> List[StatisticsResult]:
        """
        배치로 데이터셋을 분석합니다.
        
        Args:
            dataset_batches: 데이터셋 배치 목록
            
        Returns:
            통계 분석 결과 목록
        """
        results = []
        
        for i, datasets in enumerate(dataset_batches):
            try:
                result = self.analyze_dataset(datasets)
                results.append(result)
                
                # 진행률 로깅
                if (i + 1) % 10 == 0:
                    self.logger.info(f"Processed {i + 1}/{len(dataset_batches)} batches")
                    
            except Exception as e:
                self.logger.error(f"Error analyzing dataset batch {i}: {e}")
                # 오류 발생 시 기본 결과 반환
                error_result = StatisticsResult()
                error_result.total_samples = sum(len(data) for data in datasets.values()) if datasets else 0
                error_result.validation_passed = False
                error_result.validation_issues.append(f"분석 오류: {str(e)}")
                results.append(error_result)
        
        return results
    
    def get_statistics_summary(self, result: StatisticsResult) -> Dict[str, Any]:
        """통계 요약 정보를 생성합니다."""
        summary = {
            "total_samples": result.total_samples,
            "analysis_timestamp": result.analysis_timestamp,
            "validation_passed": result.validation_passed,
            "validation_issues": result.validation_issues,
            "validation_warnings": result.validation_warnings
        }
        
        # 다양성 요약
        summary["diversity"] = {
            "vocabulary_diversity": result.vocabulary_diversity,
            "topic_diversity": result.topic_diversity,
            "length_diversity": result.length_diversity
        }
        
        # 균형성 요약
        summary["balance"] = {
            "component_balance": result.component_balance,
            "topic_balance": result.topic_balance,
            "format_balance": result.format_balance
        }
        
        # 분포 요약
        summary["distributions"] = {
            "quality_distribution": result.quality_distribution,
            "length_distribution": result.length_distribution,
            "turn_distribution": result.turn_distribution
        }
        
        # 이상값 요약
        summary["outliers"] = {
            "total_outliers": sum(len(outliers) for outliers in result.outliers.values()),
            "outliers_by_type": {k: len(v) for k, v in result.outliers.items()}
        }
        
        return summary


if __name__ == "__main__":
    # 테스트 데이터
    test_datasets = {
        "sharegpt": [
            {
                "conversations": [
                    {"from": "system", "value": "Syncfusion WinForms 전문가"},
                    {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                    {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."}
                ]
            },
            {
                "conversations": [
                    {"from": "system", "value": "Syncfusion WinForms 전문가"},
                    {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                    {"from": "gpt", "value": "Chart 컴포넌트 사용법은 다음과 같습니다..."}
                ]
            }
        ],
        "alpaca": [
            {
                "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
                "input": "초보자도 이해할 수 있도록 설명해주세요.",
                "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용"
            },
            {
                "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
                "input": "데이터 바인딩 포함해서 설명해주세요.",
                "output": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가"
            }
        ],
        "openai": [
            {
                "messages": [
                    {"role": "system", "content": "Syncfusion WinForms 전문가"},
                    {"role": "user", "content": "DataGrid 사용법을 알려주세요."},
                    {"role": "assistant", "content": "DataGrid 사용법은 다음과 같습니다..."}
                ]
            },
            {
                "messages": [
                    {"role": "system", "content": "Syncfusion WinForms 전문가"},
                    {"role": "user", "content": "Chart 컴포넌트 사용법을 알려주세요."},
                    {"role": "assistant", "content": "Chart 컴포넌트 사용법은 다음과 같습니다..."}
                ]
            }
        ]
    }
    
    # 통계 분석기 생성
    statistics_analyzer = StatisticsAnalyzer()
    
    print("=== Statistics Analyzer Test ===")
    
    # 데이터셋 분석 테스트
    result = statistics_analyzer.analyze_dataset(test_datasets)
    
    # 결과 출력
    print(f"Total Samples: {result.total_samples}")
    print(f"Analysis Timestamp: {result.analysis_timestamp}")
    print(f"Validation Passed: {result.validation_passed}")
    print(f"Validation Issues: {result.validation_issues}")
    print(f"Validation Warnings: {result.validation_warnings}")
    
    print(f"\n=== Diversity Analysis ===")
    print(f"Vocabulary Diversity: {result.vocabulary_diversity:.3f}")
    print(f"Topic Diversity: {result.topic_diversity:.3f}")
    print(f"Length Diversity: {result.length_diversity:.3f}")
    
    print(f"\n=== Balance Analysis ===")
    print(f"Component Balance: {result.component_balance:.3f}")
    print(f"Topic Balance: {result.topic_balance:.3f}")
    print(f"Format Balance: {result.format_balance:.3f}")
    
    print(f"\n=== Distribution Analysis ===")
    print(f"Quality Distribution: {result.quality_distribution}")
    print(f"Length Distribution: {result.length_distribution}")
    print(f"Turn Distribution: {result.turn_distribution}")
    
    print(f"\n=== Outlier Analysis ===")
    print(f"Outliers: {result.outliers}")
    print(f"Outlier Statistics: {result.outlier_statistics}")
    
    # 요약 정보 출력
    summary = statistics_analyzer.get_statistics_summary(result)
    print(f"\n=== Summary ===")
    print(json.dumps(summary, indent=2, ensure_ascii=False))