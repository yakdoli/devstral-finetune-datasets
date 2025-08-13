"""
구조화된 로깅 시스템 단위 테스트

로깅 레벨, 포맷, 파일 로깅, 로테이션 등의 기능을 테스트합니다.
"""

import json
import logging
import tempfile
import time
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

from logging_system.structured_logger import (
    StructuredLogger, LogLevel, LogContext, 
    StructuredFormatter, ConsoleFormatter
)


class TestLogContext:
    """LogContext 테스트"""
    
    def test_log_context_creation(self):
        """LogContext 생성 테스트"""
        context = LogContext(
            timestamp="2024-01-01T12:00:00",
            level="INFO",
            logger_name="test_logger",
            message="테스트 메시지",
            module="test_module",
            function="test_function",
            line_number=42
        )
        
        assert context.timestamp == "2024-01-01T12:00:00"
        assert context.level == "INFO"
        assert context.logger_name == "test_logger"
        assert context.message == "테스트 메시지"
        assert context.module == "test_module"
        assert context.function == "test_function"
        assert context.line_number == 42
    
    def test_log_context_to_dict(self):
        """LogContext 딕셔너리 변환 테스트"""
        context = LogContext(
            timestamp="2024-01-01T12:00:00",
            level="INFO",
            logger_name="test_logger",
            message="테스트 메시지",
            extra_data={"key": "value"}
        )
        
        result = context.to_dict()
        
        assert result["timestamp"] == "2024-01-01T12:00:00"
        assert result["level"] == "INFO"
        assert result["logger_name"] == "test_logger"
        assert result["message"] == "테스트 메시지"
        assert result["extra_data"] == {"key": "value"}
        
        # None 값은 제외되어야 함
        assert "module" not in result
        assert "function" not in result


class TestStructuredFormatter:
    """StructuredFormatter 테스트"""
    
    def test_structured_formatter_basic(self):
        """기본 구조화된 포맷팅 테스트"""
        formatter = StructuredFormatter()
        
        # 로그 레코드 생성
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="",
            lineno=0,
            msg="테스트 메시지",
            args=(),
            exc_info=None
        )
        
        result = formatter.format(record)
        parsed = json.loads(result)
        
        assert parsed["level"] == "INFO"
        assert parsed["logger_name"] == "test_logger"
        assert parsed["message"] == "테스트 메시지"
        assert "timestamp" in parsed
    
    def test_structured_formatter_with_extra_data(self):
        """추가 데이터가 있는 구조화된 포맷팅 테스트"""
        formatter = StructuredFormatter()
        
        record = logging.LogRecord(
            name="test_logger",
            level=logging.ERROR,
            pathname="",
            lineno=0,
            msg="오류 메시지",
            args=(),
            exc_info=None
        )
        record.extra_data = {"error_code": 500, "user_id": "test_user"}
        record.stack_trace = "Stack trace here"
        
        result = formatter.format(record)
        parsed = json.loads(result)
        
        assert parsed["level"] == "ERROR"
        assert parsed["message"] == "오류 메시지"
        assert parsed["extra_data"]["error_code"] == 500
        assert parsed["extra_data"]["user_id"] == "test_user"
        assert parsed["stack_trace"] == "Stack trace here"


class TestConsoleFormatter:
    """ConsoleFormatter 테스트"""
    
    def test_console_formatter_basic(self):
        """기본 콘솔 포맷팅 테스트"""
        formatter = ConsoleFormatter()
        
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="",
            lineno=0,
            msg="테스트 메시지",
            args=(),
            exc_info=None
        )
        
        result = formatter.format(record)
        
        assert "INFO" in result
        assert "테스트 메시지" in result
        assert "\033[32m" in result  # 녹색 컬러 코드
        assert "\033[0m" in result   # 리셋 코드
    
    def test_console_formatter_with_extra_data(self):
        """추가 데이터가 있는 콘솔 포맷팅 테스트"""
        formatter = ConsoleFormatter()
        
        record = logging.LogRecord(
            name="test_logger",
            level=logging.WARNING,
            pathname="",
            lineno=0,
            msg="경고 메시지",
            args=(),
            exc_info=None
        )
        record.extra_data = {"warning_type": "performance"}
        
        result = formatter.format(record)
        
        assert "WARNING" in result
        assert "경고 메시지" in result
        assert "Context:" in result
        assert "performance" in result
        assert "\033[33m" in result  # 노란색 컬러 코드


