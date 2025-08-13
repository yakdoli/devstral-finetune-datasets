# Unsloth 호환 데이터셋 생성기

Unsloth 프레임워크에 최적화된 다양한 데이터셋 포맷을 생성하는 Python 모듈입니다. 기존에 구축된 모든 모듈(MD 처리, Qdrant 연동, OpenAI API 연동)과의 완벽한 통합을 지원합니다.

## 주요 특징

### 🚀 핵심 기능
- **다중 포맷 지원**: ShareGPT, Alpaca, OpenAI 포맷 생성
- **Unsloth 최적화**: 4-bit 양자화 훈련을 위한 최적화
- **메모리 효율성**: 대용량 데이터셋 처리 지원
- **품질 보장**: response_template 마커, EOS 토큰 처리
- **통계 정보**: 데이터셋 메타데이터 및 품질 지표 생성

### 🎯 Unsloth 특화 요구사항 충족
- **ShareGPT 포맷**: 다중 턴 대화 (system/human/gpt 역할)
- **Alpaca 포맷**: instruction/input/output 구조
- **OpenAI 포맷**: messages 배열 구조
- **토큰 최적화**: 50-4096 토큰 범위
- **시퀀스 길이**: 최대 4096 토큰 (Qwen2.5-7B-Instruct 최적화)
- **EOS 토큰**: `</s>` 또는 `<|im_end|>` 처리

## 설치

```bash
# 기본 의존성 설치
pip install -r requirements.txt

# 선택적 의존성 (외부 모듈과의 통합)
pip install -r optional_requirements.txt
```

## 빠른 시작

### 기본 사용법

```python
from unsloth_dataset import UnslothDatasetGenerator, DatasetConfig

# 데이터셋 생성기 설정
config = DatasetConfig(
    target_count=5000,
    max_seq_length=4096,
    train_test_split=0.9,
    formats=["sharegpt", "alpaca", "openai"],
    min_tokens=50,
    max_tokens=4096,
    eos_token="</s>",
    remove_duplicates=True,
    quality_threshold=0.7,
    batch_size=10,
    max_workers=2,
    seed=42,
    output_dir="output/dataset",
    include_metadata=True,
    shuffle_data=True
)

# 생성기 초기화
generator = UnslothDatasetGenerator(config)

# 데이터셋 생성
result = generator.generate_from_samples(samples, "my_dataset")

# 파일 저장
saved_paths = generator.save_datasets(result, "my_dataset")
```

### 외부 모듈과의 통합

```python
from md_processor import create_processor
from qdrant_connector import create_integrated_processor
from openai_connector import create_openai_connector
from unsloth_dataset import UnslothDatasetGenerator

# 데이터 소스 초기화
md_processor = create_processor()
qdrant_connector = create_integrated_processor()
openai_connector = create_openai_connector()

# 데이터셋 생성기 초기화
generator = UnslothDatasetGenerator(
    target_count=5000,
    max_seq_length=4096,
    train_test_split=0.9,
    formats=["sharegpt", "alpaca", "openai"]
)

# 데이터셋 생성
datasets = generator.generate_datasets(
    md_documents=md_processor.process_documents(),
    qdrant_documents=qdrant_connector.search_documents(),
    conversations=openai_connector.generate_conversations()
)

# 결과 저장
generator.save_datasets(datasets, "syncfusion_unsloth_dataset")
```

## 지원되는 데이터 포맷

### ShareGPT 포맷
```json
{
    "conversations": [
        {"from": "system", "value": "Syncfusion WinForms 기술 전문가입니다."},
        {"from": "human", "value": "DataGrid 컴포넌트 사용법을 알려주세요."},
        {"from": "gpt", "value": "DataGrid는 다음과 같이 사용합니다..."},
        {"from": "human", "value": "데이터 바인딩은 어떻게 하나요?"},
        {"from": "gpt", "value": "데이터 바인딩은..."}
    ]
}
```

