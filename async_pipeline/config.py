"""
비동기 파이프라인 설정 관리
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class AsyncPipelineConfig:
    """비동기 파이프라인 설정"""
    
    # 배치 처리 설정
    batch_size: int = 32
    min_batch_size: int = 16
    max_batch_size: int = 100
    
    # 동시성 제어
    max_concurrent: int = 8
    max_queue_size: int = 1000
    
    # 백프레셔 설정
    enable_backpressure: bool = True
    backpressure_threshold: float = 0.8  # 큐 사용률 임계값
    backpressure_delay: float = 0.1  # 백프레셔 지연 시간 (초)
    
    # 성능 저하 설정
    enable_graceful_degradation: bool = True
    degradation_threshold: float = 0.9  # 리소스 사용률 임계값
    degradation_factor: float = 0.5  # 성능 저하 시 배치 크기 감소 비율
    
    # 타임아웃 설정
    task_timeout: float = 300.0  # 개별 작업 타임아웃 (초)
    batch_timeout: float = 600.0  # 배치 처리 타임아웃 (초)
    
    # 재시도 설정
    max_retries: int = 3
    retry_delay: float = 1.0
    retry_backoff_factor: float = 2.0
    
    def validate(self) -> None:
        """설정 유효성 검증"""
        if not (self.min_batch_size <= self.batch_size <= self.max_batch_size):
            raise ValueError(f"배치 크기는 {self.min_batch_size}와 {self.max_batch_size} 사이여야 합니다")
        
        if self.max_concurrent <= 0:
            raise ValueError("최대 동시 실행 수는 1 이상이어야 합니다")
        
        if not (0.0 < self.backpressure_threshold < 1.0):
            raise ValueError("백프레셔 임계값은 0과 1 사이여야 합니다")
        
        if not (0.0 < self.degradation_threshold < 1.0):
            raise ValueError("성능 저하 임계값은 0과 1 사이여야 합니다")
        
        if not (0.0 < self.degradation_factor < 1.0):
            raise ValueError("성능 저하 비율은 0과 1 사이여야 합니다")