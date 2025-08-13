#!/usr/bin/env python3
"""
유틸리티 모듈
Unsloth 데이터셋 생성기에서 사용되는 공통 유틸리티 함수들을 제공합니다.
"""

import json
import logging
import hashlib
import uuid
import re
from typing import List, Dict, Any, Optional, Union, Set, Tuple
from pathlib import Path
from datetime import datetime
import asyncio
import aiofiles
from dataclasses import dataclass, asdict


logger = logging.getLogger(__name__)


@dataclass
class TextProcessingConfig:
    """텍스트 처리 설정"""
    normalize_whitespace: bool = True
    remove_special_chars: bool = True
    lowercase: bool = False
    remove_extra_newlines: bool = True
    max_length: Optional[int] = None
    min_length: Optional[int] = None
    allowed_chars: Optional[str] = None


def setup_logging(level: str = "INFO", log_file: Optional[str] = None) -> logging.Logger:
    """
    로깅을 설정합니다.
    
    Args:
        level: 로그 레벨
        log_file: 로그 파일 경로 (선택적)
        
    Returns:
        설정된 로거
    """
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {level}')
    
    # 로거 설정
    logger = logging.getLogger()
    logger.setLevel(numeric_level)
    
    # 기필터 제거
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # 포매터
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 파일 핸들러
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def normalize_text(text: str, config: Optional[TextProcessingConfig] = None) -> str:
    """
    텍스트를 정규화합니다.
    
    Args:
        text: 정규화할 텍스트
        config: 텍스트 처리 설정
        
    Returns:
        정규화된 텍스트
    """
    if not text:
        return ""
    
    if config is None:
        config = TextProcessingConfig()
    
    # 기본 정규화
    text = text.strip()
    
    # 소문자 변환
    if config.lowercase:
        text = text.lower()
    
    # 여러 공백을 단일 공백으로
    if config.normalize_whitespace:
        text = re.sub(r'\s+', ' ', text)
    
    # 추가 개행 제거
    if config.remove_extra_newlines:
        text = re.sub(r'\n\s*\n', '\n', text)
        text = re.sub(r'\r\n', '\n', text)
    
    # 특수 문자 제거
    if config.remove_special_chars:
        if config.allowed_chars:
            # 허용된 문자만 남기기
            pattern = f'[^{re.escape(config.allowed_chars)}\\s]'
        else:
            # 기본 특수 문자 제거
            pattern = r'[^\w\s\.\,\!\?\;\:\-\(\)\[\]\{\}\"\'\/\@\#\$\%\^\&\*\+\=\~\`]'
        
        text = re.sub(pattern, '', text)
    
    # 길이 제한
    if config.max_length and len(text) > config.max_length:
        text = text[:config.max_length]
    
    if config.min_length and len(text) < config.min_length:
        text = ""
    
    return text.strip()


def calculate_tokens(text: str, avg_token_length: int = 4) -> int:
    """
    텍스트의 토큰 수를 계산합니다.
    
    Args:
        text: 토큰 수를 계산할 텍스트
        avg_token_length: 평균 토큰 길이 (기본: 4)
        
    Returns:
        계산된 토큰 수
    """
    if not text:
        return 0
    
    # 문자 수 기반 토큰 계산
    token_count = len(text) // avg_token_length
    
    # 구두점 고려 (간단한 방식)
    punctuation_count = len(re.findall(r'[^\w\s]', text))
    token_count += punctuation_count // 3  # 구두점을 토큰으로 간주
    
    return max(1, token_count)


def add_eos_token(text: str, eos_token: str = "</s>") -> str:
    """
    EOS 토큰을 텍스트에 추가합니다.
    
    Args:
        text: EOS 토큰을 추가할 텍스트
        eos_token: EOS 토큰
        
    Returns:
        EOS 토큰이 추가된 텍스트
    """
    if not text:
        return eos_token
    
    if not text.endswith(eos_token):
        return text + eos_token
    
    return text


