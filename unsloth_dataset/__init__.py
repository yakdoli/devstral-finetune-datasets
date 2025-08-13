#!/usr/bin/env python3
"""
Unsloth 호환 데이터셋 포맷 생성기 모듈
Unsloth 프레임워크에 최적화된 다양한 데이터셋 포맷을 생성하는 모듈을 제공합니다.
"""

from .generator import (
    UnslothDatasetGenerator,
    DatasetConfig,
    DatasetGenerationResult
)
from .formatters.sharegpt_formatter import ShareGPTFormatter
from .formatters.alpaca_formatter import AlpacaFormatter
from .formatters.openai_formatter import OpenAIFormatter
from .validator import UnslothValidator, ValidationResult
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

__version__ = "1.0.0"
__author__ = "Unsloth Dataset Generator Team"
__email__ = "support@example.com"
__description__ = "Unsloth-Compatible Dataset Format Generator for Fine-tuning"

__all__ = [
    # Main Generator
    'UnslothDatasetGenerator',
    'DatasetConfig',
    'DatasetGenerationResult',
    'create_dataset_generator',
    
    # Formatters
    'ShareGPTFormatter',
    'AlpacaFormatter', 
    'OpenAIFormatter',
    
    # Validator
    'UnslothValidator',
    'ValidationResult',
    
    # Statistics
    'DatasetStatistics',
    'StatisticsGenerator',
    
    # Utils
    'setup_logging',
    'normalize_text',
    'calculate_tokens',
    'add_eos_token',
    'remove_duplicates',
    'split_train_test',
    'save_jsonl',
    'load_jsonl',
    'calculate_diversity_score',
    'validate_token_range',
    
    # Version info
    '__version__',
    '__author__',
    '__email__',
    '__description__'
]


def create_default_generator() -> UnslothDatasetGenerator:
    """
    기본 설정으로 데이터셋 생성기를 생성합니다.
    
    Returns:
        기본 설정으로 생성된 UnslothDatasetGenerator 인스턴스
    """
    config = DatasetConfig(
        target_count=1000,
        max_seq_length=8192,
        train_test_split=0.9,
        formats=["sharegpt", "alpaca", "openai"],
        min_tokens=50,
        max_tokens=8192,
        eos_token="</s>",
        remove_duplicates=True,
        quality_threshold=0.7
    )
    return create_dataset_generator(config)


def create_dataset_generator(config: DatasetConfig) -> UnslothDatasetGenerator:
    """
    데이터셋 생성기를 생성합니다.
    
    Args:
        config: 데이터셋 생성 설정
        
    Returns:
        생성된 UnslothDatasetGenerator 인스턴스
    """
    return UnslothDatasetGenerator(config)


def generate_sample_dataset(
    output_path: str = "sample_unsloth_dataset",
    target_count: int = 100,
    formats: list = None
) -> dict:
    """
    샘플 데이터셋을 생성합니다.
    
    Args:
        output_path: 출력 경로
        target_count: 목표 샘플 수
        formats: 생성할 포맷 목록
        
    Returns:
        생성 결과 통계
    """
    if formats is None:
        formats = ["sharegpt", "alpaca", "openai"]
    
    config = DatasetConfig(
        target_count=target_count,
        max_seq_length=8192,
        train_test_split=0.9,
        formats=formats,
        min_tokens=50,
        max_tokens=8192,
        eos_token="</s>",
        remove_duplicates=True,
        quality_threshold=0.7
    )
    
    generator = create_dataset_generator(config)
    
    # 샘플 데이터 생성 (실제 구현에서는 외부 데이터 소스와 통합)
    sample_data = [
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
            "input": "초보자도 이해할 수 있도록 단계별로 설명해주세요.",
            "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용"
        },
        {
            "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
            "input": "데이터 바인딩 포함해서 설명해주세요.",
            "output": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가"
        }
    ]
    
    result = generator.generate_from_samples(sample_data, output_path)
    return result.get_statistics()


# 모듈 로드 시 기본 로깅 설정
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


# 모듈 정보 출력
def print_module_info():
    """모듈 정보를 출력합니다."""
    print(f"Unsloth Dataset Generator Module v{__version__}")
    print(f"Author: {__author__}")
    print(f"Description: {__description__}")
    print(f"Available components:")
    print(f"  - Generator: Main dataset generation pipeline")
    print(f"  - Formatters: ShareGPT, Alpaca, OpenAI format support")
    print(f"  - Validator: Unsloth compatibility validation")
    print(f"  - Statistics: Dataset quality metrics")
    print(f"  - Utils: Common utility functions")


if __name__ == "__main__":
    # 모듈 정보 출력
    print_module_info()
    
    # 샘플 생성 테스트
    print("\n=== Sample Generation Test ===")
    try:
        stats = generate_sample_dataset("test_sample", 10)
        print(f"Sample dataset generated successfully")
        print(f"Total samples: {stats.get('total_samples', 0)}")
        print(f"Formats created: {list(stats.get('formats_by_type', {}).keys())}")
    except Exception as e:
        print(f"Sample generation failed: {e}")
    
    print("\n=== Module Ready ===")
    print("Use create_default_generator() to start generating datasets.")