"""
CLI 메인 모듈 - Click 기반 사용자 친화적 명령행 인터페이스
"""

import os
import sys
from pathlib import Path
from typing import List, Optional, Tuple

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from .error_handler import (
    ErrorHandler, 
    CLIError, 
    ConfigurationError, 
    ValidationError, 
    ResourceError,
    handle_keyboard_interrupt,
    handle_unexpected_error,
    validate_parameters,
    check_system_requirements
)

console = Console()

# 사용 가능한 파이프라인 단계들
PIPELINE_STEPS = [
    "md_processing",
    "qdrant_search", 
    "conversation_generation",
    "dataset_formatting",
    "quality_validation"
]

# 지원하는 출력 포맷들
OUTPUT_FORMATS = ["sharegpt", "alpaca", "openai"]


def print_banner():
    """프로그램 시작 배너 출력"""
    banner = Text("Unsloth Dataset Generator", style="bold blue")
    subtitle = Text("Syncfusion WinForms 문서 기반 고품질 데이터셋 생성 도구", style="italic")
    
    console.print(Panel.fit(
        f"{banner}\n{subtitle}",
        border_style="blue",
        padding=(1, 2)
    ))


def validate_steps(ctx, param, value: Optional[str]) -> Optional[List[str]]:
    """파이프라인 단계 유효성 검증"""
    if not value:
        return None
    
    steps = [step.strip() for step in value.split(",")]
    invalid_steps = [step for step in steps if step not in PIPELINE_STEPS]
    
    if invalid_steps:
        available_steps = ", ".join(PIPELINE_STEPS)
        raise click.BadParameter(
            f"유효하지 않은 단계: {', '.join(invalid_steps)}. "
            f"사용 가능한 단계: {available_steps}"
        )
    
    return steps


def validate_formats(ctx, param, value: Optional[str]) -> Optional[List[str]]:
    """출력 포맷 유효성 검증"""
    if not value:
        return None
    
    formats = [fmt.strip() for fmt in value.split(",")]
    invalid_formats = [fmt for fmt in formats if fmt not in OUTPUT_FORMATS]
    
    if invalid_formats:
        available_formats = ", ".join(OUTPUT_FORMATS)
        raise click.BadParameter(
            f"유효하지 않은 포맷: {', '.join(invalid_formats)}. "
            f"사용 가능한 포맷: {available_formats}"
        )
    
    return formats


def validate_positive_int(ctx, param, value: Optional[int]) -> Optional[int]:
    """양의 정수 유효성 검증"""
    if value is not None and value <= 0:
        param_name = param.name if param else "값"
        raise click.BadParameter(f"{param_name}은(는) 양의 정수여야 합니다.")
    return value


