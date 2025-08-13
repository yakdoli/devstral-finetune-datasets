"""
메트릭 수집기 단위 테스트

처리 성능, 품질 메트릭, 리소스 사용량, API 메트릭 수집 기능을 테스트합니다.
"""

import time
import threading
from unittest.mock import patch, MagicMock
import pytest

from logging_system.metrics_collector import (
    MetricsCollector, ProcessingMetrics, QualityMetrics, 
    ResourceMetrics, APIMetrics
)


class TestProcessingMetrics:
    """ProcessingMetrics 테스트"""
    
    def test_processing_metrics_initialization(self):
        """ProcessingMetrics 초기화 테스트"""
        metrics = ProcessingMetrics()
        
        assert metrics.total_processed == 0
        assert metrics.success_count == 0
        assert metrics.error_count == 0
        assert metrics.total_duration == 0.0
        assert metrics.avg_processing_time == 0.0
        assert metrics.throughput_per_second == 0.0
        assert metrics.processing_times == []
    
    def test_processing_metrics_update_success(self):
        """성공적인 처리 메트릭 업데이트 테스트"""
        metrics = ProcessingMetrics()
        
        metrics.update(1.5, success=True)
        metrics.update(2.0, success=True)
        metrics.update(1.0, success=True)
        
        assert metrics.total_processed == 3
        assert metrics.success_count == 3
        assert metrics.error_count == 0
        assert metrics.total_duration == 4.5
        assert metrics.avg_processing_time == 1.5  # (1.5 + 2.0 + 1.0) / 3
        assert metrics.throughput_per_second == 3 / 4.5  # 약 0.67
    
    def test_processing_metrics_update_with_errors(self):
        """오류가 있는 처리 메트릭 업데이트 테스트"""
        metrics = ProcessingMetrics()
        
        metrics.update(1.0, success=True)
        metrics.update(2.0, success=False)
        metrics.update(1.5, success=True)
        
        assert metrics.total_processed == 3
        assert metrics.success_count == 2
        assert metrics.error_count == 1
        assert metrics.total_duration == 4.5
    
    def test_processing_metrics_time_list_limit(self):
        """처리 시간 리스트 크기 제한 테스트"""
        metrics = ProcessingMetrics()
        
        # 150개의 처리 시간 추가 (제한은 100개)
        for i in range(150):
            metrics.update(i * 0.1, success=True)
        
        assert len(metrics.processing_times) == 100
        assert metrics.processing_times[0] == 5.0  # 50번째부터 시작 (50 * 0.1)
        assert metrics.processing_times[-1] == 14.9  # 149번째 (149 * 0.1)


class TestQualityMetrics:
    """QualityMetrics 테스트"""
    
    def test_quality_metrics_initialization(self):
        """QualityMetrics 초기화 테스트"""
        metrics = QualityMetrics()
        
        assert metrics.total_items == 0
        assert metrics.high_quality_count == 0
        assert metrics.medium_quality_count == 0
        assert metrics.low_quality_count == 0
        assert metrics.avg_quality_score == 0.0
        assert metrics.duplicate_count == 0
        assert metrics.safety_violations == 0
    
    def test_quality_metrics_update_high_quality(self):
        """고품질 메트릭 업데이트 테스트"""
        metrics = QualityMetrics()
        
        metrics.update(0.9, is_duplicate=False, has_safety_violation=False)
        metrics.update(0.85, is_duplicate=False, has_safety_violation=False)
        
        assert metrics.total_items == 2
        assert metrics.high_quality_count == 2
        assert metrics.medium_quality_count == 0
        assert metrics.low_quality_count == 0
        assert metrics.avg_quality_score == 0.875  # (0.9 + 0.85) / 2
    
    def test_quality_metrics_update_medium_quality(self):
        """중품질 메트릭 업데이트 테스트"""
        metrics = QualityMetrics()
        
        metrics.update(0.7, is_duplicate=False, has_safety_violation=False)
        metrics.update(0.65, is_duplicate=False, has_safety_violation=False)
        
        assert metrics.total_items == 2
        assert metrics.high_quality_count == 0
        assert metrics.medium_quality_count == 2
        assert metrics.low_quality_count == 0
        assert metrics.avg_quality_score == 0.675
    
    def test_quality_metrics_update_low_quality(self):
        """저품질 메트릭 업데이트 테스트"""
        metrics = QualityMetrics()
        
        metrics.update(0.5, is_duplicate=False, has_safety_violation=False)
        metrics.update(0.3, is_duplicate=False, has_safety_violation=False)
        
        assert metrics.total_items == 2
        assert metrics.high_quality_count == 0
        assert metrics.medium_quality_count == 0
        assert metrics.low_quality_count == 2
        assert metrics.avg_quality_score == 0.4
    
    def test_quality_metrics_update_with_duplicates_and_violations(self):
        """중복 및 안전성 위반이 있는 메트릭 업데이트 테스트"""
        metrics = QualityMetrics()
        
        metrics.update(0.8, is_duplicate=True, has_safety_violation=False)
        metrics.update(0.7, is_duplicate=False, has_safety_violation=True)
        metrics.update(0.6, is_duplicate=True, has_safety_violation=True)
        
        assert metrics.total_items == 3
        assert metrics.duplicate_count == 2
        assert metrics.safety_violations == 2


