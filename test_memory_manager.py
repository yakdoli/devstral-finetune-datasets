"""
메모리 관리자 테스트
"""

import asyncio
import pytest
import time
import gc
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any

from async_pipeline import MemoryManager, MemoryManagerConfig, ResourceMetrics


class TestMemoryManagerConfig:
    """MemoryManagerConfig 테스트"""
    
    def test_default_config(self):
        """기본 설정 테스트"""
        config = MemoryManagerConfig()
        
        assert config.memory_warning_threshold == 80.0
        assert config.memory_critical_threshold == 90.0
        assert config.memory_emergency_threshold == 95.0
        assert config.enable_dynamic_batch_sizing is True
        assert config.enable_cache_management is True
        assert config.enable_aggressive_gc is True
    
    def test_config_validation_success(self):
        """설정 유효성 검증 성공 테스트"""
        config = MemoryManagerConfig(
            memory_warning_threshold=70.0,
            memory_critical_threshold=85.0,
            memory_emergency_threshold=95.0,
            min_batch_size=4,
            max_batch_size=64
        )
        
        # 예외가 발생하지 않아야 함
        config.validate()
    
    def test_config_validation_threshold_error(self):
        """임계값 유효성 검증 실패 테스트"""
        config = MemoryManagerConfig(
            memory_warning_threshold=90.0,  # critical보다 높음
            memory_critical_threshold=80.0
        )
        
        with pytest.raises(ValueError, match="메모리 임계값은"):
            config.validate()
    
    def test_config_validation_batch_size_error(self):
        """배치 크기 유효성 검증 실패 테스트"""
        config = MemoryManagerConfig(
            min_batch_size=64,
            max_batch_size=32  # min보다 작음
        )
        
        with pytest.raises(ValueError, match="최소 배치 크기는"):
            config.validate()
    
    def test_config_validation_adjustment_factor_error(self):
        """조정 비율 유효성 검증 실패 테스트"""
        config = MemoryManagerConfig(batch_size_adjustment_factor=1.5)
        
        with pytest.raises(ValueError, match="배치 크기 조정 비율은"):
            config.validate()


