"""
설정 관리 모듈 단위 테스트
"""

import unittest
import tempfile
import os
import yaml
from pathlib import Path

from config import (
    PipelineConfig,
    MDProcessorConfig,
    OpenAIConnectorConfig,
    QdrantConnectorConfig,
    UnslothDatasetConfig,
    QualityValidatorConfig,
    LoggingConfig,
    LogLevel,
    OutputFormat,
    load_config,
    validate_config_file,
    create_default_config
)


class TestConfigDataClasses(unittest.TestCase):
    """설정 데이터클래스 테스트"""
    
    def test_md_processor_config_defaults(self):
        """MDProcessorConfig 기본값 테스트"""
        config = MDProcessorConfig()
        self.assertEqual(config.input_directory, "md_staging")
        self.assertEqual(config.file_extensions, [".md", ".markdown"])
        self.assertEqual(config.max_file_size_mb, 10)
        self.assertEqual(config.encoding, "utf-8")
        self.assertTrue(config.skip_empty_files)
        self.assertTrue(config.preserve_code_blocks)
        self.assertTrue(config.extract_api_signatures)
    
    def test_md_processor_config_validation(self):
        """MDProcessorConfig 검증 테스트"""
        # 유효하지 않은 max_file_size_mb
        with self.assertRaises(ValueError):
            MDProcessorConfig(max_file_size_mb=0)
        
        with self.assertRaises(ValueError):
            MDProcessorConfig(max_file_size_mb=-1)
        
        # 빈 file_extensions
        with self.assertRaises(ValueError):
            MDProcessorConfig(file_extensions=[])
    
    def test_openai_connector_config_defaults(self):
        """OpenAIConnectorConfig 기본값 테스트"""
        config = OpenAIConnectorConfig()
        self.assertEqual(config.api_base_url, "http://123.37.28.120:9997/v1")
        self.assertEqual(config.model_name, "qwen2.5-vl-instruct")
        self.assertIsNone(config.api_key)
        self.assertEqual(config.max_tokens, 8192)
        self.assertEqual(config.temperature, 0.7)
        self.assertEqual(config.batch_size, 16)
        self.assertEqual(config.max_concurrent_requests, 8)
    
    def test_openai_connector_config_validation(self):
        """OpenAIConnectorConfig 검증 테스트"""
        # 유효하지 않은 max_tokens
        with self.assertRaises(ValueError):
            OpenAIConnectorConfig(max_tokens=0)
        
        # 유효하지 않은 temperature
        with self.assertRaises(ValueError):
            OpenAIConnectorConfig(temperature=-0.1)
        
        with self.assertRaises(ValueError):
            OpenAIConnectorConfig(temperature=2.1)
        
        # 유효하지 않은 top_p
        with self.assertRaises(ValueError):
            OpenAIConnectorConfig(top_p=-0.1)
        
        with self.assertRaises(ValueError):
            OpenAIConnectorConfig(top_p=1.1)
        
        # 유효하지 않은 batch_size
        with self.assertRaises(ValueError):
            OpenAIConnectorConfig(batch_size=0)
        
        # 유효하지 않은 max_concurrent_requests
        with self.assertRaises(ValueError):
            OpenAIConnectorConfig(max_concurrent_requests=0)
    
    def test_qdrant_connector_config_defaults(self):
        """QdrantConnectorConfig 기본값 테스트"""
        config = QdrantConnectorConfig()
        self.assertEqual(config.host, "localhost")
        self.assertEqual(config.port, 6333)
        self.assertEqual(config.collection_name, "ws-7491d651ae044c78")
        self.assertIsNone(config.api_key)
        self.assertEqual(config.similarity_threshold, 0.7)
        self.assertEqual(config.max_results, 10)
    
    def test_qdrant_connector_config_validation(self):
        """QdrantConnectorConfig 검증 테스트"""
        # 유효하지 않은 port
        with self.assertRaises(ValueError):
            QdrantConnectorConfig(port=0)
        
        with self.assertRaises(ValueError):
            QdrantConnectorConfig(port=65536)
        
        # 유효하지 않은 similarity_threshold
        with self.assertRaises(ValueError):
            QdrantConnectorConfig(similarity_threshold=-0.1)
        
        with self.assertRaises(ValueError):
            QdrantConnectorConfig(similarity_threshold=1.1)
        
        # 유효하지 않은 max_results
        with self.assertRaises(ValueError):
            QdrantConnectorConfig(max_results=0)
        
        # 유효하지 않은 batch_size
        with self.assertRaises(ValueError):
            QdrantConnectorConfig(batch_size=0)
    
    def test_unsloth_dataset_config_defaults(self):
        """UnslothDatasetConfig 기본값 테스트"""
        config = UnslothDatasetConfig()
        self.assertEqual(config.target_conversation_count, 1000)
        self.assertEqual(config.output_formats, [
            OutputFormat.SHAREGPT, OutputFormat.ALPACA, OutputFormat.OPENAI
        ])
        self.assertEqual(config.train_test_split, 0.8)
        self.assertEqual(config.max_conversation_length, 8192)
        self.assertEqual(config.min_conversation_length, 50)
        self.assertTrue(config.include_system_messages)
    
    def test_unsloth_dataset_config_validation(self):
        """UnslothDatasetConfig 검증 테스트"""
        # 유효하지 않은 target_conversation_count
        with self.assertRaises(ValueError):
            UnslothDatasetConfig(target_conversation_count=0)
        
        # 유효하지 않은 train_test_split
        with self.assertRaises(ValueError):
            UnslothDatasetConfig(train_test_split=0.0)
        
        with self.assertRaises(ValueError):
            UnslothDatasetConfig(train_test_split=1.0)
        
        # 유효하지 않은 conversation_length
        with self.assertRaises(ValueError):
            UnslothDatasetConfig(
                min_conversation_length=100,
                max_conversation_length=50
            )
        
        # 빈 output_formats
        with self.assertRaises(ValueError):
            UnslothDatasetConfig(output_formats=[])
    
    def test_quality_validator_config_defaults(self):
        """QualityValidatorConfig 기본값 테스트"""
        config = QualityValidatorConfig()
        self.assertEqual(config.min_quality_score, 0.7)
        self.assertTrue(config.enable_safety_filter)
        self.assertTrue(config.enable_duplicate_removal)
        self.assertTrue(config.enable_auto_correction)
        self.assertEqual(config.similarity_threshold_for_duplicates, 0.9)
        self.assertEqual(config.max_correction_attempts, 3)
    
    def test_quality_validator_config_validation(self):
        """QualityValidatorConfig 검증 테스트"""
        # 유효하지 않은 min_quality_score
        with self.assertRaises(ValueError):
            QualityValidatorConfig(min_quality_score=-0.1)
        
        with self.assertRaises(ValueError):
            QualityValidatorConfig(min_quality_score=1.1)
        
        # 유효하지 않은 similarity_threshold_for_duplicates
        with self.assertRaises(ValueError):
            QualityValidatorConfig(similarity_threshold_for_duplicates=-0.1)
        
        with self.assertRaises(ValueError):
            QualityValidatorConfig(similarity_threshold_for_duplicates=1.1)
        
        # 유효하지 않은 max_correction_attempts
        with self.assertRaises(ValueError):
            QualityValidatorConfig(max_correction_attempts=0)
    
    def test_logging_config_defaults(self):
        """LoggingConfig 기본값 테스트"""
        config = LoggingConfig()
        self.assertEqual(config.level, LogLevel.INFO)
        self.assertEqual(config.file_path, "output/logs/pipeline.log")
        self.assertEqual(config.max_file_size_mb, 100)
        self.assertEqual(config.backup_count, 5)
        self.assertTrue(config.enable_console_output)
        self.assertTrue(config.enable_file_output)
    
    def test_logging_config_validation(self):
        """LoggingConfig 검증 테스트"""
        # 유효하지 않은 max_file_size_mb
        with self.assertRaises(ValueError):
            LoggingConfig(max_file_size_mb=0)
        
        # 유효하지 않은 backup_count
        with self.assertRaises(ValueError):
            LoggingConfig(backup_count=-1)
    
    def test_pipeline_config_defaults(self):
        """PipelineConfig 기본값 테스트"""
        config = PipelineConfig()
        self.assertIsInstance(config.md_processor, MDProcessorConfig)
        self.assertIsInstance(config.openai_connector, OpenAIConnectorConfig)
        self.assertIsInstance(config.qdrant_connector, QdrantConnectorConfig)
        self.assertIsInstance(config.unsloth_dataset, UnslothDatasetConfig)
        self.assertIsInstance(config.quality_validator, QualityValidatorConfig)
        self.assertIsInstance(config.logging, LoggingConfig)
        
        self.assertEqual(config.output_directory, "output")
        self.assertEqual(config.temp_directory, "temp")
        self.assertTrue(config.enable_caching)
        self.assertEqual(config.cache_directory, "cache")
        self.assertEqual(config.max_memory_usage_gb, 8.0)
        self.assertFalse(config.enable_gpu)
        self.assertEqual(config.random_seed, 42)
    
    def test_pipeline_config_validation(self):
        """PipelineConfig 검증 테스트"""
        # 유효하지 않은 max_memory_usage_gb
        with self.assertRaises(ValueError):
            PipelineConfig(max_memory_usage_gb=0)


