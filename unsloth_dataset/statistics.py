#!/usr/bin/env python3
"""
데이터셋 통계 생성기 모듈
데이터셋의 품질 지표와 통계 정보를 생성하는 모듈입니다.
"""

import json
import logging
from typing import List, Dict, Any, Optional, Union, Tuple
from dataclasses import dataclass, asdict, field
from datetime import datetime
import re
import statistics
from collections import Counter, defaultdict

logger = logging.getLogger(__name__)


@dataclass
class DatasetStatistics:
    """데이터셋 통계 정보"""
    total_samples: int = 0
    format_statistics: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    quality_metrics: Dict[str, float] = field(default_factory=dict)
    diversity_metrics: Dict[str, float] = field(default_factory=dict)
    token_analysis: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    generated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환합니다."""
        return asdict(self)


@dataclass
class FormatStatistics:
    """포맷별 통계 정보"""
    sample_count: int = 0
    average_tokens: float = 0.0
    min_tokens: int = 0
    max_tokens: int = 0
    token_distribution: Dict[str, int] = field(default_factory=dict)
    field_analysis: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    quality_score: float = 0.0
    completeness_score: float = 0.0


class StatisticsGenerator:
    """통계 생성기"""
    
    def __init__(self):
        """통계 생성기를 초기화합니다."""
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 토큰 범위 분류
        self.token_ranges = {
            "very_short": (0, 100),
            "short": (100, 500),
            "medium": (500, 1500),
            "long": (1500, 3000),
            "very_long": (3000, float('inf'))
        }
    
    def generate_dataset_statistics(
        self, 
        datasets: Dict[str, List[Dict[str, Any]]]
    ) -> DatasetStatistics:
        """
        전체 데이터셋의 통계를 생성합니다.
        
        Args:
            datasets: 포맷별 데이터셋
            
        Returns:
            데이터셋 통계 정보
        """
        stats = DatasetStatistics()
        
        # 기본 통계
        stats.total_samples = sum(len(data) for data in datasets.values())
        
        # 포맷별 통계
        for format_type, data in datasets.items():
            format_stats = self.generate_format_statistics(data)
            stats.format_statistics[format_type] = format_stats
        
        # 전체 품질 지표
        stats.quality_metrics = self._calculate_quality_metrics(datasets)
        
        # 다양성 지표
        stats.diversity_metrics = self._calculate_diversity_metrics(datasets)
        
        # 토큰 분석
        stats.token_analysis = self._analyze_token_distribution(datasets)
        
        # 메타데이터
        stats.metadata = {
            "generator_version": "1.0.0",
            "total_formats": len(datasets),
            "analysis_timestamp": datetime.now().isoformat()
        }
        
        return stats
    
    def generate_format_statistics(
        self, 
        data: List[Dict[str, Any]], 
        validation_data: Optional[List[Dict[str, Any]]] = None
    ) -> FormatStatistics:
        """
        특정 포맷의 통계를 생성합니다.
        
        Args:
            data: 주 데이터셋
            validation_data: 검증 데이터셋 (선택적)
            
        Returns:
            포맷별 통계 정보
        """
        stats = FormatStatistics()
        stats.sample_count = len(data)
        
        if not data:
            return stats
        
        # 토큰 분석
        token_counts = [self._calculate_token_count(item) for item in data]
        stats.average_tokens = statistics.mean(token_counts) if token_counts else 0
        stats.min_tokens = min(token_counts) if token_counts else 0
        stats.max_tokens = max(token_counts) if token_counts else 0
        
        # 토큰 분포
        stats.token_distribution = self._categorize_tokens(token_counts)
        
        # 필드 분석
        stats.field_analysis = self._analyze_fields(data)
        
        # 품질 점수
        stats.quality_score = self._calculate_format_quality(data)
        
        # 완성도 점수
        stats.completeness_score = self._calculate_completeness(data)
        
        # 검증 데이터 통계 추가
        if validation_data:
            val_stats = self.generate_format_statistics([validation_data])
            stats.sample_count += val_stats.sample_count
            stats.average_tokens = (stats.average_tokens + val_stats.average_tokens) / 2
        
        return stats
    
    def _calculate_token_count(self, item: Dict[str, Any]) -> int:
        """아이템의 토큰 수를 계산합니다."""
        total_chars = 0
        
        # 포맷별 토큰 계산
        if "conversations" in item:
            for conv in item["conversations"]:
                total_chars += len(conv.get("value", ""))
        
        elif "instruction" in item:
            total_chars += len(item.get("instruction", ""))
            total_chars += len(item.get("output", ""))
            total_chars += len(item.get("input", ""))
        
        elif "messages" in item:
            for msg in item["messages"]:
                total_chars += len(msg.get("content", ""))
        
        # 평균 토큰 길이를 4로 가정
        return total_chars // 4
    
    def _categorize_tokens(self, token_counts: List[int]) -> Dict[str, int]:
        """토큰 수를 범주별로 분류합니다."""
        distribution = {category: 0 for category in self.token_ranges.keys()}
        
        for count in token_counts:
            for category, (min_tokens, max_tokens) in self.token_ranges.items():
                if min_tokens <= count < max_tokens:
                    distribution[category] += 1
                    break
        
        return distribution
    
    def _analyze_fields(self, data: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        """필드별 분석을 수행합니다."""
        field_stats = {}
        
        # ShareGPT 포맷
        if data and "conversations" in data[0]:
            field_stats["conversations"] = self._analyze_conversation_fields(data)
        
        # Alpaca 포맷
        elif data and ("instruction" in data[0] or "output" in data[0]):
            field_stats["instruction"] = self._analyze_text_field(data, "instruction")
            field_stats["output"] = self._analyze_text_field(data, "output")
            if "input" in data[0]:
                field_stats["input"] = self._analyze_text_field(data, "input")
        
        # OpenAI 포맷
        elif data and "messages" in data[0]:
            field_stats["messages"] = self._analyze_message_fields(data)
        
        return field_stats
    
    def _analyze_conversation_fields(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """대화 필드 분석"""
        stats = {
            "total_conversations": 0,
            "average_turns": 0,
            "role_distribution": defaultdict(int),
            "length_distribution": defaultdict(int)
        }
        
        total_turns = 0
        all_lengths = []
        
        for item in data:
            conversations = item.get("conversations", [])
            stats["total_conversations"] += len(conversations)
            total_turns += len(conversations)
            
            for conv in conversations:
                role = conv.get("from", "unknown")
                stats["role_distribution"][role] += 1
                
                length = len(conv.get("value", ""))
                all_lengths.append(length)
                
                # 길이 분류
                if length < 50:
                    stats["length_distribution"]["very_short"] += 1
                elif length < 200:
                    stats["length_distribution"]["short"] += 1
                elif length < 500:
                    stats["length_distribution"]["medium"] += 1
                else:
                    stats["length_distribution"]["long"] += 1
        
        stats["average_turns"] = total_turns / len(data) if data else 0
        stats["average_length"] = statistics.mean(all_lengths) if all_lengths else 0
        stats["max_length"] = max(all_lengths) if all_lengths else 0
        stats["min_length"] = min(all_lengths) if all_lengths else 0
        
        return dict(stats)
    
    def _analyze_text_field(self, data: List[Dict[str, Any]], field_name: str) -> Dict[str, Any]:
        """텍스트 필드 분석"""
        values = [item.get(field_name, "") for item in data]
        lengths = [len(value) for value in values]
        
        return {
            "total_values": len(values),
            "non_empty_values": sum(1 for value in values if value.strip()),
            "average_length": statistics.mean(lengths) if lengths else 0,
            "max_length": max(lengths) if lengths else 0,
            "min_length": min(lengths) if lengths else 0,
            "empty_count": sum(1 for value in values if not value.strip())
        }
    
    def _analyze_message_fields(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """메시지 필드 분석"""
        stats = {
            "total_messages": 0,
            "average_messages_per_item": 0,
            "role_distribution": defaultdict(int),
            "message_type_distribution": defaultdict(int)
        }
        
        total_messages = 0
        
        for item in data:
            messages = item.get("messages", [])
            stats["total_messages"] += len(messages)
            total_messages += len(messages)
            
            for msg in messages:
                role = msg.get("role", "unknown")
                stats["role_distribution"][role] += 1
                
                # 메시지 타입 분류
                content = msg.get("content", "")
                if len(content) < 50:
                    stats["message_type_distribution"]["short"] += 1
                elif len(content) < 200:
                    stats["message_type_distribution"]["medium"] += 1
                else:
                    stats["message_type_distribution"]["long"] += 1
        
        stats["average_messages_per_item"] = total_messages / len(data) if data else 0
        
        return dict(stats)
    
    def _calculate_format_quality(self, data: List[Dict[str, Any]]) -> float:
        """포맷별 품질 점수를 계산합니다."""
        if not data:
            return 0.0
        
        quality_scores = []
        
        for item in data:
            score = 1.0  # 기본 점수
            
            # 필드 완성도
            if "conversations" in item:
                conversations = item.get("conversations", [])
                if len(conversations) >= 2:  # 최소 2턴
                    score += 0.2
                else:
                    score -= 0.3
                
                # 시스템 메시지 유무
                has_system = any(conv.get("from") == "system" for conv in conversations)
                if has_system:
                    score += 0.1
            
            elif "instruction" in item and "output" in item:
                instruction = item.get("instruction", "").strip()
                output = item.get("output", "").strip()
                
                if instruction and output:
                    score += 0.3
                else:
                    score -= 0.5
                
                # 지시문 길이 검증
                if len(instruction) >= 20:
                    score += 0.1
                
                # 응답 길이 검증
                if len(output) >= 20:
                    score += 0.1
            
            elif "messages" in item:
                messages = item.get("messages", [])
                if len(messages) >= 2:  # 최소 2 메시지
                    score += 0.2
                
                # 역할 다양성
                roles = set(msg.get("role") for msg in messages)
                if len(roles) >= 2:
                    score += 0.1
            
            # 품질 점수 범위 제한
            score = max(0.0, min(1.0, score))
            quality_scores.append(score)
        
        return statistics.mean(quality_scores) if quality_scores else 0.0
    
    def _calculate_completeness(self, data: List[Dict[str, Any]]) -> float:
        """데이터셋 완성도를 계산합니다."""
        if not data:
            return 0.0
        
        completeness_scores = []
        
        for item in data:
            score = 1.0
            
            # 필드 존재 여부 확인
            if "conversations" in item:
                conversations = item.get("conversations", [])
                for conv in conversations:
                    if "from" not in conv or "value" not in conv:
                        score -= 0.25
            
            elif "instruction" in item and "output" in item:
                if "instruction" not in item or not item["instruction"].strip():
                    score -= 0.5
                if "output" not in item or not item["output"].strip():
                    score -= 0.5
            
            elif "messages" in item:
                for msg in item.get("messages", []):
                    if "role" not in msg or "content" not in msg:
                        score -= 0.25
            
            completeness_scores.append(max(0.0, score))
        
        return statistics.mean(completeness_scores) if completeness_scores else 0.0
    
    def _calculate_quality_metrics(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, float]:
        """전체 품질 지표를 계산합니다."""
        metrics = {
            "overall_quality": 0.0,
            "format_quality": {},
            "completeness": 0.0,
            "consistency": 0.0
        }
        
        if not datasets:
            return metrics
        
        # 포맷별 품질 점수
        format_qualities = []
        for format_type, data in datasets.items():
            quality_score = self._calculate_format_quality(data)
            metrics["format_quality"][format_type] = quality_score
            format_qualities.append(quality_score)
        
        # 전체 품질 점수
        metrics["overall_quality"] = statistics.mean(format_qualities) if format_qualities else 0.0
        
        # 전체 완성도
        completeness_scores = []
        for data in datasets.values():
            completeness = self._calculate_completeness(data)
            completeness_scores.append(completeness)
        
        metrics["completeness"] = statistics.mean(completeness_scores) if completeness_scores else 0.0
        
        # 일관성 (포맷 간 품질 변이도)
        if len(format_qualities) > 1:
            stdev = statistics.stdev(format_qualities)
            metrics["consistency"] = 1.0 - (stdev / 1.0)  # 변이도가 낮을수록 일관성 높음
        else:
            metrics["consistency"] = 1.0
        
        return metrics
    
    def _calculate_diversity_metrics(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, float]:
        """다양성 지표를 계산합니다."""
        metrics = {
            "topic_diversity": 0.0,
            "length_diversity": 0.0,
            "format_diversity": len(datasets),
            "source_diversity": 0.0
        }
        
        # 주제 다양성 (간단한 키워드 기반 분석)
        all_topics = []
        for data in datasets.values():
            for item in data:
                # 키워드 추출 (간단한 방식)
                text_parts = []
                if "conversations" in item:
                    for conv in item.get("conversations", []):
                        text_parts.append(conv.get("value", ""))
                elif "instruction" in item:
                    text_parts.append(item.get("instruction", ""))
                elif "messages" in item:
                    for msg in item.get("messages", []):
                        text_parts.append(msg.get("content", ""))
                
                # 키워드 추출
                for text in text_parts:
                    words = re.findall(r'\b\w+\b', text.lower())
                    all_topics.extend(words[:5])  # 각 텍스트당 최대 5개 키워드
        
        if all_topics:
            unique_topics = len(set(all_topics))
            total_topics = len(all_topics)
            metrics["topic_diversity"] = unique_topics / total_topics if total_topics > 0 else 0.0
        
        # 길이 다양성
        all_lengths = []
        for data in datasets.values():
            for item in data:
                token_count = self._calculate_token_count(item)
                all_lengths.append(token_count)
        
        if all_lengths and len(set(all_lengths)) > 1:
            # 길이 분포의 엔트로피 기반 다양성
            length_ranges = defaultdict(int)
            for length in all_lengths:
                if length < 100:
                    length_ranges["short"] += 1
                elif length < 500:
                    length_ranges["medium"] += 1
                else:
                    length_ranges["long"] += 1
            
            # 엔트로피 계산
            total = sum(length_ranges.values())
            entropy = 0.0
            for count in length_ranges.values():
                if count > 0:
                    p = count / total
                    entropy -= p * (p ** 0.5)  # 제곱근을 사용한 가중치
            
            metrics["length_diversity"] = min(1.0, entropy / 3.0)  # 정규화
        
        # 소스 다양성
        all_sources = []
        for data in datasets.values():
            for item in data:
                source = item.get("source", "unknown")
                all_sources.append(source)
        
        if all_sources:
            unique_sources = len(set(all_sources))
            metrics["source_diversity"] = unique_sources / len(all_sources) if all_sources else 0.0
        
        return metrics
    
    def _analyze_token_distribution(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """토큰 분포를 분석합니다."""
        analysis = {
            "overall_token_stats": {},
            "format_token_stats": {},
            "token_range_distribution": defaultdict(int)
        }
        
        all_token_counts = []
        
        for format_type, data in datasets.items():
            format_tokens = [self._calculate_token_count(item) for item in data]
            all_token_counts.extend(format_tokens)
            
            # 포맷별 토큰 통계
            if format_tokens:
                analysis["format_token_stats"][format_type] = {
                    "count": len(format_tokens),
                    "mean": statistics.mean(format_tokens),
                    "median": statistics.median(format_tokens),
                    "min": min(format_tokens),
                    "max": max(format_tokens),
                    "std_dev": statistics.stdev(format_tokens) if len(format_tokens) > 1 else 0
                }
        
        # 전체 토큰 통계
        if all_token_counts:
            analysis["overall_token_stats"] = {
                "total_samples": len(all_token_counts),
                "mean": statistics.mean(all_token_counts),
                "median": statistics.median(all_token_counts),
                "min": min(all_token_counts),
                "max": max(all_token_counts),
                "std_dev": statistics.stdev(all_token_counts) if len(all_token_counts) > 1 else 0
            }
            
            # 토큰 범위 분포
            for count in all_token_counts:
                for category, (min_tokens, max_tokens) in self.token_ranges.items():
                    if min_tokens <= count < max_tokens:
                        analysis["token_range_distribution"][category] += 1
                        break
        
        return dict(analysis)
    
    def export_statistics(self, statistics: DatasetStatistics, output_path: str):
        """통계 정보를 파일로 내보냅니다."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(statistics.to_dict(), f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"Statistics exported to: {output_path}")


