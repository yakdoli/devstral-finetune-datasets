#!/usr/bin/env python3
"""
품질 점수 계산 모듈
다양한 지표를 통한 데이터셋 품질 평가 기능을 제공합니다.
"""

import re
import logging
import math
from typing import List, Dict, Any, Optional, Set, Tuple, Union
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from collections import Counter, defaultdict

logger = logging.getLogger(__name__)


@dataclass
class QualityScorerConfig:
    """품질 점수 계산기 설정"""
    # 내용 품질 설정
    content_quality_enabled: bool = True
    min_content_length: int = 10
    max_content_length: int = 50000
    min_sentence_count: int = 1
    min_word_count: int = 5
    
    # 구조 품질 설정
    structural_quality_enabled: bool = True
    required_conversation_turns: int = 2
    min_turn_length: int = 5
    max_turn_length: int = 1000
    
    # 언어 품질 설정
    language_quality_enabled: bool = True
    grammar_check_enabled: bool = True
    spelling_check_enabled: bool = True
    fluency_check_enabled: bool = True
    
    # 기술 품질 설정
    technical_quality_enabled: bool = True
    code_quality_enabled: bool = True
    technical_accuracy_enabled: bool = True
    
    # 가중치 설정
    content_weight: float = 0.3
    structural_weight: float = 0.25
    language_weight: float = 0.25
    technical_weight: float = 0.2
    
    # 임계값 설정
    min_quality_threshold: float = 0.6
    excellent_quality_threshold: float = 0.8


@dataclass
class QualityResult:
    """품질 검증 결과"""
    quality_score: float = 0.0
    details: Dict[str, Any] = field(default_factory=dict)
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    is_valid: bool = True


