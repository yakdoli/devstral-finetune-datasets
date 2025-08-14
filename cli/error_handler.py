"""
CLI 오류 처리 모듈 - 사용자 친화적인 오류 메시지 및 복구 제안
"""

import sys
import traceback
from typing import Optional, Dict, Any, List
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

console = Console()


class CLIError(Exception):
    """CLI 관련 기본 예외 클래스"""
    def __init__(self, message: str, suggestions: Optional[List[str]] = None):
        super().__init__(message)
        self.suggestions = suggestions or []


class ConfigurationError(CLIError):
    """설정 관련 오류"""
    pass


class ValidationError(CLIError):
    """검증 관련 오류"""
    pass


class ResourceError(CLIError):
    """리소스 관련 오류 (파일, 네트워크 등)"""
    pass


class ErrorHandler:
    """통합 오류 처리기"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.error_suggestions = {
            # 설정 파일 관련 오류
            "설정 파일을 찾을 수 없습니다": [
                "python -m cli create-config config.yaml 명령으로 기본 설정 파일을 생성하세요",
                "올바른 설정 파일 경로를 --config 옵션으로 지정하세요"
            ],
            "YAML 파싱 오류": [
                "YAML 파일의 구문을 확인하세요 (들여쓰기, 콜론, 대시 등)",
                "온라인 YAML 검증 도구를 사용하여 구문을 확인하세요",
                "python -m cli create-config new_config.yaml로 새 설정 파일을 생성하세요"
            ],
            
            # 파라미터 관련 오류
            "유효하지 않은 단계": [
                "python -m cli list-steps 명령으로 사용 가능한 단계를 확인하세요",
                "단계 이름을 쉼표로 구분하여 입력하세요 (예: md_processing,qdrant_search)"
            ],
            "유효하지 않은 포맷": [
                "python -m cli list-formats 명령으로 지원하는 포맷을 확인하세요",
                "포맷 이름을 쉼표로 구분하여 입력하세요 (예: sharegpt,alpaca)"
            ],
            "양의 정수여야 합니다": [
                "1 이상의 정수를 입력하세요",
                "0이나 음수는 사용할 수 없습니다"
            ],
            "사이의 값이어야 합니다": [
                "지정된 범위 내의 값을 입력하세요",
                "소수점 형태로 입력하세요 (예: 0.7)"
            ],
            
            # 리소스 관련 오류
            "디렉토리가 존재하지 않습니다": [
                "mkdir -p <디렉토리명> 명령으로 디렉토리를 생성하세요",
                "설정 파일에서 올바른 디렉토리 경로를 지정하세요"
            ],
            "API 키가 설정되지 않았습니다": [
                "환경 변수 OPENAI_API_KEY를 설정하세요",
                "설정 파일에서 api_key 값을 지정하세요"
            ],
            
            # 네트워크 관련 오류
            "연결할 수 없습니다": [
                "네트워크 연결을 확인하세요",
                "API 서버 주소와 포트를 확인하세요",
                "방화벽 설정을 확인하세요"
            ],
            
            # 메모리 관련 오류
            "메모리 부족": [
                "배치 크기를 줄여보세요 (--batch-size 옵션)",
                "동시 요청 수를 줄여보세요 (--max-concurrent 옵션)",
                "테스트 모드로 소량 데이터를 처리해보세요 (--test-mode)"
            ]
        }
    
    def handle_exception(self, exc: Exception, context: Optional[Dict[str, Any]] = None) -> None:
        """
        예외를 처리하고 사용자 친화적인 메시지 출력
        
        Args:
            exc: 발생한 예외
            context: 추가 컨텍스트 정보
        """
        context = context or {}
        
        # CLI 관련 예외인 경우
        if isinstance(exc, CLIError):
            self._handle_cli_error(exc, context)
        # 일반적인 예외인 경우
        else:
            self._handle_generic_error(exc, context)
    
    def _handle_cli_error(self, exc: CLIError, context: Dict[str, Any]) -> None:
        """CLI 관련 오류 처리"""
        error_type = type(exc).__name__
        error_message = str(exc)
        
        # 오류 메시지 출력
        console.print(f"\n❌ {error_type}: {error_message}", style="bold red")
        
        # 제안사항 출력
        suggestions = exc.suggestions or self._get_suggestions(error_message)
        if suggestions:
            self._print_suggestions(suggestions)
        
        # 컨텍스트 정보 출력
        if context and self.verbose:
            self._print_context(context)
    
    def _handle_generic_error(self, exc: Exception, context: Dict[str, Any]) -> None:
        """일반적인 오류 처리"""
        error_type = type(exc).__name__
        error_message = str(exc)
        
        console.print(f"\n❌ {error_type}: {error_message}", style="bold red")
        
        # 알려진 오류 패턴에 대한 제안사항
        suggestions = self._get_suggestions(error_message)
        if suggestions:
            self._print_suggestions(suggestions)
        
        # 상세 정보 출력 (verbose 모드)
        if self.verbose:
            console.print("\n🔍 상세 오류 정보:", style="yellow")
            console.print(traceback.format_exc(), style="dim")
            
            if context:
                self._print_context(context)
    
    def _get_suggestions(self, error_message: str) -> List[str]:
        """오류 메시지에 기반한 제안사항 반환"""
        suggestions = []
        
        for pattern, pattern_suggestions in self.error_suggestions.items():
            if pattern in error_message:
                suggestions.extend(pattern_suggestions)
                break
        
        return suggestions
    
    def _print_suggestions(self, suggestions: List[str]) -> None:
        """제안사항 출력"""
        console.print("\n💡 해결 방법:", style="cyan")
        for i, suggestion in enumerate(suggestions, 1):
            console.print(f"  {i}. {suggestion}", style="cyan")
    
    def _print_context(self, context: Dict[str, Any]) -> None:
        """컨텍스트 정보 출력"""
        console.print("\n📋 컨텍스트 정보:", style="yellow")
        
        context_table = Table(show_header=False, box=None)
        context_table.add_column("키", style="yellow")
        context_table.add_column("값", style="white")
        
        for key, value in context.items():
            context_table.add_row(f"{key}:", str(value))
        
        console.print(context_table)
    
    def print_help_message(self, command: Optional[str] = None) -> None:
        """도움말 메시지 출력"""
        if command:
            console.print(f"\n📖 {command} 명령어 도움말을 보려면:", style="blue")
            console.print(f"  python -m cli {command} --help", style="blue")
        else:
            console.print("\n📖 전체 도움말을 보려면:", style="blue")
            console.print("  python -m cli --help", style="blue")
        
        console.print("\n🔗 추가 리소스:", style="blue")
        console.print("  • 설정 파일 생성: python -m cli create-config config.yaml", style="blue")
        console.print("  • 파이프라인 단계 확인: python -m cli list-steps", style="blue")
        console.print("  • 출력 포맷 확인: python -m cli list-formats", style="blue")
        console.print("  • 설정 파일 검증: python -m cli validate-config", style="blue")


def handle_keyboard_interrupt() -> None:
    """키보드 인터럽트 처리"""
    console.print("\n\n⚠️  사용자에 의해 중단되었습니다.", style="yellow")
    console.print("진행 중인 작업이 안전하게 중단되었습니다.", style="dim")


def handle_unexpected_error(exc: Exception, verbose: bool = False) -> None:
    """예상치 못한 오류 처리"""
    error_handler = ErrorHandler(verbose=verbose)
    
    console.print("\n💥 예상치 못한 오류가 발생했습니다!", style="bold red")
    
    if verbose:
        console.print("\n🔍 상세 오류 정보:", style="yellow")
        console.print(traceback.format_exc(), style="dim")
    
    console.print("\n💡 문제 해결 방법:", style="cyan")
    console.print("  1. --verbose 옵션으로 상세 로그를 확인하세요", style="cyan")
    console.print("  2. 설정 파일을 검증해보세요: python -m cli validate-config", style="cyan")
    console.print("  3. 테스트 모드로 소량 데이터를 처리해보세요: --test-mode", style="cyan")
    console.print("  4. 문제가 지속되면 GitHub 이슈를 등록해주세요", style="cyan")


def validate_parameters(
    steps: Optional[List[str]] = None,
    formats: Optional[List[str]] = None,
    target_count: Optional[int] = None,
    batch_size: Optional[int] = None,
    max_concurrent: Optional[int] = None,
    sample_size: Optional[int] = None,
    min_quality_score: Optional[float] = None
) -> None:
    """
    파라미터 유효성 검증
    
    Raises:
        ValidationError: 파라미터가 유효하지 않은 경우
    """
    # 단계 검증
    if steps:
        from cli.main import PIPELINE_STEPS
        invalid_steps = [step for step in steps if step not in PIPELINE_STEPS]
        if invalid_steps:
            raise ValidationError(
                f"유효하지 않은 파이프라인 단계: {', '.join(invalid_steps)}",
                suggestions=[
                    f"사용 가능한 단계: {', '.join(PIPELINE_STEPS)}",
                    "python -m cli list-steps 명령으로 확인하세요"
                ]
            )
    
    # 포맷 검증
    if formats:
        from cli.main import OUTPUT_FORMATS
        invalid_formats = [fmt for fmt in formats if fmt not in OUTPUT_FORMATS]
        if invalid_formats:
            raise ValidationError(
                f"유효하지 않은 출력 포맷: {', '.join(invalid_formats)}",
                suggestions=[
                    f"사용 가능한 포맷: {', '.join(OUTPUT_FORMATS)}",
                    "python -m cli list-formats 명령으로 확인하세요"
                ]
            )
    
    # 양의 정수 검증
    positive_int_params = {
        "target_count": target_count,
        "batch_size": batch_size,
        "max_concurrent": max_concurrent,
        "sample_size": sample_size
    }
    
    for param_name, value in positive_int_params.items():
        if value is not None and value <= 0:
            raise ValidationError(
                f"{param_name}은(는) 양의 정수여야 합니다: {value}",
                suggestions=[
                    "1 이상의 정수를 입력하세요",
                    "0이나 음수는 사용할 수 없습니다"
                ]
            )
    
    # 품질 점수 검증
    if min_quality_score is not None and not (0.0 <= min_quality_score <= 1.0):
        raise ValidationError(
            f"min_quality_score는 0.0과 1.0 사이의 값이어야 합니다: {min_quality_score}",
            suggestions=[
                "0.0과 1.0 사이의 소수를 입력하세요",
                "예시: 0.7, 0.8, 0.9"
            ]
        )


def check_system_requirements() -> List[str]:
    """
    시스템 요구사항 확인
    
    Returns:
        List[str]: 경고 메시지 목록
    """
    warnings = []
    
    # Python 버전 확인
    if sys.version_info < (3, 8):
        warnings.append("Python 3.8 이상이 권장됩니다")
    
    # 메모리 확인 (psutil이 있는 경우)
    try:
        import psutil
        memory = psutil.virtual_memory()
        if memory.total < 4 * 1024 * 1024 * 1024:  # 4GB
            warnings.append("메모리가 4GB 미만입니다. 성능에 영향을 줄 수 있습니다")
    except ImportError:
        pass
    
    # 디스크 공간 확인
    try:
        import shutil
        free_space = shutil.disk_usage(".").free
        if free_space < 1 * 1024 * 1024 * 1024:  # 1GB
            warnings.append("디스크 여유 공간이 1GB 미만입니다")
    except Exception:
        pass
    
    return warnings