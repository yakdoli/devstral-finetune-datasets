"""
파이프라인 오케스트레이터 - 전체 데이터셋 생성 파이프라인 조정 및 관리

이 모듈은 모든 하위 모듈들을 통합하여 완전한 데이터셋 생성 파이프라인을 제공합니다.
단계별 실행, 체크포인트 지원, 오류 복구, 진행률 모니터링 등의 기능을 포함합니다.
"""

import asyncio
import json
import logging
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable, Union
from dataclasses import dataclass, field
from enum import Enum
import traceback

from tqdm.asyncio import tqdm

# 모든 모듈 임포트
from md_processor import create_processor, create_scanner
from md_processor.processor import ProcessingConfig
from qdrant_connector import create_integrated_processor
from openai_connector import create_openai_connector
from unsloth_dataset import create_dataset_generator, DatasetConfig
from quality_validator import create_default_validator
from config.config import PipelineConfig
from logging_system.structured_logger import StructuredLogger
from async_pipeline.progress_tracker import ProgressTracker
from async_pipeline.memory_manager import MemoryManager


class PipelineStage(str, Enum):
    """파이프라인 단계 열거형"""
    INITIALIZATION = "initialization"
    MD_PROCESSING = "md_processing"
    QDRANT_SEARCH = "qdrant_search"
    CONVERSATION_GENERATION = "conversation_generation"
    DATASET_TRANSFORMATION = "dataset_transformation"
    QUALITY_VALIDATION = "quality_validation"
    FINALIZATION = "finalization"


