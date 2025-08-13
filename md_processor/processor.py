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
            # 파일 존재 확인
            if not md_path.exists():
                raise FileNotFoundError(f"MD file not found: {md_path}")
            
            # 파일 크기 확인
            file_size = md_path.stat().st_size
            if file_size == 0:
                logger.warning(f"Empty file skipped: {md_path}")
                return None
            
            if file_size > self.config.max_content_length * 10:  # 대략적인 크기 제한
                logger.warning(f"File too large, skipped: {md_path} ({file_size} bytes)")
                return None
            
            # 파싱
            logger.debug(f"Parsing file: {md_path}")
            document = self.parser.parse_file(md_path, json_metadata.file_path if json_metadata else None)
            
            # 파싱 결과 검증
            if not document or not document.get('content'):
                logger.warning(f"No content extracted from: {md_path}")
                return None
            
            # 품질 필터링
            if not self.quality_filter.filter_document(document):
                reason = self.quality_filter.get_filter_reason(document)
                logger.debug(f"Quality filter failed for {md_path.name}: {reason}")
                return None
            
            # 중복 제거
            if self.duplicate_remover.is_duplicate(document):
                reason = self.duplicate_remover.get_duplicate_reason(document)
                logger.debug(f"Duplicate detected for {md_path.name}: {reason}")
                self.stats.duplicate_files += 1
                return None
            
            # 메타데이터 보강
            document = self._enrich_document_metadata(document, md_path, json_metadata)
            
            # 통계 업데이트
            self.stats.successful_files += 1
            content_length = len(document.get('content', ''))
            self.stats.total_content_length += content_length
            
            # 진행률 로깅
            if self.stats.processed_files % self.config.progress_interval == 0 and self.stats.total_files > 0:
                progress = (self.stats.processed_files / self.stats.total_files) * 100
                logger.info(f"Progress: {progress:.1f}% ({self.stats.processed_files}/{self.stats.total_files})")
            
            logger.debug(f"Successfully processed: {md_path.name}")
            return document
            
        except FileNotFoundError as e:
            error_msg = f"File not found: {md_path} - {e}"
            logger.error(error_msg)
            self.stats.errors.append(error_msg)
            self.stats.failed_files += 1
            return None
            
        except PermissionError as e:
            error_msg = f"Permission denied: {md_path} - {e}"
            logger.error(error_msg)
            self.stats.errors.append(error_msg)
            self.stats.failed_files += 1
            return None
            
        except UnicodeDecodeError as e:
            error_msg = f"Encoding error: {md_path} - {e}"
            logger.error(error_msg)
            self.stats.errors.append(error_msg)
            self.stats.failed_files += 1
            return None
            
        except Exception as e:
            error_msg = f"Unexpected error processing {md_path}: {type(e).__name__}: {e}"
            logger.error(error_msg, exc_info=True)
            self.stats.errors.append(error_msg)
            self.stats.failed_files += 1
            return None
    
    def _enrich_document_metadata(self, document: Dict[str, Any], md_path: Path, json_metadata=None) -> Dict[str, Any]:
        """문서 메타데이터 보강"""
        try:
            # 처리 시간 추가
            document['processing_timestamp'] = datetime.now().isoformat()
            
            # 파일 경로 정보 추가
            document['source_file'] = str(md_path)
            document['file_size'] = md_path.stat().st_size
            
            # JSON 메타데이터 정보 추가
            if json_metadata:
                document['has_json_metadata'] = True
                document['json_file'] = str(json_metadata.file_path)
            else:
                document['has_json_metadata'] = False
            
            # 처리 설정 정보 추가
            document['processing_config'] = {
                'min_quality_score': self.config.min_quality_score,
                'max_content_length': self.config.max_content_length,
                'remove_duplicates': self.config.remove_duplicates
            }
            
            return document
            
        except Exception as e:
            logger.warning(f"Failed to enrich metadata for {md_path}: {e}")
            return document
    
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
            
            # 메인 결과 파일 저장
            if self.config.output_format == "json":
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(documents, f, indent=2, ensure_ascii=False)
            elif self.config.output_format == "line_json":
                with open(output_path, 'w', encoding='utf-8') as f:
                    for doc in documents:
                        f.write(json.dumps(doc, ensure_ascii=False) + '\n')
            
            logger.info(f"Results saved to: {output_path} ({len(documents)} documents)")
            
            # 구조화된 메타데이터 파일 저장
            metadata_path = output_path.with_suffix('.metadata.json')
            self._save_structured_metadata(documents, metadata_path)
            
            # 통계 파일 저장
            stats_path = output_path.with_suffix('.stats.json')
            self._save_processing_statistics(stats_path)
            
            # 요약 리포트 저장
            summary_path = output_path.with_suffix('.summary.json')
            self._save_processing_summary(documents, summary_path)
            
        except Exception as e:
            logger.error(f"Failed to save results: {e}", exc_info=True)
    
    def _save_structured_metadata(self, documents: List[Dict[str, Any]], metadata_path: Path):
        """구조화된 메타데이터 저장"""
        try:
            metadata_summary = {
                "document_count": len(documents),
                "components": {},
                "api_signatures": {},
                "content_statistics": {
                    "total_words": 0,
                    "total_characters": 0,
                    "total_code_blocks": 0,
                    "total_api_signatures": 0
                },
                "quality_distribution": {
                    "high_quality": 0,  # > 0.8
                    "medium_quality": 0,  # 0.5 - 0.8
                    "low_quality": 0  # < 0.5
                },
                "generation_timestamp": datetime.now().isoformat()
            }
            
            # 문서별 메타데이터 분석
            for doc in documents:
                component = doc.get('component')
                if component:
                    if component not in metadata_summary["components"]:
                        metadata_summary["components"][component] = {
                            "document_count": 0,
                            "pages": [],
                            "total_api_signatures": 0,
                            "avg_quality_score": 0.0
                        }
                    
                    comp_info = metadata_summary["components"][component]
                    comp_info["document_count"] += 1
                    
                    if doc.get('page'):
                        comp_info["pages"].append(doc['page'])
                    
                    # API 시그니처 통계
                    api_sigs = doc.get('api_signatures', [])
                    comp_info["total_api_signatures"] += len(api_sigs)
                    
                    # 컴포넌트별 API 시그니처 수집
                    for sig in api_sigs:
                        sig_name = sig.get('name', 'unknown')
                        if sig_name not in metadata_summary["api_signatures"]:
                            metadata_summary["api_signatures"][sig_name] = {
                                "components": [],
                                "signature": sig.get('signature', ''),
                                "type": sig.get('type', 'unknown'),
                                "language": sig.get('language', 'unknown')
                            }
                        
                        if component not in metadata_summary["api_signatures"][sig_name]["components"]:
                            metadata_summary["api_signatures"][sig_name]["components"].append(component)
                
                # 콘텐츠 통계
                content_structure = doc.get('content_structure', {})
                metadata_summary["content_statistics"]["total_words"] += content_structure.get('word_count', 0)
                metadata_summary["content_statistics"]["total_characters"] += content_structure.get('character_count', 0)
                metadata_summary["content_statistics"]["total_code_blocks"] += content_structure.get('code_block_count', 0)
                metadata_summary["content_statistics"]["total_api_signatures"] += len(doc.get('api_signatures', []))
                
                # 품질 분포
                quality_score = doc.get('quality_score', 0.0)
                if quality_score > 0.8:
                    metadata_summary["quality_distribution"]["high_quality"] += 1
                elif quality_score > 0.5:
                    metadata_summary["quality_distribution"]["medium_quality"] += 1
                else:
                    metadata_summary["quality_distribution"]["low_quality"] += 1
            
            # 컴포넌트별 평균 품질 점수 계산
            for component, comp_info in metadata_summary["components"].items():
                component_docs = [doc for doc in documents if doc.get('component') == component]
                if component_docs:
                    avg_quality = sum(doc.get('quality_score', 0.0) for doc in component_docs) / len(component_docs)
                    comp_info["avg_quality_score"] = round(avg_quality, 3)
                    comp_info["pages"] = sorted(list(set(comp_info["pages"])))
            
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata_summary, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Structured metadata saved to: {metadata_path}")
            
        except Exception as e:
            logger.error(f"Failed to save structured metadata: {e}", exc_info=True)
    
    def _save_processing_statistics(self, stats_path: Path):
        """처리 통계 저장"""
        try:
            stats_data = {
                "processing_stats": {
                    "total_files": self.stats.total_files,
                    "processed_files": self.stats.processed_files,
                    "successful_files": self.stats.successful_files,
                    "failed_files": self.stats.failed_files,
                    "duplicate_files": self.stats.duplicate_files,
                    "success_rate": round(self.stats.success_rate, 2),
                    "processing_time": round(self.stats.processing_time, 2),
                    "total_content_length": self.stats.total_content_length,
                    "avg_content_length": round(self.stats.total_content_length / max(self.stats.successful_files, 1), 2)
                },
                "config": {
                    "batch_size": self.config.batch_size,
                    "min_quality_score": self.config.min_quality_score,
                    "max_content_length": self.config.max_content_length,
                    "remove_duplicates": self.config.remove_duplicates,
                    "output_format": self.config.output_format,
                    "include_metadata": self.config.include_metadata,
                    "progress_interval": self.config.progress_interval
                },
                "errors": self.stats.errors[:20],  # 최대 20개 오류 저장
                "timestamp": datetime.now().isoformat()
            }
            
            with open(stats_path, 'w', encoding='utf-8') as f:
                json.dump(stats_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Processing statistics saved to: {stats_path}")
            
        except Exception as e:
            logger.error(f"Failed to save processing statistics: {e}", exc_info=True)
    
    def _save_processing_summary(self, documents: List[Dict[str, Any]], summary_path: Path):
        """처리 요약 저장"""
        try:
            # 품질 점수 분석
            quality_scores = [doc.get('quality_score', 0.0) for doc in documents]
            avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0.0
            
            # 컴포넌트 분석
            components = {}
            for doc in documents:
                component = doc.get('component')
                if component:
                    if component not in components:
                        components[component] = 0
                    components[component] += 1
            
            # API 시그니처 분석
            total_api_signatures = sum(len(doc.get('api_signatures', [])) for doc in documents)
            
            summary = {
                "processing_summary": {
                    "total_documents": len(documents),
                    "success_rate": round(self.stats.success_rate, 2),
                    "processing_time": round(self.stats.processing_time, 2),
                    "avg_quality_score": round(avg_quality, 3),
                    "total_api_signatures": total_api_signatures,
                    "components_found": len(components),
                    "component_distribution": dict(sorted(components.items(), key=lambda x: x[1], reverse=True))
                },
                "quality_analysis": {
                    "min_quality": round(min(quality_scores) if quality_scores else 0.0, 3),
                    "max_quality": round(max(quality_scores) if quality_scores else 0.0, 3),
                    "avg_quality": round(avg_quality, 3),
                    "high_quality_docs": len([q for q in quality_scores if q > 0.8]),
                    "medium_quality_docs": len([q for q in quality_scores if 0.5 <= q <= 0.8]),
                    "low_quality_docs": len([q for q in quality_scores if q < 0.5])
                },
                "content_analysis": {
                    "total_content_length": self.stats.total_content_length,
                    "avg_content_length": round(self.stats.total_content_length / max(len(documents), 1), 2),
                    "documents_with_code": len([doc for doc in documents if doc.get('content_structure', {}).get('code_block_count', 0) > 0]),
                    "documents_with_tables": len([doc for doc in documents if doc.get('content_structure', {}).get('table_count', 0) > 0]),
                    "documents_with_images": len([doc for doc in documents if doc.get('content_structure', {}).get('image_count', 0) > 0])
                },
                "timestamp": datetime.now().isoformat()
            }
            
            with open(summary_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Processing summary saved to: {summary_path}")
            
        except Exception as e:
            logger.error(f"Failed to save processing summary: {e}", exc_info=True)


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
        remove_duplicates=False,
        output_format="json"
    )
    
    processor = create_processor(config)
    
    # 처리 실행
    output_path = Path("processed_documents.json")
    documents = processor.process_documents(output_path)
    
    print(f"\n처리 완료! 총 {len(documents)}개 문서를 처리했습니다.")
    print(f"결과 파일: {output_path}")