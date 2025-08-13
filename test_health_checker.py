"""
상태 모니터링 시스템 단위 테스트

시스템 상태 검사, 연결 상태 확인, 디버그 정보 출력 기능을 테스트합니다.
"""

import asyncio
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock, AsyncMock
import pytest
import aiohttp

from logging_system.health_checker import (
    HealthChecker, HealthStatus, SystemHealth
)


class TestHealthStatus:
    """HealthStatus 테스트"""
    
    def test_health_status_creation(self):
        """HealthStatus 생성 테스트"""
        status = HealthStatus(
            component="test_component",
            status="healthy",
            message="테스트 컴포넌트 정상",
            details={"version": "1.0.0"},
            response_time_ms=150.5
        )
        
        assert status.component == "test_component"
        assert status.status == "healthy"
        assert status.message == "테스트 컴포넌트 정상"
        assert status.details["version"] == "1.0.0"
        assert status.response_time_ms == 150.5
        assert status.timestamp is not None


class TestSystemHealth:
    """SystemHealth 테스트"""
    
    def test_system_health_creation(self):
        """SystemHealth 생성 테스트"""
        components = [
            HealthStatus("comp1", "healthy", "정상"),
            HealthStatus("comp2", "warning", "경고"),
            HealthStatus("comp3", "critical", "치명적")
        ]
        
        system_health = SystemHealth(
            overall_status="warning",
            components=components,
            uptime_seconds=3600.0
        )
        
        assert system_health.overall_status == "warning"
        assert len(system_health.components) == 3
        assert system_health.uptime_seconds == 3600.0
    
    def test_system_health_status_checks(self):
        """SystemHealth 상태 확인 메서드 테스트"""
        # 모든 컴포넌트가 정상인 경우
        healthy_components = [
            HealthStatus("comp1", "healthy", "정상"),
            HealthStatus("comp2", "healthy", "정상")
        ]
        healthy_system = SystemHealth("healthy", healthy_components)
        
        assert healthy_system.is_healthy() is True
        assert healthy_system.has_warnings() is False
        assert healthy_system.has_critical_issues() is False
        
        # 경고가 있는 경우
        warning_components = [
            HealthStatus("comp1", "healthy", "정상"),
            HealthStatus("comp2", "warning", "경고")
        ]
        warning_system = SystemHealth("warning", warning_components)
        
        assert warning_system.is_healthy() is False
        assert warning_system.has_warnings() is True
        assert warning_system.has_critical_issues() is False
        
        # 치명적 문제가 있는 경우
        critical_components = [
            HealthStatus("comp1", "healthy", "정상"),
            HealthStatus("comp2", "critical", "치명적")
        ]
        critical_system = SystemHealth("critical", critical_components)
        
        assert critical_system.is_healthy() is False
        assert critical_system.has_warnings() is False
        assert critical_system.has_critical_issues() is True


