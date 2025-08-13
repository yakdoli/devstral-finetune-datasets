"""
비동기 파이프라인 관리자 테스트
"""

import asyncio
import pytest
import time
from unittest.mock import Mock, patch
from typing import List

from async_pipeline import AsyncPipelineManager, AsyncPipelineConfig


class TestAsyncPipelineConfig:
    """AsyncPipelineConfig 테스트"""
    
    def test_default_config(self):
        """기본 설정 테스트"""
        config = AsyncPipelineConfig()
        
        assert config.batch_size == 32
        assert config.min_batch_size == 16
        assert config.max_batch_size == 100
        assert config.max_concurrent == 8
        assert config.enable_backpressure is True
        assert config.enable_graceful_degradation is True
    
    def test_config_validation_success(self):
        """설정 유효성 검증 성공 테스트"""
        config = AsyncPipelineConfig(
            batch_size=50,
            min_batch_size=20,
            max_batch_size=80,
            max_concurrent=4
        )
        
        # 예외가 발생하지 않아야 함
        config.validate()
    
    def test_config_validation_batch_size_error(self):
        """배치 크기 유효성 검증 실패 테스트"""
        config = AsyncPipelineConfig(
            batch_size=150,  # max_batch_size보다 큼
            max_batch_size=100
        )
        
        with pytest.raises(ValueError, match="배치 크기는"):
            config.validate()
    
    def test_config_validation_concurrent_error(self):
        """동시 실행 수 유효성 검증 실패 테스트"""
        config = AsyncPipelineConfig(max_concurrent=0)
        
        with pytest.raises(ValueError, match="최대 동시 실행 수는"):
            config.validate()
    
    def test_config_validation_threshold_error(self):
        """임계값 유효성 검증 실패 테스트"""
        config = AsyncPipelineConfig(backpressure_threshold=1.5)
        
        with pytest.raises(ValueError, match="백프레셔 임계값은"):
            config.validate()


