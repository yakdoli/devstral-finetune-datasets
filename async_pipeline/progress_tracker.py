"""
진행률 표시 및 성능 메트릭 추적기

실시간 진행률 표시, ETA 계산, 성능 메트릭 수집 및 리포팅을 제공합니다.
"""

import asyncio
import time
import logging
from typing import Dict, Optional, Any, List, Callable
from dataclasses import dataclass, field
from collections import deque
import threading
from tqdm.asyncio import tqdm
import json

logger = logging.getLogger(__name__)


@dataclass
class PerformanceMetrics:
    """성능 메트릭"""
    timestamp: float
    total_items: int = 0
    processed_items: int = 0
    failed_items: int = 0
    items_per_second: float = 0.0
    average_processing_time: float = 0.0
    estimated_time_remaining: float = 0.0
    memory_usage_mb: float = 0.0
    cpu_usage_percent: float = 0.0
    active_workers: int = 0
    queue_size: int = 0
    success_rate: float = 0.0
    error_rate: float = 0.0


@dataclass
class ProgressTrackerConfig:
    """진행률 추적기 설정"""
    
    # 진행률 표시 설정
    enable_progress_bar: bool = True
    progress_bar_format: str = "{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"
    update_interval: float = 0.5  # 초
    
    # 메트릭 수집 설정
    enable_metrics_collection: bool = True
    metrics_history_size: int = 1000
    metrics_update_interval: float = 1.0  # 초
    
    # ETA 계산 설정
    eta_smoothing_window: int = 50  # 최근 N개 샘플로 ETA 계산
    min_samples_for_eta: int = 10  # ETA 계산을 위한 최소 샘플 수
    
    # 성능 리포팅 설정
    enable_performance_logging: bool = True
    performance_log_interval: float = 30.0  # 초
    
    # 알림 설정
    enable_milestone_alerts: bool = True
    milestone_percentages: List[int] = field(default_factory=lambda: [25, 50, 75, 90])
    
    def validate(self) -> None:
        """설정 유효성 검증"""
        if self.update_interval <= 0:
            raise ValueError("업데이트 간격은 0보다 커야 합니다")
        
        if self.metrics_history_size <= 0:
            raise ValueError("메트릭 히스토리 크기는 0보다 커야 합니다")
        
        if self.eta_smoothing_window <= 0:
            raise ValueError("ETA 스무딩 윈도우는 0보다 커야 합니다")


