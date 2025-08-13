"""
로깅 시스템 유틸리티 함수 테스트

로깅 유틸리티 함수들의 기능을 테스트합니다.
"""

import asyncio
import json
import tempfile
import time
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

from logging_system.utils import (
    LoggingContext, log_execution_time, logging_context,
    log_batch_progress, log_api_interaction, create_monitoring_session,
    close_monitoring_session, format_metrics_for_logging, log_system_status
)
from logging_system import create_logger, create_metrics_collector, create_health_checker


class TestLoggingContext:
    """LoggingContext 테스트"""
    
    def test_logging_context_creation(self):
        """LoggingContext 생성 테스트"""
        logger = create_logger("test_context")
        metrics = create_metrics_collector()
        
        context = LoggingContext(logger, metrics)
        
        assert context.logger == logger
        assert context.metrics == metrics
        assert len(context._context_stack) == 0
    
    def test_context_stack_operations(self):
        """컨텍스트 스택 연산 테스트"""
        logger = create_logger("test_context")
        context = LoggingContext(logger)
        
        # 컨텍스트 추가
        context.push_context({"user_id": "user123", "session_id": "session456"})
        context.push_context({"operation": "data_processing", "batch_id": "batch789"})
        
        # 현재 컨텍스트 확인
        current = context.get_current_context()
        assert current["user_id"] == "user123"
        assert current["session_id"] == "session456"
        assert current["operation"] == "data_processing"
        assert current["batch_id"] == "batch789"
        
        # 컨텍스트 제거
        popped = context.pop_context()
        assert popped["operation"] == "data_processing"
        assert popped["batch_id"] == "batch789"
        
        # 남은 컨텍스트 확인
        current = context.get_current_context()
        assert current["user_id"] == "user123"
        assert current["session_id"] == "session456"
        assert "operation" not in current
        assert "batch_id" not in current
    
    def test_log_with_context(self):
        """컨텍스트와 함께 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_context")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            context = LoggingContext(logger)
            context.push_context({"user_id": "user123", "operation": "test"})
            
            context.log_with_context("info", "테스트 메시지", {"additional": "data"})
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_context.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert parsed["message"] == "테스트 메시지"
            assert parsed["extra_data"]["user_id"] == "user123"
            assert parsed["extra_data"]["operation"] == "test"
            assert parsed["extra_data"]["additional"] == "data"


class TestLogExecutionTime:
    """log_execution_time 데코레이터 테스트"""
    
    def test_successful_execution_logging(self):
        """성공적인 실행 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_execution")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            metrics = create_metrics_collector()
            
            @log_execution_time(logger, metrics, "test_operation")
            def test_function(x, y):
                time.sleep(0.1)  # 실행 시간 시뮬레이션
                return x + y
            
            result = test_function(2, 3)
            assert result == 5
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_execution.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(log_lines) == 2  # 시작, 완료 로그
            
            start_log = log_lines[0]
            assert "작업 시작: test_operation" in start_log["message"]
            assert start_log["extra_data"]["event_type"] == "operation_start"
            
            end_log = log_lines[1]
            assert "작업 완료: test_operation" in end_log["message"]
            assert end_log["extra_data"]["event_type"] == "operation_success"
            assert end_log["extra_data"]["duration_seconds"] >= 0.1
            
            # 메트릭 확인
            processing_metrics = metrics.get_processing_metrics()
            assert processing_metrics["total_processed"] == 1
            assert processing_metrics["success_count"] == 1
    
    def test_failed_execution_logging(self):
        """실패한 실행 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_execution")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            metrics = create_metrics_collector()
            
            @log_execution_time(logger, metrics, "failing_operation")
            def failing_function():
                time.sleep(0.05)
                raise ValueError("테스트 오류")
            
            with pytest.raises(ValueError):
                failing_function()
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_execution.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(log_lines) == 2  # 시작, 실패 로그
            
            error_log = log_lines[1]
            assert "작업 실패: failing_operation" in error_log["message"]
            assert error_log["level"] == "ERROR"
            assert error_log["extra_data"]["event_type"] == "operation_error"
            assert error_log["extra_data"]["error_type"] == "ValueError"
            
            # 메트릭 확인
            processing_metrics = metrics.get_processing_metrics()
            assert processing_metrics["total_processed"] == 1
            assert processing_metrics["error_count"] == 1
    
    def test_execution_logging_with_args(self):
        """인자 포함 실행 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_execution")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            @log_execution_time(logger, include_args=True)
            def function_with_args(a, b, keyword_arg="default"):
                return f"{a}-{b}-{keyword_arg}"
            
            result = function_with_args("hello", "world", keyword_arg="test")
            assert result == "hello-world-test"
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_execution.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            start_log = log_lines[0]
            assert "args" in start_log["extra_data"]
            assert "kwargs" in start_log["extra_data"]
            assert start_log["extra_data"]["kwargs"]["keyword_arg"] == "test"