class TestStructuredLogger:
    """StructuredLogger 테스트"""
    
    def test_logger_initialization(self):
        """로거 초기화 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_level="DEBUG",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            assert logger.name == "test_logger"
            assert logger.logger.level == logging.DEBUG
            
            # 로그 파일이 생성되었는지 확인
            log_file = Path(temp_dir) / "test_logger.log"
            assert log_file.parent.exists()
    
    def test_info_logging(self):
        """INFO 레벨 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            logger.info("테스트 정보 메시지", {"key": "value"})
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_logger.log"
            assert log_file.exists()
            
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert parsed["level"] == "INFO"
            assert parsed["message"] == "테스트 정보 메시지"
            assert parsed["extra_data"]["key"] == "value"
    
    def test_error_logging_with_exception(self):
        """예외가 있는 ERROR 레벨 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            try:
                raise ValueError("테스트 오류")
            except ValueError as e:
                logger.error("오류 발생", error=e, extra_data={"context": "test"})
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_logger.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert parsed["level"] == "ERROR"
            assert parsed["message"] == "오류 발생"
            assert parsed["extra_data"]["error_type"] == "ValueError"
            assert parsed["extra_data"]["error_message"] == "테스트 오류"
            assert parsed["extra_data"]["context"] == "test"
            assert "error_traceback" in parsed["extra_data"]
    
    def test_warning_logging(self):
        """WARNING 레벨 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            logger.warning("경고 메시지", {"warning_code": "W001"})
            
            log_file = Path(temp_dir) / "test_logger.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert parsed["level"] == "WARNING"
            assert parsed["message"] == "경고 메시지"
            assert parsed["extra_data"]["warning_code"] == "W001"
    
    def test_debug_logging(self):
        """DEBUG 레벨 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_level="DEBUG",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            logger.debug("디버그 메시지", {"debug_info": "상세 정보"})
            
            log_file = Path(temp_dir) / "test_logger.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert parsed["level"] == "DEBUG"
            assert parsed["message"] == "디버그 메시지"
            assert parsed["extra_data"]["debug_info"] == "상세 정보"
    
    def test_critical_logging(self):
        """CRITICAL 레벨 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            logger.critical("치명적 오류", extra_data={"severity": "high"})
            
            log_file = Path(temp_dir) / "test_logger.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert parsed["level"] == "CRITICAL"
            assert parsed["message"] == "치명적 오류"
            assert parsed["extra_data"]["severity"] == "high"
    
    def test_log_level_filtering(self):
        """로그 레벨 필터링 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_level="WARNING",  # WARNING 이상만 기록
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            logger.debug("디버그 메시지")  # 기록되지 않음
            logger.info("정보 메시지")    # 기록되지 않음
            logger.warning("경고 메시지")  # 기록됨
            logger.error("오류 메시지")   # 기록됨
            
            log_file = Path(temp_dir) / "test_logger.log"
            content = log_file.read_text(encoding='utf-8')
            lines = [line for line in content.strip().split('\n') if line]
            
            assert len(lines) == 2  # WARNING과 ERROR만 기록됨
            
            warning_log = json.loads(lines[0])
            error_log = json.loads(lines[1])
            
            assert warning_log["level"] == "WARNING"
            assert warning_log["message"] == "경고 메시지"
            assert error_log["level"] == "ERROR"
            assert error_log["message"] == "오류 메시지"
    
    def test_pipeline_logging_methods(self):
        """파이프라인 전용 로깅 메서드 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            # 파이프라인 시작 로그
            config = {"batch_size": 16, "model": "test_model"}
            logger.log_pipeline_start(config)
            
            # 진행률 로그
            logger.log_processing_progress("데이터 처리", 0.5, {"processed": 50, "total": 100})
            
            # 품질 결과 로그
            quality_results = {"avg_score": 0.85, "total_items": 100}
            logger.log_quality_results(quality_results)
            
            # 파이프라인 종료 로그
            stats = {"processed": 100, "success": 95, "errors": 5}
            logger.log_pipeline_end(True, 120.5, stats)
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_logger.log"
            content = log_file.read_text(encoding='utf-8')
            lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(lines) == 4
            
            # 파이프라인 시작 로그 확인
            start_log = lines[0]
            assert start_log["extra_data"]["event_type"] == "pipeline_start"
            assert start_log["extra_data"]["config"]["batch_size"] == 16
            
            # 진행률 로그 확인
            progress_log = lines[1]
            assert progress_log["extra_data"]["event_type"] == "processing_progress"
            assert progress_log["extra_data"]["progress_percent"] == 50.0
            
            # 품질 결과 로그 확인
            quality_log = lines[2]
            assert quality_log["extra_data"]["event_type"] == "quality_validation"
            assert quality_log["extra_data"]["results"]["avg_score"] == 0.85
            
            # 파이프라인 종료 로그 확인
            end_log = lines[3]
            assert end_log["extra_data"]["event_type"] == "pipeline_end"
            assert end_log["extra_data"]["success"] is True
            assert end_log["extra_data"]["duration_seconds"] == 120.5
    
    def test_api_call_logging(self):
        """API 호출 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            # 성공적인 API 호출
            logger.log_api_call("http://api.example.com/test", "GET", 200, 0.5)
            
            # 실패한 API 호출
            logger.log_api_call("http://api.example.com/error", "POST", 500, 1.2, "Internal Server Error")
            
            log_file = Path(temp_dir) / "test_logger.log"
            content = log_file.read_text(encoding='utf-8')
            lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(lines) == 2
            
            # 성공 로그 확인
            success_log = lines[0]
            assert success_log["level"] == "INFO"
            assert success_log["extra_data"]["status_code"] == 200
            assert success_log["extra_data"]["duration_ms"] == 500.0
            
            # 실패 로그 확인
            error_log = lines[1]
            assert error_log["level"] == "ERROR"
            assert error_log["extra_data"]["status_code"] == 500
            assert error_log["extra_data"]["error"] == "Internal Server Error"
    
    def test_batch_processing_logging(self):
        """배치 처리 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = StructuredLogger(
                name="test_logger",
                log_dir=temp_dir,
                enable_console=False,
                enable_file=True
            )
            
            logger.log_batch_processing(
                batch_size=16,
                total_items=100,
                processed=50,
                success_count=45,
                error_count=5
            )
            
            log_file = Path(temp_dir) / "test_logger.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert parsed["level"] == "INFO"
            assert parsed["extra_data"]["event_type"] == "batch_processing"
            assert parsed["extra_data"]["batch_size"] == 16
            assert parsed["extra_data"]["total_items"] == 100
            assert parsed["extra_data"]["processed_items"] == 50
            assert parsed["extra_data"]["success_count"] == 45
            assert parsed["extra_data"]["error_count"] == 5
            assert parsed["extra_data"]["progress_percent"] == 50.0
    
    def test_file_rotation(self):
        """파일 로테이션 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 작은 파일 크기로 로테이션 테스트
            logger = StructuredLogger(
                name="test_logger",
                log_dir=temp_dir,
                max_file_size=1024,  # 1KB
                backup_count=2,
                enable_console=False,
                enable_file=True
            )
            
            # 많은 로그 메시지 생성하여 로테이션 유발
            for i in range(100):
                logger.info(f"로테이션 테스트 메시지 {i:03d}", {"iteration": i, "data": "x" * 50})
            
            # 로그 파일들이 생성되었는지 확인
            log_files = list(Path(temp_dir).glob("test_logger.log*"))
            assert len(log_files) > 1  # 원본 파일 + 백업 파일들
    
    def test_console_and_file_logging(self):
        """콘솔과 파일 동시 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch('sys.stdout') as mock_stdout:
                logger = StructuredLogger(
                    name="test_logger",
                    log_dir=temp_dir,
                    enable_console=True,
                    enable_file=True
                )
                
                logger.info("동시 로깅 테스트")
                
                # 파일에 기록되었는지 확인
                log_file = Path(temp_dir) / "test_logger.log"
                assert log_file.exists()
                
                file_content = log_file.read_text(encoding='utf-8')
                file_parsed = json.loads(file_content.strip())
                assert file_parsed["message"] == "동시 로깅 테스트"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])