def remove_duplicates(samples: List[Dict[str, Any]], key_fields: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    중복 샘플을 제거합니다. 테스트 모드에서는 더 관대한 중복 제거 전략을 사용합니다.
    
    Args:
        samples: 샘플 목록
        key_fields: 중복 검사를 위한 키 필드 목록
        
    Returns:
        중복이 제거된 샘플 목록
    """
    if not samples:
        return []
    
    if key_fields is None:
        # 기본 키 필드 - 테스트 모드에서는 response만 사용하여 엄격한 중복 제거 방지
        key_fields = ["response"]
    
    seen_hashes = set()
    unique_samples = []
    
    for sample in samples:
        # 키 필드로 해시 생성
        key_values = []
        for field in key_fields:
            value = str(sample.get(field, "")).lower().strip()
            
            # 숫자만 있는 instruction 필드는 중복 검사에서 제외 (테스트 모드용)
            if field == "instruction" and value.isdigit():
                continue
                
            key_values.append(value)
        
        key_string = "|".join(key_values)
        sample_hash = hashlib.md5(key_string.encode()).hexdigest()
        
        if sample_hash not in seen_hashes:
            seen_hashes.add(sample_hash)
            unique_samples.append(sample)
    
    logger.info(f"Removed {len(samples) - len(unique_samples)} duplicate samples")
    return unique_samples


def split_train_test(
    data: List[Dict[str, Any]], 
    train_ratio: float = 0.9, 
    shuffle: bool = True,
    seed: Optional[int] = None
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    데이터를 학습/검증 세트로 분할합니다.
    
    Args:
        data: 분할할 데이터
        train_ratio: 학습 데이터 비율
        shuffle: 데이터 셔플 여부
        seed: 랜덤 시드
        
    Returns:
        (학습 데이터, 검증 데이터) 튜플
    """
    if not data:
        return [], []
    
    if seed is not None:
        import random
        random.seed(seed)
    
    if shuffle:
        import random
        random.shuffle(data)
    
    split_index = int(len(data) * train_ratio)
    train_data = data[:split_index]
    val_data = data[split_index:]
    
    logger.info(f"Split data: {len(train_data)} train, {len(val_data)} validation")
    return train_data, val_data


def save_jsonl(data: List[Dict[str, Any]], file_path: Union[str, Path], encoding: str = 'utf-8'):
    """
    데이터를 JSONL 형식으로 저장합니다.
    
    Args:
        data: 저장할 데이터
        file_path: 파일 경로
        encoding: 파일 인코딩
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w', encoding=encoding) as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')
    
    logger.info(f"Saved {len(data)} items to {file_path}")


def load_jsonl(file_path: Union[str, Path], encoding: str = 'utf-8') -> List[Dict[str, Any]]:
    """
    JSONL 파일에서 데이터를 로드합니다.
    
    Args:
        file_path: 파일 경로
        encoding: 파일 인코딩
        
    Returns:
        로드된 데이터 목록
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    data = []
    with open(file_path, 'r', encoding=encoding) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    item = json.loads(line)
                    data.append(item)
                except json.JSONDecodeError as e:
                    logger.warning(f"Invalid JSON on line {line_num}: {e}")
                    continue
    
    logger.info(f"Loaded {len(data)} items from {file_path}")
    return data


async def async_save_jsonl(
    data: List[Dict[str, Any]], 
    file_path: Union[str, Path], 
    encoding: str = 'utf-8',
    batch_size: int = 1000
):
    """
    비동기 방식으로 JSONL 파일을 저장합니다.
    
    Args:
        data: 저장할 데이터
        file_path: 파일 경로
        encoding: 파일 인코딩
        batch_size: 배치 크기
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    async with aiofiles.open(file_path, 'w', encoding=encoding) as f:
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            for item in batch:
                line = json.dumps(item, ensure_ascii=False) + '\n'
                await f.write(line)
    
    logger.info(f"Async saved {len(data)} items to {file_path}")


def calculate_diversity_score(samples: List[Dict[str, Any]]) -> float:
    """
    데이터셋의 다양성 점수를 계산합니다.
    
    Args:
        samples: 샘플 목록
        
    Returns:
        다양성 점수 (0.0 ~ 1.0)
    """
    if not samples:
        return 0.0
    
    # 텍스트 추출
    all_texts = []
    for sample in samples:
        # 포맷별 텍스트 추출
        if "conversations" in sample:
            for conv in sample["conversations"]:
                all_texts.append(conv.get("value", ""))
        elif "instruction" in sample:
            all_texts.append(sample.get("instruction", ""))
            all_texts.append(sample.get("output", ""))
        elif "messages" in sample:
            for msg in sample["messages"]:
                all_texts.append(msg.get("content", ""))
    
    # 키워드 추출
    all_keywords = []
    for text in all_texts:
        words = re.findall(r'\b\w+\b', text.lower())
        # 불용어 제거 (간단한 방식)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        keywords = [word for word in words if len(word) > 2 and word not in stop_words]
        all_keywords.extend(keywords)
    
    if not all_keywords:
        return 0.0
    
    # 다양성 계산 (고유 키워드 비율)
    unique_keywords = set(all_keywords)
    diversity_score = len(unique_keywords) / len(all_keywords)
    
    return min(1.0, diversity_score)


def validate_token_range(
    item: Dict[str, Any], 
    min_tokens: int, 
    max_tokens: int
) -> bool:
    """
    아이템의 토큰 범위를 검증합니다.
    
    Args:
        item: 검증할 아이템
        min_tokens: 최소 토큰 수
        max_tokens: 최대 토큰 수
        
    Returns:
        검증 결과
    """
    token_count = calculate_tokens_from_item(item)
    
    return min_tokens <= token_count <= max_tokens


def calculate_tokens_from_item(item: Dict[str, Any]) -> int:
    """
    아이템에서 토큰 수를 계산합니다.
    
    Args:
        item: 토큰 수를 계산할 아이템
        
    Returns:
        계산된 토큰 수
    """
    total_chars = 0
    
    # 포맷별 토큰 계산
    if "conversations" in item:
        for conv in item["conversations"]:
            total_chars += len(conv.get("value", ""))
    
    elif "instruction" in item:
        total_chars += len(item.get("instruction", ""))
        total_chars += len(item.get("output", ""))
        total_chars += len(item.get("input", ""))
    
    elif "messages" in item:
        for msg in item["messages"]:
            total_chars += len(msg.get("content", ""))
    
    # 평균 토큰 길이를 4로 가정
    return total_chars // 4


def extract_keywords_from_text(text: str, max_keywords: int = 10) -> List[str]:
    """
    텍스트에서 키워드를 추출합니다.
    
    Args:
        text: 키워드를 추출할 텍스트
        max_keywords: 최대 키워드 수
        
    Returns:
        추출된 키워드 목록
    """
    if not text:
        return []
    
    # 텍스트 전처리
    text = text.lower()
    
    # 키워드 추출
    words = re.findall(r'\b\w+\b', text)
    
    # 불용어 제거
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
        'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
        'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those'
    }
    
    # 필터링
    keywords = [
        word for word in words 
        if len(word) > 2 and word not in stop_words and not word.isdigit()
    ]
    
    # 빈도수 계산
    word_freq = Counter(keywords)
    
    # 상위 키워드 반환
    return [word for word, _ in word_freq.most_common(max_keywords)]


def calculate_content_quality(text: str) -> float:
    """
    콘텐츠 품질 점수를 계산합니다.
    
    Args:
        text: 품질을 평가할 텍스트
        
    Returns:
        품질 점수 (0.0 ~ 1.0)
    """
    if not text:
        return 0.0
    
    score = 1.0
    
    # 길이 점수
    length_score = min(1.0, len(text) / 100)  # 100자 이상이면 완벽
    score *= length_score
    
    # 문장 구조 점수
    sentence_count = len(re.findall(r'[.!?]+', text))
    if sentence_count == 0:
        score *= 0.5
    else:
        sentence_score = min(1.0, sentence_count / 3)  # 3문장 이상이면 완벽
        score *= sentence_score
    
    # 단어 다양성 점수
    words = re.findall(r'\b\w+\b', text.lower())
    if len(words) > 10:
        unique_words = set(words)
        diversity = len(unique_words) / len(words)
        score *= diversity
    
    return min(1.0, max(0.0, score))


def merge_document_sources(
    primary_docs: List[Dict[str, Any]], 
    secondary_docs: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    여러 문서 소스를 병합합니다.
    
    Args:
        primary_docs: 주요 문서 목록
        secondary_docs: 보조 문서 목록
        
    Returns:
        병합된 문서 목록
    """
    merged_docs = []
    
    # 주요 문서 추가
    for doc in primary_docs:
        doc["source_priority"] = "high"
        merged_docs.append(doc)
    
    # 보조 문서 추가
    for doc in secondary_docs:
        doc["source_priority"] = "low"
        merged_docs.append(doc)
    
    # 우선순위별 정렬
    merged_docs.sort(key=lambda x: x.get("source_priority", "medium"))
    
    return merged_docs


def generate_unique_id(prefix: str = "item") -> str:
    """
    고유 ID를 생성합니다.
    
    Args:
        prefix: ID 접두사
        
    Returns:
        생성된 고유 ID
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    random_part = str(uuid.uuid4())[:8]
    return f"{prefix}_{timestamp}_{random_part}"


def clean_filename(filename: str) -> str:
    """
    파일명을 정리합니다.
    
    Args:
        filename: 정리할 파일명
        
    Returns:
        정리된 파일명
    """
    # 허용되지 않는 문자 제거
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    # 공백을 언더스코어로
    filename = re.sub(r'\s+', '_', filename)
    
    # 파일명 길이 제한
    if len(filename) > 200:
        name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        filename = name[:200-len(ext)-1] + '.' + ext if ext else name[:200]
    
    return filename.strip('_')


def get_file_info(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    파일 정보를 가져옵니다.
    
    Args:
        file_path: 파일 경로
        
    Returns:
        파일 정보 딕셔너리
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    stat = file_path.stat()
    
    return {
        "path": str(file_path),
        "name": file_path.name,
        "size": stat.st_size,
        "size_human": format_file_size(stat.st_size),
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
        "extension": file_path.suffix.lower()
    }


def format_file_size(size_bytes: int) -> str:
    """
    파일 크기를 사람이 읽기 쉬운 형식으로 포맷합니다.
    
    Args:
        size_bytes: 바이트 크기
        
    Returns:
        포맷된 파일 크기 문자열
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"


def is_valid_md_file(file_path: Union[str, Path]) -> bool:
    """
    파일이 유효한 MD 파일인지 확인합니다.
    
    Args:
        file_path: 파일 경로
        
    Returns:
        유효성 검증 결과
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        return False
    
    if file_path.suffix.lower() not in ['.md', '.markdown']:
        return False
    
    # 파일 크기 확인
    try:
        size = file_path.stat().st_size
        if size == 0 or size > 10 * 1024 * 1024:  # 10MB 제한
            return False
    except:
        return False
    
    return True


def batch_process(
    items: List[Any], 
    process_func, 
    batch_size: int = 100, 
    max_workers: int = 4
) -> List[Any]:
    """
    배치 처리를 수행합니다.
    
    Args:
        items: 처리할 아이템 목록
        process_func: 처리 함수
        batch_size: 배치 크기
        max_workers: 최대 워커 수
        
    Returns:
        처리된 결과 목록
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 배치로 분할
        batches = [items[i:i + batch_size] for i in range(0, len(items), batch_size)]
        
        # 배치별 처리
        future_to_batch = {
            executor.submit(process_func, batch): batch 
            for batch in batches
        }
        
        for future in as_completed(future_to_batch):
            try:
                batch_result = future.result()
                results.extend(batch_result)
            except Exception as e:
                logger.error(f"Batch processing failed: {e}")
    
    return results


def create_directory_structure(base_path: Union[str, Path], subdirs: List[str]) -> None:
    """
    디렉토리 구조를 생성합니다.
    
    Args:
        base_path: 기본 경로
        subdirs: 생성할 하위 디렉토리 목록
    """
    base_path = Path(base_path)
    base_path.mkdir(parents=True, exist_ok=True)
    
    for subdir in subdirs:
        (base_path / subdir).mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Created directory structure at {base_path}")


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
        logger.error(f"Failed to save documents: {e}")
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
            raise FileNotFoundError(f"File not found: {input_path}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            documents = json.load(f)
        
        if not isinstance(documents, list):
            raise ValueError("JSON file should contain a list of documents")
        
        logger.info(f"Loaded {len(documents)} documents from {input_path}")
        return documents
    
    except Exception as e:
        logger.error(f"Failed to load documents: {e}")
        return []


if __name__ == "__main__":
    # 테스트용 샘플 데이터
    test_samples = [
        {
            "instruction": "테스트 지시문 1",
            "response": "테스트 응답 1",
            "source": "test"
        },
        {
            "instruction": "테스트 지시문 2",
            "response": "테스트 응답 2",
            "source": "test"
        },
        {
            "instruction": "테스트 지시문 1",  # 중복
            "response": "테스트 응답 1",
            "source": "test"
        }
    ]
    
    print("=== Utils Test ===")
    
    # 텍스트 정규화 테스트
    test_text = "  여러   공백과\n특수문자!@#   포함된  텍스트  "
    normalized = normalize_text(test_text)
    print(f"Text normalization: '{test_text}' -> '{normalized}'")
    
    # 토큰 계산 테스트
    token_count = calculate_tokens(normalized)
    print(f"Token count: {token_count}")
    
    # 중복 제거 테스트
    unique_samples = remove_duplicates(test_samples)
    print(f"Duplicate removal: {len(test_samples)} -> {len(unique_samples)}")
    
    # 데이터 분할 테스트
    train_data, val_data = split_train_test(unique_samples, 0.8)
    print(f"Train/test split: {len(train_data)} train, {len(val_data)} validation")
    
    # 다양성 점수 계산 테스트
    diversity_score = calculate_diversity_score(unique_samples)
    print(f"Diversity score: {diversity_score:.3f}")
    
    # 품질 점수 계산 테스트
    quality_score = calculate_content_quality("이것은 테스트 문장입니다. 여러 문장으로 구성되어 있습니다.")
    print(f"Content quality score: {quality_score:.3f}")
    
    # 파일 정보 테스트
    file_info = get_file_info(__file__)
    print(f"File info: {file_info}")