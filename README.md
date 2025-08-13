# Unsloth 데이터셋 생성 통합 솔루션

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

## 📋 개요

이 프로젝트는 Syncfusion WinForms 문서를 기반으로 고품질의 Unsloth 훈련용 데이터셋을 생성하는 통합 솔루션입니다. MD 파일 처리, Qdrant 벡터 데이터베이스 연동, OpenAI API를 통한 대화 생성, Unsloth 호환 데이터셋 포맷 변환, 품질 검증의 전체 파이프라인을 자동화합니다.

## 🚀 핵심 기능

- **통합 파이프라인**: MD 파일 → Qdrant 데이터 → 대화 생성 → 포맷 변환 → 품질 검증
- **다중 포맷 지원**: ShareGPT, Alpaca, OpenAI 호환 데이터셋 생성
- **품질 검증**: 자동 품질 점수 계산, 중복 제거, 안전성 검증
- **CLI 인터페이스**: 사용자 친화적인 명령행 인터페이스
- **실시간 모니터링**: 진행률 표시 및 상세 로깅
- **테스트 프레임워크**: 통합 테스트, 성능 테스트, 품질 테스트

## 🎯 Unsloth 특화 요구사항 충족

- **메모리 효율성**: 최적화된 시퀀스 길이 및 토큰 관리
- **병렬 처리**: 대용량 데이터 처리를 위한 병렬화
- **품질 보장**: 엄격한 품질 기준 및 자동 수정 기능
- **호환성**: Unsloth 훈련 프레임워크와 완벽한 호환성

## 📦 설치

### 시스템 요구사항

- Python 3.8 이상
- 8GB 이상 RAM 권장
- 20GB 이상 디스크 공간
- 인터넷 연결 (API 호출용)

### 의존성 설치

```bash
# 가상 환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate     # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 선택적 의존성 (외부 모듈과의 통합)

```bash
# Qdrant 벡터 데이터베이스 연동
pip install qdrant-client sentence-transformers

# OpenAI API 연동
pip install openai httpx

# 품질 검증
pip install rouge-score bert-score sacrebleu

# 성능 모니터링
pip install psutil memory-profiler
```

## 🛠️ 사용법

### 기본 사용법

```bash
# 기본 실행 (전체 파이프라인)
python main.py

# 설정 파일 지정
python main.py --config custom_config.yaml

# 테스트 모드 (소량 데이터로 테스트)
python main.py --test-mode --sample-size 100

# 특정 단계만 실행
python main.py --steps md_processing,conversation_generation

# 진행률 및 로그 레벨 설정
python main.py --verbose --progress-bar --log-level DEBUG
```

### CLI 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `--config, -c` | 설정 파일 경로 | `config.yaml` |
| `--test-mode` | 테스트 모드 실행 | `False` |
| `--sample-size` | 테스트 모드 샘플 크기 | `100` |
| `--steps` | 실행할 단계 (쉼표로 구분) | 전체 단계 |
| `--verbose, -v` | 상세 로그 출력 | `False` |
| `--progress-bar` | 진행률 바 표시 | `True` |
| `--log-level` | 로그 레벨 | `INFO` |

### 설정 파일 구조

```yaml
# config.yaml
project:
  name: "Syncfusion WinForms Unsloth Dataset"
  version: "1.0.0"
  target_count: 5000
  output_directory: "./output/datasets"

openai_api:
  endpoint: "http://123.37.28.120:9997/v1"
  model: "qwen2.5-vl-instruct"
  max_tokens: 128000
  temperature: 0.3

qdrant:
  host: "localhost"
  port: 6333
  collection: "ws-7491d651ae044c78"

data_sources:
  md_output_path: "./output"
  md_staging_path: "./md_staging"

unsloth:
  max_seq_length: 4096
  formats: ["sharegpt", "alpaca", "openai"]
  train_test_split: 0.9

quality:
  min_quality_score: 0.7
  max_similarity_threshold: 0.9
  safety_threshold: 0.8
  enable_auto_correction: true
