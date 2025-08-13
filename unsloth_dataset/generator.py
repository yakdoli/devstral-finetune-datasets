#!/usr/bin/env python3
"""
Unsloth 데이터셋 생성기 모듈
Unsloth 프레임워크에 최적화된 다양한 데이터셋 포맷을 생성하는 메인 생성기입니다.
"""

import json
import logging
import asyncio
from typing import List, Dict, Any, Optional, Union, Tuple
from dataclasses import dataclass, asdict, field
from pathlib import Path
from datetime import datetime
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

from .formatters import (
    ShareGPTFormatter, ShareGPTConfig,
    AlpacaFormatter, AlpacaConfig, 
    OpenAIFormatter, OpenAIConfig,
    create_formatter
)
from .validator import UnslothValidator
from .statistics import DatasetStatistics, StatisticsGenerator
from .utils import (
    setup_logging,
    normalize_text,
    calculate_tokens,
    add_eos_token,
    remove_duplicates,
    split_train_test,
    save_jsonl,
    load_jsonl,
    calculate_diversity_score,
    validate_token_range
)

logger = logging.getLogger(__name__)


@dataclass
class DatasetConfig:
    """데이터셋 생성 설정"""
    target_count: int = 1000
    max_seq_length: int = 8192
    train_test_split: float = 0.9
    formats: List[str] = field(default_factory=lambda: ["sharegpt", "alpaca", "openai"])
    min_tokens: int = 50
    max_tokens: int = 8192
    eos_token: str = "</s>"
    remove_duplicates: bool = True
    quality_threshold: float = 0.7
    batch_size: int = 100
    max_workers: int = 4
    seed: Optional[int] = 42
    output_dir: str = "output"
    include_metadata: bool = True
    shuffle_data: bool = True
    progress_interval: int = 100
    test_mode: bool = False


@dataclass
class DatasetGenerationResult:
    """데이터셋 생성 결과"""
    train_data: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    validation_data: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    statistics: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    validation_results: Dict[str, Any] = field(default_factory=dict)
    output_paths: Dict[str, str] = field(default_factory=dict)