class TestLoggingContextManager:
    """logging_context 컨텍스트 매니저 테스트"""
    
    def test_successful_context_execution(self):
        """성공적인 컨텍스트 실행 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_context_mgr")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            metrics = create_metrics_collector()
            
            with logging_context(logger, "test_context", {"key": "value"}, metrics) as ctx:
                assert isinstance(ctx, LoggingContext)
                ctx.log_with_context("info", "컨텍스트 내부 로그", {"internal": "data"})
                time.sleep(0.05)
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_context_mgr.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(log_lines) == 3  # 시작, 내부, 완료 로그
            
            start_log = log_lines[0]
            assert "컨텍스트 시작: test_context" in start_log["message"]
            assert start_log["extra_data"]["event_type"] == "context_start"
            assert start_log["extra_data"]["context_data"]["key"] == "value"
            
            end_log = log_lines[2]
            assert "컨텍스트 완료: test_context" in end_log["message"]
            assert end_log["extra_data"]["event_type"] == "context_success"
            assert end_log["extra_data"]["duration_seconds"] >= 0.05
    
    def test_failed_context_execution(self):
        """실패한 컨텍스트 실행 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_context_mgr")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            with pytest.raises(RuntimeError):
                with logging_context(logger, "failing_context") as ctx:
                    time.sleep(0.05)
                    raise RuntimeError("컨텍스트 내부 오류")
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_context_mgr.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(log_lines) == 2  # 시작, 실패 로그
            
            error_log = log_lines[1]
            assert "컨텍스트 실패: failing_context" in error_log["message"]
            assert error_log["level"] == "ERROR"
            assert error_log["extra_data"]["event_type"] == "context_error"
            assert error_log["extra_data"]["error_type"] == "RuntimeError"


