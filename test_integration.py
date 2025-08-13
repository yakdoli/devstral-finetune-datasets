#!/usr/bin/env python3
"""
통합 테스트 스크립트
기존 unsloth_dataset 모듈과 quality_validator 모듈의 통합을 테스트합니다.
"""

import sys
import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Any

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 모듈 임포트
try:
    from unsloth_dataset import UnslothDatasetGenerator, DatasetConfig, create_dataset_generator
    from quality_validator import QualityValidator, QualityValidatorConfig, create_default_validator
    print("✓ 모듈 임포트 성공")
except ImportError as e:
    print(f"✗ 모듈 임포트 실패: {e}")
    sys.exit(1)

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_test_data() -> Dict[str, List[Dict[str, Any]]]:
    """테스트 데이터를 생성합니다."""
    test_data = {
        "sharegpt": [
            {
                "conversations": [
                    {"from": "system", "value": "Syncfusion WinForms 전문가"},
                    {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                    {"from": "gpt", "value": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용"}
                ]
            },
            {
                "conversations": [
                    {"from": "system", "value": "Syncfusion WinForms 전문가"},
                    {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                    {"from": "gpt", "value": "Chart 컴포넌트 사용법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가"}
                ]
            },
            {
                "conversations": [
                    {"from": "system", "value": "Syncfusion WinForms 전문가"},
                    {"from": "human", "value": "DataGrid 사용법을 알려주세요.."},  # 중복 구두점
                    {"from": "gpt", "value": "DataGrid 컴포넌트 사용법은 다음과 같습니다..."}  # 중복 구두점
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
            },
            {
                "instruction": "DataGrid 사용법을 설명해주세요",  # 문장 끝에 마침표 없음
                "input": "초보자도 이해할 수 있도록 설명해주세요",
                "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용"
            }
        ],
        "openai": [
            {
                "messages": [
                    {"role": "system", "content": "Syncfusion WinForms 전문가"},
                    {"role": "user", "content": "DataGrid 사용법을 알려주세요."},
                    {"role": "assistant", "content": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용"}
                ]
            },
            {
                "messages": [
                    {"role": "system", "content": "Syncfusion WinForms 전문가"},
                    {"role": "user", "content": "Chart 컴포넌트 사용법을 알려주세요."},
                    {"role": "assistant", "content": "Chart 컴포넌트 사용법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가"}
                ]
            },
            {
                "messages": [
                    {"role": "system", "content": "Syncfusion WinForms 전문가"},
                    {"role": "user", "content": "DataGrid 사용법을 알려주세요.."},  # 중복 구두점
                    {"role": "assistant", "content": "DataGrid 컴포넌트 사용법은 다음과 같습니다..."}  # 중복 구두점
                ]
            }
        ]
    }
    
    return test_data


def test_unsloth_dataset_generator():
    """UnslothDatasetGenerator 테스트"""
    print("\n=== UnslothDatasetGenerator 테스트 ===")
    
    try:
        # 생성기 생성
        config = DatasetConfig(
            target_count=100,
            max_seq_length=4096,
            train_test_split=0.9,
            formats=["sharegpt", "alpaca", "openai"],
            min_tokens=50,
            max_tokens=4096,
            eos_token="</s>",
            remove_duplicates=True,
            quality_threshold=0.7
        )
        
        generator = create_dataset_generator(config)
        print("✓ UnslothDatasetGenerator 생성 성공")
        
        # 샘플 데이터로 테스트 (UnslothDatasetGenerator가 기대하는 형식)
        sample_data = [
            {
                "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
                "response": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용",
                "quality_score": 0.8,
                "source": "test"
            },
            {
                "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
                "response": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가",
                "quality_score": 0.9,
                "source": "test"
            }
        ]
        
        # 데이터셋 생성
        result = generator.generate_from_samples(sample_data, "test_dataset")
        print("✓ 데이터셋 생성 성공")
        
        # 결과 확인
        print(f"생성된 데이터셋 포맷: {list(result.train_data.keys())}")
        for format_type, data in result.train_data.items():
            print(f"  {format_type}: {len(data)} 아이템")
        
        return True
        
    except Exception as e:
        print(f"✗ UnslothDatasetGenerator 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_quality_validator():
    """QualityValidator 테스트"""
    print("\n=== QualityValidator 테스트 ===")
    
    try:
        # 품질 검증기 생성
        validator = create_default_validator()
        print("✓ QualityValidator 생성 성공")
        
        # 테스트 데이터 생성
        test_data = create_test_data()
        print(f"✓ 테스트 데이터 생성: {len(test_data)} 포맷, {sum(len(data) for data in test_data.values())} 아이템")
        
        # 검증 수행
        print("검증 시작...")
        validated_datasets = validator.validate_and_filter(test_data)
        print("✓ 검증 완료")
        
        # 결과 확인
        print(f"검증 결과:")
        for format_type, items in validated_datasets.items():
            valid_count = sum(1 for item in items if item.is_valid)
            print(f"  {format_type}: {valid_count}/{len(items)} 아이템 유효")
            
            # 샘플 아이템 정보 출력
            if items:
                sample_item = items[0]
                print(f"    샘플 아이템 ID: {sample_item.id}")
                print(f"    안전 점수: {sample_item.quality_validation.get('safety_score', 0.0):.3f}")
                print(f"    품질 점수: {sample_item.quality_validation.get('quality_score', 0.0):.3f}")
                print(f"    호환성 점수: {sample_item.quality_validation.get('compatibility_score', 0.0):.3f}")
        
        # 리포트 생성
        report = validator.generate_report(validated_datasets)
        print("✓ 검증 리포트 생성 성공")
        
        # 리포트 요약 출력
        print(f"\n리포트 요약:")
        print(f"  전체 아이템: {report['summary']['total_items']}")
        print(f"  유효 아이템: {report['summary']['passed_items']}")
        print(f"  무효 아이템: {report['summary']['failed_items']}")
        print(f"  전체 유효율: {report['summary']['overall_validity_rate']:.2%}")
        
        return True
        
    except Exception as e:
        print(f"✗ QualityValidator 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_integration():
    """통합 테스트"""
    print("\n=== 통합 테스트 ===")
    
    try:
        # 생성기 생성
        generator_config = DatasetConfig(
            target_count=50,
            max_seq_length=4096,
            train_test_split=0.9,
            formats=["sharegpt", "alpaca", "openai"],
            min_tokens=50,
            max_tokens=4096,
            eos_token="</s>",
            remove_duplicates=True,
            quality_threshold=0.7
        )
        
        generator = create_dataset_generator(generator_config)
        
        # 품질 검증기 생성
        validator = create_default_validator()
        
        # 샘플 데이터 생성 (UnslothDatasetGenerator가 기대하는 형식)
        sample_data = [
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
        
        print("데이터셋 생성 시작...")
        # 데이터셋 생성
        result = generator.generate_from_samples(sample_data, "integration_test_dataset")
        print("✓ 데이터셋 생성 성공")
        
        # 생성된 데이터 확인
        print(f"생성된 데이터셋:")
        for format_type, data in result.train_data.items():
            print(f"  {format_type}: {len(data)} 아이템")
        
        # 품질 검증 수행
        print("\n품질 검증 시작...")
        validated_datasets = validator.validate_and_filter(result.train_data)
        print("✓ 품질 검증 완료")
        
        # 통합 결과 확인
        print(f"\n통합 결과:")
        total_original = sum(len(data) for data in result.train_data.values())
        total_validated = sum(len(data) for data in validated_datasets.values())
        total_valid = sum(len([item for item in data if item.is_valid]) for data in validated_datasets.values())
        
        print(f"  원본 데이터: {total_original} 아이템")
        print(f"  검증 데이터: {total_validated} 아이템")
        print(f"  유효 데이터: {total_valid} 아이템")
        print(f"  유효율: {total_valid/total_original:.2%}")
        
        # 상세 결과 출력
        for format_type, validated_items in validated_datasets.items():
            print(f"\n{format_type.upper()} 포맷 결과:")
            for i, item in enumerate(validated_items[:2]):  # 상위 2개 아이템만 출력
                print(f"  아이템 {i+1}:")
                print(f"    ID: {item.id}")
                print(f"    유효 여부: {item.is_valid}")
                if item.is_valid:
                    print(f"    안전 점수: {item.quality_validation.get('safety_score', 0.0):.3f}")
                    print(f"    품질 점수: {item.quality_validation.get('quality_score', 0.0):.3f}")
                    print(f"    호환성 점수: {item.quality_validation.get('compatibility_score', 0.0):.3f}")
                else:
                    print(f"    무효 사유: {item.quality_validation.get('issues', [])}")
        
        # 리포트 생성
        report = validator.generate_report(validated_datasets)
        
        # 리포트 저장
        report_path = "integration_test_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"✓ 리포트 저장: {report_path}")
        
        return True
        
    except Exception as e:
        print(f"✗ 통합 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_performance():
    """성능 테스트"""
    print("\n=== 성능 테스트 ===")
    
    try:
        import time
        
        # 대용량 테스트 데이터 생성
        large_test_data = create_test_data()
        
        # 데이터 확장
        for format_type, items in large_test_data.items():
            large_test_data[format_type] = items * 20  # 20배 확장
        
        total_items = sum(len(data) for data in large_test_data.values())
        print(f"테스트 데이터 크기: {total_items} 아이템")
        
        # 품질 검증기 생성
        validator = create_default_validator()
        
        # 성능 측정
        start_time = time.time()
        
        print("성능 테스트 시작...")
        validated_datasets = validator.validate_and_filter(large_test_data)
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        # 결과 분석
        total_valid = sum(len([item for item in data if item.is_valid]) for data in validated_datasets.values())
        
        print(f"✓ 성능 테스트 완료")
        print(f"  처리 시간: {processing_time:.2f}초")
        print(f"  처리 속도: {total_items/processing_time:.2f} 아이템/초")
        print(f"  유효 아이템: {total_valid}/{total_items} ({total_valid/total_items:.2%})")
        
        return True
        
    except Exception as e:
        print(f"✗ 성능 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """메인 테스트 함수"""
    print("=== Unsloth Dataset + Quality Validator 통합 테스트 ===")
    
    # 테스트 결과
    test_results = {}
    
    # 개별 모듈 테스트
    test_results['unsloth_generator'] = test_unsloth_dataset_generator()
    test_results['quality_validator'] = test_quality_validator()
    
    # 통합 테스트
    test_results['integration'] = test_integration()
    
    # 성능 테스트
    test_results['performance'] = test_performance()
    
    # 최종 결과
    print("\n=== 테스트 결과 요약 ===")
    passed_tests = sum(test_results.values())
    total_tests = len(test_results)
    
    for test_name, result in test_results.items():
        status = "✓ 통과" if result else "✗ 실패"
        print(f"{test_name}: {status}")
    
    print(f"\n전체 결과: {passed_tests}/{total_tests} 테스트 통과")
    
    if passed_tests == total_tests:
        print("🎉 모든 테스트를 통과했습니다!")
        return True
    else:
        print("⚠️ 일부 테스트가 실패했습니다.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)