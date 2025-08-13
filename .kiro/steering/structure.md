# 프로젝트 구조 및 조직

## 모듈 아키텍처

### 핵심 모듈
```
├── md_processor/           # MD 파일 처리 모듈
│   ├── __init__.py        # 모듈 초기화 및 팩토리 함수
│   ├── scanner.py         # 파일 스캐닝 및 메타데이터 추출
│   ├── parser.py          # MD 콘텐츠 파싱 및 전처리
│   ├── processor.py       # 메인 처리 파이프라인
│   └── utils.py           # 유틸리티 함수

├── openai_connector/       # OpenAI API 연동 모듈
│   ├── __init__.py        # 모듈 초기화 및 메인 클래스
│   ├── client.py          # API 클라이언트 관리
│   ├── prompt_engine.py   # 프롬프트 템플릿 관리
│   ├── conversation_generator.py  # 대화 생성 로직
│   ├── token_manager.py   # 토큰 최적화
│   └── utils.py           # 유틸리티 함수

├── qdrant_connector/       # Qdrant 벡터 DB 연동 모듈
│   ├── __init__.py        # 모듈 초기화 및 메인 클래스
│   ├── client.py          # Qdrant 클라이언트 관리
│   ├── searcher.py        # 문서 검색 기능
│   ├── transformer.py     # 데이터 변환
│   ├── integration.py     # 통합 처리기
│   └── utils.py           # 유틸리티 함수

├── unsloth_dataset/        # Unsloth 데이터셋 생성 모듈
│   ├── __init__.py        # 모듈 초기화 및 팩토리 함수
│   ├── generator.py       # 메인 데이터셋 생성기
│   ├── formatters/        # 포맷별 변환기
│   │   ├── sharegpt_formatter.py
│   │   ├── alpaca_formatter.py
│   │   └── openai_formatter.py
│   ├── validator.py       # Unsloth 호환성 검증
│   ├── statistics.py      # 통계 분석
│   └── utils.py           # 유틸리티 함수

└── quality_validator/      # 품질 검증 모듈
    ├── __init__.py        # 모듈 초기화 및 메인 클래스
    ├── safety_filter.py   # 안전성 필터
    ├── duplicate_remover.py  # 중복 제거
    ├── quality_scorer.py  # 품질 점수 계산
    ├── compatibility_checker.py  # 호환성 검증
    ├── statistics_analyzer.py    # 통계 분석
    ├── auto_corrector.py  # 자동 수정
    └── utils.py           # 유틸리티 함수
```

### 데이터 디렉토리
```
├── md_staging/            # MD 파일 스테이징 영역
│   ├── DICOM/            # 컴포넌트별 MD 파일
│   ├── DocIo/
│   ├── Gauge/
│   └── [기타 컴포넌트]/
├── output/               # 출력 디렉토리
│   ├── datasets/         # 생성된 데이터셋
│   ├── logs/            # 로그 파일
│   └── reports/         # 리포트 파일
└── legacy/              # 레거시 코드 및 참조 자료
```

## 코딩 컨벤션

### 파일 명명 규칙
- **모듈 파일**: `snake_case.py`
- **클래스 파일**: 주요 클래스명과 일치 (예: `MDProcessor` → `processor.py`)
- **설정 파일**: `config.yaml`, `requirements.txt`
- **테스트 파일**: `test_[모듈명].py`

### 클래스 및 함수 명명
- **클래스**: `PascalCase` (예: `MDProcessor`, `QualityValidator`)
- **함수/메서드**: `snake_case` (예: `process_documents`, `validate_quality`)
- **상수**: `UPPER_SNAKE_CASE` (예: `MAX_TOKENS`, `DEFAULT_BATCH_SIZE`)
- **팩토리 함수**: `create_[객체명]` (예: `create_processor`, `create_validator`)

### 모듈 구조 패턴
각 모듈은 다음 구조를 따릅니다:
1. **`__init__.py`**: 모듈 초기화, 주요 클래스/함수 export, 팩토리 함수
2. **메인 클래스 파일**: 핵심 비즈니스 로직
3. **설정 클래스**: `dataclass` 기반 설정 관리
4. **유틸리티 파일**: 공통 헬퍼 함수
5. **테스트 파일**: 단위 테스트 및 통합 테스트

### 설정 관리
- **YAML 설정**: `config.yaml`에서 전역 설정 관리
- **환경 변수**: API 키 등 민감 정보
- **Dataclass 설정**: 각 모듈별 타입 안전한 설정 클래스
- **기본값**: 모든 설정에 합리적인 기본값 제공

### 에러 처리
- **로깅**: 구조화된 로깅 (INFO, WARNING, ERROR 레벨)
- **예외 처리**: 구체적인 예외 타입 사용
- **복구 가능한 오류**: 경고 로그 후 계속 진행
- **치명적 오류**: 명확한 에러 메시지와 함께 중단

### 비동기 처리
- **async/await**: 모든 I/O 작업에 비동기 패턴 사용
- **배치 처리**: 대용량 데이터 처리를 위한 배치 단위 처리
- **동시성 제한**: `asyncio.Semaphore`로 동시 요청 수 제한
- **진행률 표시**: `tqdm` 기반 진행률 바

### 데이터 포맷
- **입력**: MD 파일, JSON 메타데이터
- **중간 처리**: Python 딕셔너리 기반 구조화된 데이터
- **출력**: JSONL 포맷 (ShareGPT, Alpaca, OpenAI)
- **로그**: 구조화된 JSON 로그