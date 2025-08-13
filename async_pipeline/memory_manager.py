"""
메모리 관리 및 리소스 모니터링

시스템 리소스를 모니터링하고 메모리 사용량을 관리합니다.
"""

import asyncio
import logging
import time
import gc
from typing import Dict, Optional, Callable, Any
from dataclasses import dataclass, field
from collections import deque
import psutil
import threading

logger = logging.getLogger(__name__)


@dataclass
class ResourceMetrics:
    """리소스 메트릭"""
    timestamp: float
    memory_usage_mb: float
    memory_percent: float
    cpu_percent: float
    disk_usage_percent: float
    available_memory_mb: float
    process_memory_mb: float
    process_cpu_percent: float
    thread_count: int
    file_descriptor_count: int


@dataclass
class MemoryManagerConfig:
    """메모리 관리자 설정"""
    
    # 메모리 임계값 (백분율)
    memory_warning_threshold: float = 80.0
    memory_critical_threshold: float = 90.0
    memory_emergency_threshold: float = 95.0
    
    # 배치 크기 조정 설정
    enable_dynamic_batch_sizing: bool = True
    min_batch_size: int = 8
    max_batch_size: int = 128
    batch_size_adjustment_factor: float = 0.8
    
    # 캐시 관리 설정
    enable_cache_management: bool = True
    cache_cleanup_threshold: float = 85.0
    max_cache_size_mb: float = 1024.0
    
    # 가비지 컬렉션 설정
    enable_aggressive_gc: bool = True
    gc_threshold: float = 85.0
    gc_interval: float = 30.0  # 초
    
    # 모니터링 설정
    monitoring_interval: float = 5.0  # 초
    metrics_history_size: int = 100
    
    # 알림 설정
    enable_alerts: bool = True
    alert_cooldown: float = 60.0  # 초
    
    def validate(self) -> None:
        """설정 유효성 검증"""
        if not (0 < self.memory_warning_threshold < self.memory_critical_threshold < self.memory_emergency_threshold < 100):
            raise ValueError("메모리 임계값은 0 < warning < critical < emergency < 100 이어야 합니다")
        
        if not (self.min_batch_size <= self.max_batch_size):
            raise ValueError("최소 배치 크기는 최대 배치 크기보다 작거나 같아야 합니다")
        
        if not (0 < self.batch_size_adjustment_factor < 1):
            raise ValueError("배치 크기 조정 비율은 0과 1 사이여야 합니다")


