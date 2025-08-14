"""
파이프라인 오케스트레이터 단위 테스트

파이프라인 조정, 데이터 흐름, 단계별 실행, 체크포인트 기능을 테스트합니다.
"""

import asyncio
import json
import pytest
import tempfile
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch, MagicMock

from async_pipeline.orchestrator import (
    PipelineOrchestrator, 
    PipelineStage, 
    StageStatus, 
    StageResult,
    CheckpointData,
    create_pipeline_orchestrator
)
from config.config import PipelineConfig


class TestPipelineOrchestrator:
    """파이프라인 오케스트레이터 테스트"""
    
    @pytest.fixture
    def temp_dir(self):
        """임시 디렉토리 픽스처"""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def config(self, temp_dir):
        """테스트 설정 픽스처"""
        return PipelineConfig(
            output_directory=str(Path(temp_dir) / "output"),
            temp_directory=str(Path(temp_dir) / "temp"),
            cache_directory=str(Path(temp_dir) / "cache"),
            enable_caching=True,
            max_memory_usage_gb=2.0
        )
    
    @pytest.fixture
    def orchestrator(self, config):
        """오케스트레이터 픽스처"""
        return PipelineOrchestrator(config)
    
    def test_orchestrator_initialization(self, orchestrator, config):
        """오케스트레이터 초기화 테스트"""
        assert orchestrator.config == config
        assert orchestrator.stage_results == {}
        assert orchestrator.current_stage is None
        assert orchestrator.pipeline_start_time is None
        assert orchestrator.checkpoint_dir.exists()
    
    def test_factory_function(self, config):
        """팩토리 함수 테스트"""
        orchestrator = create_pipeline_orchestrator(config)
        assert isinstance(orchestrator, PipelineOrchestrator)
        assert orchestrator.config == config
    
    @pytest.mark.asyncio
    async def test_stage_dependencies(self, orchestrator):
        """단계 의존성 확인 테스트"""
        # 의존성이 없는 단계
        assert await orchestrator._check_dependencies(PipelineStage.INITIALIZATION)
        
        # 의존성이 있는 단계 (의존성 미충족)
        assert not await orchestrator._check_dependencies(PipelineStage.MD_PROCESSING)
        
        # 의존성 충족
        orchestrator.stage_results[PipelineStage.INITIALIZATION] = StageResult(
            stage=PipelineStage.INITIALIZATION,
            status=StageStatus.COMPLETED,
            start_time=datetime.now()
        )
        assert await orchestrator._check_dependencies(PipelineStage.MD_PROCESSING)
    
    @pytest.mark.asyncio
    async def test_should_skip_stage(self, orchestrator):
        """단계 건너뛰기 로직 테스트"""
        stage = PipelineStage.MD_PROCESSING
        
        # 기본적으로 건너뛰지 않음
        assert not await orchestrator._should_skip_stage(stage)
        
        # 이미 완료된 단계는 건너뛰기
        orchestrator.stage_results[stage] = StageResult(
            stage=stage,
            status=StageStatus.COMPLETED,
            start_time=datetime.now()
        )
        assert await orchestrator._should_skip_stage(stage)
    
    @pytest.mark.asyncio
    async def test_initialization_stage(self, orchestrator):
        """초기화 단계 테스트"""
        result = await orchestrator._handle_initialization()
        
        assert "output_directory" in result
        assert "temp_directory" in result
        assert "cache_directory" in result
        assert "memory_limit_gb" in result
        
        # 디렉토리가 실제로 생성되었는지 확인
        assert Path(orchestrator.config.output_directory).exists()
        assert Path(orchestrator.config.temp_directory).exists()
        assert Path(orchestrator.config.cache_directory).exists()
    
    @pytest.mark.asyncio
    @patch('async_pipeline.orchestrator.create_processor')
    @patch('async_pipeline.orchestrator.create_scanner')
    async def test_md_processing_stage(self, mock_scanner, mock_processor, orchestrator):
        """MD 처리 단계 테스트"""
        # Mock 설정
        mock_scanner_instance = Mock()
        mock_scanner_instance.scan_files.return_value = [
            {"path": "test1.md", "size": 1000},
            {"path": "test2.md", "size": 2000}
        ]
        mock_scanner.return_value = mock_scanner_instance
        
        mock_processor_instance = Mock()
        mock_processor_instance.process_documents.return_value = [
            {"id": "doc1", "content": "test content 1"},
            {"id": "doc2", "content": "test content 2"}
        ]
        mock_processor.return_value = mock_processor_instance
        
        # 테스트 실행
        result = await orchestrator._handle_md_processing()
        
        # 검증
        assert len(result) == 2
        assert result[0]["id"] == "doc1"
        assert result[1]["id"] == "doc2"
        mock_scanner.assert_called_once()
        mock_processor.assert_called_once()
    
    @pytest.mark.asyncio
    @patch('async_pipeline.orchestrator.create_integrated_processor')
    async def test_qdrant_search_stage(self, mock_processor, orchestrator):
        """Qdrant 검색 단계 테스트"""
        # Mock 설정
        mock_processor_instance = Mock()
        mock_processor_instance.process_local_documents.return_value = [
            {"id": "qdrant1", "content": "qdrant content 1"},
            {"id": "qdrant2", "content": "qdrant content 2"}
        ]
        mock_processor.return_value = mock_processor_instance
        
        # 테스트 실행
        result = await orchestrator._handle_qdrant_search()
        
        # 검증
        assert len(result) == 2
        assert result[0]["id"] == "qdrant1"
        mock_processor.assert_called_once()
    
    @pytest.mark.asyncio
    @patch('async_pipeline.orchestrator.create_openai_connector')
    async def test_conversation_generation_stage(self, mock_connector, orchestrator):
        """대화 생성 단계 테스트"""
        # 이전 단계 결과 설정
        orchestrator.stage_results[PipelineStage.MD_PROCESSING] = StageResult(
            stage=PipelineStage.MD_PROCESSING,
            status=StageStatus.COMPLETED,
            start_time=datetime.now(),
            data=[{"id": "doc1", "content": "test content"}]
        )
        
        # Mock 설정
        mock_conversation = Mock()
        mock_conversation.to_dict.return_value = {
            "id": "conv1",
            "conversations": [
                {"from": "human", "value": "질문"},
                {"from": "gpt", "value": "답변"}
            ]
        }
        
        mock_connector_instance = Mock()
        mock_connector_instance.client = AsyncMock()
        mock_connector_instance.client.__aenter__ = AsyncMock(return_value=mock_connector_instance.client)
        mock_connector_instance.client.__aexit__ = AsyncMock(return_value=None)
        mock_connector_instance.generate_conversations = AsyncMock(return_value=[mock_conversation])
        mock_connector.return_value = mock_connector_instance
        
        # 테스트 실행
        result = await orchestrator._handle_conversation_generation()
        
        # 검증
        assert len(result) == 1
        assert result[0]["id"] == "conv1"
        mock_connector.assert_called_once()
    
    @pytest.mark.asyncio
    @patch('async_pipeline.orchestrator.create_dataset_generator')
    async def test_dataset_transformation_stage(self, mock_generator, orchestrator):
        """데이터셋 변환 단계 테스트"""
        # 이전 단계 결과 설정
        orchestrator.stage_results[PipelineStage.CONVERSATION_GENERATION] = StageResult(
            stage=PipelineStage.CONVERSATION_GENERATION,
            status=StageStatus.COMPLETED,
            start_time=datetime.now(),
            data=[{"id": "conv1", "conversations": []}]
        )
        
        # Mock 설정
        mock_generator_instance = Mock()
        mock_generator_instance.generate_datasets.return_value = Mock()
        mock_generator_instance.save_datasets.return_value = {
            "sharegpt": "/path/to/sharegpt.jsonl",
            "alpaca": "/path/to/alpaca.jsonl"
        }
        mock_generator.return_value = mock_generator_instance
        
        # 테스트 실행
        result = await orchestrator._handle_dataset_transformation()
        
        # 검증
        assert "sharegpt" in result
        assert "alpaca" in result
        mock_generator.assert_called_once()
    
    @pytest.mark.asyncio
    @patch('async_pipeline.orchestrator.create_default_validator')
    async def test_quality_validation_stage(self, mock_validator, orchestrator, temp_dir):
        """품질 검증 단계 테스트"""
        # 테스트 데이터셋 파일 생성
        dataset_file = Path(temp_dir) / "test_dataset.jsonl"
        with open(dataset_file, 'w', encoding='utf-8') as f:
            f.write('{"conversations": [{"from": "human", "value": "test"}]}\n')
        
        # 이전 단계 결과 설정
        orchestrator.stage_results[PipelineStage.DATASET_TRANSFORMATION] = StageResult(
            stage=PipelineStage.DATASET_TRANSFORMATION,
            status=StageStatus.COMPLETED,
            start_time=datetime.now(),
            data={"sharegpt": str(dataset_file)}
        )
        
        # Mock 설정
        mock_validator_instance = Mock()
        mock_validator_instance.validate_and_filter.return_value = {
            "valid_count": 1,
            "invalid_count": 0,
            "quality_score": 0.8
        }
        mock_validator.return_value = mock_validator_instance
        
        # 테스트 실행
        result = await orchestrator._handle_quality_validation()
        
        # 검증
        assert "sharegpt" in result
        assert result["sharegpt"]["valid_count"] == 1
        mock_validator.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_finalization_stage(self, orchestrator):
        """마무리 단계 테스트"""
        # 파이프라인 시작 시간 설정
        orchestrator.pipeline_start_time = datetime.now() - timedelta(seconds=10)
        
        # 일부 단계 결과 설정
        orchestrator.stage_results[PipelineStage.INITIALIZATION] = StageResult(
            stage=PipelineStage.INITIALIZATION,
            status=StageStatus.COMPLETED,
            start_time=datetime.now()
        )
        
        # 테스트 실행
        result = await orchestrator._handle_finalization()
        
        # 검증
        assert "pipeline_duration" in result
        assert "stages_completed" in result
        assert "stages_failed" in result
        assert result["stages_completed"] == 1
        assert result["stages_failed"] == 0
        
        # 리포트 파일이 생성되었는지 확인
        report_path = Path(orchestrator.config.output_directory) / "pipeline_report.json"
        assert report_path.exists()
    
    @pytest.mark.asyncio
    async def test_checkpoint_save_and_restore(self, orchestrator, temp_dir):
        """체크포인트 저장 및 복원 테스트"""
        stage = PipelineStage.INITIALIZATION
        test_data = {"test": "data"}
        
        # 단계 결과 설정
        stage_result = StageResult(
            stage=stage,
            status=StageStatus.COMPLETED,
            start_time=datetime.now(),
            data=test_data
        )
        stage_result.complete(test_data, {"metric1": 100})
        orchestrator.stage_results[stage] = stage_result
        
        # 체크포인트 저장
        await orchestrator._save_checkpoint(stage)
        
        # 체크포인트 파일 확인
        checkpoint_file = orchestrator.checkpoint_dir / f"{stage.value}_checkpoint.json"
        assert checkpoint_file.exists()
        
        # 단계 결과 초기화
        orchestrator.stage_results.clear()
        
        # 체크포인트에서 복원
        await orchestrator._restore_from_checkpoint()
        
        # 복원 확인
        assert stage in orchestrator.stage_results
        restored_result = orchestrator.stage_results[stage]
        assert restored_result.status == StageStatus.COMPLETED
        assert restored_result.data == test_data
    
    @pytest.mark.asyncio
    async def test_execute_stage_success(self, orchestrator):
        """단계 실행 성공 테스트"""
        stage = PipelineStage.INITIALIZATION
        
        # 테스트 실행
        await orchestrator._execute_stage(stage)
        
        # 검증
        assert stage in orchestrator.stage_results
        result = orchestrator.stage_results[stage]
        assert result.status == StageStatus.COMPLETED
        assert result.data is not None
        assert result.duration is not None
    
    @pytest.mark.asyncio
    async def test_execute_stage_failure(self, orchestrator):
        """단계 실행 실패 테스트"""
        # 존재하지 않는 핸들러로 실패 유도
        stage = PipelineStage.MD_PROCESSING
        orchestrator.stage_handlers[stage] = AsyncMock(side_effect=Exception("Test error"))
        
        # 의존성 충족
        orchestrator.stage_results[PipelineStage.INITIALIZATION] = StageResult(
            stage=PipelineStage.INITIALIZATION,
            status=StageStatus.COMPLETED,
            start_time=datetime.now()
        )
        
        # 테스트 실행 및 예외 확인
        with pytest.raises(Exception, match="Test error"):
            await orchestrator._execute_stage(stage)
        
        # 실패 상태 확인
        assert stage in orchestrator.stage_results
        result = orchestrator.stage_results[stage]
        assert result.status == StageStatus.FAILED
        assert result.error == "Test error"
    
    @pytest.mark.asyncio
    @patch('async_pipeline.orchestrator.create_processor')
    @patch('async_pipeline.orchestrator.create_scanner')
    @patch('async_pipeline.orchestrator.create_integrated_processor')
    async def test_full_pipeline_execution(self, mock_qdrant, mock_scanner, mock_processor, orchestrator):
        """전체 파이프라인 실행 테스트"""
        # Mock 설정
        mock_scanner_instance = Mock()
        mock_scanner_instance.scan_files.return_value = [{"path": "test.md"}]
        mock_scanner.return_value = mock_scanner_instance
        
        mock_processor_instance = Mock()
        mock_processor_instance.process_documents.return_value = [{"id": "doc1"}]
        mock_processor.return_value = mock_processor_instance
        
        mock_qdrant_instance = Mock()
        mock_qdrant_instance.process_local_documents.return_value = []
        mock_qdrant.return_value = mock_qdrant_instance
        
        # 일부 단계만 실행
        stages = [
            PipelineStage.INITIALIZATION,
            PipelineStage.MD_PROCESSING,
            PipelineStage.QDRANT_SEARCH,
            PipelineStage.FINALIZATION
        ]
        
        # 테스트 실행
        result = await orchestrator.run_pipeline(stages=stages)
        
        # 검증
        assert "pipeline" in result
        assert "stages" in result
        assert "statistics" in result
        assert result["pipeline"]["status"] == "completed"
        assert result["statistics"]["stages_completed"] >= 3  # 최소 3개 단계 완료
    
    def test_get_stage_status(self, orchestrator):
        """단계 상태 조회 테스트"""
        stage = PipelineStage.INITIALIZATION
        
        # 결과가 없는 경우
        assert orchestrator.get_stage_status(stage) is None
        
        # 결과가 있는 경우
        orchestrator.stage_results[stage] = StageResult(
            stage=stage,
            status=StageStatus.COMPLETED,
            start_time=datetime.now()
        )
        assert orchestrator.get_stage_status(stage) == StageStatus.COMPLETED
    
    def test_get_pipeline_progress(self, orchestrator):
        """파이프라인 진행률 조회 테스트"""
        # 초기 상태
        progress = orchestrator.get_pipeline_progress()
        assert progress["completed_stages"] == 0
        assert progress["progress_percentage"] == 0.0
        
        # 일부 단계 완료
        orchestrator.stage_results[PipelineStage.INITIALIZATION] = StageResult(
            stage=PipelineStage.INITIALIZATION,
            status=StageStatus.COMPLETED,
            start_time=datetime.now()
        )
        
        progress = orchestrator.get_pipeline_progress()
        assert progress["completed_stages"] == 1
        assert progress["progress_percentage"] > 0
    
    @pytest.mark.asyncio
    async def test_memory_cleanup(self, orchestrator):
        """메모리 정리 테스트"""
        # 메모리 정리 실행 (예외가 발생하지 않아야 함)
        await orchestrator._cleanup_memory()
        
        # 메모리 사용량 확인
        usage = orchestrator.memory_manager.get_current_usage()
        assert isinstance(usage, (int, float))


