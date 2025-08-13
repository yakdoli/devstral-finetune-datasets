#!/usr/bin/env python3
"""
품질 검증 및 필터링 모듈
데이터셋의 품질을 보장하기 위한 포괄적인 검증 및 필터링 시스템을 제공합니다.
"""

import logging
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

# 서브 모듈 임포트
from .safety_filter import SafetyFilter, SafetyFilterConfig, SafetyResult
from .duplicate_remover import DuplicateRemover, DuplicateRemoverConfig, DuplicateResult
from .quality_scorer import QualityScorer, QualityScorerConfig, QualityResult
from .compatibility_checker import CompatibilityChecker, CompatibilityCheckerConfig, CompatibilityResult
from .statistics_analyzer import StatisticsAnalyzer, StatisticsAnalyzerConfig, StatisticsResult
from .auto_corrector import AutoCorrector, AutoCorrectorConfig, CorrectionResult
from .utils import (
    UtilsConfig, TextUtils, HashUtils, FileUtils, 
    ValidationUtils, ProgressUtils, LoggingUtils,
    setup_logging, normalize_text, calculate_similarity, 
    calculate_hash, find_duplicates, validate_token_range, 
    validate_text_quality, create_progress_callback, log_progress
)

__version__ = "1.0.0"
__author__ = "Quality Validator Team"
__email__ = "support@example.com"
__description__ = "Comprehensive Dataset Quality Validation and Filtering System"

__all__ = [
    # Main Classes
    'QualityValidator',
    'QualityValidatorConfig',
    'ValidationResult',
    
    # Sub-modules
    'SafetyFilter',
    'SafetyFilterConfig', 
    'SafetyResult',
    'DuplicateRemover',
    'DuplicateRemoverConfig',
    'DuplicateResult',
    'QualityScorer',
    'QualityScorerConfig',
    'QualityResult',
    'CompatibilityChecker',
    'CompatibilityCheckerConfig',
    'CompatibilityResult',
    'StatisticsAnalyzer',
    'StatisticsAnalyzerConfig',
    'StatisticsResult',
    'AutoCorrector',
    'AutoCorrectorConfig',
    'CorrectionResult',
    
    # Utils
    'UtilsConfig',
    'TextUtils',
    'HashUtils',
    'FileUtils',
    'ValidationUtils',
    'ProgressUtils',
    'LoggingUtils',
    'setup_logging',
    'normalize_text',
    'calculate_similarity',
    'calculate_hash',
    'find_duplicates',
    'validate_token_range',
    'validate_text_quality',
    'create_progress_callback',
    'log_progress',
    
    # Version info
    '__version__',
    '__author__',
    '__email__',
    '__description__'
]


@dataclass
class QualityValidatorConfig:
    """품질 검증기 설정"""
    # 안전성 필터 설정
    safety_filter_config: SafetyFilterConfig = field(default_factory=SafetyFilterConfig)
    
    # 중복 제거기 설정
    duplicate_remover_config: DuplicateRemoverConfig = field(default_factory=DuplicateRemoverConfig)
    
    # 품질 점수 계산기 설정
    quality_scorer_config: QualityScorerConfig = field(default_factory=QualityScorerConfig)
    
    # 호환성 검증기 설정
    compatibility_checker_config: CompatibilityCheckerConfig = field(default_factory=CompatibilityCheckerConfig)
    
    # 통계 분석기 설정
    statistics_analyzer_config: StatisticsAnalyzerConfig = field(default_factory=StatisticsAnalyzerConfig)
    
    # 자동 수정기 설정
    auto_corrector_config: AutoCorrectorConfig = field(default_factory=AutoCorrectorConfig)
    
    # 유틸리티 설정
    utils_config: UtilsConfig = field(default_factory=UtilsConfig)
    
    # 전체 설정
    min_quality_score: float = 0.7
    max_similarity_threshold: float = 0.9
    safety_threshold: float = 0.8
    enable_auto_correction: bool = True
    enable_statistics_analysis: bool = True
    
    # 성능 설정
    batch_size: int = 100
    max_workers: int = 8
    use_multiprocessing: bool = True
    progress_callback: Optional[callable] = None
    
    # 출력 설정
    output_format: str = "enhanced"  # enhanced, basic, detailed
    include_metadata: bool = True
    generate_report: bool = True


