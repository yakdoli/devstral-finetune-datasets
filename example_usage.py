#!/usr/bin/env python3
"""
데이터 품질 검증 및 필터링 시스템 통합 사용 예제

이 예제는 UnslothDatasetGenerator와 QualityValidator를 통합하여
고품질의 Unsloth 호환 데이터셋을 생성하고 검증하는 전체 과정을 보여줍니다.
"""

from unsloth_dataset import UnslothDatasetGenerator, DatasetConfig, create_dataset_generator
from quality_validator import QualityValidator, QualityValidatorConfig
import logging
import json
from datetime import datetime

def setup_logging():
    """로깅 설정"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def create_sample_data():
    """테스트용 샘플 데이터 생성"""
    return [
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
            "response": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 Syncfusion 참조 추가\n2. DataGrid 컨트롤을 폼에 배치\n3. 데이터 소스(DataTable, BindingSource) 설정\n4. 컬럼 구성 및 스타일 적용\n5. 이벤트 핸들러 구현",
            "quality_score": 0.8,
            "source": "test"
        },
        {
            "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
            "response": "Chart 컴포넌트 막대 그래프 생성:\n1. Chart 컨트롤 폼에 추가\n2. Series(데이터 시리즈) 설정\n3. 데이터 바인딩 (DataTable, List 등)\n4. X축, Y축 레이블 및 형식 설정\n5. 범례, 제목, 배경 스타일 적용",
            "quality_score": 0.9,
            "source": "test"
        },
        {
            "instruction": "GridControl에서 데이터 그룹화하는 방법",
            "response": "GridControl 데이터 그룹화:\n1. GridControl.DataSource 설정\n2. GridView.GroupedColumns 속성 사용\n3. 그룹화 기준 컬럼 지정\n4. 그룹 헤더 스타일 설정\n5. 그룹 펼침/접기 이벤트 처리",
            "quality_score": 0.85,
            "source": "test"
        }
    ]

def main():
    """메인 실행 함수"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("=== 데이터 품질 검증 및 필터링 시스템 통합 예제 ===")
    
    # 1. 데이터셋 생성기 초기화
    logger.info("1. 데이터셋 생성기 초기화...")
    generator_config = DatasetConfig(
        target_count=100,
        max_seq_length=8192,
        train_test_split=0.9,
        formats=["sharegpt", "alpaca", "openai"],
        min_tokens=50,
        max_tokens=8192,
        eos_token="</s>",
        remove_duplicates=True,
        quality_threshold=0.7,
        batch_size=10,
        max_workers=8,
        seed=42,
        output_dir="output/dataset",
        include_metadata=True,
        shuffle_data=True
    )
    
    generator = create_dataset_generator(generator_config)
    
    # 2. 품질 검증기 초기화
    logger.info("2. 품질 검증기 초기화...")
    validator_config = QualityValidatorConfig(
        min_quality_score=0.7,
        max_similarity_threshold=0.9,
        safety_threshold=0,
        enable_auto_correction=True,
        enable_statistics_analysis=True,
        batch_size=10,
        max_workers=8,
        output_format="enhanced",
        include_metadata=True,
        generate_report=True
    )
    validator = QualityValidator(validator_config)
    
    # 3. 샘플 데이터 생성
    logger.info("3. 샘플 데이터 생성...")
    sample_data = create_sample_data()
    logger.info(f"생성된 샘플 데이터: {len(sample_data)}개")
    
    # 4. 데이터셋 생성
    logger.info("4. 데이터셋 생성 시작...")
    raw_datasets = generator.generate_from_samples(sample_data, "test_dataset")
    
    # 생성된 데이터셋 정보 출력
    logger.info("=== 생성된 데이터셋 정보 ===")
    for format_type, data in raw_datasets.train_data.items():
        logger.info(f"{format_type}: {len(data)}개 훈련 데이터")
    for format_type, data in raw_datasets.validation_data.items():
        logger.info(f"{format_type}: {len(data)}개 검증 데이터")
    
    # 5. 품질 검증 및 필터링
    logger.info("5. 품질 검증 및 필터링 시작...")
    
    # DatasetGenerationResult를 QualityValidator가 기대하는 형식으로 변환
    datasets_for_validation = {}
    for format_type in ["sharegpt", "alpaca", "openai"]:
        train_data = raw_datasets.train_data.get(format_type, [])
        val_data = raw_datasets.validation_data.get(format_type, [])
        datasets_for_validation[format_type] = train_data + val_data
    
    validated_datasets = validator.validate_and_filter(datasets_for_validation)
    
    # 6. 검증 리포트 생성
    logger.info("6. 검증 리포트 생성...")
    validation_report = validator.generate_report(validated_datasets)
    
    # 7. 결과 출력
    logger.info("=== 검증 결과 요약 ===")
    logger.info(f"리포트 키: {list(validation_report['summary'].keys())}")
    logger.info(f"전체 아이템: {validation_report['summary']['total_items']}")
    logger.info(f"통과 아이템: {validation_report['summary']['passed_items']}")
    logger.info(f"실패 아이템: {validation_report['summary']['failed_items']}")
    logger.info(f"전체 유효율: {validation_report['summary']['overall_validity_rate']:.2f}%")
    
    # 8. 상세 결과 출력
    logger.info("=== 리포트 전체 구조 ===")
    logger.info(f"리포트 키: {list(validation_report.keys())}")
    
    if 'format_statistics' in validation_report:
        logger.info("=== 포맷별 상세 결과 ===")
        for format_type, result in validation_report['format_statistics'].items():
            logger.info(f"{format_type}:")
            logger.info(f"  전체 아이템: {result['total']}")
            logger.info(f"  유효 아이템: {result['valid']}")
            logger.info(f"  무효 아이템: {result['invalid']}")
            logger.info(f"  유효율: {result['validity_rate']:.2f}%")
    
    # 9. 검증된 데이터 샘플 출력
    logger.info("=== 검증된 데이터 샘플 ===")
    for format_type, data in validated_datasets.items():
        if data:
            sample_item = data[0]
            logger.info(f"{format_type} 포맷 샘플:")
            logger.info(f"  ID: {sample_item.id}")
            logger.info(f"  안전 점수: {sample_item.quality_validation.get('safety_score', 'N/A')}")
            logger.info(f"  품질 점수: {sample_item.quality_validation.get('quality_score', 'N/A')}")
            logger.info(f"  중복 상태: {sample_item.quality_validation.get('duplicate_status', 'N/A')}")
            logger.info(f"  Unsloth 호환성: {sample_item.quality_validation.get('unsloth_compatible', 'N/A')}")
            break
    
    # 10. 최종 결과 저장
    logger.info("10. 최종 결과 저장...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 검증 리포트 저장
    report_path = f"output/validation_report_{timestamp}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(validation_report, f, ensure_ascii=False, indent=2)
    logger.info(f"검증 리포트 저장: {report_path}")
    
    # 검증된 데이터셋 저장
    for format_type, data in validated_datasets.items():
        if data:
            dataset_path = f"output/validated_{format_type}_dataset_{timestamp}.jsonl"
            with open(dataset_path, 'w', encoding='utf-8') as f:
                for item in data:
                    # ValidationResult 객체를 딕셔너리로 변환
                    if hasattr(item, '__dict__'):
                        item_dict = vars(item)
                    else:
                        item_dict = item
                    f.write(json.dumps(item_dict, ensure_ascii=False) + '\n')
            logger.info(f"검증된 {format_type} 데이터셋 저장: {dataset_path}")
    
    logger.info("=== 데이터 품질 검증 및 필터링 시스템 통합 예제 완료 ===")
    
    return {
        "generator_config": generator_config,
        "validator_config": {
            "min_quality_score": validator.config.min_quality_score,
            "max_similarity_threshold": validator.config.max_similarity_threshold,
            "safety_threshold": validator.config.safety_threshold,
            "enable_auto_correction": validator.config.enable_auto_correction
        },
        "validation_report": validation_report,
        "validated_datasets": validated_datasets
    }

if __name__ == "__main__":
    try:
        result = main()
        print("\n🎉 통합 예제 실행 성공!")
        print(f"최종 유효 데이터셋 크기: {sum(len(data) for data in result['validated_datasets'].values())}")
    except Exception as e:
        print(f"\n❌ 통합 예제 실행 실패: {e}")
        import traceback
        traceback.print_exc()