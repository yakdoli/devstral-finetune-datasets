#!/usr/bin/env python3
"""
Unsloth 데이터셋 생성 통합 실행 스크립트

이 스크립트는 모든 모듈을 통합하여 완전한 데이터셋 생성 파이프라인을 제공합니다.
MD 파일 처리 → Qdrant 데이터 검색 → 대화 생성 → 포맷 변환 → 품질 검증의 전체 과정을 자동화합니다.
"""

import asyncio
import argparse
import json
import logging
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime

import yaml
import tqdm
from tqdm import tqdm

# 모든 모듈 임포트
from md_processor import create_processor, create_scanner
from md_processor.processor import ProcessingConfig
from qdrant_connector import create_integrated_processor
from openai_connector import create_openai_connector
from unsloth_dataset import create_dataset_generator, DatasetConfig
from quality_validator import create_default_validator, QualityValidatorConfig


@dataclass
class PipelineConfig:
    """파이프라인 전체 설정"""
    # 프로젝트 설정
    project_name: str = "Syncfusion WinForms Unsloth Dataset"
    project_version: str = "1.0.0"
    target_count: int = 5000
    output_directory: str = "./output/datasets"
    
    # OpenAI API 설정
    openai_endpoint: str = "http://123.37.28.120:9997/v1"
    openai_model: str = "qwen2.5-vl-instruct"
    openai_max_tokens: int = 128000
    openai_temperature: float = 0.3
    
    # Qdrant 설정
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_collection: str = "ws-7491d651ae044c78"
    
    # 데이터 소스 설정
    md_output_path: str = "./output"
    md_staging_path: str = "./md_staging"
    
    # Unsloth 설정
    max_seq_length: int = 4096
    formats: List[str] = field(default_factory=lambda: ["sharegpt", "alpaca", "openai"])
    train_test_split: float = 0.9
    
    # 품질 검증 설정
    min_quality_score: float = 0.7
    max_similarity_threshold: float = 0.9
    safety_threshold: float = 0.8
    enable_auto_correction: bool = True
    
    # 실행 설정
    test_mode: bool = False
    sample_size: int = 100
    verbose: bool = False
    progress_bar: bool = True
    log_level: str = "INFO"
    log_file: str = "dataset_generation.log"
    
    # 단계별 실행 설정
    steps: List[str] = field(default_factory=lambda: [
        "md_processing", "qdrant_search", "conversation_generation",
        "dataset_transformation", "quality_validation"
    ])


