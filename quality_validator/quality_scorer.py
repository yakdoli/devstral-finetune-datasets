#!/usr/bin/env python3
"""
품질 점수 계산기 모듈
ROUGE, BERT-score 기반 품질 점수를 계산하고 커스텀 메트릭을 제공합니다.
"""

import logging
import re
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json
from pathlib import Path
import math

# 선택적 임포트 (성능 향상을 위해)
try:
    from rouge_score import rouge_scorer
    ROUGE_AVAILABLE = True
except ImportError:
    ROUGE_AVAILABLE = False

try:
    from bert_score import score as bert_score
    BERT_SCORE_AVAILABLE = True
except ImportError:
    BERT_SCORE_AVAILABLE = False

try:
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False

__version__ = "1.0.0"
__author__ = "Quality Scorer Team"


@dataclass
class QualityScorerConfig:
    """품질 점수 계산기 설정"""
    # 품질 점수 임계값
    min_quality_score: float = 0.6
    
    # 사용할 메트릭
    enable_rouge_score: bool = ROUGE_AVAILABLE
    enable_bert_score: bool = False  # 기본적으로 비활성화 (무거움)
    enable_custom_metrics: bool = True
    
    # ROUGE 설정
    rouge_types: List[str] = field(default_factory=lambda: ['rouge1', 'rouge2', 'rougeL'])
    rouge_use_stemmer: bool = True
    
    # BERT Score 설정
    bert_model: str = "bert-base-multilingual-cased"
    bert_lang: str = "ko"
    
    # 커스텀 메트릭 가중치
    technical_accuracy_weight: float = 0.3
    coherence_weight: float = 0.25
    completeness_weight: float = 0.2
    readability_weight: float = 0.15
    relevance_weight: float = 0.1
    
    # 언어 설정
    language: str = "ko"
    
    # 로깅 레벨
    log_level: str = "INFO"


