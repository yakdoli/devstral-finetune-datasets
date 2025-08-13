"""
진행률 추적기 테스트
"""

import asyncio
import pytest
import time
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any

from async_pipeline import ProgressTracker, ProgressTrackerConfig, PerformanceMetrics


class TestProgressTrackerConfig:
    """ProgressTrackerConfig 테스트"""
    
    def test_default_config(self):
        """기본 설정 테스트"""
        config = ProgressTrackerConfig()
        
        assert config.enable_progress_bar is True
        assert config.enable_metrics_collection is True
        assert config.update_interval == 0.5
        assert config.metrics_update_interval == 1.0
        assert config.eta_smoothing_window == 50
        assert config.enable_milestone_alerts is True
        assert config.milestone_percentages == [25, 50, 75, 90]
    
    def test_config_validation_success(self):
        """설정 유효성 검증 성공 테스트"""
        config = ProgressTrackerConfig(
            update_interval=1.0,
            metrics_history_size=500,
            eta_smoothing_window=30
        )
        
        # 예외가 발생하지 않아야 함
        config.validate()
    
    def test_config_validation_update_interval_error(self):
        """업데이트 간격 유효성 검증 실패 테스트"""
        config = ProgressTrackerConfig(update_interval=0.0)
        
        with pytest.raises(ValueError, match="업데이트 간격은"):
            config.validate()
    
    def test_config_validation_history_size_error(self):
        """히스토리 크기 유효성 검증 실패 테스트"""
        config = ProgressTrackerConfig(metrics_history_size=0)
        
        with pytest.raises(ValueError, match="메트릭 히스토리 크기는"):
            config.validate()
    
    def test_config_validation_smoothing_window_error(self):
        """스무딩 윈도우 유효성 검증 실패 테스트"""
        config = ProgressTrackerConfig(eta_smoothing_window=0)
        
        with pytest.raises(ValueError, match="ETA 스무딩 윈도우는"):
            config.validate()


