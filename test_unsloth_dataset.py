#!/usr/bin/env python3
"""
Unsloth 데이터셋 생성기 통합 테스트
모든 모듈의 통합 기능을 검증하는 테스트 스크립트입니다.
"""

import sys
import os
import json
import tempfile
import shutil
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from unsloth_dataset.generator import UnslothDatasetGenerator, DatasetConfig
from unsloth_dataset.validator import UnslothValidator
from unsloth_dataset.statistics import StatisticsGenerator
from unsloth_dataset.utils import setup_logging, normalize_text, remove_duplicates, split_train_test
from unsloth_dataset.formatters import create_formatter


def test_formatters():
    """포맷터 모듈 테스트"""
    print("=== Testing Formatters ===")
    
    # 테스트 데이터
    test_samples = [
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
            "response": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용",
            "source": "documentation",
            "quality_score": 0.9
        },
        {
            "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
            "response": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가",
            "source": "tutorial",
            "quality_score": 0.8
        }
    ]
    
    # 각 포맷별 테스트
    formats = ["sharegpt", "alpaca", "openai"]
    
    for format_type in formats:
        print(f"\nTesting {format_type} formatter...")
        
        try:
            formatter = create_formatter(format_type)
            
            # 단일 샘플 테스트
            if format_type == "sharegpt":
                # 대화 형식으로 변환
                conversation_data = [
                    {"from": "system", "value": "Syncfusion WinForms 전문가"},
                    {"from": "human", "value": test_samples[0]["instruction"]},
                    {"from": "gpt", "value": test_samples[0]["response"]}
                ]
                result = formatter.format_from_conversation(conversation_data)
                
            elif format_type == "alpaca":
                result = formatter.format_messages(
                    instruction=test_samples[0]["instruction"],
                    response=test_samples[0]["response"],
                    context=test_samples[0].get("context", "")
                )
                
            elif format_type == "openai":
                result = formatter.format_messages(
                    user_message=test_samples[0]["instruction"],
                    assistant_message=test_samples[0]["response"],
                    system_prompt="Syncfusion WinForms 전문가"
                )
            
            # 유효성 검증
            is_valid = formatter.validate_format(result)
            print(f"  ✓ Format validation: {is_valid}")
            
            if is_valid:
                print(f"  ✓ Generated {format_type} format successfully")
                print(f"  - Keys: {list(result.keys())}")
                if "metadata" in result:
                    print(f"  - Metadata: {result['metadata']}")
            else:
                print(f"  ✗ Format validation failed")
                
        except Exception as e:
            print(f"  ✗ {format_type} formatter test failed: {e}")


def test_validator():
    """검증기 모듈 테스트"""
    print("\n=== Testing Validator ===")
    
    # 테스트 데이터
    test_data = {
        "sharegpt": [
            {
                "conversations": [
                    {"from": "system", "value": "테스트 시스템"},
                    {"from": "human", "value": "테스트 질문"},
                    {"from": "gpt", "value": "테스트 응답"}
                ]
            }
        ],
        "alpaca": [
            {
                "instruction": "테스트 지시문",
                "output": "테스트 응답",
                "input": "테스트 입력"
            }
        ],
        "openai": [
            {
                "messages": [
                    {"role": "system", "content": "테스트 시스템"},
                    {"role": "user", "content": "테스트 질문"},
                    {"role": "assistant", "content": "테스트 응답"}
                ]
            }
        ]
    }
    
    validator = UnslothValidator()
    
    # 포맷별 검증
    for format_type, data in test_data.items():
        print(f"\nTesting {format_type} validation...")
        
        try:
            result = validator.validate_dataset_format(format_type, data)
            print(f"  ✓ Validation result: {result.is_valid}")
            print(f"  - Issues: {len(result.issues)}")
            print(f"  - Warnings: {len(result.warnings)}")
            print(f"  - Recommendations: {len(result.recommendations)}")
            
            if result.issues:
                print(f"  - Issue examples: {result.issues[:2]}")
                
        except Exception as e:
            print(f"  ✗ {format_type} validation test failed: {e}")
    
    # 전체 호환성 검증
    print(f"\nTesting overall compatibility...")
    try:
        results = validator.validate_unsloth_compatibility(test_data)
        summary = validator.get_validation_summary(results)
        
        print(f"  ✓ Overall validation completed")
        print(f"  - Total formats: {summary['total_formats']}")
        print(f"  - Valid formats: {summary['valid_formats']}")
        print(f"  - Invalid formats: {summary['invalid_formats']}")
        print(f"  - Total issues: {summary['total_issues']}")
        
    except Exception as e:
        print(f"  ✗ Overall validation test failed: {e}")