class TestResourceMetrics:
    """ResourceMetrics 테스트"""
    
    @patch('psutil.cpu_percent')
    @patch('psutil.virtual_memory')
    @patch('psutil.Process')
    def test_resource_metrics_update(self, mock_process, mock_memory, mock_cpu):
        """리소스 메트릭 업데이트 테스트"""
        # Mock 설정
        mock_cpu.return_value = 45.5
        mock_memory.return_value = MagicMock(percent=60.2)
        
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value = MagicMock(rss=1024 * 1024 * 512)  # 512MB
        mock_process.return_value = mock_process_instance
        
        metrics = ResourceMetrics()
        metrics.update()
        
        assert metrics.cpu_usage_percent == 45.5
        assert metrics.memory_usage_percent == 60.2
        assert metrics.memory_usage_mb == 512.0
        assert metrics.peak_cpu_percent == 45.5
        assert metrics.peak_memory_mb == 512.0
    
    @patch('psutil.cpu_percent')
    @patch('psutil.virtual_memory')
    @patch('psutil.Process')
    def test_resource_metrics_peak_tracking(self, mock_process, mock_memory, mock_cpu):
        """리소스 메트릭 피크 추적 테스트"""
        mock_memory.return_value = MagicMock(percent=50.0)
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value = MagicMock(rss=1024 * 1024 * 256)  # 256MB
        mock_process.return_value = mock_process_instance
        
        metrics = ResourceMetrics()
        
        # 첫 번째 업데이트
        mock_cpu.return_value = 30.0
        metrics.update()
        assert metrics.peak_cpu_percent == 30.0
        assert metrics.peak_memory_mb == 256.0
        
        # 더 높은 값으로 두 번째 업데이트
        mock_cpu.return_value = 50.0
        mock_process_instance.memory_info.return_value = MagicMock(rss=1024 * 1024 * 512)  # 512MB
        metrics.update()
        assert metrics.peak_cpu_percent == 50.0
        assert metrics.peak_memory_mb == 512.0
        
        # 더 낮은 값으로 세 번째 업데이트 (피크는 유지되어야 함)
        mock_cpu.return_value = 25.0
        mock_process_instance.memory_info.return_value = MagicMock(rss=1024 * 1024 * 128)  # 128MB
        metrics.update()
        assert metrics.peak_cpu_percent == 50.0  # 피크 유지
        assert metrics.peak_memory_mb == 512.0   # 피크 유지


