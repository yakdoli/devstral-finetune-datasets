"""
구조화된 로깅 시스템

INFO, WARNING, ERROR 레벨 로깅과 컨텍스트 포함 오류 로깅을 제공합니다.
콘솔 및 파일 로깅을 지원하며 로그 로테이션 기능을 포함합니다.
"""

import json
import logging
import logging.handlers
import traceback
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Optional, Union
from dataclasses import dataclass, asdict


class LogLevel(Enum):
    """로그 레벨 열거형"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class LogContext:
    """로그 컨텍스트 데이터 클래스"""
    timestamp: str
    level: str
    logger_name: str
    message: str
    module: Optional[str] = None
    function: Optional[str] = None
    line_number: Optional[int] = None
    extra_data: Optional[Dict[str, Any]] = None
    stack_trace: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환"""
        return {k: v for k, v in asdict(self).items() if v is not None}


class StructuredFormatter(logging.Formatter):
    """구조화된 로그 포맷터"""
    
    def format(self, record: logging.LogRecord) -> str:
        """로그 레코드를 JSON 형태로 포맷팅"""
        log_context = LogContext(
            timestamp=datetime.fromtimestamp(record.created).isoformat(),
            level=record.levelname,
            logger_name=record.name,
            message=record.getMessage(),
            module=getattr(record, 'module', None),
            function=getattr(record, 'funcName', None),
            line_number=getattr(record, 'lineno', None),
            extra_data=getattr(record, 'extra_data', None),
            stack_trace=getattr(record, 'stack_trace', None)
        )
        
        return json.dumps(log_context.to_dict(), ensure_ascii=False, indent=None)


class ConsoleFormatter(logging.Formatter):
    """콘솔용 가독성 좋은 포맷터"""
    
    COLORS = {
        'DEBUG': '\033[36m',    # 청록색
        'INFO': '\033[32m',     # 녹색
        'WARNING': '\033[33m',  # 노란색
        'ERROR': '\033[31m',    # 빨간색
        'CRITICAL': '\033[35m', # 자주색
        'RESET': '\033[0m'      # 리셋
    }
    
    def format(self, record: logging.LogRecord) -> str:
        """콘솔용 컬러 포맷팅"""
        color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        reset = self.COLORS['RESET']
        
        timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        
        base_msg = f"{color}[{record.levelname}]{reset} {timestamp} - {record.getMessage()}"
        
        # 추가 컨텍스트 정보가 있으면 포함
        if hasattr(record, 'extra_data') and record.extra_data:
            extra_str = json.dumps(record.extra_data, ensure_ascii=False, indent=2)
            base_msg += f"\n  Context: {extra_str}"
            
        # 스택 트레이스가 있으면 포함
        if hasattr(record, 'stack_trace') and record.stack_trace:
            base_msg += f"\n  Stack Trace:\n{record.stack_trace}"
            
        return base_msg