### Alpaca 포맷
```json
{
    "instruction": "Syncfusion WinForms DataGrid 사용법을 설명해주세요.",
    "input": "초보자도 이해할 수 있도록 단계별로 설명해주세요.",
    "output": "DataGrid 컴포넌트 사용법:\n1. 프로젝트에 참조 추가..."
}
```

### OpenAI 포맷
```json
{
    "messages": [
        {"role": "system", "content": "Syncfusion WinForms 전문가"},
        {"role": "user", "content": "DataGrid 사용법 설명"},
        {"role": "assistant", "content": "DataGrid 사용법은..."}
    ]
}
```

## 구조

```
unsloth_dataset/
├── __init__.py                 # 모듈 초기화
├── generator.py                # 메인 데이터셋 생성기
├── validator.py                # Unsloth 호환성 검증기
├── statistics.py               # 데이터셋 통계 생성기
├── utils.py                    # 유틸리티 함수들
├── formatters/                 # 포맷별 생성기
│   ├── __init__.py
│   ├── sharegpt_formatter.py   # ShareGPT 포맷 생성기
│   ├── alpaca_formatter.py     # Alpaca 포맷 생성기
│   └── openai_formatter.py     # OpenAI 포맷 생성기
└── README.md                   # 이 문서
```

## API 문서

### UnslothDatasetGenerator

메인 데이터셋 생성기 클래스입니다.

#### 생성자

```python
UnslothDatasetGenerator(config: DatasetConfig)
```

**매개변수:**
- `config`: 데이터셋 생성 설정

#### 메서드

##### `generate_from_samples(samples, dataset_name)`
샘플 데이터로부터 데이터셋을 생성합니다.

**매개변수:**
- `samples`: 샘플 데이터 목록
- `dataset_name`: 데이터셋 이름

**반환값:**
- `DatasetGenerationResult`: 생성 결과 객체

##### `generate_datasets(md_documents, qdrant_documents, conversations)`
외부 모듈과의 통합을 통한 데이터셋 생성입니다.

**매개변수:**
- `md_documents`: MD 처리된 문서 목록
- `qdrant_documents`: Qdrant 검색 문서 목록
- `conversations`: OpenAI 생성 대화 목록

**반환값:**
- `DatasetGenerationResult`: 생성 결과 객체

##### `save_datasets(result, base_name)`
생성된 데이터셋을 파일로 저장합니다.

**매개변수:**
- `result`: 생성 결과 객체
- `base_name`: 기본 파일 이름

**반환값:**
- `dict`: 저장된 파일 경로 목록

### DatasetConfig

데이터셋 생성 설정 클래스입니다.

#### 속성

- `target_count`: 목표 샘플 수 (기본값: 1000)
- `max_seq_length`: 최대 시퀀스 길이 (기본값: 4096)
- `train_test_split`: 훈련/검증 데이터 비율 (기본값: 0.9)
- `formats`: 생성할 포맷 목록 (기본값: ["sharegpt", "alpaca", "openai"])
- `min_tokens`: 최소 토큰 수 (기본값: 50)
- `max_tokens`: 최대 토큰 수 (기본값: 4096)
- `eos_token`: EOS 토큰 (기본값: "</s>")
- `remove_duplicates`: 중복 제거 여부 (기본값: True)
- `quality_threshold`: 품질 임계값 (기본값: 0.7)
- `batch_size`: 배치 크기 (기본값: 10)
- `max_workers`: 최대 작업자 수 (기본값: 2)
- `seed`: 랜덤 시드 (기본값: 42)
- `output_dir`: 출력 디렉토리 (기본값: "output")
- `include_metadata`: 메타데이터 포함 여부 (기본값: True)
- `shuffle_data`: 데이터 셔플 여부 (기본값: True)
- `progress_interval`: 진행 표시 간격 (기본값: 100)

## 품질 보장

### 토큰 수 검증
- 50-4096 토큰 범위 준수
- 시퀀스 길이 최적화