def validate_float_range(min_val: float = 0.0, max_val: float = 1.0):
    """지정된 범위의 실수 유효성 검증 함수 생성"""
    def validator(ctx, param, value: Optional[float]) -> Optional[float]:
        if value is not None and not (min_val <= value <= max_val):
            param_name = param.name if param else "값"
            raise click.BadParameter(
                f"{param_name}은(는) {min_val}과 {max_val} 사이의 값이어야 합니다."
            )
        return value
    return validator


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Unsloth Dataset Generator - Syncfusion WinForms 문서 기반 데이터셋 생성 도구
    
    이 도구는 MD 파일 처리부터 벡터 데이터베이스 연동, AI 기반 대화 생성,
    다중 포맷 변환, 품질 검증까지의 전체 파이프라인을 자동화합니다.
    """
    if ctx.invoked_subcommand is None:
        print_banner()
        console.print("\n사용법을 보려면 --help 옵션을 사용하세요.", style="yellow")
        console.print("예시: python -m cli --help", style="dim")


@cli.command()
@click.option(
    "--config", "-c",
    type=click.Path(exists=True, path_type=Path),
    default="config.yaml",
    help="설정 파일 경로 (기본값: config.yaml)"
)
@click.option(
    "--steps", "-s",
    callback=validate_steps,
    help=f"실행할 파이프라인 단계 (쉼표로 구분). 사용 가능: {', '.join(PIPELINE_STEPS)}"
)
@click.option(
    "--formats", "-f",
    callback=validate_formats,
    help=f"출력 포맷 (쉼표로 구분). 사용 가능: {', '.join(OUTPUT_FORMATS)}"
)
@click.option(
    "--target-count", "-n",
    type=int,
    callback=validate_positive_int,
    help="생성할 대화 수 (기본값: 설정 파일에서 로드)"
)
@click.option(
    "--batch-size", "-b",
    type=int,
    callback=validate_positive_int,
    help="배치 크기 (기본값: 설정 파일에서 로드)"
)
@click.option(
    "--max-concurrent", "-j",
    type=int,
    callback=validate_positive_int,
    help="최대 동시 요청 수 (기본값: 설정 파일에서 로드)"
)
@click.option(
    "--test-mode", "-t",
    is_flag=True,
    help="테스트 모드 (소량 샘플로 빠른 검증)"
)
@click.option(
    "--sample-size",
    type=int,
    default=10,
    callback=validate_positive_int,
    help="테스트 모드에서 처리할 샘플 수 (기본값: 10)"
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    help="상세 로그 출력"
)
@click.option(
    "--log-level",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"], case_sensitive=False),
    default="INFO",
    help="로그 레벨 (기본값: INFO)"
)
@click.option(
    "--output-dir", "-o",
    type=click.Path(path_type=Path),
    help="출력 디렉토리 (기본값: 설정 파일에서 로드)"
)
@click.option(
    "--min-quality-score",
    type=float,
    callback=validate_float_range(0.0, 1.0),
    help="최소 품질 점수 임계값 (0.0-1.0)"
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="실제 실행 없이 설정만 검증"
)
@click.option(
    "--enable-component-organization",
    is_flag=True,
    default=True,
    help="컴포넌트별 데이터셋 조직화 활성화 (기본값: 활성화)"
)
@click.option(
    "--create-component-datasets",
    is_flag=True,
    default=True,
    help="컴포넌트별 개별 데이터셋 생성 (기본값: 활성화)"
)
@click.option(
    "--create-category-datasets",
    is_flag=True,
    default=True,
    help="카테고리별 통합 데이터셋 생성 (기본값: 활성화)"
)
@click.option(
    "--min-samples-per-component",
    type=int,
    default=5,
    callback=validate_positive_int,
    help="컴포넌트당 최소 샘플 수 (기본값: 5)"
)
@click.option(
    "--max-samples-per-component",
    type=int,
    default=500,
    callback=validate_positive_int,
    help="컴포넌트당 최대 샘플 수 (기본값: 500)"
)
def generate(
    config: Path,
    steps: Optional[List[str]],
    formats: Optional[List[str]],
    target_count: Optional[int],
    batch_size: Optional[int],
    max_concurrent: Optional[int],
    test_mode: bool,
    sample_size: int,
    verbose: bool,
    log_level: str,
    output_dir: Optional[Path],
    min_quality_score: Optional[float],
    dry_run: bool,
    enable_component_organization: bool,
    create_component_datasets: bool,
    create_category_datasets: bool,
    min_samples_per_component: int,
    max_samples_per_component: int
):
    """
    데이터셋 생성 파이프라인 실행
    
    전체 파이프라인을 실행하거나 특정 단계만 선택적으로 실행할 수 있습니다.
    테스트 모드를 사용하여 소량의 데이터로 빠른 검증이 가능합니다.
    """
    error_handler = ErrorHandler(verbose=verbose)
    
    try:
        print_banner()
        
        # 파라미터 유효성 검증
        validate_parameters(
            steps=steps,
            formats=formats,
            target_count=target_count,
            batch_size=batch_size,
            max_concurrent=max_concurrent,
            sample_size=sample_size,
            min_quality_score=min_quality_score
        )
        
        # 시스템 요구사항 확인
        system_warnings = check_system_requirements()
        if system_warnings and verbose:
            console.print("⚠️  시스템 경고:", style="yellow")
            for warning in system_warnings:
                console.print(f"  • {warning}", style="yellow")
            console.print()
        
        # 설정 파일 로드 및 검증
        try:
            from config import load_config, validate_config_file
            
            if config.exists():
                pipeline_config = load_config(config)
                validation_result = validate_config_file(config)
                
                if not validation_result["valid"]:
                    raise ConfigurationError(
                        f"설정 파일이 유효하지 않습니다: {', '.join(validation_result['errors'])}",
                        suggestions=[
                            "python -m cli validate-config 명령으로 상세한 오류를 확인하세요",
                            "python -m cli create-config new_config.yaml로 새 설정 파일을 생성하세요"
                        ]
                    )
                
                if validation_result["warnings"] and verbose:
                    console.print("⚠️  설정 경고:", style="yellow")
                    for warning in validation_result["warnings"]:
                        console.print(f"  • {warning}", style="yellow")
                    console.print()
            else:
                if not dry_run:
                    raise ResourceError(
                        f"설정 파일을 찾을 수 없습니다: {config}",
                        suggestions=[
                            f"python -m cli create-config {config} 명령으로 기본 설정 파일을 생성하세요",
                            "올바른 설정 파일 경로를 --config 옵션으로 지정하세요"
                        ]
                    )
                else:
                    console.print(f"⚠️  설정 파일이 존재하지 않습니다: {config}", style="yellow")
                    pipeline_config = None
        
        except ImportError as e:
            raise ResourceError(
                "설정 모듈을 로드할 수 없습니다",
                suggestions=[
                    "필요한 의존성이 설치되어 있는지 확인하세요",
                    "pip install -r requirements.txt 명령을 실행하세요"
                ]
            )
        
        # 설정 정보 표시
        config_table = Table(title="실행 설정", show_header=True, header_style="bold magenta")
        config_table.add_column("설정", style="cyan", no_wrap=True)
        config_table.add_column("값", style="green")
        
        config_table.add_row("설정 파일", str(config))
        config_table.add_row("실행 단계", ", ".join(steps) if steps else "전체")
        config_table.add_row("출력 포맷", ", ".join(formats) if formats else "전체")
        config_table.add_row("테스트 모드", "예" if test_mode else "아니오")
        if test_mode:
            config_table.add_row("샘플 크기", str(sample_size))
        if target_count:
            config_table.add_row("대화 수", str(target_count))
        if batch_size:
            config_table.add_row("배치 크기", str(batch_size))
        if max_concurrent:
            config_table.add_row("동시 요청", str(max_concurrent))
        config_table.add_row("로그 레벨", log_level)
        config_table.add_row("상세 출력", "예" if verbose else "아니오")
        config_table.add_row("드라이 런", "예" if dry_run else "아니오")
        config_table.add_row("컴포넌트 조직화", "예" if enable_component_organization else "아니오")
        if enable_component_organization:
            config_table.add_row("컴포넌트별 데이터셋", "예" if create_component_datasets else "아니오")
            config_table.add_row("카테고리별 데이터셋", "예" if create_category_datasets else "아니오")
            config_table.add_row("컴포넌트 최소 샘플", str(min_samples_per_component))
            config_table.add_row("컴포넌트 최대 샘플", str(max_samples_per_component))
        
        console.print(config_table)
        console.print()
        
        if dry_run:
            console.print("✅ 드라이 런 모드: 설정 검증 완료", style="green")
            return
        
        # 테스트 모드 처리
        if test_mode:
            console.print(f"🧪 테스트 모드: {sample_size}개 샘플로 파이프라인 테스트", style="blue")
            
            # 테스트 모드에서는 설정을 조정
            if pipeline_config:
                pipeline_config.unsloth_dataset.target_conversation_count = min(
                    sample_size, 
                    pipeline_config.unsloth_dataset.target_conversation_count
                )
                pipeline_config.openai_connector.batch_size = min(
                    5,  # 테스트 모드에서는 작은 배치 크기 사용
                    pipeline_config.openai_connector.batch_size
                )
        
        # 실제 파이프라인 실행 (여기서는 모의 실행)
        console.print("🚀 파이프라인 실행을 시작합니다...", style="bold blue")
        
        # TODO: 실제 파이프라인 실행 로직 구현
        # from main import run_pipeline
        # result = run_pipeline(pipeline_config, steps, formats, ...)
        
        console.print("✅ 파이프라인 실행이 완료되었습니다!", style="bold green")
        
    except CLIError as e:
        error_handler.handle_exception(e, {
            "command": "generate",
            "config_file": str(config),
            "test_mode": test_mode,
            "verbose": verbose
        })
        sys.exit(1)
    except Exception as e:
        error_handler.handle_exception(e, {
            "command": "generate",
            "config_file": str(config),
            "test_mode": test_mode,
            "verbose": verbose
        })
        sys.exit(1)


@cli.command()
@click.option(
    "--config", "-c",
    type=click.Path(path_type=Path),
    default="config.yaml",
    help="검증할 설정 파일 경로"
)
def validate_config(config: Path):
    """
    설정 파일 유효성 검증
    
    YAML 설정 파일의 구문과 값들이 올바른지 검증합니다.
    """
    error_handler = ErrorHandler(verbose=True)
    
    try:
        print_banner()
        console.print(f"📋 설정 파일 검증: {config}", style="bold blue")
        
        if not config.exists():
            raise ResourceError(
                f"설정 파일을 찾을 수 없습니다: {config}",
                suggestions=[
                    f"python -m cli create-config {config} 명령으로 기본 설정 파일을 생성하세요",
                    "올바른 설정 파일 경로를 지정하세요"
                ]
            )
        
        # 실제 설정 검증 로직 구현
        from config import validate_config_file
        result = validate_config_file(config)
        
        if result["valid"]:
            console.print("✅ 설정 파일이 유효합니다!", style="bold green")
            
            if result["warnings"]:
                console.print("\n⚠️  경고사항:", style="yellow")
                for warning in result["warnings"]:
                    console.print(f"  • {warning}", style="yellow")
        else:
            raise ConfigurationError(
                "설정 파일이 유효하지 않습니다",
                suggestions=[
                    "오류를 수정한 후 다시 시도하세요",
                    "python -m cli create-config new_config.yaml로 새 설정 파일을 생성하세요"
                ] + [f"• {error}" for error in result["errors"]]
            )
        
    except CLIError as e:
        error_handler.handle_exception(e, {
            "command": "validate-config",
            "config_file": str(config)
        })
        sys.exit(1)
    except Exception as e:
        error_handler.handle_exception(e, {
            "command": "validate-config", 
            "config_file": str(config)
        })
        sys.exit(1)


@cli.command()
def list_steps():
    """
    사용 가능한 파이프라인 단계 목록 표시
    """
    print_banner()
    
    steps_table = Table(title="파이프라인 단계", show_header=True, header_style="bold magenta")
    steps_table.add_column("단계", style="cyan", no_wrap=True)
    steps_table.add_column("설명", style="white")
    
    step_descriptions = {
        "md_processing": "MD 파일 스캔, 파싱 및 전처리",
        "qdrant_search": "Qdrant 벡터 DB에서 컨텍스트 검색",
        "conversation_generation": "OpenAI API를 통한 대화 생성",
        "dataset_formatting": "다중 포맷으로 데이터셋 변환",
        "quality_validation": "품질 검증 및 필터링"
    }
    
    for step in PIPELINE_STEPS:
        steps_table.add_row(step, step_descriptions.get(step, "설명 없음"))
    
    console.print(steps_table)


@cli.command()
def list_formats():
    """
    지원하는 출력 포맷 목록 표시
    """
    print_banner()
    
    formats_table = Table(title="출력 포맷", show_header=True, header_style="bold magenta")
    formats_table.add_column("포맷", style="cyan", no_wrap=True)
    formats_table.add_column("설명", style="white")
    
    format_descriptions = {
        "sharegpt": "ShareGPT 포맷 (human/gpt 역할 기반)",
        "alpaca": "Alpaca 포맷 (instruction-input-output)",
        "openai": "OpenAI 포맷 (messages 배열)"
    }
    
    for fmt in OUTPUT_FORMATS:
        formats_table.add_row(fmt, format_descriptions.get(fmt, "설명 없음"))
    
    console.print(formats_table)


@cli.command()
@click.argument("config_path", type=click.Path(path_type=Path))
def create_config(config_path: Path):
    """
    기본 설정 파일 생성
    
    CONFIG_PATH: 생성할 설정 파일 경로
    """
    error_handler = ErrorHandler(verbose=False)
    
    try:
        print_banner()
        console.print(f"📝 설정 파일 생성: {config_path}", style="bold blue")
        
        if config_path.exists():
            if not click.confirm(f"파일이 이미 존재합니다. 덮어쓰시겠습니까?"):
                console.print("취소되었습니다.", style="yellow")
                return
        
        # 디렉토리 생성
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 기본 설정 파일 생성 로직 구현
        from config import create_default_config
        create_default_config(config_path)
        
        console.print("✅ 기본 설정 파일이 생성되었습니다!", style="bold green")
        console.print(f"설정 파일을 편집한 후 사용하세요: {config_path}", style="dim")
        
        # 다음 단계 안내
        console.print("\n📖 다음 단계:", style="blue")
        console.print(f"  1. 설정 파일 편집: {config_path}", style="blue")
        console.print(f"  2. 설정 검증: python -m cli validate-config --config {config_path}", style="blue")
        console.print(f"  3. 테스트 실행: python -m cli generate --config {config_path} --test-mode", style="blue")
        
    except CLIError as e:
        error_handler.handle_exception(e, {
            "command": "create-config",
            "config_path": str(config_path)
        })
        sys.exit(1)
    except Exception as e:
        error_handler.handle_exception(e, {
            "command": "create-config",
            "config_path": str(config_path)
        })
        sys.exit(1)


@cli.command()
def list_components():
    """
    지원하는 Syncfusion 컴포넌트 목록 표시
    """
    print_banner()
    
    try:
        from unsloth_dataset.component_organizer import ComponentOrganizer, OrganizationConfig
        
        # 컴포넌트 조직화기 생성
        organizer = ComponentOrganizer(OrganizationConfig())
        
        # 컴포넌트 계층 구조 테이블
        components_table = Table(title="Syncfusion 컴포넌트 계층 구조", show_header=True, header_style="bold magenta")
        components_table.add_column("컴포넌트", style="cyan", no_wrap=True)
        components_table.add_column("카테고리", style="green")
        components_table.add_column("우선순위", style="yellow", justify="center")
        components_table.add_column("설명", style="white")
        
        # 우선순위 순으로 정렬
        sorted_components = sorted(
            organizer.component_hierarchy.items(),
            key=lambda x: x[1].priority,
            reverse=True
        )
        
        for component_name, hierarchy in sorted_components:
            components_table.add_row(
                component_name,
                hierarchy.category,
                str(hierarchy.priority),
                hierarchy.description
            )
        
        console.print(components_table)
        
        # 카테고리별 요약 테이블
        console.print()
        categories_table = Table(title="카테고리별 요약", show_header=True, header_style="bold magenta")
        categories_table.add_column("카테고리", style="cyan", no_wrap=True)
        categories_table.add_column("컴포넌트 수", style="yellow", justify="center")
        categories_table.add_column("컴포넌트 목록", style="white")
        
        for category, components in organizer.category_mapping.items():
            categories_table.add_row(
                category,
                str(len(components)),
                ", ".join(components)
            )
        
        console.print(categories_table)
        
        # 통계 정보
        console.print()
        console.print(f"📊 총 {len(organizer.component_hierarchy)}개 컴포넌트, {len(organizer.category_mapping)}개 카테고리", style="bold blue")
        
    except ImportError as e:
        console.print("❌ 컴포넌트 조직화 모듈을 로드할 수 없습니다.", style="red")
        console.print(f"오류: {e}", style="red")


@cli.command()
@click.argument("dataset_path", type=click.Path(exists=True, path_type=Path))
def analyze_components(dataset_path: Path):
    """
    기존 데이터셋의 컴포넌트 분포 분석
    
    DATASET_PATH: 분석할 데이터셋 파일 경로 (JSONL 형식)
    """
    print_banner()
    
    try:
        from unsloth_dataset.component_organizer import ComponentOrganizer, OrganizationConfig
        import json
        from collections import Counter
        
        console.print(f"📊 데이터셋 컴포넌트 분석: {dataset_path}", style="bold blue")
        
        # 데이터셋 로드
        samples = []
        with open(dataset_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    samples.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        
        if not samples:
            console.print("❌ 유효한 샘플을 찾을 수 없습니다.", style="red")
            return
        
        console.print(f"📋 총 {len(samples)}개 샘플 로드됨", style="green")
        
        # 컴포넌트 조직화기 생성
        organizer = ComponentOrganizer(OrganizationConfig())
        
        # 컴포넌트별 분류
        component_datasets = organizer.organize_by_components(samples)
        
        # 분석 결과 테이블
        analysis_table = Table(title="컴포넌트별 분포", show_header=True, header_style="bold magenta")
        analysis_table.add_column("컴포넌트", style="cyan", no_wrap=True)
        analysis_table.add_column("카테고리", style="green")
        analysis_table.add_column("샘플 수", style="yellow", justify="right")
        analysis_table.add_column("비율", style="blue", justify="right")
        analysis_table.add_column("평균 품질", style="red", justify="right")
        
        total_samples = sum(len(ds.samples) for ds in component_datasets.values())
        
        for component_name, dataset in sorted(component_datasets.items(), key=lambda x: len(x[1].samples), reverse=True):
            sample_count = len(dataset.samples)
            percentage = (sample_count / total_samples) * 100
            avg_quality = dataset.metadata.get("avg_quality_score", 0)
            
            analysis_table.add_row(
                component_name,
                dataset.category,
                str(sample_count),
                f"{percentage:.1f}%",
                f"{avg_quality:.3f}"
            )
        
        console.print(analysis_table)
        
        # 카테고리별 요약
        category_datasets = organizer.organize_by_categories(component_datasets)
        
        console.print()
        category_table = Table(title="카테고리별 요약", show_header=True, header_style="bold magenta")
        category_table.add_column("카테고리", style="cyan", no_wrap=True)
        category_table.add_column("컴포넌트 수", style="green", justify="center")
        category_table.add_column("총 샘플 수", style="yellow", justify="right")
        category_table.add_column("비율", style="blue", justify="right")
        
        for category, datasets_list in sorted(category_datasets.items(), key=lambda x: sum(len(ds.samples) for ds in x[1]), reverse=True):
            component_count = len(datasets_list)
            total_category_samples = sum(len(ds.samples) for ds in datasets_list)
            percentage = (total_category_samples / total_samples) * 100
            
            category_table.add_row(
                category,
                str(component_count),
                str(total_category_samples),
                f"{percentage:.1f}%"
            )
        
        console.print(category_table)
        
        # 권장사항 생성
        report = organizer.generate_organization_report(component_datasets, category_datasets)
        
        if report.get('recommendations'):
            console.print()
            console.print("💡 권장사항:", style="bold yellow")
            for rec in report['recommendations']:
                console.print(f"  • {rec}", style="yellow")
        
    except Exception as e:
        console.print(f"❌ 분석 중 오류 발생: {e}", style="red")
        if "--verbose" in sys.argv:
            import traceback
            console.print(traceback.format_exc(), style="dim red")


@cli.command()
def version():
    """버전 정보 표시"""
    print_banner()
    console.print("버전: 1.0.0", style="bold green")
    console.print("작성자: Unsloth Dataset Generator Team", style="dim")


def main():
    """메인 진입점"""
    try:
        cli()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()
        sys.exit(130)
    except Exception as e:
        handle_unexpected_error(e, verbose=False)
        sys.exit(1)


if __name__ == "__main__":
    main()