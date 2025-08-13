#!/usr/bin/env python3
"""
QualityScorer 단위 테스트
"""

import unittest
import tempfile
import json
from pathlib import Path

from quality_validator.quality_scorer import (
    QualityScorer, QualityScorerConfig, QualityResult,
    create_default_quality_scorer, ROUGE_AVAILABLE, BERT_SCORE_AVAILABLE
)


class TestQualityScorer(unittest.TestCase):
    """QualityScorer 테스트 클래스"""
    
    def setUp(self):
        """테스트 설정"""
        self.config = QualityScorerConfig(
            min_quality_score=0.6,
            enable_rouge_score=False,  # 테스트에서는 비활성화
            enable_bert_score=False,   # 테스트에서는 비활성화
            enable_custom_metrics=True,
            technical_accuracy_weight=0.3,
            coherence_weight=0.25,
            completeness_weight=0.2,
            readability_weight=0.15,
            relevance_weight=0.1,
            log_level="ERROR"  # 테스트 중 로그 최소화
        )
        self.quality_scorer = QualityScorer(self.config)
    
    def test_initialization(self):
        """초기화 테스트"""
        self.assertIsNotNone(self.quality_scorer)
        self.assertEqual(self.quality_scorer.config.min_quality_score, 0.6)
        self.assertTrue(self.quality_scorer.config.enable_custom_metrics)
        self.assertFalse(self.quality_scorer.config.enable_rouge_score)
        self.assertFalse(self.quality_scorer.config.enable_bert_score)
    
    def test_high_quality_content_sharegpt(self):
        """고품질 콘텐츠 테스트 (ShareGPT 형식)"""
        high_quality_item = {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "Syncfusion DataGrid 컴포넌트는 다음과 같이 사용합니다:\n\n1. 프로젝트에 Syncfusion.Grid.WinForms 참조를 추가합니다.\n2. Form에 SfDataGrid 컨트롤을 배치합니다.\n3. DataSource 속성에 데이터를 바인딩합니다.\n4. Columns 컬렉션을 통해 컬럼을 구성합니다.\n\n예제 코드:\n```csharp\nSfDataGrid dataGrid = new SfDataGrid();\ndataGrid.DataSource = dataTable;\nthis.Controls.Add(dataGrid);\n```\n\n이렇게 설정하면 기본적인 DataGrid를 사용할 수 있습니다."}
            ]
        }
        
        result = self.quality_scorer.calculate_quality_score(high_quality_item, "sharegpt")
        
        self.assertIsInstance(result, QualityResult)
        self.assertGreater(result.quality_score, 0.5)  # 합리적인 점수
        self.assertIn("technical_accuracy", result.metrics)
        self.assertIn("coherence", result.metrics)
        self.assertIn("completeness", result.metrics)
        self.assertIn("readability", result.metrics)
        self.assertIn("relevance", result.metrics)
    
    def test_high_quality_content_alpaca(self):
        """고품질 콘텐츠 테스트 (Alpaca 형식)"""
        high_quality_item = {
            "instruction": "Syncfusion Chart 컴포넌트로 막대 그래프를 만드는 방법을 설명해주세요.",
            "input": "초보자도 이해할 수 있도록 단계별로 설명해주세요.",
            "output": "Syncfusion Chart 컴포넌트로 막대 그래프를 만드는 방법:\n\n1. SfChart 컨트롤을 Form에 추가합니다.\n2. ColumnSeries를 생성하고 차트에 추가합니다.\n3. 데이터 바인딩을 설정합니다.\n4. 축 설정 및 범례를 추가합니다.\n\n예제 코드:\n```csharp\nSfChart chart = new SfChart();\nColumnSeries series = new ColumnSeries();\nseries.ItemsSource = data;\nchart.Series.Add(series);\n```"
        }
        
        result = self.quality_scorer.calculate_quality_score(high_quality_item, "alpaca")
        
        self.assertGreater(result.quality_score, 0.5)
        self.assertIn("technical_accuracy", result.metrics)
    
    def test_high_quality_content_openai(self):
        """고품질 콘텐츠 테스트 (OpenAI 형식)"""
        high_quality_item = {
            "messages": [
                {"role": "system", "content": "Syncfusion WinForms 전문가"},
                {"role": "user", "content": "DataGrid에서 데이터 필터링하는 방법을 알려주세요."},
                {"role": "assistant", "content": "Syncfusion DataGrid에서 데이터 필터링 방법:\n\n1. AllowFiltering 속성을 true로 설정합니다.\n2. FilterRowPosition을 설정하여 필터 행 위치를 지정합니다.\n3. 프로그래밍 방식으로 필터를 적용할 수 있습니다.\n\n예제:\n```csharp\ndataGrid.AllowFiltering = true;\ndataGrid.FilterRowPosition = FilterRowPosition.Top;\n```"}
            ]
        }
        
        result = self.quality_scorer.calculate_quality_score(high_quality_item, "openai")
        
        self.assertGreater(result.quality_score, 0.5)
        self.assertIn("technical_accuracy", result.metrics)
    
    def test_low_quality_content(self):
        """저품질 콘텐츠 테스트"""
        low_quality_item = {
            "conversations": [
                {"from": "human", "value": "안녕하세요"},
                {"from": "gpt", "value": "안녕하세요"}
            ]
        }
        
        result = self.quality_scorer.calculate_quality_score(low_quality_item, "sharegpt")
        
        self.assertLess(result.quality_score, 0.7)  # 낮은 품질 점수
        self.assertFalse(result.is_high_quality)
        self.assertGreater(len(result.issues), 0)  # 이슈가 있어야 함
    
    def test_technical_accuracy_calculation(self):
        """기술적 정확성 계산 테스트"""
        technical_text = "Syncfusion DataGrid 컴포넌트의 Columns 속성을 사용하여 GridColumn을 추가할 수 있습니다. DataSource 속성에 데이터를 바인딩하고 Refresh 메서드를 호출합니다."
        
        score = self.quality_scorer._calculate_technical_accuracy(technical_text)
        
        self.assertGreater(score, 0.5)  # 기술적 내용이 많으므로 높은 점수
        self.assertLessEqual(score, 1.0)
    
    def test_coherence_calculation(self):
        """일관성 계산 테스트"""
        conversation_pairs = [
            ("Syncfusion DataGrid 사용법을 알려주세요.", "DataGrid 컴포넌트는 다음과 같이 사용합니다..."),
            ("Chart 컴포넌트는 어떻게 사용하나요?", "Chart 컴포넌트 사용법을 설명드리겠습니다...")
        ]
        
        score = self.quality_scorer._calculate_coherence("", conversation_pairs)
        
        self.assertGreater(score, 0.0)
        self.assertLessEqual(score, 1.0)
    
    def test_completeness_calculation(self):
        """완성도 계산 테스트"""
        complete_text = "Syncfusion DataGrid 사용법:\n\n1. 프로젝트에 참조 추가\n2. 컨트롤 배치\n3. 데이터 바인딩\n4. 컬럼 설정\n\n예제 코드도 포함되어 있습니다."
        conversation_pairs = [
            ("질문", "상세한 답변이 포함된 응답입니다.")
        ]
        
        score = self.quality_scorer._calculate_completeness(complete_text, conversation_pairs)
        
        self.assertGreater(score, 0.4)  # 완성도가 합리적이어야 함
        self.assertLessEqual(score, 1.0)
    
    def test_readability_calculation(self):
        """가독성 계산 테스트"""
        readable_text = "이것은 읽기 쉬운 텍스트입니다. 문장이 적절한 길이를 가지고 있습니다. 특수문자도 적절히 사용되었습니다."
        
        score = self.quality_scorer._calculate_readability(readable_text)
        
        self.assertGreater(score, 0.0)
        self.assertLessEqual(score, 1.0)
    
    def test_relevance_calculation(self):
        """관련성 계산 테스트"""
        relevant_text = "Syncfusion WinForms DataGrid 컴포넌트를 사용한 프로그래밍 예제입니다. 코드 구현 방법을 설명합니다."
        
        score = self.quality_scorer._calculate_relevance(relevant_text)
        
        self.assertGreater(score, 0.5)  # Syncfusion 관련 내용이므로 높은 점수
        self.assertLessEqual(score, 1.0)
    
    def test_empty_content(self):
        """빈 콘텐츠 테스트"""
        empty_item = {
            "conversations": []
        }
        
        result = self.quality_scorer.calculate_quality_score(empty_item, "sharegpt")
        
        self.assertEqual(result.quality_score, 0.0)
        self.assertFalse(result.is_high_quality)
        self.assertIn("No text content found", result.issues[0])
    
    def test_batch_calculate_quality(self):
        """배치 품질 점수 계산 테스트"""
        test_items = [
            {
                "conversations": [
                    {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                    {"from": "gpt", "value": "DataGrid 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "안녕하세요"},
                    {"from": "gpt", "value": "안녕하세요"}
                ]
            },
            {
                "conversations": [
                    {"from": "human", "value": "Chart 컴포넌트 사용법을 알려주세요."},
                    {"from": "gpt", "value": "Chart 컴포넌트는 다음과 같이 사용합니다..."}
                ]
            }
        ]
        
        results = self.quality_scorer.batch_calculate_quality(test_items, "sharegpt")
        
        self.assertEqual(len(results), 3)
        self.assertIsInstance(results[0], QualityResult)
        self.assertIsInstance(results[1], QualityResult)
        self.assertIsInstance(results[2], QualityResult)
        
        # 첫 번째와 세 번째는 기술적 내용이 있으므로 두 번째보다 높은 점수
        self.assertGreater(results[0].quality_score, results[1].quality_score)
        self.assertGreater(results[2].quality_score, results[1].quality_score)
    
    def test_quality_statistics(self):
        """품질 통계 테스트"""
        test_results = [
            QualityResult(
                quality_score=0.8,
                is_high_quality=True,
                metrics={"technical_accuracy": 0.7, "coherence": 0.8}
            ),
            QualityResult(
                quality_score=0.4,
                is_high_quality=False,
                metrics={"technical_accuracy": 0.3, "coherence": 0.5},
                issues=["Low quality content"]
            ),
            QualityResult(
                quality_score=0.7,
                is_high_quality=True,
                metrics={"technical_accuracy": 0.6, "coherence": 0.8}
            )
        ]
        
        stats = self.quality_scorer.get_quality_statistics(test_results)
        
        self.assertEqual(stats["total_items"], 3)
        self.assertEqual(stats["high_quality_items"], 2)
        self.assertEqual(stats["low_quality_items"], 1)
        self.assertAlmostEqual(stats["quality_rate"], 2/3, places=2)
        self.assertAlmostEqual(stats["average_quality_score"], (0.8 + 0.4 + 0.7) / 3, places=2)
        self.assertIn("metric_statistics", stats)
        self.assertIn("common_issues", stats)
    
    def test_save_quality_report(self):
        """품질 리포트 저장 테스트"""
        test_results = [
            QualityResult(
                quality_score=0.8,
                is_high_quality=True,
                metrics={"technical_accuracy": 0.7}
            ),
            QualityResult(
                quality_score=0.4,
                is_high_quality=False,
                issues=["Low quality"]
            )
        ]
        
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "quality_report.json"
            
            success = self.quality_scorer.save_quality_report(test_results, str(report_path))
            
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
    
    def test_final_score_calculation(self):
        """최종 점수 계산 테스트"""
        metrics = {
            "technical_accuracy": 0.8,
            "coherence": 0.7,
            "completeness": 0.6,
            "readability": 0.9,
            "relevance": 0.5
        }
        
        final_score = self.quality_scorer._calculate_final_score(metrics)
        
        self.assertGreater(final_score, 0.0)
        self.assertLessEqual(final_score, 1.0)
        
        # 가중 평균이므로 단순 평균과는 다를 수 있음
        simple_average = sum(metrics.values()) / len(metrics)
        self.assertNotEqual(final_score, simple_average)
    
    def test_confidence_score_calculation(self):
        """신뢰도 점수 계산 테스트"""
        # 일관성 있는 메트릭 (높은 신뢰도)
        consistent_metrics = {
            "metric1": 0.8,
            "metric2": 0.82,
            "metric3": 0.78,
            "metric4": 0.81
        }
        
        high_confidence = self.quality_scorer._calculate_confidence_score(consistent_metrics)
        
        # 일관성 없는 메트릭 (낮은 신뢰도)
        inconsistent_metrics = {
            "metric1": 0.9,
            "metric2": 0.2,
            "metric3": 0.7,
            "metric4": 0.1
        }
        
        low_confidence = self.quality_scorer._calculate_confidence_score(inconsistent_metrics)
        
        self.assertGreater(high_confidence, low_confidence)
        self.assertGreaterEqual(high_confidence, 0.0)
        self.assertLessEqual(high_confidence, 1.0)
        self.assertGreaterEqual(low_confidence, 0.0)
        self.assertLessEqual(low_confidence, 1.0)
    
    def test_quality_issues_analysis(self):
        """품질 이슈 분석 테스트"""
        # 저품질 메트릭
        low_quality_metrics = {
            "technical_accuracy": 0.3,
            "coherence": 0.4,
            "completeness": 0.2,
            "readability": 0.3,
            "relevance": 0.2
        }
        
        issues, suggestions = self.quality_scorer._analyze_quality_issues("짧은 텍스트", low_quality_metrics)
        
        self.assertGreater(len(issues), 0)
        self.assertGreater(len(suggestions), 0)
        
        # 이슈 내용 확인
        issue_text = " ".join(issues)
        self.assertIn("technical accuracy", issue_text.lower())
        self.assertIn("coherence", issue_text.lower())
        self.assertIn("completeness", issue_text.lower())
    
    @unittest.skipUnless(ROUGE_AVAILABLE, "ROUGE not available")
    def test_rouge_score_calculation(self):
        """ROUGE 점수 계산 테스트 (ROUGE 사용 가능한 경우)"""
        config = QualityScorerConfig(enable_rouge_score=True)
        scorer = QualityScorer(config)
        
        conversation_pairs = [
            ("DataGrid 사용법을 알려주세요.", "DataGrid 컴포넌트 사용법을 설명드리겠습니다."),
            ("Chart 컴포넌트는 어떻게 사용하나요?", "Chart 컴포넌트 사용 방법을 알려드리겠습니다.")
        ]
        
        rouge_scores = scorer._calculate_rouge_scores(conversation_pairs)
        
        if rouge_scores:  # ROUGE가 실제로 작동하는 경우
            self.assertGreater(len(rouge_scores), 0)
            for score_name, score_value in rouge_scores.items():
                self.assertGreaterEqual(score_value, 0.0)
                self.assertLessEqual(score_value, 1.0)
    
    def test_create_default_quality_scorer(self):
        """기본 품질 점수 계산기 생성 테스트"""
        default_scorer = create_default_quality_scorer()
        
        self.assertIsNotNone(default_scorer)
        self.assertIsInstance(default_scorer, QualityScorer)
        self.assertEqual(default_scorer.config.min_quality_score, 0.6)
        self.assertTrue(default_scorer.config.enable_custom_metrics)
        self.assertEqual(default_scorer.config.technical_accuracy_weight, 0.3)
        self.assertEqual(default_scorer.config.coherence_weight, 0.25)
        self.assertEqual(default_scorer.config.completeness_weight, 0.2)
        self.assertEqual(default_scorer.config.readability_weight, 0.15)
        self.assertEqual(default_scorer.config.relevance_weight, 0.1)
    
    def test_extract_conversation_pairs(self):
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
        
        pairs = self.quality_scorer._extract_conversation_pairs(sharegpt_item, "sharegpt")
        self.assertEqual(len(pairs), 2)
        self.assertEqual(pairs[0], ("질문1", "답변1"))
        self.assertEqual(pairs[1], ("질문2", "답변2"))
        
        # Alpaca 형식
        alpaca_item = {
            "instruction": "질문",
            "input": "추가 입력",
            "output": "답변"
        }
        
        pairs = self.quality_scorer._extract_conversation_pairs(alpaca_item, "alpaca")
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
        
        pairs = self.quality_scorer._extract_conversation_pairs(openai_item, "openai")
        self.assertEqual(len(pairs), 2)
        self.assertEqual(pairs[0], ("질문1", "답변1"))
        self.assertEqual(pairs[1], ("질문2", "답변2"))


if __name__ == "__main__":
    unittest.main()