@dataclass
class QualityScoreResult:
    """품질 점수 계산 결과"""
    total_score: float = 0.0
    content_score: float = 0.0
    structural_score: float = 0.0
    language_score: float = 0.0
    technical_score: float = 0.0
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    detailed_metrics: Dict[str, Any] = field(default_factory=dict)
    scoring_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


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
        
        # 텍스트 분석 설정
        self._setup_text_analysis()
        
        # 기술 용어 사전
        self._setup_technical_dictionaries()
    
    def _setup_text_analysis(self):
        """텍스트 분석 설정을 초기화합니다."""
        # 문장 분리 패턴
        self.sentence_patterns = {
            'basic': re.compile(r'[.!?]+'),
            'code': re.compile(r'[.!?;]+'),
            'question': re.compile(r'[?！？]+')
        }
        
        # 단어 분리 패턴
        self.word_pattern = re.compile(r'\b\w+\b')
        
        # 문법 오류 패턴 (간소화된 버전)
        self.grammar_patterns = [
            (r'\s+,\s+', ', '),  # 쉼표 주변 공백
            (r'\s+\.+', '.'),   # 마침표 주변 공백
            (r'\s+!+', '!'),    # 느낌표 주변 공백
            (r'\s+\?+', '?'),   # 물음표 주변 공백
            (r'\s+:+', ':'),    # 콜론 주변 공백
            (r'\s+;+', ';'),    # 세미콜론 주변 공백
        ]
        
        # 반복되는 문자 패턴
        self.repeated_char_pattern = re.compile(r'(.)\1{2,}')
    
    def _setup_technical_dictionaries(self):
        """기술 용어 사전을 설정합니다."""
        # Syncfusion 관련 기술 용어
        self.syncfusion_terms = {
            'winforms', 'wpf', 'blazor', 'maui', 'xamarin', 'asp.net', 'mvc',
            'datagrid', 'grid', 'chart', 'gauge', 'spreadsheet', 'report',
            'pdf', 'docio', 'xlsio', 'presentation', 'diagram', 'schedule',
            'edit', 'tools', 'calculate', 'pivotgrid', 'olap', 'qtp',
            'htmlui', 'projio', 'pdfviewer', 'pivotgrid', 'grouping',
            'olap-common', 'chart', 'gauge', 'grid', 'edit', 'tools',
            'calculate', 'pdf', 'docio', 'xlsio', 'presentation', 'diagram',
            'schedule', 'htmlui', 'projio', 'pdfviewer', 'pivotgrid'
        }
        
        # 프로그래밍 관련 용어
        self.programming_terms = {
            'class', 'method', 'function', 'variable', 'parameter', 'argument',
            'return', 'if', 'else', 'for', 'while', 'do', 'switch', 'case',
            'try', 'catch', 'finally', 'throw', 'import', 'from', 'as',
            'public', 'private', 'protected', 'static', 'virtual', 'override',
            'abstract', 'interface', 'namespace', 'using', 'include', 'require',
            'def', 'lambda', 'yield', 'async', 'await', 'try', 'except',
            'finally', 'raise', 'with', 'pass', 'break', 'continue'
        }
        
        # 코드 블록 패턴
        self.code_block_patterns = [
            r'```[\s\S]*?```',  # 백틱 코드 블록
            r'`[^`]+`',        # 인라인 코드
            r'<code[^>]*>.*?</code>',  # HTML 코드 태그
            r'<pre[^>]*>.*?</pre>',    # HTML pre 태그
        ]
    
    def calculate_quality_score(self, item: Dict[str, Any], item_type: str = "text") -> QualityScoreResult:
        """
        아이템의 품질 점수를 계산합니다.
        
        Args:
            item: 품질 평가할 아이템
            item_type: 아이템 타입 (text, conversation, code)
            
        Returns:
            품질 점수 계산 결과
        """
        result = QualityScoreResult()
        
        if not item:
            result.total_score = 0.0
            result.issues.append("빈 아이템")
            return result
        
        # 각 품질 요소별 점수 계산
        scores = {}
        
        # 1. 내용 품질 점수
        if self.config.content_quality_enabled:
            content_score, content_metrics = self._calculate_content_quality(item, item_type)
            scores['content'] = content_score
            result.content_score = content_score
            result.detailed_metrics['content'] = content_metrics
        
        # 2. 구조 품질 점수
        if self.config.structural_quality_enabled:
            structural_score, structural_metrics = self._calculate_structural_quality(item, item_type)
            scores['structural'] = structural_score
            result.structural_score = structural_score
            result.detailed_metrics['structural'] = structural_metrics
        
        # 3. 언어 품질 점수
        if self.config.language_quality_enabled:
            language_score, language_metrics = self._calculate_language_quality(item, item_type)
            scores['language'] = language_score
            result.language_score = language_score
            result.detailed_metrics['language'] = language_metrics
        
        # 4. 기술 품질 점수
        if self.config.technical_quality_enabled:
            technical_score, technical_metrics = self._calculate_technical_quality(item, item_type)
            scores['technical'] = technical_score
            result.technical_score = technical_score
            result.detailed_metrics['technical'] = technical_metrics
        
        # 가중치 적용하여 최종 점수 계산
        result.total_score = self._calculate_weighted_score(scores)
        
        # 이슈 및 경고 생성
        self._generate_quality_issues(result, scores)
        
        return result
    
    def _calculate_content_quality(self, item: Dict[str, Any], item_type: str) -> Tuple[float, Dict[str, Any]]:
        """내용 품질 점수를 계산합니다."""
        metrics = {}
        score = 1.0
        
        # 텍스트 추출
        text = self._extract_text_for_analysis(item, item_type)
        
        if not text:
            return 0.0, {"error": "텍스트 추출 실패"}
        
        # 길이 점수
        text_length = len(text)
        length_score = self._calculate_length_score(text_length)
        score *= length_score
        metrics['length'] = text_length
        metrics['length_score'] = length_score
        
        # 문장 구조 점수
        sentence_count = self._count_sentences(text)
        sentence_score = self._calculate_sentence_score(sentence_count, text_length)
        score *= sentence_score
        metrics['sentence_count'] = sentence_count
        metrics['sentence_score'] = sentence_score
        
        # 단어 다양성 점수
        word_diversity = self._calculate_word_diversity(text)
        score *= word_diversity
        metrics['word_diversity'] = word_diversity
        
        # 정보성 점수
        informativeness = self._calculate_informativeness(text)
        score *= informativeness
        metrics['informativeness'] = informativeness
        
        # 일관성 점수
        consistency = self._calculate_consistency(text)
        score *= consistency
        metrics['consistency'] = consistency
        
        return max(0.0, min(1.0, score)), metrics
    
    def _calculate_structural_quality(self, item: Dict[str, Any], item_type: str) -> Tuple[float, Dict[str, Any]]:
        """구조 품질 점수를 계산합니다."""
        metrics = {}
        score = 1.0
        
        if item_type == "conversation":
            # 대화 구조 품질
            conversations = item.get("conversations", [])
            metrics['turn_count'] = len(conversations)
            
            # 최소 턴 수 확인
            if len(conversations) < self.config.required_conversation_turns:
                score *= 0.5
                metrics['turn_score'] = 0.5
            else:
                metrics['turn_score'] = 1.0
            
            # 각 턴의 길이 점수
            turn_scores = []
            for i, conv in enumerate(conversations):
                turn_length = len(conv.get("value", ""))
                turn_score = self._calculate_turn_length_score(turn_length)
                turn_scores.append(turn_score)
            
            avg_turn_score = sum(turn_scores) / len(turn_scores) if turn_scores else 0
            score *= avg_turn_score
            metrics['average_turn_score'] = avg_turn_score
            
            # 역할 순서 점수
            role_score = self._calculate_role_sequence_score(conversations)
            score *= role_score
            metrics['role_sequence_score'] = role_score
            
        elif item_type in ["text", "instruction"]:
            # 텍스트 구조 품질
            structure_score = self._calculate_text_structure_score(item)
            score *= structure_score
            metrics['structure_score'] = structure_score
        
        return max(0.0, min(1.0, score)), metrics
    
    def _calculate_language_quality(self, item: Dict[str, Any], item_type: str) -> Tuple[float, Dict[str, Any]]:
        """언어 품질 점수를 계산합니다."""
        metrics = {}
        score = 1.0
        
        # 텍스트 추출
        text = self._extract_text_for_analysis(item, item_type)
        
        if not text:
            return 0.0, {"error": "텍스트 추출 실패"}
        
        # 문법 점수
        if self.config.grammar_check_enabled:
            grammar_score = self._calculate_grammar_score(text)
            score *= grammar_score
            metrics['grammar_score'] = grammar_score
        
        # 맞춤법 점수
        if self.config.spelling_check_enabled:
            spelling_score = self._calculate_spelling_score(text)
            score *= spelling_score
            metrics['spelling_score'] = spelling_score
        
        # 유창성 점수
        if self.config.fluency_check_enabled:
            fluency_score = self._calculate_fluency_score(text)
            score *= fluency_score
            metrics['fluency_score'] = fluency_score
        
        # 자연스러움 점수
        naturalness_score = self._calculate_naturalness_score(text)
        score *= naturalness_score
        metrics['naturalness_score'] = naturalness_score
        
        return max(0.0, min(1.0, score)), metrics
    
    def _calculate_technical_quality(self, item: Dict[str, Any], item_type: str) -> Tuple[float, Dict[str, Any]]:
        """기술 품질 점수를 계산합니다."""
        metrics = {}
        score = 1.0
        
        # 텍스트 추출
        text = self._extract_text_for_analysis(item, item_type)
        
        if not text:
            return 0.0, {"error": "텍스트 추출 실패"}
        
        # 코드 품질 점수
        if self.config.code_quality_enabled:
            code_score, code_metrics = self._calculate_code_quality(text)
            score *= code_score
            metrics['code_quality'] = code_metrics
        
        # 기술적 정확성 점수
        if self.config.technical_accuracy_enabled:
            accuracy_score = self._calculate_technical_accuracy(text, item_type)
            score *= accuracy_score
            metrics['technical_accuracy'] = accuracy_score
        
        # 실용성 점수
        practicality_score = self._calculate_practicality_score(text)
        score *= practicality_score
        metrics['practicality_score'] = practicality_score
        
        return max(0.0, min(1.0, score)), metrics
    
    def _extract_text_for_analysis(self, item: Dict[str, Any], item_type: str) -> str:
        """분석을 위한 텍스트를 추출합니다."""
        text_parts = []
        
        if item_type == "conversation":
            for conv in item.get("conversations", []):
                text_parts.append(conv.get("value", ""))
        elif item_type == "instruction":
            text_parts.append(item.get("instruction", ""))
            text_parts.append(item.get("response", ""))
            text_parts.append(item.get("output", ""))
        elif item_type == "code":
            text_parts.append(item.get("code", ""))
            text_parts.append(item.get("explanation", ""))
        else:
            # 일반 텍스트
            for field in ["instruction", "response", "input", "output", "content", "text"]:
                if field in item:
                    text_parts.append(str(item[field]))
        
        return " ".join(text_parts)
    
    def _calculate_length_score(self, length: int) -> float:
        """길이 점수를 계산합니다."""
        if length < self.config.min_content_length:
            return 0.3
        elif length > self.config.max_content_length:
            return 0.7
        else:
            # 선형 보간
            normalized = (length - self.config.min_content_length) / (self.config.max_content_length - self.config.min_content_length)
            return 0.3 + 0.7 * normalized
    
    def _count_sentences(self, text: str) -> int:
        """문장 수를 계산합니다."""
        # 여러 패턴으로 문장 분리
        sentences = []
        for pattern_name, pattern in self.sentence_patterns.items():
            matches = pattern.findall(text)
            sentences.extend(matches)
        
        return len(sentences)
    
    def _calculate_sentence_score(self, sentence_count: int, text_length: int) -> float:
        """문장 점수를 계산합니다."""
        if sentence_count < self.config.min_sentence_count:
            return 0.5
        
        # 평균 문장 길이 계산
        avg_sentence_length = text_length / sentence_count if sentence_count > 0 else 0
        
        # 적절한 문장 길이 범위 확인
        if avg_sentence_length < 10 or avg_sentence_length > 100:
            return 0.7
        
        return 1.0
    
    def _calculate_word_diversity(self, text: str) -> float:
        """단어 다양성 점수를 계산합니다."""
        words = self.word_pattern.findall(text.lower())
        
        if len(words) < 10:
            return 0.5
        
        # 고유 단어 비율 계산
        unique_words = set(words)
        diversity = len(unique_words) / len(words)
        
        # 불용어 제외 후 다시 계산
        filtered_words = [word for word in words if word not in self._get_stop_words()]
        if len(filtered_words) > 0:
            unique_filtered = set(filtered_words)
            filtered_diversity = len(unique_filtered) / len(filtered_words)
            diversity = (diversity + filtered_diversity) / 2
        
        return min(1.0, diversity)
    
    def _calculate_informativeness(self, text: str) -> float:
        """정보성 점수를 계산합니다."""
        # 명사, 동사, 형용사 비율 계산
        words = self.word_pattern.findall(text.lower())
        
        if not words:
            return 0.0
        
        # 간단한 품사 패턴 (간소화된 버전)
        content_words = 0
        for word in words:
            if len(word) > 3 and not word.isdigit():
                content_words += 1
        
        content_ratio = content_words / len(words)
        return min(1.0, content_ratio)
    
    def _calculate_consistency(self, text: str) -> float:
        """일관성 점수를 계산합니다."""
        # 반복되는 패턴 검사
        repeated_chars = self.repeated_char_pattern.findall(text)
        
        if repeated_chars:
            return 0.8  # 반복 문자가 있으면 점수 감소
        
        # 일관된 주제 유지 여부 검사 (간단한 버전)
        sentences = self.sentence_patterns['basic'].split(text)
        
        if len(sentences) < 2:
            return 1.0
        
        # 첫 문장과 마지막 문장의 유사도 검사
        first_sentence = sentences[0].strip()
        last_sentence = sentences[-1].strip()
        
        if first_sentence and last_sentence:
            first_words = set(first_sentence.lower().split())
            last_words = set(last_sentence.lower().split())
            
            if first_words and last_words:
                intersection = len(first_words.intersection(last_words))
                union = len(first_words.union(last_words))
                
                if union > 0:
                    similarity = intersection / union
                    return 0.7 + 0.3 * similarity
        
        return 0.8
    
    def _calculate_turn_length_score(self, turn_length: int) -> float:
        """대화 턴 길이 점수를 계산합니다."""
        if turn_length < self.config.min_turn_length:
            return 0.5
        elif turn_length > self.config.max_turn_length:
            return 0.7
        else:
            normalized = (turn_length - self.config.min_turn_length) / (self.config.max_turn_length - self.config.min_turn_length)
            return 0.5 + 0.5 * normalized
    
    def _calculate_role_sequence_score(self, conversations: List[Dict[str, Any]]) -> float:
        """역할 순서 점수를 계산합니다."""
        if not conversations:
            return 0.0
        
        # 기대되는 역할 순서
        expected_roles = ['system', 'human', 'gpt']
        
        # 실제 역할 순서
        actual_roles = [conv.get('from', '') for conv in conversations]
        
        # 순서 점수 계산
        score = 0.0
        for i, expected in enumerate(expected_roles):
            if i < len(actual_roles) and actual_roles[i] == expected:
                score += 1.0 / len(expected_roles)
        
        return score
    
    def _calculate_text_structure_score(self, item: Dict[str, Any]) -> float:
        """텍스트 구조 점수를 계산합니다."""
        score = 1.0
        
        # 필드 존재 여부 확인
        required_fields = ['instruction', 'response']
        for field in required_fields:
            if field not in item or not item[field]:
                score *= 0.5
        
        # 필드 길이 확인
        for field in required_fields:
            if field in item:
                field_length = len(str(item[field]))
                if field_length < 10:
                    score *= 0.8
        
        return score
    
    def _calculate_grammar_score(self, text: str) -> float:
        """문법 점수를 계산합니다."""
        score = 1.0
        
        # 간단한 문법 패턴 검사
        grammar_issues = 0
        
        # 연속된 구두점 검사
        if re.search(r'[.!?]{2,}', text):
            grammar_issues += 1
        
        # 불필요한 공백 검사
        if re.search(r'\s{2,}', text):
            grammar_issues += 1
        
        # 대문자 사용 검사
        sentences = self.sentence_patterns['basic'].split(text)
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and not sentence[0].isupper():
                grammar_issues += 0.1
        
        # 문법 이슈에 따른 점수 감소
        if grammar_issues > 0:
            score = max(0.3, 1.0 - grammar_issues * 0.1)
        
        return score
    
    def _calculate_spelling_score(self, text: str) -> float:
        """맞춤법 점수를 계산합니다."""
        # 간단한 맞춤법 검사 (간소화된 버전)
        words = self.word_pattern.findall(text.lower())
        
        if not words:
            return 1.0
        
        # 명백한 맞춤법 오류 검사
        spelling_errors = 0
        
        common_misspellings = {
            'teh': 'the',
            'adn': 'and',
            'thier': 'their',
            'recieve': 'receive',
            'seperate': 'separate',
            'definately': 'definitely',
            'occured': 'occurred',
            'untill': 'until',
            'alot': 'a lot'
        }
        
        for word in words:
            if word in common_misspellings:
                spelling_errors += 1
        
        # 맞춤법 오류 비율 계산
        error_rate = spelling_errors / len(words) if words else 0
        
        return max(0.5, 1.0 - error_rate * 2)
    
    def _calculate_fluency_score(self, text: str) -> float:
        """유창성 점수를 계산합니다."""
        score = 1.0
        
        # 문장 길이 변화 계산
        sentences = self.sentence_patterns['basic'].split(text)
        if len(sentences) > 1:
            sentence_lengths = [len(s.strip()) for s in sentences if s.strip()]
            
            if len(sentence_lengths) > 1:
                # 길이 변화 계산
                length_variance = np.var(sentence_lengths)
                
                # 변화가 너무 크면 유창성 감소
                if length_variance > 1000:
                    score *= 0.8
        
        # 반복되는 구조 검사
        repeated_patterns = re.findall(r'(\b\w+\s+\b\w+\s+\b\w+\b).*\1', text)
        if repeated_patterns:
            score *= 0.9
        
        return score
    
    def _calculate_naturalness_score(self, text: str) -> float:
        """자연스러움 점수를 계산합니다."""
        score = 1.0
        
        # 인공적인 패턴 검사
        artificial_patterns = [
            r'이것은.*입니다\.$',
            r'다음은.*입니다\.$',
            r'위의.*는.*입니다\.$',
            r'아래.*는.*입니다\.$'
        ]
        
        for pattern in artificial_patterns:
            if re.search(pattern, text):
                score *= 0.9
        
        # 지나치게 형식적인 표현 검사
        formal_patterns = [
            r'본문에서',
            r'상기한',
            r'전술한',
            r'아래에 기재된'
        ]
        
        formal_count = sum(1 for pattern in formal_patterns if re.search(pattern, text))
        if formal_count > 0:
            score *= (1.0 - formal_count * 0.1)
        
        return max(0.5, score)
    
    def _calculate_code_quality(self, text: str) -> Tuple[float, Dict[str, Any]]:
        """코드 품질 점수를 계산합니다."""
        metrics = {}
        score = 1.0
        
        # 코드 블록 검사
        code_blocks = []
        for pattern in self.code_block_patterns:
            matches = re.findall(pattern, text, re.MULTILINE | re.IGNORECASE)
            code_blocks.extend(matches)
        
        metrics['code_blocks'] = len(code_blocks)
        
        if code_blocks:
            # 코드 품질 분석
            for code_block in code_blocks:
                # 코드 구조 점수
                structure_score = self._analyze_code_structure(code_block)
                score *= structure_score
                
                # 코드 정확성 점수
                accuracy_score = self._analyze_code_accuracy(code_block)
                score *= accuracy_score
        
        return max(0.0, min(1.0, score)), metrics
    
    def _analyze_code_structure(self, code: str) -> float:
        """코드 구조를 분석합니다."""
        score = 1.0
        
        # 코드 블록 크기 검사
        if len(code) > 5000:
            score *= 0.8
        
        # 코드 구조 요소 검사
        structure_elements = [
            (r'class\s+\w+', 'class'),
            (r'def\s+\w+\s*\(', 'function'),
            (r'if\s+.*?:', 'conditional'),
            (r'for\s+.*?in\s+.*?:', 'loop'),
            (r'while\s+.*?:', 'loop'),
            (r'try:.*?except:', 'exception')
        ]
        
        found_elements = []
        for pattern, element_type in structure_elements:
            if re.search(pattern, code, re.MULTILINE | re.IGNORECASE):
                found_elements.append(element_type)
        
        # 구조적 복잡도 점수
        if len(found_elements) > 3:
            score *= 0.9
        
        return score
    
    def _analyze_code_accuracy(self, code: str) -> float:
        """코드 정확성을 분석합니다."""
        score = 1.0
        
        # 명백한 오류 검사
        error_patterns = [
            r'\bimport\s+[^,\s]+\s*,',  # 잘못된 import 구문
            r'\bdef\s+\w+\s*\([^)]*\)\s*:',  # 잘못된 함수 정의
            r'\bclass\s+\w+\s*[^:]*[^:]\s*:',  # 잘못된 클래스 정의
            r'\bif\s+[^:]*[^:]\s*:',  # 잘못된 if 구문
        ]
        
        for pattern in error_patterns:
            if re.search(pattern, code, re.MULTILINE | re.IGNORECASE):
                score *= 0.8
        
        return score
    
    def _calculate_technical_accuracy(self, text: str, item_type: str) -> float:
        """기술적 정확성 점수를 계산합니다."""
        score = 1.0
        
        # 기술 용어 사용 검사
        words = self.word_pattern.findall(text.lower())
        
        if words:
            # Syncfusion 용어 사용 검사
            syncfusion_terms_used = sum(1 for word in words if word in self.syncfusion_terms)
            programming_terms_used = sum(1 for word in words if word in self.programming_terms)
            
            # 용어 사용 비율 계산
            total_terms = syncfusion_terms_used + programming_terms_used
            if total_terms > 0:
                term_ratio = total_terms / len(words)
                score = min(1.0, 0.5 + term_ratio * 0.5)
        
        # 기술적 정확성 검사
        accuracy_issues = 0
        
        # 모순되는 정보 검사
        if 'WinForms' in text and 'WPF' in text:
            if '동시에' in text or '같이' in text:
                accuracy_issues += 1
        
        # 정확성 이슈에 따른 점수 감소
        if accuracy_issues > 0:
            score *= (1.0 - accuracy_issues * 0.2)
        
        return max(0.3, score)
    
    def _calculate_practicality_score(self, text: str) -> float:
        """실용성 점수를 계산합니다."""
        score = 1.0
        
        # 실용적인 표현 검사
        practical_keywords = [
            '예제', '사용법', '방법', '단계', '팁', '주의', '참고',
            'example', 'usage', 'method', 'step', 'tip', 'note', 'reference'
        ]
        
        practical_count = sum(1 for keyword in practical_keywords if keyword.lower() in text.lower())
        
        # 실용성 점수 계산
        if len(text.split()) > 0:
            practical_ratio = practical_count / len(text.split())
            score = min(1.0, 0.6 + practical_ratio * 0.4)
        
        # 추상적인 표현 검사
        abstract_patterns = [
            r'일반적으로',
            r'보통',
            r'대부분',
            r'일반적으로 말하면',
            r'generally',
            r'usually',
            r'typically'
        ]
        
        abstract_count = sum(1 for pattern in abstract_patterns if re.search(pattern, text, re.IGNORECASE))
        if abstract_count > 2:
            score *= 0.8
        
        return max(0.3, score)
    
    def _calculate_weighted_score(self, scores: Dict[str, float]) -> float:
        """가중치 적용 점수를 계산합니다."""
        weighted_score = 0.0
        
        if 'content' in scores:
            weighted_score += scores['content'] * self.config.content_weight
        
        if 'structural' in scores:
            weighted_score += scores['structural'] * self.config.structural_weight
        
        if 'language' in scores:
            weighted_score += scores['language'] * self.config.language_weight
        
        if 'technical' in scores:
            weighted_score += scores['technical'] * self.config.technical_weight
        
        return weighted_score
    
    def _generate_quality_issues(self, result: QualityScoreResult, scores: Dict[str, float]):
        """품질 이슈를 생성합니다."""
        issues = []
        warnings = []
        suggestions = []
        
        # 전체 점수 기반 이슈
        if result.total_score < self.config.min_quality_threshold:
            issues.append(f"품질 점수가 너무 낮음 ({result.total_score:.2f})")
        elif result.total_score < self.config.excellent_quality_threshold:
            warnings.append(f"품질 점수가 개선될 여지가 있음 ({result.total_score:.2f})")
        
        # 각 요소별 이슈
        for score_type, score in scores.items():
            if score < 0.5:
                issues.append(f"{score_type} 품질이 매우 낮음 ({score:.2f})")
            elif score < 0.7:
                warnings.append(f"{score_type} 품질이 개선될 필요 있음 ({score:.2f})")
        
        # 구체적인 제안 생성
        if result.content_score < 0.7:
            suggestions.append("내용을 더 풍부하게 작성해주세요")
        
        if result.structural_score < 0.7:
            suggestions.append("구조를 더 명확하게 개선해주세요")
        
        if result.language_score < 0.7:
            suggestions.append("언어 표현을 더 자연스럽게 수정해주세요")
        
        if result.technical_score < 0.7:
            suggestions.append("기술적 내용을 더 정확하게 작성해주세요")
        
        # 결과에 추가
        result.issues.extend(issues)
        result.warnings.extend(warnings)
        result.suggestions.extend(suggestions)
    
    def _get_stop_words(self) -> Set[str]:
        """불용어 목록을 반환합니다."""
        return {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
            'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
            'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those',
            'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his',
            'her', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs'
        }
    
    def batch_calculate_scores(self, items: List[Dict[str, Any]], item_type: str = "text") -> List[QualityScoreResult]:
        """
        배치로 품질 점수를 계산합니다.
        
        Args:
            items: 품질 평가할 아이템 목록
            item_type: 아이템 타입
            
        Returns:
            품질 점수 계산 결과 목록
        """
        results = []
        
        for i, item in enumerate(items):
            try:
                result = self.calculate_quality_score(item, item_type)
                results.append(result)
                
                # 진행률 로깅
                if (i + 1) % 100 == 0:
                    self.logger.info(f"Processed {i + 1}/{len(items)} items")
                    
            except Exception as e:
                self.logger.error(f"Error calculating quality score for item {i}: {e}")
                # 오류 발생 시 기본 결과 반환
                error_result = QualityScoreResult()
                error_result.total_score = 0.0
                error_result.issues.append(f"처리 오류: {str(e)}")
                results.append(error_result)
        
        return results
    
    def get_quality_summary(self, results: List[QualityScoreResult]) -> Dict[str, Any]:
        """품질 요약 정보를 생성합니다."""
        if not results:
            return {"total": 0, "average_score": 0.0}
        
        total = len(results)
        average_score = sum(r.total_score for r in results) / total
        
        # 품질 등급별 통계
        quality_grades = {
            "excellent": sum(1 for r in results if r.total_score >= self.config.excellent_quality_threshold),
            "good": sum(1 for r in results if self.config.min_quality_threshold <= r.total_score < self.config.excellent_quality_threshold),
            "poor": sum(1 for r in results if r.total_score < self.config.min_quality_threshold)
        }
        
        # 각 요소별 평균 점수
        avg_content_score = sum(r.content_score for r in results) / total
        avg_structural_score = sum(r.structural_score for r in results) / total
        avg_language_score = sum(r.language_score for r in results) / total
        avg_technical_score = sum(r.technical_score for r in results) / total
        
        return {
            "total": total,
            "average_score": average_score,
            "quality_grades": quality_grades,
            "average_content_score": avg_content_score,
            "average_structural_score": avg_structural_score,
            "average_language_score": avg_language_score,
            "average_technical_score": avg_technical_score,
            "issues_count": sum(len(r.issues) for r in results),
            "warnings_count": sum(len(r.warnings) for r in results),
            "suggestions_count": sum(len(r.suggestions) for r in results),
            "timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    # 테스트 데이터
    test_items = [
        {
            "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
            "response": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가\n2. DataGrid 컨트롤 폼에 배치\n3. 데이터 소스 설정\n4. 컬럼 구성\n5. 스타일 적용",
            "conversations": [
                {"from": "system", "value": "Syncfusion WinForms 전문가"},
                {"from": "human", "value": "DataGrid 사용법을 알려주세요."},
                {"from": "gpt", "value": "DataGrid 사용법은 다음과 같습니다..."}
            ]
        },
        {
            "instruction": "Chart 컴포넌트로 막대 그래프를 만드는 방법",
            "response": "Chart 컴포넌트 막대 그래프 생성 방법:\n1. Chart 컨트롤 추가\n2. Series 설정\n3. 데이터 바인딩\n4. 축 설정\n5. 범례 추가",
            "conversations": [
                {"from": "system", "value": "Syncfusion WinForms 전문가"},
                {"from": "human", "value": "막대 그래프 만드는 방법이 궁금합니다."},
                {"from": "gpt", "value": "막대 그래프를 만드는 방법은 다음과 같습니다..."}
            ]
        },
        {
            "instruction": "간단한 테스트",
            "response": "간단한 답변",
            "conversations": [
                {"from": "system", "value": "전문가"},
                {"from": "human", "value": "테스트"},
                {"from": "gpt", "value": "답변"}
            ]
        }
    ]
    
    # 품질 점수 계산기 생성
    quality_scorer = QualityScorer()
    
    print("=== Quality Scorer Test ===")
    
    # 개별 아이템 품질 평가 테스트
    for i, item in enumerate(test_items):
        print(f"\nItem {i + 1}:")
        result = quality_scorer.calculate_quality_score(item, "conversation")
        print(f"  Total Score: {result.total_score:.2f}")
        print(f"  Content Score: {result.content_score:.2f}")
        print(f"  Structural Score: {result.structural_score:.2f}")
        print(f"  Language Score: {result.language_score:.2f}")
        print(f"  Technical Score: {result.technical_score:.2f}")
        print(f"  Issues: {result.issues}")
        print(f"  Warnings: {result.warnings}")
        print(f"  Suggestions: {result.suggestions}")
    
    # 배치 품질 평가 테스트
    print(f"\n=== Batch Quality Scoring Test ===")
    batch_results = quality_scorer.batch_calculate_scores(test_items, "conversation")
    summary = quality_scorer.get_quality_summary(batch_results)
    
    print(f"Total Items: {summary['total']}")
    print(f"Average Score: {summary['average_score']:.2f}")
    print(f"Excellent: {summary['quality_grades']['excellent']}")
    print(f"Good: {summary['quality_grades']['good']}")
    print(f"Poor: {summary['quality_grades']['poor']}")
    print(f"Average Content Score: {summary['average_content_score']:.2f}")
    print(f"Average Structural Score: {summary['average_structural_score']:.2f}")
    print(f"Average Language Score: {summary['average_language_score']:.2f}")
    print(f"Average Technical Score: {summary['average_technical_score']:.2f}")
    print(f"Issues: {summary['issues_count']}")
    print(f"Warnings: {summary['warnings_count']}")
    print(f"Suggestions: {summary['suggestions_count']}")