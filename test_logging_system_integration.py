"""
로깅 및 모니터링 시스템 통합 테스트

구조화된 로깅, 메트릭 수집, 상태 모니터링의 통합 기능을 테스트합니다.
"""

import asyncio
import tempfile
import time
from pathlib import Path
from unittest.mock import patch, MagicMock, AsyncMock
import pytest
import json

from logging_system import (
    create_logger, create_metrics_collector, create_health_checker,
    StructuredLogger, MetricsCollector, HealthChecker
)


class TestLoggingSystemIntegration:
    """로깅 시스템 통합 테스트"""
    
    def test_factory_functions(self):
        """팩토리 함수 테스트"""
        # 로거 생성
        logger = create_logger("test_logger", "DEBUG")
        assert isinstance(logger, StructuredLogger)
        assert logger.name == "test_logger"
        
        # 메트릭 수집기 생성
        collector = create_metrics_collector()
        assert isinstance(collector, MetricsCollector)
        
        # 상태 검사기 생성
        checker = create_health_checker()
        assert isinstance(checker, HealthChecker)
    
    def test_logger_and_metrics_integration(self):
        """로거와 메트릭 수집기 통합 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("integration_test", "INFO")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            collector = create_metrics_collector()
            
            # 처리 시뮬레이션
            start_time = time.time()
            
            logger.info("처리 시작", {"batch_id": "batch_001"})
            
            # 성공적인 처리
            processing_time = 1.5
            collector.record_processing(processing_time, success=True)
            collector.record_quality(0.85, is_duplicate=False, has_safety_violation=False)
            
            logger.info("항목 처리 완료", {
                "processing_time": processing_time,
                "quality_score": 0.85,
                "success": True
            })
            
            # 실패한 처리
            try:
                raise ValueError("처리 오류 시뮬레이션")
            except ValueError as e:
                processing_time = 0.8
                collector.record_processing(processing_time, success=False)
                logger.error("처리 실패", error=e, extra_data={
                    "processing_time": processing_time,
                    "batch_id": "batch_001"
                })
            
            # API 호출 시뮬레이션
            api_response_time = 0.5
            collector.record_api_call(api_response_time, status_code=200)
            logger.log_api_call("http://api.example.com/test", "POST", 200, api_response_time)
            
            total_time = time.time() - start_time
            logger.info("처리 완료", {"total_time": total_time})
            
            # 메트릭 확인
            processing_metrics = collector.get_processing_metrics()
            assert processing_metrics['total_processed'] == 2
            assert processing_metrics['success_count'] == 1
            assert processing_metrics['error_count'] == 1
            
            quality_metrics = collector.get_quality_metrics()
            assert quality_metrics['total_items'] == 1
            assert quality_metrics['high_quality_count'] == 1
            
            api_metrics = collector.get_api_metrics()
            assert api_metrics['total_calls'] == 1
            assert api_metrics['successful_calls'] == 1
            
            # 로그 파일 확인
            log_file = Path(temp_dir) / "integration_test.log"
            assert log_file.exists()
            
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            assert len(log_lines) >= 4  # 시작, 완료, 실패, API 호출 로그
            
            # 각 로그 타입 확인
            start_log = log_lines[0]
            assert start_log['message'] == "처리 시작"
            assert start_log['extra_data']['batch_id'] == "batch_001"
            
            # 오류 로그 확인
            error_logs = [log for log in log_lines if log['level'] == 'ERROR']
            assert len(error_logs) >= 1
            error_log = error_logs[0]
            assert "처리 실패" in error_log['message']
            assert error_log['extra_data']['error_type'] == "ValueError"
    
    @pytest.mark.asyncio
    async def test_health_checker_and_logger_integration(self):
        """상태 검사기와 로거 통합 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("health_integration", "INFO")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            checker = create_health_checker()
            
            # 상태 검사 시작 로그
            logger.info("시스템 상태 검사 시작")
            
            # Mock을 사용한 상태 검사
            with patch.object(checker, 'check_api_connectivity') as mock_api, \
                 patch.object(checker, 'check_qdrant_status') as mock_qdrant, \
                 patch.object(checker, 'check_resource_availability') as mock_resources, \
                 patch.object(checker, 'check_file_system') as mock_filesystem:
                
                # Mock 설정
                mock_api.return_value = MagicMock(
                    component="openai_api", status="healthy", message="API 정상",
                    details={"status_code": 200}, response_time_ms=150.0
                )
                mock_qdrant.return_value = MagicMock(
                    component="qdrant", status="warning", message="컬렉션 누락",
                    details={"target_collection_exists": False}, response_time_ms=200.0
                )
                mock_resources.return_value = {
                    'memory': MagicMock(component="memory", status="healthy", message="메모리 정상"),
                    'cpu': MagicMock(component="cpu", status="healthy", message="CPU 정상"),
                    'disk': MagicMock(component="disk", status="healthy", message="디스크 정상")
                }
                mock_filesystem.return_value = MagicMock(
                    component="filesystem", status="healthy", message="파일시스템 정상"
                )
                
                # 상태 검사 수행
                system_health = await checker.perform_full_health_check()
                
                # 결과 로깅
                logger.info("시스템 상태 검사 완료", {
                    "overall_status": system_health.overall_status,
                    "component_count": len(system_health.components),
                    "healthy_components": sum(1 for c in system_health.components if c.status == "healthy"),
                    "warning_components": sum(1 for c in system_health.components if c.status == "warning"),
                    "critical_components": sum(1 for c in system_health.components if c.status == "critical")
                })
                
                # 각 컴포넌트 상태 로깅
                for component in system_health.components:
                    if component.status != "healthy":
                        logger.warning(f"컴포넌트 문제 발견: {component.component}", {
                            "component": component.component,
                            "status": component.status,
                            "message": component.message,
                            "details": component.details
                        })
                
                # 상태 리포트 생성 및 로깅
                health_report = checker.generate_health_report()
                logger.info("상태 리포트 생성 완료", {
                    "report_summary": health_report['summary']
                })
                
                # 로그 파일 확인
                log_file = Path(temp_dir) / "health_integration.log"
                content = log_file.read_text(encoding='utf-8')
                log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
                
                # 로그 내용 검증
                start_logs = [log for log in log_lines if "상태 검사 시작" in log['message']]
                assert len(start_logs) == 1
                
                complete_logs = [log for log in log_lines if "상태 검사 완료" in log['message']]
                assert len(complete_logs) == 1
                complete_log = complete_logs[0]
                assert complete_log['extra_data']['overall_status'] == "warning"
                
                warning_logs = [log for log in log_lines if log['level'] == 'WARNING']
                assert len(warning_logs) >= 1  # Qdrant 경고
    
    def test_metrics_collector_with_background_collection(self):
        """백그라운드 메트릭 수집과 로깅 통합 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = create_logger("metrics_integration", "INFO")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            collector = create_metrics_collector()
            collector.collection_interval = 0.1  # 0.1초 간격
            
            try:
                # 백그라운드 수집 시작
                collector.start_collection()
                logger.info("메트릭 수집 시작")
                
                # 일부 작업 시뮬레이션
                for i in range(5):
                    processing_time = 0.5 + i * 0.1
                    success = i % 4 != 0  # 4번째마다 실패
                    
                    collector.record_processing(processing_time, success=success)
                    collector.record_quality(0.8 - i * 0.05)
                    collector.record_api_call(0.3 + i * 0.05, status_code=200 if success else 500)
                    
                    logger.info(f"작업 {i+1} 완료", {
                        "processing_time": processing_time,
                        "success": success,
                        "iteration": i + 1
                    })
                    
                    time.sleep(0.05)  # 짧은 대기
                
                # 잠시 대기하여 백그라운드 수집 확인
                time.sleep(0.3)
                
                # 메트릭 요약 로깅
                all_metrics = collector.get_all_metrics()
                logger.info("메트릭 수집 완료", {
                    "processing_summary": {
                        "total_processed": all_metrics['processing']['total_processed'],
                        "success_rate": all_metrics['processing']['success_rate'],
                        "avg_processing_time": all_metrics['processing']['avg_processing_time']
                    },
                    "quality_summary": {
                        "total_items": all_metrics['quality']['total_items'],
                        "avg_quality_score": all_metrics['quality']['avg_quality_score'],
                        "high_quality_rate": all_metrics['quality']['high_quality_rate']
                    },
                    "api_summary": {
                        "total_calls": all_metrics['api']['total_calls'],
                        "success_rate": all_metrics['api']['success_rate'],
                        "avg_response_time": all_metrics['api']['avg_response_time']
                    }
                })
                
                # 리소스 히스토리 확인
                resource_history = collector.get_resource_history(minutes=1)
                if resource_history:
                    logger.info("리소스 히스토리 수집됨", {
                        "history_count": len(resource_history),
                        "latest_cpu": resource_history[-1]['cpu_percent'] if resource_history else None,
                        "latest_memory": resource_history[-1]['memory_mb'] if resource_history else None
                    })
                
            finally:
                collector.stop_collection()
                logger.info("메트릭 수집 중지")
            
            # 로그 파일 검증
            log_file = Path(temp_dir) / "metrics_integration.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            # 작업 완료 로그 확인
            work_logs = [log for log in log_lines if "작업" in log['message'] and "완료" in log['message']]
            assert len(work_logs) == 5
            
            # 메트릭 요약 로그 확인
            summary_logs = [log for log in log_lines if "메트릭 수집 완료" in log['message']]
            assert len(summary_logs) == 1
            summary_log = summary_logs[0]
            assert summary_log['extra_data']['processing_summary']['total_processed'] == 5
    
    @pytest.mark.asyncio
    async def test_full_system_monitoring_scenario(self):
        """전체 시스템 모니터링 시나리오 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 모든 컴포넌트 초기화
            logger = create_logger("full_system", "INFO")
            logger._setup_file_handler(temp_dir, 10*1024*1024, 5)
            
            collector = create_metrics_collector()
            checker = create_health_checker()
            
            # 시스템 시작 로그
            logger.log_pipeline_start({
                "mode": "integration_test",
                "components": ["logger", "metrics", "health_checker"]
            })
            
            try:
                # 백그라운드 메트릭 수집 시작
                collector.start_collection()
                
                # 초기 상태 검사
                with patch.object(checker, 'check_api_connectivity') as mock_api, \
                     patch.object(checker, 'check_qdrant_status') as mock_qdrant, \
                     patch.object(checker, 'check_resource_availability') as mock_resources, \
                     patch.object(checker, 'check_file_system') as mock_filesystem:
                    
                    # 정상 상태로 Mock 설정
                    mock_api.return_value = MagicMock(component="openai_api", status="healthy", message="API 정상")
                    mock_qdrant.return_value = MagicMock(component="qdrant", status="healthy", message="Qdrant 정상")
                    mock_resources.return_value = {
                        'memory': MagicMock(component="memory", status="healthy", message="메모리 정상"),
                        'cpu': MagicMock(component="cpu", status="healthy", message="CPU 정상"),
                        'disk': MagicMock(component="disk", status="healthy", message="디스크 정상")
                    }
                    mock_filesystem.return_value = MagicMock(component="filesystem", status="healthy", message="파일시스템 정상")
                    
                    initial_health = await checker.perform_full_health_check()
                    logger.info("초기 상태 검사 완료", {
                        "overall_status": initial_health.overall_status,
                        "healthy_components": sum(1 for c in initial_health.components if c.status == "healthy")
                    })
                
                # 작업 처리 시뮬레이션
                total_items = 10
                for i in range(total_items):
                    start_time = time.time()
                    
                    # 처리 시뮬레이션
                    processing_time = 0.5 + (i % 3) * 0.2
                    success = i % 7 != 0  # 7번째마다 실패
                    quality_score = 0.9 - (i % 5) * 0.1
                    
                    # 메트릭 기록
                    collector.record_processing(processing_time, success=success)
                    collector.record_quality(quality_score, is_duplicate=(i % 10 == 0))
                    collector.record_api_call(0.3, status_code=200 if success else 500)
                    
                    # 진행률 로깅
                    progress = (i + 1) / total_items
                    logger.log_processing_progress("데이터 처리", progress, {
                        "current_item": i + 1,
                        "total_items": total_items,
                        "processing_time": processing_time,
                        "success": success,
                        "quality_score": quality_score
                    })
                    
                    # 오류 발생 시 상세 로깅
                    if not success:
                        logger.error("처리 실패", extra_data={
                            "item_index": i,
                            "processing_time": processing_time,
                            "error_type": "simulated_error"
                        })
                    
                    time.sleep(0.05)  # 짧은 대기
                
                # 최종 메트릭 수집 및 로깅
                final_metrics = collector.get_all_metrics()
                logger.info("처리 완료 - 최종 메트릭", {
                    "total_processed": final_metrics['processing']['total_processed'],
                    "success_rate": final_metrics['processing']['success_rate'],
                    "avg_quality_score": final_metrics['quality']['avg_quality_score'],
                    "api_success_rate": final_metrics['api']['success_rate']
                })
                
                # 최종 상태 검사
                with patch.object(checker, 'check_api_connectivity') as mock_api, \
                     patch.object(checker, 'check_qdrant_status') as mock_qdrant, \
                     patch.object(checker, 'check_resource_availability') as mock_resources, \
                     patch.object(checker, 'check_file_system') as mock_filesystem:
                    
                    # 일부 경고 상태로 변경
                    mock_api.return_value = MagicMock(component="openai_api", status="warning", message="API 응답 지연")
                    mock_qdrant.return_value = MagicMock(component="qdrant", status="healthy", message="Qdrant 정상")
                    mock_resources.return_value = {
                        'memory': MagicMock(component="memory", status="warning", message="메모리 사용률 높음"),
                        'cpu': MagicMock(component="cpu", status="healthy", message="CPU 정상"),
                        'disk': MagicMock(component="disk", status="healthy", message="디스크 정상")
                    }
                    mock_filesystem.return_value = MagicMock(component="filesystem", status="healthy", message="파일시스템 정상")
                    
                    final_health = await checker.perform_full_health_check()
                    logger.info("최종 상태 검사 완료", {
                        "overall_status": final_health.overall_status,
                        "status_change": initial_health.overall_status != final_health.overall_status
                    })
                
                # 요약 리포트 생성
                summary_report = collector.generate_summary_report()
                health_report = checker.generate_health_report()
                
                logger.info("시스템 모니터링 완료", {
                    "monitoring_summary": {
                        "total_processed": summary_report['summary']['total_processed'],
                        "avg_throughput": summary_report['summary']['avg_throughput'],
                        "final_health_status": health_report['overall_status'],
                        "uptime_hours": summary_report['uptime_hours']
                    }
                })
                
            finally:
                collector.stop_collection()
                
                # 파이프라인 종료 로그
                logger.log_pipeline_end(True, time.time(), {
                    "total_processed": final_metrics['processing']['total_processed'],
                    "success_rate": final_metrics['processing']['success_rate']
                })
            
            # 로그 파일 검증
            log_file = Path(temp_dir) / "full_system.log"
            content = log_file.read_text(encoding='utf-8')
            log_lines = [json.loads(line) for line in content.strip().split('\n') if line]
            
            # 주요 로그 이벤트 확인
            pipeline_start_logs = [log for log in log_lines if log.get('extra_data', {}).get('event_type') == 'pipeline_start']
            assert len(pipeline_start_logs) == 1
            
            progress_logs = [log for log in log_lines if log.get('extra_data', {}).get('event_type') == 'processing_progress']
            assert len(progress_logs) == total_items
            
            error_logs = [log for log in log_lines if log['level'] == 'ERROR']
            assert len(error_logs) > 0  # 시뮬레이션된 오류들
            
            pipeline_end_logs = [log for log in log_lines if log.get('extra_data', {}).get('event_type') == 'pipeline_end']
            assert len(pipeline_end_logs) == 1
            
            # 메트릭 및 상태 관련 로그 확인
            metrics_logs = [log for log in log_lines if "메트릭" in log['message']]
            health_logs = [log for log in log_lines if "상태 검사" in log['message']]
            
            assert len(metrics_logs) > 0
            assert len(health_logs) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])