class TestMemoryManager:
    """MemoryManager 테스트"""
    
    @pytest.fixture
    def config(self):
        """테스트용 설정"""
        return MemoryManagerConfig(
            memory_warning_threshold=70.0,
            memory_critical_threshold=80.0,
            memory_emergency_threshold=90.0,
            monitoring_interval=0.1,
            gc_interval=0.2,
            alert_cooldown=0.1,
            min_batch_size=4,
            max_batch_size=64
        )
    
    @pytest.fixture
    def manager(self, config):
        """테스트용 메모리 관리자"""
        return MemoryManager(config)
    
    def test_manager_initialization(self, manager):
        """관리자 초기화 테스트"""
        assert manager.config.memory_warning_threshold == 70.0
        assert not manager._running
        assert len(manager._cache_registry) == 0
        assert manager._current_batch_size == 32
    
    @pytest.mark.asyncio
    async def test_start_stop_manager(self, manager):
        """관리자 시작/중지 테스트"""
        # 시작
        await manager.start()
        assert manager._running is True
        assert manager._monitor_task is not None
        assert manager._gc_task is not None
        
        # 중지
        await manager.stop()
        assert manager._running is False
    
    @patch('psutil.virtual_memory')
    @patch('psutil.cpu_percent')
    @patch('psutil.disk_usage')
    @patch('psutil.Process')
    def test_get_current_metrics(self, mock_process, mock_disk, mock_cpu, mock_memory, manager):
        """현재 메트릭 가져오기 테스트"""
        # Mock 설정
        mock_memory.return_value.used = 8 * 1024 * 1024 * 1024  # 8GB
        mock_memory.return_value.percent = 75.0
        mock_memory.return_value.available = 2 * 1024 * 1024 * 1024  # 2GB
        mock_cpu.return_value = 50.0
        mock_disk.return_value.percent = 60.0
        
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value.rss = 512 * 1024 * 1024  # 512MB
        mock_process_instance.cpu_percent.return_value = 25.0
        mock_process_instance.open_files.return_value = []
        mock_process.return_value = mock_process_instance
        
        # 메트릭 가져오기
        metrics = manager.get_current_metrics()
        
        assert isinstance(metrics, ResourceMetrics)
        assert metrics.memory_usage_mb == 8192.0
        assert metrics.memory_percent == 75.0
        assert metrics.cpu_percent == 50.0
        assert metrics.process_memory_mb == 512.0
    
    def test_cache_registration(self, manager):
        """캐시 등록 테스트"""
        cache_obj = {}
        
        # 캐시 등록
        manager.register_cache('test_cache', cache_obj, 100.0)
        
        assert 'test_cache' in manager._cache_registry
        assert manager._cache_registry['test_cache'] is cache_obj
        assert manager._cache_sizes['test_cache'] == 100.0
        
        # 캐시 등록 해제
        manager.unregister_cache('test_cache')
        
        assert 'test_cache' not in manager._cache_registry
        assert 'test_cache' not in manager._cache_sizes
    
    def test_cache_cleanup(self, manager):
        """캐시 정리 테스트"""
        # 테스트 캐시 생성
        cache1 = {'data': 'test1'}
        cache2 = {'data': 'test2'}
        
        manager.register_cache('cache1', cache1, 50.0)
        manager.register_cache('cache2', cache2, 75.0)
        
        # 캐시 정리
        manager.cleanup_caches(force=True)
        
        # 캐시가 비워졌는지 확인
        assert len(cache1) == 0
        assert len(cache2) == 0
    
    @patch('psutil.virtual_memory')
    @patch('psutil.cpu_percent')
    @patch('psutil.disk_usage')
    @patch('psutil.Process')
    def test_optimal_batch_size_calculation(self, mock_process, mock_disk, mock_cpu, mock_memory, manager):
        """최적 배치 크기 계산 테스트"""
        # Mock 프로세스 설정
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value.rss = 512 * 1024 * 1024
        mock_process_instance.cpu_percent.return_value = 25.0
        mock_process_instance.open_files.return_value = []
        mock_process.return_value = mock_process_instance
        
        mock_cpu.return_value = 50.0
        mock_disk.return_value.percent = 60.0
        mock_memory.return_value.used = 4 * 1024 * 1024 * 1024
        mock_memory.return_value.available = 4 * 1024 * 1024 * 1024
        
        current_batch_size = 32
        
        # 메모리 여유 상황 (40%)
        mock_memory.return_value.percent = 40.0
        new_size = manager.get_optimal_batch_size(current_batch_size)
        assert new_size >= current_batch_size  # 배치 크기 증가 또는 유지
        
        # 메모리 경고 상황 (75%)
        mock_memory.return_value.percent = 75.0
        new_size = manager.get_optimal_batch_size(current_batch_size)
        assert new_size <= current_batch_size  # 배치 크기 감소 또는 유지
        
        # 메모리 위험 상황 (85%)
        mock_memory.return_value.percent = 85.0
        new_size = manager.get_optimal_batch_size(current_batch_size)
        assert new_size <= current_batch_size * 0.8  # 배치 크기 감소
    
    def test_optimal_batch_size_disabled(self, manager):
        """동적 배치 크기 조정 비활성화 테스트"""
        manager.config.enable_dynamic_batch_sizing = False
        current_batch_size = 32
        
        new_size = manager.get_optimal_batch_size(current_batch_size)
        assert new_size == current_batch_size  # 변경되지 않음
    
    def test_force_garbage_collection(self, manager):
        """강제 가비지 컬렉션 테스트"""
        # 가비지 생성
        garbage = []
        for i in range(1000):
            garbage.append([i] * 100)
        
        # 참조 제거
        del garbage
        
        # 가비지 컬렉션 실행
        result = manager.force_garbage_collection()
        
        assert isinstance(result, dict)
        assert 'generation_0' in result
        assert 'objects_before' in result
        assert 'objects_after' in result
    
    def test_alert_callback_registration(self, manager):
        """알림 콜백 등록 테스트"""
        callback_called = False
        
        def test_callback(metrics):
            nonlocal callback_called
            callback_called = True
        
        manager.register_alert_callback('memory_warning', test_callback)
        
        assert 'memory_warning' in manager._alert_callbacks
        assert manager._alert_callbacks['memory_warning'] is test_callback
    
    @pytest.mark.asyncio
    @patch('psutil.virtual_memory')
    @patch('psutil.cpu_percent')
    @patch('psutil.disk_usage')
    @patch('psutil.Process')
    async def test_alert_system(self, mock_process, mock_disk, mock_cpu, mock_memory, manager):
        """알림 시스템 테스트"""
        # Mock 설정 - 높은 메모리 사용률
        mock_memory.return_value.used = 8 * 1024 * 1024 * 1024
        mock_memory.return_value.percent = 85.0  # 위험 수준
        mock_memory.return_value.available = 1 * 1024 * 1024 * 1024
        mock_cpu.return_value = 50.0
        mock_disk.return_value.percent = 60.0
        
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value.rss = 512 * 1024 * 1024
        mock_process_instance.cpu_percent.return_value = 25.0
        mock_process_instance.open_files.return_value = []
        mock_process.return_value = mock_process_instance
        
        # 알림 콜백 등록
        alert_received = []
        
        def alert_callback(metrics):
            alert_received.append('memory_critical')
        
        manager.register_alert_callback('memory_critical', alert_callback)
        
        # 알림 확인
        metrics = manager.get_current_metrics()
        await manager._check_alerts(metrics)
        
        # 알림이 발생했는지 확인
        assert len(alert_received) > 0
        assert 'memory_critical' in alert_received
    
    @pytest.mark.asyncio
    async def test_monitoring_loop(self, manager):
        """모니터링 루프 테스트"""
        await manager.start()
        
        # 잠시 실행
        await asyncio.sleep(0.3)
        
        await manager.stop()
        
        # 메트릭이 수집되었는지 확인
        history = manager.get_metrics_history()
        assert len(history) > 0
    
    def test_memory_summary(self, manager):
        """메모리 사용 요약 테스트"""
        # 테스트 캐시 등록
        manager.register_cache('test_cache', {}, 100.0)
        
        summary = manager.get_memory_summary()
        
        assert isinstance(summary, dict)
        assert 'system_memory' in summary
        assert 'process_memory' in summary
        assert 'cache_info' in summary
        assert 'batch_sizing' in summary
        assert 'gc_info' in summary
        
        # 캐시 정보 확인
        assert summary['cache_info']['registered_caches'] == 1
        assert summary['cache_info']['total_cache_size_mb'] == 100.0
    
    @pytest.mark.asyncio
    async def test_metrics_history_limit(self, manager):
        """메트릭 히스토리 제한 테스트"""
        # 새로운 관리자를 작은 히스토리 크기로 생성
        small_config = MemoryManagerConfig(metrics_history_size=3)
        small_manager = MemoryManager(small_config)
        
        # 메트릭을 여러 번 추가
        for i in range(5):
            metrics = small_manager.get_current_metrics()
            small_manager._metrics_history.append(metrics)
        
        # 최대 크기만큼만 유지되는지 확인
        history = small_manager.get_metrics_history()
        assert len(history) <= 3
    
    @pytest.mark.asyncio
    async def test_alert_cooldown(self, manager):
        """알림 쿨다운 테스트"""
        manager.config.alert_cooldown = 1.0  # 1초 쿨다운
        
        alert_count = 0
        
        def alert_callback(metrics):
            nonlocal alert_count
            alert_count += 1
        
        manager.register_alert_callback('memory_warning', alert_callback)
        
        # 높은 메모리 사용률로 메트릭 생성
        with patch('psutil.virtual_memory') as mock_memory:
            mock_memory.return_value.percent = 75.0
            
            metrics = manager.get_current_metrics()
            
            # 연속으로 알림 확인
            await manager._check_alerts(metrics)
            await manager._check_alerts(metrics)
            await manager._check_alerts(metrics)
            
            # 쿨다운으로 인해 한 번만 호출되어야 함
            assert alert_count <= 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])