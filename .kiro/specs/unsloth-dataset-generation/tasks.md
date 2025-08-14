# Implementation Plan

- [x] 1. 프로젝트 구조 및 핵심 인터페이스 설정
  - 디렉토리 구조 생성 (md_processor, openai_connector, qdrant_connector, unsloth_dataset, quality_validator)
  - 각 모듈의 기본 __init__.py 파일 및 메인 클래스 인터페이스 정의
  - 공통 설정 관리 클래스 및 데이터 모델 구현
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

- [x] 2. MD 파일 처리 모듈 구현
- [x] 2.1 MD 파일 스캐너 및 메타데이터 추출기 구현
  - MDFileScanner 클래스로 재귀적 파일 스캔 기능 구현
  - 파일 메타데이터 추출 (컴포넌트명, 페이지 번호, 콘텐츠 구조)
  - 단위 테스트 작성 (파일 스캔, 메타데이터 추출)
  - _Requirements: 1.1, 1.2_

- [x] 2.2 MD 콘텐츠 파서 및 전처리기 구현
  - MDParser 클래스로 마크다운 파싱 및 구조 분석
  - ContentPreprocessor로 텍스트 정규화 및 코드 예제 보존
  - API 시그니처 자동 추출 기능 구현
  - 단위 테스트 작성 (파싱, 전처리, API 추출)
  - _Requirements: 1.3, 10.1, 10.2_

- [x] 2.3 MD 처리 파이프라인 통합 및 오류 처리
  - MDProcessor 메인 클래스 구현
  - 오류 처리 및 로깅 시스템 통합
  - 구조화된 JSON 메타데이터 생성
  - 통합 테스트 작성
  - _Requirements: 1.4, 1.5, 7.1, 7.2_

- [x] 3. Qdrant 벡터 데이터베이스 연동 모듈 구현
- [x] 3.1 Qdrant 연결 관리자 및 기본 검색 기능 구현
  - QdrantConnectionManager로 연결 관리 및 상태 모니터링
  - 기본 연결 설정 (100.88.88.88:6333, collection: ws-7491d651ae044c78)
  - 연결 실패 시 재시도 로직 (최대 3회, 지수적 백오프)
  - 단위 테스트 작성 (연결, 재시도 로직)
  - _Requirements: 2.1, 2.4_

- [x] 3.2 의미적 검색 및 컨텍스트 검색 구현
  - QdrantDocumentSearcher로 의미적 유사도 검색
  - 유사도 임계값 0.7 이상 결과 필터링
  - 배치 검색 및 메타데이터 기반 검색 지원
  - 단위 테스트 작성 (검색, 필터링, 배치 처리)
  - _Requirements: 2.2, 2.3_

- [x] 3.3 검색 결과 변환 및 통합 처리기 구현
  - QdrantDataTransformer로 검색 결과 정규화
  - IntegratedDocumentProcessor로 로컬 문서와 벡터 DB 통합
  - 컨텍스트 포맷팅 및 메타데이터 관리
  - 통합 테스트 작성
  - _Requirements: 2.5, 3.2_

- [x] 4. OpenAI 호환 API 연동 모듈 구현
- [x] 4.1 API 클라이언트 및 연결 관리 구현
  - OpenAIClient로 http://123.37.28.120:9997/v1 엔드포인트 연결
  - qwen2.5-vl-instruct 모델 설정
  - API 호출 실패 시 재시도 로직 및 속도 제한
  - 단위 테스트 작성 (연결, 재시도, 속도 제한)
  - _Requirements: 3.1, 3.4_

- [x] 4.2 프롬프트 엔진 및 템플릿 관리 구현
  - PromptEngine으로 프롬프트 템플릿 관리
  - Syncfusion WinForms 전용 프롬프트 템플릿 작성
  - 컨텍스트 기반 동적 프롬프트 생성
  - 단위 테스트 작성 (템플릿 관리, 프롬프트 생성)
  - _Requirements: 3.2, 10.3_

