#!/usr/bin/env python3
"""
MD 파일 스캐너 모듈
지정된 경로에서 MD 파일을 재귀적으로 검색하고 파일 메타데이터를 추출합니다.
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Generator, Tuple
from datetime import datetime
import logging
import hashlib

logger = logging.getLogger(__name__)


class FileMetadata:
    """파일 메타데이터 정보"""
    
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.file_size = file_path.stat().st_size
        self.last_modified = datetime.fromtimestamp(file_path.stat().st_mtime)
        self.file_hash = self._calculate_hash()
        
    def _calculate_hash(self) -> str:
        """파일 해시 계산"""
        hash_sha256 = hashlib.sha256()
        try:
            with open(self.file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except Exception as e:
            logger.warning(f"Failed to calculate hash for {self.file_path}: {e}")
            return ""
    
    def to_dict(self) -> Dict[str, Any]:
        """메타데이터를 딕셔너리로 변환"""
        return {
            "file_path": str(self.file_path),
            "file_size": self.file_size,
            "last_modified": self.last_modified.isoformat(),
            "file_hash": self.file_hash
        }


class MDFileScanner:
    """MD 파일 스캐너 클래스"""
    
    def __init__(self, base_paths: List[str]):
        """
        초기화
        
        Args:
            base_paths: 스캔할 기본 경로 목록
        """
        # 경로 정규화
        normalized_paths = []
        for path in base_paths:
            # 절대 경로로 변환
            abs_path = Path(path).resolve()
            # 경로가 존재하지 않으면 현재 작업 디렉토리 기준으로 생성
            if not abs_path.exists():
                if 'output' in path:
                    abs_path = Path.cwd() / 'output'
                elif 'md_staging' in path:
                    abs_path = Path.cwd() / 'md_staging'
                else:
                    abs_path = Path.cwd() / path
            
            # 디렉토리가 존재하지 않으면 생성
            if abs_path.is_dir() or abs_path.suffix.lower() in {'.md', '.markdown'}:
                normalized_paths.append(abs_path)
            else:
                # 디렉토리가 존재하지 않으면 생성 시도
                try:
                    abs_path.mkdir(parents=True, exist_ok=True)
                    normalized_paths.append(abs_path)
                except Exception as e:
                    logger.warning(f"Cannot create directory {abs_path}: {e}")
        
        self.base_paths = normalized_paths
        self.supported_extensions = {'.md', '.markdown'}
        
    def scan_files(self, recursive: bool = True) -> Generator[Tuple[Path, FileMetadata], None, None]:
        """
        MD 파일을 스캔합니다.
        
        Args:
            recursive: 재귀적으로 스캔할지 여부
            
        Yields:
            (파일 경로, 메타데이터) 튜플
        """
        for base_path in self.base_paths:
            if not base_path.exists():
                logger.warning(f"Base path does not exist: {base_path}")
                continue
                
            logger.info(f"Scanning directory: {base_path}")
            
            if base_path.is_file():
                if base_path.suffix.lower() in self.supported_extensions:
                    yield base_path, FileMetadata(base_path)
            else:
                if recursive:
                    for file_path in base_path.rglob("*.md"):
                        yield file_path, FileMetadata(file_path)
                else:
                    for file_path in base_path.glob("*.md"):
                        yield file_path, FileMetadata(file_path)
    
    def find_md_json_pairs(self) -> Generator[Tuple[Path, Path, FileMetadata, Optional[FileMetadata]], None, None]:
        """
        MD 파일과 해당하는 JSON 파일 쌍을 찾습니다.
        
        Yields:
            (md_경로, json_경로, md_메타데이터, json_메타데이터) 튜플
        """
        for md_path, md_metadata in self.scan_files():
            json_path = md_path.with_suffix('.json')
            json_metadata = None
            
            if json_path.exists():
                json_metadata = FileMetadata(json_path)
            
            yield md_path, json_path, md_metadata, json_metadata
    
    def get_component_files(self) -> Generator[Tuple[Path, FileMetadata], None, None]:
        """
        컴포넌트 단위 파일 (./output/{컴포넌트}.md)을 찾습니다.
        
        Yields:
            (파일 경로, 메타데이터) 튜플
        """
        # output 디렉토리가 base_paths에 있는지 확인
        output_path = None
        for base_path in self.base_paths:
            if base_path.name == "output" or "output" in str(base_path):
                output_path = base_path
                break
        
        if not output_path:
            output_path = Path("output")
        
        if not output_path.exists():
            logger.warning(f"Output directory does not exist: {output_path}")
            return
            
        for file_path in output_path.glob("*.md"):
            if file_path.is_file():
                yield file_path, FileMetadata(file_path)
    
    def get_page_files(self) -> Generator[Tuple[Path, Path, FileMetadata, Optional[FileMetadata]], None, None]:
        """
        페이지 단위 파일 (./md_staging/{컴포넌트}/{페이지}.md)을 찾습니다.
        
        Yields:
            (md_경로, json_경로, md_메타데이터, json_메타데이터) 튜플
        """
        # md_staging 디렉토리가 base_paths에 있는지 확인
        md_staging_path = None
        for base_path in self.base_paths:
            if base_path.name == "md_staging" or "md_staging" in str(base_path):
                md_staging_path = base_path
                break
        
        if not md_staging_path:
            md_staging_path = Path("md_staging")
        
        if not md_staging_path.exists():
            logger.warning(f"MD staging directory does not exist: {md_staging_path}")
            return
            
        for component_dir in md_staging_path.iterdir():
            if not component_dir.is_dir():
                continue
                
            for md_path, json_path, md_metadata, json_metadata in self._scan_component_directory(component_dir):
                yield md_path, json_path, md_metadata, json_metadata
    
    def _scan_component_directory(self, component_dir: Path) -> Generator[Tuple[Path, Path, FileMetadata, Optional[FileMetadata]], None, None]:
        """
        컴포넌트 디렉토리를 스캔합니다.
        
        Args:
            component_dir: 컴포넌트 디렉토리 경로
            
        Yields:
            (md_경로, json_경로, md_메타데이터, json_메타데이터) 튜플
        """
        for file_path in component_dir.glob("page_*.md"):
            if file_path.is_file():
                json_path = file_path.with_suffix('.json')
                json_metadata = None
                
                if json_path.exists():
                    json_metadata = FileMetadata(json_path)
                
                yield file_path, json_path, FileMetadata(file_path), json_metadata
    
    def get_scan_statistics(self) -> Dict[str, Any]:
        """
        스캔 통계 정보를 반환합니다.
        
        Returns:
            스캔 통계 딕셔너리
        """
        stats = {
            "total_md_files": 0,
            "total_json_files": 0,
            "component_files": 0,
            "page_files": 0,
            "directories_scanned": 0,
            "scan_time": datetime.now().isoformat()
        }
        
        # 기본 경로 통계
        for base_path in self.base_paths:
            if base_path.exists():
                stats["directories_scanned"] += 1
                
                if base_path.is_dir():
                    stats["total_md_files"] += len(list(base_path.rglob("*.md")))
                    stats["total_json_files"] += len(list(base_path.rglob("*.json")))
        
        # 컴포넌트 파일 통계
        component_files = list(self.get_component_files())
        stats["component_files"] = len(component_files)
        
        # 페이지 파일 통계
        page_files = list(self.get_page_files())
        stats["page_files"] = len([item for item in page_files if item[0].exists()])
        
        return stats


def create_scanner(base_paths: List[str] = None) -> MDFileScanner:
    """
    MD 파일 스캐너를 생성합니다.
    
    Args:
        base_paths: 스캔할 기본 경로 목록 (기본값: ['./output', './md_staging'])
        
    Returns:
        MDFileScanner 인스턴스
    """
    if base_paths is None:
        base_paths = ['./output', './md_staging']
    
    return MDFileScanner(base_paths)


if __name__ == "__main__":
    # 테스트 코드
    logging.basicConfig(level=logging.INFO)
    
    scanner = create_scanner()
    
    print("=== 스캔 통계 ===")
    stats = scanner.get_scan_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    print("\n=== 컴포넌트 파일 ===")
    for file_path, metadata in scanner.get_component_files():
        print(f"{file_path.name} ({metadata.file_size} bytes)")
    
    print("\n=== 페이지 파일 ===")
    for md_path, json_path, md_metadata, json_metadata in scanner.get_page_files():
        print(f"{md_path.name} -> {json_path.name if json_path.exists() else 'No JSON'}")