class MemoryManager:
    """메모리 관리자"""
    
    def __init__(self, config: Optional[MemoryManagerConfig] = None):
        self.config = config or MemoryManagerConfig()
        self.config.validate()
        
        # 내부 상태
        self._running = False
        self._monitor_task: Optional[asyncio.Task] = None
        self._gc_task: Optional[asyncio.Task] = None
        
        # 메트릭 히스토리
        self._metrics_history: deque = deque(maxlen=self.config.metrics_history_size)
        self._last_alert_time: Dict[str, float] = {}
        
        # 캐시 관리
        self._cache_registry: Dict[str, Any] = {}
        self._cache_sizes: Dict[str, float] = {}
        
        # 동적 배치 크기
        self._current_batch_size: int = 32
        self._batch_size_history: deque = deque(maxlen=10)
        
        # 콜백 함수들
        self._alert_callbacks: Dict[str, Callable] = {}
        
        logger.info("MemoryManager 초기화 완료")
    
    async def start(self) -> None:
        """메모리 관리자 시작"""
        if self._running:
            logger.warning("메모리 관리자가 이미 실행 중입니다")
            return
        
        self._running = True
        
        # 모니터링 태스크 시작
        self._monitor_task = asyncio.create_task(self._monitor_resources())
        
        # 가비지 컬렉션 태스크 시작
        if self.config.enable_aggressive_gc:
            self._gc_task = asyncio.create_task(self._garbage_collection_loop())
        
        logger.info("메모리 관리자 시작")
    
    async def stop(self) -> None:
        """메모리 관리자 중지"""
        if not self._running:
            return
        
        self._running = False
        
        # 태스크 중지
        if self._monitor_task:
            self._monitor_task.cancel()
            try:
                await self._monitor_task
            except asyncio.CancelledError:
                pass
        
        if self._gc_task:
            self._gc_task.cancel()
            try:
                await self._gc_task
            except asyncio.CancelledError:
                pass
        
        logger.info("메모리 관리자 중지")
    
    def get_current_metrics(self) -> ResourceMetrics:
        """현재 리소스 메트릭 반환"""
        try:
            # 시스템 메트릭
            memory = psutil.virtual_memory()
            cpu_percent = psutil.cpu_percent(interval=0.1)
            disk = psutil.disk_usage('/')
            
            # 프로세스 메트릭
            process = psutil.Process()
            process_memory = process.memory_info()
            process_cpu = process.cpu_percent()
            
            return ResourceMetrics(
                timestamp=time.time(),
                memory_usage_mb=memory.used / 1024 / 1024,
                memory_percent=memory.percent,
                cpu_percent=cpu_percent,
                disk_usage_percent=disk.percent,
                available_memory_mb=memory.available / 1024 / 1024,
                process_memory_mb=process_memory.rss / 1024 / 1024,
                process_cpu_percent=process_cpu,
                thread_count=threading.active_count(),
                file_descriptor_count=len(process.open_files())
            )
        except Exception as e:
            logger.error(f"메트릭 수집 오류: {str(e)}")
            return ResourceMetrics(
                timestamp=time.time(),
                memory_usage_mb=0,
                memory_percent=0,
                cpu_percent=0,
                disk_usage_percent=0,
                available_memory_mb=0,
                process_memory_mb=0,
                process_cpu_percent=0,
                thread_count=0,
                file_descriptor_count=0
            )
    
    def get_metrics_history(self) -> list[ResourceMetrics]:
        """메트릭 히스토리 반환"""
        return list(self._metrics_history)
    
    def get_optimal_batch_size(self, current_batch_size: int) -> int:
        """최적 배치 크기 계산"""
        if not self.config.enable_dynamic_batch_sizing:
            return current_batch_size
        
        metrics = self.get_current_metrics()
        
        # 메모리 사용률에 따른 배치 크기 조정
        if metrics.memory_percent > self.config.memory_critical_threshold:
            # 메모리 부족 시 배치 크기 대폭 감소
            new_size = max(
                self.config.min_batch_size,
                int(current_batch_size * 0.5)
            )
        elif metrics.memory_percent > self.config.memory_warning_threshold:
            # 메모리 경고 시 배치 크기 감소
            new_size = max(
                self.config.min_batch_size,
                int(current_batch_size * self.config.batch_size_adjustment_factor)
            )
        elif metrics.memory_percent < 50.0:
            # 메모리 여유 시 배치 크기 증가
            new_size = min(
                self.config.max_batch_size,
                int(current_batch_size * 1.2)
            )
        else:
            new_size = current_batch_size
        
        # 배치 크기 히스토리 업데이트
        self._batch_size_history.append(new_size)
        self._current_batch_size = new_size
        
        if new_size != current_batch_size:
            logger.info(f"배치 크기 조정: {current_batch_size} -> {new_size} (메모리: {metrics.memory_percent:.1f}%)")
        
        return new_size
    
    def register_cache(self, name: str, cache_object: Any, size_mb: float = 0.0) -> None:
        """캐시 등록"""
        self._cache_registry[name] = cache_object
        self._cache_sizes[name] = size_mb
        logger.debug(f"캐시 등록: {name} ({size_mb:.1f}MB)")
    
    def unregister_cache(self, name: str) -> None:
        """캐시 등록 해제"""
        if name in self._cache_registry:
            del self._cache_registry[name]
            del self._cache_sizes[name]
            logger.debug(f"캐시 등록 해제: {name}")
    
    def cleanup_caches(self, force: bool = False) -> None:
        """캐시 정리"""
        if not self.config.enable_cache_management and not force:
            return
        
        metrics = self.get_current_metrics()
        
        if metrics.memory_percent > self.config.cache_cleanup_threshold or force:
            total_freed = 0.0
            
            for name, cache_obj in self._cache_registry.items():
                try:
                    if hasattr(cache_obj, 'clear'):
                        cache_obj.clear()
                        freed_size = self._cache_sizes.get(name, 0.0)
                        total_freed += freed_size
                        logger.debug(f"캐시 정리: {name} ({freed_size:.1f}MB)")
                except Exception as e:
                    logger.error(f"캐시 정리 오류 ({name}): {str(e)}")
            
            if total_freed > 0:
                logger.info(f"캐시 정리 완료: {total_freed:.1f}MB 해제")
            
            # 가비지 컬렉션 실행
            gc.collect()
    
    def force_garbage_collection(self) -> Dict[str, int]:
        """강제 가비지 컬렉션"""
        before_counts = [len(gc.get_objects())]
        
        # 모든 세대에 대해 가비지 컬렉션 실행
        collected = []
        for generation in range(3):
            collected.append(gc.collect(generation))
        
        after_counts = [len(gc.get_objects())]
        
        result = {
            'generation_0': collected[0] if len(collected) > 0 else 0,
            'generation_1': collected[1] if len(collected) > 1 else 0,
            'generation_2': collected[2] if len(collected) > 2 else 0,
            'objects_before': before_counts[0],
            'objects_after': after_counts[0],
            'objects_freed': before_counts[0] - after_counts[0]
        }
        
        logger.debug(f"가비지 컬렉션 완료: {result}")
        return result
    
    def register_alert_callback(self, alert_type: str, callback: Callable[[ResourceMetrics], None]) -> None:
        """알림 콜백 등록"""
        self._alert_callbacks[alert_type] = callback
        logger.debug(f"알림 콜백 등록: {alert_type}")
    
    async def _monitor_resources(self) -> None:
        """리소스 모니터링 루프"""
        while self._running:
            try:
                metrics = self.get_current_metrics()
                self._metrics_history.append(metrics)
                
                # 알림 확인
                await self._check_alerts(metrics)
                
                # 자동 캐시 정리
                if (self.config.enable_cache_management and 
                    metrics.memory_percent > self.config.cache_cleanup_threshold):
                    self.cleanup_caches()
                
                await asyncio.sleep(self.config.monitoring_interval)
                
            except Exception as e:
                logger.error(f"리소스 모니터링 오류: {str(e)}")
                await asyncio.sleep(self.config.monitoring_interval * 2)
    
    async def _garbage_collection_loop(self) -> None:
        """가비지 컬렉션 루프"""
        while self._running:
            try:
                await asyncio.sleep(self.config.gc_interval)
                
                metrics = self.get_current_metrics()
                if metrics.memory_percent > self.config.gc_threshold:
                    self.force_garbage_collection()
                
            except Exception as e:
                logger.error(f"가비지 컬렉션 루프 오류: {str(e)}")
                await asyncio.sleep(self.config.gc_interval * 2)
    
    async def _check_alerts(self, metrics: ResourceMetrics) -> None:
        """알림 확인 및 발송"""
        if not self.config.enable_alerts:
            return
        
        current_time = time.time()
        
        # 메모리 알림
        if metrics.memory_percent > self.config.memory_emergency_threshold:
            await self._send_alert('memory_emergency', metrics, current_time)
        elif metrics.memory_percent > self.config.memory_critical_threshold:
            await self._send_alert('memory_critical', metrics, current_time)
        elif metrics.memory_percent > self.config.memory_warning_threshold:
            await self._send_alert('memory_warning', metrics, current_time)
        
        # CPU 알림
        if metrics.cpu_percent > 90.0:
            await self._send_alert('cpu_high', metrics, current_time)
        
        # 디스크 알림
        if metrics.disk_usage_percent > 90.0:
            await self._send_alert('disk_full', metrics, current_time)
    
    async def _send_alert(self, alert_type: str, metrics: ResourceMetrics, current_time: float) -> None:
        """알림 발송"""
        # 쿨다운 확인
        last_alert = self._last_alert_time.get(alert_type, 0)
        if current_time - last_alert < self.config.alert_cooldown:
            return
        
        self._last_alert_time[alert_type] = current_time
        
        # 로그 알림
        if alert_type == 'memory_emergency':
            logger.critical(f"메모리 응급 상황: {metrics.memory_percent:.1f}% 사용 중")
        elif alert_type == 'memory_critical':
            logger.error(f"메모리 위험 수준: {metrics.memory_percent:.1f}% 사용 중")
        elif alert_type == 'memory_warning':
            logger.warning(f"메모리 경고: {metrics.memory_percent:.1f}% 사용 중")
        elif alert_type == 'cpu_high':
            logger.warning(f"CPU 사용률 높음: {metrics.cpu_percent:.1f}%")
        elif alert_type == 'disk_full':
            logger.warning(f"디스크 공간 부족: {metrics.disk_usage_percent:.1f}% 사용 중")
        
        # 콜백 실행
        callback = self._alert_callbacks.get(alert_type)
        if callback:
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(metrics)
                else:
                    callback(metrics)
            except Exception as e:
                logger.error(f"알림 콜백 오류 ({alert_type}): {str(e)}")
    
    def get_memory_summary(self) -> Dict[str, Any]:
        """메모리 사용 요약 반환"""
        metrics = self.get_current_metrics()
        
        return {
            'system_memory': {
                'total_mb': psutil.virtual_memory().total / 1024 / 1024,
                'used_mb': metrics.memory_usage_mb,
                'available_mb': metrics.available_memory_mb,
                'percent': metrics.memory_percent
            },
            'process_memory': {
                'rss_mb': metrics.process_memory_mb,
                'percent': metrics.process_cpu_percent
            },
            'cache_info': {
                'registered_caches': len(self._cache_registry),
                'total_cache_size_mb': sum(self._cache_sizes.values())
            },
            'batch_sizing': {
                'current_batch_size': self._current_batch_size,
                'dynamic_sizing_enabled': self.config.enable_dynamic_batch_sizing
            },
            'gc_info': {
                'gc_counts': gc.get_count(),
                'gc_thresholds': gc.get_threshold()
            }
        }