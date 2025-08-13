#!/usr/bin/env python3
"""
MD 파일 프로세서 모듈
메인 처리 로직을 담당하며, 스캐너와 파서를 조합하여 문서를 병합하고 처리합니다.
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Generator, Set
from datetime import datetime
import hashlib
from dataclasses import dataclass

from .scanner import MDFileScanner, create_scanner
from .parser import MDParser, create_parser

logger = logging.getLogger(__name__)


@dataclass
class ProcessingConfig:
    """처리 설정 클래스"""
    batch_size: int = 100
    min_quality_score: float = 0.1
    max_content_length: int = 50000
    remove_duplicates: bool = True
    output_format: str = "json"  # json, line_json
    include_metadata: bool = True
    progress_interval: int = 10


@dataclass
class ProcessingStats:
    """처리 통계 클래스"""
    total_files: int = 0
    processed_files: int = 0
    successful_files: int = 0
    failed_files: int = 0
    duplicate_files: int = 0
    total_content_length: int = 0
    start_time: float = 0
    end_time: float = 0
    errors: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []
    
    @property
    def success_rate(self) -> float:
        """성공률 계산"""
        if self.total_files == 0:
            return 0.0
        return (self.successful_files / self.total_files) * 100
    
    @property
    def processing_time(self) -> float:
        """처리 시간 계산"""
        if self.start_time == 0:
            return 0.0
        end_time = self.end_time if self.end_time > 0 else datetime.now().timestamp()
        return end_time - self.start_time


class QualityFilter:
    """품질 필터 클래스"""
    
    def __init__(self, config: ProcessingConfig):
        self.config = config
    
    def filter_document(self, document: Dict[str, Any]) -> bool:
        """
        문서의 품질을 필터링합니다.
        
        Args:
            document: 문서 딕셔너리
            
        Returns:
            필터링 통과 여부
        """
        # 품질 점수 검사
        if document.get('quality_score', 0.0) < self.config.min_quality_score:
            return False
        
        # 콘텐츠 길이 검사
        content = document.get('content', '')
        if len(content) > self.config.max_content_length:
            return False
        
        # 최소 길이 검사
        if len(content.strip()) < 50:
            return False
        
        return True
    
    def get_filter_reason(self, document: Dict[str, Any]) -> Optional[str]:
        """
        필터링 이유를 반환합니다.
        
        Args:
            document: 문서 딕셔너리
            
        Returns:
            필터링 이유 또는 None (통과 시)
        """
        quality_score = document.get('quality_score', 0.0)
        if quality_score < self.config.min_quality_score:
            return f"Quality score too low: {quality_score:.2f} < {self.config.min_quality_score}"
        
        content = document.get('content', '')
        if len(content) > self.config.max_content_length:
            return f"Content too long: {len(content)} > {self.config.max_content_length}"
        
        if len(content.strip()) < 50:
            return f"Content too short: {len(content.strip())} < 50"
        
        return None


class DuplicateRemover:
    """중복 제거기 클래스"""
    
    def __init__(self, config: ProcessingConfig):
        self.config = config
        self.content_hashes: Set[str] = set()
        self.title_hashes: Set[str] = set()
    
    def is_duplicate(self, document: Dict[str, Any]) -> bool:
        """
        문서가 중복인지 확인합니다.
        
        Args:
            document: 문서 딕셔너리
            
        Returns:
            중복 여부
        """
        if not self.config.remove_duplicates:
            return False
        
        # 콘텐츠 해시 계산
        content = document.get('content', '')
        content_hash = hashlib.md5(content.encode()).hexdigest()
        
        # 제목 해시 계산
        title = document.get('title', '')
        title_hash = hashlib.md5(title.encode()).hexdigest()
        
        # 중복 확인
        if content_hash in self.content_hashes:
            return True
        
        if title_hash in self.title_hashes:
            return True
        
        # 해시 저장
        self.content_hashes.add(content_hash)
        self.title_hashes.add(title_hash)
        
        return False
    
    def get_duplicate_reason(self, document: Dict[str, Any]) -> Optional[str]:
        """
        중복 이유를 반환합니다.
        
        Args:
            document: 문서 딕셔너리
            
        Returns:
            중복 이유 또는 None (중복 아닐 시)
        """
        if not self.config.remove_duplicates:
            return None
        
        content = document.get('content', '')
        title = document.get('title', '')
        
        content_hash = hashlib.md5(content.encode()).hexdigest()
        title_hash = hashlib.md5(title.encode()).hexdigest()
        
        if content_hash in self.content_hashes:
            return "Duplicate content"
        
        if title_hash in self.title_hashes:
            return "Duplicate title"
        
        return None


class MDProcessor:
    """MD 파일 프로세서 메인 클래스"""
    
    def __init__(self, config: ProcessingConfig = None):
        """
        초기화
        
        Args:
            config: 처리 설정
        """
        self.config = config or ProcessingConfig()
        self.scanner = create_scanner()
        self.parser = create_parser()
        self.quality_filter = QualityFilter(self.config)
        self.duplicate_remover = DuplicateRemover(self.config)
        self.stats = ProcessingStats()
    
    def process_documents(self, output_path: Path = None) -> List[Dict[str, Any]]:
        """
        모든 문서를 처리합니다.
        
        Args:
            output_path: 출력 파일 경로 (선택적)
            
        Returns:
            처리된 문서 목록
        """
        self.stats.start_time = datetime.now().timestamp()
        self.stats.total_files = sum(1 for _ in self.scanner.scan_files())
        
        logger.info(f"Starting processing of {self.stats.total_files} files")
        
        processed_documents = []
        
        # 컴포넌트 파일 처리
        component_docs = self._process_component_files()
        processed_documents.extend(component_docs)
        
        # 페이지 파일 처리
        page_docs = self._process_page_files()
        processed_documents.extend(page_docs)
        
        # 정렬
        processed_documents.sort(key=lambda x: x.get('title', ''))
        
        self.stats.end_time = datetime.now().timestamp()
        
        # 결과 출력
        logger.info(f"Processing completed!")
        logger.info(f"Total files: {self.stats.total_files}")
        logger.info(f"Processed files: {self.stats.processed_files}")
        logger.info(f"Successful files: {self.stats.successful_files}")
        logger.info(f"Failed files: {self.stats.failed_files}")
        logger.info(f"Duplicate files: {self.stats.duplicate_files}")
        logger.info(f"Success rate: {self.stats.success_rate:.1f}%")
        logger.info(f"Processing time: {self.stats.processing_time:.1f}s")
        
        # 오류 출력
        if self.stats.errors:
            logger.warning(f"Errors encountered ({len(self.stats.errors)}):")
            for error in self.stats.errors[:5]:  # 최대 5개 오류 출력
                logger.warning(f"  - {error}")
        
        # 파일 출력
        if output_path:
            self._save_results(processed_documents, output_path)
        
        return processed_documents
    
    def process_documents_batch(self, output_path: Path = None) -> Generator[List[Dict[str, Any]], None, None]:
        """
        문서를 배치 단위로 처리합니다.
        
        Args:
            output_path: 출력 파일 경로 (선택적)
            
        Yields:
            처리된 문서 배치
        """
        self.stats.start_time = datetime.now().timestamp()
        
        batch = []
        batch_count = 0
        
        # 컴포넌트 파일 처리
        for file_path, metadata in self.scanner.get_component_files():
            document = self._process_single_file(file_path, metadata)
            if document:
                batch.append(document)
                
                if len(batch) >= self.config.batch_size:
                    batch_count += 1
                    yield batch
                    batch = []
        
        # 페이지 파일 처리
        for md_path, json_path, md_metadata, json_metadata in self.scanner.get_page_files():
            document = self._process_single_file(md_path, md_metadata, json_metadata)
            if document:
                batch.append(document)
                
                if len(batch) >= self.config.batch_size:
                    batch_count += 1
                    yield batch
                    batch = []
        
        # 마지막 배치 처리
        if batch:
            batch_count += 1
            yield batch
        
        self.stats.end_time = datetime.now().timestamp()
        
        logger.info(f"Batch processing completed! Total batches: {batch_count}")
        logger.info(f"Total files processed: {self.stats.processed_files}")
        logger.info(f"Success rate: {self.stats.success_rate:.1f}%")
        
        # 전체 결과 저장
        if output_path:
            all_docs = list(self.process_documents())
            self._save_results(all_docs, output_path)
    
    def _process_component_files(self) -> List[Dict[str, Any]]:
        """컴포넌트 파일을 처리합니다."""
        documents = []
        
        for file_path, metadata in self.scanner.get_component_files():
            document = self._process_single_file(file_path, metadata)
            if document:
                documents.append(document)
        
        return documents
    
    def _process_page_files(self) -> List[Dict[str, Any]]:
        """페이지 파일을 처리합니다."""
        documents = []
        
        for md_path, json_path, md_metadata, json_metadata in self.scanner.get_page_files():
            document = self._process_single_file(md_path, md_metadata, json_metadata)
            if document:
                documents.append(document)
        
        return documents
    
    def _process_single_file(self, md_path: Path, md_metadata, json_metadata=None) -> Optional[Dict[str, Any]]:
        """단일 파일을 처리합니다."""
        self.stats.processed_files += 1
        
        try:
            # 파싱
            document = self.parser.parse_file(md_path, json_metadata.file_path if json_metadata else None)
            
            # 품질 필터링
            if not self.quality_filter.filter_document(document):
                reason = self.quality_filter.get_filter_reason(document)
                logger.debug(f"Filtered {md_path.name}: {reason}")
                return None
            
            # 중복 제거
            if self.duplicate_remover.is_duplicate(document):
                reason = self.duplicate_remover.get_duplicate_reason(document)
                logger.debug(f"Duplicate {md_path.name}: {reason}")
                self.stats.duplicate_files += 1
                return None
            
            # 통계 업데이트
            self.stats.successful_files += 1
            content_length = len(document.get('content', ''))
            self.stats.total_content_length += content_length
            
            # 진행률 로깅
            if self.stats.processed_files % self.config.progress_interval == 0:
                progress = (self.stats.processed_files / self.stats.total_files) * 100
                logger.info(f"Progress: {progress:.1f}% ({self.stats.processed_files}/{self.stats.total_files})")
            
            return document
            
        except Exception as e:
            error_msg = f"Error processing {md_path}: {e}"
            logger.error(error_msg)
            self.stats.errors.append(error_msg)
            self.stats.failed_files += 1
            return None
    
    def process_document(self, md_path: Path, md_metadata, json_metadata=None) -> Optional[Dict[str, Any]]:
        """
        단일 문서를 처리합니다.
        
        Args:
            md_path: MD 파일 경로
            md_metadata: MD 파일 메타데이터
            json_metadata: JSON 파일 메타데이터 (선택적)
            
        Returns:
            처리된 문서 또는 None (실패 시)
        """
        return self._process_single_file(md_path, md_metadata, json_metadata)
    
    def _save_results(self, documents: List[Dict[str, Any]], output_path: Path):
        """결과를 파일로 저장합니다."""
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            if self.config.output_format == "json":
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(documents, f, indent=2, ensure_ascii=False)
            elif self.config.output_format == "line_json":
                with open(output_path, 'w', encoding='utf-8') as f:
                    for doc in documents:
                        f.write(json.dumps(doc, ensure_ascii=False) + '\n')
            
            logger.info(f"Results saved to: {output_path}")
            
            # 통계 파일 저장
            stats_path = output_path.with_suffix('.stats.json')
            stats_data = {
                "processing_stats": {
                    "total_files": self.stats.total_files,
                    "processed_files": self.stats.processed_files,
                    "successful_files": self.stats.successful_files,
                    "failed_files": self.stats.failed_files,
                    "duplicate_files": self.stats.duplicate_files,
                    "success_rate": self.stats.success_rate,
                    "processing_time": self.stats.processing_time,
                    "total_content_length": self.stats.total_content_length
                },
                "config": {
                    "batch_size": self.config.batch_size,
                    "min_quality_score": self.config.min_quality_score,
                    "max_content_length": self.config.max_content_length,
                    "remove_duplicates": self.config.remove_duplicates,
                    "output_format": self.config.output_format
                },
                "errors": self.stats.errors[:10]  # 최대 10개 오류 저장
            }
            
            with open(stats_path, 'w', encoding='utf-8') as f:
                json.dump(stats_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Statistics saved to: {stats_path}")
            
        except Exception as e:
            logger.error(f"Failed to save results: {e}")


def create_processor(config: ProcessingConfig = None) -> MDProcessor:
    """
    MD 프로세서를 생성합니다.
    
    Args:
        config: 처리 설정
        
    Returns:
        MDProcessor 인스턴스
    """
    return MDProcessor(config)


if __name__ == "__main__":
    # 테스트 코드
    logging.basicConfig(level=logging.INFO)
    
    # 기본 설정으로 프로세서 생성
    config = ProcessingConfig(
        batch_size=50,
        min_quality_score=0.1,
        max_content_length=20000,
        remove_duplicates=False
        output_format="json"
    )
    
    processor = create_processor(config)
    
    # 처리 실행
    output_path = Path("processed_documents.json")
    documents = processor.process_documents(output_path)
    
    print(f"\n처리 완료! 총 {len(documents)}개 문서를 처리했습니다.")
    print(f"결과 파일: {output_path}")