if __name__ == "__main__":
    # 테스트 데이터
    test_datasets = {
        "sharegpt": [
            {
                "conversations": [
                    {"from": "system", "value": "시스템 프롬프트"},
                    {"from": "human", "value": "사용자 질문입니다."},
                    {"from": "gpt", "value": "AI 응답 내용입니다."}
                ]
            }
        ],
        "alpaca": [
            {
                "instruction": "지시문 내용",
                "output": "응답 내용",
                "input": "입력 내용"
            }
        ],
        "openai": [
            {
                "messages": [
                    {"role": "system", "content": "시스템 메시지"},
                    {"role": "user", "content": "사용자 메시지"},
                    {"role": "assistant", "content": "어시스턴트 메시지"}
                ]
            }
        ]
    }
    
    # 통계 생성기 생성
    stats_generator = StatisticsGenerator()
    
    print("=== Statistics Generator Test ===")
    
    # 데이터셋 통계 생성
    dataset_stats = stats_generator.generate_dataset_statistics(test_datasets)
    
    print(f"\nDataset Statistics:")
    print(f"Total samples: {dataset_stats.total_samples}")
    print(f"Quality metrics: {dataset_stats.quality_metrics}")
    print(f"Diversity metrics: {dataset_stats.diversity_metrics}")
    
    # 포맷별 통계
    for format_type, format_stats in dataset_stats.format_statistics.items():
        print(f"\n{format_type.upper()} Format Statistics:")
        print(f"  Sample count: {format_stats.sample_count}")
        print(f"  Average tokens: {format_stats.average_tokens:.2f}")
        print(f"  Token range: {format_stats.min_tokens} - {format_stats.max_tokens}")
        print(f"  Quality score: {format_stats.quality_score:.2f}")
        print(f"  Completeness score: {format_stats.completeness_score:.2f}")
        
        if format_stats.token_distribution:
            print(f"  Token distribution: {format_stats.token_distribution}")
    
    # 토큰 분석
    print(f"\nToken Analysis:")
    token_analysis = dataset_stats.token_analysis
    if "overall_token_stats" in token_analysis:
        overall = token_analysis["overall_token_stats"]
        print(f"  Overall: {overall}")
    
    if "token_range_distribution" in token_analysis:
        distribution = token_analysis["token_range_distribution"]
        print(f"  Range distribution: {dict(distribution)}")
    
    # 파일로 내보내기
    stats_generator.export_statistics(dataset_stats, "test_statistics.json")
    print(f"\nStatistics exported to test_statistics.json")