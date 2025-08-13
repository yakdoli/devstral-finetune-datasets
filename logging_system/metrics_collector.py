"""
메트릭 수집 시스템

처리 성능, 품질 메트릭, 리소스 사용량 등을 수집하고 분석합니다.
"""

import time
import psutil
import threading
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Deque
from statistics import mean, median


@dataclass
class ProcessingMetrics:
    """처리 성능 메트릭"""
    total_processed: int = 0
    success_count: int = 0
    error_count: int = 0
    total_duration: float = 0.0
    avg_processing_time: float = 0.0
    throughput_per_second: float = 0.0
    peak_throughput: float = 0.0
    processing_times: List[float] = field(default_factory=list)
    
    def update(self, duration: float, success: bool = True):
        """메트릭 업데이트"""
        self.total_processed += 1
        if success:
            self.success_count += 1
        else:
            self.error_count += 1
        
        self.total_duration += duration
        self.processing_times.append(duration)
        
        # 최근 100개 항목만 유지
        if len(self.processing_times) > 100:
            self.processing_times = self.processing_times[-100:]
        
        # 평균 처리 시간 계산
        if self.processing_times:
            self.avg_processing_time = mean(self.processing_times)
        
        # 처리량 계산 (초당 처리 개수)
        if self.total_duration > 0:
            self.throughput_per_second = self.total_processed / self.total_duration


@dataclass
class QualityMetrics:
    """품질 메트릭"""
    total_items: int = 0
    high_quality_count: int = 0  # 품질 점수 >= 0.8
    medium_quality_count: int = 0  # 품질 점수 0.6-0.8
    low_quality_count: int = 0  # 품질 점수 < 0.6
    avg_quality_score: float = 0.0
    quality_scores: List[float] = field(default_factory=list)
    duplicate_count: int = 0
    safety_violations: int = 0
    
    def update(self, quality_score: float, is_duplicate: bool = False, 
               has_safety_violation: bool = False):
        """품질 메트릭 업데이트"""
        self.total_items += 1
        self.quality_scores.append(quality_score)
        
        if quality_score >= 0.8:
            self.high_quality_count += 1
        elif quality_score >= 0.6:
            self.medium_quality_count += 1
        else:
            self.low_quality_count += 1
        
        if is_duplicate:
            self.duplicate_count += 1
        
        if has_safety_violation:
            self.safety_violations += 1
        
        # 평균 품질 점수 계산
        if self.quality_scores:
            self.avg_quality_score = mean(self.quality_scores)


@dataclass
class ResourceMetrics:
    """리소스 사용량 메트릭"""
    cpu_usage_percent: float = 0.0
    memory_usage_mb: float = 0.0
    memory_usage_percent: float = 0.0
    disk_usage_mb: float = 0.0
    network_sent_mb: float = 0.0
    network_recv_mb: float = 0.0
    peak_memory_mb: float = 0.0
    peak_cpu_percent: float = 0.0
    
    def update(self):
        """리소스 메트릭 업데이트"""
        # CPU 사용률
        self.cpu_usage_percent = psutil.cpu_percent(interval=0.1)
        self.peak_cpu_percent = max(self.peak_cpu_percent, self.cpu_usage_percent)
        
        # 메모리 사용량
        memory = psutil.virtual_memory()
        process = psutil.Process()
        process_memory = process.memory_info()
        
        self.memory_usage_mb = process_memory.rss / 1024 / 1024
        self.memory_usage_percent = memory.percent
        self.peak_memory_mb = max(self.peak_memory_mb, self.memory_usage_mb)
        
        # 디스크 사용량 (현재 프로세스)
        try:
            io_counters = process.io_counters()
            self.disk_usage_mb = (io_counters.read_bytes + io_counters.write_bytes) / 1024 / 1024
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
        
        # 네트워크 사용량
        try:
            net_io = psutil.net_io_counters()
            if net_io:
                self.network_sent_mb = net_io.bytes_sent / 1024 / 1024
                self.network_recv_mb = net_io.bytes_recv / 1024 / 1024
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


@dataclass
class APIMetrics:
    """API 호출 메트릭"""
    total_calls: int = 0
    successful_calls: int = 0
    failed_calls: int = 0
    total_response_time: float = 0.0
    avg_response_time: float = 0.0
    response_times: List[float] = field(default_factory=list)
    status_codes: Dict[int, int] = field(default_factory=lambda: defaultdict(int))
    error_types: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    
    def update(self, response_time: float, status_code: Optional[int] = None, 
               error_type: Optional[str] = None):
        """API 메트릭 업데이트"""
        self.total_calls += 1
        self.total_response_time += response_time
        self.response_times.append(response_time)
        
        # 최근 100개 응답 시간만 유지
        if len(self.response_times) > 100:
            self.response_times = self.response_times[-100:]
        
        if status_code:
            self.status_codes[status_code] += 1
            if 200 <= status_code < 300:
                self.successful_calls += 1
            else:
                self.failed_calls += 1
        
        if error_type:
            self.error_types[error_type] += 1
            self.failed_calls += 1
        
        # 평균 응답 시간 계산
        if self.response_times:
            self.avg_response_time = mean(self.response_times)


