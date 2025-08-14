#!/usr/bin/env python3
"""
MD 처리 모듈 초기화 파일
로컬 MD 파일 처리를 위한 핵심 모듈을 제공합니다.
"""

from .scanner import MDFileScanner, create_scanner, FileMetadata
from .parser import MDParser, create_parser, DocumentMetadata, ContentPreprocessor, MetadataExtractor
from .processor import MDProcessor, create_processor, ProcessingConfig, ProcessingStats
from .utils import (
    setup_logging,
    normalize_text,
    clean_filename,
    generate_unique_id,
    extract_metadata_from_content,
    calculate_content_stats,
    validate_document_structure,
    merge_documents,
    save_documents_to_json,
    load_documents_from_json,
    create_directory_structure,
    get_file_info,
    format_file_size,
    is_valid_md_file,
    batch_process
)

__version__ = "1.0.0"
__author__ = "MD Processor Team"
__email__ = "support@example.com"
__description__ = "Local MD File Processing Module for Syncfusion WinForms Documentation"

__all__ = [
    # Scanner
    'MDFileScanner',
    'create_scanner',
    'FileMetadata',
    
    # Parser
    'MDParser',
    'create_parser',
    'DocumentMetadata',
    'ContentPreprocessor',
    'MetadataExtractor',
    
    # Processor
    'MDProcessor',
    'create_processor',
    'create_md_processor',
    'MDProcessorConfig',
    'ProcessingConfig',
    'ProcessingStats',
    
    # Utils
    'setup_logging',
    'normalize_text',
    'clean_filename',
    'generate_unique_id',
    'extract_metadata_from_content',
    'calculate_content_stats',
    'validate_document_structure',
    'merge_documents',
    'save_documents_to_json',
    'load_documents_from_json',
    'create_directory_structure',
    'get_file_info',
    'format_file_size',
    'is_valid_md_file',
    'batch_process',
    
    # Version info
    '__version__',
    '__author__',
    '__email__',
    '__description__'
]


def create_md_processor(config=None) -> MDProcessor:
    """
    MD 프로세서를 생성합니다.
    
    Args:
        config: MDProcessorConfig 또는 ProcessingConfig 인스턴스
        
    Returns:
        생성된 MDProcessor 인스턴스
    """
    if config is None:
        # 기본 설정 사용
        processing_config = ProcessingConfig(
            batch_size=100,
            min_quality_score=0.1,
            max_content_length=50000,
            remove_duplicates=True,
            output_format="json",
            include_metadata=True,
            progress_interval=10
        )
    elif hasattr(config, 'base_paths'):
        # MDProcessorConfig 타입인 경우
        processing_config = ProcessingConfig(
            batch_size=getattr(config, 'batch_size', 100),
            min_quality_score=getattr(config, 'min_quality_score', 0.1),
            max_content_length=getattr(config, 'max_content_length', 50000),
            remove_duplicates=getattr(config, 'remove_duplicates', True),
            output_format=getattr(config, 'output_format', "json"),
            include_metadata=getattr(config, 'include_metadata', True),
            progress_interval=getattr(config, 'progress_interval', 10)
        )
    else:
        # ProcessingConfig 타입인 경우
        processing_config = config
    
    return create_processor(processing_config)


# MDProcessorConfig 클래스 정의
class MDProcessorConfig:
    """MD 프로세서 설정 클래스"""
    
    def __init__(self, base_paths=None, output_path="output", max_files=None, 
                 enable_api_extraction=True, enable_code_extraction=True,
                 batch_size=100, min_quality_score=0.1, max_content_length=50000,
                 remove_duplicates=True, output_format="json", include_metadata=True,
                 progress_interval=10):
        self.base_paths = base_paths or ["md_staging"]
        self.output_path = output_path
        self.max_files = max_files
        self.enable_api_extraction = enable_api_extraction
        self.enable_code_extraction = enable_code_extraction
        self.batch_size = batch_size
        self.min_quality_score = min_quality_score
        self.max_content_length = max_content_length
        self.remove_duplicates = remove_duplicates
        self.output_format = output_format
        self.include_metadata = include_metadata
        self.progress_interval = progress_interval


def create_default_processor() -> MDProcessor:
    """
    기본 설정으로 MD 프로세서를 생성합니다.
    
    Returns:
        기본 설정으로 생성된 MDProcessor 인스턴스
    """
    config = ProcessingConfig(
        batch_size=100,
        min_quality_score=0.1,
        max_content_length=50000,
        remove_duplicates=True,
        output_format="json",
        include_metadata=True,
        progress_interval=10
    )
    return create_processor(config)


def process_documents_simple(output_path: str = "processed_documents.json", 
                           base_paths: list = None) -> list:
    """
    간단한 인터페이스로 문서를 처리합니다.
    
    Args:
        output_path: 출력 파일 경로
        base_paths: 스캔할 기본 경로 목록
        
    Returns:
        처리된 문서 목록
    """
    if base_paths is None:
        base_paths = ['./output', './md_staging']
    
    processor = create_default_processor()
    return processor.process_documents(Path(output_path))


def get_processing_stats() -> dict:
    """
    처리 통계 정보를 가져옵니다.
    
    Returns:
        처리 통계 딕셔너리
    """
    scanner = create_scanner()
    return scanner.get_scan_statistics()


def quick_scan() -> dict:
    """
    빠른 스캔을 수행합니다.
    
    Returns:
        스캔 결과 요약
    """
    scanner = create_scanner()
    
    # 기본 스캔 통계
    stats = scanner.get_scan_statistics()
    
    # 컴포넌트 파일 목록
    component_files = list(scanner.get_component_files())
    stats['component_files_list'] = [f.name for f, _ in component_files[:10]]  # 최대 10개
    
    # 페이지 파일 목록
    page_files = list(scanner.get_page_files())
    stats['page_files_list'] = [
        f"{f.name} -> {j.name if j.exists() else 'No JSON'}" 
        for f, j, _, _ in page_files[:10]  # 최대 10개
    ]
    
    return stats


# 모듈 로드 시 기본 로깅 설정
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


# 모듈 정보 출력
def print_module_info():
    """모듈 정보를 출력합니다."""
    print(f"MD Processor Module v{__version__}")
    print(f"Author: {__author__}")
    print(f"Description: {__description__}")
    print(f"Available components:")
    print(f"  - Scanner: MD file scanning and metadata extraction")
    print(f"  - Parser: MD content parsing and preprocessing")
    print(f"  - Processor: Main processing pipeline")
    print(f"  - Utils: Utility functions and helpers")


if __name__ == "__main__":
    # 모듈 정보 출력
    print_module_info()
    
    # 빠른 스캔 테스트
    print("\n=== Quick Scan Test ===")
    try:
        scan_result = quick_scan()
        print(f"Total MD files: {scan_result.get('total_md_files', 0)}")
        print(f"Total JSON files: {scan_result.get('total_json_files', 0)}")
        print(f"Component files: {scan_result.get('component_files', 0)}")
        print(f"Page files: {scan_result.get('page_files', 0)}")
        print(f"Directories scanned: {scan_result.get('directories_scanned', 0)}")
    except Exception as e:
        print(f"Quick scan failed: {e}")
    
    print("\n=== Module Ready ===")
    print("Use process_documents_simple() to start processing documents.")