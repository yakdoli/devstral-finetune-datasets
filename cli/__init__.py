"""
CLI 모듈 - 사용자 친화적인 명령행 인터페이스

이 모듈은 Click 기반의 사용자 친화적인 CLI 인터페이스를 제공합니다.
다음 기능들을 지원합니다:

- 데이터셋 생성 파이프라인 실행
- 선택적 파이프라인 단계 실행
- 설정 파일 검증 및 생성
- 테스트 모드 지원
- 상세한 도움말 및 사용 예제

사용 예시:
    python -m cli generate --config config.yaml --test-mode
    python -m cli list-steps
    python -m cli validate-config --config config.yaml
"""

from .main import cli, main, PIPELINE_STEPS, OUTPUT_FORMATS

__all__ = [
    'cli', 
    'main', 
    'PIPELINE_STEPS', 
    'OUTPUT_FORMATS'
]

__version__ = "1.0.0"