class TestStageResult:
    """StageResult 클래스 테스트"""
    
    def test_stage_result_initialization(self):
        """StageResult 초기화 테스트"""
        start_time = datetime.now()
        result = StageResult(
            stage=PipelineStage.INITIALIZATION,
            status=StageStatus.PENDING,
            start_time=start_time
        )
        
        assert result.stage == PipelineStage.INITIALIZATION
        assert result.status == StageStatus.PENDING
        assert result.start_time == start_time
        assert result.end_time is None
        assert result.duration is None
        assert result.data is None
        assert result.error is None
        assert result.metrics == {}
    
    def test_stage_result_complete(self):
        """StageResult 완료 처리 테스트"""
        result = StageResult(
            stage=PipelineStage.INITIALIZATION,
            status=StageStatus.RUNNING,
            start_time=datetime.now()
        )
        
        test_data = {"test": "data"}
        test_metrics = {"metric1": 100}
        
        result.complete(data=test_data, metrics=test_metrics)
        
        assert result.status == StageStatus.COMPLETED
        assert result.data == test_data
        assert result.metrics == test_metrics
        assert result.end_time is not None
        assert result.duration is not None
        assert result.error is None
    
    def test_stage_result_fail(self):
        """StageResult 실패 처리 테스트"""
        result = StageResult(
            stage=PipelineStage.INITIALIZATION,
            status=StageStatus.RUNNING,
            start_time=datetime.now()
        )
        
        error_message = "Test error"
        result.fail(error_message)
        
        assert result.status == StageStatus.FAILED
        assert result.error == error_message
        assert result.end_time is not None
        assert result.duration is not None


class TestCheckpointData:
    """CheckpointData 클래스 테스트"""
    
    def test_checkpoint_data_initialization(self):
        """CheckpointData 초기화 테스트"""
        stage = PipelineStage.INITIALIZATION
        timestamp = datetime.now()
        data = {"test": "data"}
        metadata = {"version": "1.0"}
        
        checkpoint = CheckpointData(
            stage=stage,
            timestamp=timestamp,
            data=data,
            metadata=metadata
        )
        
        assert checkpoint.stage == stage
        assert checkpoint.timestamp == timestamp
        assert checkpoint.data == data
        assert checkpoint.metadata == metadata


if __name__ == "__main__":
    pytest.main([__file__, "-v"])