- [x] 4.3 대화 생성기 및 토큰 관리 구현
  - ConversationGenerator로 대화 생성 로직
  - TokenManager로 8192 토큰 제한 관리
  - 대화 품질 제어 및 기술적 정확성 검증
  - 단위 테스트 작성 (대화 생성, 토큰 관리)
  - _Requirements: 3.3, 3.5, 6.3_

- [x] 5. Unsloth 데이터셋 생성 모듈 구현
- [x] 5.1 다중 포맷 변환기 구현
  - ShareGPTFormatter로 ShareGPT 포맷 변환 (human/gpt 역할)
  - AlpacaFormatter로 Alpaca 포맷 변환 (instruction-input-output)
  - OpenAIFormatter로 OpenAI 포맷 변환 (messages 배열)
  - 단위 테스트 작성 (각 포맷 변환)
  - _Requirements: 4.1, 4.2, 4.3, 4.4_

- [x] 5.2 Unsloth 호환성 검증기 구현
  - UnslothValidator로 Unsloth 프레임워크 호환성 검증
  - 데이터 구조 및 필드명 검증
  - 자동 포맷 수정 기능
  - 단위 테스트 작성 (호환성 검증, 자동 수정)
  - _Requirements: 9.1, 9.2, 9.3, 9.4_

- [x] 5.3 데이터셋 생성기 및 분할 기능 구현
  - UnslothDatasetGenerator 메인 클래스 구현
  - 훈련/검증 데이터셋 분할 (80/20)
  - JSONL 포맷으로 UTF-8 인코딩 출력
  - 통합 테스트 작성
  - _Requirements: 4.5, 9.5_

- [x] 6. 품질 검증 모듈 구현
- [x] 6.1 안전성 필터 및 중복 제거기 구현
  - SafetyFilter로 부적절한 콘텐츠 필터링
  - DuplicateRemover로 0.9 이상 유사도 중복 제거
  - 편향성 및 유해 콘텐츠 탐지
  - 단위 테스트 작성 (안전성 검사, 중복 탐지)
  - _Requirements: 5.2, 5.3_

- [x] 6.2 품질 점수 계산기 구현
  - QualityScorer로 ROUGE, BERT-score 기반 품질 점수 계산
  - 0.6 미만 품질 점수 샘플 플래그/제거
  - 커스텀 메트릭 추가 (기술적 정확성, 일관성)
  - 단위 테스트 작성 (품질 점수 계산)
  - _Requirements: 5.1, 5.4_

- [x] 6.3 자동 수정기 및 통계 분석기 구현
  - AutoCorrector로 일반적인 포맷 문제 자동 수정
  - StatisticsAnalyzer로 데이터셋 통계 분석
  - 상세한 품질 리포트 생성
  - 통합 테스트 작성
  - _Requirements: 5.5, 7.3_

- [x] 7. 배치 처리 및 성능 최적화 구현
- [x] 7.1 비동기 배치 처리 시스템 구현
  - AsyncPipelineManager로 비동기 파이프라인 관리
  - 설정 가능한 배치 크기 (16-100) 및 동시 요청 제한 (최대 8개)
  - 백프레셔 및 우아한 성능 저하 구현
  - 단위 테스트 작성 (배치 처리, 동시성 제어)
  - _Requirements: 6.1, 6.2, 6.4_

- [x] 7.2 메모리 관리 및 리소스 모니터링 구현
  - MemoryManager로 메모리 사용량 모니터링
  - 동적 배치 크기 조정 및 캐시 관리
  - 리소스 제약 시 자동 조정
  - 단위 테스트 작성 (메모리 관리, 리소스 모니터링)
  - _Requirements: 6.3, 6.4_

