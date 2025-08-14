#!/usr/bin/env python3
"""
컴포넌트별 데이터셋 조직화 최종 통합 테스트
전체 파이프라인에서 컴포넌트 조직화 기능이 올바르게 작동하는지 검증합니다.
"""

import json
import logging
import tempfile
import asyncio
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


def create_comprehensive_test_samples() -> List[Dict[str, Any]]:
    """포괄적인 테스트 샘플 데이터를 생성합니다."""
    samples = []
    
    # 각 컴포넌트별로 다양한 샘플 생성
    component_samples = {
        "grid": [
            {
                "instruction": "DataGrid에서 데이터 바인딩하는 방법을 설명해주세요.",
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
            {
                "instruction": "DataGrid에서 셀 편집을 활성화하는 방법은?",
                "response": "AllowEditing 속성을 true로 설정하고 EditMode를 지정하여 셀 편집을 활성화할 수 있습니다.",
                "source": "md_staging/grid/page_003.md",
                "quality_score": 0.88,
                "metadata": {"component": "grid", "page": 3}
            }
        ],
        "chart": [
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
            {
                "instruction": "차트에 애니메이션 효과를 추가하는 방법은?",
                "response": "EnableAnimation 속성을 true로 설정하고 AnimationDuration을 지정합니다.",
                "source": "md_staging/chart/page_003.md",
                "quality_score": 0.86,
                "metadata": {"component": "chart", "page": 3}
            }
        ],
        "DocIo": [
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
            }
        ],
        "pdf": [
            {
                "instruction": "PDF 문서를 생성하는 기본 방법을 알려주세요.",
                "response": "PdfDocument 클래스를 사용하여 새 PDF를 생성하고 페이지와 콘텐츠를 추가합니다.",
                "source": "md_staging/pdf/page_001.md",
                "quality_score": 0.89,
                "metadata": {"component": "pdf", "page": 1}
            },
            {
                "instruction": "PDF에 이미지를 삽입하는 방법은?",
                "response": "PdfBitmap 클래스를 사용하여 이미지를 로드하고 DrawImage 메서드로 삽입합니다.",
                "source": "md_staging/pdf/page_002.md",
                "quality_score": 0.84,
                "metadata": {"component": "pdf", "page": 2}
            }
        ],
        "XlsIO": [
            {
                "instruction": "XlsIO로 Excel 파일을 생성하는 방법은?",
                "response": "ExcelEngine을 생성하고 IWorkbook을 통해 새 Excel 파일을 만들 수 있습니다.",
                "source": "md_staging/XlsIO/page_001.md",
                "quality_score": 0.92,
                "metadata": {"component": "XlsIO", "page": 1}
            },
            {
                "instruction": "Excel에서 차트를 생성하는 방법을 설명해주세요.",
                "response": "IChartShape을 사용하여 워크시트에 차트를 추가하고 데이터 범위를 설정합니다.",
                "source": "md_staging/XlsIO/page_002.md",
                "quality_score": 0.88,
                "metadata": {"component": "XlsIO", "page": 2}
            }
        ],
        "schedule": [
            {
                "instruction": "스케줄러에서 약속을 추가하는 방법은?",
                "response": "ScheduleAppointment 객체를 생성하고 Appointments 컬렉션에 추가합니다.",
                "source": "md_staging/schedule/page_001.md",
                "quality_score": 0.84,
                "metadata": {"component": "schedule", "page": 1}
            }
        ],
        "Gauge": [
            {
                "instruction": "Gauge 컨트롤로 원형 게이지를 만드는 방법은?",
                "response": "CircularGauge 컨트롤을 사용하고 Scale과 Pointer를 설정합니다.",
                "source": "md_staging/Gauge/page_001.md",
                "quality_score": 0.81,
                "metadata": {"component": "Gauge", "page": 1}
            }
        ]
    }
    
    # 모든 컴포넌트 샘플을 하나의 리스트로 통합
    for component_name, component_samples_list in component_samples.items():
        samples.extend(component_samples_list)
    
    # 미분류 샘플 추가
    samples.extend([
        {
            "instruction": "일반적인 WinForms 개발 팁을 알려주세요.",
            "response": "성능 최적화, 메모리 관리, 사용자 경험 개선 등의 팁을 제공합니다.",
            "source": "general_tips.md",
            "quality_score": 0.75,
            "metadata": {"page": 1}
        },
        {
            "instruction": "Syncfusion 컨트롤의 테마를 변경하는 방법은?",
            "response": "ThemeManager를 사용하여 전역 테마를 설정하거나 개별 컨트롤의 테마를 변경할 수 있습니다.",
            "source": "theming_guide.md",
            "quality_score": 0.78,
            "metadata": {"page": 1}
        }
    ])
    
    return samples