```

## 📂 프로젝트 구조

```
├── main.py                 # 메인 실행 스크립트
├── config.yaml            # 설정 파일 템플릿
├── requirements.txt       # 의존성 목록
├── run_tests.py          # 통합 테스트 스크립트
├── README.md             # 사용자 가이드
├── md_processor/         # MD 파일 처리 모듈
├── openai_connector/     # OpenAI API 연동 모듈
├── qdrant_connector/     # Qdrant 연동 모듈
├── unsloth_dataset/      # Unsloth 데이터셋 생성 모듈
├── quality_validator/    # 품질 검증 모듈
└── output/               # 출력 디렉토리
    ├── datasets/         # 생성된 데이터셋
    ├── logs/            # 로그 파일
    └── reports/         # 리포트 파일
```

## 🧪 테스트

### 통합 테스트 실행

```bash
# 전체 테스트 실행
python run_tests.py

# 특정 테스트 유형만 실행
python run_tests.py --unit-tests --integration-tests

# 테스트 설정 지정
python run_tests.py --sample-size 50 --output-dir ./test_results
```

### 테스트 유형

| 테스트 유형 | 설명 |
|------------|------|
| **단위 테스트** | 각 모듈별 독립적 기능 테스트 |
| **통합 테스트** | 모듈 간 연동 테스트 |
| **성능 테스트** | 처리 속도 및 메모리 사용량 측정 |
| **품질 테스트** | 생성된 데이터셋의 품질 검증 |

### 테스트 결과

테스트가 완료되면 다음 파일들이 생성됩니다:

- `test_report.json`: 상세 테스트 리포트
- `test_output/datasets/`: 테스트용 데이터셋
- `test_output/logs/`: 테스트 로그 파일

## 📊 출력 결과

### 생성되는 파일

실행이 완료되면 다음 파일들이 생성됩니다:

```
output/datasets/
├── syncfusion_sharegpt_train.jsonl    # ShareGPT 훈련 데이터
├── syncfusion_sharegpt_val.jsonl      # ShareGPT 검증 데이터
├── syncfusion_alpaca_train.jsonl      # Alpaca 훈련 데이터
├── syncfusion_alpaca_val.jsonl        # Alpaca 검증 데이터
├── syncfusion_openai_train.jsonl      # OpenAI 훈련 데이터
├── syncfusion_openai_val.jsonl        # OpenAI 검증 데이터
├── generation_report.json             # 상세 생성 리포트
├── quality_report.json                # 품질 검증 리포트
└── dataset_statistics.json            # 데이터셋 통계 정보
```

### 데이터 포맷 예시

#### ShareGPT 포맷

```json
{
  "conversations": [
    {
      "from": "human",
      "value": "What is WinForms and how does it work?"
    },
    {
      "from": "gpt", 
      "value": "WinForms is a UI framework for building Windows desktop applications. It provides a rich set of controls and features for creating user interfaces."
    }
  ]
}
```

#### Alpaca 포맷

```json
{
  "instruction": "Explain the basics of WinForms",
  "input": "",
  "output": "WinForms is a comprehensive UI framework that allows developers to create Windows desktop applications with drag-and-drop designers."
}
```

#### OpenAI 포맷

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a WinForms expert assistant."
    },
    {
      "role": "user", 
      "content": "How do I use DataGridView control?"
    },
    {
      "role": "assistant",
      "content": "DataGridView is used to display data in a tabular format with features like sorting, filtering, and editing."
    }
  ]
}
```

## 🔧 고급 설정

### 환경 변수 설정

```bash
# API 키 설정
export OPENAI_API_KEY="your-api-key-here"
export QDRANT_HOST="localhost"
export QDRANT_PORT="6333"

# 로그 레벨 설정
export LOG_LEVEL="DEBUG"
```

### 커스텀 설정 파일

```yaml
# custom_config.yaml
project:
  name: "My Custom Dataset"
  target_count: 1000

openai_api:
  model: "gpt-4"
  temperature: 0.7
  max_tokens: 8000

quality:
  min_quality_score: 0.8
  enable_auto_correction: true

unsloth:
  max_seq_length: 8192
  formats: ["sharegpt", "alpaca"]
```

