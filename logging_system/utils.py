"""
로깅 시스템 유틸리티 함수

로깅 시스템과 다른 모듈 간의 통합을 위한 헬퍼 함수들을 제공합니다.
"""

import time
import functools
from typing import Any, Dict, Optional, Callable, Union
from contextlib import contextmanager
from datetime import datetime

from .structured_logger import StructuredLogger
from .metrics_collector import MetricsCollector
from .health_checker import HealthChecker


class LoggingContext:
    """로깅 컨텍스트 관리자"""
    
    def __init__(self, logger: StructuredLogger, metrics: Optional[MetricsCollector] = None):
        self.logger = logger
        self.metrics = metrics
        self._context_stack = []
    
    def push_context(self, context: Dict[str, Any]):
        """컨텍스트 스택에 추가"""
        self._context_stack.append(context)
    
    def pop_context(self) -> Optional[Dict[str, Any]]:
        """컨텍스트 스택에서 제거"""
        return self._context_stack.pop() if self._context_stack else None
    
    def get_current_context(self) -> Dict[str, Any]:
        """현재 컨텍스트 반환"""
        merged_context = {}
        for context in self._context_stack:
            merged_context.update(context)
        return merged_context
    
    def log_with_context(self, level: str, message: str, extra_data: Optional[Dict[str, Any]] = None):
        """컨텍스트와 함께 로그 기록"""
        current_context = self.get_current_context()
        if extra_data:
            current_context.update(extra_data)
        
        log_method = getattr(self.logger, level.lower())
        log_method(message, current_context)