def test_component_organization_comprehensive():
    """포괄적인 컴포넌트 조직화 테스트"""
    logger.info("=== 포괄적인 컴포넌트 조직화 테스트 시작 ===")
    
    # 테스트 샘플 생성
    samples = create_comprehensive_test_samples()
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
    
    # 1. 컴포넌트별 조직화
    logger.info("--- 1. 컴포넌트별 조직화 ---")
    component_datasets = organizer.organize_by_components(samples)
    
    logger.info(f"조직화된 컴포넌트 수: {len(component_datasets)}")
    for component_name, dataset in component_datasets.items():
        logger.info(f"  {component_name} ({dataset.category}): {len(dataset.samples)} 샘플, "
                   f"평균 품질: {dataset.metadata.get('avg_quality_score', 0):.3f}")
    
    # 2. 카테고리별 조직화
    logger.info("--- 2. 카테고리별 조직화 ---")
    category_datasets = organizer.organize_by_categories(component_datasets)
    
    logger.info(f"조직화된 카테고리 수: {len(category_datasets)}")
    for category, datasets_list in category_datasets.items():
        total_samples = sum(len(ds.samples) for ds in datasets_list)
        avg_quality = sum(ds.metadata.get("avg_quality_score", 0) for ds in datasets_list) / len(datasets_list)
        logger.info(f"  {category}: {len(datasets_list)} 컴포넌트, {total_samples} 샘플, "
                   f"평균 품질: {avg_quality:.3f}")
    
    # 3. 균형잡힌 분할
    logger.info("--- 3. 균형잡힌 분할 ---")
    train_datasets, val_datasets = organizer.create_balanced_splits(component_datasets, 0.8)
    
    logger.info("훈련/검증 분할 결과:")
    for component_name in component_datasets.keys():
        train_count = len(train_datasets[component_name].samples)
        val_count = len(val_datasets[component_name].samples)
        total_count = train_count + val_count
        train_ratio = train_count / total_count if total_count > 0 else 0
        logger.info(f"  {component_name}: 훈련 {train_count}, 검증 {val_count} (비율: {train_ratio:.2f})")
    
    # 4. 카테고리별 특화 데이터셋
    logger.info("--- 4. 카테고리별 특화 데이터셋 ---")
    category_samples = organizer.create_category_specific_datasets(category_datasets, 5)
    
    logger.info("카테고리별 특화 데이터셋:")
    for category, samples_list in category_samples.items():
        components = set(sample.get("component", "unknown") for sample in samples_list)
        logger.info(f"  {category}: {len(samples_list)} 샘플, 컴포넌트: {', '.join(components)}")
    
    # 5. 조직화 리포트
    logger.info("--- 5. 조직화 리포트 ---")
    report = organizer.generate_organization_report(component_datasets, category_datasets)
    
    logger.info("조직화 리포트 요약:")
    logger.info(f"  총 컴포넌트: {report['summary']['total_components']}")
    logger.info(f"  총 카테고리: {report['summary']['total_categories']}")
    logger.info(f"  총 샘플: {report['summary']['total_samples']}")
    
    if report['recommendations']:
        logger.info("권장사항:")
        for rec in report['recommendations']:
            logger.info(f"  - {rec}")
    
    # 6. 검증
    logger.info("--- 6. 결과 검증 ---")
    
    # 모든 샘플이 분류되었는지 확인
    total_organized_samples = sum(len(ds.samples) for ds in component_datasets.values())
    assert total_organized_samples == len(samples), f"샘플 수 불일치: {total_organized_samples} != {len(samples)}"
    
    # 각 카테고리에 적절한 컴포넌트가 포함되었는지 확인
    expected_categories = {
        "data_display": ["grid"],
        "visualization": ["chart", "Gauge"],
        "document_processing": ["DocIo", "pdf", "XlsIO"],
        "scheduling": ["schedule"],
        "mixed": ["mixed"]
    }
    
    for category, expected_components in expected_categories.items():
        if category in category_datasets:
            actual_components = [ds.component_name for ds in category_datasets[category]]
            for expected_comp in expected_components:
                if expected_comp in component_datasets:
                    assert expected_comp in actual_components, f"컴포넌트 {expected_comp}가 카테고리 {category}에 없음"
    
    logger.info("✅ 모든 검증 통과")
    logger.info("=== 포괄적인 컴포넌트 조직화 테스트 완료 ===")
    return True


