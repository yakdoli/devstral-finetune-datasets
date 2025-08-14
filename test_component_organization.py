#!/usr/bin/env python3
"""
컴포넌트별 데이터셋 조직화 기능 통합 테스트
"""

import json
import logging
import tempfile
from pathlib import Path
from typing import List, Dict, Any

from unsloth_dataset import (
    UnslothDatasetGenerator,
    DatasetConfig,
    ComponentOrganizer,
    OrganizationConfig
)

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_test_samples() -> List[Dict[str, Any]]:
    """테스트용 샘플 데이터를 생성합니다."""
    samples = [
        # DataGrid 관련 샘플
        {
            "instruction": "Syncfusion DataGrid에서 데이터 바인딩하는 방법을 설명해주세요.",
            "response": "DataGrid에서 데이터 바인딩은 DataSource 속성을 사용합니다. List<T>, DataTable, BindingSource 등을 지원합니다.",
            "source": "md_staging/grid/page_001.md",
            "quality_score": 0.9,
            "metadata": {"component": "grid", "page": 1}
        },
        {
            "instruction": "Grid 컨트롤에서 컬럼을 동적으로 추가하는 방법은?",
            "response": "GridColumn을 생성하고 Columns.Add() 메서드를 사용하여 동적으로 컬럼을 추가할 수 있습니다.",
            "source": "md_staging/grid/page_002.md",
            "quality_score": 0.85,
            "metadata": {"component": "grid", "page": 2}
        },
        
        # Chart 관련 샘플
        {
            "instruction": "Chart 컨트롤로 막대 그래프를 만드는 방법을 알려주세요.",
            "response": "ChartSeries를 생성하고 Type을 Column으로 설정한 후 데이터를 바인딩합니다.",
            "source": "md_staging/chart/page_001.md",
            "quality_score": 0.88,
            "metadata": {"component": "chart", "page": 1}
        },
        {
            "instruction": "차트에서 범례를 커스터마이징하는 방법은?",
            "response": "Legend 속성을 통해 위치, 색상, 폰트 등을 설정할 수 있습니다.",
            "source": "md_staging/chart/page_002.md",
            "quality_score": 0.82,
            "metadata": {"component": "chart", "page": 2}
        },
        
        # DocIO 관련 샘플
        {
            "instruction": "DocIO를 사용해서 Word 문서를 생성하는 방법은?",
            "response": "WordDocument 클래스를 사용하여 새 문서를 생성하고 텍스트, 이미지 등을 추가할 수 있습니다.",
            "source": "md_staging/DocIo/page_001.md",
            "quality_score": 0.91,
            "metadata": {"component": "DocIo", "page": 1}
        },
        {
            "instruction": "Word 문서에서 표를 생성하는 방법을 설명해주세요.",
            "response": "IWTable 인터페이스를 사용하여 표를 생성하고 행과 열을 추가할 수 있습니다.",
            "source": "md_staging/DocIo/page_002.md",
            "quality_score": 0.87,
            "metadata": {"component": "DocIo", "page": 2}
        },
        
        # PDF 관련 샘플
        {
            "instruction": "PDF 문서를 생성하는 기본 방법을 알려주세요.",
            "response": "PdfDocument 클래스를 사용하여 새 PDF를 생성하고 페이지와 콘텐츠를 추가합니다.",
            "source": "md_staging/pdf/page_001.md",
            "quality_score": 0.89,
            "metadata": {"component": "pdf", "page": 1}
        },
        
        # Schedule 관련 샘플
        {
            "instruction": "스케줄러에서 약속을 추가하는 방법은?",
            "response": "ScheduleAppointment 객체를 생성하고 Appointments 컬렉션에 추가합니다.",
            "source": "md_staging/schedule/page_001.md",
            "quality_score": 0.84,
            "metadata": {"component": "schedule", "page": 1}
        },
        
        # 미분류 샘플
        {
            "instruction": "일반적인 WinForms 개발 팁을 알려주세요.",
            "response": "성능 최적화, 메모리 관리, 사용자 경험 개선 등의 팁을 제공합니다.",
            "source": "general_tips.md",
            "quality_score": 0.75,
            "metadata": {"page": 1}
        }
    ]
    
    return samples