def log_execution_time(logger: StructuredLogger, 
                      metrics: Optional[MetricsCollector] = None,
                      operation_name: Optional[str] = None,
                      log_level: str = "info",
                      include_args: bool = False):
    """
    함수 실행 시간을 로깅하는 데코레이터
    
    Args:
        logger: 구조화된 로거
        metrics: 메트릭 수집기 (선택사항)
        operation_name: 작업 이름 (기본값: 함수명)
        log_level: 로그 레벨
        include_args: 함수 인자 포함 여부
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            op_name = operation_name or func.__name__
            start_time = time.time()
            
            # 시작 로그
            log_data = {
                "operation": op_name,
                "event_type": "operation_start",
                "timestamp": datetime.now().isoformat()
            }
            
            if include_args:
                log_data["args"] = str(args)[:200]  # 최대 200자
                log_data["kwargs"] = {k: str(v)[:100] for k, v in kwargs.items()}
            
            log_method = getattr(logger, log_level.lower())
            log_method(f"작업 시작: {op_name}", log_data)
            
            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time
                
                # 성공 로그
                success_data = {
                    "operation": op_name,
                    "event_type": "operation_success",
                    "duration_seconds": duration,
                    "timestamp": datetime.now().isoformat()
                }
                
                log_method(f"작업 완료: {op_name} ({duration:.3f}초)", success_data)
                
                # 메트릭 기록
                if metrics:
                    metrics.record_processing(duration, success=True)
                
                return result
                
            except Exception as e:
                duration = time.time() - start_time
                
                # 실패 로그
                error_data = {
                    "operation": op_name,
                    "event_type": "operation_error",
                    "duration_seconds": duration,
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                    "timestamp": datetime.now().isoformat()
                }
                
                logger.error(f"작업 실패: {op_name} ({duration:.3f}초)", error=e, extra_data=error_data)
                
                # 메트릭 기록
                if metrics:
                    metrics.record_processing(duration, success=False)
                
                raise
        
        return wrapper
    return decorator


@contextmanager
def logging_context(logger: StructuredLogger, 
                   context_name: str, 
                   context_data: Optional[Dict[str, Any]] = None,
                   metrics: Optional[MetricsCollector] = None):
    """
    로깅 컨텍스트 관리자
    
    Args:
        logger: 구조화된 로거
        context_name: 컨텍스트 이름
        context_data: 컨텍스트 데이터
        metrics: 메트릭 수집기 (선택사항)
    """
    start_time = time.time()
    context_id = f"{context_name}_{int(start_time * 1000)}"
    
    # 컨텍스트 시작 로그
    start_data = {
        "context_id": context_id,
        "context_name": context_name,
        "event_type": "context_start",
        "timestamp": datetime.now().isoformat()
    }
    
    if context_data:
        start_data["context_data"] = context_data
    
    logger.info(f"컨텍스트 시작: {context_name}", start_data)
    
    try:
        yield LoggingContext(logger, metrics)
        
        # 컨텍스트 성공 종료 로그
        duration = time.time() - start_time
        success_data = {
            "context_id": context_id,
            "context_name": context_name,
            "event_type": "context_success",
            "duration_seconds": duration,
            "timestamp": datetime.now().isoformat()
        }
        
        logger.info(f"컨텍스트 완료: {context_name} ({duration:.3f}초)", success_data)
        
    except Exception as e:
        # 컨텍스트 실패 종료 로그
        duration = time.time() - start_time
        error_data = {
            "context_id": context_id,
            "context_name": context_name,
            "event_type": "context_error",
            "duration_seconds": duration,
            "error_type": type(e).__name__,
            "error_message": str(e),
            "timestamp": datetime.now().isoformat()
        }
        
        logger.error(f"컨텍스트 실패: {context_name} ({duration:.3f}초)", error=e, extra_data=error_data)
        raise


def log_batch_progress(logger: StructuredLogger,
                      batch_name: str,
                      current: int,
                      total: int,
                      batch_size: int,
                      success_count: int,
                      error_count: int,
                      extra_data: Optional[Dict[str, Any]] = None):
    """
    배치 처리 진행률 로깅
    
    Args:
        logger: 구조화된 로거
        batch_name: 배치 이름
        current: 현재 처리된 항목 수
        total: 전체 항목 수
        batch_size: 배치 크기
        success_count: 성공 개수
        error_count: 오류 개수
        extra_data: 추가 데이터
    """
    progress_percent = (current / total) * 100 if total > 0 else 0
    
    log_data = {
        "batch_name": batch_name,
        "event_type": "batch_progress",
        "current": current,
        "total": total,
        "batch_size": batch_size,
        "progress_percent": progress_percent,
        "success_count": success_count,
        "error_count": error_count,
        "success_rate": success_count / max(current, 1),
        "timestamp": datetime.now().isoformat()
    }
    
    if extra_data:
        log_data.update(extra_data)
    
    logger.info(f"배치 진행: {batch_name} ({current}/{total}, {progress_percent:.1f}%)", log_data)


def log_api_interaction(logger: StructuredLogger,
                       metrics: Optional[MetricsCollector] = None):
    """
    API 상호작용 로깅 데코레이터
    
    Args:
        logger: 구조화된 로거
        metrics: 메트릭 수집기 (선택사항)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            
            # API 호출 시작 로그
            logger.info(f"API 호출 시작: {func.__name__}", {
                "function": func.__name__,
                "event_type": "api_call_start",
                "timestamp": datetime.now().isoformat()
            })
            
            try:
                result = await func(*args, **kwargs)
                duration = time.time() - start_time
                
                # 성공 로그
                logger.info(f"API 호출 성공: {func.__name__} ({duration:.3f}초)", {
                    "function": func.__name__,
                    "event_type": "api_call_success",
                    "duration_seconds": duration,
                    "timestamp": datetime.now().isoformat()
                })
                
                # 메트릭 기록
                if metrics:
                    metrics.record_api_call(duration, status_code=200)
                
                return result
                
            except Exception as e:
                duration = time.time() - start_time
                
                # 실패 로그
                logger.error(f"API 호출 실패: {func.__name__} ({duration:.3f}초)", error=e, extra_data={
                    "function": func.__name__,
                    "event_type": "api_call_error",
                    "duration_seconds": duration,
                    "timestamp": datetime.now().isoformat()
                })
                
                # 메트릭 기록
                if metrics:
                    metrics.record_api_call(duration, error_type=type(e).__name__)
                
                raise
        
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.time()
            
            # API 호출 시작 로그
            logger.info(f"API 호출 시작: {func.__name__}", {
                "function": func.__name__,
                "event_type": "api_call_start",
                "timestamp": datetime.now().isoformat()
            })
            
            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time
                
                # 성공 로그
                logger.info(f"API 호출 성공: {func.__name__} ({duration:.3f}초)", {
                    "function": func.__name__,
                    "event_type": "api_call_success",
                    "duration_seconds": duration,
                    "timestamp": datetime.now().isoformat()
                })
                
                # 메트릭 기록
                if metrics:
                    metrics.record_api_call(duration, status_code=200)
                
                return result
                
            except Exception as e:
                duration = time.time() - start_time
                
                # 실패 로그
                logger.error(f"API 호출 실패: {func.__name__} ({duration:.3f}초)", error=e, extra_data={
                    "function": func.__name__,
                    "event_type": "api_call_error",
                    "duration_seconds": duration,
                    "timestamp": datetime.now().isoformat()
                })
                
                # 메트릭 기록
                if metrics:
                    metrics.record_api_call(duration, error_type=type(e).__name__)
                
                raise
        
        # 비동기 함수인지 확인
        import asyncio
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    
    return decorator