def test_integrated_dataset_generation_with_organization():
    """컴포넌트 조직화가 포함된 통합 데이터셋 생성 테스트"""
    logger.info("=== 통합 데이터셋 생성 + 컴포넌트 조직화 테스트 시작 ===")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # 데이터셋 설정 (컴포넌트 조직화 포함)
        config = DatasetConfig(
            target_count=50,
            max_seq_length=8192,
            train_test_split=0.8,
            formats=["sharegpt", "alpaca", "openai"],
            min_tokens=10,
            max_tokens=8192,
            output_dir=temp_dir,
            test_mode=True,
            enable_component_organization=True,
            create_component_specific_datasets=True,
            create_category_specific_datasets=True,
            component_organization=OrganizationConfig(
                min_samples_per_component=1,
                max_samples_per_component=20,
                enable_hierarchical_grouping=True,
                enable_category_balancing=True,
                priority_based_sampling=True,
                output_separate_files=True,
                include_mixed_category=True,
                mixed_category_ratio=0.1
            )
        )
        
        # 데이터셋 생성기 생성
        generator = UnslothDatasetGenerator(config)
        
        # 테스트 샘플로 데이터셋 생성
        samples = create_comprehensive_test_samples()
        result = generator.generate_from_samples(samples, "comprehensive_test_dataset")
        
        # 결과 검증
        logger.info("생성된 데이터셋 정보:")
        logger.info(f"  기본 훈련 데이터 포맷: {len(result.train_data)}")
        logger.info(f"  기본 검증 데이터 포맷: {len(result.validation_data)}")
        logger.info(f"  컴포넌트 데이터셋: {len(result.component_datasets)}")
        logger.info(f"  카테고리 데이터셋: {len(result.category_datasets)}")
        
        # 각 포맷별 기본 데이터셋 확인
        for format_type, train_data in result.train_data.items():
            val_data = result.validation_data.get(format_type, [])
            logger.info(f"  {format_type}: 훈련 {len(train_data)}, 검증 {len(val_data)}")
        
        # 컴포넌트별 데이터셋 확인
        if result.component_train_data:
            logger.info("컴포넌트별 훈련 데이터:")
            for format_type, component_data in result.component_train_data.items():
                logger.info(f"  {format_type} 포맷:")
                for component, samples_list in component_data.items():
                    logger.info(f"    {component}: {len(samples_list)} 샘플")
        
        # 카테고리별 데이터셋 확인
        if result.category_specific_data:
            logger.info("카테고리별 특화 데이터:")
            for format_type, category_data in result.category_specific_data.items():
                logger.info(f"  {format_type} 포맷:")
                for category, samples_list in category_data.items():
                    logger.info(f"    {category}: {len(samples_list)} 샘플")
        
        # 파일 저장 및 검증
        saved_paths = generator.save_datasets(result, "comprehensive_test_dataset")
        logger.info(f"저장된 파일 수: {len(saved_paths)}")
        
        # 파일 존재 확인
        for file_type, file_path in saved_paths.items():
            assert Path(file_path).exists(), f"파일이 존재하지 않음: {file_path}"
        
        # 컴포넌트별 파일 확인
        component_files = [path for key, path in saved_paths.items() if "component_" in key]
        category_files = [path for key, path in saved_paths.items() if "category_" in key]
        
        logger.info(f"컴포넌트별 파일: {len(component_files)}")
        logger.info(f"카테고리별 파일: {len(category_files)}")
        
        # 조직화 리포트 확인
        if result.organization_report:
            logger.info("조직화 리포트:")
            logger.info(f"  컴포넌트 수: {result.organization_report['summary']['total_components']}")
            logger.info(f"  카테고리 수: {result.organization_report['summary']['total_categories']}")
            logger.info(f"  총 샘플: {result.organization_report['summary']['total_samples']}")
        
        # 샘플 파일 내용 검증
        logger.info("--- 샘플 파일 내용 검증 ---")
        
        # 기본 데이터셋 파일 검증
        for format_type in config.formats:
            train_file = Path(temp_dir) / f"comprehensive_test_dataset_{format_type}_train" / "train.jsonl"
            if train_file.exists():
                with open(train_file, 'r', encoding='utf-8') as f:
                    train_samples = [json.loads(line) for line in f]
                logger.info(f"  {format_type} 훈련 파일: {len(train_samples)} 샘플")
                
                # 첫 번째 샘플 구조 확인
                if train_samples:
                    sample = train_samples[0]
                    if format_type == "sharegpt":
                        assert "conversations" in sample, "ShareGPT 포맷에 conversations 필드가 없음"
                    elif format_type == "alpaca":
                        assert "instruction" in sample and "output" in sample, "Alpaca 포맷 필드가 없음"
                    elif format_type == "openai":
                        assert "messages" in sample, "OpenAI 포맷에 messages 필드가 없음"
        
        # 컴포넌트별 파일 검증
        components_dir = Path(temp_dir) / "components"
        if components_dir.exists():
            for component_dir in components_dir.iterdir():
                if component_dir.is_dir():
                    logger.info(f"  컴포넌트 '{component_dir.name}' 디렉토리 확인됨")
                    
                    # 메타데이터 파일 확인
                    metadata_file = component_dir / "metadata.json"
                    if metadata_file.exists():
                        with open(metadata_file, 'r', encoding='utf-8') as f:
                            metadata = json.load(f)
                        logger.info(f"    메타데이터: {metadata.get('sample_count', 0)} 샘플")
        
        logger.info("✅ 모든 파일 검증 통과")
        logger.info("=== 통합 데이터셋 생성 + 컴포넌트 조직화 테스트 완료 ===")
        return True