@dataclass
class QualityResult:
    """품질 점수 결과"""
    quality_score: float
    is_high_quality: bool
    details: Dict[str, Any] = field(default_factory=dict)
    metrics: Dict[str, float] = field(default_factory=dict)
    issues: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    confidence_score: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class QualityScorer:
    """품질 점수 계산기 클래스"""
    
    def __init__(self, config: Optional[QualityScorerConfig] = None):
        """
        품질 점수 계산기를 초기화합니다.
        
        Args:
            config: 품질 점수 계산기 설정
        """
        self.config = config or QualityScorerConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 로깅 설정
        self._setup_logging()
        
        # 메트릭 도구 초기화
        self._initialize_metrics()
        
        # 기술적 키워드 및 패턴 초기화
        self._initialize_technical_patterns()
        
        self.logger.info("QualityScorer initialized successfully")
    
    def _setup_logging(self):
        """로깅을 설정합니다."""
        level = getattr(logging, self.config.log_level.upper(), logging.INFO)
        self.logger.setLevel(level)
    
    def _initialize_metrics(self):
        """메트릭 도구를 초기화합니다."""
        # ROUGE 스코어러 초기화
        if self.config.enable_rouge_score and ROUGE_AVAILABLE:
            try:
                self.rouge_scorer = rouge_scorer.RougeScorer(
                    self.config.rouge_types,
                    use_stemmer=self.config.rouge_use_stemmer
                )
                self.logger.info("ROUGE scorer initialized")
            except Exception as e:
                self.logger.error(f"Error initializing ROUGE scorer: {e}")
                self.config.enable_rouge_score = False
        
        # NLTK 데이터 다운로드 (필요한 경우)
        if NLTK_AVAILABLE:
            try:
                nltk.data.find('tokenizers/punkt')
                nltk.data.find('corpora/stopwords')
            except LookupError:
                try:
                    nltk.download('punkt', quiet=True)
                    nltk.download('stopwords', quiet=True)
                except Exception as e:
                    self.logger.warning(f"Could not download NLTK data: {e}")
    
    def _initialize_technical_patterns(self):
        """기술적 패턴을 초기화합니다."""
        # Syncfusion WinForms 관련 기술 키워드
        self.technical_keywords = {
            "components": [
                "DataGrid", "Chart", "Gauge", "TreeView", "ListView", "ComboBox",
                "Button", "TextBox", "Label", "Panel", "Form", "Dialog",
                "Menu", "Toolbar", "StatusBar", "TabControl", "SplitContainer"
            ],
            "properties": [
                "DataSource", "Columns", "Rows", "Text", "Value", "Enabled",
                "Visible", "Size", "Location", "Anchor", "Dock", "Font",
                "ForeColor", "BackColor", "BorderStyle"
            ],
            "methods": [
                "Add", "Remove", "Clear", "Update", "Refresh", "Load", "Save",
                "Show", "Hide", "Focus", "Click", "DoubleClick", "KeyPress",
                "MouseClick", "Paint", "Resize"
            ],
            "events": [
                "Click", "DoubleClick", "KeyPress", "KeyDown", "KeyUp",
                "MouseClick", "MouseDown", "MouseUp", "MouseMove",
                "Paint", "Resize", "Load", "FormClosing"
            ],
            "namespaces": [
                "Syncfusion", "System.Windows.Forms", "System.Drawing",
                "System.ComponentModel", "System.Data", "System.Collections"
            ]
        }
        
        # 코드 패턴
        self.code_patterns = [
            re.compile(r'\b(class|public|private|protected|static|void|int|string|bool)\b', re.IGNORECASE),
            re.compile(r'\b(if|else|for|while|foreach|switch|case|try|catch|finally)\b', re.IGNORECASE),
            re.compile(r'\b(new|this|base|using|namespace|return)\b', re.IGNORECASE),
            re.compile(r'[A-Za-z_][A-Za-z0-9_]*\s*\(.*?\)', re.IGNORECASE),  # 메서드 호출
            re.compile(r'[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_]*', re.IGNORECASE),  # 속성 접근
            re.compile(r'//.*$|/\*.*?\*/', re.MULTILINE | re.DOTALL),  # 주석
        ]
        
        # 품질 지표 키워드
        self.quality_indicators = {
            "positive": [
                "예제", "샘플", "단계별", "방법", "설명", "가이드", "튜토리얼",
                "구현", "사용법", "활용", "적용", "설정", "구성", "초기화",
                "최적화", "성능", "효율", "안정", "보안", "테스트"
            ],
            "negative": [
                "모름", "잘못", "오류", "에러", "실패", "불가능", "안됨",
                "문제", "버그", "이상", "비정상", "작동안함"
            ]
        }
    
    def calculate_quality_score(self, item: Dict[str, Any], format_type: str = "sharegpt") -> QualityResult:
        """
        아이템의 품질 점수를 계산합니다.
        
        Args:
            item: 품질을 평가할 아이템
            format_type: 데이터 포맷 타입
            
        Returns:
            품질 점수 결과
        """
        try:
            # 텍스트 콘텐츠 추출
            text_content = self._extract_text_content(item, format_type)
            conversation_pairs = self._extract_conversation_pairs(item, format_type)
            
            if not text_content:
                return QualityResult(
                    quality_score=0.0,
                    is_high_quality=False,
                    issues=["No text content found for quality assessment"]
                )
            
            # 품질 메트릭 계산
            quality_metrics = {}
            
            # 1. 커스텀 메트릭 계산
            if self.config.enable_custom_metrics:
                custom_metrics = self._calculate_custom_metrics(text_content, conversation_pairs)
                quality_metrics.update(custom_metrics)
            
            # 2. ROUGE 점수 계산 (대화 쌍이 있는 경우)
            if self.config.enable_rouge_score and conversation_pairs:
                rouge_metrics = self._calculate_rouge_scores(conversation_pairs)
                quality_metrics.update(rouge_metrics)
            
            # 3. BERT Score 계산 (활성화된 경우)
            if self.config.enable_bert_score and conversation_pairs:
                bert_metrics = self._calculate_bert_scores(conversation_pairs)
                quality_metrics.update(bert_metrics)
            
            # 최종 품질 점수 계산
            final_score = self._calculate_final_score(quality_metrics)
            
            # 품질 이슈 및 제안사항 생성
            issues, suggestions = self._analyze_quality_issues(text_content, quality_metrics)
            
            # 신뢰도 점수 계산
            confidence_score = self._calculate_confidence_score(quality_metrics)
            
            result = QualityResult(
                quality_score=final_score,
                is_high_quality=final_score >= self.config.min_quality_score,
                details={
                    "text_length": len(text_content),
                    "conversation_pairs": len(conversation_pairs),
                    "format_type": format_type
                },
                metrics=quality_metrics,
                issues=issues,
                suggestions=suggestions,
                confidence_score=confidence_score
            )
            
            self.logger.debug(f"Quality score calculated: {final_score:.3f}")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error calculating quality score: {e}")
            return QualityResult(
                quality_score=0.0,
                is_high_quality=False,
                issues=[f"Quality calculation error: {str(e)}"]
            )
    
    def _extract_text_content(self, item: Dict[str, Any], format_type: str) -> str:
        """아이템에서 텍스트 콘텐츠를 추출합니다."""
        text_parts = []
        
        try:
            if format_type == "sharegpt":
                conversations = item.get("conversations", [])
                for conv in conversations:
                    if isinstance(conv, dict) and "value" in conv:
                        text_parts.append(conv["value"])
            
            elif format_type == "alpaca":
                for key in ["instruction", "input", "output"]:
                    if key in item and item[key]:
                        text_parts.append(item[key])
            
            elif format_type == "openai":
                messages = item.get("messages", [])
                for msg in messages:
                    if isinstance(msg, dict) and "content" in msg:
                        text_parts.append(msg["content"])
            
            return " ".join(text_parts)
            
        except Exception as e:
            self.logger.error(f"Error extracting text content: {e}")
            return ""
    
    def _extract_conversation_pairs(self, item: Dict[str, Any], format_type: str) -> List[Tuple[str, str]]:
        """대화 쌍을 추출합니다."""
        pairs = []
        
        try:
            if format_type == "sharegpt":
                conversations = item.get("conversations", [])
                human_msg = ""
                
                for conv in conversations:
                    if conv.get("from") == "human":
                        human_msg = conv.get("value", "")
                    elif conv.get("from") == "gpt" and human_msg:
                        pairs.append((human_msg, conv.get("value", "")))
                        human_msg = ""
            
            elif format_type == "alpaca":
                instruction = item.get("instruction", "")
                input_text = item.get("input", "")
                output = item.get("output", "")
                
                if instruction and output:
                    query = instruction + (" " + input_text if input_text else "")
                    pairs.append((query, output))
            
            elif format_type == "openai":
                messages = item.get("messages", [])
                user_msg = ""
                
                for msg in messages:
                    if msg.get("role") == "user":
                        user_msg = msg.get("content", "")
                    elif msg.get("role") == "assistant" and user_msg:
                        pairs.append((user_msg, msg.get("content", "")))
                        user_msg = ""
            
            return pairs
            
        except Exception as e:
            self.logger.error(f"Error extracting conversation pairs: {e}")
            return []
    
    def _calculate_custom_metrics(self, text: str, conversation_pairs: List[Tuple[str, str]]) -> Dict[str, float]:
        """커스텀 메트릭을 계산합니다."""
        metrics = {}
        
        # 1. 기술적 정확성 (Technical Accuracy)
        metrics["technical_accuracy"] = self._calculate_technical_accuracy(text)
        
        # 2. 일관성 (Coherence)
        metrics["coherence"] = self._calculate_coherence(text, conversation_pairs)
        
        # 3. 완성도 (Completeness)
        metrics["completeness"] = self._calculate_completeness(text, conversation_pairs)
        
        # 4. 가독성 (Readability)
        metrics["readability"] = self._calculate_readability(text)
        
        # 5. 관련성 (Relevance)
        metrics["relevance"] = self._calculate_relevance(text)
        
        return metrics
    
    def _calculate_technical_accuracy(self, text: str) -> float:
        """기술적 정확성을 계산합니다."""
        score = 0.5  # 기본 점수
        
        # 기술 키워드 밀도
        total_words = len(text.split())
        if total_words == 0:
            return 0.0
        
        technical_word_count = 0
        for category, keywords in self.technical_keywords.items():
            for keyword in keywords:
                technical_word_count += text.lower().count(keyword.lower())
        
        keyword_density = technical_word_count / total_words
        score += min(keyword_density * 2, 0.3)  # 최대 0.3 추가
        
        # 코드 패턴 존재
        code_pattern_count = 0
        for pattern in self.code_patterns:
            matches = pattern.findall(text)
            code_pattern_count += len(matches)
        
        if code_pattern_count > 0:
            score += min(code_pattern_count * 0.05, 0.2)  # 최대 0.2 추가
        
        return min(score, 1.0)
    
    def _calculate_coherence(self, text: str, conversation_pairs: List[Tuple[str, str]]) -> float:
        """일관성을 계산합니다."""
        if not conversation_pairs:
            return 0.7  # 기본 점수
        
        coherence_scores = []
        
        for query, response in conversation_pairs:
            # 질문과 답변의 주제 일치도
            query_words = set(query.lower().split())
            response_words = set(response.lower().split())
            
            # 공통 단어 비율
            common_words = query_words.intersection(response_words)
            if len(query_words) > 0:
                word_overlap = len(common_words) / len(query_words)
                coherence_scores.append(min(word_overlap * 2, 1.0))
            
            # 기술적 용어 일치도
            tech_terms_in_query = 0
            tech_terms_in_response = 0
            
            for category, keywords in self.technical_keywords.items():
                for keyword in keywords:
                    if keyword.lower() in query.lower():
                        tech_terms_in_query += 1
                    if keyword.lower() in response.lower():
                        tech_terms_in_response += 1
            
            if tech_terms_in_query > 0:
                tech_coherence = min(tech_terms_in_response / tech_terms_in_query, 1.0)
                coherence_scores.append(tech_coherence)
        
        return sum(coherence_scores) / len(coherence_scores) if coherence_scores else 0.7
    
    def _calculate_completeness(self, text: str, conversation_pairs: List[Tuple[str, str]]) -> float:
        """완성도를 계산합니다."""
        score = 0.0
        
        # 텍스트 길이 기반 점수
        text_length = len(text)
        if text_length < 50:
            score += 0.2
        elif text_length < 200:
            score += 0.5
        elif text_length < 500:
            score += 0.8
        else:
            score += 1.0
        
        # 대화 쌍의 완성도
        if conversation_pairs:
            complete_pairs = 0
            for query, response in conversation_pairs:
                if len(query.strip()) > 10 and len(response.strip()) > 20:
                    complete_pairs += 1
            
            pair_completeness = complete_pairs / len(conversation_pairs)
            score = (score + pair_completeness) / 2
        
        # 구조적 완성도 (단계별 설명, 예제 등)
        structure_indicators = ["1.", "2.", "3.", "첫째", "둘째", "셋째", "예제", "샘플", "방법"]
        structure_count = sum(1 for indicator in structure_indicators if indicator in text)
        
        if structure_count > 0:
            score += min(structure_count * 0.05, 0.2)
        
        return min(score, 1.0)
    
    def _calculate_readability(self, text: str) -> float:
        """가독성을 계산합니다."""
        if not text:
            return 0.0
        
        score = 0.5  # 기본 점수
        
        # 문장 길이 분석
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if sentences:
            avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
            
            # 적절한 문장 길이 (10-25 단어)
            if 10 <= avg_sentence_length <= 25:
                score += 0.2
            elif avg_sentence_length < 10:
                score += 0.1
            else:
                score -= 0.1
        
        # 문단 구조
        paragraphs = text.split('\n\n')
        if len(paragraphs) > 1:
            score += 0.1
        
        # 특수문자 과다 사용 확인
        special_char_ratio = len(re.findall(r'[!@#$%^&*()_+={}\[\]|\\:";\'<>?,./]', text)) / len(text)
        if special_char_ratio < 0.05:
            score += 0.1
        elif special_char_ratio > 0.15:
            score -= 0.2
        
        # 대문자 과다 사용 확인
        upper_ratio = sum(1 for c in text if c.isupper()) / len(text)
        if upper_ratio < 0.1:
            score += 0.1
        elif upper_ratio > 0.3:
            score -= 0.2
        
        return max(0.0, min(score, 1.0))
    
    def _calculate_relevance(self, text: str) -> float:
        """관련성을 계산합니다."""
        score = 0.5  # 기본 점수
        
        # Syncfusion WinForms 관련성
        syncfusion_keywords = ["syncfusion", "winforms", "datagrid", "chart", "gauge"]
        syncfusion_count = sum(1 for keyword in syncfusion_keywords if keyword.lower() in text.lower())
        
        if syncfusion_count > 0:
            score += min(syncfusion_count * 0.1, 0.3)
        
        # 프로그래밍 관련성
        programming_keywords = ["코드", "프로그램", "개발", "구현", "클래스", "메서드", "속성"]
        programming_count = sum(1 for keyword in programming_keywords if keyword in text)
        
        if programming_count > 0:
            score += min(programming_count * 0.05, 0.2)
        
        # 품질 지표 키워드
        positive_count = sum(1 for keyword in self.quality_indicators["positive"] if keyword in text)
        negative_count = sum(1 for keyword in self.quality_indicators["negative"] if keyword in text)
        
        score += min(positive_count * 0.02, 0.1)
        score -= min(negative_count * 0.05, 0.2)
        
        return max(0.0, min(score, 1.0))
    
    def _calculate_rouge_scores(self, conversation_pairs: List[Tuple[str, str]]) -> Dict[str, float]:
        """ROUGE 점수를 계산합니다."""
        if not ROUGE_AVAILABLE or not conversation_pairs:
            return {}
        
        rouge_scores = {rouge_type: [] for rouge_type in self.config.rouge_types}
        
        try:
            for query, response in conversation_pairs:
                # 참조 텍스트로 질문을 사용하고, 가설 텍스트로 답변을 사용
                scores = self.rouge_scorer.score(query, response)
                
                for rouge_type in self.config.rouge_types:
                    if rouge_type in scores:
                        rouge_scores[rouge_type].append(scores[rouge_type].fmeasure)
            
            # 평균 점수 계산
            avg_rouge_scores = {}
            for rouge_type, scores in rouge_scores.items():
                if scores:
                    avg_rouge_scores[f"rouge_{rouge_type}"] = sum(scores) / len(scores)
            
            return avg_rouge_scores
            
        except Exception as e:
            self.logger.error(f"Error calculating ROUGE scores: {e}")
            return {}
    
    def _calculate_bert_scores(self, conversation_pairs: List[Tuple[str, str]]) -> Dict[str, float]:
        """BERT Score를 계산합니다."""
        if not BERT_SCORE_AVAILABLE or not conversation_pairs:
            return {}
        
        try:
            references = [pair[0] for pair in conversation_pairs]
            candidates = [pair[1] for pair in conversation_pairs]
            
            P, R, F1 = bert_score(
                candidates, references,
                model_type=self.config.bert_model,
                lang=self.config.bert_lang,
                verbose=False
            )
            
            return {
                "bert_precision": float(P.mean()),
                "bert_recall": float(R.mean()),
                "bert_f1": float(F1.mean())
            }
            
        except Exception as e:
            self.logger.error(f"Error calculating BERT scores: {e}")
            return {}
    
    def _calculate_final_score(self, metrics: Dict[str, float]) -> float:
        """최종 품질 점수를 계산합니다."""
        if not metrics:
            return 0.0
        
        weighted_score = 0.0
        total_weight = 0.0
        
        # 커스텀 메트릭 가중치 적용
        custom_metrics = {
            "technical_accuracy": self.config.technical_accuracy_weight,
            "coherence": self.config.coherence_weight,
            "completeness": self.config.completeness_weight,
            "readability": self.config.readability_weight,
            "relevance": self.config.relevance_weight
        }
        
        for metric, weight in custom_metrics.items():
            if metric in metrics:
                weighted_score += metrics[metric] * weight
                total_weight += weight
        
        # ROUGE 점수 (사용 가능한 경우)
        rouge_weight = 0.1
        rouge_scores = [v for k, v in metrics.items() if k.startswith("rouge_")]
        if rouge_scores:
            avg_rouge = sum(rouge_scores) / len(rouge_scores)
            weighted_score += avg_rouge * rouge_weight
            total_weight += rouge_weight
        
        # BERT Score (사용 가능한 경우)
        bert_weight = 0.1
        if "bert_f1" in metrics:
            weighted_score += metrics["bert_f1"] * bert_weight
            total_weight += bert_weight
        
        # 가중 평균 계산
        if total_weight > 0:
            final_score = weighted_score / total_weight
        else:
            final_score = sum(metrics.values()) / len(metrics)
        
        return max(0.0, min(final_score, 1.0))
    
    def _analyze_quality_issues(self, text: str, metrics: Dict[str, float]) -> Tuple[List[str], List[str]]:
        """품질 이슈와 제안사항을 분석합니다."""
        issues = []
        suggestions = []
        
        # 기술적 정확성 이슈
        if metrics.get("technical_accuracy", 0) < 0.5:
            issues.append("Low technical accuracy - insufficient technical content")
            suggestions.append("Include more Syncfusion WinForms specific terms and code examples")
        
        # 일관성 이슈
        if metrics.get("coherence", 0) < 0.6:
            issues.append("Low coherence - question and answer don't align well")
            suggestions.append("Ensure answers directly address the questions asked")
        
        # 완성도 이슈
        if metrics.get("completeness", 0) < 0.5:
            issues.append("Low completeness - content appears incomplete")
            suggestions.append("Provide more detailed explanations and examples")
        
        # 가독성 이슈
        if metrics.get("readability", 0) < 0.5:
            issues.append("Low readability - text is difficult to read")
            suggestions.append("Use shorter sentences and better paragraph structure")
        
        # 관련성 이슈
        if metrics.get("relevance", 0) < 0.5:
            issues.append("Low relevance - content not sufficiently related to WinForms")
            suggestions.append("Focus more on WinForms development topics")
        
        # 텍스트 길이 이슈
        text_length = len(text)
        if text_length < 100:
            issues.append("Content too short")
            suggestions.append("Provide more detailed explanations")
        elif text_length > 2000:
            issues.append("Content too long")
            suggestions.append("Consider breaking into smaller, focused responses")
        
        return issues, suggestions
    
    def _calculate_confidence_score(self, metrics: Dict[str, float]) -> float:
        """신뢰도 점수를 계산합니다."""
        if not metrics:
            return 0.0
        
        # 메트릭의 일관성 확인
        metric_values = list(metrics.values())
        if len(metric_values) < 2:
            return 0.5
        
        # 표준편차 계산 (낮을수록 일관성 높음)
        mean_value = sum(metric_values) / len(metric_values)
        variance = sum((x - mean_value) ** 2 for x in metric_values) / len(metric_values)
        std_dev = math.sqrt(variance)
        
        # 신뢰도 점수 (표준편차가 낮을수록 높은 신뢰도)
        confidence = max(0.0, 1.0 - std_dev * 2)
        
        # 메트릭 수가 많을수록 신뢰도 증가
        metric_count_bonus = min(len(metrics) * 0.1, 0.3)
        
        return min(confidence + metric_count_bonus, 1.0)
    
    def batch_calculate_quality(self, items: List[Dict[str, Any]], format_type: str = "sharegpt") -> List[QualityResult]:
        """
        여러 아이템의 품질 점수를 배치로 계산합니다.
        
        Args:
            items: 품질을 평가할 아이템 목록
            format_type: 데이터 포맷 타입
            
        Returns:
            품질 점수 결과 목록
        """
        results = []
        
        for i, item in enumerate(items):
            try:
                result = self.calculate_quality_score(item, format_type)
                results.append(result)
                
                if (i + 1) % 100 == 0:
                    self.logger.info(f"Processed {i + 1}/{len(items)} items for quality scoring")
                    
            except Exception as e:
                self.logger.error(f"Error calculating quality for item {i}: {e}")
                results.append(QualityResult(
                    quality_score=0.0,
                    is_high_quality=False,
                    issues=[f"Quality calculation error: {str(e)}"]
                ))
        
        high_quality_count = sum(1 for r in results if r.is_high_quality)
        self.logger.info(f"Quality scoring completed: {high_quality_count}/{len(results)} items are high quality")
        
        return results
    
    def get_quality_statistics(self, results: List[QualityResult]) -> Dict[str, Any]:
        """품질 점수 통계를 생성합니다."""
        if not results:
            return {}
        
        scores = [r.quality_score for r in results]
        high_quality_count = sum(1 for r in results if r.is_high_quality)
        
        # 메트릭별 통계
        metric_stats = {}
        all_metrics = set()
        for result in results:
            all_metrics.update(result.metrics.keys())
        
        for metric in all_metrics:
            metric_values = [r.metrics.get(metric, 0.0) for r in results]
            metric_stats[metric] = {
                "mean": sum(metric_values) / len(metric_values),
                "min": min(metric_values),
                "max": max(metric_values)
            }
        
        # 이슈 통계
        all_issues = []
        for result in results:
            all_issues.extend(result.issues)
        
        issue_counts = {}
        for issue in all_issues:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
        
        return {
            "total_items": len(results),
            "high_quality_items": high_quality_count,
            "low_quality_items": len(results) - high_quality_count,
            "quality_rate": high_quality_count / len(results),
            "average_quality_score": sum(scores) / len(scores),
            "min_quality_score": min(scores),
            "max_quality_score": max(scores),
            "metric_statistics": metric_stats,
            "common_issues": dict(sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)[:10]),
            "average_confidence": sum(r.confidence_score for r in results) / len(results)
        }
    
    def save_quality_report(self, results: List[QualityResult], output_path: str) -> bool:
        """품질 점수 리포트를 저장합니다."""
        try:
            report = {
                "report_version": "1.0.0",
                "generated_at": datetime.now().isoformat(),
                "configuration": {
                    "min_quality_score": self.config.min_quality_score,
                    "enable_rouge_score": self.config.enable_rouge_score,
                    "enable_bert_score": self.config.enable_bert_score,
                    "enable_custom_metrics": self.config.enable_custom_metrics,
                    "technical_accuracy_weight": self.config.technical_accuracy_weight,
                    "coherence_weight": self.config.coherence_weight,
                    "completeness_weight": self.config.completeness_weight,
                    "readability_weight": self.config.readability_weight,
                    "relevance_weight": self.config.relevance_weight
                },
                "statistics": self.get_quality_statistics(results),
                "detailed_results": [
                    {
                        "quality_score": r.quality_score,
                        "is_high_quality": r.is_high_quality,
                        "details": r.details,
                        "metrics": r.metrics,
                        "issues": r.issues,
                        "suggestions": r.suggestions,
                        "confidence_score": r.confidence_score,
                        "timestamp": r.timestamp
                    }
                    for r in results
                ]
            }
            
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"Quality report saved to {output_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving quality report: {e}")
            return False