### 대화 구조 검증
- 올바른 역할 순서 확인
- 필수 필드 검증

### 중복 제거
- 유사한 대화 필터링
- 해시 기반 중복 탐지

### EOS 토큰 처리
- 적절한 종료 토큰 추가
- 포맷별 최적화

### 인코딩 검증
- UTF-8 호환성 확인
- 특수 문자 처리

## 메타데이터 생성

### 데이터셋 통계
- 샘플 수, 평균 토큰 수, 턴 분포
- 포맷별 통계 정보

### 품질 지표
- 다양성 점수, 품질 점수
- 포맷별 품질 평가

### 소스 정보
- 사용된 문서 및 생성 설정
- 데이터 소스 추적

### Unsloth 호환성
- 검증 결과 리포트
- 최적화 권장사항

## 성능 최적화

### 메모리 효율성
- 스트리밍 방식 파일 처리
- 배치 처리 지원
- 메모리 관리 최적화

### 병렬 처리
- 멀티스레딩 지원
- 비동기 처리
- 작업 분할

### 대용량 데이터 처리
- 청크 단위 처리
- 점진적 로딩
- 메모리 누수 방지

## 테스트

```bash
# 기본 테스트 실행
python -m pytest tests/

# 통합 테스트 실행
python test_unsloth_dataset.py

# 특정 테스트 실행
python -m pytest tests/test_formatters.py
```

## 예제

자세한 사용 예제는 `example_usage.py` 파일을 참조하세요.

## 문제 해결

### 일반적인 문제

1. **메모리 부족**
   - `batch_size` 값을 줄이세요
   - `max_workers` 값을 조절하세요
   - 데이터를 청크로 나누어 처리하세요

2. **토큰 수 초과**
   - `max_tokens` 값을 조절하세요
   - 텍스트를 분할하여 처리하세요
   - 요약 기능을 사용하세요

3. **포맷 변환 실패**
   - 입력 데이터 구조를 확인하세요
   - 필드 이름이 올바른지 확인하세요
   - 유효성 검사 로그를 확인하세요

### 로깅

```python
import logging

# 로깅 레벨 설정
logging.basicConfig(level=logging.INFO)

# 특정 모듈의 로깅 설정
logging.getLogger('unsloth_dataset').setLevel(logging.DEBUG)
```

## 기여

기여는 환영합니다! 다음 단계를 따라주세요:

1. 이 저장소를 포크하세요
2. 기능 브랜치를 생성하세요 (`git checkout -b feature/amazing-feature`)
3. 변경 사항을 커밋하세요 (`git commit -m 'Add amazing feature'`)
4. 브랜치를 푸시하세요 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성하세요

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 지원

문의사항이 있으면 다음 방법으로 연락주세요:

- 이슈 트래커: [GitHub Issues](https://github.com/your-repo/issues)
- 이메일: support@example.com

## 업데이트 로그

### v1.0.0 (2024-01-01)
- 초기 버전 출시
- ShareGPT, Alpaca, OpenAI 포맷 지원
- 기본 통합 기능 구현
- 테스트 스위트 완성

### v1.1.0 (2024-01-15)
- 성능 최적화
- 메모리 효율성 개선
- 새로운 유틸리티 함수 추가
- 버그 수정

## 관련 프로젝트

- [MD Processor](../md_processor/) - MD 문서 처리 모듈
- [Qdrant Connector](../qdrant_connector/) - Qdrant 벡터 DB 연동 모듈
- [OpenAI Connector](../openai_connector/) - OpenAI API 연동 모듈

## 크레딧

이 프로젝트는 다음 프로젝트들의 영향을 받았습니다:

- [Unsloth](https://github.com/unslothai/unsloth) - 고성능 언어 모델 훈련
- [ShareGPT](https://sharegpt.com/) - 대화 데이터셋
- [Alpaca](https://github.com/tatsu-lab/stanford_alpaca) - 지시 데이터셋
- [OpenAI API](https://platform.openai.com/) - 생성형 AI API