class DatasetGenerationPipeline:
    """데이터셋 생성 파이프라인 메인 클래스"""
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.logger = self._setup_logging()
        self.stats = {
            "start_time": datetime.now(),
            "steps_completed": [],
            "documents_processed": 0,
            "conversations_generated": 0,
            "datasets_created": 0,
            "quality_validated": 0,
            "errors": []
        }
        
    def _setup_logging(self) -> logging.Logger:
        """로깅 설정"""
        logging.basicConfig(
            level=getattr(logging, self.config.log_level),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.config.log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        return logging.getLogger(__name__)
    
    async def run_pipeline(self) -> Dict[str, Any]:
        """전체 파이프라인 실행"""
        self.logger.info("데이터셋 생성 파이프라인 시작")
        self.logger.info(f"프로젝트: {self.config.project_name} v{self.config.project_version}")
        
        try:
            # 1. 설정 로드 및 디렉토리 생성
            await self._setup_environment()
            
            # 2. MD 파일 처리
            md_documents = None
            if "md_processing" in self.config.steps:
                md_documents = await self._process_md_files()
                self.stats["steps_completed"].append("md_processing")
            
            # 3. Qdrant 데이터 검색
            qdrant_documents = None
            if "qdrant_search" in self.config.steps:
                qdrant_documents = await self._search_qdrant_documents()
                self.stats["steps_completed"].append("qdrant_search")
            
            # 4. 대화 생성
            conversations = None
            if "conversation_generation" in self.config.steps:
                all_documents = (md_documents or []) + (qdrant_documents or [])
                conversations = await self._generate_conversations(all_documents)
                self.stats["steps_completed"].append("conversation_generation")
            
            # 5. 데이터셋 생성
            datasets = {}
            if "dataset_transformation" in self.config.steps:
                datasets = await self._create_datasets(conversations)
                self.stats["steps_completed"].append("dataset_transformation")
            
            # 6. 품질 검증
            validation_results = {}
            if "quality_validation" in self.config.steps:
                validation_results = await self._validate_quality(datasets)
                self.stats["steps_completed"].append("quality_validation")
            
            # 7. 최종 결과 생성
            result = await self._generate_final_result(
                md_documents, qdrant_documents, conversations, datasets, validation_results
            )
            
            return result
            
        except Exception as e:
            self.logger.error(f"파이프라인 실행 실패: {str(e)}")
            self.stats["errors"].append(str(e))
            raise
    
    async def _setup_environment(self):
        """환경 설정"""
        self.logger.info("환경 설정 중...")
        
        # 출력 디렉토리 생성
        output_path = Path(self.config.output_directory)
        output_path.mkdir(parents=True, exist_ok=True)
        self.logger.info(f"환경 설정 완료: {output_path.absolute()}")
    
    async def _process_md_files(self) -> List[Dict[str, Any]]:
        """MD 파일 처리"""
        self.logger.info("MD 파일 처리 중...")
        
        try:
            # MD 프로세서 생성
            processing_config = ProcessingConfig(
                batch_size=50,
                min_quality_score=0.6,
                max_content_length=8000,
                remove_duplicates=True,
                output_format="json",
                include_metadata=True
            )
            md_processor = create_processor(processing_config)
            
            # 파일 스캐너 생성 (output과 md_staging 두 경로 모두 지정)
            scanner = create_scanner([self.config.md_output_path, self.config.md_staging_path])
            
            # 파일 스캔
            md_files = list(scanner.scan_files(recursive=True))
            self.logger.info(f"발견된 MD 파일: {len(md_files)}개")
            
            # 파일 처리
            output_path = Path(self.config.output_directory) / "processed_documents.json"
            processed_docs = md_processor.process_documents(output_path)
            
            self.stats["documents_processed"] = len(processed_docs)
            self.logger.info(f"MD 파일 처리 완료: {len(processed_docs)}개 문서")
            
            return processed_docs
            
        except Exception as e:
            self.logger.error(f"MD 파일 처리 실패: {str(e)}")
            self.stats["errors"].append(f"MD 처리 실패: {str(e)}")
            return []
    
    async def _search_qdrant_documents(self) -> List[Dict[str, Any]]:
        """Qdrant 데이터 검색"""
        self.logger.info("Qdrant 데이터 검색 중...")
        
        try:
            # Qdrant 프로세서 생성
            qdrant_processor = create_integrated_processor()
            
            # 문서 검색
            search_results = qdrant_processor.process_local_documents(
                base_paths=[self.config.md_staging_path],
                output_path=None
            )
            
            self.stats["documents_processed"] += len(search_results)
            self.logger.info(f"Qdrant 검색 완료: {len(search_results)}개 문서")
            
            return search_results
            
        except Exception as e:
            self.logger.error(f"Qdrant 검색 실패: {str(e)}")
            self.stats["errors"].append(f"Qdrant 검색 실패: {str(e)}")
            return []
    
    async def _generate_conversations(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """대화 생성"""
        self.logger.info("대화 생성 중...")
        
        try:
            # OpenAI 커넥터 생성
            openai_connector = create_openai_connector()
            
            # 대화 생성기 생성
            conversation_generator = openai_connector
            
            # 대화 생성
            conversations = []
            sample_size = min(len(documents), self.config.sample_size) if self.config.test_mode else len(documents)
            
            # async with 컨텍스트로 OpenAI 클라이언트 세션 초기화
            async with openai_connector.client:
                for i, document in enumerate(tqdm(documents[:sample_size], desc="대화 생성")):
                    try:
                        # 단일 대화 생성을 위해 generate_conversations 메서드 수정
                        conversation_list = await conversation_generator.generate_conversations([document], target_count=1)
                        if conversation_list:
                            # Conversation 객체를 Dict로 변환
                            for conv in conversation_list:
                                conversations.append(conv.to_dict())
                    except Exception as e:
                        self.logger.warning(f"대화 생성 실패: {i}, 오류: {str(e)}")
            
            self.stats["conversations_generated"] = len(conversations)
            self.logger.info(f"대화 생성 완료: {len(conversations)}개 대화")
            
            return conversations
            
        except Exception as e:
            self.logger.error(f"대화 생성 실패: {str(e)}")
            self.stats["errors"].append(f"대화 생성 실패: {str(e)}")
            return []
    
    async def _create_datasets(self, conversations: List[Dict[str, Any]]) -> Dict[str, str]:
        """데이터셋 생성"""
        self.logger.info("데이터셋 생성 중...")
        
        try:
            # 데이터셋 생성기 설정
            dataset_config = DatasetConfig(
                max_seq_length=self.config.max_seq_length,
                formats=self.config.formats,
                train_test_split=self.config.train_test_split,
                output_dir=self.config.output_directory,
                test_mode=self.config.test_mode
            )
            
            dataset_generator = create_dataset_generator(dataset_config)
            
            # 데이터셋 생성
            result = dataset_generator.generate_datasets(conversations=conversations)
            datasets = dataset_generator.save_datasets(result, base_name="syncfusion_winforms_test")
            
            self.stats["datasets_created"] = len(datasets)
            self.logger.info(f"데이터셋 생성 완료: {len(datasets)}개 포맷")
            
            return datasets
            
        except Exception as e:
            self.logger.error(f"데이터셋 생성 실패: {str(e)}")
            self.stats["errors"].append(f"데이터셋 생성 실패: {str(e)}")
            return {}
    
    async def _validate_quality(self, datasets: Dict[str, str]) -> Dict[str, Any]:
        """품질 검증"""
        self.logger.info("품질 검증 중...")
        
        try:
            # 품질 검증기 생성
            validator = create_default_validator()
            
            # 데이터셋 품질 검증
            validation_results = {}
            
            # datasets가 비어있는 경우 처리
            if not datasets:
                self.logger.warning("검증할 데이터셋이 없습니다.")
                return validation_results
            
            for format_name, file_path in datasets.items():
                try:
                    # 데이터셋 로드 및 검증
                    with open(file_path, 'r', encoding='utf-8') as f:
                        dataset = [json.loads(line) for line in f]
                    
                    # 데이터셋을 딕셔너리 형식으로 변환
                    dataset_dict = {format_name: dataset}
                    
                    # 검증 수행
                    result = validator.validate_and_filter(dataset_dict)
                    validation_results[format_name] = result
                except Exception as e:
                    self.logger.warning(f"품질 검증 실패: {format_name}, 오류: {str(e)}")
            
            self.stats["quality_validated"] = len(validation_results)
            self.logger.info(f"품질 검증 완료: {len(validation_results)}개 포맷")
            
            return validation_results
            
        except Exception as e:
            self.logger.error(f"품질 검증 실패: {str(e)}")
            self.stats["errors"].append(f"품질 검증 실패: {str(e)}")
            return {}
    
    async def _generate_final_result(self, md_documents: List[Dict[str, Any]], 
                                   qdrant_documents: List[Dict[str, Any]],
                                   conversations: List[Dict[str, Any]], 
                                   datasets: Dict[str, str],
                                   validation_results: Dict[str, Any]) -> Dict[str, Any]:
        """최종 결과 생성"""
        
        end_time = datetime.now()
        duration = end_time - self.stats["start_time"]
        
        return {
            "project": {
                "name": self.config.project_name,
                "version": self.config.project_version,
                "duration_seconds": duration.total_seconds()
            },
            "statistics": {
                "documents_processed": self.stats["documents_processed"],
                "conversations_generated": self.stats["conversations_generated"],
                "datasets_created": self.stats["datasets_created"],
                "quality_validated": self.stats["quality_validated"],
                "errors_count": len(self.stats["errors"])
            },
            "datasets": {
                "sample_size": self.config.sample_size,
                "target_count": self.config.target_count,
                "formats": self.config.formats,
                "output_directory": self.config.output_directory
            },
            "steps_completed": self.stats["steps_completed"],
            "errors": self.stats["errors"]
        }


def load_config(config_path: str) -> PipelineConfig:
    """설정 파일 로드"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)
        
        return PipelineConfig(**config_data)
    except Exception as e:
        print(f"설정 파일 로드 실패: {str(e)}")
        sys.exit(1)


def create_default_config() -> PipelineConfig:
    """기본 설정 생성"""
    return PipelineConfig()


def main():
    """메인 실행 함수"""
    parser = argparse.ArgumentParser(description="Unsloth 데이터셋 생성 통합 스크립트")
    parser.add_argument("--config", "-c", type=str, default="config.yaml",
                       help="설정 파일 경로")
    parser.add_argument("--test-mode", action="store_true",
                       help="테스트 모드 실행 (소량 데이터)")
    parser.add_argument("--sample-size", type=int, default=100,
                       help="테스트 모드 샘플 크기")
    parser.add_argument("--steps", type=str, default=None,
                       help="실행할 단계 (쉼표로 구분)")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="상세 로그 출력")
    parser.add_argument("--progress-bar", action="store_true", default=True,
                       help="진행률 바 표시")
    parser.add_argument("--log-level", type=str, default="INFO",
                       choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                       help="로그 레벨")
    
    args = parser.parse_args()
    
    # 설정 로드
    if Path(args.config).exists():
        config = load_config(args.config)
    else:
        print(f"설정 파일 '{args.config}' 를 찾을 수 없습니다. 기본 설정을 사용합니다.")
        config = create_default_config()
    
    # CLI 인자로 설정 업데이트
    config.test_mode = args.test_mode
    config.sample_size = args.sample_size
    config.verbose = args.verbose or config.verbose
    config.progress_bar = args.progress_bar
    config.log_level = args.log_level
    
    if args.steps:
        config.steps = args.steps.split(",")
    
    # 파이프라인 실행
    pipeline = DatasetGenerationPipeline(config)
    
    try:
        result = asyncio.run(pipeline.run_pipeline())
        
        print("\n" + "="*50)
        print("데이터셋 생성 완료!")
        print("="*50)
        print(f"프로젝트: {result['project']['name']}")
        print(f"처리 시간: {result['project']['duration_seconds']:.2f}초")
        print(f"처리된 문서: {result['statistics']['documents_processed']}개")
        print(f"생성된 대화: {result['statistics']['conversations_generated']}개")
        print(f"생성된 데이터셋: {result['statistics']['datasets_created']}개")
        print(f"품질 검증 항목: {result['statistics']['quality_validated']}개")
        print(f"완료된 단계: {', '.join(result['steps_completed'])}")
        print(f"출력 디렉토리: {config.output_directory}")
        
        if result['statistics']['errors_count'] > 0:
            print(f"\n발생한 오류: {result['statistics']['errors_count']}개")
            for error in result['errors']:
                print(f"  - {error}")
        
        print("\n생성된 파일:")
        output_dir = Path(config.output_directory)
        if output_dir.exists():
            for file in output_dir.glob("*.json*"):
                print(f"  - {file.name}")
        
    except KeyboardInterrupt:
        print("\n사용자에 의해 실행이 중단되었습니다.")
        sys.exit(1)
    except Exception as e:
        print(f"\n실행 실패: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()