@dataclass
class ValidationResult:
    """검증 결과"""
    id: str
    conversations: List[Dict[str, Any]]
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    # 품질 검증 메타데이터
    quality_validation: Dict[str, Any] = field(default_factory=dict)
    
    # 검증 상태
    is_valid: bool = True
    validation_passed: bool = True
    
    # 통계 정보
    statistics: Dict[str, Any] = field(default_factory=dict)
    
    # 생성 시간
    validation_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class QualityValidator:
    """품질 검증기 메인 클래스"""
    
    def __init__(self, config: Optional[QualityValidatorConfig] = None):
        """
        품질 검증기를 초기화합니다.
        
        Args:
            config: 품질 검증기 설정
        """
        self.config = config or QualityValidatorConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 로깅 설정
        self._setup_logging()
        
        # 서브 모듈 초기화
        self._initialize_modules()
        
        # 통계 정보
        self.validation_stats = {
            'total_processed': 0,
            'total_passed': 0,
            'total_failed': 0,
            'start_time': None,
            'end_time': None
        }
        
        self.logger.info("QualityValidator initialized successfully")
    
    def _setup_logging(self):
        """로깅을 설정합니다."""
        # 로거 설정
        logger = logging.getLogger('quality_validator')
        logger.setLevel(logging.INFO)
        
        # 핸들러 생성
        if not logger.handlers:
            # 콘솔 핸들러
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            
            # 포맷터
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            console_handler.setFormatter(formatter)
            
            # 핸들러 추가
            logger.addHandler(console_handler)
    
    def _initialize_modules(self):
        """서브 모듈을 초기화합니다."""
        try:
            # 안전성 필터
            self.safety_filter = SafetyFilter(self.config.safety_filter_config)
            
            # 중복 제거기
            self.duplicate_remover = DuplicateRemover(self.config.duplicate_remover_config)
            
            # 품질 점수 계산기
            self.quality_scorer = QualityScorer(self.config.quality_scorer_config)
            
            # 호환성 검증기
            self.compatibility_checker = CompatibilityChecker(self.config.compatibility_checker_config)
            
            # 통계 분석기
            self.statistics_analyzer = StatisticsAnalyzer(self.config.statistics_analyzer_config)
            
            # 자동 수정기
            self.auto_corrector = AutoCorrector(self.config.auto_corrector_config)
            
            # 유틸리티
            self.text_utils = TextUtils(self.config.utils_config)
            self.hash_utils = HashUtils(self.config.utils_config)
            self.file_utils = FileUtils(self.config.utils_config)
            self.validation_utils = ValidationUtils(self.config.utils_config)
            self.progress_utils = ProgressUtils(self.config.utils_config)
            
            self.logger.info("All sub-modules initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Error initializing modules: {e}")
            raise
    
    def validate_and_filter(self, datasets: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[ValidationResult]]:
        """
        데이터셋을 검증하고 필터링합니다.
        
        Args:
            datasets: 포맷별 데이터셋
            
        Returns:
            검증된 데이터셋
        """
        self.validation_stats['start_time'] = datetime.now().isoformat()
        
        self.logger.info(f"Starting validation and filtering for {len(datasets)} formats")
        
        validated_datasets = {}
        
        for format_type, items in datasets.items():
            self.logger.info(f"Processing {format_type} format with {len(items)} items")
            
            try:
                # 형식별 검증
                validated_items = self._validate_format_items(items, format_type)
                
                # 결과 저장
                validated_datasets[format_type] = validated_items
                
                self.logger.info(f"Validation completed for {format_type}: {len(validated_items)}/{len(items)} items passed")
                
            except Exception as e:
                self.logger.error(f"Error validating {format_type} format: {e}")
                # 오류 발생 시 원본 데이터 반환
                validated_datasets[format_type] = self._create_validation_results(items, format_type)
        
        self.validation_stats['end_time'] = datetime.now().isoformat()
        self.validation_stats['total_processed'] = sum(len(items) for items in datasets.values())
        self.validation_stats['total_passed'] = sum(len(items) for items in validated_datasets.values())
        self.validation_stats['total_failed'] = self.validation_stats['total_processed'] - self.validation_stats['total_passed']
        
        self.logger.info(f"Validation completed: {self.validation_stats['total_passed']}/{self.validation_stats['total_processed']} items passed")
        
        return validated_datasets
    
    def _validate_format_items(self, items: List[Dict[str, Any]], format_type: str) -> List[ValidationResult]:
        """형식별 아이템을 검증합니다."""
        validated_results = []
        
        for i, item in enumerate(items):
            try:
                # 고유 ID 생성
                item_id = f"{format_type}_{i}"
                
                # 데이터 구조 변환 (UnslothDatasetGenerator 출력 형식으로 변환)
                converted_item = self._convert_item_format(item, format_type)
                
                # 기본 검증 결과 생성
                validation_result = ValidationResult(
                    id=item_id,
                    conversations=self._extract_conversations(converted_item, format_type),
                    metadata={
                        'original_metadata': converted_item.get('metadata', {}),
                        'format_type': format_type,
                        'item_index': i
                    }
                )
                
                # 안전성 검증
                safety_result = self.safety_filter.check_safety(item, format_type)
                validation_result.quality_validation['safety_score'] = safety_result.safety_score
                validation_result.quality_validation['safety_issues'] = safety_result.issues
                
                if safety_result.safety_score < self.config.safety_threshold:
                    validation_result.is_valid = False
                    validation_result.validation_passed = False
                    continue
                
                # 중복 검증
                duplicate_result = self.duplicate_remover.check_duplicates(item, format_type)
                validation_result.quality_validation['duplicate_status'] = duplicate_result.status
                validation_result.quality_validation['similarity_score'] = duplicate_result.similarity_score
                
                if duplicate_result.is_duplicate:
                    validation_result.is_valid = False
                    validation_result.validation_passed = False
                    continue
                
                # 품질 점수 계산
                quality_result = self.quality_scorer.calculate_quality_score(item, format_type)
                validation_result.quality_validation['quality_score'] = quality_result.quality_score
                validation_result.quality_validation['quality_details'] = quality_result.details
                
                if quality_result.quality_score < self.config.min_quality_score:
                    validation_result.is_valid = False
                    validation_result.validation_passed = False
                    continue
                
                # 호환성 검증
                compatibility_result = self.compatibility_checker.check_compatibility(item, format_type)
                validation_result.quality_validation['unsloth_compatible'] = compatibility_result.is_compatible
                validation_result.quality_validation['compatibility_score'] = compatibility_result.compatibility_score
                validation_result.quality_validation['compatibility_issues'] = compatibility_result.issues
                
                if not compatibility_result.is_compatible:
                    validation_result.is_valid = False
                    validation_result.validation_passed = False
                    continue
                
                # 자동 수정 (활성화된 경우)
                if self.config.enable_auto_correction:
                    correction_result = self.auto_corrector.correct_item(item, format_type)
                    
                    if correction_result.changes_made:
                        # 수정된 아이템으로 업데이트
                        validation_result.conversations = self._extract_conversations(
                            correction_result.corrected_item, format_type
                        )
                        validation_result.quality_validation['auto_corrections'] = correction_result.corrections_applied
                        validation_result.quality_validation['correction_confidence'] = correction_result.confidence_score
                
                # 최종 검증 상태
                validation_result.validation_passed = validation_result.is_valid
                
                # 통계 분석 (활성화된 경우)
                if self.config.enable_statistics_analysis:
                    stats_result = self.statistics_analyzer.analyze_dataset({format_type: [item]})
                    validation_result.statistics = self._extract_statistics(stats_result)
                
                # 타임스탬프 업데이트
                validation_result.quality_validation['validation_timestamp'] = datetime.now().isoformat()
                
                validated_results.append(validation_result)
                
                # 진행률 콜백
                if self.config.progress_callback:
                    self.config.progress_callback(i + 1, len(items))
                
            except Exception as e:
                self.logger.error(f"Error validating item {i}: {e}")
                # 오류 발생 시 기본 결과 반환
                validation_result = ValidationResult(
                    id=f"{format_type}_{i}",
                    conversations=self._extract_conversations(item, format_type),
                    metadata={
                        'original_metadata': item.get('metadata', {}),
                        'format_type': format_type,
                        'item_index': i
                    },
                    is_valid=False,
                    validation_passed=False,
                    quality_validation={
                        'validation_timestamp': datetime.now().isoformat(),
                        'issues': [f"Validation error: {str(e)}"]
                    }
                )
                validated_results.append(validation_result)
        
        return validated_results
    
    def _extract_conversations(self, item: Dict[str, Any], format_type: str) -> List[Dict[str, Any]]:
        """아이템에서 대화를 추출합니다."""
        if format_type == "sharegpt":
            return item.get("conversations", [])
        elif format_type == "alpaca":
            return [
                {"from": "human", "value": item.get("instruction", "") + " " + item.get("input", "")},
                {"from": "gpt", "value": item.get("output", "")}
            ]
        elif format_type == "openai":
            return item.get("messages", [])
        else:
            return []
    
    def _create_validation_results(self, items: List[Dict[str, Any]], format_type: str) -> List[ValidationResult]:
        """검증 결과를 생성합니다."""
        results = []
        
        for i, item in enumerate(items):
            item_id = f"{format_type}_{i}"
            
            result = ValidationResult(
                id=item_id,
                conversations=self._extract_conversations(item, format_type),
                metadata={
                    'original_metadata': item.get('metadata', {}),
                    'format_type': format_type,
                    'item_index': i
                },
                is_valid=False,
                validation_passed=False,
                quality_validation={
                    'validation_timestamp': datetime.now().isoformat(),
                    'issues': ['Validation skipped due to error']
                }
            )
            
            results.append(result)
        
        return results
    
    def _extract_statistics(self, stats_result: StatisticsResult) -> Dict[str, Any]:
        """통계 정보를 추출합니다."""
        return {
            'total_samples': stats_result.total_samples,
            'vocabulary_diversity': stats_result.vocabulary_diversity,
            'topic_diversity': stats_result.topic_diversity,
            'length_diversity': stats_result.length_diversity,
            'component_balance': stats_result.component_balance,
            'topic_balance': stats_result.topic_balance,
            'format_balance': stats_result.format_balance,
            'validation_passed': stats_result.validation_passed,
            'validation_issues': stats_result.validation_issues,
            'validation_warnings': stats_result.validation_warnings
        }
    
    def generate_report(self, validated_datasets: Dict[str, List[ValidationResult]] = None) -> Dict[str, Any]:
        """
        검증 리포트를 생성합니다.
        
        Args:
            validated_datasets: 검증된 데이터셋
            
        Returns:
            검증 리포트
        """
        if validated_datasets is None:
            validated_datasets = {}
        
        # 기본 통계
        total_items = sum(len(items) for items in validated_datasets.values())
        passed_items = sum(len(items) for items in validated_datasets.values())
        
        # 포맷별 통계
        format_stats = {}
        for format_type, items in validated_datasets.items():
            valid_items = sum(1 for item in items if item.is_valid)
            format_stats[format_type] = {
                'total': len(items),
                'valid': valid_items,
                'invalid': len(items) - valid_items,
                'validity_rate': valid_items / len(items) if len(items) > 0 else 0.0
            }
        
        # 품질 통계
        quality_stats = {}
        for format_type, items in validated_datasets.items():
            if items:
                safety_scores = [item.quality_validation.get('safety_score', 0.0) for item in items]
                quality_scores = [item.quality_validation.get('quality_score', 0.0) for item in items]
                compatibility_scores = [item.quality_validation.get('compatibility_score', 0.0) for item in items]
                
                quality_stats[format_type] = {
                    'avg_safety_score': sum(safety_scores) / len(safety_scores),
                    'avg_quality_score': sum(quality_scores) / len(quality_scores),
                    'avg_compatibility_score': sum(compatibility_scores) / len(compatibility_scores),
                    'min_safety_score': min(safety_scores),
                    'max_safety_score': max(safety_scores),
                    'min_quality_score': min(quality_scores),
                    'max_quality_score': max(quality_scores),
                    'min_compatibility_score': min(compatibility_scores),
                    'max_compatibility_score': max(compatibility_scores)
                }
        
        # 이슈 통계
        issue_stats = {}
        for format_type, items in validated_datasets.items():
            issues = []
            for item in items:
                if 'safety_issues' in item.quality_validation:
                    issues.extend(item.quality_validation['safety_issues'])
                if 'compatibility_issues' in item.quality_validation:
                    issues.extend(item.quality_validation['compatibility_issues'])
            
            issue_counts = {}
            for issue in issues:
                issue_counts[issue] = issue_counts.get(issue, 0) + 1
            
            issue_stats[format_type] = issue_counts
        
        # 리포트 생성
        report = {
            'report_version': '1.0.0',
            'generated_at': datetime.now().isoformat(),
            'validation_stats': self.validation_stats,
            'summary': {
                'total_items': total_items,
                'passed_items': passed_items,
                'failed_items': total_items - passed_items,
                'overall_validity_rate': passed_items / total_items if total_items > 0 else 0.0
            },
            'format_statistics': format_stats,
            'quality_statistics': quality_stats,
            'issue_statistics': issue_stats,
            'configuration': {
                'min_quality_score': self.config.min_quality_score,
                'max_similarity_threshold': self.config.max_similarity_threshold,
                'safety_threshold': self.config.safety_threshold,
                'enable_auto_correction': self.config.enable_auto_correction,
                'enable_statistics_analysis': self.config.enable_statistics_analysis
            }
        }
        
        self.logger.info(f"Validation report generated: {passed_items}/{total_items} items passed")
        
        return report
    
    def save_validated_datasets(self, validated_datasets: Dict[str, List[ValidationResult]], output_path: str) -> Dict[str, str]:
        """
        검증된 데이터셋을 저장합니다.
        
        Args:
            validated_datasets: 검증된 데이터셋
            output_path: 출력 경로
            
        Returns:
            저장된 파일 경로 목록
        """
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        saved_files = {}
        
        for format_type, items in validated_datasets.items():
            # 파일 경로 생성
            file_path = output_dir / f"{format_type}_validated.jsonl"
            
            # 데이터 변환
            validated_items = []
            for item in items:
                validated_item = {
                    'id': item.id,
                    'conversations': item.conversations,
                    'metadata': item.metadata,
                    'quality_validation': item.quality_validation,
                    'statistics': item.statistics
                }
                validated_items.append(validated_item)
            
            # 파일 저장
            if self.file_utils.write_jsonl_file(str(file_path), validated_items):
                saved_files[format_type] = str(file_path)
                self.logger.info(f"Saved validated {format_type} dataset to {file_path}")
            else:
                self.logger.error(f"Failed to save validated {format_type} dataset")
        
        return saved_files
    
    def get_validation_summary(self, validated_datasets: Dict[str, List[ValidationResult]]) -> Dict[str, Any]:
        """검증 요약 정보를 생성합니다."""
        summary = {
            'total_formats': len(validated_datasets),
            'total_items': sum(len(items) for items in validated_datasets.values()),
            'valid_items': sum(len([item for item in items if item.is_valid]) for items in validated_datasets.values()),
            'invalid_items': sum(len([item for item in items if not item.is_valid]) for items in validated_datasets.values()),
            'formats': {}
        }
        
        for format_type, items in validated_datasets.items():
            valid_items = [item for item in items if item.is_valid]
            invalid_items = [item for item in items if not item.is_valid]
            
            format_summary = {
                'total_items': len(items),
                'valid_items': len(valid_items),
                'invalid_items': len(invalid_items),
                'validity_rate': len(valid_items) / len(items) if len(items) > 0 else 0.0,
                'avg_safety_score': sum(item.quality_validation.get('safety_score', 0.0) for item in valid_items) / len(valid_items) if valid_items else 0.0,
                'avg_quality_score': sum(item.quality_validation.get('quality_score', 0.0) for item in valid_items) / len(valid_items) if valid_items else 0.0,
                'avg_compatibility_score': sum(item.quality_validation.get('compatibility_score', 0.0) for item in valid_items) / len(valid_items) if valid_items else 0.0
            }
            
            summary['formats'][format_type] = format_summary
        
        return summary
    
    def _convert_item_format(self, item: Dict[str, Any], format_type: str) -> Dict[str, Any]:
        """UnslothDatasetGenerator 출력 형식을 QualityValidator 입력 형식으로 변환합니다."""
        converted_item = item.copy()
        
        # 기본 메타데이터 추가
        if 'metadata' not in converted_item:
            converted_item['metadata'] = {}
        
        # 포맷별 데이터 구조 변환
        if format_type == 'sharegpt':
            # ShareGPT 형식: 이미 올바른 구조
            pass
        elif format_type == 'alpaca':
            # Alpaca 형식을 ShareGPT 형식으로 변환
            if 'instruction' in item and 'output' in item:
                converted_item['conversations'] = [
                    {"from": "system", "value": "Syncfusion WinForms 전문가"},
                    {"from": "human", "value": item.get('instruction', '') + (' ' + item.get('input', '') if item.get('input') else '')},
                    {"from": "gpt", "value": item.get('output', '')}
                ]
                # 원본 필드 제거
                for key in ['instruction', 'input', 'output']:
                    if key in converted_item:
                        del converted_item[key]
        elif format_type == 'openai':
            # OpenAI 형식을 ShareGPT 형식으로 변환
            if 'messages' in item:
                messages = item['messages']
                converted_item['conversations'] = []
                
                # 메시지를 conversations로 변환
                for msg in messages:
                    if msg['role'] == 'system':
                        converted_item['conversations'].append({"from": "system", "value": msg['content']})
                    elif msg['role'] == 'user':
                        converted_item['conversations'].append({"from": "human", "value": msg['content']})
                    elif msg['role'] == 'assistant':
                        converted_item['conversations'].append({"from": "gpt", "value": msg['content']})
                
                # 원본 필드 제거
                if 'messages' in converted_item:
                    del converted_item['messages']
        
        # 메타데이터에 변환 정보 추가
        converted_item['metadata']['format_conversion'] = {
            'original_format': format_type,
            'converted_to': 'sharegpt',  # 모든 포맷을 sharegpt 형식으로 통일
            'conversion_timestamp': datetime.now().isoformat()
        }
        
        return converted_item