class TestProgressTracker:
    """ProgressTracker 테스트"""
    
    @pytest.fixture
    def config(self):
        """테스트용 설정"""
        return ProgressTrackerConfig(
            enable_progress_bar=False,  # 테스트에서는 진행률 바 비활성화
            update_interval=0.1,
            metrics_update_interval=0.1,
            performance_log_interval=0.2,
            eta_smoothing_window=5,
            milestone_percentages=[25, 50, 75]
        )
    
    @pytest.fixture
    def tracker(self, config):
        """테스트용 진행률 추적기"""
        return ProgressTracker(config)
    
    def test_tracker_initialization(self, tracker):
        """추적기 초기화 테스트"""
        assert tracker.config.update_interval == 0.1
        assert not tracker._running
        assert tracker._total_items == 0
        assert tracker._processed_items == 0
        assert tracker._current_stage == "초기화"
    
    @pytest.mark.asyncio
    async def test_start_stop_tracker(self, tracker):
        """추적기 시작/중지 테스트"""
        # 시작
        await tracker.start(100, "테스트 처리")
        assert tracker._running is True
        assert tracker._total_items == 100
        assert tracker._start_time is not None
        
        # 중지
        await tracker.stop()
        assert tracker._running is False
        assert tracker._end_time is not None
    
    @pytest.mark.asyncio
    async def test_progress_update(self, tracker):
        """진행률 업데이트 테스트"""
        await tracker.start(100, "테스트")
        
        try:
            # 진행률 업데이트
            tracker.update_progress(processed_count=10, failed_count=2, processing_time=0.5)
            
            assert tracker._processed_items == 10
            assert tracker._failed_items == 2
            assert len(tracker._processing_times) == 1
            assert tracker._processing_times[0] == 0.5
            
            # 추가 업데이트
            tracker.update_progress(processed_count=5, processing_time=0.3)
            
            assert tracker._processed_items == 15
            assert tracker._failed_items == 2
            assert len(tracker._processing_times) == 2
            
        finally:
            await tracker.stop()
    
    def test_stage_setting(self, tracker):
        """단계 설정 테스트"""
        # 단계 콜백 등록
        callback_called = False
        callback_stage = None
        
        def stage_callback(stage, metrics):
            nonlocal callback_called, callback_stage
            callback_called = True
            callback_stage = stage
        
        tracker.register_stage_callback("데이터 로딩", stage_callback)
        
        # 단계 설정
        tracker.set_stage("데이터 로딩")
        
        assert tracker._current_stage == "데이터 로딩"
        assert callback_called is True
        assert callback_stage == "데이터 로딩"
    
    @pytest.mark.asyncio
    async def test_metrics_collection(self, tracker):
        """메트릭 수집 테스트"""
        await tracker.start(100, "테스트")
        
        try:
            # 진행률 업데이트
            tracker.update_progress(processed_count=20, processing_time=0.1)
            
            # 메트릭 가져오기
            metrics = tracker.get_current_metrics()
            
            assert isinstance(metrics, PerformanceMetrics)
            assert metrics.total_items == 100
            assert metrics.processed_items == 20
            assert metrics.items_per_second > 0
            assert metrics.success_rate > 0
            
            # 잠시 대기하여 메트릭 수집
            await asyncio.sleep(0.2)
            
            # 히스토리 확인
            history = tracker.get_metrics_history()
            assert len(history) > 0
            
        finally:
            await tracker.stop()
    
    @pytest.mark.asyncio
    async def test_milestone_alerts(self, tracker):
        """마일스톤 알림 테스트"""
        milestone_alerts = []
        
        def milestone_callback(percentage, metrics):
            milestone_alerts.append(percentage)
        
        # 마일스톤 콜백 등록
        tracker.register_milestone_callback(25, milestone_callback)
        tracker.register_milestone_callback(50, milestone_callback)
        
        await tracker.start(100, "테스트")
        
        try:
            # 25% 달성
            tracker.update_progress(processed_count=25)
            assert 25 in milestone_alerts
            
            # 50% 달성
            tracker.update_progress(processed_count=25)
            assert 50 in milestone_alerts
            
            # 마일스톤이 중복으로 발생하지 않는지 확인
            tracker.update_progress(processed_count=5)
            assert milestone_alerts.count(25) == 1
            assert milestone_alerts.count(50) == 1
            
        finally:
            await tracker.stop()
    
    def test_eta_calculation(self, tracker):
        """ETA 계산 테스트"""
        # 처리 시간 데이터 추가
        for i in range(10):
            tracker._processing_times.append(0.1)  # 각 항목당 0.1초
        
        tracker._total_items = 100
        tracker._processed_items = 20
        tracker._start_time = time.time() - 2.0  # 2초 전에 시작
        
        metrics = tracker.get_current_metrics()
        
        # ETA가 계산되었는지 확인
        assert metrics.estimated_time_remaining > 0
        assert metrics.items_per_second > 0
        assert metrics.average_processing_time == 0.1
    
    def test_progress_report_generation(self, tracker):
        """진행률 리포트 생성 테스트"""
        tracker._total_items = 100
        tracker._processed_items = 30
        tracker._failed_items = 5
        tracker._start_time = time.time() - 10.0
        tracker._current_stage = "데이터 처리"
        
        report = tracker.generate_progress_report()
        
        assert isinstance(report, dict)
        assert "progress" in report
        assert "performance" in report
        assert "system" in report
        
        # 진행률 정보 확인
        progress = report["progress"]
        assert progress["total_items"] == 100
        assert progress["processed_items"] == 30
        assert progress["failed_items"] == 5
        assert progress["completion_percentage"] == 30.0
        assert progress["current_stage"] == "데이터 처리"
        
        # 성능 정보 확인
        performance = report["performance"]
        assert "elapsed_time_seconds" in performance
        assert "items_per_second" in performance
        assert "success_rate" in performance
    
    def test_final_report_generation(self, tracker):
        """최종 리포트 생성 테스트"""
        tracker._total_items = 100
        tracker._processed_items = 95
        tracker._failed_items = 5
        tracker._start_time = time.time() - 60.0
        tracker._end_time = time.time()
        tracker._milestone_alerts_sent = {25, 50, 75}
        
        # 처리 시간 데이터 추가
        for i in range(10):
            tracker._processing_times.append(0.2)
        
        report = tracker.generate_final_report()
        
        assert isinstance(report, dict)
        assert "summary" in report
        assert "timing" in report
        assert "metrics_collected" in report
        assert "milestones_reached" in report
        
        # 요약 정보 확인
        summary = report["summary"]
        assert summary["total_items"] == 100
        assert summary["processed_items"] == 95
        assert summary["failed_items"] == 5
        assert summary["success_rate"] == 95.0
        
        # 타이밍 정보 확인
        timing = report["timing"]
        assert timing["average_processing_time"] == 0.2
        assert timing["total_duration"] > 0
        
        # 마일스톤 확인
        assert report["milestones_reached"] == [25, 50, 75]
    
    def test_eta_formatting(self, tracker):
        """ETA 포맷팅 테스트"""
        # ETA가 0인 경우
        tracker._total_items = 100
        tracker._processed_items = 100
        eta_str = tracker.get_eta_formatted()
        assert eta_str == "계산 중..."
        
        # 정상적인 ETA 계산
        tracker._processed_items = 50
        tracker._start_time = time.time() - 10.0
        
        # 처리 시간 데이터 추가
        for i in range(10):
            tracker._processing_times.append(0.2)
        
        eta_str = tracker.get_eta_formatted()
        assert "초" in eta_str or "분" in eta_str or "시간" in eta_str
    
    def test_throughput_stats(self, tracker):
        """처리량 통계 테스트"""
        # 메트릭 히스토리에 데이터 추가
        for i in range(5):
            metrics = PerformanceMetrics(
                timestamp=time.time(),
                items_per_second=10.0 + i * 2.0  # 10, 12, 14, 16, 18
            )
            tracker._metrics_history.append(metrics)
        
        stats = tracker.get_throughput_stats()
        
        assert isinstance(stats, dict)
        assert "current" in stats
        assert "average" in stats
        assert "peak" in stats
        assert "min" in stats
        
        assert stats["current"] == 18.0  # 마지막 값
        assert stats["peak"] == 18.0     # 최대값
        assert stats["min"] == 10.0      # 최소값
        assert stats["average"] == 14.0  # 평균값
    
    def test_completion_percentage_property(self, tracker):
        """완료 백분율 속성 테스트"""
        # 초기 상태
        assert tracker.completion_percentage == 0.0
        
        # 진행률 설정
        tracker._total_items = 200
        tracker._processed_items = 50
        
        assert tracker.completion_percentage == 25.0
        
        # 완료 상태
        tracker._processed_items = 200
        assert tracker.completion_percentage == 100.0
    
    def test_is_running_property(self, tracker):
        """실행 상태 속성 테스트"""
        assert tracker.is_running is False
        
        tracker._running = True
        assert tracker.is_running is True
        
        tracker._running = False
        assert tracker.is_running is False
    
    @pytest.mark.asyncio
    async def test_metrics_collection_loop(self, tracker):
        """메트릭 수집 루프 테스트"""
        await tracker.start(100, "테스트")
        
        try:
            # 진행률 업데이트
            tracker.update_progress(processed_count=10)
            
            # 메트릭 수집을 위해 잠시 대기
            await asyncio.sleep(0.3)
            
            # 메트릭이 수집되었는지 확인
            history = tracker.get_metrics_history()
            assert len(history) > 0
            
        finally:
            await tracker.stop()
    
    def test_no_start_time_final_report(self, tracker):
        """시작 시간이 없는 경우 최종 리포트 테스트"""
        report = tracker.generate_final_report()
        
        assert "error" in report
        assert report["error"] == "추적이 시작되지 않았습니다"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])