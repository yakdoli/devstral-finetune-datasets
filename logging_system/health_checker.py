"""
시스템 상태 모니터링

시스템 상태 검사, 연결 상태 확인, 상세 디버그 정보 출력 기능을 제공합니다.
"""

import asyncio
import aiohttp
import time
import psutil
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
import json


@dataclass
class HealthStatus:
    """상태 검사 결과"""
    component: str
    status: str  # 'healthy', 'warning', 'critical', 'unknown'
    message: str
    details: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    response_time_ms: Optional[float] = None


@dataclass
class SystemHealth:
    """전체 시스템 상태"""
    overall_status: str
    components: List[HealthStatus]
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    uptime_seconds: float = 0.0
    
    def is_healthy(self) -> bool:
        """전체 시스템이 건강한지 확인"""
        return self.overall_status == 'healthy'
    
    def has_warnings(self) -> bool:
        """경고가 있는지 확인"""
        return any(comp.status == 'warning' for comp in self.components)
    
    def has_critical_issues(self) -> bool:
        """치명적 문제가 있는지 확인"""
        return any(comp.status == 'critical' for comp in self.components)


class HealthChecker:
    """시스템 상태 검사기"""
    
    def __init__(self):
        """상태 검사기 초기화"""
        self.start_time = time.time()
        self.last_check_time = None
        self.check_history: List[SystemHealth] = []
        self.max_history = 100  # 최대 100개 히스토리 유지
        
        # 기본 설정
        self.openai_endpoint = "http://123.37.28.120:9997/v1"
        self.qdrant_host = "100.88.88.88"
        self.qdrant_port = 6333
        self.timeout_seconds = 10.0
        
        # 임계값 설정
        self.memory_warning_threshold = 80.0  # 메모리 사용률 80% 이상 경고
        self.memory_critical_threshold = 95.0  # 메모리 사용률 95% 이상 치명적
        self.cpu_warning_threshold = 80.0     # CPU 사용률 80% 이상 경고
        self.cpu_critical_threshold = 95.0    # CPU 사용률 95% 이상 치명적
        self.disk_warning_threshold = 85.0    # 디스크 사용률 85% 이상 경고
        self.disk_critical_threshold = 95.0   # 디스크 사용률 95% 이상 치명적
    
    def configure(self, openai_endpoint: Optional[str] = None, 
                 qdrant_host: Optional[str] = None, 
                 qdrant_port: Optional[int] = None,
                 timeout_seconds: Optional[float] = None):
        """설정 업데이트"""
        if openai_endpoint:
            self.openai_endpoint = openai_endpoint
        if qdrant_host:
            self.qdrant_host = qdrant_host
        if qdrant_port:
            self.qdrant_port = qdrant_port
        if timeout_seconds:
            self.timeout_seconds = timeout_seconds
    
    async def check_api_connectivity(self) -> HealthStatus:
        """OpenAI API 연결 상태 확인"""
        start_time = time.time()
        
        try:
            timeout = aiohttp.ClientTimeout(total=self.timeout_seconds)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                # 모델 목록 엔드포인트로 연결 테스트
                url = f"{self.openai_endpoint}/models"
                async with session.get(url) as response:
                    response_time = (time.time() - start_time) * 1000
                    
                    if response.status == 200:
                        data = await response.json()
                        model_count = len(data.get('data', []))
                        
                        return HealthStatus(
                            component="openai_api",
                            status="healthy",
                            message=f"API 연결 정상 ({model_count}개 모델 사용 가능)",
                            details={
                                'endpoint': self.openai_endpoint,
                                'status_code': response.status,
                                'model_count': model_count,
                                'models': [model.get('id') for model in data.get('data', [])][:5]  # 최대 5개만
                            },
                            response_time_ms=response_time
                        )
                    else:
                        return HealthStatus(
                            component="openai_api",
                            status="warning",
                            message=f"API 응답 이상 (HTTP {response.status})",
                            details={
                                'endpoint': self.openai_endpoint,
                                'status_code': response.status,
                                'response_text': await response.text()
                            },
                            response_time_ms=response_time
                        )
                        
        except asyncio.TimeoutError:
            return HealthStatus(
                component="openai_api",
                status="critical",
                message=f"API 연결 시간 초과 ({self.timeout_seconds}초)",
                details={
                    'endpoint': self.openai_endpoint,
                    'timeout_seconds': self.timeout_seconds
                }
            )
        except Exception as e:
            return HealthStatus(
                component="openai_api",
                status="critical",
                message=f"API 연결 실패: {str(e)}",
                details={
                    'endpoint': self.openai_endpoint,
                    'error_type': type(e).__name__,
                    'error_message': str(e)
                }
            )
    
    async def check_qdrant_status(self) -> HealthStatus:
        """Qdrant 연결 상태 확인"""
        start_time = time.time()
        
        try:
            timeout = aiohttp.ClientTimeout(total=self.timeout_seconds)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                # Qdrant 상태 확인 엔드포인트
                url = f"http://{self.qdrant_host}:{self.qdrant_port}/collections"
                async with session.get(url) as response:
                    response_time = (time.time() - start_time) * 1000
                    
                    if response.status == 200:
                        data = await response.json()
                        collections = data.get('result', {}).get('collections', [])
                        
                        # 특정 컬렉션 확인
                        target_collection = "ws-7491d651ae044c78"
                        collection_exists = any(
                            col.get('name') == target_collection for col in collections
                        )
                        
                        status = "healthy" if collection_exists else "warning"
                        message = f"Qdrant 연결 정상 ({len(collections)}개 컬렉션)"
                        if not collection_exists:
                            message += f" - 대상 컬렉션 '{target_collection}' 없음"
                        
                        return HealthStatus(
                            component="qdrant",
                            status=status,
                            message=message,
                            details={
                                'host': self.qdrant_host,
                                'port': self.qdrant_port,
                                'status_code': response.status,
                                'collection_count': len(collections),
                                'target_collection_exists': collection_exists,
                                'collections': [col.get('name') for col in collections][:5]  # 최대 5개만
                            },
                            response_time_ms=response_time
                        )
                    else:
                        return HealthStatus(
                            component="qdrant",
                            status="warning",
                            message=f"Qdrant 응답 이상 (HTTP {response.status})",
                            details={
                                'host': self.qdrant_host,
                                'port': self.qdrant_port,
                                'status_code': response.status
                            },
                            response_time_ms=response_time
                        )
                        
        except asyncio.TimeoutError:
            return HealthStatus(
                component="qdrant",
                status="critical",
                message=f"Qdrant 연결 시간 초과 ({self.timeout_seconds}초)",
                details={
                    'host': self.qdrant_host,
                    'port': self.qdrant_port,
                    'timeout_seconds': self.timeout_seconds
                }
            )
        except Exception as e:
            return HealthStatus(
                component="qdrant",
                status="critical",
                message=f"Qdrant 연결 실패: {str(e)}",
                details={
                    'host': self.qdrant_host,
                    'port': self.qdrant_port,
                    'error_type': type(e).__name__,
                    'error_message': str(e)
                }
            )
    
    def check_resource_availability(self) -> Dict[str, HealthStatus]:
        """리소스 가용성 확인"""
        results = {}
        
        # 메모리 사용량 확인
        memory = psutil.virtual_memory()
        memory_status = "healthy"
        if memory.percent >= self.memory_critical_threshold:
            memory_status = "critical"
        elif memory.percent >= self.memory_warning_threshold:
            memory_status = "warning"
        
        results['memory'] = HealthStatus(
            component="memory",
            status=memory_status,
            message=f"메모리 사용률: {memory.percent:.1f}%",
            details={
                'used_gb': memory.used / 1024 / 1024 / 1024,
                'total_gb': memory.total / 1024 / 1024 / 1024,
                'available_gb': memory.available / 1024 / 1024 / 1024,
                'percent': memory.percent,
                'warning_threshold': self.memory_warning_threshold,
                'critical_threshold': self.memory_critical_threshold
            }
        )
        
        # CPU 사용률 확인
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_status = "healthy"
        if cpu_percent >= self.cpu_critical_threshold:
            cpu_status = "critical"
        elif cpu_percent >= self.cpu_warning_threshold:
            cpu_status = "warning"
        
        results['cpu'] = HealthStatus(
            component="cpu",
            status=cpu_status,
            message=f"CPU 사용률: {cpu_percent:.1f}%",
            details={
                'percent': cpu_percent,
                'core_count': psutil.cpu_count(),
                'logical_core_count': psutil.cpu_count(logical=True),
                'warning_threshold': self.cpu_warning_threshold,
                'critical_threshold': self.cpu_critical_threshold
            }
        )
        
        # 디스크 사용량 확인
        disk = psutil.disk_usage('/')
        disk_status = "healthy"
        disk_percent = (disk.used / disk.total) * 100
        if disk_percent >= self.disk_critical_threshold:
            disk_status = "critical"
        elif disk_percent >= self.disk_warning_threshold:
            disk_status = "warning"
        
        results['disk'] = HealthStatus(
            component="disk",
            status=disk_status,
            message=f"디스크 사용률: {disk_percent:.1f}%",
            details={
                'used_gb': disk.used / 1024 / 1024 / 1024,
                'total_gb': disk.total / 1024 / 1024 / 1024,
                'free_gb': disk.free / 1024 / 1024 / 1024,
                'percent': disk_percent,
                'warning_threshold': self.disk_warning_threshold,
                'critical_threshold': self.disk_critical_threshold
            }
        )
        
        return results
    
    def check_file_system(self) -> HealthStatus:
        """파일 시스템 상태 확인"""
        try:
            # 필수 디렉토리 확인
            required_dirs = [
                Path("md_staging"),
                Path("output"),
                Path("output/logs"),
                Path("output/datasets"),
                Path("output/reports")
            ]
            
            missing_dirs = []
            for dir_path in required_dirs:
                if not dir_path.exists():
                    missing_dirs.append(str(dir_path))
            
            # 쓰기 권한 확인
            test_file = Path("output/.health_check_test")
            can_write = True
            try:
                test_file.parent.mkdir(parents=True, exist_ok=True)
                test_file.write_text("test")
                test_file.unlink()
            except Exception:
                can_write = False
            
            if missing_dirs or not can_write:
                status = "warning"
                message = "파일 시스템 문제 발견"
                if missing_dirs:
                    message += f" - 누락된 디렉토리: {', '.join(missing_dirs)}"
                if not can_write:
                    message += " - 쓰기 권한 없음"
            else:
                status = "healthy"
                message = "파일 시스템 정상"
            
            return HealthStatus(
                component="filesystem",
                status=status,
                message=message,
                details={
                    'required_directories': [str(d) for d in required_dirs],
                    'missing_directories': missing_dirs,
                    'can_write': can_write,
                    'output_dir_exists': Path("output").exists()
                }
            )
            
        except Exception as e:
            return HealthStatus(
                component="filesystem",
                status="critical",
                message=f"파일 시스템 검사 실패: {str(e)}",
                details={
                    'error_type': type(e).__name__,
                    'error_message': str(e)
                }
            )
    
    async def perform_full_health_check(self) -> SystemHealth:
        """전체 상태 검사 수행"""
        self.last_check_time = time.time()
        components = []
        
        # API 연결 상태 확인
        api_status = await self.check_api_connectivity()
        components.append(api_status)
        
        # Qdrant 상태 확인
        qdrant_status = await self.check_qdrant_status()
        components.append(qdrant_status)
        
        # 리소스 상태 확인
        resource_statuses = self.check_resource_availability()
        components.extend(resource_statuses.values())
        
        # 파일 시스템 상태 확인
        filesystem_status = self.check_file_system()
        components.append(filesystem_status)
        
        # 전체 상태 결정
        critical_count = sum(1 for comp in components if comp.status == 'critical')
        warning_count = sum(1 for comp in components if comp.status == 'warning')
        
        if critical_count > 0:
            overall_status = 'critical'
        elif warning_count > 0:
            overall_status = 'warning'
        else:
            overall_status = 'healthy'
        
        system_health = SystemHealth(
            overall_status=overall_status,
            components=components,
            uptime_seconds=time.time() - self.start_time
        )
        
        # 히스토리에 추가
        self.check_history.append(system_health)
        if len(self.check_history) > self.max_history:
            self.check_history = self.check_history[-self.max_history:]
        
        return system_health
    
    def generate_health_report(self, include_history: bool = False) -> Dict[str, Any]:
        """상태 리포트 생성"""
        if not self.check_history:
            return {
                'error': '상태 검사 히스토리가 없습니다. 먼저 perform_full_health_check()를 실행하세요.'
            }
        
        latest_check = self.check_history[-1]
        
        report = {
            'report_timestamp': datetime.now().isoformat(),
            'system_uptime_hours': latest_check.uptime_seconds / 3600,
            'last_check_timestamp': latest_check.timestamp,
            'overall_status': latest_check.overall_status,
            'summary': {
                'healthy_components': sum(1 for comp in latest_check.components if comp.status == 'healthy'),
                'warning_components': sum(1 for comp in latest_check.components if comp.status == 'warning'),
                'critical_components': sum(1 for comp in latest_check.components if comp.status == 'critical'),
                'total_components': len(latest_check.components)
            },
            'components': {
                comp.component: {
                    'status': comp.status,
                    'message': comp.message,
                    'response_time_ms': comp.response_time_ms,
                    'details': comp.details
                }
                for comp in latest_check.components
            }
        }
        
        if include_history and len(self.check_history) > 1:
            report['history'] = {
                'check_count': len(self.check_history),
                'recent_checks': [
                    {
                        'timestamp': check.timestamp,
                        'overall_status': check.overall_status,
                        'component_summary': {
                            'healthy': sum(1 for comp in check.components if comp.status == 'healthy'),
                            'warning': sum(1 for comp in check.components if comp.status == 'warning'),
                            'critical': sum(1 for comp in check.components if comp.status == 'critical')
                        }
                    }
                    for check in self.check_history[-10:]  # 최근 10개만
                ]
            }
        
        return report
    
    def get_debug_info(self, verbose: bool = False) -> Dict[str, Any]:
        """상세 디버그 정보 출력"""
        debug_info = {
            'timestamp': datetime.now().isoformat(),
            'system_info': {
                'python_version': f"{psutil.sys.version_info.major}.{psutil.sys.version_info.minor}.{psutil.sys.version_info.micro}",
                'platform': psutil.sys.platform,
                'hostname': psutil.os.uname().nodename if hasattr(psutil.os, 'uname') else 'unknown',
                'pid': psutil.os.getpid(),
                'uptime_seconds': time.time() - self.start_time
            },
            'configuration': {
                'openai_endpoint': self.openai_endpoint,
                'qdrant_host': self.qdrant_host,
                'qdrant_port': self.qdrant_port,
                'timeout_seconds': self.timeout_seconds,
                'thresholds': {
                    'memory_warning': self.memory_warning_threshold,
                    'memory_critical': self.memory_critical_threshold,
                    'cpu_warning': self.cpu_warning_threshold,
                    'cpu_critical': self.cpu_critical_threshold,
                    'disk_warning': self.disk_warning_threshold,
                    'disk_critical': self.disk_critical_threshold
                }
            }
        }
        
        if verbose:
            # 상세 시스템 정보
            debug_info['detailed_system_info'] = {
                'cpu_info': {
                    'physical_cores': psutil.cpu_count(logical=False),
                    'logical_cores': psutil.cpu_count(logical=True),
                    'cpu_freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
                    'cpu_times': psutil.cpu_times()._asdict()
                },
                'memory_info': psutil.virtual_memory()._asdict(),
                'disk_info': {
                    'disk_usage': psutil.disk_usage('/')._asdict(),
                    'disk_io': psutil.disk_io_counters()._asdict() if psutil.disk_io_counters() else None
                },
                'network_info': psutil.net_io_counters()._asdict() if psutil.net_io_counters() else None,
                'process_info': {
                    'memory_info': psutil.Process().memory_info()._asdict(),
                    'cpu_percent': psutil.Process().cpu_percent(),
                    'num_threads': psutil.Process().num_threads(),
                    'create_time': psutil.Process().create_time()
                }
            }
            
            # 환경 변수 (민감한 정보 제외)
            import os
            safe_env_vars = {
                k: v for k, v in os.environ.items()
                if not any(sensitive in k.lower() for sensitive in ['key', 'token', 'password', 'secret'])
            }
            debug_info['environment_variables'] = safe_env_vars
        
        return debug_info