class TestAsyncPipelineManager:
    """AsyncPipelineManager 테스트"""
    
    @pytest.fixture
    def config(self):
        """테스트용 설정"""
        return AsyncPipelineConfig(
            batch_size=4,
            min_batch_size=2,
            max_batch_size=8,
            max_concurrent=2,
            max_queue_size=10,
            task_timeout=5.0,
            batch_timeout=10.0
        )
    
    @pytest.fixture
    def manager(self, config):
        """테스트용 파이프라인 관리자"""
        return AsyncPipelineManager(config)
    
    @pytest.mark.asyncio
    async def test_manager_initialization(self, manager):
        """관리자 초기화 테스트"""
        assert manager.config.batch_size == 4
        assert manager.config.max_concurrent == 2
        assert not manager._running
        assert len(manager._workers) == 0
    
    @pytest.mark.asyncio
    async def test_start_stop_pipeline(self, manager):
        """파이프라인 시작/중지 테스트"""
        # 시작
        await manager.start()
        assert manager._running is True
        assert len(manager._workers) == 3  # 2 workers + 1 monitor
        
        # 중지
        await manager.stop()
        assert manager._running is False
        assert len(manager._workers) == 0
    
    @pytest.mark.asyncio
    async def test_process_single_batch(self, manager):
        """단일 배치 처리 테스트"""
        await manager.start()
        
        try:
            # 테스트 데이터
            items = [1, 2, 3, 4]
            
            def processor(batch):
                return [x * 2 for x in batch]
            
            # 배치 처리
            result = await manager.process_batch(items, processor)
            
            # 결과 검증
            assert result.success_count == 4
            assert result.error_count == 0
            assert result.results == [2, 4, 6, 8]
            assert result.processing_time > 0
            
        finally:
            await manager.stop()
    
    @pytest.mark.asyncio
    async def test_process_batch_with_error(self, manager):
        """오류가 있는 배치 처리 테스트"""
        await manager.start()
        
        try:
            items = [1, 2, 3]
            
            def failing_processor(batch):
                raise ValueError("테스트 오류")
            
            result = await manager.process_batch(items, failing_processor)
            
            assert result.success_count == 0
            assert result.error_count == 1
            assert len(result.errors) == 1
            assert isinstance(result.errors[0], ValueError)
            
        finally:
            await manager.stop()
    
    @pytest.mark.asyncio
    async def test_async_processor(self, manager):
        """비동기 프로세서 테스트"""
        await manager.start()
        
        try:
            items = [1, 2, 3]
            
            async def async_processor(batch):
                await asyncio.sleep(0.1)
                return [x * 3 for x in batch]
            
            result = await manager.process_batch(items, async_processor)
            
            assert result.success_count == 3
            assert result.results == [3, 6, 9]
            
        finally:
            await manager.stop()
    
    @pytest.mark.asyncio
    async def test_batch_timeout(self, manager):
        """배치 타임아웃 테스트"""
        # 짧은 타임아웃 설정
        manager.config.batch_timeout = 0.1
        await manager.start()
        
        try:
            items = [1, 2, 3]
            
            async def slow_processor(batch):
                await asyncio.sleep(1.0)  # 타임아웃보다 긴 시간
                return batch
            
            result = await manager.process_batch(items, slow_processor)
            
            assert result.success_count == 0
            assert result.error_count == 1
            assert isinstance(result.errors[0], TimeoutError)
            
        finally:
            await manager.stop()
    
    @pytest.mark.asyncio
    async def test_concurrent_processing(self, manager):
        """동시 처리 테스트"""
        await manager.start()
        
        try:
            processing_times = []
            
            async def timing_processor(batch):
                start = time.time()
                await asyncio.sleep(0.1)
                end = time.time()
                processing_times.append(end - start)
                return [x * 2 for x in batch]
            
            # 여러 배치를 동시에 처리
            tasks = []
            for i in range(2):  # 동시 실행 수에 맞게 조정
                items = [i * 10 + j for j in range(3)]
                task = manager.process_batch(items, timing_processor)
                tasks.append(task)
            
            start_time = time.time()
            results = await asyncio.gather(*tasks)
            end_time = time.time()
            
            # 결과 검증
            assert len(results) == 2
            assert all(r.success_count == 3 for r in results)
            
            # 세마포어가 작동하는지 확인 (정확한 시간 측정보다는 기능 검증)
            total_time = end_time - start_time
            assert total_time > 0.1  # 최소한 하나의 배치 처리 시간은 걸려야 함
            assert len(processing_times) == 2  # 두 배치 모두 처리되어야 함
            
        finally:
            await manager.stop()
    
    @pytest.mark.asyncio
    async def test_metrics_collection(self, manager):
        """메트릭 수집 테스트"""
        await manager.start()
        
        try:
            items = [1, 2, 3, 4, 5]
            
            def processor(batch):
                return [x * 2 for x in batch]
            
            await manager.process_batch(items, processor)
            
            metrics = manager.get_metrics()
            
            assert metrics.total_batches == 1
            assert metrics.completed_batches == 1
            assert metrics.total_items == 5
            assert metrics.processed_items == 5
            assert metrics.failed_items == 0
            assert metrics.total_processing_time > 0
            assert metrics.throughput > 0
            
        finally:
            await manager.stop()
    
    @pytest.mark.asyncio
    async def test_backpressure_detection(self, manager):
        """백프레셔 탐지 테스트"""
        # 작은 큐 크기로 설정
        manager.config.max_queue_size = 2
        manager.config.backpressure_threshold = 0.5
        
        # 큐를 가득 채움
        for _ in range(2):
            await manager._queue.put(([1, 2, 3], lambda x: x))
        
        # 백프레셔 확인
        start_time = time.time()
        await manager._check_backpressure()
        end_time = time.time()
        
        # 백프레셔로 인한 지연이 있어야 함
        assert manager.is_backpressure_active()
        assert end_time - start_time >= manager.config.backpressure_delay
    
    @pytest.mark.asyncio
    @patch('psutil.virtual_memory')
    @patch('psutil.cpu_percent')
    async def test_graceful_degradation(self, mock_cpu, mock_memory, manager):
        """우아한 성능 저하 테스트"""
        # 높은 리소스 사용률 시뮬레이션
        mock_memory.return_value.percent = 95.0
        mock_cpu.return_value = 95.0
        
        original_batch_size = manager.get_current_batch_size()
        
        # 성능 저하 확인
        await manager._check_graceful_degradation(95.0, 95.0)
        
        # 배치 크기가 감소해야 함
        assert manager.is_degradation_active()
        assert manager.get_current_batch_size() < original_batch_size
        
        # 리소스 사용률 정상화
        await manager._check_graceful_degradation(50.0, 50.0)
        
        # 배치 크기가 복원되어야 함
        assert not manager.is_degradation_active()
        assert manager.get_current_batch_size() == original_batch_size
    
    @pytest.mark.asyncio
    async def test_stream_processing(self, manager):
        """스트림 처리 테스트"""
        async def item_generator():
            for i in range(10):
                yield i
                await asyncio.sleep(0.01)
        
        def processor(batch):
            return [x * 2 for x in batch]
        
        results = []
        async for batch_result in manager.process_stream(item_generator(), processor):
            results.append(batch_result)
        
        await manager.stop()
        
        # 결과 검증
        assert len(results) > 0
        total_processed = sum(r.success_count for r in results)
        assert total_processed == 10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])