class StageStatus(str, Enum):
    """단계 상태 열거형"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class StageResult:
    """단계 실행 결과"""
    stage: PipelineStage
    status: StageStatus
    start_time: datetime
    end_time: Optional[datetime] = None
    duration: Optional[timedelta] = None
    data: Optional[Any] = None
    error: Optional[str] = None
    metrics: Dict[str, Any] = field(default_factory=dict)
    
    def complete(self, data: Any = None, metrics: Dict[str, Any] = None):
        """단계 완료 처리"""
        self.end_time = datetime.now()
        self.duration = self.end_time - self.start_time
        self.status = StageStatus.COMPLETED
        self.data = data
        if metrics:
            self.metrics.update(metrics)
    
    def fail(self, error: str):
        """단계 실패 처리"""
        self.end_time = datetime.now()
        self.duration = self.end_time - self.start_time
        self.status = StageStatus.FAILED
        self.error = error


@dataclass
class CheckpointData:
    """체크포인트 데이터"""
    stage: PipelineStage
    timestamp: datetime
    data: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


class PipelineOrchestrator:
    """
    파이프라인 오케스트레이터 - 전체 데이터셋 생성 파이프라인 조정
    
    주요 기능:
    - 단계별 파이프라인 실행 및 관리
    - 체크포인트 지원 (중간 결과 저장/복원)
    - 오류 복구 및 재시도 로직
    - 실시간 진행률 모니터링
    - 메모리 및 리소스 관리
    - 상세한 로깅 및 메트릭 수집
    """
    
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.logger = StructuredLogger("PipelineOrchestrator")
        self.progress_tracker = ProgressTracker()
        self.memory_manager = MemoryManager()
        
        # 파이프라인 상태
        self.stage_results: Dict[PipelineStage, StageResult] = {}
        self.current_stage: Optional[PipelineStage] = None
        self.pipeline_start_time: Optional[datetime] = None
        self.pipeline_end_time: Optional[datetime] = None
        
        # 체크포인트 관리
        self.checkpoint_dir = Path(config.output_directory) / "checkpoints"
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        
        # 단계별 핸들러 매핑
        self.stage_handlers = {
            PipelineStage.INITIALIZATION: self._handle_initialization,
            PipelineStage.MD_PROCESSING: self._handle_md_processing,
            PipelineStage.QDRANT_SEARCH: self._handle_qdrant_search,
            PipelineStage.CONVERSATION_GENERATION: self._handle_conversation_generation,
            PipelineStage.DATASET_TRANSFORMATION: self._handle_dataset_transformation,
            PipelineStage.QUALITY_VALIDATION: self._handle_quality_validation,
            PipelineStage.FINALIZATION: self._handle_finalization,
        }
        
        # 단계별 의존성 정의
        self.stage_dependencies = {
            PipelineStage.INITIALIZATION: [],
            PipelineStage.MD_PROCESSING: [PipelineStage.INITIALIZATION],
            PipelineStage.QDRANT_SEARCH: [PipelineStage.INITIALIZATION],
            PipelineStage.CONVERSATION_GENERATION: [
                PipelineStage.MD_PROCESSING, 
                PipelineStage.QDRANT_SEARCH
            ],
            PipelineStage.DATASET_TRANSFORMATION: [PipelineStage.CONVERSATION_GENERATION],
            PipelineStage.QUALITY_VALIDATION: [PipelineStage.DATASET_TRANSFORMATION],
            PipelineStage.FINALIZATION: [PipelineStage.QUALITY_VALIDATION],
        }
    
    async def run_pipeline(self, 
                          stages: Optional[List[PipelineStage]] = None,
                          resume_from_checkpoint: bool = False) -> Dict[str, Any]:
        """
        전체 파이프라인 실행
        
        Args:
            stages: 실행할 단계 목록 (None이면 모든 단계)
            resume_from_checkpoint: 체크포인트에서 재개 여부
            
        Returns:
            Dict[str, Any]: 파이프라인 실행 결과
        """
        self.pipeline_start_time = datetime.now()
        self.logger.info("파이프라인 실행 시작", extra={
            "config": self.config.__dict__,
            "stages": [s.value for s in (stages or list(PipelineStage))]
        })
        
        try:
            # 체크포인트에서 복원
            if resume_from_checkpoint:
                await self._restore_from_checkpoint()
            
            # 실행할 단계 결정
            if stages is None:
                stages = list(PipelineStage)
            
            # 단계별 실행
            for stage in stages:
                if await self._should_skip_stage(stage):
                    self.logger.info(f"단계 건너뛰기: {stage.value}")
                    continue
                
                await self._execute_stage(stage)
                
                # 체크포인트 저장
                await self._save_checkpoint(stage)
                
                # 메모리 정리
                await self._cleanup_memory()
            
            # 파이프라인 완료
            self.pipeline_end_time = datetime.now()
            result = await self._generate_pipeline_result()
            
            self.logger.info("파이프라인 실행 완료", extra={
                "duration": (self.pipeline_end_time - self.pipeline_start_time).total_seconds(),
                "stages_completed": len([r for r in self.stage_results.values() 
                                       if r.status == StageStatus.COMPLETED])
            })
            
            return result
            
        except Exception as e:
            self.logger.error("파이프라인 실행 실패", extra={
                "error": str(e),
                "traceback": traceback.format_exc(),
                "current_stage": self.current_stage.value if self.current_stage else None
            })
            raise
    
    async def _execute_stage(self, stage: PipelineStage):
        """단계 실행"""
        self.current_stage = stage
        
        # 의존성 확인
        if not await self._check_dependencies(stage):
            raise RuntimeError(f"단계 {stage.value}의 의존성이 충족되지 않았습니다")
        
        # 단계 결과 초기화
        stage_result = StageResult(
            stage=stage,
            status=StageStatus.RUNNING,
            start_time=datetime.now()
        )
        self.stage_results[stage] = stage_result
        
        self.logger.info(f"단계 시작: {stage.value}")
        
        try:
            # 단계별 핸들러 실행
            handler = self.stage_handlers.get(stage)
            if not handler:
                raise RuntimeError(f"단계 {stage.value}에 대한 핸들러가 없습니다")
            
            # 진행률 추적 시작
            self.progress_tracker.start_stage(stage.value)
            
            # 핸들러 실행
            result_data = await handler()
            
            # 단계 완료
            stage_result.complete(
                data=result_data,
                metrics=self.progress_tracker.get_stage_metrics(stage.value)
            )
            
            self.logger.info(f"단계 완료: {stage.value}", extra={
                "duration": stage_result.duration.total_seconds(),
                "metrics": stage_result.metrics
            })
            
        except Exception as e:
            stage_result.fail(str(e))
            self.logger.error(f"단계 실패: {stage.value}", extra={
                "error": str(e),
                "traceback": traceback.format_exc()
            })
            raise
        finally:
            self.progress_tracker.end_stage(stage.value)
    
    async def _check_dependencies(self, stage: PipelineStage) -> bool:
        """단계 의존성 확인"""
        dependencies = self.stage_dependencies.get(stage, [])
        
        for dep_stage in dependencies:
            if dep_stage not in self.stage_results:
                return False
            
            if self.stage_results[dep_stage].status != StageStatus.COMPLETED:
                return False
        
        return True
    
    async def _should_skip_stage(self, stage: PipelineStage) -> bool:
        """단계 건너뛰기 여부 확인"""
        # 이미 완료된 단계는 건너뛰기
        if stage in self.stage_results and self.stage_results[stage].status == StageStatus.COMPLETED:
            return True
        
        # 설정에 따른 단계 건너뛰기
        stage_config_map = {
            PipelineStage.MD_PROCESSING: "enable_md_processing",
            PipelineStage.QDRANT_SEARCH: "enable_qdrant_search",
            PipelineStage.CONVERSATION_GENERATION: "enable_conversation_generation",
            PipelineStage.DATASET_TRANSFORMATION: "enable_dataset_transformation",
            PipelineStage.QUALITY_VALIDATION: "enable_quality_validation",
        }
        
        config_key = stage_config_map.get(stage)
        if config_key and hasattr(self.config, config_key):
            return not getattr(self.config, config_key)
        
        return False
    
    # 단계별 핸들러 구현
    
    async def _handle_initialization(self) -> Dict[str, Any]:
        """초기화 단계"""
        self.logger.info("파이프라인 초기화 중...")
        
        # 출력 디렉토리 생성
        output_dir = Path(self.config.output_directory)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 임시 디렉토리 생성
        temp_dir = Path(self.config.temp_directory)
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        # 캐시 디렉토리 생성
        if self.config.enable_caching:
            cache_dir = Path(self.config.cache_directory)
            cache_dir.mkdir(parents=True, exist_ok=True)
        
        # 메모리 관리자 초기화
        self.memory_manager.set_memory_limit(self.config.max_memory_usage_gb)
        
        return {
            "output_directory": str(output_dir.absolute()),
            "temp_directory": str(temp_dir.absolute()),
            "cache_directory": str(cache_dir.absolute()) if self.config.enable_caching else None,
            "memory_limit_gb": self.config.max_memory_usage_gb
        }
    
    async def _handle_md_processing(self) -> List[Dict[str, Any]]:
        """MD 파일 처리 단계"""
        self.logger.info("MD 파일 처리 시작...")
        
        # MD 프로세서 생성
        processing_config = ProcessingConfig(
            batch_size=50,
            min_quality_score=self.config.quality_validator.min_quality_score,
            max_content_length=self.config.unsloth_dataset.max_conversation_length,
            remove_duplicates=self.config.quality_validator.enable_duplicate_removal,
            output_format="json",
            include_metadata=True
        )
        
        md_processor = create_processor(processing_config)
        
        # 파일 스캐너 생성
        scanner = create_scanner([
            self.config.md_processor.input_directory,
            str(Path(self.config.output_directory) / "md_files")
        ])
        
        # 파일 스캔
        md_files = list(scanner.scan_files(recursive=True))
        self.logger.info(f"발견된 MD 파일: {len(md_files)}개")
        
        if not md_files:
            self.logger.warning("처리할 MD 파일이 없습니다")
            return []
        
        # 진행률 추적
        self.progress_tracker.set_total_items("md_processing", len(md_files))
        
        # 파일 처리
        output_path = Path(self.config.output_directory) / "processed_documents.json"
        processed_docs = md_processor.process_documents(output_path)
        
        self.logger.info(f"MD 파일 처리 완료: {len(processed_docs)}개 문서")
        
        return processed_docs
    
    async def _handle_qdrant_search(self) -> List[Dict[str, Any]]:
        """Qdrant 검색 단계"""
        self.logger.info("Qdrant 데이터 검색 시작...")
        
        try:
            # Qdrant 프로세서 생성
            qdrant_processor = create_integrated_processor()
            
            # 문서 검색
            search_results = qdrant_processor.process_local_documents(
                base_paths=[self.config.md_processor.input_directory],
                output_path=None
            )
            
            self.logger.info(f"Qdrant 검색 완료: {len(search_results)}개 문서")
            
            return search_results
            
        except Exception as e:
            self.logger.warning(f"Qdrant 검색 실패, 건너뛰기: {str(e)}")
            return []
    
    async def _handle_conversation_generation(self) -> List[Dict[str, Any]]:
        """대화 생성 단계"""
        self.logger.info("대화 생성 시작...")
        
        # 이전 단계 결과 수집
        md_documents = self.stage_results.get(PipelineStage.MD_PROCESSING, StageResult(
            PipelineStage.MD_PROCESSING, StageStatus.SKIPPED, datetime.now()
        )).data or []
        
        qdrant_documents = self.stage_results.get(PipelineStage.QDRANT_SEARCH, StageResult(
            PipelineStage.QDRANT_SEARCH, StageStatus.SKIPPED, datetime.now()
        )).data or []
        
        all_documents = md_documents + qdrant_documents
        
        if not all_documents:
            self.logger.warning("대화 생성을 위한 문서가 없습니다")
            return []
        
        # OpenAI 커넥터 생성
        openai_connector = create_openai_connector()
        
        # 대화 생성
        conversations = []
        target_count = min(
            len(all_documents),
            self.config.unsloth_dataset.target_conversation_count
        )
        
        self.progress_tracker.set_total_items("conversation_generation", target_count)
        
        # 배치 단위로 대화 생성
        batch_size = self.config.openai_connector.batch_size
        
        async with openai_connector.client:
            for i in range(0, target_count, batch_size):
                batch_docs = all_documents[i:i + batch_size]
                
                try:
                    batch_conversations = await openai_connector.generate_conversations(
                        batch_docs, target_count=len(batch_docs)
                    )
                    
                    # Conversation 객체를 Dict로 변환
                    for conv in batch_conversations:
                        conversations.append(conv.to_dict())
                    
                    self.progress_tracker.update_progress("conversation_generation", len(batch_conversations))
                    
                except Exception as e:
                    self.logger.warning(f"배치 대화 생성 실패: {str(e)}")
                    continue
                
                # 메모리 관리
                if self.memory_manager.should_cleanup():
                    await self._cleanup_memory()
        
        self.logger.info(f"대화 생성 완료: {len(conversations)}개 대화")
        
        return conversations
    
    async def _handle_dataset_transformation(self) -> Dict[str, str]:
        """데이터셋 변환 단계"""
        self.logger.info("데이터셋 변환 시작...")
        
        # 이전 단계 결과 가져오기
        conversations = self.stage_results.get(
            PipelineStage.CONVERSATION_GENERATION, 
            StageResult(PipelineStage.CONVERSATION_GENERATION, StageStatus.SKIPPED, datetime.now())
        ).data or []
        
        if not conversations:
            self.logger.warning("변환할 대화가 없습니다")
            return {}
        
        # 데이터셋 생성기 설정 (컴포넌트 조직화 포함)
        from unsloth_dataset.component_organizer import OrganizationConfig
        
        dataset_config = DatasetConfig(
            max_seq_length=self.config.unsloth_dataset.max_conversation_length,
            formats=[fmt.value for fmt in self.config.unsloth_dataset.output_formats],
            train_test_split=self.config.unsloth_dataset.train_test_split,
            output_dir=self.config.output_directory,
            test_mode=False,
            # 컴포넌트 조직화 활성화
            enable_component_organization=True,
            create_component_specific_datasets=True,
            create_category_specific_datasets=True,
            component_organization=OrganizationConfig(
                min_samples_per_component=5,
                max_samples_per_component=500,
                enable_hierarchical_grouping=True,
                enable_category_balancing=True,
                priority_based_sampling=True,
                output_separate_files=True,
                include_mixed_category=True,
                mixed_category_ratio=0.1
            )
        )
        
        dataset_generator = create_dataset_generator(dataset_config)
        
        # 데이터셋 생성 (컴포넌트 조직화 포함)
        result = dataset_generator.generate_datasets(conversations=conversations)
        datasets = dataset_generator.save_datasets(result, base_name="syncfusion_winforms")
        
        # 컴포넌트 조직화 결과 로깅
        if result.component_datasets:
            self.logger.info(f"컴포넌트별 데이터셋 생성: {len(result.component_datasets)}개 컴포넌트")
            for component_name, dataset in result.component_datasets.items():
                self.logger.info(f"  {component_name} ({dataset.category}): {len(dataset.samples)} 샘플")
        
        if result.category_datasets:
            self.logger.info(f"카테고리별 데이터셋 생성: {len(result.category_datasets)}개 카테고리")
            for category, datasets_list in result.category_datasets.items():
                total_samples = sum(len(ds.samples) for ds in datasets_list)
                self.logger.info(f"  {category}: {len(datasets_list)} 컴포넌트, {total_samples} 샘플")
        
        # 조직화 리포트 로깅
        if result.organization_report:
            report = result.organization_report
            self.logger.info("데이터셋 조직화 리포트:")
            self.logger.info(f"  총 컴포넌트: {report['summary']['total_components']}")
            self.logger.info(f"  총 카테고리: {report['summary']['total_categories']}")
            self.logger.info(f"  총 샘플: {report['summary']['total_samples']}")
            
            if report.get('recommendations'):
                self.logger.info("권장사항:")
                for rec in report['recommendations'][:3]:  # 상위 3개만 로깅
                    self.logger.info(f"  - {rec}")
        
        self.logger.info(f"데이터셋 변환 완료: {len(datasets)}개 파일 생성")
        
        return datasets
    
    async def _handle_quality_validation(self) -> Dict[str, Any]:
        """품질 검증 단계"""
        self.logger.info("품질 검증 시작...")
        
        # 이전 단계 결과 가져오기
        datasets = self.stage_results.get(
            PipelineStage.DATASET_TRANSFORMATION,
            StageResult(PipelineStage.DATASET_TRANSFORMATION, StageStatus.SKIPPED, datetime.now())
        ).data or {}
        
        if not datasets:
            self.logger.warning("검증할 데이터셋이 없습니다")
            return {}
        
        # 품질 검증기 생성
        validator = create_default_validator()
        
        # 데이터셋 품질 검증
        validation_results = {}
        
        for format_name, file_path in datasets.items():
            try:
                # 데이터셋 로드
                with open(file_path, 'r', encoding='utf-8') as f:
                    dataset = [json.loads(line) for line in f]
                
                # 검증 수행
                dataset_dict = {format_name: dataset}
                result = validator.validate_and_filter(dataset_dict)
                validation_results[format_name] = result
                
            except Exception as e:
                self.logger.warning(f"품질 검증 실패: {format_name}, 오류: {str(e)}")
        
        self.logger.info(f"품질 검증 완료: {len(validation_results)}개 포맷")
        
        return validation_results
    
    async def _handle_finalization(self) -> Dict[str, Any]:
        """마무리 단계"""
        self.logger.info("파이프라인 마무리 중...")
        
        # 최종 통계 수집
        final_stats = {
            "pipeline_duration": (datetime.now() - self.pipeline_start_time).total_seconds(),
            "stages_completed": len([r for r in self.stage_results.values() 
                                   if r.status == StageStatus.COMPLETED]),
            "stages_failed": len([r for r in self.stage_results.values() 
                                if r.status == StageStatus.FAILED]),
            "memory_usage": self.memory_manager.get_current_usage(),
            "performance_metrics": self.progress_tracker.get_overall_metrics()
        }
        
        # 최종 리포트 생성
        report_path = Path(self.config.output_directory) / "pipeline_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(final_stats, f, indent=2, ensure_ascii=False, default=str)
        
        self.logger.info("파이프라인 마무리 완료", extra=final_stats)
        
        return final_stats
    
    # 체크포인트 관리
    
    async def _save_checkpoint(self, stage: PipelineStage):
        """체크포인트 저장"""
        if not self.config.enable_caching:
            return
        
        stage_result = self.stage_results.get(stage)
        if not stage_result or stage_result.status != StageStatus.COMPLETED:
            return
        
        checkpoint_data = CheckpointData(
            stage=stage,
            timestamp=datetime.now(),
            data=stage_result.data,
            metadata={
                "duration": stage_result.duration.total_seconds() if stage_result.duration else 0,
                "metrics": stage_result.metrics
            }
        )
        
        checkpoint_file = self.checkpoint_dir / f"{stage.value}_checkpoint.json"
        
        try:
            with open(checkpoint_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "stage": checkpoint_data.stage.value,
                    "timestamp": checkpoint_data.timestamp.isoformat(),
                    "data": checkpoint_data.data,
                    "metadata": checkpoint_data.metadata
                }, f, indent=2, ensure_ascii=False, default=str)
            
            self.logger.debug(f"체크포인트 저장: {stage.value}")
            
        except Exception as e:
            self.logger.warning(f"체크포인트 저장 실패: {stage.value}, 오류: {str(e)}")
    
    async def _restore_from_checkpoint(self):
        """체크포인트에서 복원"""
        if not self.config.enable_caching:
            return
        
        for stage in PipelineStage:
            checkpoint_file = self.checkpoint_dir / f"{stage.value}_checkpoint.json"
            
            if not checkpoint_file.exists():
                continue
            
            try:
                with open(checkpoint_file, 'r', encoding='utf-8') as f:
                    checkpoint_data = json.load(f)
                
                # 단계 결과 복원
                stage_result = StageResult(
                    stage=stage,
                    status=StageStatus.COMPLETED,
                    start_time=datetime.fromisoformat(checkpoint_data["timestamp"]),
                    end_time=datetime.fromisoformat(checkpoint_data["timestamp"]),
                    data=checkpoint_data["data"],
                    metrics=checkpoint_data["metadata"].get("metrics", {})
                )
                
                self.stage_results[stage] = stage_result
                self.logger.info(f"체크포인트에서 복원: {stage.value}")
                
            except Exception as e:
                self.logger.warning(f"체크포인트 복원 실패: {stage.value}, 오류: {str(e)}")
    
    # 유틸리티 메서드
    
    async def _cleanup_memory(self):
        """메모리 정리"""
        self.memory_manager.cleanup_cache()
        
        # 가비지 컬렉션 강제 실행
        import gc
        gc.collect()
    
    async def _generate_pipeline_result(self) -> Dict[str, Any]:
        """파이프라인 실행 결과 생성"""
        total_duration = (self.pipeline_end_time - self.pipeline_start_time).total_seconds()
        
        return {
            "pipeline": {
                "start_time": self.pipeline_start_time.isoformat(),
                "end_time": self.pipeline_end_time.isoformat(),
                "duration_seconds": total_duration,
                "status": "completed"
            },
            "stages": {
                stage.value: {
                    "status": result.status.value,
                    "duration_seconds": result.duration.total_seconds() if result.duration else 0,
                    "error": result.error,
                    "metrics": result.metrics
                }
                for stage, result in self.stage_results.items()
            },
            "statistics": {
                "stages_completed": len([r for r in self.stage_results.values() 
                                       if r.status == StageStatus.COMPLETED]),
                "stages_failed": len([r for r in self.stage_results.values() 
                                    if r.status == StageStatus.FAILED]),
                "memory_peak_usage_gb": self.memory_manager.get_peak_usage(),
                "performance_metrics": self.progress_tracker.get_overall_metrics()
            },
            "outputs": {
                "output_directory": self.config.output_directory,
                "checkpoint_directory": str(self.checkpoint_dir)
            }
        }
    
    def get_stage_status(self, stage: PipelineStage) -> Optional[StageStatus]:
        """단계 상태 조회"""
        result = self.stage_results.get(stage)
        return result.status if result else None
    
    def get_stage_result(self, stage: PipelineStage) -> Optional[StageResult]:
        """단계 결과 조회"""
        return self.stage_results.get(stage)
    
    def get_pipeline_progress(self) -> Dict[str, Any]:
        """파이프라인 진행률 조회"""
        total_stages = len(PipelineStage)
        completed_stages = len([r for r in self.stage_results.values() 
                              if r.status == StageStatus.COMPLETED])
        
        return {
            "total_stages": total_stages,
            "completed_stages": completed_stages,
            "progress_percentage": (completed_stages / total_stages) * 100,
            "current_stage": self.current_stage.value if self.current_stage else None,
            "stage_details": {
                stage.value: result.status.value
                for stage, result in self.stage_results.items()
            }
        }


def create_pipeline_orchestrator(config: PipelineConfig) -> PipelineOrchestrator:
    """파이프라인 오케스트레이터 팩토리 함수"""
    return PipelineOrchestrator(config)