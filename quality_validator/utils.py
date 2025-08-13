#!/usr/bin/env python3
"""
유틸리티 모듈
품질 검증 및 필터링 시스템에서 사용하는 공통 유틸리티 함수들을 제공합니다.
"""

import re
import json
import logging
import hashlib
import math
import unicodedata
from typing import List, Dict, Any, Optional, Set, Tuple, Union, Callable
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class UtilsConfig:
    """유틸리티 설정"""
    # 텍스트 처리 설정
    text_normalization_enabled: bool = True
    remove_extra_whitespace: bool = True
    normalize_unicode: bool = True
    preserve_code_blocks: bool = True
    
    # 해시 설정
    hash_algorithm: str = "md5"
    hash_chunk_size: int = 8192
    
    # 유사도 계산 설정
    similarity_threshold: float = 0.9
    similarity_method: str = "cosine"  # cosine, jaccard, euclidean
    
    # 토큰화 설정
    token_method: str = "simple"  # simple, word, sentence
    min_token_length: int = 1
    max_token_length: int = 100
    
    # 파일 처리 설정
    file_encoding: str = "utf-8"
    file_chunk_size: int = 65536
    
    # 로깅 설정
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class TextUtils:
    """텍스트 처리 유틸리티"""
    
    def __init__(self, config: Optional[UtilsConfig] = None):
        """텍스트 유틸리티를 초기화합니다."""
        self.config = config or UtilsConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 정규화 패턴
        self.normalization_patterns = {
            'whitespace': re.compile(r'\s+'),
            'punctuation': re.compile(r'[^\w\s]'),
            'html_tags': re.compile(r'<[^>]+>'),
            'urls': re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
            'emails': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'code_blocks': re.compile(r'```[\s\S]*?```'),
            'inline_code': re.compile(r'`[^`]+`')
        }
        
        # 언어별 패턴
        self.language_patterns = {
            'korean': re.compile(r'[가-힣]'),
            'english': re.compile(r'[a-zA-Z]'),
            'numbers': re.compile(r'\d+'),
            'special_chars': re.compile(r'[^\w\s]')
        }
    
    def normalize_text(self, text: str) -> str:
        """텍스트를 정규화합니다."""
        if not text:
            return ""
        
        # 유니코드 정규화
        if self.config.normalize_unicode:
            text = unicodedata.normalize('NFKC', text)
        
        # 추가 공백 제거
        if self.config.remove_extra_whitespace:
            text = self.normalization_patterns['whitespace'].sub(' ', text)
        
        # HTML 태그 제거
        text = self.normalization_patterns['html_tags'].sub('', text)
        
        # URL 제거
        text = self.normalization_patterns['urls'].sub('[URL]', text)
        
        # 이메일 제거
        text = self.normalization_patterns['emails'].sub('[EMAIL]', text)
        
        # 양쪽 공백 제거
        text = text.strip()
        
        return text
    
    def extract_text_features(self, text: str) -> Dict[str, Any]:
        """텍스트 특징을 추출합니다."""
        if not text:
            return {}
        
        features = {}
        
        # 기본 통계
        features['length'] = len(text)
        features['word_count'] = len(text.split())
        features['sentence_count'] = len(self.normalization_patterns['punctuation'].split(text))
        features['paragraph_count'] = text.count('\n\n') + 1
        
        # 언어별 문자 수
        features['korean_chars'] = len(self.language_patterns['korean'].findall(text))
        features['english_chars'] = len(self.language_patterns['english'].findall(text))
        features['numbers'] = len(self.language_patterns['numbers'].findall(text))
        features['special_chars'] = len(self.language_patterns['special_chars'].findall(text))
        
        # 코드 블록 수
        features['code_blocks'] = len(self.normalization_patterns['code_blocks'].findall(text))
        features['inline_code'] = len(self.normalization_patterns['inline_code'].findall(text))
        
        # URL 및 이메일 수
        features['urls'] = len(self.normalization_patterns['urls'].findall(text))
        features['emails'] = len(self.normalization_patterns['emails'].findall(text))
        
        return features
    
    def tokenize_text(self, text: str, method: str = None) -> List[str]:
        """텍스트를 토큰화합니다."""
        if not text:
            return []
        
        method = method or self.config.token_method
        
        if method == "simple":
            # 간단한 단어 토큰화
            tokens = text.split()
        elif method == "word":
            # 단어 단위 토큰화 (구두문 포함)
            tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
        elif method == "sentence":
            # 문장 단위 토큰화
            tokens = re.split(r'[.!?]+', text)
        else:
            tokens = text.split()
        
        # 토큰 필터링
        tokens = [
            token.strip() for token in tokens
            if len(token.strip()) >= self.config.min_token_length
            and len(token.strip()) <= self.config.max_token_length
        ]
        
        return tokens
    
    def calculate_text_similarity(self, text1: str, text2: str, method: str = None) -> float:
        """두 텍스트 간의 유사도를 계산합니다."""
        method = method or self.config.similarity_method
        
        # 텍스트 정규화
        text1_norm = self.normalize_text(text1)
        text2_norm = self.normalize_text(text2)
        
        if method == "cosine":
            return self._calculate_cosine_similarity(text1_norm, text2_norm)
        elif method == "jaccard":
            return self._calculate_jaccard_similarity(text1_norm, text2_norm)
        elif method == "euclidean":
            return self._calculate_euclidean_similarity(text1_norm, text2_norm)
        else:
            return 0.0
    
    def _calculate_cosine_similarity(self, text1: str, text2: str) -> float:
        """코사인 유사도를 계산합니다."""
        # 단어 빈도 계산
        words1 = self.tokenize_text(text1)
        words2 = self.tokenize_text(text2)
        
        if not words1 or not words2:
            return 0.0
        
        # 단어 집합 생성
        all_words = set(words1) | set(words2)
        
        # 벡터 생성
        vec1 = [words1.count(word) for word in all_words]
        vec2 = [words2.count(word) for word in all_words]
        
        # 코사인 유사도 계산
        dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(v * v for v in vec1))
        magnitude2 = math.sqrt(sum(v * v for v in vec2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        
        return dot_product / (magnitude1 * magnitude2)
    
    def _calculate_jaccard_similarity(self, text1: str, text2: str) -> float:
        """자카드 유사도를 계산합니다."""
        # 단어 집합 생성
        words1 = set(self.tokenize_text(text1))
        words2 = set(self.tokenize_text(text2))
        
        if not words1 and not words2:
            return 1.0
        if not words1 or not words2:
            return 0.0
        
        # 자카드 유사도 계산
        intersection = len(words1 & words2)
        union = len(words1 | words2)
        
        return intersection / union
    
    def _calculate_euclidean_similarity(self, text1: str, text2: str) -> float:
        """유클리드 거리 기반 유사도를 계산합니다."""
        # 단어 빈도 계산
        words1 = self.tokenize_text(text1)
        words2 = self.tokenize_text(text2)
        
        if not words1 or not words2:
            return 0.0
        
        # 단어 집합 생성
        all_words = set(words1) | set(words2)
        
        # 벡터 생성
        vec1 = [words1.count(word) for word in all_words]
        vec2 = [words2.count(word) for word in all_words]
        
        # 유클리드 거리 계산
        distance = math.sqrt(sum((v1 - v2) ** 2 for v1, v2 in zip(vec1, vec2)))
        
        # 거리를 유사도로 변환
        max_distance = math.sqrt(len(all_words) * max(max(vec1), max(vec2)) ** 2)
        similarity = 1.0 - (distance / max_distance) if max_distance > 0 else 0.0
        
        return similarity


class HashUtils:
    """해시 유틸리티"""
    
    def __init__(self, config: Optional[UtilsConfig] = None):
        """해시 유틸리티를 초기화합니다."""
        self.config = config or UtilsConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    def calculate_text_hash(self, text: str, algorithm: str = None) -> str:
        """텍스트의 해시를 계산합니다."""
        algorithm = algorithm or self.config.hash_algorithm
        
        # 인코딩
        text_bytes = text.encode(self.config.file_encoding)
        
        # 해시 계산
        if algorithm == "md5":
            return hashlib.md5(text_bytes).hexdigest()
        elif algorithm == "sha1":
            return hashlib.sha1(text_bytes).hexdigest()
        elif algorithm == "sha256":
            return hashlib.sha256(text_bytes).hexdigest()
        elif algorithm == "sha512":
            return hashlib.sha512(text_bytes).hexdigest()
        else:
            return hashlib.md5(text_bytes).hexdigest()
    
    def calculate_file_hash(self, file_path: str, algorithm: str = None) -> str:
        """파일의 해시를 계산합니다."""
        algorithm = algorithm or self.config.hash_algorithm
        
        try:
            hash_obj = hashlib.new(algorithm)
            
            with open(file_path, 'rb') as f:
                while chunk := f.read(self.config.hash_chunk_size):
                    hash_obj.update(chunk)
            
            return hash_obj.hexdigest()
        
        except Exception as e:
            self.logger.error(f"Error calculating file hash for {file_path}: {e}")
            return ""
    
    def calculate_similarity_hash(self, text: str) -> str:
        """유사도 비교를 위한 해시를 계산합니다."""
        # 텍스트 정규화
        normalized_text = text.lower().strip()
        
        # 불필요한 문자 제거
        normalized_text = re.sub(r'[^\w\s]', '', normalized_text)
        
        # 공백 정규화
        normalized_text = re.sub(r'\s+', ' ', normalized_text)
        
        return self.calculate_text_hash(normalized_text, "md5")
    
    def find_duplicate_hashes(self, items: List[Dict[str, Any]], hash_field: str = "content") -> Dict[str, List[int]]:
        """중복 해시를 찾습니다."""
        hash_map = defaultdict(list)
        
        for i, item in enumerate(items):
            if hash_field in item:
                content = str(item[hash_field])
                hash_value = self.calculate_similarity_hash(content)
                hash_map[hash_value].append(i)
        
        # 중복 항목만 필터링
        duplicates = {hash_val: indices for hash_val, indices in hash_map.items() if len(indices) > 1}
        
        return duplicates


class FileUtils:
    """파일 처리 유틸리티"""
    
    def __init__(self, config: Optional[UtilsConfig] = None):
        """파일 유틸리티를 초기화합니다."""
        self.config = config or UtilsConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    def read_file(self, file_path: str) -> str:
        """파일을 읽습니다."""
        try:
            with open(file_path, 'r', encoding=self.config.file_encoding) as f:
                return f.read()
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return ""
    
    def write_file(self, file_path: str, content: str) -> bool:
        """파일을 씁니다."""
        try:
            # 디렉토리 생성
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding=self.config.file_encoding) as f:
                f.write(content)
            
            return True
        except Exception as e:
            self.logger.error(f"Error writing file {file_path}: {e}")
            return False
    
    def read_json_file(self, file_path: str) -> Dict[str, Any]:
        """JSON 파일을 읽습니다."""
        try:
            with open(file_path, 'r', encoding=self.config.file_encoding) as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Error reading JSON file {file_path}: {e}")
            return {}
    
    def write_json_file(self, file_path: str, data: Dict[str, Any]) -> bool:
        """JSON 파일을 씁니다."""
        try:
            # 디렉토리 생성
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding=self.config.file_encoding) as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            self.logger.error(f"Error writing JSON file {file_path}: {e}")
            return False
    
    def read_jsonl_file(self, file_path: str) -> List[Dict[str, Any]]:
        """JSONL 파일을 읽습니다."""
        try:
            data = []
            with open(file_path, 'r', encoding=self.config.file_encoding) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        data.append(json.loads(line))
            return data
        except Exception as e:
            self.logger.error(f"Error reading JSONL file {file_path}: {e}")
            return []
    
    def write_jsonl_file(self, file_path: str, data: List[Dict[str, Any]]) -> bool:
        """JSONL 파일을 씁니다."""
        try:
            # 디렉토리 생성
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding=self.config.file_encoding) as f:
                for item in data:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
            
            return True
        except Exception as e:
            self.logger.error(f"Error writing JSONL file {file_path}: {e}")
            return False
    
    def get_file_info(self, file_path: str) -> Dict[str, Any]:
        """파일 정보를 가져옵니다."""
        try:
            path = Path(file_path)
            if not path.exists():
                return {}
            
            stat = path.stat()
            
            return {
                'path': str(path),
                'name': path.name,
                'size': stat.st_size,
                'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'extension': path.suffix,
                'is_file': path.is_file(),
                'is_dir': path.is_dir()
            }
        except Exception as e:
            self.logger.error(f"Error getting file info for {file_path}: {e}")
            return {}