def test_component_organization():
    """컴포넌트 조직화 기능을 테스트합니다."""
    logger.info("=== 컴포넌트 조직화 테스트 시작 ===")
    
    # 테스트 샘플 생성
    samples = create_test_samples()
    logger.info(f"테스트 샘플 수: {len(samples)}")
    
    # 조직화 설정
    org_config = OrganizationConfig(
        min_samples_per_component=1,
        max_samples_per_component=10,
        enable_hierarchical_grouping=True,
        enable_category_balancing=True,
        priority_based_sampling=True,
        output_separate_files=True,
        include_mixed_category=True,
        mixed_category_ratio=0.1
    )
    
    # 컴포넌트 조직화기 생성
    organizer = ComponentOrganizer(org_config)
    
    # 컴포넌트별 조직화 테스트
    logger.info("--- 컴포넌트별 조직화 테스트 ---")
    component_datasets = organizer.organize_by_components(samples)
    
    logger.info(f"조직화된 컴포넌트 수: {len(component_datasets)}")
    for component_name, dataset in component_datasets.items():
        logger.info(f"  {component_name} ({dataset.category}): {len(dataset.samples)} 샘플")
    
    # 카테고리별 조직화 테스트
    logger.info("--- 카테고리별 조직화 테스트 ---")
    category_datasets = organizer.organize_by_categories(component_datasets)
    
    logger.info(f"조직화된 카테고리 수: {len(category_datasets)}")
    for category, datasets in category_datasets.items():
        total_samples = sum(len(ds.samples) for ds in datasets)
        logger.info(f"  {category}: {len(datasets)} 컴포넌트, {total_samples} 샘플")
    
    # 균형잡힌 분할 테스트
    logger.info("--- 균형잡힌 분할 테스트 ---")
    train_datasets, val_datasets = organizer.create_balanced_splits(component_datasets, 0.8)
    
    logger.info("훈련/검증 분할 결과:")
    for component_name in component_datasets.keys():
        train_count = len(train_datasets[component_name].samples)
        val_count = len(val_datasets[component_name].samples)
        logger.info(f"  {component_name}: 훈련 {train_count}, 검증 {val_count}")
    
    # 카테고리별 특화 데이터셋 생성 테스트
    logger.info("--- 카테고리별 특화 데이터셋 테스트 ---")
    category_samples = organizer.create_category_specific_datasets(category_datasets, 3)
    
    logger.info("카테고리별 특화 데이터셋:")
    for category, samples in category_samples.items():
        logger.info(f"  {category}: {len(samples)} 샘플")
    
    # 조직화 리포트 생성 테스트
    logger.info("--- 조직화 리포트 생성 테스트 ---")
    report = organizer.generate_organization_report(component_datasets, category_datasets)
    
    logger.info("조직화 리포트 요약:")
    logger.info(f"  총 컴포넌트: {report['summary']['total_components']}")
    logger.info(f"  총 카테고리: {report['summary']['total_categories']}")
    logger.info(f"  총 샘플: {report['summary']['total_samples']}")
    
    if report['recommendations']:
        logger.info("권장사항:")
        for rec in report['recommendations']:
            logger.info(f"  - {rec}")
    
    logger.info("=== 컴포넌트 조직화 테스트 완료 ===")
    return True