class TestAPIMetrics:
    """APIMetrics 테스트"""
    
    def test_api_metrics_initialization(self):
        """APIMetrics 초기화 테스트"""
        metrics = APIMetrics()
        
        assert metrics.total_calls == 0
        assert metrics.successful_calls == 0
        assert metrics.failed_calls == 0
        assert metrics.total_response_time == 0.0
        assert metrics.avg_response_time == 0.0
        assert len(metrics.status_codes) == 0
        assert len(metrics.error_types) == 0
    
    def test_api_metrics_successful_calls(self):
        """성공적인 API 호출 메트릭 테스트"""
        metrics = APIMetrics()
        
        metrics.update(0.5, status_code=200)
        metrics.update(0.8, status_code=201)
        metrics.update(0.3, status_code=204)
        
        assert metrics.total_calls == 3
        assert metrics.successful_calls == 3
        assert metrics.failed_calls == 0
        assert metrics.total_response_time == 1.6
        assert metrics.avg_response_time == 1.6 / 3
        assert metrics.status_codes[200] == 1
        assert metrics.status_codes[201] == 1
        assert metrics.status_codes[204] == 1
    
    def test_api_metrics_failed_calls(self):
        """실패한 API 호출 메트릭 테스트"""
        metrics = APIMetrics()
        
        metrics.update(1.0, status_code=400)
        metrics.update(1.5, status_code=500)
        metrics.update(0.8, error_type="ConnectionError")
        
        assert metrics.total_calls == 3
        assert metrics.successful_calls == 0
        assert metrics.failed_calls == 3
        assert metrics.status_codes[400] == 1
        assert metrics.status_codes[500] == 1
        assert metrics.error_types["ConnectionError"] == 1
    
    def test_api_metrics_response_time_limit(self):
        """응답 시간 리스트 크기 제한 테스트"""
        metrics = APIMetrics()
        
        # 150개의 응답 시간 추가 (제한은 100개)
        for i in range(150):
            metrics.update(i * 0.01, status_code=200)
        
        assert len(metrics.response_times) == 100
        assert metrics.response_times[0] == 0.5  # 50번째부터 시작
        assert metrics.response_times[-1] == 1.49  # 149번째


class TestMetricsCollector:
    """MetricsCollector 테스트"""
    
    def test_metrics_collector_initialization(self):
        """MetricsCollector 초기화 테스트"""
        collector = MetricsCollector(collection_interval=1.0)
        
        assert collector.collection_interval == 1.0
        assert isinstance(collector.processing_metrics, ProcessingMetrics)
        assert isinstance(collector.quality_metrics, QualityMetrics)
        assert isinstance(collector.resource_metrics, ResourceMetrics)
        assert isinstance(collector.api_metrics, APIMetrics)
        assert len(collector.resource_history) == 0
        assert len(collector.throughput_history) == 0
    
    def test_record_processing(self):
        """처리 메트릭 기록 테스트"""
        collector = MetricsCollector()
        
        collector.record_processing(1.5, success=True)
        collector.record_processing(2.0, success=False)
        
        metrics = collector.get_processing_metrics()
        assert metrics['total_processed'] == 2
        assert metrics['success_count'] == 1
        assert metrics['error_count'] == 1
        assert metrics['success_rate'] == 0.5
    
    def test_record_quality(self):
        """품질 메트릭 기록 테스트"""
        collector = MetricsCollector()
        
        collector.record_quality(0.9, is_duplicate=False, has_safety_violation=False)
        collector.record_quality(0.7, is_duplicate=True, has_safety_violation=False)
        collector.record_quality(0.5, is_duplicate=False, has_safety_violation=True)
        
        metrics = collector