def test_statistics():
    """통계 생성기 모듈 테스트"""
    print("\n=== Testing Statistics Generator ===")
    
    # 테스트 데이터
    test_datasets = {
        "sharegpt": [
            {
                "conversations": [
                    {"from": "system", "value": "시스템 프롬프트"},
                    {"from": "human", "value": "사용자 질문입니다."},
                    {"from": "gpt", "value": "AI 응답 내용입니다."}
                ]
            }
        ],
        "alpaca": [
            {
                "instruction": "지시문 내용",
                "output": "응답 내용",
                "input": "입력 내용"
            }
        ],
        "openai": [
            {
                "messages": [
                    {"role": "system", "content": "시스템 메시지"},
                    {"role": "user", "content": "사용자 메시지"},
                    {"role": "assistant", "content": "어시스턴트 메시지"}
                ]
            }
        ]
    }
    
    stats_generator = StatisticsGenerator()
    
    try:
        # 데이터셋 통계 생성
        dataset_stats = stats_generator.generate_dataset_statistics(test_datasets)
        
        print(f"  ✓ Dataset statistics generated")
        print(f"  - Total samples: {dataset_stats.total_samples}")
        print(f"  - Quality metrics: {dataset_stats.quality_metrics}")
        print(f"  - Diversity metrics: {dataset_stats.diversity_metrics}")
        
        # 포맷별 통계
        for format_type, format_stats in dataset_stats.format_statistics.items():
            print(f"  - {format_type}: {format_stats.sample_count} samples, "
                  f"quality: {format_stats.quality_score:.2f}")
        
    except Exception as e:
        print(f"  ✗ Statistics generation test failed: {e}")


def test_utils():
    """유틸리티 모듈 테스트"""
    print("\n=== Testing Utils ===")
    
    try:
        # 로깅 테스트
        logger = setup_logging("INFO")
        print("  ✓ Logging setup completed")
        
        # 텍스트 정규화 테스트
        test_text = "  여러   공백과\n특수문자!@#   포함된  텍스트  "
        normalized = normalize_text(test_text)
        print(f"  ✓ Text normalization: '{test_text}' -> '{normalized}'")
        
        # 중복 제거 테스트
        test_samples = [
            {"instruction": "테스트 1", "response": "응답 1"},
            {"instruction": "테스트 2", "response": "응답 2"},
            {"instruction": "테스트 1", "response": "응답 1"},  # 중복
        ]
        unique_samples = remove_duplicates(test_samples)
        print(f"  ✓ Duplicate removal: {len(test_samples)} -> {len(unique_samples)}")
        
        # 데이터 분할 테스트
        train_data, val_data = split_train_test(unique_samples, 0.8)
        print(f"  ✓ Train/test split: {len(train_data)} train, {len(val_data)} validation")
        
    except Exception as e:
        print(f"  ✗ Utils test failed: {e}")


