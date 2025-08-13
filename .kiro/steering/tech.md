# 기술 스택 및 빌드 시스템

## 핵심 기술 스택
- **언어**: Python 3.8+
- **비동기 처리**: asyncio, aiohttp, aiofiles
- **데이터 처리**: pandas, numpy, scipy, scikit-learn
- **텍스트 처리**: nltk, spacy, regex, beautifulsoup4
- **벡터 데이터베이스**: qdrant-client, sentence-transformers
- **AI/ML**: openai, transformers, torch, datasets, huggingface-hub
- **품질 검증**: rouge-score, bert-score, sacrebleu
- **CLI**: click, typer, rich, tqdm
- **설정 관리**: PyYAML, python-dotenv, pydantic

## 프로젝트 구조
```
├── main.py                 # 메인 실행 스크립트
├── config.yaml            # 설정 파일
├── requirements.txt       # 의존성 목록
├── md_processor/          # MD 파일 처리 모듈
├── openai_connector/      # OpenAI API 연동 모듈
├── qdrant_connector/      # Qdrant 연동 모듈
├── unsloth_dataset/       # Unsloth 데이터셋 생성 모듈
├── quality_validator/     # 품질 검증 모듈
├── md_staging/           # MD 파일 스테이징 디렉토리
└── output/               # 출력 디렉토리
```

## 공통 명령어

### 환경 설정
```bash
# 가상 환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 실행 명령어
```bash
# 기본 실행 (전체 파이프라인)
python main.py

# 설정 파일 지정
python main.py --config custom_config.yaml

# 테스트 모드 (소량 데이터로 테스트)
python main.py --test-mode --sample-size 100

# 특정 단계만 실행
python main.py --steps md_processing,conversation_generation

# 상세 로그 출력
python main.py --verbose --log-level DEBUG
```

### 테스트 명령어
```bash
# 전체 테스트 실행
python run_tests.py

# 특정 모듈 테스트
python -m pytest test_md_processor.py -v
python -m pytest test_openai_connector.py -v
python -m pytest test_unsloth_dataset.py -v

# 통합 테스트
python test_integration.py
```

### 개발 도구
```bash
# 코드 포맷팅
black .
isort .

# 코드 품질 검사
flake8 .
mypy .

# 테스트 커버리지
pytest --cov=. --cov-report=html
```

## API 설정
- **OpenAI 호환 API**: `http://123.37.28.120:9997/v1`
- **모델**: `qwen2.5-vl-instruct`
- **Qdrant**: `localhost:6333`
- **컬렉션**: `ws-7491d651ae044c78`

## 성능 최적화
- **배치 처리**: 기본 배치 크기 16-100
- **병렬 처리**: 최대 8개 동시 요청
- **메모리 관리**: 최대 시퀀스 길이 8192 토큰
- **비동기 처리**: asyncio 기반 비동기 파이프라인