def test_performance_and_scalability():
    """성능 및 확장성 테스트"""
    logger.info("=== 성능 및 확장성 테스트 시작 ===")
    
    import time
    
    # 대량 샘플 생성 (실제 환경 시뮬레이션)
    base_samples = create_comprehensive_test_samples()
    large_samples = []
    
    # 샘플을 복제하여 대량 데이터셋 생성
    for i in range(10):  # 10배 확장
        for sample in base_samples:
            new_sample = sample.copy()
            new_sample["instruction"] = f"[복제 {i+1}] {sample['instruction']}"
            new_sample["metadata"] = {**sample.get("metadata", {}), "replica": i+1}
            large_samples.append(new_sample)
    
    logger.info(f"대량 테스트 샘플 수: {len(large_samples)}")
    
    # 성능 측정
    start_time = time.time()
    
    # 조직화 설정
    org_config = OrganizationConfig(
        min_samples_per_component=5,
        max_samples_per_component=50,
        enable_hierarchical_grouping=True,
        enable_category_balancing=True,
        priority_based_sampling=True,
        output_separate_files=True,
        include_mixed_category=True,
        mixed_category_ratio=0.1
    )
    
    # 컴포넌트 조직화기 생성
    organizer = ComponentOrganizer(org_config)
    
    # 조직화 수행
    component_datasets = organizer.organize_by_components(large_samples)
    category_datasets = organizer.organize_by_categories(component_datasets)
    
    # 성능 측정 완료
    end_time = time.time()
    processing_time = end_time - start_time
    
    logger.info(f"처리 시간: {processing_time:.2f}초")
    logger.info(f"초당 처리 샘플 수: {len(large_samples) / processing_time:.1f}")
    logger.info(f"조직화된 컴포넌트 수: {len(component_datasets)}")
    logger.info(f"조직화된 카테고리 수: {len(category_datasets)}")
    
    # 메모리 사용량 확인
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 / 1024  # MB
    logger.info(f"메모리 사용량: {memory_usage:.1f} MB")
    
    # 성능 기준 검증
    assert processing_time < 30, f"처리 시간이 너무 오래 걸림: {processing_time:.2f}초"
    assert len(large_samples) / processing_time > 10, f"처리 속도가 너무 느림: {len(large_samples) / processing_time:.1f} 샘플/초"
    
    logger.info("✅ 성능 및 확장성 테스트 통과")
    logger.info("=== 성능 및 확장성 테스트 완료 ===")
    return True


def main():
    """메인 테스트 함수"""
    logger.info("컴포넌트별 데이터셋 조직화 최종 통합 테스트 시작")
    
    try:
        # 개별 테스트 실행
        test_component_organization_comprehensive()
        test_integrated_dataset_generation_with_organization()
        test_performance_and_scalability()
        
        logger.info("🎉 모든 통합 테스트가 성공적으로 완료되었습니다!")
        logger.info("컴포넌트별 데이터셋 조직화 기능이 올바르게 구현되었습니다.")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ 통합 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)