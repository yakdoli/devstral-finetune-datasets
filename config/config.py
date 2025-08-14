"""
설정 관리 핵심 모듈 - 데이터클래스 기반 설정 관리
"""

import os
import yaml
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from enum import Enum


class LogLevel(str, Enum):
    """로그 레벨 열거형"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class OutputFormat(str, Enum):
    """출력 포맷 열거형"""
    SHAREGPT = "sharegpt"
    ALPACA = "alpaca"
    OPENAI = "openai"


@dataclass
class MDProcessorConfig:
    """MD 파일 처리 설정"""
    input_directory: str = "md_staging"
    file_extensions: List[str] = field(default_factory=lambda: [".md", ".markdown"])
    max_file_size_mb: int = 10
    encoding: str = "utf-8"
    skip_empty_files: bool = True
    preserve_code_blocks: bool = True
    extract_api_signatures: bool = True
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_file_size_mb <= 0:
            raise ValueError("max_file_size_mb는 양의 정수여야 합니다")
        if not self.file_extensions:
            raise ValueError("file_extensions는 비어있을 수 없습니다")


@dataclass
class OpenAIConnectorConfig:
    """OpenAI API 연동 설정"""
    api_base_url: str = "http://123.37.28.120:9997/v1"
    model_name: str = "qwen2.5-vl-instruct"
    api_key: Optional[str] = None
    max_tokens: int = 8192
    temperature: float = 0.7
    top_p: float = 0.9
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    batch_size: int = 16
    max_concurrent_requests: int = 8
    request_timeout: int = 60
    retry_attempts: int = 3
    retry_delay: float = 1.0
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_tokens <= 0:
            raise ValueError("max_tokens는 양의 정수여야 합니다")
        if not (0.0 <= self.temperature <= 2.0):
            raise ValueError("temperature는 0.0과 2.0 사이여야 합니다")
        if not (0.0 <= self.top_p <= 1.0):
            raise ValueError("top_p는 0.0과 1.0 사이여야 합니다")
        if self.batch_size <= 0:
            raise ValueError("batch_size는 양의 정수여야 합니다")
        if self.max_concurrent_requests <= 0:
            raise ValueError("max_concurrent_requests는 양의 정수여야 합니다")


@dataclass
class QdrantConnectorConfig:
    """Qdrant 벡터 DB 연동 설정"""
    host: str = "localhost"
    port: int = 6333
    collection_name: str = "ws-7491d651ae044c78"
    api_key: Optional[str] = None
    timeout: int = 30
    retry_attempts: int = 3
    retry_delay: float = 1.0
    similarity_threshold: float = 0.7
    max_results: int = 10
    batch_size: int = 100
    
    def __post_init__(self):
        """초기화 후 검증"""
        if not (1 <= self.port <= 65535):
            raise ValueError("port는 1과 65535 사이여야 합니다")
        if not (0.0 <= self.similarity_threshold <= 1.0):
            raise ValueError("similarity_threshold는 0.0과 1.0 사이여야 합니다")
        if self.max_results <= 0:
            raise ValueError("max_results는 양의 정수여야 합니다")
        if self.batch_size <= 0:
            raise ValueError("batch_size는 양의 정수여야 합니다")


@dataclass
class UnslothDatasetConfig:
    """Unsloth 데이터셋 생성 설정"""
    target_conversation_count: int = 1000
    output_formats: List[OutputFormat] = field(default_factory=lambda: [
        OutputFormat.SHAREGPT, OutputFormat.ALPACA, OutputFormat.OPENAI
    ])
    train_test_split: float = 0.8
    max_conversation_length: int = 8192
    min_conversation_length: int = 50
    include_system_messages: bool = True
    conversation_templates: Dict[str, str] = field(default_factory=lambda: {
        "question_answer": "사용자가 {topic}에 대해 질문하고 전문가가 답변하는 대화",
        "tutorial": "{topic}에 대한 단계별 튜토리얼 대화",
        "troubleshooting": "{topic} 관련 문제 해결 대화"
    })
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.target_conversation_count <= 0:
            raise ValueError("target_conversation_count는 양의 정수여야 합니다")
        if not (0.0 < self.train_test_split < 1.0):
            raise ValueError("train_test_split는 0.0과 1.0 사이여야 합니다")
        if self.max_conversation_length <= self.min_conversation_length:
            raise ValueError("max_conversation_length는 min_conversation_length보다 커야 합니다")
        if not self.output_formats:
            raise ValueError("output_formats는 비어있을 수 없습니다")


@dataclass
class QualityValidatorConfig:
    """품질 검증 설정"""
    min_quality_score: float = 0.7
    enable_safety_filter: bool = True
    enable_duplicate_removal: bool = True
    enable_auto_correction: bool = True
    similarity_threshold_for_duplicates: float = 0.9
    max_correction_attempts: int = 3
    quality_metrics: List[str] = field(default_factory=lambda: [
        "coherence", "relevance", "completeness", "accuracy"
    ])
    safety_categories: List[str] = field(default_factory=lambda: [
        "hate", "harassment", "violence", "self-harm", "sexual", "dangerous"
    ])
    
    def __post_init__(self):
        """초기화 후 검증"""
        if not (0.0 <= self.min_quality_score <= 1.0):
            raise ValueError("min_quality_score는 0.0과 1.0 사이여야 합니다")
        if not (0.0 <= self.similarity_threshold_for_duplicates <= 1.0):
            raise ValueError("similarity_threshold_for_duplicates는 0.0과 1.0 사이여야 합니다")
        if self.max_correction_attempts <= 0:
            raise ValueError("max_correction_attempts는 양의 정수여야 합니다")


@dataclass
class LoggingConfig:
    """로깅 설정"""
    level: LogLevel = LogLevel.INFO
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: Optional[str] = "output/logs/pipeline.log"
    max_file_size_mb: int = 100
    backup_count: int = 5
    enable_console_output: bool = True
    enable_file_output: bool = True
    enable_structured_logging: bool = True
    log_performance_metrics: bool = True
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_file_size_mb <= 0:
            raise ValueError("max_file_size_mb는 양의 정수여야 합니다")
        if self.backup_count < 0:
            raise ValueError("backup_count는 0 이상이어야 합니다")


@dataclass
class PipelineConfig:
    """전체 파이프라인 설정"""
    # 모듈별 설정
    md_processor: MDProcessorConfig = field(default_factory=MDProcessorConfig)
    openai_connector: OpenAIConnectorConfig = field(default_factory=OpenAIConnectorConfig)
    qdrant_connector: QdrantConnectorConfig = field(default_factory=QdrantConnectorConfig)
    unsloth_dataset: UnslothDatasetConfig = field(default_factory=UnslothDatasetConfig)
    quality_validator: QualityValidatorConfig = field(default_factory=QualityValidatorConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    
    # 전역 설정
    output_directory: str = "output"
    temp_directory: str = "temp"
    enable_caching: bool = True
    cache_directory: str = "cache"
    max_memory_usage_gb: float = 8.0
    enable_gpu: bool = False
    random_seed: Optional[int] = 42
    
    def __post_init__(self):
        """초기화 후 검증"""
        if self.max_memory_usage_gb <= 0:
            raise ValueError("max_memory_usage_gb는 양의 수여야 합니다")
        
        # 환경 변수에서 API 키 로드
        if not self.openai_connector.api_key:
            self.openai_connector.api_key = os.getenv("OPENAI_API_KEY")
        
        if not self.qdrant_connector.api_key:
            self.qdrant_connector.api_key = os.getenv("QDRANT_API_KEY")


def load_config(config_path: Union[str, Path]) -> PipelineConfig:
    """
    YAML 설정 파일을 로드하여 PipelineConfig 객체 생성
    
    Args:
        config_path: 설정 파일 경로
        
    Returns:
        PipelineConfig: 로드된 설정 객체
        
    Raises:
        FileNotFoundError: 설정 파일이 존재하지 않는 경우
        yaml.YAMLError: YAML 파싱 오류
        ValueError: 설정 값 검증 오류
    """
    config_path = Path(config_path)
    
    if not config_path.exists():
        raise FileNotFoundError(f"설정 파일을 찾을 수 없습니다: {config_path}")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        
        if yaml_data is None:
            yaml_data = {}
        
        # 중첩된 딕셔너리를 데이터클래스로 변환
        config_dict = _convert_yaml_to_config_dict(yaml_data)
        
        return PipelineConfig(**config_dict)
        
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"YAML 파싱 오류: {e}")
    except TypeError as e:
        raise ValueError(f"설정 구조 오류: {e}")
    except Exception as e:
        raise ValueError(f"설정 로드 오류: {e}")


def _convert_yaml_to_config_dict(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    """YAML 데이터를 설정 딕셔너리로 변환"""
    config_dict = {}
    
    # 각 모듈 설정 변환
    module_configs = {
        'md_processor': MDProcessorConfig,
        'openai_connector': OpenAIConnectorConfig,
        'qdrant_connector': QdrantConnectorConfig,
        'unsloth_dataset': UnslothDatasetConfig,
        'quality_validator': QualityValidatorConfig,
        'logging': LoggingConfig
    }
    
    for module_name, config_class in module_configs.items():
        if module_name in yaml_data:
            module_data = yaml_data[module_name]
            if isinstance(module_data, dict):
                config_dict[module_name] = config_class(**module_data)
    
    # 전역 설정 복사
    global_keys = [
        'output_directory', 'temp_directory', 'enable_caching', 'cache_directory',
        'max_memory_usage_gb', 'enable_gpu', 'random_seed'
    ]
    
    for key in global_keys:
        if key in yaml_data:
            config_dict[key] = yaml_data[key]
    
    return config_dict


def validate_config_file(config_path: Union[str, Path]) -> Dict[str, Any]:
    """
    설정 파일 유효성 검증
    
    Args:
        config_path: 검증할 설정 파일 경로
        
    Returns:
        Dict[str, Any]: 검증 결과 정보
        
    Raises:
        FileNotFoundError: 설정 파일이 존재하지 않는 경우
        ValueError: 설정 검증 실패
    """
    try:
        config = load_config(config_path)
        
        # 추가 검증 로직
        validation_results = {
            "valid": True,
            "config": config,
            "warnings": [],
            "errors": []
        }
        
        # 디렉토리 존재 확인
        directories_to_check = [
            config.md_processor.input_directory,
            config.output_directory,
            config.temp_directory
        ]
        
        if config.enable_caching:
            directories_to_check.append(config.cache_directory)
        
        for directory in directories_to_check:
            if not Path(directory).exists():
                validation_results["warnings"].append(
                    f"디렉토리가 존재하지 않습니다: {directory}"
                )
        
        # API 키 확인
        if not config.openai_connector.api_key:
            validation_results["warnings"].append(
                "OpenAI API 키가 설정되지 않았습니다"
            )
        
        # 메모리 사용량 경고
        if config.max_memory_usage_gb > 16:
            validation_results["warnings"].append(
                f"메모리 사용량이 높게 설정되었습니다: {config.max_memory_usage_gb}GB"
            )
        
        return validation_results
        
    except Exception as e:
        return {
            "valid": False,
            "config": None,
            "warnings": [],
            "errors": [str(e)]
        }


def create_default_config(output_path: Union[str, Path]) -> None:
    """
    기본 설정 파일 생성
    
    Args:
        output_path: 생성할 설정 파일 경로
    """
    output_path = Path(output_path)
    
    # 기본 설정 객체 생성
    default_config = PipelineConfig()
    
    # 설정을 YAML 형태로 변환
    config_dict = _config_to_dict(default_config)
    
    # YAML 파일로 저장
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(
            config_dict,
            f,
            default_flow_style=False,
            allow_unicode=True,
            indent=2,
            sort_keys=False
        )


def _config_to_dict(config: PipelineConfig) -> Dict[str, Any]:
    """PipelineConfig 객체를 딕셔너리로 변환"""
    result = {}
    
    # 모듈별 설정 변환
    module_configs = {
        'md_processor': config.md_processor,
        'openai_connector': config.openai_connector,
        'qdrant_connector': config.qdrant_connector,
        'unsloth_dataset': config.unsloth_dataset,
        'quality_validator': config.quality_validator,
        'logging': config.logging
    }
    
    for module_name, module_config in module_configs.items():
        result[module_name] = _dataclass_to_dict(module_config)
    
    # 전역 설정 추가
    global_settings = {
        'output_directory': config.output_directory,
        'temp_directory': config.temp_directory,
        'enable_caching': config.enable_caching,
        'cache_directory': config.cache_directory,
        'max_memory_usage_gb': config.max_memory_usage_gb,
        'enable_gpu': config.enable_gpu,
        'random_seed': config.random_seed
    }
    
    result.update(global_settings)
    
    return result


def _dataclass_to_dict(obj: Any) -> Dict[str, Any]:
    """데이터클래스 객체를 딕셔너리로 변환"""
    if hasattr(obj, '__dataclass_fields__'):
        result = {}
        for field_name, field_obj in obj.__dataclass_fields__.items():
            value = getattr(obj, field_name)
            if isinstance(value, Enum):
                result[field_name] = value.value
            elif isinstance(value, list):
                # 리스트 내의 Enum 객체들도 처리
                result[field_name] = [
                    item.value if isinstance(item, Enum) else item
                    for item in value
                ]
            elif hasattr(value, '__dataclass_fields__'):
                result[field_name] = _dataclass_to_dict(value)
            else:
                result[field_name] = value
        return result
    else:
        return obj