def create_default_quality_scorer() -> QualityScorer:
    """기본 설정으로 품질 점수 계산기를 생성합니다."""
    config = QualityScorerConfig(
        min_quality_score=0.6,
        enable_rouge_score=ROUGE_AVAILABLE,
        enable_bert_score=False,  # 기본적으로 비활성화
        enable_custom_metrics=True,
        technical_accuracy_weight=0.3,
        coherence_weight=0.25,
        completeness_weight=0.2,
        readability_weight=0.15,
        relevance_weight=0.1,
        language="ko",
        log_level="INFO"
    )
    
    return QualityScorer(config)


if __name__ == "__main__":
    # 모듈 테스트
    print(f"Quality Scorer Module v{__version__}")
    print(f"Author: {__author__}")
    print(f"ROUGE available: {ROUGE_AVAILABLE}")
    print(f"BERT Score available: {BERT_SCORE_AVAILABLE}")
    print(f"NLTK available: {NLTK_AVAILABLE}")
    
    # 샘플 테스트
    quality_scorer = create_default_quality_scorer()
    
    # 테스트 데이터
    test_items = [
        {
            "conversations": [
                {"from": "human", "value": "Syncfusion DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "Syncfusion DataGrid 컴포넌트는 다음과 같이 사용합니다:\n\n1. 프로젝트에 Syncfusion.Grid.WinForms 참조를 추가합니다.\n2. Form에 SfDataGrid 컨트롤을 배치합니다.\n3. DataSource 속성에 데이터를 바인딩합니다.\n4. Columns 컬렉션을 통해 컬럼을 구성합니다.\n\n예제 코드:\n```csharp\nSfDataGrid dataGrid = new SfDataGrid();\ndataGrid.DataSource = dataTable;\nthis.Controls.Add(dataGrid);\n```"}
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
                {"from": "human", "value": "Chart 컴포넌트로 막대 그래프를 만드는 방법을 알려주세요."},
                {"from": "gpt", "value": "Syncfusion Chart 컴포넌트로 막대 그래프를 만드는 방법:\n\n1. SfChart 컨트롤을 Form에 추가\n2. ColumnSeries를 생성하고 차트에 추가\n3. 데이터 바인딩 설정\n4. 축 설정 및 범례 추가\n\n상세한 구현 방법과 속성 설정을 통해 다양한 스타일의 막대 그래프를 생성할 수 있습니다."}
            ]
        }
    ]
    
    # 품질 점수 계산
    results = quality_scorer.batch_calculate_quality(test_items)
    
    for i, result in enumerate(results):
        print(f"\nItem {i+1}:")
        print(f"  Quality Score: {result.quality_score:.3f}")
        print(f"  High Quality: {result.is_high_quality}")
        print(f"  Confidence: {result.confidence_score:.3f}")
        print(f"  Metrics: {result.metrics}")
        if result.issues:
            print(f"  Issues: {result.issues}")
        if result.suggestions:
            print(f"  Suggestions: {result.suggestions}")
    
    # 통계 출력
    stats = quality_scorer.get_quality_statistics(results)
    print(f"\nStatistics:")
    print(f"  Quality rate: {stats['quality_rate']:.3f}")
    print(f"  Average score: {stats['average_quality_score']:.3f}")
    print(f"  Average confidence: {stats['average_confidence']:.3f}")