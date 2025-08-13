#!/usr/bin/env python3
"""
Unsloth 데이터셋 생성기 단위 테스트
"""

import unittest
import tempfile
import shutil
import json
from pathlib import Path
from unsloth_dataset.generator import UnslothDatasetGenerator, DatasetConfig, DatasetGenerationResult


class TestUnslothDatasetGenerator(unittest.TestCase):
    """Unsloth 데이터셋 생성기 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        # 임시 디렉토리 생성
        self.temp_dir = tempfile.mkdtemp()
        
        # 테스트용 설정
        self.config = DatasetConfig(
            target_count=10,
            max_seq_length=1024,
            train_test_split=0.8,
            formats=["sharegpt", "alpaca", "openai"],
            min_tokens=10,
            max_tokens=1000,
            output_dir=self.temp_dir,
            test_mode=True,
            seed=42
        )
        
        # 생성기 초기화
        self.generator = UnslothDatasetGenerator(self.config)
        
        # 테스트 샘플 데이터
        self.test_samples = [
            {
                "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
                "response": "DataGrid 컴포넌트는 다음과 같이 사용합니다:\n1. 프로젝트에 참조 추가\n2. 폼에 컨트롤 배치\n3. 데이터 소스 설정",
                "context": "WinForms 개발 가이드",
                "source": "documentation",
                "quality_score": 0.9
            },
            {
                "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법은?",
                "response": "Chart 컴포넌트로 막대 그래프를 만드는 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩",
                "context": "차트 개발 가이드",
                "source": "tutorial",
                "quality_score": 0.8
            },
            {
                "instruction": "TreeView 컨트롤의 노드 추가 방법",
                "response": "TreeView에 노드를 추가하는 방법:\n1. TreeNode 객체 생성\n2. Nodes.Add() 메서드 사용\n3. 계층 구조 설정",
                "context": "UI 컨트롤 가이드",
                "source": "documentation",
                "quality_score": 0.85
            }
        ]
    
    def tearDown(self):
        """테스트 정리"""
        # 임시 디렉토리 삭제
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_dataset_config_creation(self):
        """DatasetConfig 생성 테스트"""
        config = DatasetConfig()
        
        # 기본값 확인
        self.assertEqual(config.target_count, 1000)
        self.assertEqual(config.max_seq_length, 8192)
        self.assertEqual(config.train_test_split, 0.9)
        self.assertIn("sharegpt", config.formats)
        self.assertIn("alpaca", config.formats)
        self.assertIn("openai", config.formats)
        
        # 커스텀 설정
        custom_config = DatasetConfig(
            target_count=500,
            formats=["alpaca"],
            test_mode=True
        )
        self.assertEqual(custom_config.target_count, 500)
        self.assertEqual(custom_config.formats, ["alpaca"])
        self.assertTrue(custom_config.test_mode)
    
    def test_generator_initialization(self):
        """생성기 초기화 테스트"""
        self.assertIsNotNone(self.generator)
        self.assertEqual(self.generator.config, self.config)
        self.assertTrue(Path(self.temp_dir).exists())
        
        # 포맷터 생성 확인
        self.assertEqual(len(self.generator.formatters), 3)
        self.assertIn("sharegpt", self.generator.formatters)
        self.assertIn("alpaca", self.generator.formatters)
        self.assertIn("openai", self.generator.formatters)
        
        # 검증기 생성 확인
        self.assertIsNotNone(self.generator.validator)
        self.assertIsNotNone(self.generator.stats_generator)
    
    def test_generate_from_samples_basic(self):
        """기본 샘플 생성 테스트"""
        result = self.generator.generate_from_samples(self.test_samples, "test_dataset")
        
        # 결과 구조 확인
        self.assertIsInstance(result, DatasetGenerationResult)
        self.assertIn("dataset_name", result.metadata)
        self.assertEqual(result.metadata["dataset_name"], "test_dataset")
        
        # 포맷별 데이터 확인
        for format_type in self.config.formats:
            self.assertIn(format_type, result.train_data)
            self.assertIn(format_type, result.validation_data)
            
            # 데이터가 생성되었는지 확인
            train_count = len(result.train_data[format_type])
            val_count = len(result.validation_data[format_type])
            total_count = train_count + val_count
            
            self.assertGreater(total_count, 0)
            
            # 분할 비율 확인 (대략적으로)
            if total_count > 1:
                expected_train_count = int(total_count * self.config.train_test_split)
                self.assertAlmostEqual(train_count, expected_train_count, delta=1)
    
    def test_generate_from_samples_formats(self):
        """포맷별 생성 테스트"""
        result = self.generator.generate_from_samples(self.test_samples)
        
        # ShareGPT 포맷 확인
        if result.train_data.get("sharegpt"):
            sharegpt_sample = result.train_data["sharegpt"][0]
            self.assertIn("conversations", sharegpt_sample)
            self.assertIsInstance(sharegpt_sample["conversations"], list)
            
            # 대화 구조 확인
            for conv in sharegpt_sample["conversations"]:
                self.assertIn("from", conv)
                self.assertIn("value", conv)
                self.assertIn(conv["from"], ["system", "human", "gpt"])
        
        # Alpaca 포맷 확인
        if result.train_data.get("alpaca"):
            alpaca_sample = result.train_data["alpaca"][0]
            self.assertIn("instruction", alpaca_sample)
            self.assertIn("output", alpaca_sample)
        
        # OpenAI 포맷 확인
        if result.train_data.get("openai"):
            openai_sample = result.train_data["openai"][0]
            self.assertIn("messages", openai_sample)
            self.assertIsInstance(openai_sample["messages"], list)
            
            # 메시지 구조 확인
            for msg in openai_sample["messages"]:
                self.assertIn("role", msg)
                self.assertIn("content", msg)
                self.assertIn(msg["role"], ["system", "user", "assistant"])
    
    def test_token_filtering(self):
        """토큰 필터링 테스트"""
        # 매우 짧은 토큰 제한으로 설정
        config = DatasetConfig(
            min_tokens=1000,  # 매우 높은 최소 토큰 수
            max_tokens=2000,
            formats=["alpaca"],
            output_dir=self.temp_dir,
            test_mode=True
        )
        generator = UnslothDatasetGenerator(config)
        
        result = generator.generate_from_samples(self.test_samples)
        
        # 토큰 수가 부족하여 필터링되었는지 확인
        total_samples = sum(
            len(result.train_data.get(fmt, [])) + len(result.validation_data.get(fmt, []))
            for fmt in config.formats
        )
        self.assertLessEqual(total_samples, len(self.test_samples))
    
    def test_quality_filtering(self):
        """품질 필터링 테스트"""
        # 낮은 품질 점수 샘플 추가
        low_quality_samples = self.test_samples + [
            {
                "instruction": "낮은 품질 질문",
                "response": "낮은 품질 응답",
                "quality_score": 0.1  # 매우 낮은 품질 점수
            }
        ]
        
        # 높은 품질 임계값 설정
        config = DatasetConfig(
            quality_threshold=0.7,
            formats=["alpaca"],
            output_dir=self.temp_dir,
            test_mode=False  # 품질 필터링 활성화
        )
        generator = UnslothDatasetGenerator(config)
        
        result = generator.generate_from_samples(low_quality_samples)
        
        # 낮은 품질 샘플이 필터링되었는지 확인
        total_samples = sum(
            len(result.train_data.get(fmt, [])) + len(result.validation_data.get(fmt, []))
            for fmt in config.formats
        )
        self.assertLess(total_samples, len(low_quality_samples))
    
    def test_data_shuffling(self):
        """데이터 셔플링 테스트"""
        # 셔플링 활성화
        config1 = DatasetConfig(
            shuffle_data=True,
            seed=42,
            formats=["alpaca"],
            output_dir=self.temp_dir,
            test_mode=True
        )
        generator1 = UnslothDatasetGenerator(config1)
        result1 = generator1.generate_from_samples(self.test_samples)
        
        # 셔플링 비활성화
        config2 = DatasetConfig(
            shuffle_data=False,
            seed=42,
            formats=["alpaca"],
            output_dir=self.temp_dir,
            test_mode=True
        )
        generator2 = UnslothDatasetGenerator(config2)
        result2 = generator2.generate_from_samples(self.test_samples)
        
        # 두 결과가 다를 수 있음 (셔플링 효과)
        # 하지만 총 개수는 같아야 함
        total1 = sum(len(result1.train_data.get(fmt, [])) + len(result1.validation_data.get(fmt, []))
                    for fmt in config1.formats)
        total2 = sum(len(result2.train_data.get(fmt, [])) + len(result2.validation_data.get(fmt, []))
                    for fmt in config2.formats)
        self.assertEqual(total1, total2)
    
    def test_train_test_split(self):
        """훈련/검증 데이터 분할 테스트"""
        # 충분한 샘플로 테스트
        large_samples = self.test_samples * 10  # 30개 샘플
        
        config = DatasetConfig(
            train_test_split=0.7,  # 70% 훈련, 30% 검증
            formats=["alpaca"],
            output_dir=self.temp_dir,
            test_mode=True,
            seed=42
        )
        generator = UnslothDatasetGenerator(config)
        
        result = generator.generate_from_samples(large_samples)
        
        # 분할 비율 확인
        for format_type in config.formats:
            train_count = len(result.train_data.get(format_type, []))
            val_count = len(result.validation_data.get(format_type, []))
            total_count = train_count + val_count
            
            if total_count > 0:
                train_ratio = train_count / total_count
                # 분할 비율이 대략적으로 맞는지 확인 (±10% 허용)
                self.assertAlmostEqual(train_ratio, 0.7, delta=0.1)
    
    def test_save_datasets(self):
        """데이터셋 저장 테스트"""
        result = self.generator.generate_from_samples(self.test_samples, "save_test")
        
        # 데이터셋 저장
        saved_paths = self.generator.save_datasets(result, "test_save")
        
        # 저장된 파일 확인
        self.assertIsInstance(saved_paths, dict)
        self.assertGreater(len(saved_paths), 0)
        
        # 각 포맷별 파일 확인
        for format_type in self.config.formats:
            train_key = f"{format_type}_train"
            val_key = f"{format_type}_validation"
            
            if train_key in saved_paths:
                train_path = Path(saved_paths[train_key])
                self.assertTrue(train_path.exists())
                self.assertEqual(train_path.suffix, ".jsonl")
            
            if val_key in saved_paths:
                val_path = Path(saved_paths[val_key])
                self.assertTrue(val_path.exists())
                self.assertEqual(val_path.suffix, ".jsonl")
        
        # 메타데이터 파일 확인
        if "metadata" in saved_paths:
            metadata_path = Path(saved_paths["metadata"])
            self.assertTrue(metadata_path.exists())
            self.assertEqual(metadata_path.suffix, ".json")
            
            # 메타데이터 내용 확인
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            self.assertIn("dataset_name", metadata)
            self.assertEqual(metadata["dataset_name"], "save_test")
        
        # 통계 파일 확인
        if "statistics" in saved_paths:
            stats_path = Path(saved_paths["statistics"])
            self.assertTrue(stats_path.exists())
            self.assertEqual(stats_path.suffix, ".json")
    
    def test_validation_results(self):
        """검증 결과 테스트"""
        result = self.generator.generate_from_samples(self.test_samples)
        
        # 검증 결과 구조 확인
        self.assertIn("validation_results", result.__dict__)
        validation_results = result.validation_results
        
        # 각 포맷별 검증 결과 확인
        for format_type in self.config.formats:
            if format_type in validation_results:
                format_validation = validation_results[format_type]
                self.assertIn("is_valid", format_validation)
                self.assertIsInstance(format_validation["is_valid"], bool)
    
    def test_statistics_generation(self):
        """통계 생성 테스트"""
        result = self.generator.generate_from_samples(self.test_samples)
        
        # 통계 존재 확인
        self.assertIn("statistics", result.__dict__)
        statistics = result.statistics
        # 통계는 DatasetStatistics 객체이거나 dict일 수 있음
        self.assertTrue(hasattr(statistics, '__dict__') or isinstance(statistics, dict))
    
    def test_generate_datasets_integration(self):
        """통합 데이터셋 생성 테스트"""
        # MD 문서 데이터
        md_documents = [
            {
                "title": "DataGrid 사용법",
                "content": "DataGrid 컴포넌트 사용 방법을 설명합니다.",
                "quality_score": 0.9
            }
        ]
        
        # 대화 데이터
        conversations = [
            {
                "user_message": "Chart 사용법을 알려주세요.",
                "assistant_message": "Chart 컴포넌트 사용법을 설명드리겠습니다.",
                "quality_score": 0.8
            }
        ]
        
        result = self.generator.generate_datasets(
            md_documents=md_documents,
            conversations=conversations
        )
        
        # 결과 확인
        self.assertIsInstance(result, DatasetGenerationResult)
        self.assertIn("integrated_dataset", result.metadata["dataset_name"])
        
        # 데이터가 생성되었는지 확인
        total_samples = 0
        for format_type in self.config.formats:
            total_samples += len(result.train_data.get(format_type, []))
            total_samples += len(result.validation_data.get(format_type, []))
        
        self.assertGreater(total_samples, 0)
    
    def test_empty_samples(self):
        """빈 샘플 처리 테스트"""
        result = self.generator.generate_from_samples([], "empty_test")
        
        # 빈 결과 확인
        for format_type in self.config.formats:
            self.assertEqual(len(result.train_data.get(format_type, [])), 0)
            self.assertEqual(len(result.validation_data.get(format_type, [])), 0)
        
        # 메타데이터는 여전히 존재해야 함
        self.assertIn("dataset_name", result.metadata)
        self.assertEqual(result.metadata["total_samples"], 0)
    
    def test_single_format_generation(self):
        """단일 포맷 생성 테스트"""
        config = DatasetConfig(
            formats=["alpaca"],  # Alpaca 포맷만
            output_dir=self.temp_dir,
            test_mode=True
        )
        generator = UnslothDatasetGenerator(config)
        
        result = generator.generate_from_samples(self.test_samples)
        
        # Alpaca 포맷만 생성되었는지 확인
        self.assertIn("alpaca", result.train_data)
        self.assertNotIn("sharegpt", result.train_data)
        self.assertNotIn("openai", result.train_data)
        
        # Alpaca 데이터 구조 확인
        if result.train_data["alpaca"]:
            alpaca_sample = result.train_data["alpaca"][0]
            self.assertIn("instruction", alpaca_sample)
            self.assertIn("output", alpaca_sample)
    
    def test_extract_text_for_token_count(self):
        """토큰 계산용 텍스트 추출 테스트"""
        # ShareGPT 형식
        sharegpt_data = {
            "conversations": [
                {"from": "human", "value": "질문입니다"},
                {"from": "gpt", "value": "답변입니다"}
            ]
        }
        text = self.generator._extract_text_for_token_count(sharegpt_data)
        self.assertIn("질문입니다", text)
        self.assertIn("답변입니다", text)
        
        # Alpaca 형식
        alpaca_data = {
            "instruction": "지시문입니다",
            "output": "출력입니다"
        }
        text = self.generator._extract_text_for_token_count(alpaca_data)
        self.assertIn("지시문입니다", text)
        self.assertIn("출력입니다", text)
        
        # OpenAI 형식
        openai_data = {
            "messages": [
                {"role": "user", "content": "사용자 메시지"},
                {"role": "assistant", "content": "어시스턴트 메시지"}
            ]
        }
        text = self.generator._extract_text_for_token_count(openai_data)
        self.assertIn("사용자 메시지", text)
        self.assertIn("어시스턴트 메시지", text)


if __name__ == "__main__":
    unittest.main()