class TestHealthChecker:
    """HealthChecker 테스트"""
    
    def test_health_checker_initialization(self):
        """HealthChecker 초기화 테스트"""
        checker = HealthChecker()
        
        assert checker.openai_endpoint == "http://123.37.28.120:9997/v1"
        assert checker.qdrant_host == "100.88.88.88"
        assert checker.qdrant_port == 6333
        assert checker.timeout_seconds == 10.0
        assert checker.memory_warning_threshold == 80.0
        assert checker.memory_critical_threshold == 95.0
        assert len(checker.check_history) == 0
    
    def test_health_checker_configuration(self):
        """HealthChecker 설정 테스트"""
        checker = HealthChecker()
        
        checker.configure(
            openai_endpoint="http://custom-api.com/v1",
            qdrant_host="custom-qdrant.com",
            qdrant_port=7333,
            timeout_seconds=15.0
        )
        
        assert checker.openai_endpoint == "http://custom-api.com/v1"
        assert checker.qdrant_host == "custom-qdrant.com"
        assert checker.qdrant_port == 7333
        assert checker.timeout_seconds == 15.0
    
    @pytest.mark.asyncio
    async def test_check_api_connectivity_success(self):
        """API 연결 성공 테스트"""
        checker = HealthChecker()
        
        # Mock 응답 데이터
        mock_response_data = {
            "data": [
                {"id": "model1", "object": "model"},
                {"id": "model2", "object": "model"}
            ]
        }
        
        with patch('aiohttp.ClientSession') as mock_session:
            mock_response = AsyncMock()
            mock_response.status = 200
            mock_response.json = AsyncMock(return_value=mock_response_data)
            
            mock_session.return_value.__aenter__.return_value.get.return_value.__aenter__.return_value = mock_response
            
            result = await checker.check_api_connectivity()
            
            assert result.component == "openai_api"
            assert result.status == "healthy"
            assert "API 연결 정상" in result.message
            assert result.details["model_count"] == 2
            assert result.details["status_code"] == 200
            assert result.response_time_ms is not None
    
    @pytest.mark.asyncio
    async def test_check_api_connectivity_http_error(self):
        """API 연결 HTTP 오류 테스트"""
        checker = HealthChecker()
        
        with patch('aiohttp.ClientSession') as mock_session:
            mock_response = AsyncMock()
            mock_response.status = 500
            mock_response.text = AsyncMock(return_value="Internal Server Error")
            
            mock_session.return_value.__aenter__.return_value.get.return_value.__aenter__.return_value = mock_response
            
            result = await checker.check_api_connectivity()
            
            assert result.component == "openai_api"
            assert result.status == "warning"
            assert "API 응답 이상" in result.message
            assert result.details["status_code"] == 500
    
    @pytest.mark.asyncio
    async def test_check_api_connectivity_timeout(self):
        """API 연결 시간 초과 테스트"""
        checker = HealthChecker()
        checker.timeout_seconds = 1.0
        
        with patch('aiohttp.ClientSession') as mock_session:
            mock_session.return_value.__aenter__.return_value.get.side_effect = asyncio.TimeoutError()
            
            result = await checker.check_api_connectivity()
            
            assert result.component == "openai_api"
            assert result.status == "critical"
            assert "API 연결 시간 초과" in result.message
            assert result.details["timeout_seconds"] == 1.0
    
    @pytest.mark.asyncio
    async def test_check_api_connectivity_connection_error(self):
        """API 연결 오류 테스트"""
        checker = HealthChecker()
        
        with patch('aiohttp.ClientSession') as mock_session:
            mock_session.return_value.__aenter__.return_value.get.side_effect = aiohttp.ClientConnectorError(
                connection_key=None, os_error=None
            )
            
            result = await checker.check_api_connectivity()
            
            assert result.component == "openai_api"
            assert result.status == "critical"
            assert "API 연결 실패" in result.message
            assert result.details["error_type"] == "ClientConnectorError"
    
    @pytest.mark.asyncio
    async def test_check_qdrant_status_success(self):
        """Qdrant 상태 확인 성공 테스트"""
        checker = HealthChecker()
        
        mock_response_data = {
            "result": {
                "collections": [
                    {"name": "ws-7491d651ae044c78"},
                    {"name": "other-collection"}
                ]
            }
        }
        
        with patch('aiohttp.ClientSession') as mock_session:
            mock_response = AsyncMock()
            mock_response.status = 200
            mock_response.json = AsyncMock(return_value=mock_response_data)
            
            mock_session.return_value.__aenter__.return_value.get.return_value.__aenter__.return_value = mock_response
            
            result = await checker.check_qdrant_status()
            
            assert result.component == "qdrant"
            assert result.status == "healthy"
            assert "Qdrant 연결 정상" in result.message
            assert result.details["collection_count"] == 2
            assert result.details["target_collection_exists"] is True
    
    @pytest.mark.asyncio
    async def test_check_qdrant_status_missing_collection(self):
        """Qdrant 대상 컬렉션 누락 테스트"""
        checker = HealthChecker()
        
        mock_response_data = {
            "result": {
                "collections": [
                    {"name": "other-collection"}
                ]
            }
        }
        
        with patch('aiohttp.ClientSession') as mock_session:
            mock_response = AsyncMock()
            mock_response.status = 200
            mock_response.json = AsyncMock(return_value=mock_response_data)
            
            mock_session.return_value.__aenter__.return_value.get.return_value.__aenter__.return_value = mock_response
            
            result = await checker.check_qdrant_status()
            
            assert result.component == "qdrant"
            assert result.status == "warning"
            assert "대상 컬렉션" in result.message
            assert result.details["target_collection_exists"] is False
    
    @patch('psutil.virtual_memory')
    def test_check_resource_availability_memory_healthy(self, mock_memory):
        """메모리 리소스 정상 상태 테스트"""
        mock_memory.return_value = MagicMock(
            used=4 * 1024 * 1024 * 1024,  # 4GB
            total=8 * 1024 * 1024 * 1024,  # 8GB
            available=4 * 1024 * 1024 * 1024,  # 4GB
            percent=50.0
        )
        
        checker = HealthChecker()
        results = checker.check_resource_availability()
        
        memory_status = results['memory']
        assert memory_status.component == "memory"
        assert memory_status.status == "healthy"
        assert "메모리 사용률: 50.0%" in memory_status.message
        assert memory_status.details['percent'] == 50.0
    
    @patch('psutil.virtual_memory')
    def test_check_resource_availability_memory_warning(self, mock_memory):
        """메모리 리소스 경고 상태 테스트"""
        mock_memory.return_value = MagicMock(
            used=7 * 1024 * 1024 * 1024,  # 7GB
            total=8 * 1024 * 1024 * 1024,  # 8GB
            available=1 * 1024 * 1024 * 1024,  # 1GB
            percent=87.5
        )
        
        checker = HealthChecker()
        results = checker.check_resource_availability()
        
        memory_status = results['memory']
        assert memory_status.component == "memory"
        assert memory_status.status == "warning"
        assert "메모리 사용률: 87.5%" in memory_status.message
    
    @patch('psutil.virtual_memory')
    def test_check_resource_availability_memory_critical(self, mock_memory):
        """메모리 리소스 치명적 상태 테스트"""
        mock_memory.return_value = MagicMock(
            used=7.8 * 1024 * 1024 * 1024,  # 7.8GB
            total=8 * 1024 * 1024 * 1024,    # 8GB
            available=0.2 * 1024 * 1024 * 1024,  # 0.2GB
            percent=97.5
        )
        
        checker = HealthChecker()
        results = checker.check_resource_availability()
        
        memory_status = results['memory']
        assert memory_status.component == "memory"
        assert memory_status.status == "critical"
        assert "메모리 사용률: 97.5%" in memory_status.message
    
    @patch('psutil.cpu_percent')
    def test_check_resource_availability_cpu(self, mock_cpu):
        """CPU 리소스 상태 테스트"""
        mock_cpu.return_value = 45.5
        
        with patch('psutil.cpu_count', return_value=4):
            checker = HealthChecker()
            results = checker.check_resource_availability()
            
            cpu_status = results['cpu']
            assert cpu_status.component == "cpu"
            assert cpu_status.status == "healthy"
            assert "CPU 사용률: 45.5%" in cpu_status.message
            assert cpu_status.details['core_count'] == 4
    
    @patch('psutil.disk_usage')
    def test_check_resource_availability_disk(self, mock_disk):
        """디스크 리소스 상태 테스트"""
        mock_disk.return_value = MagicMock(
            used=400 * 1024 * 1024 * 1024,   # 400GB
            total=1000 * 1024 * 1024 * 1024,  # 1TB
            free=600 * 1024 * 1024 * 1024     # 600GB
        )
        
        checker = HealthChecker()
        results = checker.check_resource_availability()
        
        disk_status = results['disk']
        assert disk_status.component == "disk"
        assert disk_status.status == "healthy"
        assert "디스크 사용률: 40.0%" in disk_status.message
    
    def test_check_file_system_healthy(self):
        """파일 시스템 정상 상태 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 필요한 디렉토리 생성
            required_dirs = [
                Path(temp_dir) / "md_staging",
                Path(temp_dir) / "output",
                Path(temp_dir) / "output" / "logs",
                Path(temp_dir) / "output" / "datasets",
                Path(temp_dir) / "output" / "reports"
            ]
            
            for dir_path in required_dirs:
                dir_path.mkdir(parents=True, exist_ok=True)
            
            # 현재 디렉토리를 임시 디렉토리로 변경
            import os
            original_cwd = os.getcwd()
            try:
                os.chdir(temp_dir)
                
                checker = HealthChecker()
                result = checker.check_file_system()
                
                assert result.component == "filesystem"
                assert result.status == "healthy"
                assert "파일 시스템 정상" in result.message
                assert result.details["can_write"] is True
                assert len(result.details["missing_directories"]) == 0
                
            finally:
                os.chdir(original_cwd)
    
    def test_check_file_system_missing_directories(self):
        """파일 시스템 디렉토리 누락 테스트"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 일부 디렉토리만 생성
            (Path(temp_dir) / "md_staging").mkdir()
            (Path(temp_dir) / "output").mkdir()
            
            import os
            original_cwd = os.getcwd()
            try:
                os.chdir(temp_dir)
                
                checker = HealthChecker()
                result = checker.check_file_system()
                
                assert result.component == "filesystem"
                assert result.status == "warning"
                assert "파일 시스템 문제 발견" in result.message
                assert len(result.details["missing_directories"]) > 0
                
            finally:
                os.chdir(original_cwd)
    
    @pytest.mark.asyncio
    async def test_perform_full_health_check(self):
        """전체 상태 검사 수행 테스트"""
        checker = HealthChecker()
        
        # API 및 Qdrant 모킹
        with patch.object(checker, 'check_api_connectivity') as mock_api, \
             patch.object(checker, 'check_qdrant_status') as mock_qdrant, \
             patch.object(checker, 'check_resource_availability') as mock_resources, \
             patch.object(checker, 'check_file_system') as mock_filesystem:
            
            # Mock 반환값 설정
            mock_api.return_value = HealthStatus("openai_api", "healthy", "API 정상")
            mock_qdrant.return_value = HealthStatus("qdrant", "healthy", "Qdrant 정상")
            mock_resources.return_value = {
                'memory': HealthStatus("memory", "healthy", "메모리 정상"),
                'cpu': HealthStatus("cpu", "healthy", "CPU 정상"),
                'disk': HealthStatus("disk", "healthy", "디스크 정상")
            }
            mock_filesystem.return_value = HealthStatus("filesystem", "healthy", "파일시스템 정상")
            
            result = await checker.perform_full_health_check()
            
            assert isinstance(result, SystemHealth)
            assert result.overall_status == "healthy"
            assert len(result.components) == 6  # API + Qdrant + 3개 리소스 + 파일시스템
            assert len(checker.check_history) == 1
    
    @pytest.mark.asyncio
    async def test_perform_full_health_check_with_warnings(self):
        """경고가 있는 전체 상태 검사 테스트"""
        checker = HealthChecker()
        
        with patch.object(checker, 'check_api_connectivity') as mock_api, \
             patch.object(checker, 'check_qdrant_status') as mock_qdrant, \
             patch.object(checker, 'check_resource_availability') as mock_resources, \
             patch.object(checker, 'check_file_system') as mock_filesystem:
            
            # 일부 경고 상태로 설정
            mock_api.return_value = HealthStatus("openai_api", "warning", "API 경고")
            mock_qdrant.return_value = HealthStatus("qdrant", "healthy", "Qdrant 정상")
            mock_resources.return_value = {
                'memory': HealthStatus("memory", "healthy", "메모리 정상"),
                'cpu': HealthStatus("cpu", "healthy", "CPU 정상"),
                'disk': HealthStatus("disk", "healthy", "디스크 정상")
            }
            mock_filesystem.return_value = HealthStatus("filesystem", "healthy", "파일시스템 정상")
            
            result = await checker.perform_full_health_check()
            
            assert result.overall_status == "warning"
            assert result.has_warnings() is True
            assert result.has_critical_issues() is False
    
    @pytest.mark.asyncio
    async def test_perform_full_health_check_with_critical(self):
        """치명적 문제가 있는 전체 상태 검사 테스트"""
        checker = HealthChecker()
        
        with patch.object(checker, 'check_api_connectivity') as mock_api, \
             patch.object(checker, 'check_qdrant_status') as mock_qdrant, \
             patch.object(checker, 'check_resource_availability') as mock_resources, \
             patch.object(checker, 'check_file_system') as mock_filesystem:
            
            # 치명적 문제 상태로 설정
            mock_api.return_value = HealthStatus("openai_api", "critical", "API 치명적")
            mock_qdrant.return_value = HealthStatus("qdrant", "healthy", "Qdrant 정상")
            mock_resources.return_value = {
                'memory': HealthStatus("memory", "healthy", "메모리 정상"),
                'cpu': HealthStatus("cpu", "healthy", "CPU 정상"),
                'disk': HealthStatus("disk", "healthy", "디스크 정상")
            }
            mock_filesystem.return_value = HealthStatus("filesystem", "healthy", "파일시스템 정상")
            
            result = await checker.perform_full_health_check()
            
            assert result.overall_status == "critical"
            assert result.has_critical_issues() is True
    
    @pytest.mark.asyncio
    async def test_generate_health_report(self):
        """상태 리포트 생성 테스트"""
        checker = HealthChecker()
        
        # 먼저 상태 검사 수행
        with patch.object(checker, 'check_api_connectivity') as mock_api, \
             patch.object(checker, 'check_qdrant_status') as mock_qdrant, \
             patch.object(checker, 'check_resource_availability') as mock_resources, \
             patch.object(checker, 'check_file_system') as mock_filesystem:
            
            mock_api.return_value = HealthStatus("openai_api", "healthy", "API 정상")
            mock_qdrant.return_value = HealthStatus("qdrant", "warning", "Qdrant 경고")
            mock_resources.return_value = {
                'memory': HealthStatus("memory", "healthy", "메모리 정상"),
                'cpu': HealthStatus("cpu", "healthy", "CPU 정상"),
                'disk': HealthStatus("disk", "healthy", "디스크 정상")
            }
            mock_filesystem.return_value = HealthStatus("filesystem", "healthy", "파일시스템 정상")
            
            await checker.perform_full_health_check()
            
            report = checker.generate_health_report()
            
            assert 'report_timestamp' in report
            assert 'system_uptime_hours' in report
            assert 'last_check_timestamp' in report
            assert report['overall_status'] == "warning"
            
            summary = report['summary']
            assert summary['healthy_components'] == 5
            assert summary['warning_components'] == 1
            assert summary['critical_components'] == 0
            assert summary['total_components'] == 6
            
            assert 'components' in report
            assert 'openai_api' in report['components']
            assert 'qdrant' in report['components']
    
    @pytest.mark.asyncio
    async def test_generate_health_report_with_history(self):
        """히스토리 포함 상태 리포트 생성 테스트"""
        checker = HealthChecker()
        
        # 여러 번 상태 검사 수행
        with patch.object(checker, 'check_api_connectivity') as mock_api, \
             patch.object(checker, 'check_qdrant_status') as mock_qdrant, \
             patch.object(checker, 'check_resource_availability') as mock_resources, \
             patch.object(checker, 'check_file_system') as mock_filesystem:
            
            mock_api.return_value = HealthStatus("openai_api", "healthy", "API 정상")
            mock_qdrant.return_value = HealthStatus("qdrant", "healthy", "Qdrant 정상")
            mock_resources.return_value = {
                'memory': HealthStatus("memory", "healthy", "메모리 정상"),
                'cpu': HealthStatus("cpu", "healthy", "CPU 정상"),
                'disk': HealthStatus("disk", "healthy", "디스크 정상")
            }
            mock_filesystem.return_value = HealthStatus("filesystem", "healthy", "파일시스템 정상")
            
            # 첫 번째 검사
            await checker.perform_full_health_check()
            
            # 두 번째 검사 (경고 상태로 변경)
            mock_api.return_value = HealthStatus("openai_api", "warning", "API 경고")
            await checker.perform_full_health_check()
            
            report = checker.generate_health_report(include_history=True)
            
            assert 'history' in report
            assert report['history']['check_count'] == 2
            assert len(report['history']['recent_checks']) == 2
    
    def test_generate_health_report_no_history(self):
        """히스토리가 없는 상태에서 리포트 생성 테스트"""
        checker = HealthChecker()
        
        report = checker.generate_health_report()
        
        assert 'error' in report
        assert '상태 검사 히스토리가 없습니다' in report['error']
    
    def test_get_debug_info_basic(self):
        """기본 디버그 정보 테스트"""
        checker = HealthChecker()
        
        debug_info = checker.get_debug_info(verbose=False)
        
        assert 'timestamp' in debug_info
        assert 'system_info' in debug_info
        assert 'configuration' in debug_info
        
        system_info = debug_info['system_info']
        assert 'python_version' in system_info
        assert 'platform' in system_info
        assert 'uptime_seconds' in system_info
        
        config = debug_info['configuration']
        assert config['openai_endpoint'] == "http://123.37.28.120:9997/v1"
        assert config['qdrant_host'] == "100.88.88.88"
        assert config['qdrant_port'] == 6333
    
    @patch('psutil.cpu_count')
    @patch('psutil.cpu_freq')
    @patch('psutil.cpu_times')
    @patch('psutil.virtual_memory')
    @patch('psutil.disk_usage')
    @patch('psutil.Process')
    def test_get_debug_info_verbose(self, mock_process, mock_disk, mock_memory, 
                                   mock_cpu_times, mock_cpu_freq, mock_cpu_count):
        """상세 디버그 정보 테스트"""
        # Mock 설정
        mock_cpu_count.side_effect = [4, 8]  # physical, logical
        mock_cpu_freq.return_value = MagicMock(current=2400.0, min=800.0, max=3200.0)
        mock_cpu_times.return_value = MagicMock(user=100.0, system=50.0, idle=1000.0)
        mock_memory.return_value = MagicMock(total=8*1024**3, available=4*1024**3, percent=50.0)
        mock_disk.return_value = MagicMock(total=1000*1024**3, used=400*1024**3, free=600*1024**3)
        
        mock_process_instance = MagicMock()
        mock_process_instance.memory_info.return_value = MagicMock(rss=512*1024**2)
        mock_process_instance.cpu_percent.return_value = 25.5
        mock_process_instance.num_threads.return_value = 8
        mock_process_instance.create_time.return_value = 1640995200.0
        mock_process.return_value = mock_process_instance
        
        checker = HealthChecker()
        debug_info = checker.get_debug_info(verbose=True)
        
        assert 'detailed_system_info' in debug_info
        assert 'environment_variables' in debug_info
        
        detailed_info = debug_info['detailed_system_info']
        assert 'cpu_info' in detailed_info
        assert 'memory_info' in detailed_info
        assert 'disk_info' in detailed_info
        assert 'process_info' in detailed_info
        
        cpu_info = detailed_info['cpu_info']
        assert cpu_info['physical_cores'] == 4
        assert cpu_info['logical_cores'] == 8
        
        process_info = detailed_info['process_info']
        assert process_info['cpu_percent'] == 25.5
        assert process_info['num_threads'] == 8


if __name__ == "__main__":
    pytest.main([__file__, "-v"])