class StructuredLogger:
    """구조화된 로거 클래스"""
    
    def __init__(
        self,
        name: str = "unsloth_dataset",
        log_level: str = "INFO",
        log_dir: Optional[Union[str, Path]] = None,
        max_file_size: int = 10 * 1024 * 1024,  # 10MB
        backup_count: int = 5,
        enable_console: bool = True,
        enable_file: bool = True
    ):
        """
        구조화된 로거 초기화
        
        Args:
            name: 로거 이름
            log_level: 로그 레벨
            log_dir: 로그 파일 디렉토리
            max_file_size: 최대 파일 크기 (바이트)
            backup_count: 백업 파일 개수
            enable_console: 콘솔 로깅 활성화
            enable_file: 파일 로깅 활성화
        """
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, log_level.upper()))
        
        # 기존 핸들러 제거
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        
        # 콘솔 핸들러 설정
        if enable_console:
            self._setup_console_handler()
        
        # 파일 핸들러 설정
        if enable_file:
            self._setup_file_handler(log_dir, max_file_size, backup_count)
    
    def _setup_console_handler(self):
        """콘솔 핸들러 설정"""
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(ConsoleFormatter())
        self.logger.addHandler(console_handler)
    
    def _setup_file_handler(self, log_dir: Optional[Union[str, Path]], max_file_size: int, backup_count: int):
        """파일 핸들러 설정 (로테이션 지원)"""
        if log_dir is None:
            log_dir = Path("output/logs")
        else:
            log_dir = Path(log_dir)
        
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"{self.name}.log"
        
        # 로테이팅 파일 핸들러 설정
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=max_file_size,
            backupCount=backup_count,
            encoding='utf-8'
        )
        file_handler.setFormatter(StructuredFormatter())
        self.logger.addHandler(file_handler)
    
    def _log_with_context(
        self,
        level: LogLevel,
        message: str,
        extra_data: Optional[Dict[str, Any]] = None,
        include_stack: bool = False
    ):
        """컨텍스트와 함께 로그 기록"""
        # 호출자 정보 수집
        import inspect
        frame = inspect.currentframe()
        try:
            # 2단계 위의 프레임 (실제 호출자)
            caller_frame = frame.f_back.f_back
            module = caller_frame.f_globals.get('__name__', 'unknown')
            function = caller_frame.f_code.co_name
            line_number = caller_frame.f_lineno
        finally:
            del frame
        
        # 로그 레코드 생성
        record = self.logger.makeRecord(
            name=self.logger.name,
            level=getattr(logging, level.value),
            fn='',
            lno=0,
            msg=message,
            args=(),
            exc_info=None
        )
        
        # 추가 정보 설정
        record.module = module
        record.funcName = function
        record.lineno = line_number
        record.extra_data = extra_data
        
        # 스택 트레이스 포함
        if include_stack:
            record.stack_trace = traceback.format_stack()
        
        self.logger.handle(record)
    
    def debug(self, message: str, extra_data: Optional[Dict[str, Any]] = None):
        """DEBUG 레벨 로그"""
        self._log_with_context(LogLevel.DEBUG, message, extra_data)
    
    def info(self, message: str, extra_data: Optional[Dict[str, Any]] = None):
        """INFO 레벨 로그"""
        self._log_with_context(LogLevel.INFO, message, extra_data)
    
    def warning(self, message: str, extra_data: Optional[Dict[str, Any]] = None):
        """WARNING 레벨 로그"""
        self._log_with_context(LogLevel.WARNING, message, extra_data)
    
    def error(
        self,
        message: str,
        error: Optional[Exception] = None,
        extra_data: Optional[Dict[str, Any]] = None,
        include_stack: bool = True
    ):
        """ERROR 레벨 로그 (스택 트레이스 포함)"""
        if error:
            # 예외 정보를 extra_data에 추가
            error_data = {
                'error_type': type(error).__name__,
                'error_message': str(error),
                'error_traceback': traceback.format_exception(type(error), error, error.__traceback__)
            }
            if extra_data:
                extra_data.update(error_data)
            else:
                extra_data = error_data
        
        self._log_with_context(LogLevel.ERROR, message, extra_data, include_stack)
    
    def critical(
        self,
        message: str,
        error: Optional[Exception] = None,
        extra_data: Optional[Dict[str, Any]] = None,
        include_stack: bool = True
    ):
        """CRITICAL 레벨 로그 (스택 트레이스 포함)"""
        if error:
            # 예외 정보를 extra_data에 추가
            error_data = {
                'error_type': type(error).__name__,
                'error_message': str(error),
                'error_traceback': traceback.format_exception(type(error), error, error.__traceback__)
            }
            if extra_data:
                extra_data.update(error_data)
            else:
                extra_data = error_data
        
        self._log_with_context(LogLevel.CRITICAL, message, extra_data, include_stack)
    
    def log_pipeline_start(self, config: Dict[str, Any]):
        """파이프라인 시작 로그"""
        self.info("파이프라인 시작", {
            'event_type': 'pipeline_start',
            'config': config,
            'timestamp': datetime.now().isoformat()
        })
    
    def log_pipeline_end(self, success: bool, duration: float, stats: Optional[Dict[str, Any]] = None):
        """파이프라인 종료 로그"""
        self.info("파이프라인 완료", {
            'event_type': 'pipeline_end',
            'success': success,
            'duration_seconds': duration,
            'statistics': stats or {},
            'timestamp': datetime.now().isoformat()
        })
    
    def log_processing_progress(self, step: str, progress: float, details: Optional[Dict[str, Any]] = None):
        """처리 진행률 로그"""
        self.info(f"처리 진행: {step} ({progress:.1%})", {
            'event_type': 'processing_progress',
            'step': step,
            'progress_percent': progress * 100,
            'details': details or {},
            'timestamp': datetime.now().isoformat()
        })
    
    def log_quality_results(self, results: Dict[str, Any]):
        """품질 검증 결과 로그"""
        self.info("품질 검증 완료", {
            'event_type': 'quality_validation',
            'results': results,
            'timestamp': datetime.now().isoformat()
        })
    
    def log_error_with_context(self, error: Exception, context: Dict[str, Any]):
        """컨텍스트 포함 오류 로그"""
        self.error(
            f"오류 발생: {str(error)}",
            error=error,
            extra_data={
                'event_type': 'error_with_context',
                'context': context,
                'timestamp': datetime.now().isoformat()
            }
        )
    
    def log_api_call(self, endpoint: str, method: str, status_code: Optional[int] = None, 
                     duration: Optional[float] = None, error: Optional[str] = None):
        """API 호출 로그"""
        log_data = {
            'event_type': 'api_call',
            'endpoint': endpoint,
            'method': method,
            'timestamp': datetime.now().isoformat()
        }
        
        if status_code is not None:
            log_data['status_code'] = status_code
        if duration is not None:
            log_data['duration_ms'] = duration * 1000
        if error:
            log_data['error'] = error
        
        if error or (status_code and status_code >= 400):
            self.error(f"API 호출 실패: {method} {endpoint}", extra_data=log_data)
        else:
            self.info(f"API 호출 성공: {method} {endpoint}", log_data)
    
    def log_batch_processing(self, batch_size: int, total_items: int, processed: int, 
                           success_count: int, error_count: int):
        """배치 처리 로그"""
        self.info(f"배치 처리 상태: {processed}/{total_items} 완료", {
            'event_type': 'batch_processing',
            'batch_size': batch_size,
            'total_items': total_items,
            'processed_items': processed,
            'success_count': success_count,
            'error_count': error_count,
            'progress_percent': (processed / total_items) * 100 if total_items > 0 else 0,
            'timestamp': datetime.now().isoformat()
        })