def create_monitoring_session(logger_name: str = "monitoring_session",
                            log_level: str = "INFO",
                            log_dir: Optional[str] = None,
                            enable_metrics: bool = True,
                            enable_health_check: bool = True,
                            metrics_interval: float = 5.0) -> Dict[str, Any]:
    """
    통합 모니터링 세션 생성
    
    Args:
        logger_name: 로거 이름
        log_level: 로그 레벨
        log_dir: 로그 디렉토리
        enable_metrics: 메트릭 수집 활성화
        enable_health_check: 상태 검사 활성화
        metrics_interval: 메트릭 수집 간격
    
    Returns:
        모니터링 컴포넌트들을 포함한 딕셔너리
    """
    # 로거 생성
    logger = StructuredLogger(
        name=logger_name,
        log_level=log_level,
        log_dir=log_dir
    )
    
    session = {
        "logger": logger,
        "start_time": time.time()
    }
    
    # 메트릭 수집기 생성
    if enable_metrics:
        metrics = MetricsCollector(collection_interval=metrics_interval)
        metrics.start_collection()
        session["metrics"] = metrics
    
    # 상태 검사기 생성
    if enable_health_check:
        health_checker = HealthChecker()
        session["health_checker"] = health_checker
    
    # 세션 시작 로그
    logger.info("모니터링 세션 시작", {
        "session_id": logger_name,
        "log_level": log_level,
        "metrics_enabled": enable_metrics,
        "health_check_enabled": enable_health_check,
        "timestamp": datetime.now().isoformat()
    })
    
    return session


def close_monitoring_session(session: Dict[str, Any]):
    """
    모니터링 세션 종료
    
    Args:
        session: create_monitoring_session으로 생성된 세션
    """
    logger = session.get("logger")
    metrics = session.get("metrics")
    start_time = session.get("start_time", time.time())
    
    duration = time.time() - start_time
    
    # 최종 메트릭 수집
    final_stats = {}
    if metrics:
        metrics.stop_collection()
        final_stats = metrics.get_all_metrics()
    
    # 세션 종료 로그
    if logger:
        logger.info("모니터링 세션 종료", {
            "session_duration": duration,
            "final_metrics": final_stats.get("processing", {}) if final_stats else {},
            "timestamp": datetime.now().isoformat()
        })


def format_metrics_for_logging(metrics: Dict[str, Any], 
                              include_detailed: bool = False) -> Dict[str, Any]:
    """
    로깅을 위한 메트릭 포맷팅
    
    Args:
        metrics: 메트릭 데이터
        include_detailed: 상세 정보 포함 여부
    
    Returns:
        포맷팅된 메트릭 데이터
    """
    formatted = {
        "summary": {
            "total_processed": metrics.get("processing", {}).get("total_processed", 0),
            "success_rate": metrics.get("processing", {}).get("success_rate", 0.0),
            "avg_quality_score": metrics.get("quality", {}).get("avg_quality_score", 0.0),
            "api_success_rate": metrics.get("api", {}).get("success_rate", 0.0),
            "current_memory_mb": metrics.get("resources", {}).get("current_memory_mb", 0.0),
            "current_cpu_percent": metrics.get("resources", {}).get("current_cpu_percent", 0.0)
        }
    }
    
    if include_detailed:
        formatted["detailed"] = {
            "processing": metrics.get("processing", {}),
            "quality": metrics.get("quality", {}),
            "api": metrics.get("api", {}),
            "resources": metrics.get("resources", {})
        }
    
    return formatted


def log_system_status(logger: StructuredLogger,
                     metrics: Optional[MetricsCollector] = None,
                     health_checker: Optional[HealthChecker] = None,
                     include_detailed: bool = False):
    """
    시스템 상태 종합 로깅
    
    Args:
        logger: 구조화된 로거
        metrics: 메트릭 수집기
        health_checker: 상태 검사기
        include_detailed: 상세 정보 포함 여부
    """
    status_data = {
        "event_type": "system_status",
        "timestamp": datetime.now().isoformat()
    }
    
    # 메트릭 정보 추가
    if metrics:
        all_metrics = metrics.get_all_metrics()
        status_data["metrics"] = format_metrics_for_logging(all_metrics, include_detailed)
    
    # 상태 검사 정보 추가
    if health_checker and health_checker.check_history:
        latest_health = health_checker.check_history[-1]
        status_data["health"] = {
            "overall_status": latest_health.overall_status,
            "healthy_components": sum(1 for c in latest_health.components if c.status == "healthy"),
            "warning_components": sum(1 for c in latest_health.components if c.status == "warning"),
            "critical_components": sum(1 for c in latest_health.components if c.status == "critical")
        }
        
        if include_detailed:
            status_data["health"]["components"] = {
                c.component: {"status": c.status, "message": c.message}
                for c in latest_health.components
            }
    
    logger.info("시스템 상태 리포트", status_data)