class ProgressTracker:
    """진행률 추적기"""
    
    def __init__(self, config: Optional[ProgressTrackerConfig] = None):
        self.config = config or ProgressTrackerConfig()
        self.config.validate()
        
        # 내부 상태
        self._running = False
        self._start_time: Optional[float] = None
        self._end_time: Optional[float] = None
        
        # 진행률 상태
        self._total_items = 0
        self._processed_items = 0
        self._failed_items = 0
        self._current_stage = "초기화"
        
        # 진행률 바
        self._progress_bar: Optional[tqdm] = None
        self._progress_lock = threading.Lock()
        
        # 메트릭 히스토리
        self._metrics_history: deque = deque(maxlen=self.config.metrics_history_size)
        self._processing_times: deque = deque(maxlen=self.config.eta_smoothing_window)
        
        # 마일스톤 추적
        self._milestone_alerts_sent = set()
        
        # 콜백 함수들
        self._stage_callbacks: Dict[str, Callable] = {}
        self._milestone_callbacks: Dict[int, Callable] = {}
        
        # 태스크
        self._metrics_task: Optional[asyncio.Task] = None
        self._performance_log_task: Optional[asyncio.Task] = None
        
        logger.info("ProgressTracker 초기화 완료")
    
    async def start(self, total_items: int, description: str = "처리 중") -> None:
        """진행률 추적 시작"""
        if self._running:
            logger.warning("진행률 추적기가 이미 실행 중입니다")
            return
        
        self._running = True
        self._start_time = time.time()
        self._total_items = total_items
        self._processed_items = 0
        self._failed_items = 0
        self._milestone_alerts_sent.clear()
        
        # 진행률 바 초기화
        if self.config.enable_progress_bar:
            self._progress_bar = tqdm(
                total=total_items,
                desc=description,
                bar_format=self.config.progress_bar_format,
                dynamic_ncols=True,
                leave=True
            )
        
        # 메트릭 수집 태스크 시작
        if self.config.enable_metrics_collection:
            self._metrics_task = asyncio.create_task(self._collect_metrics_loop())
        
        # 성능 로깅 태스크 시작
        if self.config.enable_performance_logging:
            self._performance_log_task = asyncio.create_task(self._performance_logging_loop())
        
        logger.info(f"진행률 추적 시작: {total_items}개 항목, '{description}'")
    
    async def stop(self) -> None:
        """진행률 추적 중지"""
        if not self._running:
            return
        
        self._running = False
        self._end_time = time.time()
        
        # 태스크 중지
        if self._metrics_task:
            self._metrics_task.cancel()
            try:
                await self._metrics_task
            except asyncio.CancelledError:
                pass
        
        if self._performance_log_task:
            self._performance_log_task.cancel()
            try:
                await self._performance_log_task
            except asyncio.CancelledError:
                pass
        
        # 진행률 바 종료
        if self._progress_bar:
            self._progress_bar.close()
            self._progress_bar = None
        
        # 최종 리포트 생성
        final_report = self.generate_final_report()
        logger.info(f"진행률 추적 완료: {json.dumps(final_report, indent=2, ensure_ascii=False)}")
    
    def update_progress(
        self,
        processed_count: int = 1,
        failed_count: int = 0,
        processing_time: Optional[float] = None,
        stage: Optional[str] = None
    ) -> None:
        """진행률 업데이트"""
        with self._progress_lock:
            self._processed_items += processed_count
            self._failed_items += failed_count
            
            if stage:
                self._current_stage = stage
            
            if processing_time is not None:
                self._processing_times.append(processing_time)
            
            # 진행률 바 업데이트
            if self._progress_bar:
                self._progress_bar.update(processed_count)
                
                # 포스트픽스 정보 업데이트
                postfix = self._get_progress_postfix()
                self._progress_bar.set_postfix_str(postfix)
            
            # 마일스톤 확인
            self._check_milestones()
    
    def set_stage(self, stage: str) -> None:
        """현재 단계 설정"""
        self._current_stage = stage
        
        if self._progress_bar:
            self._progress_bar.set_description(stage)
        
        # 단계 콜백 실행
        callback = self._stage_callbacks.get(stage)
        if callback:
            try:
                callback(stage, self.get_current_metrics())
            except Exception as e:
                logger.error(f"단계 콜백 오류 ({stage}): {str(e)}")
        
        logger.debug(f"단계 변경: {stage}")
    
    def get_current_metrics(self) -> PerformanceMetrics:
        """현재 성능 메트릭 반환"""
        current_time = time.time()
        
        # 처리 속도 계산
        elapsed_time = current_time - (self._start_time or current_time)
        items_per_second = self._processed_items / elapsed_time if elapsed_time > 0 else 0.0
        
        # 평균 처리 시간 계산
        avg_processing_time = (
            sum(self._processing_times) / len(self._processing_times)
            if self._processing_times else 0.0
        )
        
        # ETA 계산
        remaining_items = self._total_items - self._processed_items
        eta = remaining_items / items_per_second if items_per_second > 0 else 0.0
        
        # 성공률 계산
        total_completed = self._processed_items + self._failed_items
        success_rate = (
            self._processed_items / total_completed * 100
            if total_completed > 0 else 0.0
        )
        error_rate = (
            self._failed_items / total_completed * 100
            if total_completed > 0 else 0.0
        )
        
        return PerformanceMetrics(
            timestamp=current_time,
            total_items=self._total_items,
            processed_items=self._processed_items,
            failed_items=self._failed_items,
            items_per_second=items_per_second,
            average_processing_time=avg_processing_time,
            estimated_time_remaining=eta,
            success_rate=success_rate,
            error_rate=error_rate
        )
    
    def get_metrics_history(self) -> List[PerformanceMetrics]:
        """메트릭 히스토리 반환"""
        return list(self._metrics_history)
    
    def register_stage_callback(self, stage: str, callback: Callable[[str, PerformanceMetrics], None]) -> None:
        """단계 변경 콜백 등록"""
        self._stage_callbacks[stage] = callback
        logger.debug(f"단계 콜백 등록: {stage}")
    
    def register_milestone_callback(self, percentage: int, callback: Callable[[int, PerformanceMetrics], None]) -> None:
        """마일스톤 콜백 등록"""
        self._milestone_callbacks[percentage] = callback
        logger.debug(f"마일스톤 콜백 등록: {percentage}%")
    
    def generate_progress_report(self) -> Dict[str, Any]:
        """진행률 리포트 생성"""
        metrics = self.get_current_metrics()
        elapsed_time = time.time() - (self._start_time or time.time())
        
        return {
            "progress": {
                "total_items": metrics.total_items,
                "processed_items": metrics.processed_items,
                "failed_items": metrics.failed_items,
                "completion_percentage": (metrics.processed_items / metrics.total_items * 100) if metrics.total_items > 0 else 0.0,
                "current_stage": self._current_stage
            },
            "performance": {
                "elapsed_time_seconds": elapsed_time,
                "items_per_second": metrics.items_per_second,
                "average_processing_time": metrics.average_processing_time,
                "estimated_time_remaining": metrics.estimated_time_remaining,
                "success_rate": metrics.success_rate,
                "error_rate": metrics.error_rate
            },
            "system": {
                "memory_usage_mb": metrics.memory_usage_mb,
                "cpu_usage_percent": metrics.cpu_usage_percent,
                "active_workers": metrics.active_workers,
                "queue_size": metrics.queue_size
            }
        }
    
    def generate_final_report(self) -> Dict[str, Any]:
        """최종 리포트 생성"""
        if not self._start_time:
            return {"error": "추적이 시작되지 않았습니다"}
        
        end_time = self._end_time or time.time()
        total_time = end_time - self._start_time
        
        return {
            "summary": {
                "total_items": self._total_items,
                "processed_items": self._processed_items,
                "failed_items": self._failed_items,
                "success_rate": (self._processed_items / self._total_items * 100) if self._total_items > 0 else 0.0,
                "total_time_seconds": total_time,
                "average_items_per_second": self._processed_items / total_time if total_time > 0 else 0.0
            },
            "timing": {
                "start_time": self._start_time,
                "end_time": end_time,
                "total_duration": total_time,
                "average_processing_time": (
                    sum(self._processing_times) / len(self._processing_times)
                    if self._processing_times else 0.0
                )
            },
            "metrics_collected": len(self._metrics_history),
            "milestones_reached": list(self._milestone_alerts_sent)
        }
    
    def _get_progress_postfix(self) -> str:
        """진행률 바 포스트픽스 생성"""
        metrics = self.get_current_metrics()
        
        postfix_parts = []
        
        if metrics.items_per_second > 0:
            postfix_parts.append(f"{metrics.items_per_second:.1f} items/s")
        
        if metrics.success_rate > 0:
            postfix_parts.append(f"성공률: {metrics.success_rate:.1f}%")
        
        if metrics.error_rate > 0:
            postfix_parts.append(f"오류율: {metrics.error_rate:.1f}%")
        
        if self._current_stage != "처리 중":
            postfix_parts.append(f"단계: {self._current_stage}")
        
        return " | ".join(postfix_parts)
    
    def _check_milestones(self) -> None:
        """마일스톤 확인 및 알림"""
        if not self.config.enable_milestone_alerts:
            return
        
        if self._total_items == 0:
            return
        
        completion_percentage = (self._processed_items / self._total_items) * 100
        
        for milestone in self.config.milestone_percentages:
            if (completion_percentage >= milestone and 
                milestone not in self._milestone_alerts_sent):
                
                self._milestone_alerts_sent.add(milestone)
                
                # 마일스톤 콜백 실행
                callback = self._milestone_callbacks.get(milestone)
                if callback:
                    try:
                        callback(milestone, self.get_current_metrics())
                    except Exception as e:
                        logger.error(f"마일스톤 콜백 오류 ({milestone}%): {str(e)}")
                
                logger.info(f"마일스톤 달성: {milestone}% 완료")
    
    async def _collect_metrics_loop(self) -> None:
        """메트릭 수집 루프"""
        while self._running:
            try:
                metrics = self.get_current_metrics()
                self._metrics_history.append(metrics)
                
                await asyncio.sleep(self.config.metrics_update_interval)
                
            except Exception as e:
                logger.error(f"메트릭 수집 오류: {str(e)}")
                await asyncio.sleep(self.config.metrics_update_interval * 2)
    
    async def _performance_logging_loop(self) -> None:
        """성능 로깅 루프"""
        while self._running:
            try:
                await asyncio.sleep(self.config.performance_log_interval)
                
                report = self.generate_progress_report()
                logger.info(f"성능 리포트: {json.dumps(report, indent=2, ensure_ascii=False)}")
                
            except Exception as e:
                logger.error(f"성능 로깅 오류: {str(e)}")
                await asyncio.sleep(self.config.performance_log_interval * 2)
    
    def get_eta_formatted(self) -> str:
        """포맷된 ETA 문자열 반환"""
        metrics = self.get_current_metrics()
        eta_seconds = metrics.estimated_time_remaining
        
        if eta_seconds <= 0:
            return "계산 중..."
        
        hours = int(eta_seconds // 3600)
        minutes = int((eta_seconds % 3600) // 60)
        seconds = int(eta_seconds % 60)
        
        if hours > 0:
            return f"{hours}시간 {minutes}분 {seconds}초"
        elif minutes > 0:
            return f"{minutes}분 {seconds}초"
        else:
            return f"{seconds}초"
    
    def get_throughput_stats(self) -> Dict[str, float]:
        """처리량 통계 반환"""
        if len(self._metrics_history) < 2:
            return {"current": 0.0, "average": 0.0, "peak": 0.0, "min": 0.0}
        
        throughputs = [m.items_per_second for m in self._metrics_history if m.items_per_second > 0]
        
        if not throughputs:
            return {"current": 0.0, "average": 0.0, "peak": 0.0, "min": 0.0}
        
        return {
            "current": throughputs[-1],
            "average": sum(throughputs) / len(throughputs),
            "peak": max(throughputs),
            "min": min(throughputs)
        }
    
    @property
    def is_running(self) -> bool:
        """실행 상태 반환"""
        return self._running
    
    @property
    def completion_percentage(self) -> float:
        """완료 백분율 반환"""
        if self._total_items == 0:
            return 0.0
        return (self._processed_items / self._total_items) * 100