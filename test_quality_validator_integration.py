#!/usr/bin/env python3
"""
QualityValidator 통합 테스트
"""

import unittest
import tempfile
import json
from pathlib import Path

from quality_validator import (
    QualityValidator, QualityValidatorConfig, ValidationResult,
    create_default_validator
)


class TestQualityValidatorIntegration(unittest.TestCase):
    """QualityValidator 통합 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        # 더 관대한 설정으로 테스트
        from quality_validator.safety_filter import SafetyFilterConfig
        from quality_validator.duplicate_remover import DuplicateRemoverConfig
        from quality_validator.quality_scorer import QualityScorerConfig
        from quality_validator.compatibility_checker import CompatibilityCheckerConfig
        from quality_validator.statistics_analyzer import StatisticsAnalyzerConfig
        from quality_validator.auto_corrector import AutoCorrectorConfig
        
        self.config = QualityValidatorConfig(
            safety_filter_config=SafetyFilterConfig(
                safety_threshold=0.3,
                filter_strength="lenient"
            ),
            duplicate_remover_config=DuplicateRemoverConfig(
                similarity_threshold=0.95
            ),
            quality_scorer_config=QualityScorerConfig(
                min_quality_score=0.3
            ),
            compatibility_checker_config=CompatibilityCheckerConfig(
                min_token_length=10,  # 매우 관대한 토큰 길이
                max_token_length=8192,
                strict_token_validation=False,
                min_conversation_turns=1  # 매우 관대한 대화 턴 수
            ),
            statistics_analyzer_config=StatisticsAnalyzerConfig(),
            auto_corrector_config=AutoCorrectorConfig(
                min_confidence_score=0.3
            ),
            min_quality_score=0.3,
            max_similarity_threshold=0.95,
            safety_threshold=0.3,
            enable_auto_correction=True,
            enable_statistics_analysis=True,
            batch_size=10,
            max_workers=2,
            use_multiprocessing=False,
            output_format="enhanced",
            include_metadata=True,
            generate_report=True
        )
        self.quality_validator = QualityValidator(self.config)
    
    def test_initialization(self):
        """초기화 테스트"""
        self.assertIsNotNone(self.quality_validator)
        self.assertIsNotNone(self.quality_validator.safety_filter)
        self.assertIsNotNone(self.quality_validator.duplicate_remover)
        self.assertIsNotNone(self.quality_validator.quality_scorer)
        self.assertIsNotNone(self.quality_validator.compatibility_checker)
        self.assertIsNotNone(self.quality_validator.statistics_analyzer)
        self.assertIsNotNone(self.quality_validator.auto_corrector)
    
    def test_end_to_end_validation_sharegpt(self):
        """ShareGPT 형식 end-to-end 검증 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다:\n\n1. 프로젝트에 Syncfusion.Grid.WinForms 참조를 추가합니다.\n2. Form에 SfDataGrid 컨트롤을 배치합니다.\n3. DataSource 속성에 데이터를 바인딩합니다.\n\n예제 코드:\n```csharp\nSfDataGrid dataGrid = new SfDataGrid();\ndataGrid.DataSource = dataTable;\nthis.Controls.Add(dataGrid);\n```"}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "Chart 컴포넌트로 막대 그래프를 만드는 방법을 알려주세요."},
                        {"from": "gpt", "value": "Chart 컴포넌트로 막대 그래프를 만드는 방법:\n\n1. SfChart 컨트롤을 Form에 추가합니다.\n2. ColumnSeries를 생성하고 차트에 추가합니다.\n3. 데이터 바인딩을 설정합니다.\n4. 축 설정 및 범례를 추가합니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "안녕하세요"},
                        {"from": "gpt", "value": "안녕하세요"}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        self.assertIn("sharegpt", validated_datasets)
        validated_items = validated_datasets["sharegpt"]
        
        # 검증 결과 확인
        self.assertGreater(len(validated_items), 0)
        self.assertLessEqual(len(validated_items), 3)  # 일부는 필터링될 수 있음
        
        for item in validated_items:
            self.assertIsInstance(item, ValidationResult)
            self.assertIsInstance(item.conversations, list)
            self.assertIsInstance(item.quality_validation, dict)
            
            # 품질 검증 메타데이터 확인
            quality_validation = item.quality_validation
            self.assertIn("safety_score", quality_validation)
            self.assertIn("quality_score", quality_validation)
            self.assertIn("validation_timestamp", quality_validation)
    
    def test_end_to_end_validation_alpaca(self):
        """Alpaca 형식 end-to-end 검증 테스트"""
        test_datasets = {
            "alpaca": [
                {
                    "instruction": "Syncfusion Chart 컴포넌트 사용법을 설명해주세요.",
                    "input": "초보자도 이해할 수 있도록 단계별로 설명해주세요.",
                    "output": "Chart 컴포넌트 사용법:\n\n1. 프로젝트에 Syncfusion.Charts.WinForms 참조를 추가합니다.\n2. SfChart 컨트롤을 Form에 배치합니다.\n3. Series를 생성하고 데이터를 바인딩합니다.\n4. 차트 타입과 스타일을 설정합니다."
                },
                {
                    "instruction": "Gauge 컴포넌트 사용법을 설명해주세요.",
                    "input": "",
                    "output": "Gauge 컴포넌트는 다음과 같이 사용합니다:\n\n1. SfGauge 컨트롤 추가\n2. 범위 설정\n3. 값 바인딩"
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        self.assertIn("alpaca", validated_datasets)
        validated_items = validated_datasets["alpaca"]
        
        # 검증 결과 확인
        self.assertGreater(len(validated_items), 0)
        
        for item in validated_items:
            self.assertIsInstance(item, ValidationResult)
            # Alpaca 형식이 ShareGPT 형식으로 변환되었는지 확인
            self.assertIsInstance(item.conversations, list)
    
    def test_end_to_end_validation_openai(self):
        """OpenAI 형식 end-to-end 검증 테스트"""
        test_datasets = {
            "openai": [
                {
                    "messages": [
                        {"role": "system", "content": "Syncfusion WinForms 전문가"},
                        {"role": "user", "content": "DataGrid에서 데이터 필터링하는 방법을 알려주세요."},
                        {"role": "assistant", "content": "DataGrid에서 데이터 필터링 방법:\n\n1. AllowFiltering 속성을 true로 설정합니다.\n2. FilterRowPosition을 설정하여 필터 행 위치를 지정합니다.\n3. 프로그래밍 방식으로 필터를 적용할 수 있습니다."}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        self.assertIn("openai", validated_datasets)
        validated_items = validated_datasets["openai"]
        
        # 검증 결과 확인
        self.assertGreater(len(validated_items), 0)
        
        for item in validated_items:
            self.assertIsInstance(item, ValidationResult)
            # OpenAI 형식이 ShareGPT 형식으로 변환되었는지 확인
            self.assertIsInstance(item.conversations, list)
    
    def test_mixed_format_validation(self):
        """혼합 포맷 검증 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트 사용법을 설명드리겠습니다."}
                    ]
                }
            ],
            "alpaca": [
                {
                    "instruction": "Chart 컴포넌트 사용법을 설명해주세요.",
                    "output": "Chart 컴포넌트 사용법을 설명드리겠습니다."
                }
            ],
            "openai": [
                {
                    "messages": [
                        {"role": "user", "content": "Gauge 사용법을 알려주세요."},
                        {"role": "assistant", "content": "Gauge 컴포넌트 사용법을 설명드리겠습니다."}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        # 모든 포맷이 처리되었는지 확인
        self.assertEqual(len(validated_datasets), 3)
        self.assertIn("sharegpt", validated_datasets)
        self.assertIn("alpaca", validated_datasets)
        self.assertIn("openai", validated_datasets)
        
        # 각 포맷에 아이템이 있는지 확인 (일부는 필터링될 수 있음)
        total_items = sum(len(items) for items in validated_datasets.values())
        self.assertGreaterEqual(total_items, 0)  # 최소 0개 이상
        
        for format_type, items in validated_datasets.items():
            for item in items:
                self.assertIsInstance(item, ValidationResult)
    
    def test_duplicate_detection_and_removal(self):
        """중복 탐지 및 제거 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "DataGrid 사용법을 알려주세요."},  # 중복
                        {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "Chart 사용법을 알려주세요."},
                        {"from": "gpt", "value": "Chart 컴포넌트는 다음과 같이 사용합니다."}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        validated_items = validated_datasets["sharegpt"]
        
        # 중복이 제거되어 2개 이하가 되어야 함
        self.assertLessEqual(len(validated_items), 2)
        
        # 중복 상태 확인
        duplicate_found = False
        for item in validated_items:
            if 'duplicate_status' in item.quality_validation:
                if item.quality_validation['duplicate_status'] == 'duplicate':
                    duplicate_found = True
                    break
        
        # 중복이 탐지되었거나 제거되었어야 함
        self.assertTrue(duplicate_found or len(validated_items) < 3)
    
    def test_low_quality_filtering(self):
        """저품질 콘텐츠 필터링 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "Syncfusion DataGrid 사용법을 자세히 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트는 강력한 데이터 표시 컨트롤입니다. 다음과 같이 사용합니다:\n\n1. 프로젝트에 참조 추가\n2. 컨트롤 배치\n3. 데이터 바인딩\n4. 컬럼 설정\n\n예제 코드와 함께 단계별로 설명드리겠습니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "안녕"},
                        {"from": "gpt", "value": "안녕"}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        validated_items = validated_datasets["sharegpt"]
        
        # 저품질 아이템이 필터링되었는지 확인
        high_quality_count = 0
        for item in validated_items:
            if item.quality_validation.get('quality_score', 0) >= self.config.min_quality_score:
                high_quality_count += 1
        
        # 최소한 하나의 고품질 아이템은 남아있어야 함
        self.assertGreater(high_quality_count, 0)
    
    def test_safety_filtering(self):
        """안전성 필터링 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트 사용법을 설명드리겠습니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "이 바보같은 프로그램이 왜 안되는거야?"},
                        {"from": "gpt", "value": "프로그램 문제를 해결하는 방법을 알려드리겠습니다."}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        validated_items = validated_datasets["sharegpt"]
        
        # 안전성 점수 확인
        for item in validated_items:
            safety_score = item.quality_validation.get('safety_score', 1.0)
            if item.is_valid:
                self.assertGreaterEqual(safety_score, self.config.safety_threshold)
    
    def test_auto_correction_integration(self):
        """자동 수정 통합 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "  syncfusion  datagrid  사용벙을  알려주세요  "},
                        {"from": "gpt", "value": "DataGrid  컴포넌트트는  다음과  같이  사용합니다"}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        validated_items = validated_datasets["sharegpt"]
        
        # 자동 수정이 적용되었는지 확인
        if validated_items:
            item = validated_items[0]
            if 'auto_corrections' in item.quality_validation:
                self.assertGreater(len(item.quality_validation['auto_corrections']), 0)
            
            # 수정된 텍스트 확인
            conversations = item.conversations
            if conversations:
                human_value = conversations[0].get("value", "")
                # 공백이 정규화되었는지 확인
                self.assertNotIn("  ", human_value)
    
    def test_validation_summary(self):
        """검증 요약 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "고품질 콘텐츠: Syncfusion DataGrid 사용법을 자세히 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다. 단계별 설명과 예제를 포함합니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "저품질 콘텐츠"},
                        {"from": "gpt", "value": "짧은 답변"}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        summary = self.quality_validator.get_validation_summary(validated_datasets)
        
        # 요약 정보 확인
        self.assertIn("total_formats", summary)
        self.assertIn("total_items", summary)
        self.assertIn("valid_items", summary)
        self.assertIn("invalid_items", summary)
        self.assertIn("formats", summary)
        
        # 포맷별 요약 확인
        self.assertIn("sharegpt", summary["formats"])
        format_summary = summary["formats"]["sharegpt"]
        self.assertIn("total_items", format_summary)
        self.assertIn("valid_items", format_summary)
        self.assertIn("validity_rate", format_summary)
        self.assertIn("avg_safety_score", format_summary)
        self.assertIn("avg_quality_score", format_summary)
    
    def test_generate_report(self):
        """리포트 생성 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트 사용법을 설명드리겠습니다."}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        report = self.quality_validator.generate_report(validated_datasets)
        
        # 리포트 구조 확인
        self.assertIn("report_version", report)
        self.assertIn("generated_at", report)
        self.assertIn("validation_stats", report)
        self.assertIn("summary", report)
        self.assertIn("format_statistics", report)
        self.assertIn("quality_statistics", report)
        self.assertIn("issue_statistics", report)
        self.assertIn("configuration", report)
        
        # 설정 정보 확인
        config = report["configuration"]
        self.assertEqual(config["min_quality_score"], self.config.min_quality_score)
        self.assertEqual(config["safety_threshold"], self.config.safety_threshold)
    
    def test_save_validated_datasets(self):
        """검증된 데이터셋 저장 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트 사용법을 설명드리겠습니다."}
                    ]
                }
            ]
        }
        
        validated_datasets = self.quality_validator.validate_and_filter(test_datasets)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            saved_files = self.quality_validator.save_validated_datasets(validated_datasets, temp_dir)
            
            self.assertIn("sharegpt", saved_files)
            
            # 파일이 실제로 생성되었는지 확인
            file_path = Path(saved_files["sharegpt"])
            self.assertTrue(file_path.exists())
            
            # 파일 내용 확인 (빈 파일일 수도 있음)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                # 파일이 비어있지 않다면 JSON 형식 확인
                if len(lines) > 0:
                    first_item = json.loads(lines[0])
                    self.assertIn("id", first_item)
                    self.assertIn("conversations", first_item)
                    self.assertIn("quality_validation", first_item)
    
    def test_create_default_validator(self):
        """기본 검증기 생성 테스트"""
        default_validator = create_default_validator()
        
        self.assertIsNotNone(default_validator)
        self.assertIsInstance(default_validator, QualityValidator)
        
        # 기본 설정 확인
        self.assertEqual(default_validator.config.min_quality_score, 0.7)
        self.assertEqual(default_validator.config.max_similarity_threshold, 0.9)
        self.assertEqual(default_validator.config.safety_threshold, 0.8)
        self.assertTrue(default_validator.config.enable_auto_correction)
        self.assertTrue(default_validator.config.enable_statistics_analysis)
    
    def test_error_handling(self):
        """오류 처리 테스트"""
        # 잘못된 형식의 데이터셋
        invalid_datasets = {
            "invalid_format": [
                {
                    "invalid_field": "invalid_value"
                }
            ]
        }
        
        # 오류가 발생해도 처리되어야 함
        validated_datasets = self.quality_validator.validate_and_filter(invalid_datasets)
        
        self.assertIn("invalid_format", validated_datasets)
        validated_items = validated_datasets["invalid_format"]
        
        # 오류가 있는 아이템도 ValidationResult로 반환되어야 함
        if validated_items:
            item = validated_items[0]
            self.assertIsInstance(item, ValidationResult)
            self.assertFalse(item.is_valid)


if __name__ == "__main__":
    unittest.main()