def test_generator():
    """데이터셋 생성기 통합 테스트"""
    print("\n=== Testing Dataset Generator ===")
    
    # 테스트 데이터
    test_samples = [
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
            "response": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용",
            "source": "documentation",
            "quality_score": 0.9
        },
        {
            "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
            "response": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가",
            "source": "tutorial",
            "quality_score": 0.8
        },
        {
            "instruction": "PDF 뷰어 컴포넌트 사용법",
            "response": "PDF 뷰어 컴포넌트 사용법:\n1. PDF 뷰어 컨트롤 추가\n2. PDF 파일 로드\n3. 페이지 네비게이션\n4. 확대/축소\n5. 인쇄 기능",
            "source": "documentation",
            "quality_score": 0.85
        }
    ]
    
    # 임시 디렉토리 생성
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # 데이터셋 생성기 설정
            config = DatasetConfig(
                target_count=100,
                max_seq_length=8192,
                train_test_split=0.9,
                formats=["sharegpt", "alpaca", "openai"],
                min_tokens=50,
                max_tokens=8192,
                eos_token="</s>",
                remove_duplicates=True,
                quality_threshold=0.7,
                batch_size=12,
                max_workers=8,
                output_dir=temp_dir
            )
            
            generator = UnslothDatasetGenerator(config)
            
            # 데이터셋 생성
            print("  Generating dataset...")
            result = generator.generate_from_samples(test_samples, "test_dataset")
            
            print(f"  ✓ Dataset generation completed")
            print(f"  - Total samples: {result.metadata['total_samples']}")
            print(f"  - Formats: {result.metadata['formats']}")
            
            # 포맷별 결과 확인
            for fmt in config.formats:
                train_count = result.get_train_count(fmt)
                val_count = result.get_validation_count(fmt)
                print(f"  - {fmt}: {train_count} train, {val_count} validation")
            
            # 검증 결과 확인
            validation_results = result.validation_results
            print(f"  - Validation results: {len(validation_results)} formats validated")
            
            for fmt, val_result in validation_results.items():
                is_valid = val_result.get("is_valid", False)
                issues = len(val_result.get("issues", []))
                print(f"    {fmt}: {'✓' if is_valid else '✗'} (issues: {issues})")
            
            # 통계 확인
            statistics = result.statistics
            print(f"  - Statistics generated: {len(statistics)} metrics")
            
            # 파일 저장 테스트
            print("  Testing file saving...")
            saved_paths = generator.save_datasets(result, "test_dataset")
            
            print(f"  ✓ Files saved successfully")
            for file_type, path in saved_paths.items():
                if Path(path).exists():
                    print(f"    {file_type}: ✓")
                else:
                    print(f"    {file_type}: ✗")
            
        except Exception as e:
            print(f"  ✗ Dataset generator test failed: {e}")


def test_integration():
    """통합 테스트"""
    print("\n=== Integration Test ===")
    
    # 임시 디렉토리 생성
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # 데이터셋 생성기 설정
            config = DatasetConfig(
                target_count=50,
                max_seq_length=8192,
                train_test_split=0.9,
                formats=["sharegpt", "alpaca", "openai"],
                min_tokens=50,
                max_tokens=8192,
                eos_token="</s>",
                remove_duplicates=True,
                quality_threshold=0.7,
                batch_size=12,
                max_workers=8,
                output_dir=temp_dir
            )
            
            generator = UnslothDatasetGenerator(config)
            validator = UnslothValidator()
            stats_generator = StatisticsGenerator()
            
            # 테스트 데이터 생성
            test_samples = []
            for i in range(10):
                test_samples.append({
                    "instruction": f"테스트 지시문 {i+1}",
                    "response": f"테스트 응답 {i+1}",
                    "source": "test",
                    "quality_score": 0.8 + (i % 3) * 0.1
                })
            
            # 데이터셋 생성
            result = generator.generate_from_samples(test_samples, "integration_test")
            
            # 검증 수행
            validation_results = validator.validate_unsloth_compatibility(
                {fmt: result.train_data.get(fmt, []) + result.validation_data.get(fmt, []) 
                 for fmt in config.formats}
            )
            
            # 통계 생성
            datasets = {
                fmt: result.train_data.get(fmt, []) + result.validation_data.get(fmt, [])
                for fmt in config.formats
            }
            stats = stats_generator.generate_dataset_statistics(datasets)
            
            # 결과 확인
            print(f"  ✓ Integration test completed")
            print(f"  - Dataset generated: {result.metadata['total_samples']} samples")
            print(f"  - Validation: {len([r for r in validation_results.values() if r.is_valid])}/{len(validation_results)} valid")
            print(f"  - Statistics: {len(stats.format_statistics)} formats analyzed")
            
            # 파일 확인
            saved_paths = generator.save_datasets(result, "integration_test")
            existing_files = sum(1 for path in saved_paths.values() if Path(path).exists())
            print(f"  - Files saved: {existing_files}/{len(saved_paths)}")
            
        except Exception as e:
            print(f"  ✗ Integration test failed: {e}")
            import traceback
            traceback.print_exc()


def main():
    """메인 테스트 함수"""
    print("Unsloth Dataset Generator Integration Test")
    print("=" * 50)
    
    # 개별 모듈 테스트
    test_formatters()
    test_validator()
    test_statistics()
    test_utils()
    test_generator()
    test_integration()
    
    print("\n" + "=" * 50)
    print("Integration Test Completed")


if __name__ == "__main__":
    main()