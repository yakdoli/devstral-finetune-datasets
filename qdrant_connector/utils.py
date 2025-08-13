#!/usr/bin/env python3
"""
Qdrant 연동 모듈 유틸리티
공통 유틸리티 함수와 헬퍼 함수들을 제공합니다.
"""

import os
import re
import json
import logging
import time
from typing import List, Dict, Any, Optional, Union, Tuple
from pathlib import Path
from datetime import datetime
import hashlib
import unicodedata

logger = logging.getLogger(__name__)


def setup_logging(level: str = "INFO", log_file: Optional[str] = None) -> logging.Logger:
    """
    로깅 설정을 초기화합니다.
    
    Args:
        level: 로깅 레벨
        log_file: 로그 파일 경로 (선택적)
        
    Returns:
        설정된 로거
    """
    log_level = getattr(logging, level.upper(), logging.INFO)
    
    # 포매터 설정
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 핸들러 설정
    handlers = [logging.StreamHandler()]
    
    if log_file:
        # 로그 파일 디렉토리 생성
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file, encoding='utf-8'))
    
    # 로거 설정
    logging.basicConfig(
        level=log_level,
        handlers=handlers,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    return logging.getLogger(__name__)


def normalize_text(text: str) -> str:
    """
    텍스트를 정규화합니다.
    
    Args:
        text: 정규화할 텍스트
        
    Returns:
        정규화된 텍스트
    """
    if not text:
        return ""
    
    # 유니코드 정규화
    text = unicodedata.normalize('NFKC', text)
    
    # 여러 공백을 단일 공백으로 변경
    text = re.sub(r'\s+', ' ', text)
    
    # 줄바꿈 정리
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # 양 끝 공백 제거
    text = text.strip()
    
    return text


def clean_filename(filename: str) -> str:
    """
    파일명에서 특수 문자를 제거합니다.
    
    Args:
        filename: 정리할 파일명
        
    Returns:
        정리된 파일명
    """
    # 허용되지 않는 문자 제거
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    
    # 공백을 언더스코어로 변경
    filename = re.sub(r'\s+', '_', filename)
    
    # 점 여러 개는 하나로 변경
    filename = re.sub(r'\.+', '.', filename)
    
    # 양 끝 점 제거
    filename = filename.strip('.')
    
    # 빈 파일명 처리
    if not filename:
        filename = "unnamed"
    
    return filename


def generate_unique_id(content: str, prefix: str = "doc") -> str:
    """
    고유 ID를 생성합니다.
    
    Args:
        content: ID 생성에 사용할 콘텐츠
        prefix: ID 접두사
        
    Returns:
        고유 ID
    """
    content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()[:8]
    return f"{prefix}_{content_hash}"


def extract_keywords_from_text(text: str, max_keywords: int = 10) -> List[str]:
    """
    텍스트에서 키워드를 추출합니다.
    
    Args:
        text: 키워드를 추출할 텍스트
        max_keywords: 최대 키워드 수
        
    Returns:
        키워드 목록
    """
    if not text:
        return []
    
    # 간단한 키워드 추출 (명사, 형용사 추출)
    words = re.findall(r'\b\w+\b', text.lower())
    
    # 불용어 제거
    stop_words = {
        'the', 'is', 'at', 'which', 'on', 'a', 'an', 'and', 'or', 'but', 'in', 'with',
        'to', 'for', 'of', 'as', 'by', 'from', 'up', 'about', 'into', 'through',
        'during', 'before', 'after', 'above', 'below', 'from', 'to', 'up', 'down',
        'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
        'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
        'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only',
        'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just',
        'don', 'should', 'now', 'this', 'that', 'these', 'those', 'am', 'are', 'was',
        'were', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
        'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
        'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
        'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
        'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
        'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
        'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
        'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
        'will', 'just', 'don', 'should', 'now'
    }
    
    # 단어 빈도 계산
    word_freq = {}
    for word in words:
        if len(word) > 2 and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # 빈도수 기준 정렬
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # 상위 키워드 반환
    keywords = [word for word, freq in sorted_words[:max_keywords]]
    
    return keywords


def calculate_content_quality(content: str) -> float:
    """
    콘텐츠 품질 점수를 계산합니다.
    
    Args:
        content: 품질을 평가할 콘텐츠
        
    Returns:
        품질 점수 (0.0-1.0)
    """
    if not content:
        return 0.0
    
    score = 1.0
    
    # 길이 점수 (100자 이상, 10000자 이하가 최적)
    content_length = len(content)
    if content_length < 100:
        score *= 0.5
    elif content_length > 10000:
        score *= 0.7
    else:
        score *= min(1.0, content_length / 1000)
    
    # 문장 구조 점수
    sentences = re.split(r'[.!?]+', content)
    sentence_count = len([s for s in sentences if s.strip()])
    
    if sentence_count == 0:
        score *= 0.1
    elif sentence_count < 3:
        score *= 0.5
    else:
        score *= min(1.0, sentence_count / 10)
    
    # 단어 다양성 점수
    words = re.findall(r'\b\w+\b', content.lower())
    unique_words = set(words)
    
    if len(words) == 0:
        score *= 0.1
    else:
        diversity = len(unique_words) / len(words)
        score *= diversity
    
    # 구조적 요소 점수
    has_headers = len(re.findall(r'^#+\s+', content, re.MULTILINE)) > 0
    has_lists = len(re.findall(r'^\s*[-*+]\s+', content, re.MULTILINE)) > 0
    has_code = len(re.findall(r'```', content)) > 0
    
    structure_score = 0.0
    if has_headers:
        structure_score += 0.3
    if has_lists:
        structure_score += 0.3
    if has_code:
        structure_score += 0.4
    
    score *= (0.5 + 0.5 * structure_score)
    
    return min(1.0, max(0.0, score))


def merge_document_sources(
    local_documents: List[Dict[str, Any]],
    qdrant_documents: List[Dict[str, Any]],
    strategy: str = "append"
) -> List[Dict[str, Any]]:
    """
    로컬 문서와 Qdrant 문서를 병합합니다.
    
    Args:
        local_documents: 로컬 문서 목록
        qdrant_documents: Qdrant 문서 목록
        strategy: 병합 전략 ("append", "interleave", "prioritize_local")
        
    Returns:
        병합된 문서 목록
    """
    if strategy == "append":
        # 단순히 이어 붙이기
        return local_documents + qdrant_documents
    
    elif strategy == "interleave":
        # 교차 배치
        merged = []
        max_len = max(len(local_documents), len(qdrant_documents))
        
        for i in range(max_len):
            if i < len(local_documents):
                merged.append(local_documents[i])
            if i < len(qdrant_documents):
                merged.append(qdrant_documents[i])
        
        return merged
    
    elif strategy == "prioritize_local":
        # 로컬 문서 우선
        merged = local_documents.copy()
        
        # Qdrant 문서 중 로컬에 없는 것만 추가
        local_ids = {doc["id"] for doc in local_documents}
        
        for qdrant_doc in qdrant_documents:
            if qdrant_doc["id"] not in local_ids:
                merged.append(qdrant_doc)
        
        return merged
    
    else:
        # 기본적으로 append
        return local_documents + qdrant_documents


def save_documents_to_json(
    documents: List[Dict[str, Any]],
    output_path: Union[str, Path],
    indent: int = 2,
    ensure_ascii: bool = False
) -> bool:
    """
    문서를 JSON 파일로 저장합니다.
    
    Args:
        documents: 저장할 문서 목록
        output_path: 출력 파일 경로
        indent: JSON 들여쓰기
        ensure_ascii: ASCII 문자 보장 여부
        
    Returns:
        저장 성공 여부
    """
    try:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(documents, f, indent=indent, ensure_ascii=ensure_ascii)
        
        logger.info(f"Saved {len(documents)} documents to {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to save documents to {output_path}: {e}")
        return False


def load_documents_from_json(input_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    JSON 파일에서 문서를 불러옵니다.
    
    Args:
        input_path: 입력 파일 경로
        
    Returns:
        불러온 문서 목록
    """
    try:
        input_path = Path(input_path)
        
        if not input_path.exists():
            logger.warning(f"File not found: {input_path}")
            return []
        
        with open(input_path, 'r', encoding='utf-8') as f:
            documents = json.load(f)
        
        # 단일 문서인 경우 리스트로 변환
        if isinstance(documents, dict):
            documents = [documents]
        
        logger.info(f"Loaded {len(documents)} documents from {input_path}")
        return documents
        
    except Exception as e:
        logger.error(f"Failed to load documents from {input_path}: {e}")
        return []


def create_qdrant_filter_from_dict(filter_dict: Dict[str, Any]) -> Any:
    """
    딕셔너리를 Qdrant 필터 형식으로 변환합니다.
    
    Args:
        filter_dict: 필터 딕셔너리
        
    Returns:
        Qdrant 필터 객체
    """
    from qdrant_client import models
    
    if not filter_dict:
        return None
    
    must_conditions = []
    
    for key, value in filter_dict.items():
        if isinstance(value, str):
            # 문자열 매칭
            must_conditions.append(
                models.FieldCondition(
                    key=key,
                    match=models.MatchText(text=value)
                )
            )
        elif isinstance(value, list):
            # 리스트 매칭
            must_conditions.append(
                models.FieldCondition(
                    key=key,
                    match=models.MatchAny(any=value)
                )
            )
        elif isinstance(value, (int, float)):
            # 숫자 정확한 매칭
            must_conditions.append(
                models.FieldCondition(
                    key=key,
                    match=models.MatchValue(value=value)
                )
            )
        elif isinstance(value, dict):
            # 복잡한 조건
            if "gte" in value or "lte" in value:
                range_params = {}
                if "gte" in value:
                    range_params["gte"] = value["gte"]
                if "lte" in value:
                    range_params["lte"] = value["lte"]
                if "gt" in value:
                    range_params["gt"] = value["gt"]
                if "lt" in value:
                    range_params["lt"] = value["lt"]
                
                must_conditions.append(
                    models.FieldCondition(
                        key=key,
                        range=models.Range(**range_params)
                    )
                )
            elif "match" in value:
                must_conditions.append(
                    models.FieldCondition(
                        key=key,
                        match=models.MatchText(text=value["match"])
                    )
                )
            elif "must" in value:
                # 중첩된 조건
                nested_filter = create_qdrant_filter_from_dict(value["must"])
                if nested_filter:
                    must_conditions.append(nested_filter)
    
    if must_conditions:
        return models.Filter(must=must_conditions)
    return None


def validate_qdrant_connection_config(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Qdrant 연결 설정을 검증합니다.
    
    Args:
        config: 연결 설정 딕셔너리
        
    Returns:
        (유효성 여부, 오류 목록)
    """
    errors = []
    
    # 필수 필드 검증
    required_fields = ["host", "port", "collection_name"]
    for field in required_fields:
        if field not in config:
            errors.append(f"Missing required field: {field}")
    
    # 포트 형식 검증
    if "port" in config:
        try:
            port = int(config["port"])
            if not (1 <= port <= 65535):
                errors.append("Port must be between 1 and 65535")
        except (ValueError, TypeError):
            errors.append("Port must be a number")
    
    # 컬렉션 이름 검증
    if "collection_name" in config:
        collection_name = config["collection_name"]
        if not isinstance(collection_name, str) or not collection_name.strip():
            errors.append("Collection name must be a non-empty string")
    
    return len(errors) == 0, errors


def get_environment_config() -> Dict[str, Any]:
    """
    환경변수에서 Qdrant 설정을 가져옵니다.
    
    Returns:
        환경변수 설정 딕셔너리
    """
    config = {
        "host": os.getenv("QDRANT_HOST", "100.100.88.88"),
        "port": int(os.getenv("QDRANT_PORT", "6333")),
        "api_key": os.getenv("QDRANT_API_KEY"),
        "collection_name": os.getenv("QDRANT_COLLECTION", "ws-7491d651ae044c78"),
        "timeout": int(os.getenv("QDRANT_TIMEOUT", "30")),
        "https": os.getenv("QDRANT_HTTPS", "false").lower() == "true",
        "prefer_grpc": os.getenv("QDRANT_PREFER_GRPC", "false").lower() == "true"
    }
    
    return config


def benchmark_search_performance(
    searcher,
    queries: List[str],
    iterations: int = 5
) -> Dict[str, Any]:
    """
    검색 성능을 벤치마크합니다.
    
    Args:
        searcher: 검색기 인스턴스
        queries: 벤치마크할 쿼리 목록
        iterations: 반복 횟수
        
    Returns:
        벤치마크 결과
    """
    results = {
        "queries": queries,
        "iterations": iterations,
        "total_searches": len(queries) * iterations,
        "results": []
    }
    
    for query in queries:
        query_results = {
            "query": query,
            "times": [],
            "avg_time": 0.0,
            "min_time": float('inf'),
            "max_time": 0.0
        }
        
        for i in range(iterations):
            start_time = time.time()
            
            try:
                search_results = searcher.search_documents(query, limit=10)
                end_time = time.time()
                
                execution_time = end_time - start_time
                query_results["times"].append(execution_time)
                
                query_results["min_time"] = min(query_results["min_time"], execution_time)
                query_results["max_time"] = max(query_results["max_time"], execution_time)
                
            except Exception as e:
                logger.error(f"Search failed for query '{query}': {e}")
                query_results["times"].append(float('inf'))
        
        # 평균 계산
        valid_times = [t for t in query_results["times"] if t != float('inf')]
        if valid_times:
            query_results["avg_time"] = sum(valid_times) / len(valid_times)
        
        results["results"].append(query_results)
    
    # 전체 통계 계산
    all_times = []
    for result in results["results"]:
        all_times.extend([t for t in result["times"] if t != float('inf')])
    
    if all_times:
        results["overall_avg"] = sum(all_times) / len(all_times)
        results["overall_min"] = min(all_times)
        results["overall_max"] = max(all_times)
    else:
        results["overall_avg"] = 0.0
        results["overall_min"] = 0.0
        results["overall_max"] = 0.0
    
    return results


if __name__ == "__main__":
    # 테스트 코드
    setup_logging("INFO")
    
    # 텍스트 정규화 테스트
    test_text = "  Hello   World  \n\n  Test  \n"
    normalized = normalize_text(test_text)
    print(f"정규화된 텍스트: '{normalized}'")
    
    # 키워드 추출 테스트
    test_content = """
    Syncfusion Grid 컴포넌트는 강력한 데이터 그리드 기능을 제공합니다.
    이 컴포넌트는 데이터 바인딩, 정렬, 필터링 등 다양한 기능을 지원합니다.
    """
    keywords = extract_keywords_from_text(test_content, max_keywords=5)
    print(f"추출된 키워드: {keywords}")
    
    # 품질 점수 계산 테스트
    quality_score = calculate_content_quality(test_content)
    print(f"콘텐츠 품질 점수: {quality_score:.2f}")
    
    # 고유 ID 생성 테스트
    unique_id = generate_unique_id(test_content)
    print(f"생성된 고유 ID: {unique_id}")
    
    # 환경 설정 테스트
    env_config = get_environment_config()
    print(f"환경 설정: {env_config}")