class TestBatchProgressLogging:
    """log_batch_progress 함수 테스트"""
    
    def test_batch_progress_logging(self):
        """배치 진행률 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_batch")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            log_batch_progress(
                logger=logger,
                batch_name="test_batch",
                current=50,
                total=100,
                batch_size=10,
                success_count=45,
                error_count=5,
                extra_data={"worker_id": "worker_1"}
            )
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_batch.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert "배치 진행: test_batch (50/100, 50.0%)" in parsed["message"]
            assert parsed["extra_data"]["event_type"] == "batch_progress"
            assert parsed["extra_data"]["current"] == 50
            assert parsed["extra_data"]["total"] == 100
            assert parsed["extra_data"]["progress_percent"] == 50.0
            assert parsed["extra_data"]["success_count"] == 45
            assert parsed["extra_data"]["error_count"] == 5
            assert parsed["extra_data"]["success_rate"] == 0.9  # 45/50
            assert parsed["extra_data"]["worker_id"] == "worker_1"


class TestAPIInteractionLogging:
    """log_api_interaction 데코레이터 테스트"""
    
    @pytest.mark.asyncio
    async def test_async_api_success_logging(self):
        """비동기 API 성공 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_api")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            metrics = create_metrics_collector()
            
            @log_api_interaction(logger, metrics)
            async def async_api_call():
                await asyncio.sleep(0.1)
                return {"status": "success", "data": "test_data"}
            
            result = await async_api_call()
            assert result["status"] == "success"
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_api.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(log_lines) == 2  # 시작, 성공 로그
            
            start_log = log_lines[0]
            assert "API 호출 시작: async_api_call" in start_log["message"]
            assert start_log["extra_data"]["event_type"] == "api_call_start"
            
            success_log = log_lines[1]
            assert "API 호출 성공: async_api_call" in success_log["message"]
            assert success_log["extra_data"]["event_type"] == "api_call_success"
            assert success_log["extra_data"]["duration_seconds"] >= 0.1
            
            # 메트릭 확인
            api_metrics = metrics.get_api_metrics()
            assert api_metrics["total_calls"] == 1
            assert api_metrics["successful_calls"] == 1
    
    def test_sync_api_failure_logging(self):
        """동기 API 실패 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_api")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            metrics = create_metrics_collector()
            
            @log_api_interaction(logger, metrics)
            def failing_api_call():
                time.sleep(0.05)
                raise ConnectionError("API 연결 실패")
            
            with pytest.raises(ConnectionError):
                failing_api_call()
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_api.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(log_lines) == 2  # 시작, 실패 로그
            
            error_log = log_lines[1]
            assert "API 호출 실패: failing_api_call" in error_log["message"]
            assert error_log["level"] == "ERROR"
            assert error_log["extra_data"]["event_type"] == "api_call_error"
            
            # 메트릭 확인
            api_metrics = metrics.get_api_metrics()
            assert api_metrics["total_calls"] == 1
            assert api_metrics["failed_calls"] == 1


class TestMonitoringSession:
    """모니터링 세션 테스트"""
    
    def test_create_and_close_monitoring_session(self):
        """모니터링 세션 생성 및 종료 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            session = create_monitoring_session(
                logger_name="test_session",
                log_level="DEBUG",
                log_dir=temp_dir,
                enable_metrics=True,
                enable_health_check=True,
                metrics_interval=0.1
            )
            
            assert "logger" in session
            assert "metrics" in session
            assert "health_checker" in session
            assert "start_time" in session
            
            # 일부 작업 시뮬레이션
            logger = session["logger"]
            metrics = session["metrics"]
            
            logger.info("세션 테스트 작업")
            metrics.record_processing(0.5, success=True)
            metrics.record_quality(0.85)
            
            time.sleep(0.2)  # 백그라운드 수집 대기
            
            # 세션 종료
            close_monitoring_session(session)
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_session.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            # 시작 및 종료 로그 확인
            start_logs = [log for log in log_lines if "모니터링 세션 시작" in log["message"]]
            end_logs = [log for log in log_lines if "모니터링 세션 종료" in log["message"]]
            
            assert len(start_logs) == 1
            assert len(end_logs) == 1
            
            end_log = end_logs[0]
            assert "session_duration" in end_log["extra_data"]
            assert "final_metrics" in end_log["extra_data"]
    
    def test_monitoring_session_minimal(self):
        """최소 구성 모니터링 세션 테스트"""
        session = create_monitoring_session(
            logger_name="minimal_session",
            enable_metrics=False,
            enable_health_check=False
        )
        
        assert "logger" in session
        assert "metrics" not in session
        assert "health_checker" not in session
        
        close_monitoring_session(session)