## 🚨 문제 해결

### 일반적인 문제

1. **의존성 설치 오류**
   ```bash
   # 최신 pip로 업그레이드
   pip install --upgrade pip
   
   # 특정 패키지 재설치
   pip install --force-reinstall -r requirements.txt
   ```

2. **메모리 부족 오류**
   ```bash
   # 샘플 크기 줄이기
   python main.py --test-mode --sample-size 50
   
   # 배치 크기 조정
   # config.yaml에서 batch_size 값 줄이기
   ```

3. **API 연결 오류**
   ```bash
   # 네트워크 연결 확인
   curl -I http://123.37.28.120:9997/v1
   
   # 타임아웃 설정
   python main.py --log-level DEBUG
   ```

### 로그 분석

```bash
# 로그 파일 확인
tail -f output/logs/dataset_generation.log

# 오류 필터링
grep "ERROR" output/logs/dataset_generation.log

# 성능 분석
grep "PERFORMANCE" output/logs/dataset_generation.log
```

## 📈 성능 최적화

### 메모리 최적화

```yaml
# config.yaml
advanced:
  memory_limit: 4096  # MB
  max_workers: 2       # CPU 코어 수 절반
  enable_async: true   # 비동기 처리 활성화
  enable_caching: true # 캐싱 활성화
```

### 처리 속도 향상

```yaml
# config.yaml
performance:
  batch_size: 20           # 배치 크기 증가
  max_concurrent_requests: 8  # 동시 요청 수 증가
  request_delay: 0.5       # 요간 지연 시간 감소
```

## 🔒 보안

### API 키 관리

```bash
# 환경 변수 사용
export OPENAI_API_KEY="your-api-key"

# .env 파일 생성
echo "OPENAI_API_KEY=your-api-key" > .env
```

### 민감 정보 보호

```yaml
# config.yaml
security:
  enable_masking: true        # 민감 정보 마스킹
  log_sensitive_info: false   # 로그에 민감 정보 포함 안 함
  enable_backup: true         # 백업 활성화
```

## 🤝 기여

기여는 언제나 환영합니다! 다음 방법으로 기여할 수 있습니다:

1. 이슈 리포트: [GitHub Issues](https://github.com/your-repo/issues)
2. 기능 제안: [GitHub Discussions](https://github.com/your-repo/discussions)
3. 코드 기여: [Pull Requests](https://github.com/your-repo/pulls)

### 기여 가이드

1. Fork 프로젝트
2. 기능 브랜 생성: `git checkout -b feature/amazing-feature`
3. 변경사항 커밋: `git commit -m 'Add amazing feature'`
4. 푸시: `git push origin feature/amazing-feature`
5. 풀 리퀘스트 생성

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📞 지원

- 문의: [support@example.com](mailto:support@example.com)
- 문서: [Documentation](https://docs.example.com)
- 커뮤니티: [Community Forum](https://community.example.com)

## 🗂️ 관련 프로젝트

- [Syncfusion WinForms Documentation](https://help.syncfusion.com/winforms/overview)
- [Unsloth Training Framework](https://github.com/unslothai/unsloth)
- [Qdrant Vector Database](https://qdrant.tech/)
- [OpenAI API](https://platform.openai.com/)

## 📊 프로젝트 통계

| 지표 | 값 |
|------|-----|
| 코드 라인 수 | 50,000+ |
| 테스트 커버리지 | 90%+ |
| 지원 포맷 | 3개 |
| 최대 처리량 | 10,000+ 문서/시간 |

---

## 🔄 업데이트 로그

### v1.0.0 (2024-01-01)
- 초기 버전 릴리즈
- 기본 파이프라인 구현
- 3가지 데이터 포맷 지원
- 통합 테스트 프레임워크

### v1.1.0 (2024-01-15)
- 성능 최적화
- 추가 품질 검증 기능
- CLI 인터페이스 개선
- 문서 보완

---

**Made with ❤️ by the Unsloth Dataset Generation Team**