#!/usr/bin/env python3
"""
Qdrant 클라이언트 모듈
Qdrant 벡터 데이터베이스와의 연결을 관리합니다.
"""

import os
import logging
from typing import Optional, Dict, Any, List
from pathlib import Path
import qdrant_client
from qdrant_client import QdrantClient, models
from qdrant_client.http import models as http_models
from qdrant_client.http.exceptions import UnexpectedResponse

logger = logging.getLogger(__name__)


class QdrantClientConfig:
    """Qdrant 클라이언트 설정 클래스"""
    
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6333,
        api_key: Optional[str] = None,
        timeout: int = 30,
        collection_name: str = "ws-7491d651ae044c78",
        grpc_port: int = 6334,
        https: bool = False,
        prefer_grpc: bool = False
    ):
        """
        Qdrant 클라이언트 설정을 초기화합니다.
        
        Args:
            host: Qdrant 호스트 주소
            port: Qdrant HTTP 포트
            api_key: API 키 (선택적)
            timeout: 연결 타임아웃 (초)
            collection_name: 기본 컬렉션 이름
            grpc_port: Qdrant gRPC 포트
            https: HTTPS 사용 여부
            prefer_grpc: gRPC 사용 선호 여부
        """
        self.host = host
        self.port = port
        self.api_key = api_key
        self.timeout = timeout
        self.collection_name = collection_name
        self.grpc_port = grpc_port
        self.https = https
        self.prefer_grpc = prefer_grpc
        
        # 환경변수에서 값 가져오기
        self._load_from_env()
    
    def _load_from_env(self):
        """환경변수에서 설정 값을 로드합니다."""
        self.host = os.getenv("QDRANT_HOST", self.host)
        self.port = int(os.getenv("QDRANT_PORT", self.port))
        self.api_key = os.getenv("QDRANT_API_KEY", self.api_key)
        self.collection_name = os.getenv("QDRANT_COLLECTION", self.collection_name)
        self.timeout = int(os.getenv("QDRANT_TIMEOUT", self.timeout))
        self.https = os.getenv("QDRANT_HTTPS", "false").lower() == "true"
        self.prefer_grpc = os.getenv("QDRANT_PREFER_GRPC", "false").lower() == "true"


class QdrantConnectionManager:
    """Qdrant 연결 관리 클래스"""
    
    def __init__(self, config: QdrantClientConfig):
        """
        Qdrant 연결 관리자를 초기화합니다.
        
        Args:
            config: Qdrant 클라이언트 설정
        """
        self.config = config
        self.client: Optional[QdrantClient] = None
        self.is_connected = False
        self.connection_error: Optional[str] = None
    
    def connect(self) -> bool:
        """
        Qdrant 서버에 연결합니다.
        
        Returns:
            연결 성공 여부
        """
        try:
            # 연결 옵션 설정
            url = f"http{'s' if self.config.https else ''}://{self.config.host}:{self.config.port}"
            
            # 클라이언트 생성
            self.client = QdrantClient(
                url=url,
                api_key=self.config.api_key,
                timeout=self.config.timeout,
                prefer_grpc=self.config.prefer_grpc
            )
            
            # 연결 테스트
            self.client.get_collections()
            self.is_connected = True
            self.connection_error = None
            
            logger.info(f"Successfully connected to Qdrant at {url}")
            return True
            
        except Exception as e:
            self.is_connected = False
            self.connection_error = str(e)
            logger.error(f"Failed to connect to Qdrant: {e}")
            return False
    
    def disconnect(self):
        """Qdrant 연결을 종료합니다."""
        if self.client:
            self.client = None
        self.is_connected = False
        logger.info("Disconnected from Qdrant")
    
    def ensure_connection(self) -> bool:
        """
        연결이 활성화되어 있는지 확인하고 필요시 연결합니다.
        
        Returns:
            연결 상태
        """
        if not self.is_connected:
            return self.connect()
        return True
    
    def get_client(self) -> Optional[QdrantClient]:
        """
        Qdrant 클라이언트를 반환합니다.
        
        Returns:
            Qdrant 클라이언트 인스턴스
        """
        if not self.ensure_connection():
            raise ConnectionError(f"Failed to connect to Qdrant: {self.connection_error}")
        return self.client
    
    def get_collection_info(self) -> Optional[Dict[str, Any]]:
        """
        컬렉션 정보를 가져옵니다.
        
        Returns:
            컬렉션 정보 딕셔너리
        """
        if not self.ensure_connection():
            return None
        
        try:
            collection_info = self.client.get_collection(self.config.collection_name)
            return {
                "name": self.config.collection_name,
                "status": collection_info.status,
                "vectors_count": collection_info.vectors_count,
                "config": collection_info.config.dict() if collection_info.config else None,
                "params": collection_info.params.dict() if collection_info.params else None
            }
        except Exception as e:
            logger.error(f"Failed to get collection info: {e}")
            return None
    
    def health_check(self) -> Dict[str, Any]:
        """
        Qdrant 서버 상태를 확인합니다.
        
        Returns:
            상태 정보 딕셔너리
        """
        if not self.ensure_connection():
            return {
                "status": "error",
                "message": self.connection_error,
                "connected": False
            }
        
        try:
            # 서버 상태 확인
            collections = self.client.get_collections()
            
            return {
                "status": "healthy",
                "connected": True,
                "host": self.config.host,
                "port": self.config.port,
                "collections": collections.result.collections,
                "collection_name": self.config.collection_name
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "connected": False
            }