class ValidationUtils:
    """검증 유틸리티"""
    
    def __init__(self, config: Optional[UtilsConfig] = None):
        """검증 유틸리티를 초기화합니다."""
        self.config = config or UtilsConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    def validate_token_range(self, text: str, min_tokens: int = None, max_tokens: int = None) -> Dict[str, Any]:
        """토큰 범위를 검증합니다."""
        min_tokens = min_tokens or self.config.min_token_length
        max_tokens = max_tokens or self.config.max_token_length
        
        # 토큰 수 계산
        tokens = text.split()
        token_count = len(tokens)
        
        result = {
            'is_valid': min_tokens <= token_count <= max_tokens,
            'token_count': token_count,
            'min_tokens': min_tokens,
            'max_tokens': max_tokens,
            'status': 'valid'
        }
        
        if token_count < min_tokens:
            result['status'] = 'too_short'
            result['message'] = f"토큰 수가 너무 적음: {token_count} < {min_tokens}"
        elif token_count > max_tokens:
            result['status'] = 'too_long'
            result['message'] = f"토큰 수가 너김: {token_count} > {max_tokens}"
        
        return result
    
    def validate_text_quality(self, text: str) -> Dict[str, Any]:
        """텍스트 품질을 검증합니다."""
        if not text:
            return {
                'is_valid': False,
                'score': 0.0,
                'issues': ['empty_text'],
                'warnings': []
            }
        
        issues = []
        warnings = []
        score = 1.0
        
        # 길이 검증
        if len(text) < 10:
            issues.append('text_too_short')
            score *= 0.5
        elif len(text) > 20000:
            warnings.append('text_too_long')
            score *= 0.9
        
        # 구두문 검증
        if text.count('..') > 0:
            issues.append('double_punctuation')
            score *= 0.8
        
        # 공백 검증
        if '  ' in text:
            warnings.append('extra_whitespace')
            score *= 0.95
        
        # 문장 끝 검증
        if not text.rstrip().endswith(('.', '!', '?')):
            warnings.append('missing_sentence_end')
            score *= 0.9
        
        # 최종 점수 계산
        final_score = max(0.0, min(1.0, score))
        
        return {
            'is_valid': len(issues) == 0,
            'score': final_score,
            'issues': issues,
            'warnings': warnings
        }
    
    def validate_conversation_structure(self, conversations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """대화 구조를 검증합니다."""
        if not conversations:
            return {
                'is_valid': False,
                'issues': ['empty_conversations'],
                'warnings': []
            }
        
        issues = []
        warnings = []
        score = 1.0
        
        # 필수 역할 검증
        required_roles = {'system', 'human', 'gpt'}
        present_roles = {conv.get('from', '') for conv in conversations}
        
        missing_roles = required_roles - present_roles
        if missing_roles:
            issues.append(f'missing_roles: {missing_roles}')
            score *= 0.7
        
        # 역할 순서 검증
        expected_sequence = ['system', 'human', 'gpt']
        actual_sequence = [conv.get('from', '') for conv in conversations]
        
        for i, (expected, actual) in enumerate(zip(expected_sequence, actual_sequence)):
            if expected != actual:
                warnings.append(f'sequence_mismatch: expected {expected}, got {actual}')
                score *= 0.95
        
        # 중복 역할 검증
        role_counts = Counter(actual_sequence)
        duplicate_roles = [role for role, count in role_counts.items() if count > 1]
        if duplicate_roles:
            warnings.append(f'duplicate_roles: {duplicate_roles}')
            score *= 0.9
        
        # 필드 검증
        for i, conv in enumerate(conversations):
            if 'from' not in conv:
                issues.append(f'missing_from_field: turn {i}')
                score *= 0.5
            
            if 'value' not in conv:
                issues.append(f'missing_value_field: turn {i}')
                score *= 0.5
            
            if not conv.get('value', '').strip():
                issues.append(f'empty_value: turn {i}')
                score *= 0.5
        
        # 최종 점수 계산
        final_score = max(0.0, min(1.0, score))
        
        return {
            'is_valid': len(issues) == 0,
            'score': final_score,
            'issues': issues,
            'warnings': warnings,
            'total_turns': len(conversations),
            'present_roles': list(present_roles),
            'duplicate_roles': duplicate_roles
        }


class ProgressUtils:
    """진행률 유틸리티"""
    
    def __init__(self, config: Optional[UtilsConfig] = None):
        """진행률 유틸리티를 초기화합니다."""
        self.config = config or UtilsConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    def create_progress_callback(self, total: int, description: str = "Processing") -> Callable[[int], None]:
        """진행률 콜백을 생성합니다."""
        import sys
        
        def progress_callback(current: int):
            if total == 0:
                return
            
            percentage = (current / total) * 100
            bar_length = 50
            filled_length = int(bar_length * current // total)
            
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            
            sys.stdout.write(f'\r{description}: |{bar}| {percentage:.1f}% ({current}/{total})')
            sys.stdout.flush()
            
            if current == total:
                print()  # 줄바꿈
        
        return progress_callback
    
    def log_progress(self, current: int, total: int, message: str = None):
        """진행률을 로깅합니다."""
        if total == 0:
            return
        
        percentage = (current / total) * 100
        
        if message:
            self.logger.info(f"{message}: {current}/{total} ({percentage:.1f}%)")
        else:
            self.logger.info(f"Progress: {current}/{total} ({percentage:.1f}%)")


class LoggingUtils:
    """로깅 유틸리티"""
    
    def __init__(self, config: Optional[UtilsConfig] = None):
        """로깅 유틸리티를 초기화합니다."""
        self.config = config or UtilsConfig()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # 로거 설정
        self._setup_logging()
    
    def _setup_logging(self):
        """로깅을 설정합니다."""
        # 로거 생성
        logger = logging.getLogger('quality_validator')
        logger.setLevel(getattr(logging, self.config.log_level))
        
        # 핸들러 생성
        if not logger.handlers:
            # 콘솔 핸들러
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            
            # 포맷터
            formatter = logging.Formatter(self.config.log_format)
            console_handler.setFormatter(formatter)
            
            # 핸들러 추가
            logger.addHandler(console_handler)
    
    def get_logger(self, name: str = None) -> logging.Logger:
        """로거를 가져옵니다."""
        if name:
            return logging.getLogger(f'quality_validator.{name}')
        return logging.getLogger('quality_validator')


# 전역 유틸리티 인스턴스
_text_utils = TextUtils()
_hash_utils = HashUtils()
_file_utils = FileUtils()
_validation_utils = ValidationUtils()
_progress_utils = ProgressUtils()
_logging_utils = LoggingUtils()


def setup_logging(level: str = "INFO") -> logging.Logger:
    """로깅을 설정합니다."""
    return _logging_utils.get_logger()


def normalize_text(text: str) -> str:
    """텍스트를 정규화합니다."""
    return _text_utils.normalize_text(text)


def calculate_similarity(text1: str, text2: str, method: str = None) -> float:
    """두 텍스트 간의 유사도를 계산합니다."""
    return _text_utils.calculate_text_similarity(text1, text2, method)


def calculate_hash(text: str, algorithm: str = None) -> str:
    """텍스트의 해시를 계산합니다."""
    return _hash_utils.calculate_text_hash(text, algorithm)


def find_duplicates(items: List[Dict[str, Any]], hash_field: str = "content") -> Dict[str, List[int]]:
    """중복 항목을 찾습니다."""
    return _hash_utils.find_duplicate_hashes(items, hash_field)


def validate_token_range(text: str, min_tokens: int = None, max_tokens: int = None) -> Dict[str, Any]:
    """토큰 범위를 검증합니다."""
    return _validation_utils.validate_token_range(text, min_tokens, max_tokens)


def validate_text_quality(text: str) -> Dict[str, Any]:
    """텍스트 품질을 검증합니다."""
    return _validation_utils.validate_text_quality(text)


def create_progress_callback(total: int, description: str = "Processing") -> Callable[[int], None]:
    """진행률 콜백을 생성합니다."""
    return _progress_utils.create_progress_callback(total, description)


def log_progress(current: int, total: int, message: str = None):
    """진행률을 로깅합니다."""
    _progress_utils.log_progress(current, total, message)


if __name__ == "__main__":
    # 테스트 데이터
    test_texts = [
        "  여러   공백과\n특수문자!@#   포함된  텍스트  ",
        "간단한 테스트 문장입니다.",
        "이것은 또 다른 테스트 문장입니다.",
        "간단한 테스트 문장입니다.",  # 중복
        "DataGrid 사용법은 다음과 같습니다...",
        "Chart 컴포넌트 사용법은 다음과 같습니다..."
    ]
    
    print("=== Utils Test ===")
    
    # 텍스트 정규화 테스트
    print("\n1. Text Normalization Test:")
    for i, text in enumerate(test_texts):
        normalized = normalize_text(text)
        print(f"  Text {i+1}: '{text}' -> '{normalized}'")
    
    # 유사도 계산 테스트
    print("\n2. Similarity Calculation Test:")
    text1 = "간단한 테스트 문장입니다."
    text2 = "이것은 간단한 테스트 문장입니다."
    text3 = "완전히 다른 내용의 문장입니다."
    
    similarity_12 = calculate_similarity(text1, text2)
    similarity_13 = calculate_similarity(text1, text3)
    
    print(f"  Similarity between '{text1}' and '{text2}': {similarity_12:.3f}")
    print(f"  Similarity between '{text1}' and '{text3}': {similarity_13:.3f}")
    
    # 해시 계산 테스트
    print("\n3. Hash Calculation Test:")
    for i, text in enumerate(test_texts):
        hash_value = calculate_hash(text)
        print(f"  Text {i+1}: '{text}' -> {hash_value}")
    
    # 중복 찾기 테스트
    print("\n4. Duplicate Detection Test:")
    duplicates = find_duplicates([{"content": text} for text in test_texts])
    print(f"  Duplicates found: {duplicates}")
    
    # 토큰 범위 검증 테스트
    print("\n5. Token Range Validation Test:")
    test_tokens = [
        "Short text",
        "This is a medium length text with several words.",
        "This is a very long text with many words that exceeds the typical token limit and should be flagged as too long for most natural language processing applications and machine learning models."
    ]
    
    for i, text in enumerate(test_tokens):
        validation = validate_token_range(text, min_tokens=3, max_tokens=20)
        print(f"  Text {i+1}: {validation}")
    
    # 텍스트 품질 검증 테스트
    print("\n6. Text Quality Validation Test:")
    quality_texts = [
        "Good quality text with proper punctuation.",
        "Bad quality text with double punctuation..",
        "",
        "   ",
        "Short.",
        "This is a very long text with many words that might be considered too long for some applications but is actually quite reasonable for most natural language processing tasks."
    ]
    
    for i, text in enumerate(quality_texts):
        quality = validate_text_quality(text)
        print(f"  Text {i+1}: {quality}")
    
    # 진행률 테스트
    print("\n7. Progress Test:")
    progress_callback = create_progress_callback(10, "Processing items")
    
    for i in range(11):
        progress_callback(i)
        # 실제 작업 시뮬레이션
        import time
        time.sleep(0.1)