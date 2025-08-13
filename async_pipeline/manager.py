"""
비동기 파이프라인 관리자

대용량 데이터 처리를 위한 비동기 배치 처리 시스템을 제공합니다.
"""

import asyncio
import logging
import time
from typing import Any, Callable, Dict, List, Optional, TypeVar, Generic, AsyncIterator
from dataclasses import dataclass
from collections import deque
import psutil

from .config import AsyncPipelineConfig

T = TypeVar('T')
R = TypeVar('R')

logger = logging.getLogger(__name__)


@dataclass
class BatchResult:
    """배치 처리 결과"""
    batch_id: str
    items: List[Any]
    results: List[Any]
    errors: List[Exception]
    processing_time: float
    success_count: int
    error_count: int


@dataclass
class PipelineMetrics:
    """파이프라인 성능 메트릭"""
    total_items: int = 0
    processed_items: int = 0
    failed_items: int = 0
    total_batches: int = 0
    completed_batches: int = 0
    failed_batches: int = 0
    total_processing_time: float = 0.0
    average_batch_time: float = 0.0
    throughput: float = 0.0  # items per second
    current_queue_size: int = 0
    peak_queue_size: int = 0
    memory_usage_mb: float = 0.0
    cpu_usage_percent: float = 0.0


class AsyncPipelineManager(Generic[T, R]):
    """비동기 파이프라인 관리자"""
    
    def __init__(self, config: Optional[AsyncPipelineConfig] = None):
        self.config = config or AsyncPipelineConfig()
        self.config.validate()
        
        # 내부 상태
        self._queue: asyncio.Queue = asyncio.Queue(maxsize=self.config.max_queue_size)
        self._semaphore = asyncio.Semaphore(self.config.max_concurrent)
        self._running = False
        self._workers: List[asyncio.Task] = []
        self._metrics = PipelineMetrics()
        self._batch_counter = 0
        
        # 백프레셔 및 성능 저하 상태
        self._current_batch_size = self.config.batch_size
        self._backpressure_active = False
        self._degradation_active = False
        
        # 결과 수집
        self._results: deque = deque()
        self._result_event = asyncio.Event()
        
        logger.info(f"AsyncPipelineManager 초기화 완료: batch_size={self.config.batch_size}, max_concurrent={self.config.max_concurrent}")
    
    async def start(self) -> None:
        """파이프라인 시작"""
        if self._running:
            logger.warning("파이프라인이 이미 실행 중입니다")
            return
        
        self._running = True
        self._metrics = PipelineMetrics()
        
        # 워커 태스크 시작
        for i in range(self.config.max_concurrent):
            worker = asyncio.create_task(self._worker(f"worker-{i}"))
            self._workers.append(worker)
        
        # 모니터링 태스크 시작
        monitor_task = asyncio.create_task(self._monitor_resources())
        self._workers.append(monitor_task)
        
        logger.info(f"파이프라인 시작: {len(self._workers)}개 워커 실행")
    
    async def stop(self) -> None:
        """파이프라인 중지"""
        if not self._running:
            return
        
        self._running = False
        
        # 큐에 종료 신호 추가
        for _ in range(self.config.max_concurrent):
            await self._queue.put(None)
        
        # 모든 워커 완료 대기
        if self._workers:
            await asyncio.gather(*self._workers, return_exceptions=True)
            self._workers.clear()
        
        logger.info("파이프라인 중지 완료")
    
    async def process_batch(
        self,
        items: List[T],
        processor: Callable[[List[T]], R],
        batch_id: Optional[str] = None
    ) -> BatchResult:
        """단일 배치 처리"""
        if not batch_id:
            self._batch_counter += 1
            batch_id = f"batch-{self._batch_counter}"
        
        start_time = time.time()
        results = []
        errors = []
        
        try:
            async with self._semaphore:
                # 백프레셔 확인
                await self._check_backpressure()
                
                # 배치 처리 실행
                if asyncio.iscoroutinefunction(processor):
                    batch_results = await asyncio.wait_for(
                        processor(items),
                        timeout=self.config.batch_timeout
                    )
                else:
                    # 동기 함수를 비동기로 실행
                    batch_results = await asyncio.get_event_loop().run_in_executor(
                        None, processor, items
                    )
                
                if isinstance(batch_results, list):
                    results.extend(batch_results)
                else:
                    results.append(batch_results)
                
        except asyncio.TimeoutError:
            error = TimeoutError(f"배치 {batch_id} 처리 시간 초과")
            errors.append(error)
            logger.error(f"배치 {batch_id} 타임아웃: {len(items)}개 항목")
            
        except Exception as e:
            errors.append(e)
            logger.error(f"배치 {batch_id} 처리 오류: {str(e)}")
        
        processing_time = time.time() - start_time
        
        # 결과 생성
        batch_result = BatchResult(
            batch_id=batch_id,
            items=items,
            results=results,
            errors=errors,
            processing_time=processing_time,
            success_count=len(results),
            error_count=len(errors)
        )
        
        # 메트릭 업데이트
        self._update_metrics(batch_result)
        
        return batch_result
    
    async def process_stream(
        self,
        items: AsyncIterator[T],
        processor: Callable[[List[T]], R]
    ) -> AsyncIterator[BatchResult]:
        """스트림 처리"""
        if not self._running:
            await self.start()
        
        batch = []
        processed_batches = []
        
        async for item in items:
            batch.append(item)
            
            if len(batch) >= self._current_batch_size:
                # 배치 직접 처리
                result = await self.process_batch(batch, processor)
                processed_batches.append(result)
                yield result
                batch = []
        
        # 마지막 배치 처리
        if batch:
            result = await self.process_batch(batch, processor)
            processed_batches.append(result)
            yield result
    
    async def _worker(self, worker_id: str) -> None:
        """워커 태스크"""
        logger.debug(f"워커 {worker_id} 시작")
        
        while self._running:
            try:
                # 큐에서 작업 가져오기
                task = await asyncio.wait_for(
                    self._queue.get(),
                    timeout=1.0
                )
                
                if task is None:  # 종료 신호
                    break
                
                batch, processor = task
                
                # 배치 처리
                result = await self.process_batch(batch, processor)
                
                # 결과 저장
                self._results.append(result)
                self._result_event.set()
                
                # 큐 작업 완료 표시
                self._queue.task_done()
                
            except asyncio.TimeoutError:
                continue  # 타임아웃은 정상적인 상황
            except Exception as e:
                logger.error(f"워커 {worker_id} 오류: {str(e)}")
        
        logger.debug(f"워커 {worker_id} 종료")
    
    async def _monitor_resources(self) -> None:
        """리소스 모니터링"""
        while self._running:
            try:
                # 시스템 리소스 확인
                memory_percent = psutil.virtual_memory().percent
                cpu_percent = psutil.cpu_percent(interval=1)
                
                # 메트릭 업데이트
                process = psutil.Process()
                self._metrics.memory_usage_mb = process.memory_info().rss / 1024 / 1024
                self._metrics.cpu_usage_percent = cpu_percent
                self._metrics.current_queue_size = self._queue.qsize()
                self._metrics.peak_queue_size = max(
                    self._metrics.peak_queue_size,
                    self._metrics.current_queue_size
                )
                
                # 성능 저하 확인
                await self._check_graceful_degradation(memory_percent, cpu_percent)
                
                await asyncio.sleep(5.0)  # 5초마다 모니터링
                
            except Exception as e:
                logger.error(f"리소스 모니터링 오류: {str(e)}")
                await asyncio.sleep(10.0)
    
    async def _check_backpressure(self) -> None:
        """백프레셔 확인 및 처리"""
        if not self.config.enable_backpressure:
            return
        
        queue_usage = self._queue.qsize() / self.config.max_queue_size
        
        if queue_usage > self.config.backpressure_threshold:
            if not self._backpressure_active:
                self._backpressure_active = True
                logger.warning(f"백프레셔 활성화: 큐 사용률 {queue_usage:.2%}")
            
            # 백프레셔 지연
            await asyncio.sleep(self.config.backpressure_delay)
        else:
            if self._backpressure_active:
                self._backpressure_active = False
                logger.info("백프레셔 비활성화")
    
    async def _check_graceful_degradation(self, memory_percent: float, cpu_percent: float) -> None:
        """우아한 성능 저하 확인 및 처리"""
        if not self.config.enable_graceful_degradation:
            return
        
        resource_usage = max(memory_percent, cpu_percent) / 100.0
        
        if resource_usage > self.config.degradation_threshold:
            if not self._degradation_active:
                self._degradation_active = True
                
                # 배치 크기 감소
                new_batch_size = max(
                    self.config.min_batch_size,
                    int(self._current_batch_size * self.config.degradation_factor)
                )
                
                if new_batch_size != self._current_batch_size:
                    self._current_batch_size = new_batch_size
                    logger.warning(
                        f"성능 저하 모드 활성화: 리소스 사용률 {resource_usage:.2%}, "
                        f"배치 크기 {self._current_batch_size}로 감소"
                    )
        else:
            if self._degradation_active:
                self._degradation_active = False
                self._current_batch_size = self.config.batch_size
                logger.info(f"성능 저하 모드 비활성화: 배치 크기 {self._current_batch_size}로 복원")
    
    def _update_metrics(self, batch_result: BatchResult) -> None:
        """메트릭 업데이트"""
        self._metrics.total_batches += 1
        self._metrics.completed_batches += 1
        self._metrics.total_items += len(batch_result.items)
        self._metrics.processed_items += batch_result.success_count
        self._metrics.failed_items += batch_result.error_count
        self._metrics.total_processing_time += batch_result.processing_time
        
        if self._metrics.completed_batches > 0:
            self._metrics.average_batch_time = (
                self._metrics.total_processing_time / self._metrics.completed_batches
            )
        
        if self._metrics.total_processing_time > 0:
            self._metrics.throughput = (
                self._metrics.processed_items / self._metrics.total_processing_time
            )
        
        if batch_result.error_count > 0:
            self._metrics.failed_batches += 1
    
    def get_metrics(self) -> PipelineMetrics:
        """현재 메트릭 반환"""
        return self._metrics
    
    def get_current_batch_size(self) -> int:
        """현재 배치 크기 반환"""
        return self._current_batch_size
    
    def is_backpressure_active(self) -> bool:
        """백프레셔 활성 상태 반환"""
        return self._backpressure_active
    
    def is_degradation_active(self) -> bool:
        """성능 저하 모드 활성 상태 반환"""
        return self._degradation_active