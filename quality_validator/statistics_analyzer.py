#!/usr/bin/env python3
"""
통계 분석기 모듈
데이터셋의 상세한 통계 분석을 수행합니다.
"""

import logging
import re
from typing import List, Dict, Any, Optional, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json
from pathlib import Path
from collections import Counter, defaultdict
import math

__version__ = "1.0.0"
__author__ = "Statistics Analyzer Team"


@dataclass
class StatisticsAnalyzerConfig:
    """통계 분석기 설정"""
    # 분석 활성화 옵션
    enable_basic_statistics: bool = True
    enable_content_analysis: bool = True
    enable_quality_analysis: bool = True
    enable_diversity_analysis: bool = True
    enable_balance_analysis: bool = True
    
    # 분석 세부 설정
    min_word_frequency: int = 2
    max_vocabulary_size: int = 10000
    topic_analysis_depth: int = 50
    
    # 언어 설정
    language: str = "ko"
    
    # 로깅 레벨
    log_level: str = "INFO"


@dataclass
class StatisticsResult:
    """통계 분석 결과"""
    total_samples: int
    basic_statistics: Dict[str, Any] = field(default_factory=dict)
    content_statistics: Dict[str, Any] = field(default_factory=dict)
    quality_statistics: Dict[str, Any] = field(default_factory=dict)
    diversity_statistics: Dict[str, Any] = field(default_factory=dict)
    balance_statistics: Dict[str, Any] = field(default_factory=dict)
    
    # 다양성 메트릭
    vocabulary_diversity: float = 0.0
    topic_diversity: float = 0.0
    length_diversity: float = 0.0
    
    # 균형 메트릭
    component_balance: float = 0.0
    topic_balance: float = 0.0
    format_balance: float = 0.0
    
    # 검증 결과
    validation_passed: bool = True
    validation_issues: List[str] = field(default_factory=list)
    validation_warnings: List[str] = field(default_factory=list)
    
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


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
        
        # 로깅 설정
        self._setup_logging()
        
        # 분석 도구 초기화
        self._initialize_analysis_tools()
        
        self.logger.info("StatisticsAnalyzer initialized successfully")
    
    def _setup_logging(self):
        """로깅을 설정합니다."""
        level = getattr(logging, self.config.log_level.upper(), logging.INFO)
        self.logger.setLevel(level)
    
    def _initialize_analysis_tools(self):
        """분석 도구를 초기화합니다."""
        # Syncfusion WinForms 관련 키워드
        self.component_keywords = {
            "DataGrid": ["datagrid", "grid", "table", "데이터그리드", "그리드", "테이블"],
            "Chart": ["chart", "graph", "plot", "차트", "그래프", "플롯"],
            "Gauge": ["gauge", "meter", "indicator", "게이지", "미터", "지시계"],
            "TreeView": ["treeview", "tree", "hierarchy", "트리뷰", "트리", "계층"],
            "ListView": ["listview", "list", "목록뷰", "리스트"],
            "ComboBox": ["combobox", "dropdown", "콤보박스", "드롭다운"],
            "Button": ["button", "btn", "버튼"],
            "TextBox": ["textbox", "input", "텍스트박스", "입력"],
            "Form": ["form", "window", "폼", "윈도우", "창"],
            "Dialog": ["dialog", "modal", "popup", "다이얼로그", "모달", "팝업"]
        }
        
        # 기술적 주제 키워드
        self.topic_keywords = {
            "데이터바인딩": ["databinding", "binding", "datasource", "데이터바인딩", "바인딩", "데이터소스"],
            "이벤트처리": ["event", "handler", "click", "이벤트", "핸들러", "클릭"],
            "스타일링": ["style", "theme", "appearance", "스타일", "테마", "외관"],
            "레이아웃": ["layout", "positioning", "alignment", "레이아웃", "위치", "정렬"],
            "성능최적화": ["performance", "optimization", "efficiency", "성능", "최적화", "효율"],
            "커스터마이징": ["customization", "custom", "personalization", "커스터마이징", "사용자정의"],
            "데이터처리": ["data", "processing", "manipulation", "데이터", "처리", "조작"],
            "UI/UX": ["ui", "ux", "interface", "experience", "인터페이스", "사용자경험"]
        }
        
        # 품질 지표 키워드
        self.quality_keywords = {
            "positive": [
                "예제", "샘플", "단계별", "방법", "설명", "가이드", "튜토리얼",
                "구현", "사용법", "활용", "적용", "설정", "구성", "초기화"
            ],
            "negative": [
                "모름", "잘못", "오류", "에러", "실패", "불가능", "안됨",
                "문제", "버그", "이상", "비정상"
            ]
        }
        
        self.logger.info("Analysis tools initialized")
    
    def analyze_dataset(self, datasets: Dict[str, List[Dict[str, Any]]]) -> StatisticsResult:
        """
        데이터셋을 분석합니다.
        
        Args:
            datasets: 포맷별 데이터셋
            
        Returns:
            통계 분석 결과
        """
        try:
            total_samples = sum(len(items) for items in datasets.values())
            
            if total_samples == 0:
                return StatisticsResult(
                    total_samples=0,
                    validation_passed=False,
                    validation_issues=["No samples found in dataset"]
                )
            
            result = StatisticsResult(total_samples=total_samples)
            
            # 기본 통계 분석
            if self.config.enable_basic_statistics:
                result.basic_statistics = self._analyze_basic_statistics(datasets)
            
            # 콘텐츠 분석
            if self.config.enable_content_analysis:
                result.content_statistics = self._analyze_content_statistics(datasets)
            
            # 품질 분석
            if self.config.enable_quality_analysis:
                result.quality_statistics = self._analyze_quality_statistics(datasets)
            
            # 다양성 분석
            if self.config.enable_diversity_analysis:
                diversity_metrics = self._analyze_diversity(datasets)
                result.diversity_statistics = diversity_metrics
                result.vocabulary_diversity = diversity_metrics.get("vocabulary_diversity", 0.0)
                result.topic_diversity = diversity_metrics.get("topic_diversity", 0.0)
                result.length_diversity = diversity_metrics.get("length_diversity", 0.0)
            
            # 균형 분석
            if self.config.enable_balance_analysis:
                balance_metrics = self._analyze_balance(datasets)
                result.balance_statistics = balance_metrics
                result.component_balance = balance_metrics.get("component_balance", 0.0)
                result.topic_balance = balance_metrics.get("topic_balance", 0.0)
                result.format_balance = balance_metrics.get("format_balance", 0.0)
            
            # 검증 수행
            result = self._validate_dataset_quality(result, datasets)
            
            self.logger.info(f"Dataset analysis completed: {total_samples} samples analyzed")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error in dataset analysis: {e}")
            return StatisticsResult(
                total_samples=0,
                validation_passed=False,
                validation_issues=[f"Analysis error: {str(e)}"]
            )
    
    def _analyze_basic_statistics(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """기본 통계를 분석합니다."""
        stats = {
            "total_formats": len(datasets),
            "format_distribution": {},
            "total_conversations": 0,
            "total_words": 0,
            "total_characters": 0,
            "average_words_per_sample": 0.0,
            "average_characters_per_sample": 0.0
        }
        
        total_samples = 0
        total_words = 0
        total_characters = 0
        
        for format_type, items in datasets.items():
            format_stats = {
                "sample_count": len(items),
                "word_count": 0,
                "character_count": 0,
                "average_words": 0.0,
                "average_characters": 0.0
            }
            
            for item in items:
                text_content = self._extract_text_content(item, format_type)
                words = len(text_content.split())
                characters = len(text_content)
                
                format_stats["word_count"] += words
                format_stats["character_count"] += characters
                total_words += words
                total_characters += characters
            
            if len(items) > 0:
                format_stats["average_words"] = format_stats["word_count"] / len(items)
                format_stats["average_characters"] = format_stats["character_count"] / len(items)
            
            stats["format_distribution"][format_type] = format_stats
            total_samples += len(items)
        
        stats["total_conversations"] = total_samples
        stats["total_words"] = total_words
        stats["total_characters"] = total_characters
        
        if total_samples > 0:
            stats["average_words_per_sample"] = total_words / total_samples
            stats["average_characters_per_sample"] = total_characters / total_samples
        
        return stats
    
    def _analyze_content_statistics(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """콘텐츠 통계를 분석합니다."""
        stats = {
            "vocabulary": {},
            "word_frequency": {},
            "sentence_statistics": {},
            "code_statistics": {},
            "technical_content": {}
        }
        
        # 전체 텍스트 수집
        all_texts = []
        for format_type, items in datasets.items():
            for item in items:
                text_content = self._extract_text_content(item, format_type)
                all_texts.append(text_content)
        
        # 어휘 분석
        all_words = []
        for text in all_texts:
            words = re.findall(r'\b\w+\b', text.lower())
            all_words.extend(words)
        
        word_counter = Counter(all_words)
        unique_words = len(word_counter)
        total_words = len(all_words)
        
        stats["vocabulary"] = {
            "unique_words": unique_words,
            "total_words": total_words,
            "vocabulary_richness": unique_words / total_words if total_words > 0 else 0,
            "most_common_words": word_counter.most_common(20)
        }
        
        # 단어 빈도 분석
        frequent_words = {word: count for word, count in word_counter.items() 
                         if count >= self.config.min_word_frequency}
        stats["word_frequency"] = {
            "frequent_words_count": len(frequent_words),
            "frequency_distribution": dict(Counter(frequent_words.values()).most_common(10))
        }
        
        # 문장 통계
        all_sentences = []
        for text in all_texts:
            sentences = re.split(r'[.!?]', text)
            sentences = [s.strip() for s in sentences if s.strip()]
            all_sentences.extend(sentences)
        
        sentence_lengths = [len(s.split()) for s in all_sentences]
        
        stats["sentence_statistics"] = {
            "total_sentences": len(all_sentences),
            "average_sentence_length": sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0,
            "min_sentence_length": min(sentence_lengths) if sentence_lengths else 0,
            "max_sentence_length": max(sentence_lengths) if sentence_lengths else 0,
            "sentence_length_std": self._calculate_std(sentence_lengths)
        }
        
        # 코드 통계
        code_blocks = []
        inline_codes = []
        for text in all_texts:
            # 코드 블록 찾기
            code_blocks.extend(re.findall(r'```.*?\n(.*?)\n```', text, re.DOTALL))
            # 인라인 코드 찾기
            inline_codes.extend(re.findall(r'`([^`]+)`', text))
        
        stats["code_statistics"] = {
            "code_blocks_count": len(code_blocks),
            "inline_codes_count": len(inline_codes),
            "total_code_lines": sum(len(block.split('\n')) for block in code_blocks),
            "average_code_block_length": sum(len(block.split('\n')) for block in code_blocks) / len(code_blocks) if code_blocks else 0
        }
        
        # 기술적 콘텐츠 분석
        component_mentions = defaultdict(int)
        topic_mentions = defaultdict(int)
        
        combined_text = ' '.join(all_texts).lower()
        
        for component, keywords in self.component_keywords.items():
            for keyword in keywords:
                component_mentions[component] += combined_text.count(keyword.lower())
        
        for topic, keywords in self.topic_keywords.items():
            for keyword in keywords:
                topic_mentions[topic] += combined_text.count(keyword.lower())
        
        stats["technical_content"] = {
            "component_mentions": dict(component_mentions),
            "topic_mentions": dict(topic_mentions),
            "most_mentioned_component": max(component_mentions.items(), key=lambda x: x[1]) if component_mentions else None,
            "most_mentioned_topic": max(topic_mentions.items(), key=lambda x: x[1]) if topic_mentions else None
        }
        
        return stats
    
    def _analyze_quality_statistics(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """품질 통계를 분석합니다."""
        stats = {
            "quality_indicators": {},
            "completeness_metrics": {},
            "coherence_metrics": {},
            "technical_accuracy": {}
        }
        
        # 전체 텍스트 수집
        all_texts = []
        conversation_pairs = []
        
        for format_type, items in datasets.items():
            for item in items:
                text_content = self._extract_text_content(item, format_type)
                all_texts.append(text_content)
                
                # 대화 쌍 추출
                pairs = self._extract_conversation_pairs(item, format_type)
                conversation_pairs.extend(pairs)
        
        # 품질 지표 분석
        positive_indicators = 0
        negative_indicators = 0
        
        combined_text = ' '.join(all_texts).lower()
        
        for keyword in self.quality_keywords["positive"]:
            positive_indicators += combined_text.count(keyword)
        
        for keyword in self.quality_keywords["negative"]:
            negative_indicators += combined_text.count(keyword)
        
        stats["quality_indicators"] = {
            "positive_indicators": positive_indicators,
            "negative_indicators": negative_indicators,
            "quality_ratio": positive_indicators / (positive_indicators + negative_indicators) if (positive_indicators + negative_indicators) > 0 else 0.5
        }
        
        # 완성도 메트릭
        text_lengths = [len(text) for text in all_texts]
        short_texts = sum(1 for length in text_lengths if length < 100)
        long_texts = sum(1 for length in text_lengths if length > 1000)
        
        stats["completeness_metrics"] = {
            "average_text_length": sum(text_lengths) / len(text_lengths) if text_lengths else 0,
            "short_texts_ratio": short_texts / len(text_lengths) if text_lengths else 0,
            "long_texts_ratio": long_texts / len(text_lengths) if text_lengths else 0,
            "length_variance": self._calculate_variance(text_lengths)
        }
        
        # 일관성 메트릭
        if conversation_pairs:
            coherence_scores = []
            for query, response in conversation_pairs:
                # 단순한 일관성 점수 (공통 단어 비율)
                query_words = set(query.lower().split())
                response_words = set(response.lower().split())
                
                if len(query_words) > 0:
                    common_words = query_words.intersection(response_words)
                    coherence_score = len(common_words) / len(query_words)
                    coherence_scores.append(coherence_score)
            
            stats["coherence_metrics"] = {
                "average_coherence": sum(coherence_scores) / len(coherence_scores) if coherence_scores else 0,
                "coherence_variance": self._calculate_variance(coherence_scores),
                "high_coherence_ratio": sum(1 for score in coherence_scores if score > 0.3) / len(coherence_scores) if coherence_scores else 0
            }
        
        # 기술적 정확성
        technical_terms = 0
        code_examples = 0
        
        for text in all_texts:
            # 기술 용어 카운트
            for component_keywords in self.component_keywords.values():
                for keyword in component_keywords:
                    technical_terms += text.lower().count(keyword.lower())
            
            # 코드 예제 카운트
            code_examples += len(re.findall(r'```.*?```', text, re.DOTALL))
            code_examples += len(re.findall(r'`[^`]+`', text))
        
        stats["technical_accuracy"] = {
            "technical_terms_count": technical_terms,
            "code_examples_count": code_examples,
            "technical_density": technical_terms / len(all_texts) if all_texts else 0,
            "code_density": code_examples / len(all_texts) if all_texts else 0
        }
        
        return stats
    
    def _analyze_diversity(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """다양성을 분석합니다."""
        stats = {
            "vocabulary_diversity": 0.0,
            "topic_diversity": 0.0,
            "length_diversity": 0.0,
            "format_diversity": 0.0,
            "content_diversity": {}
        }
        
        # 어휘 다양성 (Type-Token Ratio)
        all_words = []
        for format_type, items in datasets.items():
            for item in items:
                text_content = self._extract_text_content(item, format_type)
                words = re.findall(r'\b\w+\b', text_content.lower())
                all_words.extend(words)
        
        unique_words = len(set(all_words))
        total_words = len(all_words)
        stats["vocabulary_diversity"] = unique_words / total_words if total_words > 0 else 0
        
        # 주제 다양성
        topic_distribution = defaultdict(int)
        total_samples = 0
        
        for format_type, items in datasets.items():
            for item in items:
                text_content = self._extract_text_content(item, format_type).lower()
                total_samples += 1
                
                for topic, keywords in self.topic_keywords.items():
                    for keyword in keywords:
                        if keyword.lower() in text_content:
                            topic_distribution[topic] += 1
                            break  # 한 번만 카운트
        
        # 엔트로피 기반 주제 다양성
        if total_samples > 0:
            topic_entropy = 0
            for count in topic_distribution.values():
                if count > 0:
                    prob = count / total_samples
                    topic_entropy -= prob * math.log2(prob)
            
            max_entropy = math.log2(len(self.topic_keywords)) if len(self.topic_keywords) > 0 else 1
            stats["topic_diversity"] = topic_entropy / max_entropy if max_entropy > 0 else 0
        
        # 길이 다양성
        text_lengths = []
        for format_type, items in datasets.items():
            for item in items:
                text_content = self._extract_text_content(item, format_type)
                text_lengths.append(len(text_content))
        
        if text_lengths:
            length_std = self._calculate_std(text_lengths)
            length_mean = sum(text_lengths) / len(text_lengths)
            stats["length_diversity"] = length_std / length_mean if length_mean > 0 else 0
        
        # 포맷 다양성
        format_counts = {format_type: len(items) for format_type, items in datasets.items()}
        total_items = sum(format_counts.values())
        
        if total_items > 0:
            format_entropy = 0
            for count in format_counts.values():
                if count > 0:
                    prob = count / total_items
                    format_entropy -= prob * math.log2(prob)
            
            max_format_entropy = math.log2(len(datasets)) if len(datasets) > 0 else 1
            stats["format_diversity"] = format_entropy / max_format_entropy if max_format_entropy > 0 else 0
        
        # 콘텐츠 다양성 세부 분석
        stats["content_diversity"] = {
            "topic_distribution": dict(topic_distribution),
            "length_distribution": {
                "short": sum(1 for length in text_lengths if length < 200),
                "medium": sum(1 for length in text_lengths if 200 <= length < 800),
                "long": sum(1 for length in text_lengths if length >= 800)
            },
            "vocabulary_richness": unique_words / total_words if total_words > 0 else 0
        }
        
        return stats
    
    def _analyze_balance(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """균형을 분석합니다."""
        stats = {
            "component_balance": 0.0,
            "topic_balance": 0.0,
            "format_balance": 0.0,
            "length_balance": 0.0,
            "balance_details": {}
        }
        
        # 컴포넌트 균형
        component_distribution = defaultdict(int)
        total_samples = 0
        
        for format_type, items in datasets.items():
            for item in items:
                text_content = self._extract_text_content(item, format_type).lower()
                total_samples += 1
                
                for component, keywords in self.component_keywords.items():
                    for keyword in keywords:
                        if keyword.lower() in text_content:
                            component_distribution[component] += 1
                            break
        
        # 균형 점수 계산 (표준편차 기반)
        if component_distribution:
            component_counts = list(component_distribution.values())
            component_mean = sum(component_counts) / len(component_counts)
            component_std = self._calculate_std(component_counts)
            stats["component_balance"] = 1 - (component_std / component_mean) if component_mean > 0 else 0
        
        # 주제 균형
        topic_distribution = defaultdict(int)
        
        for format_type, items in datasets.items():
            for item in items:
                text_content = self._extract_text_content(item, format_type).lower()
                
                for topic, keywords in self.topic_keywords.items():
                    for keyword in keywords:
                        if keyword.lower() in text_content:
                            topic_distribution[topic] += 1
                            break
        
        if topic_distribution:
            topic_counts = list(topic_distribution.values())
            topic_mean = sum(topic_counts) / len(topic_counts)
            topic_std = self._calculate_std(topic_counts)
            stats["topic_balance"] = 1 - (topic_std / topic_mean) if topic_mean > 0 else 0
        
        # 포맷 균형
        format_counts = [len(items) for items in datasets.values()]
        if format_counts:
            format_mean = sum(format_counts) / len(format_counts)
            format_std = self._calculate_std(format_counts)
            stats["format_balance"] = 1 - (format_std / format_mean) if format_mean > 0 else 0
        
        # 길이 균형
        text_lengths = []
        for format_type, items in datasets.items():
            for item in items:
                text_content = self._extract_text_content(item, format_type)
                text_lengths.append(len(text_content))
        
        if text_lengths:
            # 길이를 구간별로 분류
            short_count = sum(1 for length in text_lengths if length < 200)
            medium_count = sum(1 for length in text_lengths if 200 <= length < 800)
            long_count = sum(1 for length in text_lengths if length >= 800)
            
            length_counts = [short_count, medium_count, long_count]
            length_mean = sum(length_counts) / len(length_counts)
            length_std = self._calculate_std(length_counts)
            stats["length_balance"] = 1 - (length_std / length_mean) if length_mean > 0 else 0
        
        # 균형 세부 정보
        stats["balance_details"] = {
            "component_distribution": dict(component_distribution),
            "topic_distribution": dict(topic_distribution),
            "format_distribution": {format_type: len(items) for format_type, items in datasets.items()},
            "length_distribution": {
                "short": short_count if 'short_count' in locals() else 0,
                "medium": medium_count if 'medium_count' in locals() else 0,
                "long": long_count if 'long_count' in locals() else 0
            }
        }
        
        return stats
    
    def _validate_dataset_quality(self, result: StatisticsResult, datasets: Dict[str, List[Dict[str, Any]]]) -> StatisticsResult:
        """데이터셋 품질을 검증합니다."""
        issues = []
        warnings = []
        
        # 기본 검증
        if result.total_samples < 100:
            warnings.append("Dataset size is small (< 100 samples)")
        elif result.total_samples < 10:
            issues.append("Dataset size is too small (< 10 samples)")
        
        # 다양성 검증
        if result.vocabulary_diversity < 0.1:
            issues.append("Very low vocabulary diversity")
        elif result.vocabulary_diversity < 0.2:
            warnings.append("Low vocabulary diversity")
        
        if result.topic_diversity < 0.3:
            warnings.append("Low topic diversity")
        
        # 균형 검증
        if result.component_balance < 0.3:
            warnings.append("Poor component balance")
        
        if result.topic_balance < 0.3:
            warnings.append("Poor topic balance")
        
        if result.format_balance < 0.5:
            warnings.append("Poor format balance")
        
        # 콘텐츠 품질 검증
        if result.content_statistics:
            avg_length = result.basic_statistics.get("average_characters_per_sample", 0)
            if avg_length < 50:
                issues.append("Average content length is too short")
            elif avg_length < 100:
                warnings.append("Average content length is short")
        
        # 기술적 콘텐츠 검증
        if result.content_statistics.get("technical_content", {}).get("component_mentions"):
            total_mentions = sum(result.content_statistics["technical_content"]["component_mentions"].values())
            if total_mentions < result.total_samples * 0.5:
                warnings.append("Low technical content density")
        
        result.validation_issues = issues
        result.validation_warnings = warnings
        result.validation_passed = len(issues) == 0
        
        return result
    
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
    
    def _extract_conversation_pairs(self, item: Dict[str, Any], format_type: str) -> List[Tuple[str, str]]:
        """대화 쌍을 추출합니다."""
        pairs = []
        
        try:
            if format_type == "sharegpt":
                conversations = item.get("conversations", [])
                human_msg = ""
                
                for conv in conversations:
                    if conv.get("from") == "human":
                        human_msg = conv.get("value", "")
                    elif conv.get("from") == "gpt" and human_msg:
                        pairs.append((human_msg, conv.get("value", "")))
                        human_msg = ""
            
            elif format_type == "alpaca":
                instruction = item.get("instruction", "")
                input_text = item.get("input", "")
                output = item.get("output", "")
                
                if instruction and output:
                    query = instruction + (" " + input_text if input_text else "")
                    pairs.append((query, output))
            
            elif format_type == "openai":
                messages = item.get("messages", [])
                user_msg = ""
                
                for msg in messages:
                    if msg.get("role") == "user":
                        user_msg = msg.get("content", "")
                    elif msg.get("role") == "assistant" and user_msg:
                        pairs.append((user_msg, msg.get("content", "")))
                        user_msg = ""
            
            return pairs
            
        except Exception as e:
            self.logger.error(f"Error extracting conversation pairs: {e}")
            return []
    
    def _calculate_std(self, values: List[float]) -> float:
        """표준편차를 계산합니다."""
        if not values:
            return 0.0
        
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return math.sqrt(variance)
    
    def _calculate_variance(self, values: List[float]) -> float:
        """분산을 계산합니다."""
        if not values:
            return 0.0
        
        mean = sum(values) / len(values)
        return sum((x - mean) ** 2 for x in values) / len(values)
    
    def save_statistics_report(self, result: StatisticsResult, output_path: str) -> bool:
        """통계 리포트를 저장합니다."""
        try:
            report = {
                "report_version": "1.0.0",
                "generated_at": datetime.now().isoformat(),
                "configuration": {
                    "enable_basic_statistics": self.config.enable_basic_statistics,
                    "enable_content_analysis": self.config.enable_content_analysis,
                    "enable_quality_analysis": self.config.enable_quality_analysis,
                    "enable_diversity_analysis": self.config.enable_diversity_analysis,
                    "enable_balance_analysis": self.config.enable_balance_analysis,
                    "min_word_frequency": self.config.min_word_frequency,
                    "max_vocabulary_size": self.config.max_vocabulary_size,
                    "topic_analysis_depth": self.config.topic_analysis_depth
                },
                "summary": {
                    "total_samples": result.total_samples,
                    "vocabulary_diversity": result.vocabulary_diversity,
                    "topic_diversity": result.topic_diversity,
                    "length_diversity": result.length_diversity,
                    "component_balance": result.component_balance,
                    "topic_balance": result.topic_balance,
                    "format_balance": result.format_balance,
                    "validation_passed": result.validation_passed
                },
                "detailed_statistics": {
                    "basic_statistics": result.basic_statistics,
                    "content_statistics": result.content_statistics,
                    "quality_statistics": result.quality_statistics,
                    "diversity_statistics": result.diversity_statistics,
                    "balance_statistics": result.balance_statistics
                },
                "validation": {
                    "validation_passed": result.validation_passed,
                    "validation_issues": result.validation_issues,
                    "validation_warnings": result.validation_warnings
                },
                "timestamp": result.timestamp
            }
            
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"Statistics report saved to {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving statistics report: {e}")
            return False


def create_default_statistics_analyzer() -> StatisticsAnalyzer:
    """기본 설정으로 통계 분석기를 생성합니다."""
    config = StatisticsAnalyzerConfig(
        enable_basic_statistics=True,
        enable_content_analysis=True,
        enable_quality_analysis=True,
        enable_diversity_analysis=True,
        enable_balance_analysis=True,
        min_word_frequency=2,
        max_vocabulary_size=10000,
        topic_analysis_depth=50,
        language="ko",
        log_level="INFO"
    )
    
    return StatisticsAnalyzer(config)


if __name__ == "__main__":
    # 모듈 테스트
    print(f"Statistics Analyzer Module v{__version__}")
    print(f"Author: {__author__}")
    
    # 샘플 테스트
    statistics_analyzer = create_default_statistics_analyzer()
    
    # 테스트 데이터
    test_datasets = {
        "sharegpt": [
            {
                "conversations": [
                    {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                    {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다:\n\n1. 프로젝트에 참조 추가\n2. 컨트롤 배치\n3. 데이터 바인딩\n\n예제 코드:\n```csharp\nSfDataGrid dataGrid = new SfDataGrid();\n```"}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "Chart 컴포넌트로 막대 그래프를 만드는 방법을 알려주세요."},
                    {"from": "gpt", "value": "Chart 컴포넌트로 막대 그래프를 만드는 방법:\n\n1. SfChart 컨트롤 추가\n2. ColumnSeries 생성\n3. 데이터 바인딩"}
                ]
            }
        ],
        "alpaca": [
            {
                "instruction": "Gauge 컴포넌트 사용법을 설명해주세요.",
                "input": "초보자도 이해할 수 있도록 설명해주세요.",
                "output": "Gauge 컴포넌트는 다음과 같이 사용합니다:\n\n1. SfGauge 컨트롤 추가\n2. 범위 설정\n3. 값 바인딩"
            }
        ]
    }
    
    # 통계 분석
    result = statistics_analyzer.analyze_dataset(test_datasets)
    
    print(f"\nAnalysis Results:")
    print(f"  Total samples: {result.total_samples}")
    print(f"  Vocabulary diversity: {result.vocabulary_diversity:.3f}")
    print(f"  Topic diversity: {result.topic_diversity:.3f}")
    print(f"  Length diversity: {result.length_diversity:.3f}")
    print(f"  Component balance: {result.component_balance:.3f}")
    print(f"  Topic balance: {result.topic_balance:.3f}")
    print(f"  Format balance: {result.format_balance:.3f}")
    print(f"  Validation passed: {result.validation_passed}")
    
    if result.validation_issues:
        print(f"  Issues: {result.validation_issues}")
    
    if result.validation_warnings:
        print(f"  Warnings: {result.validation_warnings}")
    
    # 기본 통계
    if result.basic_statistics:
        print(f"\nBasic Statistics:")
        print(f"  Total words: {result.basic_statistics.get('total_words', 0)}")
        print(f"  Average words per sample: {result.basic_statistics.get('average_words_per_sample', 0):.1f}")
    
    # 콘텐츠 통계
    if result.content_statistics:
        vocab_stats = result.content_statistics.get('vocabulary', {})
        print(f"\nContent Statistics:")
        print(f"  Unique words: {vocab_stats.get('unique_words', 0)}")
        print(f"  Vocabulary richness: {vocab_stats.get('vocabulary_richness', 0):.3f}")
        
        tech_stats = result.content_statistics.get('technical_content', {})
        if tech_stats.get('most_mentioned_component'):
            print(f"  Most mentioned component: {tech_stats['most_mentioned_component'][0]} ({tech_stats['most_mentioned_component'][1]} times)")