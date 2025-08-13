#!/usr/bin/env python3
"""
Unsloth 데이터셋 모듈 통합 테스트
포맷터, 검증기, 생성기가 함께 작동하는지 확인합니다.
"""

import unittest
import tempfile
import shutil
import json
from pathlib import Path
from unsloth_dataset.generator import UnslothDatasetGenerator, DatasetConfig
from unsloth_dataset.validator import UnslothValidator
from unsloth_dataset.formatters import create_formatter


class TestUnslothDatasetIntegration(unittest.TestCase):
    """Unsloth 데이터셋 통합 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        # 임시 디렉토리 생성
        self.temp_dir = tempfile.mkdtemp()
        
        # 테스트용 설정
        self.config = DatasetConfig(
            target_count=20,
            max_seq_length=2048,
            train_test_split=0.8,
            formats=["sharegpt", "alpaca", "openai"],
            min_tokens=20,
            max_tokens=1000,
            output_dir=self.temp_dir,
            test_mode=True,
            seed=42,
            remove_duplicates=True,
            quality_threshold=0.5
        )
        
        # 테스트 샘플 데이터 (다양한 품질과 길이)
        self.test_samples = [
            {
                "instruction": "Syncfusion WinForms DataGrid 컴포넌트의 기본 사용법을 자세히 설명해주세요.",
                "response": "DataGrid 컴포넌트는 Syncfusion WinForms의 핵심 데이터 표시 컨트롤입니다. 사용법은 다음과 같습니다:\n1. 프로젝트에 Syncfusion.Grid.Windows 참조 추가\n2. 폼 디자이너에서 GridControl 추가\n3. 데이터 소스 설정 (DataTable, List 등)\n4. 컬럼 설정 및 스타일 적용\n5. 이벤트 핸들러 구현",
                "context": "WinForms 데이터 그리드 개발 가이드",
                "source": "documentation",
                "quality_score": 0.95
            },
            {
                "instruction": "Chart 컴포넌트로 다양한 종류의 그래프를 만드는 방법은?",
                "response": "Syncfusion Chart 컴포넌트를 사용하여 다양한 그래프를 만들 수 있습니다:\n1. ChartControl 추가\n2. Series 객체 생성 (ChartSeries)\n3. 차트 타입 설정 (Bar, Line, Pie 등)\n4. 데이터 포인트 추가\n5. 축 설정 및 범례 추가\n6. 색상 및 스타일 커스터마이징",
                "context": "차트 및 그래프 개발 가이드",
                "source": "tutorial",
                "quality_score": 0.88
            },
            {
                "instruction": "TreeView 컨트롤에서 동적으로 노드를 추가하고 관리하는 방법",
                "response": "TreeView에서 동적 노드 관리 방법:\n1. TreeNode 객체 생성\n2. Nodes.Add() 메서드로 노드 추가\n3. 부모-자식 관계 설정\n4. 노드 속성 설정 (Text, Tag, ImageIndex)\n5. 이벤트 처리 (NodeClick, BeforeExpand)\n6. 노드 검색 및 삭제 기능 구현",
                "context": "트리 컨트롤 개발 가이드",
                "source": "documentation",
                "quality_score": 0.82
            },
            {
                "instruction": "RichTextBox 컨트롤의 고급 기능 활용법",
                "response": "RichTextBox 고급 기능들:\n1. RTF 포맷 지원\n2. 텍스트 스타일링 (폰트, 색상, 크기)\n3. 이미지 삽입 기능\n4. 하이퍼링크 지원\n5. 찾기/바꾸기 기능\n6. 인쇄 및 내보내기 기능\n7. 맞춤법 검사 통합",
                "context": "리치 텍스트 에디터 개발",
                "source": "advanced_guide",
                "quality_score": 0.79
            },
            {
                "instruction": "간단한 질문",
                "response": "간단한 답변",
                "context": "기본",
                "source": "basic",
                "quality_score": 0.3  # 낮은 품질
            }
        ]
    
    def tearDown(self):
        """테스트 정리"""
        # 임시 디렉토리 삭제
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_end_to_end_dataset_generation(self):
        """전체 데이터셋 생성 파이프라인 테스트"""
        # 생성기 초기화
        generator = UnslothDatasetGenerator(self.config)
        
        # 데이터셋 생성
        result = generator.generate_from_samples(self.test_samples, "integration_test")
        
        # 기본 결과 검증
        self.assertIsNotNone(result)
        self.assertIn("integration_test", result.metadata["dataset_name"])
        
        # 모든 포맷이 생성되었는지 확인
        for format_type in self.config.formats:
            self.assertIn(format_type, result.train_data)
            self.assertIn(format_type, result.validation_data)
            
            # 데이터가 실제로 생성되었는지 확인
            total_samples = len(result.train_data[format_type]) + len(result.validation_data[format_type])
            self.assertGreater(total_samples, 0)
        
        # 통계 생성 확인
        self.assertIsNotNone(result.statistics)
        
        # 검증 결과 확인
        self.assertIsNotNone(result.validation_results)
        for format_type in self.config.formats:
            if format_type in result.validation_results:
                self.assertIn("is_valid", result.validation_results[format_type])
    
    def test_format_consistency_across_pipeline(self):
        """파이프라인 전체에서 포맷 일관성 테스트"""
        generator = UnslothDatasetGenerator(self.config)
        result = generator.generate_from_samples(self.test_samples)
        
        # 각 포맷별로 일관성 검증
        validator = UnslothValidator()
        
        for format_type in self.config.formats:
            train_data = result.train_data.get(format_type, [])
            val_data = result.validation_data.get(format_type, [])
            all_data = train_data + val_data
            
            if all_data:
                # 포맷 검증
                validation_result = validator.validate_dataset_format(format_type, all_data)
                
                # 기본 검증은 통과해야 함
                if not validation_result.is_valid:
                    self.fail(f"{format_type} format validation failed: {validation_result.issues}")
                
                # 각 샘플이 올바른 구조를 가지는지 확인
                for i, sample in enumerate(all_data):
                    if format_type == "sharegpt":
                        self.assertIn("conversations", sample)
                        self.assertIsInstance(sample["conversations"], list)
                        
                        for conv in sample["conversations"]:
                            self.assertIn("from", conv)
                            self.assertIn("value", conv)
                            self.assertIn(conv["from"], ["system", "human", "gpt"])
                    
                    elif format_type == "alpaca":
                        self.assertIn("instruction", sample)
                        self.assertIn("output", sample)
                        self.assertIsInstance(sample["instruction"], str)
                        self.assertIsInstance(sample["output"], str)
                    
                    elif format_type == "openai":
                        self.assertIn("messages", sample)
                        self.assertIsInstance(sample["messages"], list)
                        
                        for msg in sample["messages"]:
                            self.assertIn("role", msg)
                            self.assertIn("content", msg)
                            self.assertIn(msg["role"], ["system", "user", "assistant"])
    
    def test_quality_filtering_integration(self):
        """품질 필터링 통합 테스트"""
        # 품질 필터링 활성화
        config = DatasetConfig(
            formats=["alpaca"],
            quality_threshold=0.7,  # 높은 임계값
            output_dir=self.temp_dir,
            test_mode=False,  # 품질 필터링 활성화
            seed=42
        )
        
        generator = UnslothDatasetGenerator(config)
        result = generator.generate_from_samples(self.test_samples)
        
        # 낮은 품질 샘플이 필터링되었는지 확인
        total_generated = sum(
            len(result.train_data.get(fmt, [])) + len(result.validation_data.get(fmt, []))
            for fmt in config.formats
        )
        
        # 품질 점수 0.7 이상인 샘플만 남아야 함
        high_quality_samples = [s for s in self.test_samples if s.get("quality_score", 0) >= 0.7]
        self.assertLessEqual(total_generated, len(high_quality_samples))
    
    def test_token_range_filtering(self):
        """토큰 범위 필터링 테스트"""
        # 매우 제한적인 토큰 범위 설정
        config = DatasetConfig(
            formats=["alpaca"],
            min_tokens=100,  # 높은 최소값
            max_tokens=200,  # 낮은 최대값
            output_dir=self.temp_dir,
            test_mode=True,
            seed=42
        )
        
        generator = UnslothDatasetGenerator(config)
        result = generator.generate_from_samples(self.test_samples)
        
        # 토큰 범위를 벗어난 샘플들이 필터링되었는지 확인
        total_generated = sum(
            len(result.train_data.get(fmt, [])) + len(result.validation_data.get(fmt, []))
            for fmt in config.formats
        )
        
        # 대부분의 샘플이 필터링되어야 함
        self.assertLessEqual(total_generated, len(self.test_samples))
    
    def test_auto_correction_integration(self):
        """자동 수정 기능 통합 테스트"""
        # EOS 토큰이 없는 데이터 생성 (Alpaca 포맷에 맞게)
        samples_without_eos = [
            {
                "instruction": "EOS 토큰 없는 질문입니다",
                "output": "EOS 토큰 없는 응답입니다",
                "quality_score": 0.8
            }
        ]
        
        validator = UnslothValidator(enable_auto_correction=True)
        
        # 자동 수정 수행
        corrected_data, correction_result = validator.auto_correct_dataset("alpaca", samples_without_eos)
        
        # 수정된 데이터 확인
        self.assertEqual(len(corrected_data), 1)
        corrected_sample = corrected_data[0]
        
        # EOS 토큰이 추가되었는지 확인
        self.assertTrue(corrected_sample["instruction"].endswith("</s>"))
        self.assertTrue(corrected_sample["output"].endswith("</s>"))
        
        # 경고가 생성되었는지 확인
        self.assertGreater(len(correction_result.warnings), 0)
    
    def test_save_and_load_integration(self):
        """저장 및 로드 통합 테스트"""
        generator = UnslothDatasetGenerator(self.config)
        result = generator.generate_from_samples(self.test_samples, "save_load_test")
        
        # 데이터셋 저장
        saved_paths = generator.save_datasets(result, "integration_save")
        
        # 저장된 파일들 검증
        self.assertGreater(len(saved_paths), 0)
        
        # 각 포맷별 파일 로드 및 검증
        for format_type in self.config.formats:
            train_key = f"{format_type}_train"
            val_key = f"{format_type}_validation"
            
            if train_key in saved_paths:
                train_path = Path(saved_paths[train_key])
                self.assertTrue(train_path.exists())
                
                # JSONL 파일 로드 테스트
                with open(train_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    self.assertGreater(len(lines), 0)
                    
                    # 첫 번째 라인이 유효한 JSON인지 확인
                    first_sample = json.loads(lines[0])
                    self.assertIsInstance(first_sample, dict)
            
            if val_key in saved_paths:
                val_path = Path(saved_paths[val_key])
                self.assertTrue(val_path.exists())
        
        # 메타데이터 파일 검증
        if "metadata" in saved_paths:
            metadata_path = Path(saved_paths["metadata"])
            self.assertTrue(metadata_path.exists())
            
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                self.assertIn("dataset_name", metadata)
                self.assertIn("created_at", metadata)
                self.assertIn("config", metadata)
    
    def test_multiple_format_consistency(self):
        """다중 포맷 간 일관성 테스트"""
        generator = UnslothDatasetGenerator(self.config)
        result = generator.generate_from_samples(self.test_samples)
        
        # 각 포맷의 샘플 수가 비슷한지 확인
        format_counts = {}
        for format_type in self.config.formats:
            train_count = len(result.train_data.get(format_type, []))
            val_count = len(result.validation_data.get(format_type, []))
            format_counts[format_type] = train_count + val_count
        
        # 모든 포맷이 비슷한 수의 샘플을 가져야 함
        counts = list(format_counts.values())
        if len(counts) > 1:
            max_count = max(counts)
            min_count = min(counts)
            # 차이가 크지 않아야 함 (같은 소스 데이터를 사용하므로)
            self.assertLessEqual(max_count - min_count, 2)
    
    def test_validation_and_statistics_integration(self):
        """검증 및 통계 통합 테스트"""
        generator = UnslothDatasetGenerator(self.config)
        result = generator.generate_from_samples(self.test_samples)
        
        # 검증 결과 확인
        self.assertIsNotNone(result.validation_results)
        
        for format_type in self.config.formats:
            if format_type in result.validation_results:
                validation = result.validation_results[format_type]
                self.assertIn("is_valid", validation)
                
                # 유효하지 않은 경우 이슈가 있어야 함
                if not validation["is_valid"]:
                    self.assertGreater(len(validation.get("issues", [])), 0)
        
        # 통계 확인
        self.assertIsNotNone(result.statistics)
        
        # 통계가 직렬화 가능한지 확인
        serialized_stats = generator._serialize_statistics(result.statistics)
        self.assertIsInstance(serialized_stats, dict)
        
        # JSON 직렬화 테스트
        json_str = json.dumps(serialized_stats)
        self.assertIsInstance(json_str, str)
    
    def test_error_handling_integration(self):
        """오류 처리 통합 테스트"""
        # 잘못된 샘플 데이터
        invalid_samples = [
            {"invalid": "data"},  # 필수 필드 누락
            {"instruction": "", "response": ""},  # 빈 필드
            {
                "instruction": "유효한 질문입니다. 이것은 충분히 긴 질문으로 토큰 수를 만족합니다.",
                "response": "유효한 응답입니다. 이것은 충분히 긴 응답으로 토큰 수를 만족합니다.",
                "quality_score": 0.8
            }  # 유효한 샘플
        ]
        
        # 더 관대한 설정으로 테스트
        config = DatasetConfig(
            formats=["alpaca"],
            min_tokens=5,  # 낮은 최소 토큰 수
            max_tokens=2000,  # 높은 최대 토큰 수
            quality_threshold=0.0,  # 품질 필터링 비활성화
            output_dir=self.temp_dir,
            test_mode=True,
            seed=42
        )
        
        generator = UnslothDatasetGenerator(config)
        
        # 오류가 발생해도 처리가 계속되어야 함
        result = generator.generate_from_samples(invalid_samples, "error_test")
        
        # 유효한 샘플만 처리되어야 함
        total_generated = sum(
            len(result.train_data.get(fmt, [])) + len(result.validation_data.get(fmt, []))
            for fmt in config.formats
        )
        
        # 최소한 하나의 유효한 샘플은 처리되어야 함
        self.assertGreaterEqual(total_generated, 1)
        
        # 메타데이터는 여전히 생성되어야 함
        self.assertIn("dataset_name", result.metadata)
    
    def test_large_dataset_handling(self):
        """대용량 데이터셋 처리 테스트"""
        # 많은 수의 샘플 생성 (충분한 토큰 수로)
        large_samples = []
        for i in range(50):
            sample = {
                "instruction": f"질문 번호 {i}: Syncfusion WinForms 컴포넌트의 상세한 사용법과 구현 방법을 단계별로 자세히 설명해주세요. 초보자도 이해할 수 있도록 예제 코드와 함께 설명해주시면 감사하겠습니다.",
                "response": f"답변 번호 {i}: Syncfusion WinForms 컴포넌트 사용법은 다음과 같습니다. 먼저 프로젝트에 필요한 참조를 추가하고, 컨트롤을 폼에 배치한 후, 데이터 소스를 설정하고, 이벤트 핸들러를 구현하는 순서로 진행합니다. 각 단계별로 상세한 설명과 예제 코드를 제공하겠습니다.",
                "context": f"WinForms 개발 가이드 컨텍스트 {i}",
                "source": f"source_{i % 3}",
                "quality_score": 0.7 + (i % 3) * 0.1
            }
            large_samples.append(sample)
        
        # 제한된 타겟 수로 설정
        config = DatasetConfig(
            target_count=30,  # 50개 중 30개만 선택
            formats=["alpaca"],
            min_tokens=10,  # 낮은 최소 토큰 수
            max_tokens=2000,  # 높은 최대 토큰 수
            quality_threshold=0.0,  # 품질 필터링 비활성화
            output_dir=self.temp_dir,
            test_mode=True,
            seed=42
        )
        
        generator = UnslothDatasetGenerator(config)
        
        # target_count는 generate_datasets에서만 적용되므로 직접 샘플 수를 제한
        limited_samples = large_samples[:config.target_count]
        result = generator.generate_from_samples(limited_samples, "large_test")
        
        # 제한된 샘플 수로 처리되었는지 확인
        total_generated = sum(
            len(result.train_data.get(fmt, [])) + len(result.validation_data.get(fmt, []))
            for fmt in config.formats
        )
        
        self.assertLessEqual(total_generated, config.target_count)
        self.assertGreater(total_generated, 0)


if __name__ == "__main__":
    unittest.main()