- [x] 7.3 진행률 표시 및 성능 메트릭 구현
  - 실시간 진행률 표시 (tqdm 기반)
  - ETA 계산 및 처리 속도 모니터링
  - 성능 메트릭 수집 및 리포팅
  - 통합 테스트 작성
  - _Requirements: 6.5, 7.3_

- [x] 8. 로깅 및 모니터링 시스템 구현
- [x] 8.1 구조화된 로깅 시스템 구현
  - StructuredLogger로 INFO, WARNING, ERROR 레벨 로깅
  - 컨텍스트 포함 오류 로깅 및 스택 트레이스
  - 콘솔 및 파일 로깅 (로테이션 지원)
  - 단위 테스트 작성 (로깅 레벨, 포맷)
  - _Requirements: 7.1, 7.2, 7.5_

- [x] 8.2 메트릭 수집 및 상태 모니터링 구현
  - MetricsCollector로 처리 성능 및 품질 메트릭 수집
  - HealthChecker로 시스템 상태 검사
  - 상세 디버그 정보 출력 (verbose 모드)
  - 단위 테스트 작성 (메트릭 수집, 상태 검사)
  - _Requirements: 7.3, 7.4_

- [x] 9. CLI 인터페이스 및 설정 관리 구현
- [x] 9.1 CLI 인터페이스 및 명령어 파서 구현
  - Click/Typer 기반 사용자 친화적 CLI 인터페이스
  - 명확한 도움말 문서 및 사용 예제
  - 선택적 파이프라인 단계 실행 지원
  - 단위 테스트 작성 (CLI 명령어, 파라미터 검증)
  - _Requirements: 8.1, 8.3_

- [x] 9.2 YAML 설정 관리 및 검증 구현
  - PipelineConfig 데이터클래스 기반 설정 관리
  - YAML 설정 파일 로딩 및 검증
  - 환경 변수 지원 및 기본값 제공
  - 단위 테스트 작성 (설정 로딩, 검증)
  - _Requirements: 8.2, 8.4_

- [x] 9.3 테스트 모드 및 오류 처리 구현
  - 소량 샘플 처리 테스트 모드
  - 유효하지 않은 파라미터에 대한 도움말 메시지
  - 통합 오류 처리 및 사용자 친화적 오류 메시지
  - 통합 테스트 작성
  - _Requirements: 8.4, 8.5_

- [x] 10. 파이프라인 통합 및 오케스트레이션 구현
- [x] 10.1 파이프라인 오케스트레이터 구현
  - PipelineOrchestrator로 전체 파이프라인 조정
  - 모듈 간 데이터 흐름 관리
  - 단계별 실행 및 체크포인트 지원
  - 단위 테스트 작성 (파이프라인 조정, 데이터 흐름)
  - _Requirements: 전체 요구사항 통합_

- [x] 10.2 컴포넌트별 데이터셋 조직화 구현
  - Syncfusion 컴포넌트별 데이터셋 그룹화
  - 컴포넌트 계층 구조 유지
  - 타겟 훈련을 위한 카테고리별 분할
  - 통합 테스트 작성
  - _Requirements: 10.4, 10.5_

- [x] 10.3 최종 통합 테스트 및 성능 검증
  - 전체 파이프라인 end-to-end 테스트
  - 대용량 데이터셋 처리 성능 테스트
  - Unsloth 프레임워크와의 실제 호환성 검증
  - 최종 품질 검증 및 리포트 생성
  - _Requirements: 모든 요구사항 검증_

- [ ] 11. 문서화 및 배포 준비
- [ ] 11.1 사용자 문서 및 API 문서 작성
  - README.md 작성 (설치, 사용법, 예제)
  - API 문서 생성 (docstring 기반)
  - 설정 파일 예제 및 튜토리얼
  - 문서 테스트 작성

- [ ] 11.2 패키징 및 의존성 관리
  - requirements.txt 최종 정리
  - setup.py 또는 pyproject.toml 작성
  - Docker 컨테이너 지원 (선택사항)
  - 배포 스크립트 작성