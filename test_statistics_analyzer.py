#!/usr/bin/env python3
"""
StatisticsAnalyzer 단위 테스트
"""

import unittest
import tempfile
import json
from pathlib import Path

from quality_validator.statistics_analyzer import (
    StatisticsAnalyzer, StatisticsAnalyzerConfig, StatisticsResult,
    create_default_statistics_analyzer
)


class TestStatisticsAnalyzer(unittest.TestCase):
    """StatisticsAnalyzer 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.config = StatisticsAnalyzerConfig(
            enable_basic_statistics=True,
            enable_content_analysis=True,
            enable_quality_analysis=True,
            enable_diversity_analysis=True,
            enable_balance_analysis=True,
            min_word_frequency=2,
            max_vocabulary_size=10000,
            topic_analysis_depth=50,
            log_level="ERROR"  # 테스트 중 로그 최소화
        )
        self.statistics_analyzer = StatisticsAnalyzer(self.config)
    
    def test_initialization(self):
        """초기화 테스트"""
        self.assertIsNotNone(self.statistics_analyzer)
        self.assertTrue(self.statistics_analyzer.config.enable_basic_statistics)
        self.assertTrue(self.statistics_analyzer.config.enable_content_analysis)
        self.assertTrue(self.statistics_analyzer.config.enable_quality_analysis)
        self.assertTrue(self.statistics_analyzer.config.enable_diversity_analysis)
        self.assertTrue(self.statistics_analyzer.config.enable_balance_analysis)
    
    def test_empty_dataset_analysis(self):
        """빈 데이터셋 분석 테스트"""
        empty_datasets = {}
        
        result = self.statistics_analyzer.analyze_dataset(empty_datasets)
        
        self.assertIsInstance(result, StatisticsResult)
        self.assertEqual(result.total_samples, 0)
        self.assertFalse(result.validation_passed)
        self.assertIn("No samples found", result.validation_issues[0])
    
    def test_basic_statistics_analysis(self):
        """기본 통계 분석 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                        {"from": "gpt", "value": "Chart 컴포넌트는 다음과 같이 사용합니다."}
                    ]
                }
            ],
            "alpaca": [
                {
                    "instruction": "Gauge 컴포넌트 사용법을 설명해주세요.",
                    "input": "초보자도 이해할 수 있도록 설명해주세요.",
                    "output": "Gauge 컴포넌트는 다음과 같이 사용합니다."
                }
            ]
        }
        
        result = self.statistics_analyzer.analyze_dataset(test_datasets)
        
        self.assertEqual(result.total_samples, 3)
        self.assertIsInstance(result.basic_statistics, dict)
        
        basic_stats = result.basic_statistics
        self.assertEqual(basic_stats["total_formats"], 2)
        self.assertEqual(basic_stats["total_conversations"], 3)
        self.assertGreater(basic_stats["total_words"], 0)
        self.assertGreater(basic_stats["total_characters"], 0)
        self.assertGreater(basic_stats["average_words_per_sample"], 0)
        
        # 포맷별 분포 확인
        self.assertIn("sharegpt", basic_stats["format_distribution"])
        self.assertIn("alpaca", basic_stats["format_distribution"])
        self.assertEqual(basic_stats["format_distribution"]["sharegpt"]["sample_count"], 2)
        self.assertEqual(basic_stats["format_distribution"]["alpaca"]["sample_count"], 1)
    
    def test_content_statistics_analysis(self):
        """콘텐츠 통계 분석 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다:\n\n1. 프로젝트에 참조 추가\n2. 컨트롤 배치\n\n예제 코드:\n```csharp\nSfDataGrid dataGrid = new SfDataGrid();\n```"}
                    ]
                }
            ]
        }
        
        result = self.statistics_analyzer.analyze_dataset(test_datasets)
        
        content_stats = result.content_statistics
        
        # 어휘 통계 확인
        self.assertIn("vocabulary", content_stats)
        vocab_stats = content_stats["vocabulary"]
        self.assertGreater(vocab_stats["unique_words"], 0)
        self.assertGreater(vocab_stats["total_words"], 0)
        self.assertGreaterEqual(vocab_stats["vocabulary_richness"], 0)
        self.assertLessEqual(vocab_stats["vocabulary_richness"], 1)
        
        # 문장 통계 확인
        self.assertIn("sentence_statistics", content_stats)
        sentence_stats = content_stats["sentence_statistics"]
        self.assertGreater(sentence_stats["total_sentences"], 0)
        self.assertGreater(sentence_stats["average_sentence_length"], 0)
        
        # 코드 통계 확인
        self.assertIn("code_statistics", content_stats)
        code_stats = content_stats["code_statistics"]
        self.assertGreaterEqual(code_stats["code_blocks_count"], 1)  # 예제에 코드 블록이 있음
        
        # 기술적 콘텐츠 확인
        self.assertIn("technical_content", content_stats)
        tech_stats = content_stats["technical_content"]
        self.assertIn("component_mentions", tech_stats)
        self.assertGreater(tech_stats["component_mentions"].get("DataGrid", 0), 0)
    
    def test_quality_statistics_analysis(self):
        """품질 통계 분석 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트 사용법을 단계별로 설명드리겠습니다. 예제 코드도 포함되어 있습니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "이 프로그램이 안됩니다."},
                        {"from": "gpt", "value": "문제를 해결하는 방법을 알려드리겠습니다."}
                    ]
                }
            ]
        }
        
        result = self.statistics_analyzer.analyze_dataset(test_datasets)
        
        quality_stats = result.quality_statistics
        
        # 품질 지표 확인
        self.assertIn("quality_indicators", quality_stats)
        quality_indicators = quality_stats["quality_indicators"]
        self.assertGreaterEqual(quality_indicators["positive_indicators"], 0)
        self.assertGreaterEqual(quality_indicators["negative_indicators"], 0)
        self.assertGreaterEqual(quality_indicators["quality_ratio"], 0)
        self.assertLessEqual(quality_indicators["quality_ratio"], 1)
        
        # 완성도 메트릭 확인
        self.assertIn("completeness_metrics", quality_stats)
        completeness = quality_stats["completeness_metrics"]
        self.assertGreater(completeness["average_text_length"], 0)
        self.assertGreaterEqual(completeness["short_texts_ratio"], 0)
        self.assertLessEqual(completeness["short_texts_ratio"], 1)
        
        # 일관성 메트릭 확인
        self.assertIn("coherence_metrics", quality_stats)
        coherence = quality_stats["coherence_metrics"]
        self.assertGreaterEqual(coherence["average_coherence"], 0)
        self.assertLessEqual(coherence["average_coherence"], 1)
        
        # 기술적 정확성 확인
        self.assertIn("technical_accuracy", quality_stats)
        tech_accuracy = quality_stats["technical_accuracy"]
        self.assertGreaterEqual(tech_accuracy["technical_terms_count"], 0)
        self.assertGreaterEqual(tech_accuracy["technical_density"], 0)
    
    def test_diversity_analysis(self):
        """다양성 분석 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트는 데이터 바인딩을 통해 사용합니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "Chart 컴포넌트로 그래프를 만드는 방법을 알려주세요."},
                        {"from": "gpt", "value": "Chart 컴포넌트는 다양한 차트 타입을 지원합니다."}
                    ]
                }
            ],
            "alpaca": [
                {
                    "instruction": "Gauge 컴포넌트의 스타일링 방법을 설명해주세요.",
                    "output": "Gauge 컴포넌트는 테마를 통해 스타일을 변경할 수 있습니다."
                }
            ]
        }
        
        result = self.statistics_analyzer.analyze_dataset(test_datasets)
        
        # 다양성 메트릭 확인
        self.assertGreaterEqual(result.vocabulary_diversity, 0)
        self.assertLessEqual(result.vocabulary_diversity, 1)
        self.assertGreaterEqual(result.topic_diversity, 0)
        self.assertLessEqual(result.topic_diversity, 1)
        self.assertGreaterEqual(result.length_diversity, 0)
        
        # 다양성 통계 세부 확인
        diversity_stats = result.diversity_statistics
        self.assertIn("content_diversity", diversity_stats)
        content_diversity = diversity_stats["content_diversity"]
        self.assertIn("topic_distribution", content_diversity)
        self.assertIn("length_distribution", content_diversity)
    
    def test_balance_analysis(self):
        """균형 분석 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                        {"from": "gpt", "value": "DataGrid 컴포넌트 사용법입니다."}
                    ]
                },
                {
                    "conversations": [
                        {"from": "human", "value": "Chart 사용법을 알려주세요."},
                        {"from": "gpt", "value": "Chart 컴포넌트 사용법입니다."}
                    ]
                }
            ],
            "alpaca": [
                {
                    "instruction": "Gauge 사용법을 설명해주세요.",
                    "output": "Gauge 컴포넌트 사용법입니다."
                },
                {
                    "instruction": "TreeView 사용법을 설명해주세요.",
                    "output": "TreeView 컴포넌트 사용법입니다."
                }
            ]
        }
        
        result = self.statistics_analyzer.analyze_dataset(test_datasets)
        
        # 균형 메트릭 확인
        self.assertGreaterEqual(result.component_balance, 0)
        self.assertLessEqual(result.component_balance, 1)
        self.assertGreaterEqual(result.topic_balance, 0)
        self.assertLessEqual(result.topic_balance, 1)
        self.assertGreaterEqual(result.format_balance, 0)
        self.assertLessEqual(result.format_balance, 1)
        
        # 균형 통계 세부 확인
        balance_stats = result.balance_statistics
        self.assertIn("balance_details", balance_stats)
        balance_details = balance_stats["balance_details"]
        self.assertIn("component_distribution", balance_details)
        self.assertIn("format_distribution", balance_details)
        
        # 포맷 균형 확인 (각 포맷에 2개씩 있으므로 완벽한 균형)
        format_dist = balance_details["format_distribution"]
        self.assertEqual(format_dist["sharegpt"], 2)
        self.assertEqual(format_dist["alpaca"], 2)
    
    def test_dataset_validation(self):
        """데이터셋 검증 테스트"""
        # 작은 데이터셋 (경고 발생)
        small_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "안녕하세요"},
                        {"from": "gpt", "value": "안녕하세요"}
                    ]
                }
            ]
        }
        
        result = self.statistics_analyzer.analyze_dataset(small_datasets)
        
        # 검증 경고가 있어야 함
        self.assertGreater(len(result.validation_warnings), 0)
        
        # 매우 작은 데이터셋 (이슈 발생)
        tiny_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "hi"},
                        {"from": "gpt", "value": "hi"}
                    ]
                }
            ] * 5  # 5개 샘플
        }
        
        result = self.statistics_analyzer.analyze_dataset(tiny_datasets)
        
        # 검증 경고나 이슈가 있어야 함
        self.assertTrue(len(result.validation_warnings) > 0 or len(result.validation_issues) > 0)
    
    def test_conversation_pairs_extraction(self):
        """대화 쌍 추출 테스트"""
        # ShareGPT 형식
        sharegpt_item = {
            "conversations": [
                {"from": "human", "value": "질문1"},
                {"from": "gpt", "value": "답변1"},
                {"from": "human", "value": "질문2"},
                {"from": "gpt", "value": "답변2"}
            ]
        }
        
        pairs = self.statistics_analyzer._extract_conversation_pairs(sharegpt_item, "sharegpt")
        self.assertEqual(len(pairs), 2)
        self.assertEqual(pairs[0], ("질문1", "답변1"))
        self.assertEqual(pairs[1], ("질문2", "답변2"))
        
        # Alpaca 형식
        alpaca_item = {
            "instruction": "질문",
            "input": "추가 입력",
            "output": "답변"
        }
        
        pairs = self.statistics_analyzer._extract_conversation_pairs(alpaca_item, "alpaca")
        self.assertEqual(len(pairs), 1)
        self.assertEqual(pairs[0], ("질문 추가 입력", "답변"))
        
        # OpenAI 형식
        openai_item = {
            "messages": [
                {"role": "user", "content": "질문1"},
                {"role": "assistant", "content": "답변1"},
                {"role": "user", "content": "질문2"},
                {"role": "assistant", "content": "답변2"}
            ]
        }
        
        pairs = self.statistics_analyzer._extract_conversation_pairs(openai_item, "openai")
        self.assertEqual(len(pairs), 2)
        self.assertEqual(pairs[0], ("질문1", "답변1"))
        self.assertEqual(pairs[1], ("질문2", "답변2"))
    
    def test_text_content_extraction(self):
        """텍스트 콘텐츠 추출 테스트"""
        # ShareGPT 형식
        sharegpt_item = {
            "conversations": [
                {"from": "human", "value": "안녕하세요"},
                {"from": "gpt", "value": "안녕하세요. 도움이 필요하시나요?"}
            ]
        }
        
        text = self.statistics_analyzer._extract_text_content(sharegpt_item, "sharegpt")
        self.assertIn("안녕하세요", text)
        self.assertIn("도움이 필요하시나요", text)
        
        # Alpaca 형식
        alpaca_item = {
            "instruction": "질문입니다",
            "input": "추가 정보",
            "output": "답변입니다"
        }
        
        text = self.statistics_analyzer._extract_text_content(alpaca_item, "alpaca")
        self.assertIn("질문입니다", text)
        self.assertIn("추가 정보", text)
        self.assertIn("답변입니다", text)
        
        # OpenAI 형식
        openai_item = {
            "messages": [
                {"role": "user", "content": "사용자 메시지"},
                {"role": "assistant", "content": "어시스턴트 응답"}
            ]
        }
        
        text = self.statistics_analyzer._extract_text_content(openai_item, "openai")
        self.assertIn("사용자 메시지", text)
        self.assertIn("어시스턴트 응답", text)
    
    def test_mathematical_calculations(self):
        """수학적 계산 테스트"""
        # 표준편차 계산
        values = [1.0, 2.0, 3.0, 4.0, 5.0]
        std = self.statistics_analyzer._calculate_std(values)
        expected_std = (((1-3)**2 + (2-3)**2 + (3-3)**2 + (4-3)**2 + (5-3)**2) / 5) ** 0.5
        self.assertAlmostEqual(std, expected_std, places=5)
        
        # 분산 계산
        variance = self.statistics_analyzer._calculate_variance(values)
        expected_variance = ((1-3)**2 + (2-3)**2 + (3-3)**2 + (4-3)**2 + (5-3)**2) / 5
        self.assertAlmostEqual(variance, expected_variance, places=5)
        
        # 빈 리스트 처리
        empty_std = self.statistics_analyzer._calculate_std([])
        empty_variance = self.statistics_analyzer._calculate_variance([])
        self.assertEqual(empty_std, 0.0)
        self.assertEqual(empty_variance, 0.0)
    
    def test_save_statistics_report(self):
        """통계 리포트 저장 테스트"""
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "테스트 질문"},
                        {"from": "gpt", "value": "테스트 답변"}
                    ]
                }
            ]
        }
        
        result = self.statistics_analyzer.analyze_dataset(test_datasets)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "statistics_report.json"
            
            success = self.statistics_analyzer.save_statistics_report(result, str(report_path))
            
            self.assertTrue(success)
            self.assertTrue(report_path.exists())
            
            # 리포트 내용 확인
            with open(report_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            
            self.assertIn("report_version", report)
            self.assertIn("generated_at", report)
            self.assertIn("configuration", report)
            self.assertIn("summary", report)
            self.assertIn("detailed_statistics", report)
            self.assertIn("validation", report)
            
            # 요약 정보 확인
            summary = report["summary"]
            self.assertEqual(summary["total_samples"], 1)
            self.assertIn("vocabulary_diversity", summary)
            self.assertIn("validation_passed", summary)
            
            # 상세 통계 확인
            detailed = report["detailed_statistics"]
            self.assertIn("basic_statistics", detailed)
            self.assertIn("content_statistics", detailed)
            self.assertIn("quality_statistics", detailed)
            self.assertIn("diversity_statistics", detailed)
            self.assertIn("balance_statistics", detailed)
    
    def test_selective_analysis_configuration(self):
        """선택적 분석 설정 테스트"""
        # 기본 통계만 활성화
        basic_only_config = StatisticsAnalyzerConfig(
            enable_basic_statistics=True,
            enable_content_analysis=False,
            enable_quality_analysis=False,
            enable_diversity_analysis=False,
            enable_balance_analysis=False,
            log_level="ERROR"
        )
        
        basic_only_analyzer = StatisticsAnalyzer(basic_only_config)
        
        test_datasets = {
            "sharegpt": [
                {
                    "conversations": [
                        {"from": "human", "value": "테스트"},
                        {"from": "gpt", "value": "응답"}
                    ]
                }
            ]
        }
        
        result = basic_only_analyzer.analyze_dataset(test_datasets)
        
        # 기본 통계만 있어야 함
        self.assertNotEqual(result.basic_statistics, {})
        self.assertEqual(result.content_statistics, {})
        self.assertEqual(result.quality_statistics, {})
        self.assertEqual(result.diversity_statistics, {})
        self.assertEqual(result.balance_statistics, {})
        
        # 다양성 및 균형 메트릭은 기본값이어야 함
        self.assertEqual(result.vocabulary_diversity, 0.0)
        self.assertEqual(result.topic_diversity, 0.0)
        self.assertEqual(result.component_balance, 0.0)
    
    def test_create_default_statistics_analyzer(self):
        """기본 통계 분석기 생성 테스트"""
        default_analyzer = create_default_statistics_analyzer()
        
        self.assertIsNotNone(default_analyzer)
        self.assertIsInstance(default_analyzer, StatisticsAnalyzer)
        self.assertTrue(default_analyzer.config.enable_basic_statistics)
        self.assertTrue(default_analyzer.config.enable_content_analysis)
        self.assertTrue(default_analyzer.config.enable_quality_analysis)
        self.assertTrue(default_analyzer.config.enable_diversity_analysis)
        self.assertTrue(default_analyzer.config.enable_balance_analysis)
        self.assertEqual(default_analyzer.config.min_word_frequency, 2)
        self.assertEqual(default_analyzer.config.max_vocabulary_size, 10000)
        self.assertEqual(default_analyzer.config.topic_analysis_depth, 50)
        self.assertEqual(default_analyzer.config.language, "ko")


if __name__ == "__main__":
    unittest.main()