class TestConfigLoading(unittest.TestCase):
    """설정 로딩 테스트"""
    
    def test_load_config_valid_yaml(self):
        """유효한 YAML 설정 로딩 테스트"""
        config_data = {
            'md_processor': {
                'input_directory': 'test_md',
                'max_file_size_mb': 5
            },
            'openai_connector': {
                'model_name': 'test-model',
                'max_tokens': 4096
            },
            'output_directory': 'test_output',
            'max_memory_usage_gb': 4.0
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(config_data, f)
            config_path = f.name
        
        try:
            config = load_config(config_path)
            
            self.assertEqual(config.md_processor.input_directory, 'test_md')
            self.assertEqual(config.md_processor.max_file_size_mb, 5)
            self.assertEqual(config.openai_connector.model_name, 'test-model')
            self.assertEqual(config.openai_connector.max_tokens, 4096)
            self.assertEqual(config.output_directory, 'test_output')
            self.assertEqual(config.max_memory_usage_gb, 4.0)
            
        finally:
            os.unlink(config_path)
    
    def test_load_config_empty_yaml(self):
        """빈 YAML 설정 로딩 테스트"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("")
            config_path = f.name
        
        try:
            config = load_config(config_path)
            # 기본값으로 설정되어야 함
            self.assertIsInstance(config, PipelineConfig)
            
        finally:
            os.unlink(config_path)
    
    def test_load_config_nonexistent_file(self):
        """존재하지 않는 파일 로딩 테스트"""
        with self.assertRaises(FileNotFoundError):
            load_config("nonexistent.yaml")
    
    def test_load_config_invalid_yaml(self):
        """유효하지 않은 YAML 로딩 테스트"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("invalid: yaml: content: [")
            config_path = f.name
        
        try:
            with self.assertRaises(yaml.YAMLError):
                load_config(config_path)
                
        finally:
            os.unlink(config_path)
    
    def test_load_config_invalid_values(self):
        """유효하지 않은 설정값 로딩 테스트"""
        config_data = {
            'md_processor': {
                'max_file_size_mb': -1  # 유효하지 않은 값
            }
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(config_data, f)
            config_path = f.name
        
        try:
            with self.assertRaises(ValueError):
                load_config(config_path)
                
        finally:
            os.unlink(config_path)


class TestConfigValidation(unittest.TestCase):
    """설정 검증 테스트"""
    
    def test_validate_config_file_valid(self):
        """유효한 설정 파일 검증 테스트"""
        config_data = {
            'md_processor': {
                'input_directory': 'md_staging'
            },
            'output_directory': 'output'
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(config_data, f)
            config_path = f.name
        
        try:
            result = validate_config_file(config_path)
            
            self.assertTrue(result['valid'])
            self.assertIsInstance(result['config'], PipelineConfig)
            self.assertIsInstance(result['warnings'], list)
            self.assertIsInstance(result['errors'], list)
            
        finally:
            os.unlink(config_path)
    
    def test_validate_config_file_invalid(self):
        """유효하지 않은 설정 파일 검증 테스트"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("invalid: yaml: [")
            config_path = f.name
        
        try:
            result = validate_config_file(config_path)
            
            self.assertFalse(result['valid'])
            self.assertIsNone(result['config'])
            self.assertGreater(len(result['errors']), 0)
            
        finally:
            os.unlink(config_path)
    
    def test_validate_config_file_nonexistent(self):
        """존재하지 않는 설정 파일 검증 테스트"""
        result = validate_config_file("nonexistent.yaml")
        
        self.assertFalse(result['valid'])
        self.assertIsNone(result['config'])
        self.assertGreater(len(result['errors']), 0)


class TestConfigCreation(unittest.TestCase):
    """설정 생성 테스트"""
    
    def test_create_default_config(self):
        """기본 설정 파일 생성 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.yaml"
            
            create_default_config(config_path)
            
            self.assertTrue(config_path.exists())
            
            # 생성된 파일을 다시 로드해서 검증
            config = load_config(config_path)
            self.assertIsInstance(config, PipelineConfig)
    
    def test_create_default_config_overwrite(self):
        """기본 설정 파일 덮어쓰기 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "test_config.yaml"
            
            # 먼저 파일 생성
            config_path.write_text("existing content")
            self.assertTrue(config_path.exists())
            
            # 덮어쓰기
            create_default_config(config_path)
            
            # YAML 형태로 덮어써졌는지 확인
            config = load_config(config_path)
            self.assertIsInstance(config, PipelineConfig)


class TestEnvironmentVariables(unittest.TestCase):
    """환경 변수 테스트"""
    
    def test_api_key_from_environment(self):
        """환경 변수에서 API 키 로드 테스트"""
        # 환경 변수 설정
        os.environ['OPENAI_API_KEY'] = 'test-openai-key'
        os.environ['QDRANT_API_KEY'] = 'test-qdrant-key'
        
        try:
            config = PipelineConfig()
            
            self.assertEqual(config.openai_connector.api_key, 'test-openai-key')
            self.assertEqual(config.qdrant_connector.api_key, 'test-qdrant-key')
            
        finally:
            # 환경 변수 정리
            if 'OPENAI_API_KEY' in os.environ:
                del os.environ['OPENAI_API_KEY']
            if 'QDRANT_API_KEY' in os.environ:
                del os.environ['QDRANT_API_KEY']


if __name__ == "__main__":
    unittest.main()