class UnslothDatasetGenerator:
    """Unsloth 데이터셋 생성기 클래스"""
    
    def __init__(self, config: DatasetConfig):
        """
        Unsloth 데이터셋 생성기를 초기화합니다.
        
        Args:
            config: 데이터셋 생성 설정
        """
        self.config = config
        self.output_dir = Path(config.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 난수 시드 설정
        if config.seed is not None:
            random.seed(config.seed)
        
        # 포맷터 생성
        self.formatters = {}
        for format_type in config.formats:
            self.formatters[format_type] = create_formatter(format_type)
        
        # 검증기 생성
        self.validator = UnslothValidator()
        
        # 통계 생성기 생성
        self.stats_generator = StatisticsGenerator()
        
        # 로깅 설정
        self.logger = setup_logging("INFO")
        self.logger.info(f"UnslothDatasetGenerator initialized with config: {asdict(config)}")
    
    def generate_from_samples(
        self, 
        samples: List[Dict[str, Any]], 
        dataset_name: str = "dataset"
    ) -> DatasetGenerationResult:
        """
        샘플 데이터로부터 데이터셋을 생성합니다.
        
        Args:
            samples: 샘플 데이터 목록
            dataset_name: 데이터셋 이름
            
        Returns:
            생성된 데이터셋 결과
        """
        self.logger.info(f"Generating dataset from {len(samples)} samples")
        
        # 결과 객체 생성
        result = DatasetGenerationResult()
        result.metadata = {
            "dataset_name": dataset_name,
            "created_at": datetime.now().isoformat(),
            "config": asdict(self.config),
            "total_samples": len(samples)
        }
        
        # 중복 제거 (테스트 모드에서는 완전히 비활성화)
        if self.config.test_mode:
            self.logger.info("Test mode: deduplication disabled to preserve samples")
        elif self.config.remove_duplicates:
            samples = remove_duplicates(samples)
            self.logger.info(f"After deduplication: {len(samples)} samples")
        
        # 품질 필터링 (테스트 모드에서는 완화)
        if self.config.test_mode:
            quality_threshold = 0.0  # 테스트 모드에서는 품질 필터링 완전 비활성화
        else:
            quality_threshold = 0.1 if self.config.quality_threshold > 0.5 else self.config.quality_threshold
        
        samples = [s for s in samples if s.get("quality_score", 0) >= quality_threshold]
        self.logger.info(f"After quality filtering (threshold {quality_threshold}): {len(samples)} samples")
        
        # 데이터 셔플
        if self.config.shuffle_data:
            random.shuffle(samples)
        
        # 각 포맷별로 데이터셋 생성
        for format_type in self.config.formats:
            self.logger.info(f"Processing {format_type} format...")
            
            formatter = self.formatters[format_type]
            format_samples = []
            
            # 샘플별로 포맷 변환
            for i, sample in enumerate(samples):
                try:
                    if format_type == "sharegpt":
                        # ShareGPT 포맷으로 변환
                        formatted = formatter.format_batch([{
                            "instruction": sample["instruction"],
                            "response": sample["response"],
                            "context": sample.get("context", ""),
                            "source": sample.get("source", "unknown"),
                            "quality_score": sample.get("quality_score", 0.8)
                        }])[0]
                        
                    elif format_type == "alpaca":
                        # Alpaca 포맷으로 변환
                        formatted = formatter.format_batch([{
                            "instruction": sample["instruction"],
                            "output": sample["response"],
                            "input": sample.get("context", ""),
                            "source": sample.get("source", "unknown"),
                            "quality_score": sample.get("quality_score", 0.8)
                        }])[0]
                        
                    elif format_type == "openai":
                        # OpenAI 포맷으로 변환
                        formatted = formatter.format_messages(
                            user_message=sample["instruction"],
                            assistant_message=sample["response"],
                            system_prompt=sample.get("system_prompt", "Syncfusion WinForms 전문가")
                        )
                    
                    # 토큰 수 계산 및 검증
                    text_content = self._extract_text_for_token_count(formatted)
                    token_count = calculate_tokens(text_content)
                    
                    if self.config.min_tokens <= token_count <= self.config.max_tokens:
                        formatted["metadata"] = {
                            "original_index": i,
                            "token_count": token_count,
                            "quality_score": sample.get("quality_score", 0),
                            "source": sample.get("source", "unknown")
                        }
                        format_samples.append(formatted)
                    else:
                        self.logger.debug(f"Sample {i} token count {token_count} out of range")
                        
                except Exception as e:
                    self.logger.warning(f"Failed to format sample {i} for {format_type}: {e}")
                    continue
            
            # 훈련/검증 데이터 분할
            train_data, val_data = split_train_test(
                format_samples, 
                self.config.train_test_split,
                self.config.seed
            )
            
            result.train_data[format_type] = train_data
            result.validation_data[format_type] = val_data
            
            self.logger.info(f"{format_type}: {len(train_data)} train, {len(val_data)} validation")
        
        # 통계 생성
        datasets = {}
        for format_type in self.config.formats:
            datasets[format_type] = result.train_data.get(format_type, []) + result.validation_data.get(format_type, [])
        
        result.statistics = self.stats_generator.generate_dataset_statistics(datasets)
        
        # 검증 수행
        result.validation_results = self._validate_datasets(result)
        
        self.logger.info("Dataset generation completed successfully")
        return result
    
    def _extract_text_for_token_count(self, formatted_data: Dict[str, Any]) -> str:
        """토큰 수 계산을 위한 텍스트를 추출합니다."""
        text_parts = []
        
        if "conversations" in formatted_data:
            # ShareGPT 형식
            for conv in formatted_data["conversations"]:
                text_parts.append(conv["value"])
        elif "messages" in formatted_data:
            # OpenAI 형식
            for msg in formatted_data["messages"]:
                text_parts.append(msg["content"])
        elif "instruction" in formatted_data and "output" in formatted_data:
            # Alpaca 형식
            text_parts.append(formatted_data["instruction"])
            text_parts.append(formatted_data["output"])
        
        return " ".join(text_parts)
    
    def _validate_datasets(self, result: DatasetGenerationResult) -> Dict[str, Dict[str, Any]]:
        """데이터셋을 검증합니다."""
        validation_results = {}
        
        for format_type in self.config.formats:
            train_data = result.train_data.get(format_type, [])
            val_data = result.validation_data.get(format_type, [])
            
            # 포맷별 검증
            format_validation = self.validator.validate_dataset_format(
                format_type, train_data + val_data
            )
            
            # 토큰 범위 검증
            token_validation = self.validator.validate_token_ranges(
                train_data + val_data, 
                self.config.min_tokens, 
                self.config.max_tokens
            )
            
            validation_results[format_type] = {
                "format_validation": format_validation,
                "token_validation": token_validation,
                "is_valid": format_validation.is_valid and token_validation.is_valid,
                "issues": format_validation.issues + token_validation.issues
            }
        
        return validation_results
    
    def _serialize_statistics(self, statistics: Any) -> Dict[str, Any]:
        """통계 객체를 직렬화 가능한 형태로 변환합니다."""
        import json
        from collections import defaultdict
        
        def convert_defaultdict(obj):
            """defaultdict를 일반 dict로 변환합니다."""
            if isinstance(obj, defaultdict):
                return dict(obj)
            elif isinstance(obj, dict):
                return {k: convert_defaultdict(v) for k, v in obj.items()}
            elif isinstance(obj, (list, tuple)):
                return [convert_defaultdict(item) for item in obj]
            else:
                return obj
        
        try:
            if hasattr(statistics, 'asdict'):
                # dataclass 객체인 경우
                result = statistics.asdict()
            elif hasattr(statistics, '__dict__'):
                # 일반 객체인 경우
                result = statistics.__dict__.copy()
            elif isinstance(statistics, dict):
                result = statistics.copy()
            else:
                # 기본 타입인 경우 그대로 사용
                return statistics
            
            # defaultdict를 일반 dict로 변환
            result = convert_defaultdict(result)
            
            # JSON 직렬화 가능한지 테스트
            json.dumps(result)
            return result
            
        except Exception as e:
            self.logger.warning(f"Failed to serialize statistics: {e}")
            # 실패한 경우 기본 정보만 반환
            return {
                "serialization_error": str(e),
                "type": str(type(statistics)),
                "timestamp": datetime.now().isoformat()
            }
    
    def save_datasets(self, result: DatasetGenerationResult, base_name: str = "dataset") -> Dict[str, str]:
        """
        데이터셋을 파일로 저장합니다.
        
        Args:
            result: 데이터셋 생성 결과
            base_name: 기본 파일 이름
            
        Returns:
            저장된 파일 경로 목록
        """
        saved_paths = {}
        
        # 각 포맷별로 파일 저장
        for format_type in self.config.formats:
            # 훈련 데이터 저장
            train_dir = self.output_dir / f"{base_name}_{format_type}_train"
            train_dir.mkdir(parents=True, exist_ok=True)
            train_file = train_dir / "train.jsonl"
            
            train_data = result.train_data.get(format_type, [])
            if train_data:
                save_jsonl(train_data, train_file)
                saved_paths[f"{format_type}_train"] = str(train_file)
            
            # 검증 데이터 저장
            val_dir = self.output_dir / f"{base_name}_{format_type}_validation"
            val_dir.mkdir(parents=True, exist_ok=True)
            val_file = val_dir / "validation.jsonl"
            
            val_data = result.validation_data.get(format_type, [])
            if val_data:
                save_jsonl(val_data, val_file)
                saved_paths[f"{format_type}_validation"] = str(val_file)
        
        # 메타데이터 파일 저장
        if self.config.include_metadata:
            metadata_path = self.output_dir / f"{base_name}_metadata.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(result.metadata, f, indent=2, ensure_ascii=False)
            saved_paths["metadata"] = str(metadata_path)
        
        # 통계 파일 저장
        if self.config.include_metadata:
            stats_path = self.output_dir / f"{base_name}_statistics.json"
            # 통계 객체를 직렬화 가능한 딕셔너리로 변환
            serializable_stats = self._serialize_statistics(result.statistics)
            with open(stats_path, 'w', encoding='utf-8') as f:
                json.dump(serializable_stats, f, indent=2, ensure_ascii=False)
            saved_paths["statistics"] = str(stats_path)
        
        # 검증 결과 파일 저장 (간단한 버전)
        validation_path = self.output_dir / f"{base_name}_validation.json"
        simple_validation = {}
        for format_type, validation_result in result.validation_results.items():
            if isinstance(validation_result, dict):
                simple_validation[format_type] = validation_result
            else:
                simple_validation[format_type] = {
                    "is_valid": validation_result.is_valid,
                    "issues_count": len(validation_result.issues),
                    "warnings_count": len(validation_result.warnings),
                    "recommendations_count": len(validation_result.recommendations)
                }
        
        try:
            with open(validation_path, 'w', encoding='utf-8') as f:
                json.dump(simple_validation, f, indent=2, ensure_ascii=False)
            saved_paths["validation"] = str(validation_path)
        except Exception as e:
            self.logger.warning(f"Failed to save validation results: {e}")
        
        return saved_paths
    
    def get_train_count(self, format_type: str) -> int:
        """훈련 데이터 샘플 수를 반환합니다."""
        return len(self.train_data.get(format_type, []))
    
    def get_validation_count(self, format_type: str) -> int:
        """검증 데이터 샘플 수를 반환합니다."""
        return len(self.validation_data.get(format_type, []))
    
    def generate_datasets(
        self,
        md_documents: Optional[List[Dict[str, Any]]] = None,
        qdrant_documents: Optional[List[Dict[str, Any]]] = None,
        conversations: Optional[List[Dict[str, Any]]] = None
    ) -> DatasetGenerationResult:
        """
        다양한 데이터 소스로부터 통합 데이터셋을 생성합니다.
        
        Args:
            md_documents: MD 문서 데이터
            qdrant_documents: Qdrant 문서 데이터
            conversations: 대화 데이터
            
        Returns:
            생성된 데이터셋 결과
        """
        all_samples = []
        
        # MD 문서 처리
        if md_documents:
            for doc in md_documents:
                sample = {
                    "instruction": f"다음 내용에 대해 설명해주세요: {doc.get('title', '문서')}",
                    "response": doc.get("content", ""),
                    "source": "md_document",
                    "quality_score": doc.get("quality_score", 0.8)
                }
                all_samples.append(sample)
        
        # Qdrant 문서 처리
        if qdrant_documents:
            for doc in qdrant_documents:
                sample = {
                    "instruction": f"다음 내용에 대해 설명해주세요: {doc.get('title', '문서')}",
                    "response": doc.get("content", ""),
                    "source": "qdrant_document",
                    "quality_score": doc.get("quality_score", 0.8)
                }
                all_samples.append(sample)
        
        # 대화 데이터 처리
        if conversations:
            for conv in conversations:
                sample = {
                    "instruction": conv.get("user_message", ""),
                    "response": conv.get("assistant_message", ""),
                    "source": "conversation",
                    "quality_score": conv.get("quality_score", 0.8)
                }
                all_samples.append(sample)
        
        # 샘플 수 조정
        if len(all_samples) > self.config.target_count:
            all_samples = random.sample(all_samples, self.config.target_count)
        
        return self.generate_from_samples(all_samples, "integrated_dataset")