def create_default_validator() -> QualityValidator:
    """
    기본 설정으로 품질 검증기를 생성합니다.
    
    Returns:
        기본 설정으로 생성된 QualityValidator 인스턴스
    """
    config = QualityValidatorConfig(
        min_quality_score=0.7,
        max_similarity_threshold=0.9,
        safety_threshold=0.8,
        enable_auto_correction=True,
        enable_statistics_analysis=True,
        batch_size=100,
        max_workers=4,
        use_multiprocessing=True,
        output_format="enhanced",
        include_metadata=True,
        generate_report=True
    )
    
    return QualityValidator(config)


# 모듈 로드 시 기본 로깅 설정
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())


if __name__ == "__main__":
    # 모듈 정보 출력
    print(f"Quality Validator Module v{__version__}")
    print(f"Author: {__author__}")
    print(f"Description: {__description__}")
    print(f"Available components:")
    print(f"  - Safety Filter: Content safety validation")
    print(f"  - Duplicate Remover: Duplicate detection and removal")
    print(f"  - Quality Scorer: Quality score calculation")
    print(f"  - Compatibility Checker: Unsloth compatibility validation")
    print(f"  - Statistics Analyzer: Dataset statistics analysis")
    print(f"  - Auto Corrector: Automatic issue correction")
    print(f"  - Utils: Common utility functions")
    
    # 샘플 생성 테스트
    print("\n=== Sample Validation Test ===")
    
    try:
        # 기본 검증기 생성
        validator = create_default_validator()
        
        # 샘플 데이터 생성
        sample_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "system", "value": "Syncfusion WinForms 전문가"},
                        {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "system", "value": "Syncfusion WinForms 전문가"},
                        {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                        {"from": "gpt", "value": "Chart 컴포넌트 사용법은 다음과 같습니다..."}
                    ]
                }
            ],
            "alpaca": [
                {
                    "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
                    "input": "초보자도 이해할 수 있도록 설명해주세요.",
                    "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용"
                },
                {
                    "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
                    "input": "데이터 바인딩 포함해서 설명해주세요.",
                    "output": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가"
                }
            ],
            "openai": [
                {
                    "messages": [
                        {"role": "system", "content": "Syncfusion WinForms 전문가"},
                        {"role": "user", "content": "DataGrid 사용법을 알려주세요."},
                        {"role": "assistant", "content": "DataGrid 사용법은 다음과 같습니다..."}
                    ]
                },
                {
                    "messages": [
                        {"role": "system", "content": "Syncfusion WinForms 전문가"},
                        {"role": "user", "content": "Chart 컴포넌트 사용법을 알려주세요."},
                        {"role": "assistant", "content": "Chart 컴포넌트 사용법은 다음과 같습니다..."}
                    ]
                }
            ]
        }
        
        # 검증 수행
        print("Starting validation...")
        validated_datasets = validator.validate_and_filter(sample_datasets)
        
        # 결과 요약
        summary = validator.get_validation_summary(validated_datasets)
        print(f"\nValidation Summary:")
        print(f"Total Formats: {summary['total_formats']}")
        print(f"Total Items: {summary['total_items']}")
        print(f"Valid Items: {summary['valid_items']}")
        print(f"Invalid Items: {summary['invalid_items']}")
        
        # 포맷별 요약
        for format_type, format_summary in summary['formats'].items():
            print(f"\n{format_type.upper()} Format:")
            print(f"  Total Items: {format_summary['total_items']}")
            print(f"  Valid Items: {format_summary['valid_items']}")
            print(f"  Invalid Items: {format_summary['invalid_items']}")
            print(f"  Validity Rate: {format_summary['validity_rate']:.2%}")
            print(f"  Avg Safety Score: {format_summary['avg_safety_score']:.3f}")
            print(f"  Avg Quality Score: {format_summary['avg_quality_score']:.3f}")
            print(f"  Avg Compatibility Score: {format_summary['avg_compatibility_score']:.3f}")
        
        # 리포트 생성
        print(f"\nGenerating validation report...")
        report = validator.generate_report(validated_datasets)
        print(f"Report generated successfully")
        print(f"Overall validity rate: {report['summary']['overall_validity_rate']:.2%}")
        
        print("\n=== Validation Test Completed Successfully ===")
        
    except Exception as e:
        print(f"Validation test failed: {e}")
        import traceback
        traceback.print_exc()