class QdrantClientFactory:
    """Qdrant 클라이언트 팩토리 클래스"""
    
    @staticmethod
    def create_default_config() -> QdrantClientConfig:
        """
        기본 설정으로 Qdrant 클라이언트 설정을 생성합니다.
        
        Returns:
            기본 설정으로 생성된 QdrantClientConfig
        """
        return QdrantClientConfig()
    
    @staticmethod
    def create_from_env() -> QdrantClientConfig:
        """
        환경변수에서 설정을 읽어 Qdrant 클라이언트 설정을 생성합니다.
        
        Returns:
            환경변수로 생성된 QdrantClientConfig
        """
        return QdrantClientConfig()
    
    @staticmethod
    def create_connection_manager(config: QdrantClientConfig) -> QdrantConnectionManager:
        """
        Qdrant 연결 관리자를 생성합니다.
        
        Args:
            config: Qdrant 클라이언트 설정
            
        Returns:
            QdrantConnectionManager 인스턴스
        """
        return QdrantConnectionManager(config)


# 전역 클라이언트 인스턴스
_global_client_manager: Optional[QdrantConnectionManager] = None


def get_global_client_manager() -> Optional[QdrantConnectionManager]:
    """
    전역 클라이언트 관리자를 반환합니다.
    
    Returns:
        전역 QdrantConnectionManager 인스턴스
    """
    global _global_client_manager
    return _global_client_manager


def set_global_client_manager(manager: QdrantConnectionManager):
    """
    전역 클라이언트 관리자를 설정합니다.
    
    Args:
        manager: QdrantConnectionManager 인스턴스
    """
    global _global_client_manager
    _global_client_manager = manager


def create_qdrant_client(
    host: str = "localhost",
    port: int = 6333,
    api_key: Optional[str] = None,
    collection_name: str = "ws-7491d651ae044c78"
) -> QdrantConnectionManager:
    """
    Qdrant 클라이언트를 생성합니다.
    
    Args:
        host: Qdrant 호스트 주소
        port: Qdrant 포트
        api_key: API 키
        collection_name: 컬렉션 이름
        
    Returns:
        QdrantConnectionManager 인스턴스
    """
    config = QdrantClientConfig(
        host=host,
        port=port,
        api_key=api_key,
        collection_name=collection_name
    )
    
    manager = QdrantConnectionManager(config)
    set_global_client_manager(manager)
    
    return manager


if __name__ == "__main__":
    # 테스트 코드
    logging.basicConfig(level=logging.INFO)
    
    # 기본 클라이언트 생성
    client_manager = create_qdrant_client()
    
    # 연결 테스트
    if client_manager.connect():
        print("Qdrant 연결 성공!")
        
        # 상태 확인
        health = client_manager.health_check()
        print(f"상태: {health}")
        
        # 컬렉션 정보 확인
        collection_info = client_manager.get_collection_info()
        if collection_info:
            print(f"컬렉션 정보: {collection_info}")
        
        client_manager.disconnect()
    else:
        print(f"Qdrant 연결 실패: {client_manager.connection_error}")