class MetricsCollector:
    """메트릭 수집기 메인 클래스"""
    
    def __init__(self, collection_interval: float = 5.0):
        """
        메트릭 수집기 초기화
        
        Args:
            collection_interval: 리소스 메트릭 수집 간격 (초)
        """
        self.collection_interval = collection_interval
        self.start_time = time.time()
        
        # 메트릭 저장소
        self.processing_metrics = ProcessingMetrics()
        self.quality_metrics = QualityMetrics()
        self.resource_metrics = ResourceMetrics()
        self.api_metrics = APIMetrics()
        
        # 시계열 데이터 저장 (최근 1시간)
        self.resource_history: Deque[Dict[str, Any]] = deque(maxlen=720)  # 5초 간격으로 1시간
        self.throughput_history: Deque[Dict[str, Any]] = deque(maxlen=360)  # 10초 간격으로 1시간
        
        # 백그라운드 수집 스레드
        self._collection_thread = None
        self._stop_collection = threading.Event()
        self._lock = threading.Lock()
    
    def start_collection(self):
        """백그라운드 메트릭 수집 시작"""
        if self._collection_thread is None or not self._collection_thread.is_alive():
            self._stop_collection.clear()
            self._collection_thread = threading.Thread(target=self._collect_metrics_loop)
            self._collection_thread.daemon = True
            self._collection_thread.start()
    
    def stop_collection(self):
        """백그라운드 메트릭 수집 중지"""
        self._stop_collection.set()
        if self._collection_thread and self._collection_thread.is_alive():
            self._collection_thread.join(timeout=1.0)
    
    def _collect_metrics_loop(self):
        """백그라운드 메트릭 수집 루프"""
        while not self._stop_collection.wait(self.collection_interval):
            try:
                with self._lock:
                    # 리소스 메트릭 업데이트
                    self.resource_metrics.update()
                    
                    # 시계열 데이터 저장
                    timestamp = datetime.now()
                    self.resource_history.append({
                        'timestamp': timestamp.isoformat(),
                        'cpu_percent': self.resource_metrics.cpu_usage_percent,
                        'memory_mb': self.resource_metrics.memory_usage_mb,
                        'memory_percent': self.resource_metrics.memory_usage_percent
                    })
                    
                    # 처리량 히스토리 업데이트 (10초마다)
                    if len(self.resource_history) % 2 == 0:  # 5초 * 2 = 10초
                        self.throughput_history.append({
                            'timestamp': timestamp.isoformat(),
                            'throughput': self.processing_metrics.throughput_per_second,
                            'total_processed': self.processing_metrics.total_processed
                        })
                        
            except Exception as e:
                # 메트릭 수집 오류는 조용히 무시
                pass
    
    def record_processing(self, duration: float, success: bool = True):
        """처리 메트릭 기록"""
        with self._lock:
            self.processing_metrics.update(duration, success)
    
    def record_quality(self, quality_score: float, is_duplicate: bool = False, 
                      has_safety_violation: bool = False):
        """품질 메트릭 기록"""
        with self._lock:
            self.quality_metrics.update(quality_score, is_duplicate, has_safety_violation)
    
    def record_api_call(self, response_time: float, status_code: Optional[int] = None, 
                       error_type: Optional[str] = None):
        """API 호출 메트릭 기록"""
        with self._lock:
            self.api_metrics.update(response_time, status_code, error_type)
    
    def get_processing_metrics(self) -> Dict[str, Any]:
        """처리 성능 메트릭 반환"""
        with self._lock:
            metrics = self.processing_metrics
            return {
                'total_processed': metrics.total_processed,
                'success_count': metrics.success_count,
                'error_count': metrics.error_count,
                'success_rate': metrics.success_count / max(metrics.total_processed, 1),
                'total_duration': metrics.total_duration,
                'avg_processing_time': metrics.avg_processing_time,
                'throughput_per_second': metrics.throughput_per_second,
                'peak_throughput': metrics.peak_throughput,
                'median_processing_time': median(metrics.processing_times) if metrics.processing_times else 0.0,
                'min_processing_time': min(metrics.processing_times) if metrics.processing_times else 0.0,
                'max_processing_time': max(metrics.processing_times) if metrics.processing_times else 0.0
            }
    
    def get_quality_metrics(self) -> Dict[str, Any]:
        """품질 메트릭 반환"""
        with self._lock:
            metrics = self.quality_metrics
            total = max(metrics.total_items, 1)
            return {
                'total_items': metrics.total_items,
                'high_quality_count': metrics.high_quality_count,
                'medium_quality_count': metrics.medium_quality_count,
                'low_quality_count': metrics.low_quality_count,
                'high_quality_rate': metrics.high_quality_count / total,
                'medium_quality_rate': metrics.medium_quality_count / total,
                'low_quality_rate': metrics.low_quality_count / total,
                'avg_quality_score': metrics.avg_quality_score,
                'duplicate_count': metrics.duplicate_count,
                'duplicate_rate': metrics.duplicate_count / total,
                'safety_violations': metrics.safety_violations,
                'safety_violation_rate': metrics.safety_violations / total,
                'median_quality_score': median(metrics.quality_scores) if metrics.quality_scores else 0.0,
                'min_quality_score': min(metrics.quality_scores) if metrics.quality_scores else 0.0,
                'max_quality_score': max(metrics.quality_scores) if metrics.quality_scores else 0.0
            }
    
    def get_resource_metrics(self) -> Dict[str, Any]:
        """리소스 사용량 메트릭 반환"""
        with self._lock:
            metrics = self.resource_metrics
            return {
                'current_cpu_percent': metrics.cpu_usage_percent,
                'peak_cpu_percent': metrics.peak_cpu_percent,
                'current_memory_mb': metrics.memory_usage_mb,
                'peak_memory_mb': metrics.peak_memory_mb,
                'memory_usage_percent': metrics.memory_usage_percent,
                'disk_usage_mb': metrics.disk_usage_mb,
                'network_sent_mb': metrics.network_sent_mb,
                'network_recv_mb': metrics.network_recv_mb
            }
    
    def get_api_metrics(self) -> Dict[str, Any]:
        """API 호출 메트릭 반환"""
        with self._lock:
            metrics = self.api_metrics
            total = max(metrics.total_calls, 1)
            return {
                'total_calls': metrics.total_calls,
                'successful_calls': metrics.successful_calls,
                'failed_calls': metrics.failed_calls,
                'success_rate': metrics.successful_calls / total,
                'failure_rate': metrics.failed_calls / total,
                'avg_response_time': metrics.avg_response_time,
                'total_response_time': metrics.total_response_time,
                'median_response_time': median(metrics.response_times) if metrics.response_times else 0.0,
                'min_response_time': min(metrics.response_times) if metrics.response_times else 0.0,
                'max_response_time': max(metrics.response_times) if metrics.response_times else 0.0,
                'status_codes': dict(metrics.status_codes),
                'error_types': dict(metrics.error_types)
            }
    
    def get_all_metrics(self) -> Dict[str, Any]:
        """모든 메트릭 반환"""
        uptime = time.time() - self.start_time
        
        return {
            'timestamp': datetime.now().isoformat(),
            'uptime_seconds': uptime,
            'processing': self.get_processing_metrics(),
            'quality': self.get_quality_metrics(),
            'resources': self.get_resource_metrics(),
            'api': self.get_api_metrics()
        }
    
    def get_resource_history(self, minutes: int = 60) -> List[Dict[str, Any]]:
        """리소스 사용량 히스토리 반환"""
        with self._lock:
            cutoff_time = datetime.now() - timedelta(minutes=minutes)
            return [
                entry for entry in self.resource_history
                if datetime.fromisoformat(entry['timestamp']) >= cutoff_time
            ]
    
    def get_throughput_history(self, minutes: int = 60) -> List[Dict[str, Any]]:
        """처리량 히스토리 반환"""
        with self._lock:
            cutoff_time = datetime.now() - timedelta(minutes=minutes)
            return [
                entry for entry in self.throughput_history
                if datetime.fromisoformat(entry['timestamp']) >= cutoff_time
            ]
    
    def reset_metrics(self):
        """모든 메트릭 초기화"""
        with self._lock:
            self.processing_metrics = ProcessingMetrics()
            self.quality_metrics = QualityMetrics()
            self.resource_metrics = ResourceMetrics()
            self.api_metrics = APIMetrics()
            self.resource_history.clear()
            self.throughput_history.clear()
            self.start_time = time.time()
    
    def generate_summary_report(self) -> Dict[str, Any]:
        """요약 리포트 생성"""
        all_metrics = self.get_all_metrics()
        uptime_hours = all_metrics['uptime_seconds'] / 3600
        
        return {
            'report_timestamp': all_metrics['timestamp'],
            'uptime_hours': uptime_hours,
            'summary': {
                'total_processed': all_metrics['processing']['total_processed'],
                'success_rate': all_metrics['processing']['success_rate'],
                'avg_throughput': all_metrics['processing']['throughput_per_second'],
                'avg_quality_score': all_metrics['quality']['avg_quality_score'],
                'high_quality_rate': all_metrics['quality']['high_quality_rate'],
                'peak_memory_mb': all_metrics['resources']['peak_memory_mb'],
                'peak_cpu_percent': all_metrics['resources']['peak_cpu_percent'],
                'api_success_rate': all_metrics['api']['success_rate'],
                'avg_api_response_time': all_metrics['api']['avg_response_time']
            },
            'detailed_metrics': all_metrics
        }