.get_quality_metrics()
        assert metrics['total_items'] == 3
        assert metrics['high_quality_count'] == 1
        assert metrics['medium_quality_count'] == 1
        assert metrics['low_quality_count'] == 1
        assert metrics['duplicate_count'] == 1
        assert metrics['safety_violations'] == 1
    
    def test_record_api_call(self):
        """API 호출 메트릭 기록 테스트"""
        collector = MetricsCollector()
        
        collector.record_api_call(0.5, status_code=200)
        collector.record_api_call(1.0, status_code=500)
        collector.record_api_call(0.8, error_type="TimeoutError")
        
        metrics = collector.get_api_metrics()
        assert metrics['total_calls'] == 3
        assert metrics['successful_calls'] == 1
        assert metrics['failed_calls'] == 2
        assert metrics['success_rate'] == 1/3
    
    def test_get_processing_metrics(self):
        """처리 메트릭 반환 테스트"""
        collector = MetricsCollector()
        
        collector.record_processing(1.0, success=True)
        collector.record_processing(2.0, success=True)
        collector.record_processing(3.0, success=False)
        
        metrics = collector.get_processing_metrics()
        
        assert metrics['total_processed'] == 3
        assert metrics['success_count'] == 2
        assert metrics['error_count'] == 1
        assert metrics['success_rate'] == 2/3
        assert metrics['total_duration'] == 6.0
        assert metrics['avg_processing_time'] == 2.0
        assert metrics['median_processing_time'] == 2.0
        assert metrics['min_processing_time'] == 1.0
        assert metrics['max_processing_time'] == 3.0
    
    def test_get_quality_metrics(self):
        """품질 메트릭 반환 테스트"""
        collector = MetricsCollector()
        
        collector.record_quality(0.9)  # high
        collector.record_quality(0.7)  # medium
        collector.record_quality(0.5)  # low
        collector.record_quality(0.8, is_duplicate=True)  # high + duplicate
        collector.record_quality(0.6, has_safety_violation=True)  # medium + violation
        
        metrics = collector.get_quality_metrics()
        
        assert metrics['total_items'] == 5
        assert metrics['high_quality_count'] == 2
        assert metrics['medium_quality_count'] == 2
        assert metrics['low_quality_count'] == 1
        assert metrics['high_quality_rate'] == 2/5
        assert metrics['medium_quality_rate'] == 2/5
        assert metrics['low_quality_rate'] == 1/5
        assert metrics['duplicate_count'] == 1
        assert metrics['duplicate_rate'] == 1/5
        assert metrics['safety_violations'] == 1
        assert metrics['safety_violation_rate'] == 1/5
    
    @patch('psutil.cpu_percent')
    @patch('psutil.virtual_memory')
    @patch('psutil.Process')
    def test_get_resource_metrics(self, mock_process, mock_memory, mock_cpu):
        """리소스 메트릭 반환 테스트"""
        mock_cpu.return_value = 45.5
        mock_memory.return_value = MagicMock(percent=60.2)
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value = MagicMock(rss=1024 * 1024 * 512)
        mock_process.return_value = mock_process_instance
        
        collector = MetricsCollector()
        collector.resource_metrics.update()
        
        metrics = collector.get_resource_metrics()
        
        assert metrics['current_cpu_percent'] == 45.5
        assert metrics['peak_cpu_percent'] == 45.5
        assert metrics['current_memory_mb'] == 512.0
        assert metrics['peak_memory_mb'] == 512.0
        assert metrics['memory_usage_percent'] == 60.2
    
    def test_get_api_metrics(self):
        """API 메트릭 반환 테스트"""
        collector = MetricsCollector()
        
        collector.record_api_call(0.5, status_code=200)
        collector.record_api_call(1.0, status_code=200)
        collector.record_api_call(1.5, status_code=500)
        collector.record_api_call(0.8, error_type="ConnectionError")
        
        metrics = collector.get_api_metrics()
        
        assert metrics['total_calls'] == 4
        assert metrics['successful_calls'] == 2
        assert metrics['failed_calls'] == 2
        assert metrics['success_rate'] == 0.5
        assert metrics['failure_rate'] == 0.5
        assert metrics['avg_response_time'] == 0.95  # (0.5 + 1.0 + 1.5 + 0.8) / 4
        assert metrics['median_response_time'] == 0.9  # median of [0.5, 0.8, 1.0, 1.5]
        assert metrics['min_response_time'] == 0.5
        assert metrics['max_response_time'] == 1.5
        assert metrics['status_codes'][200] == 2
        assert metrics['status_codes'][500] == 1
        assert metrics['error_types']['ConnectionError'] == 1
    
    def test_get_all_metrics(self):
        """전체 메트릭 반환 테스트"""
        collector = MetricsCollector()
        
        # 일부 메트릭 기록
        collector.record_processing(1.0, success=True)
        collector.record_quality(0.8)
        collector.record_api_call(0.5, status_code=200)
        
        all_metrics = collector.get_all_metrics()
        
        assert 'timestamp' in all_metrics
        assert 'uptime_seconds' in all_metrics
        assert 'processing' in all_metrics
        assert 'quality' in all_metrics
        assert 'resources' in all_metrics
        assert 'api' in all_metrics
        
        # 각 섹션의 기본 구조 확인
        assert all_metrics['processing']['total_processed'] == 1
        assert all_metrics['quality']['total_items'] == 1
        assert all_metrics['api']['total_calls'] == 1
    
    def test_reset_metrics(self):
        """메트릭 초기화 테스트"""
        collector = MetricsCollector()
        
        # 일부 메트릭 기록
        collector.record_processing(1.0, success=True)
        collector.record_quality(0.8)
        collector.record_api_call(0.5, status_code=200)
        
        # 초기화 전 확인
        assert collector.get_processing_metrics()['total_processed'] == 1
        assert collector.get_quality_metrics()['total_items'] == 1
        assert collector.get_api_metrics()['total_calls'] == 1
        
        # 초기화
        collector.reset_metrics()
        
        # 초기화 후 확인
        assert collector.get_processing_metrics()['total_processed'] == 0
        assert collector.get_quality_metrics()['total_items'] == 0
        assert collector.get_api_metrics()['total_calls'] == 0
        assert len(collector.resource_history) == 0
        assert len(collector.throughput_history) == 0
    
    def test_generate_summary_report(self):
        """요약 리포트 생성 테스트"""
        collector = MetricsCollector()
        
        # 일부 메트릭 기록
        collector.record_processing(1.0, success=True)
        collector.record_processing(2.0, success=True)
        collector.record_quality(0.9)
        collector.record_quality(0.8)
        collector.record_api_call(0.5, status_code=200)
        
        report = collector.generate_summary_report()
        
        assert 'report_timestamp' in report
        assert 'uptime_hours' in report
        assert 'summary' in report
        assert 'detailed_metrics' in report
        
        summary = report['summary']
        assert summary['total_processed'] == 2
        assert summary['success_rate'] == 1.0
        assert summary['avg_quality_score'] == 0.85
        assert summary['high_quality_rate'] == 1.0
        assert summary['api_success_rate'] == 1.0
    
    @patch('psutil.cpu_percent')
    @patch('psutil.virtual_memory')
    @patch('psutil.Process')
    def test_background_collection(self, mock_process, mock_memory, mock_cpu):
        """백그라운드 메트릭 수집 테스트"""
        mock_cpu.return_value = 30.0
        mock_memory.return_value = MagicMock(percent=50.0)
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value = MagicMock(rss=1024 * 1024 * 256)
        mock_process.return_value = mock_process_instance
        
        collector = MetricsCollector(collection_interval=0.1)  # 0.1초 간격
        
        try:
            collector.start_collection()
            time.sleep(0.3)  # 0.3초 대기 (약 3번 수집)
            
            # 리소스 히스토리가 수집되었는지 확인
            assert len(collector.resource_history) > 0
            
            # 히스토리 데이터 구조 확인
            history_entry = collector.resource_history[0]
            assert 'timestamp' in history_entry
            assert 'cpu_percent' in history_entry
            assert 'memory_mb' in history_entry
            assert 'memory_percent' in history_entry
            
        finally:
            collector.stop_collection()
    
    def test_resource_history_filtering(self):
        """리소스 히스토리 필터링 테스트"""
        collector = MetricsCollector()
        
        # 가짜 히스토리 데이터 추가
        from datetime import datetime, timedelta
        now = datetime.now()
        
        # 2시간 전, 1시간 전, 30분 전 데이터 추가
        collector.resource_history.append({
            'timestamp': (now - timedelta(hours=2)).isoformat(),
            'cpu_percent': 20.0,
            'memory_mb': 200.0,
            'memory_percent': 40.0
        })
        collector.resource_history.append({
            'timestamp': (now - timedelta(hours=1)).isoformat(),
            'cpu_percent': 30.0,
            'memory_mb': 300.0,
            'memory_percent': 50.0
        })
        collector.resource_history.append({
            'timestamp': (now - timedelta(minutes=30)).isoformat(),
            'cpu_percent': 40.0,
            'memory_mb': 400.0,
            'memory_percent': 60.0
        })
        
        # 최근 1시간 데이터만 가져오기
        recent_history = collector.get_resource_history(minutes=60)
        
        # 1시간 이내 데이터만 반환되어야 함 (2개)
        assert len(recent_history) == 2
        assert recent_history[0]['cpu_percent'] == 30.0  # 1시간 전
        assert recent_history[1]['cpu_percent'] == 40.0  # 30분 전
    
    def test_throughput_history_filtering(self):
        """처리량 히스토리 필터링 테스트"""
        collector = MetricsCollector()
        
        # 가짜 처리량 히스토리 데이터 추가
        from datetime import datetime, timedelta
        now = datetime.now()
        
        collector.throughput_history.append({
            'timestamp': (now - timedelta(hours=2)).isoformat(),
            'throughput': 10.0,
            'total_processed': 100
        })
        collector.throughput_history.append({
            'timestamp': (now - timedelta(minutes=30)).isoformat(),
            'throughput': 15.0,
            'total_processed': 200
        })
        
        # 최근 1시간 데이터만 가져오기
        recent_history = collector.get_throughput_history(minutes=60)
        
        # 1시간 이내 데이터만 반환되어야 함 (1개)
        assert len(recent_history) == 1
        assert recent_history[0]['throughput'] == 15.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])