def test_integrated_dataset_generation():
    """통합 데이터셋 생성 테스트"""
    logger.info("=== 통합 데이터셋 생성 테스트 시작 ===")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # 데이터셋 설정
        config = DatasetConfig(
            target_count=20,
            max_seq_length=8192,
            train_test_split=0.8,
            formats=["sharegpt", "alpaca"],
            min_tokens=10,
            max_tokens=8192,
            output_dir=temp_dir,
            test_mode=True,
            enable_component_organization=True,
            create_component_specific_datasets=True,
            create_category_specific_datasets=True
        )
        
        # 데이터셋 생성기 생성
        generator = UnslothDatasetGenerator(config)
        
        # 테스트 샘플로 데이터셋 생성
        samples = create_test_samples()
        result = generator.generate_from_samples(samples, "test_component_dataset")
        
        # 결과 검증
        logger.info("생성된 데이터셋 정보:")
        logger.info(f"  기본 훈련 데이터: {len(result.train_data)}")
        logger.info(f"  기본 검증 데이터: {len(result.validation_data)}")
        logger.info(f"  컴포넌트 데이터셋: {len(result.component_datasets)}")
        logger.info(f"  카테고리 데이터셋: {len(result.category_datasets)}")
        
        # 컴포넌트별 데이터셋 확인
        if result.component_train_data:
            logger.info("컴포넌트별 훈련 데이터:")
            for format_type, component_data in result.component_train_data.items():
                logger.info(f"  {format_type} 포맷:")
                for component, samples in component_data.items():
                    logger.info(f"    {component}: {len(samples)} 샘플")
        
        # 카테고리별 데이터셋 확인
        if result.category_specific_data:
            logger.info("카테고리별 특화 데이터:")
            for format_type, category_data in result.category_specific_data.items():
                logger.info(f"  {format_type} 포맷:")
                for category, samples in category_data.items():
                    logger.info(f"    {category}: {len(samples)} 샘플")
        
        # 파일 저장 테스트
        saved_paths = generator.save_datasets(result, "test_component_dataset")
        logger.info(f"저장된 파일 수: {len(saved_paths)}")
        
        # 저장된 파일 확인
        component_files = [path for key, path in saved_paths.items() if "component_" in key]
        category_files = [path for key, path in saved_paths.items() if "category_" in key]
        
        logger.info(f"컴포넌트별 파일: {len(component_files)}")
        logger.info(f"카테고리별 파일: {len(category_files)}")
        
        # 조직화 리포트 확인
        if result.organization_report:
            logger.info("조직화 리포트 생성됨")
            logger.info(f"  컴포넌트 수: {result.organization_report['summary']['total_components']}")
            logger.info(f"  카테고리 수: {result.organization_report['summary']['total_categories']}")
        
        logger.info("=== 통합 데이터셋 생성 테스트 완료 ===")
        return True


def test_component_hierarchy():
    """컴포넌트 계층 구조 테스트"""
    logger.info("=== 컴포넌트 계층 구조 테스트 시작 ===")
    
    org_config = OrganizationConfig()
    organizer = ComponentOrganizer(org_config)
    
    # 계층 구조 확인
    logger.info("정의된 컴포넌트 계층 구조:")
    for component_name, hierarchy in organizer.component_hierarchy.items():
        logger.info(f"  {component_name}:")
        logger.info(f"    카테고리: {hierarchy.category}")
        logger.info(f"    설명: {hierarchy.description}")
        logger.info(f"    우선순위: {hierarchy.priority}")
    
    # 카테고리 매핑 확인
    logger.info("\n카테고리별 컴포넌트 매핑:")
    for category, components in organizer.category_mapping.items():
        logger.info(f"  {category}: {', '.join(components)}")
    
    logger.info("=== 컴포넌트 계층 구조 테스트 완료 ===")
    return True


def main():
    """메인 테스트 함수"""
    logger.info("컴포넌트별 데이터셋 조직화 통합 테스트 시작")
    
    try:
        # 개별 테스트 실행
        test_component_hierarchy()
        test_component_organization()
        test_integrated_dataset_generation()
        
        logger.info("✅ 모든 테스트가 성공적으로 완료되었습니다!")
        return True
        
    except Exception as e:
        logger.error(f"❌ 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)