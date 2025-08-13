#!/usr/bin/env python3
"""
DuplicateRemover 단위 테스트
"""

import unittest
import tempfile
import json
from pathlib import Path

from quality_validator.duplicate_remover import (
    DuplicateRemover, DuplicateRemoverConfig, DuplicateResult,
    create_default_duplicate_remover, SKLEARN_AVAILABLE
)


class TestDuplicateRemover(unittest.TestCase):
    """DuplicateRemover 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.config = DuplicateRemoverConfig(
            similarity_threshold=0.9,
            detection_method="fuzzy",
            enable_text_normalization=True,
            enable_hash_check=True,
            enable_semantic_similarity=False,  # 테스트에서는 비활성화
            batch_size=100,
            memory_efficient=False,  # 테스트에서는 메모리 효율 모드 비활성화
            removal_strategy="keep_first",
            log_level="ERROR"  # 테스트 중 로그 최소화
        )
        self.duplicate_remover = DuplicateRemover(self.config)
    
    def test_initialization(self):
        """초기화 테스트"""
        self.assertIsNotNone(self.duplicate_remover)
        self.assertEqual(self.duplicate_remover.config.similarity_threshold, 0.9)
        self.assertEqual(self.duplicate_remover.config.detection_method, "fuzzy")
        self.assertTrue(self.duplicate_remover.config.enable_text_normalization)
        self.assertTrue(self.duplicate_remover.config.enable_hash_check)
    
    def test_unique_content_sharegpt(self):
        """고유한 콘텐츠 테스트 (ShareGPT 형식)"""
        unique_item = {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        }
        
        result = self.duplicate_remover.check_duplicates(unique_item, "sharegpt")
        
        self.assertIsInstance(result, DuplicateResult)
        self.assertFalse(result.is_duplicate)
        self.assertEqual(result.status, "unique")
        self.assertEqual(result.similarity_score, 0.0)
        self.assertIsNone(result.duplicate_of)
    
    def test_unique_content_alpaca(self):
        """고유한 콘텐츠 테스트 (Alpaca 형식)"""
        unique_item = {
            "instruction": "Syncfusion Chart 컴포넌트 사용법을 설명해주세요.",
            "input": "초보자도 이해할 수 있도록 설명해주세요.",
            "output": "Chart 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. Chart 컨트롤 폼에 배치"
        }
        
        result = self.duplicate_remover.check_duplicates(unique_item, "alpaca")
        
        self.assertFalse(result.is_duplicate)
        self.assertEqual(result.status, "unique")
    
    def test_unique_content_openai(self):
        """고유한 콘텐츠 테스트 (OpenAI 형식)"""
        unique_item = {
            "messages": [
                {"role": "system", "content": "Syncfusion WinForms 전문가"},
                {"role": "user", "content": "DataGrid 사용법을 알려주세요."},
                {"role": "assistant", "content": "DataGrid 사용법은 다음과 같습니다..."}
            ]
        }
        
        result = self.duplicate_remover.check_duplicates(unique_item, "openai")
        
        self.assertFalse(result.is_duplicate)
        self.assertEqual(result.status, "unique")
    
    def test_exact_duplicate_detection(self):
        """정확한 중복 탐지 테스트"""
        original_item = {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        }
        
        duplicate_item = {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        }
        
        # 첫 번째 아이템 등록
        result1 = self.duplicate_remover.check_duplicates(original_item, "sharegpt")
        self.assertFalse(result1.is_duplicate)
        
        # 두 번째 아이템 (중복) 검사
        result2 = self.duplicate_remover.check_duplicates(duplicate_item, "sharegpt")
        self.assertTrue(result2.is_duplicate)
        self.assertEqual(result2.status, "exact_duplicate")
        self.assertEqual(result2.similarity_score, 1.0)
        self.assertIsNotNone(result2.duplicate_of)
    
    def test_fuzzy_duplicate_detection(self):
        """퍼지 중복 탐지 테스트"""
        original_item = {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        }
        
        fuzzy_duplicate_item = {
            "conversations": [
                {"from": "human", "value": "syncfusion datagrid 사용법을 알려주세요."},  # 대소문자 차이
                {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
            ]
        }
        
        # 첫 번째 아이템 등록
        result1 = self.duplicate_remover.check_duplicates(original_item, "sharegpt")
        self.assertFalse(result1.is_duplicate)
        
        # 두 번째 아이템 (퍼지 중복) 검사
        result2 = self.duplicate_remover.check_duplicates(fuzzy_duplicate_item, "sharegpt")
        self.assertTrue(result2.is_duplicate)
        self.assertEqual(result2.status, "fuzzy_duplicate")
        self.assertGreaterEqual(result2.similarity_score, 0.9)
        self.assertIsNotNone(result2.duplicate_of)
    
    def test_text_normalization(self):
        """텍스트 정규화 테스트"""
        test_text = "  Syncfusion   DataGrid  사용법을   알려주세요!!!  "
        normalized = self.duplicate_remover._normalize_text(test_text)
        
        expected = "syncfusion datagrid 사용법을 알려주세요"
        self.assertEqual(normalized, expected)
    
    def test_text_normalization_disabled(self):
        """텍스트 정규화 비활성화 테스트"""
        config = DuplicateRemoverConfig(enable_text_normalization=False)
        remover = DuplicateRemover(config)
        
        test_text = "  Syncfusion   DataGrid  사용법을   알려주세요!!!  "
        normalized = remover._normalize_text(test_text)
        
        # 정규화가 비활성화되면 원본 텍스트 반환
        self.assertEqual(normalized, test_text)
    
    def test_empty_content(self):
        """빈 콘텐츠 테스트"""
        empty_item = {
            "conversations": []
        }
        
        result = self.duplicate_remover.check_duplicates(empty_item, "sharegpt")
        
        self.assertFalse(result.is_duplicate)
        self.assertEqual(result.status, "no_content")
        self.assertEqual(result.similarity_score, 0.0)
    
    def test_batch_check_duplicates(self):
        """배치 중복 검사 테스트"""
        test_items = [
            {
                "conversations": [
                    {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                    {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                    {"from": "gpt", "value": "Chart 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},  # 중복
                    {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "syncfusion datagrid 사용법을 알려주세요."},  # 퍼지 중복
                    {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            }
        ]
        
        results = self.duplicate_remover.batch_check_duplicates(test_items, "sharegpt")
        
        self.assertEqual(len(results), 4)
        
        # 첫 번째와 두 번째는 고유
        self.assertFalse(results[0].is_duplicate)
        self.assertFalse(results[1].is_duplicate)
        
        # 세 번째와 네 번째는 중복
        self.assertTrue(results[2].is_duplicate)
        self.assertTrue(results[3].is_duplicate)
    
    def test_remove_duplicates_keep_first(self):
        """중복 제거 테스트 (첫 번째 유지)"""
        test_items = [
            {
                "conversations": [
                    {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                    {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                    {"from": "gpt", "value": "Chart 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},  # 중복
                    {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            }
        ]
        
        unique_items, results = self.duplicate_remover.remove_duplicates(test_items, "sharegpt")
        
        # 중복이 제거되어 2개만 남아야 함
        self.assertEqual(len(unique_items), 2)
        self.assertEqual(len(results), 3)
        
        # 결과 확인
        self.assertFalse(results[0].is_duplicate)
        self.assertFalse(results[1].is_duplicate)
        self.assertTrue(results[2].is_duplicate)
    
    def test_duplicate_statistics(self):
        """중복 통계 테스트"""
        test_results = [
            DuplicateResult(is_duplicate=False, similarity_score=0.0, status="unique"),
            DuplicateResult(is_duplicate=True, similarity_score=1.0, status="exact_duplicate", confidence_score=1.0),
            DuplicateResult(is_duplicate=True, similarity_score=0.95, status="fuzzy_duplicate", confidence_score=0.9),
            DuplicateResult(is_duplicate=False, similarity_score=0.0, status="unique")
        ]
        
        stats = self.duplicate_remover.get_duplicate_statistics(test_results)
        
        self.assertEqual(stats["total_items"], 4)
        self.assertEqual(stats["unique_items"], 2)
        self.assertEqual(stats["duplicate_items"], 2)
        self.assertEqual(stats["duplication_rate"], 0.5)
        self.assertEqual(stats["exact_duplicates"], 1)
        self.assertEqual(stats["fuzzy_duplicates"], 1)
        self.assertEqual(stats["semantic_duplicates"], 0)
        self.assertAlmostEqual(stats["average_similarity_score"], (1.0 + 0.95) / 2, places=2)
        self.assertAlmostEqual(stats["average_confidence_score"], (1.0 + 0.9) / 2, places=2)
    
    def test_save_duplicate_report(self):
        """중복 리포트 저장 테스트"""
        test_results = [
            DuplicateResult(is_duplicate=False, similarity_score=0.0, status="unique"),
            DuplicateResult(is_duplicate=True, similarity_score=1.0, status="exact_duplicate")
        ]
        
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "duplicate_report.json"
            
            success = self.duplicate_remover.save_duplicate_report(test_results, str(report_path))
            
            self.assertTrue(success)
            self.assertTrue(report_path.exists())
            
            # 리포트 내용 확인
            with open(report_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            
            self.assertIn("report_version", report)
            self.assertIn("generated_at", report)
            self.assertIn("configuration", report)
            self.assertIn("statistics", report)
            self.assertIn("detailed_results", report)
            self.assertEqual(len(report["detailed_results"]), 2)
    
    def test_clear_cache(self):
        """캐시 정리 테스트"""
        # 아이템 등록
        test_item = {
            "conversations": [
                {"from": "human", "value": "Test content"},
                {"from": "gpt", "value": "Test response"}
            ]
        }
        
        result = self.duplicate_remover.check_duplicates(test_item, "sharegpt")
        self.assertFalse(result.is_duplicate)
        
        # 캐시에 데이터가 있는지 확인
        self.assertGreater(len(self.duplicate_remover.exact_hashes), 0)
        
        # 캐시 정리
        self.duplicate_remover.clear_cache()
        
        # 캐시가 비워졌는지 확인
        self.assertEqual(len(self.duplicate_remover.exact_hashes), 0)
        self.assertEqual(len(self.duplicate_remover.fuzzy_hashes), 0)
        if hasattr(self.duplicate_remover, 'document_ids'):
            self.assertEqual(len(self.duplicate_remover.document_ids), 0)
        self.assertEqual(self.duplicate_remover.processing_stats['total_processed'], 0)
    
    def test_detection_method_exact(self):
        """정확한 중복 검사 방법 테스트"""
        config = DuplicateRemoverConfig(
            detection_method="exact",
            enable_hash_check=True,
            log_level="ERROR"
        )
        remover = DuplicateRemover(config)
        
        original_item = {
            "conversations": [
                {"from": "human", "value": "Test content"},
                {"from": "gpt", "value": "Test response"}
            ]
        }
        
        similar_item = {
            "conversations": [
                {"from": "human", "value": "test content"},  # 대소문자만 다름
                {"from": "gpt", "value": "Test response"}
            ]
        }
        
        # 첫 번째 아이템 등록
        result1 = remover.check_duplicates(original_item, "sharegpt")
        self.assertFalse(result1.is_duplicate)
        
        # 두 번째 아이템 검사 (정확한 방법에서는 중복으로 인식되지 않아야 함)
        result2 = remover.check_duplicates(similar_item, "sharegpt")
        self.assertFalse(result2.is_duplicate)  # 정확한 매칭에서는 중복이 아님
    
    def test_memory_efficient_mode(self):
        """메모리 효율 모드 테스트"""
        config = DuplicateRemoverConfig(
            memory_efficient=True,
            log_level="ERROR"
        )
        remover = DuplicateRemover(config)
        
        test_item = {
            "conversations": [
                {"from": "human", "value": "Test content"},
                {"from": "gpt", "value": "Test response"}
            ]
        }
        
        result = remover.check_duplicates(test_item, "sharegpt")
        
        self.assertFalse(result.is_duplicate)
        
        # 메모리 효율 모드에서는 text_contents가 저장되지 않아야 함
        self.assertFalse(hasattr(remover, 'text_contents') and remover.text_contents)
    
    @unittest.skipUnless(SKLEARN_AVAILABLE, "sklearn not available")
    def test_semantic_similarity(self):
        """의미적 유사도 테스트 (sklearn 사용 가능한 경우)"""
        config = DuplicateRemoverConfig(
            detection_method="semantic",
            enable_semantic_similarity=True,
            memory_efficient=False,
            log_level="ERROR"
        )
        remover = DuplicateRemover(config)
        
        original_item = {
            "conversations": [
                {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 컴포넌트 사용 방법을 설명드리겠습니다."}
            ]
        }
        
        semantic_similar_item = {
            "conversations": [
                {"from": "human", "value": "DataGrid 컴포넌트 사용 방법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 사용법을 설명드리겠습니다."}
            ]
        }
        
        # 첫 번째 아이템 등록
        result1 = remover.check_duplicates(original_item, "sharegpt")
        self.assertFalse(result1.is_duplicate)
        
        # 두 번째 아이템 검사 (의미적으로 유사)
        result2 = remover.check_duplicates(semantic_similar_item, "sharegpt")
        
        # 의미적 유사도가 높으면 중복으로 인식될 수 있음
        if result2.is_duplicate:
            self.assertEqual(result2.status, "semantic_duplicate")
            self.assertGreaterEqual(result2.similarity_score, 0.0)
    
    def test_create_default_duplicate_remover(self):
        """기본 중복 제거기 생성 테스트"""
        default_remover = create_default_duplicate_remover()
        
        self.assertIsNotNone(default_remover)
        self.assertIsInstance(default_remover, DuplicateRemover)
        self.assertEqual(default_remover.config.similarity_threshold, 0.9)
        self.assertEqual(default_remover.config.detection_method, "fuzzy")
        self.assertTrue(default_remover.config.enable_text_normalization)
        self.assertTrue(default_remover.config.enable_hash_check)
        self.assertEqual(default_remover.config.removal_strategy, "keep_first")


if __name__ == "__main__":
    unittest.main()