class TestMetricsFormatting:
    """메트릭 포맷팅 테스트"""
    
    def test_format_metrics_for_logging_summary(self):
        """메트릭 요약 포맷팅 테스트"""
        metrics_data = {
            "processing": {
                "total_processed": 100,
                "success_rate": 0.95,
                "avg_processing_time": 1.5
            },
            "quality": {
                "avg_quality_score": 0.85,
                "high_quality_count": 80
            },
            "api": {
                "success_rate": 0.98,
                "avg_response_time": 0.5
            },
            "resources": {
                "current_memory_mb": 512.0,
                "current_cpu_percent": 45.5
            }
        }
        
        formatted = format_metrics_for_logging(metrics_data, include_detailed=False)
        
        assert "summary" in formatted
        assert "detailed" not in formatted
        
        summary = formatted["summary"]
        assert summary["total_processed"] == 100
        assert summary["success_rate"] == 0.95
        assert summary["avg_quality_score"] == 0.85
        assert summary["api_success_rate"] == 0.98
        assert summary["current_memory_mb"] == 512.0
        assert summary["current_cpu_percent"] == 45.5
    
    def test_format_metrics_for_logging_detailed(self):
        """메트릭 상세 포맷팅 테스트"""
        metrics_data = {
            "processing": {"total_processed": 100},
            "quality": {"avg_quality_score": 0.85},
            "api": {"success_rate": 0.98},
            "resources": {"current_memory_mb": 512.0}
        }
        
        formatted = format_metrics_for_logging(metrics_data, include_detailed=True)
        
        assert "summary" in formatted
        assert "detailed" in formatted
        
        detailed = formatted["detailed"]
        assert "processing" in detailed
        assert "quality" in detailed
        assert "api" in detailed
        assert "resources" in detailed


class TestSystemStatusLogging:
    """시스템 상태 로깅 테스트"""
    
    @pytest.mark.asyncio
    async def test_log_system_status_complete(self):
        """완전한 시스템 상태 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_status")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            metrics = create_metrics_collector()
            health_checker = create_health_checker()
            
            # 일부 메트릭 기록
            metrics.record_processing(1.0, success=True)
            metrics.record_quality(0.8)
            metrics.record_api_call(0.5, status_code=200)
            
            # 상태 검사 수행 (Mock 사용)
            with patch.object(health_checker, 'check_api_connectivity') as mock_api, \
                 patch.object(health_checker, 'check_qdrant_status') as mock_qdrant, \
                 patch.object(health_checker, 'check_resource_availability') as mock_resources, \
                 patch.object(health_checker, 'check_file_system') as mock_filesystem:
                
                mock_api.return_value = MagicMock(component="openai_api", status="healthy", message="API 정상")
                mock_qdrant.return_value = MagicMock(component="qdrant", status="warning", message="Qdrant 경고")
                mock_resources.return_value = {
                    'memory': MagicMock(component="memory", status="healthy", message="메모리 정상"),
                    'cpu': MagicMock(component="cpu", status="healthy", message="CPU 정상"),
                    'disk': MagicMock(component="disk", status="healthy", message="디스크 정상")
                }
                mock_filesystem.return_value = MagicMock(component="filesystem", status="healthy", message="파일시스템 정상")
                
                await health_checker.perform_full_health_check()
            
            # 시스템 상태 로깅
            log_system_status(logger, metrics, health_checker, include_detailed=True)
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_status.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert "시스템 상태 리포트" in parsed["message"]
            assert parsed["extra_data"]["event_type"] == "system_status"
            
            # 메트릭 정보 확인
            assert "metrics" in parsed["extra_data"]
            metrics_data = parsed["extra_data"]["metrics"]
            assert "summary" in metrics_data
            assert "detailed" in metrics_data
            assert metrics_data["summary"]["total_processed"] == 1
            
            # 상태 정보 확인
            assert "health" in parsed["extra_data"]
            health_data = parsed["extra_data"]["health"]
            assert health_data["overall_status"] == "warning"
            assert health_data["healthy_components"] == 5
            assert health_data["warning_components"] == 1
            assert "components" in health_data
    
    def test_log_system_status_minimal(self):
        """최소 구성 시스템 상태 로깅 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("test_status_minimal")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            log_system_status(logger)
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "test_status_minimal.log"
            content = log_file.read_text(encoding='utf-8')
            parsed = json.loads(content.strip())
            
            assert "시스템 상태 리포트" in parsed["message"]
            assert parsed["extra_data"]["event_type"] == "system_status"
            assert "metrics" not in parsed["extra_data"]
            assert "health" not in parsed["extra_data"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])