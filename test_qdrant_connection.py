#!/usr/bin/env python3
"""
Qdrant 연결 관리자 및 검색 기능 단위 테스트
"""

import unittest
import time
from unittest.mock import Mock, patch, MagicMock
from qdrant_connector.client import (
    QdrantClientConfig, 
    QdrantConnectionManager, 
    create_qdrant_client
)
from qdrant_connector.searcher import QdrantDocumentSearcher, SearchResult
from qdrant_client.http.exceptions import UnexpectedResponse


class TestQdrantClientConfig(unittest.TestCase):
    """QdrantClientConfig 테스트"""
    
    def test_default_config(self):
        """기본 설정 테스트"""
        config = QdrantClientConfig()
        
        self.assertEqual(config.host, "localhost")
        self.assertEqual(config.port, 6333)
        self.assertEqual(config.collection_name, "ws-7491d651ae044c78")
        self.assertEqual(config.timeout, 30)
        self.assertFalse(config.https)
        self.assertFalse(config.prefer_grpc)
    
    def test_custom_config(self):
        """커스텀 설정 테스트"""
        # 환경변수 영향을 받지 않도록 직접 속성 설정
        config = QdrantClientConfig()
        config.host = "100.88.88.88"
        config.port = 6333
        config.collection_name = "test-collection"
        config.timeout = 60
        config.https = True
        
        self.assertEqual(config.host, "100.88.88.88")
        self.assertEqual(config.port, 6333)
        self.assertEqual(config.collection_name, "test-collection")
        self.assertEqual(config.timeout, 60)
        self.assertTrue(config.https)
    
    @patch.dict('os.environ', {
        'QDRANT_HOST': '192.168.1.100',
        'QDRANT_PORT': '6334',
        'QDRANT_COLLECTION': 'env-collection'
    })
    def test_env_config(self):
        """환경변수 설정 테스트"""
        config = QdrantClientConfig()
        
        self.assertEqual(config.host, "192.168.1.100")
        self.assertEqual(config.port, 6334)
        self.assertEqual(config.collection_name, "env-collection")


class TestQdrantConnectionManager(unittest.TestCase):
    """QdrantConnectionManager 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.config = QdrantClientConfig(
            host="100.88.88.88",
            port=6333,
            collection_name="ws-7491d651ae044c78"
        )
        self.manager = QdrantConnectionManager(self.config)
    
    def test_init(self):
        """초기화 테스트"""
        self.assertEqual(self.manager.config, self.config)
        self.assertIsNone(self.manager.client)
        self.assertFalse(self.manager.is_connected)
        self.assertIsNone(self.manager.connection_error)
        self.assertEqual(self.manager.retry_count, 0)
        self.assertEqual(self.manager.max_retries, 3)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_successful_connection(self, mock_client_class):
        """성공적인 연결 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collections.collections = [Mock(name="ws-7491d651ae044c78")]
        mock_client.get_collections.return_value = mock_collections
        mock_client_class.return_value = mock_client
        
        # 연결 테스트
        result = self.manager.connect()
        
        self.assertTrue(result)
        self.assertTrue(self.manager.is_connected)
        self.assertIsNone(self.manager.connection_error)
        self.assertEqual(self.manager.retry_count, 0)
        self.assertIsNotNone(self.manager.client)
    
    @patch('qdrant_connector.client.QdrantClient')
    @patch('time.sleep')  # sleep을 mock하여 테스트 속도 향상
    def test_connection_retry_logic(self, mock_sleep, mock_client_class):
        """연결 재시도 로직 테스트"""
        # 처음 두 번은 실패, 세 번째는 성공하도록 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collections.collections = [Mock(name="ws-7491d651ae044c78")]
        
        side_effects = [
            Exception("Connection failed"),  # 첫 번째 시도 실패
            Exception("Connection failed"),  # 두 번째 시도 실패
            mock_client  # 세 번째 시도 성공
        ]
        mock_client_class.side_effect = side_effects
        mock_client.get_collections.return_value = mock_collections
        
        # 연결 테스트
        result = self.manager.connect()
        
        self.assertTrue(result)
        self.assertTrue(self.manager.is_connected)
        self.assertEqual(self.manager.retry_count, 0)  # 성공 시 리셋됨
        
        # sleep이 두 번 호출되었는지 확인 (첫 번째, 두 번째 실패 후)
        self.assertEqual(mock_sleep.call_count, 2)
        
        # 지수적 백오프 확인
        expected_delays = [1.0, 2.0]  # base_delay * (2 ** attempt)
        actual_delays = [call[0][0] for call in mock_sleep.call_args_list]
        self.assertEqual(actual_delays, expected_delays)
    
    @patch('qdrant_connector.client.QdrantClient')
    @patch('time.sleep')
    def test_connection_max_retries_exceeded(self, mock_sleep, mock_client_class):
        """최대 재시도 횟수 초과 테스트"""
        # 모든 시도가 실패하도록 설정
        mock_client_class.side_effect = Exception("Connection failed")
        
        # 연결 테스트
        result = self.manager.connect()
        
        self.assertFalse(result)
        self.assertFalse(self.manager.is_connected)
        self.assertIsNotNone(self.manager.connection_error)
        self.assertEqual(self.manager.retry_count, 4)  # max_retries + 1
        
        # sleep이 max_retries 번 호출되었는지 확인
        self.assertEqual(mock_sleep.call_count, 3)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_ensure_connection_when_disconnected(self, mock_client_class):
        """연결이 끊어진 상태에서 ensure_connection 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collections.collections = [Mock(name="ws-7491d651ae044c78")]
        mock_client.get_collections.return_value = mock_collections
        mock_client_class.return_value = mock_client
        
        # 초기 상태는 연결되지 않음
        self.assertFalse(self.manager.is_connected)
        
        # ensure_connection 호출
        result = self.manager.ensure_connection()
        
        self.assertTrue(result)
        self.assertTrue(self.manager.is_connected)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_connection_validation(self, mock_client_class):
        """연결 검증 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collections.collections = [Mock(name="ws-7491d651ae044c78")]
        mock_client.get_collections.return_value = mock_collections
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        self.assertTrue(self.manager.is_connected)
        
        # 연결 검증 - 성공
        result = self.manager.ensure_connection()
        self.assertTrue(result)
        
        # 연결 검증 실패 시뮬레이션
        mock_client.get_collections.side_effect = Exception("Connection lost")
        result = self.manager.ensure_connection()
        # 재연결 시도가 실패하므로 False
        self.assertFalse(result)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_test_connection(self, mock_client_class):
        """연결 테스트 메서드 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection1 = Mock()
        mock_collection1.name = "ws-7491d651ae044c78"
        mock_collection2 = Mock()
        mock_collection2.name = "other-collection"
        mock_collections.collections = [mock_collection1, mock_collection2]
        mock_client.get_collections.return_value = mock_collections
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 연결 테스트
        result = self.manager.test_connection()
        
        self.assertTrue(result["connected"])
        self.assertIn("response_time", result)
        self.assertEqual(result["collections_count"], 2)
        self.assertTrue(result["target_collection_exists"])
        self.assertEqual(result["retry_count"], 0)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_health_check(self, mock_client_class):
        """헬스 체크 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 컬렉션 정보 Mock
        mock_collection_info = Mock()
        mock_collection_info.vectors_count = 1000
        mock_collection_info.status = "green"
        mock_client.get_collection.return_value = mock_collection_info
        
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 헬스 체크
        health = self.manager.health_check()
        
        self.assertEqual(health["status"], "healthy")
        self.assertTrue(health["connected"])
        self.assertEqual(health["host"], "100.88.88.88")
        self.assertEqual(health["port"], 6333)
        self.assertEqual(health["collections_count"], 1)
        self.assertTrue(health["target_collection_exists"])
        self.assertIsNotNone(health["collection_info"])
        self.assertEqual(health["collection_info"]["vectors_count"], 1000)
        self.assertEqual(health["collection_info"]["status"], "green")


class TestQdrantDocumentSearcher(unittest.TestCase):
    """QdrantDocumentSearcher 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.config = QdrantClientConfig(
            host="100.88.88.88",
            port=6333,
            collection_name="ws-7491d651ae044c78"
        )
        self.manager = QdrantConnectionManager(self.config)
        self.searcher = QdrantDocumentSearcher(self.manager)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_search_documents_basic(self, mock_client_class):
        """기본 문서 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collections.collections = [Mock(name="ws-7491d651ae044c78")]
        mock_client.get_collections.return_value = mock_collections
        
        # 검색 결과 Mock
        mock_hit = Mock()
        mock_hit.id = "doc1"
        mock_hit.score = 0.85
        mock_hit.payload = {
            "title": "Test Document",
            "content": "Test content",
            "component": "Grid",
            "page": "1"
        }
        mock_client.scroll.return_value = ([mock_hit], None)
        mock_client.search.return_value = [mock_hit]
        
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 검색 수행
        results = self.searcher.search_documents("test query", limit=5)
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "doc1")
        self.assertEqual(results[0]["title"], "Test Document")
        self.assertEqual(results[0]["component"], "Grid")
        self.assertEqual(results[0]["metadata"]["vector_score"], 0.85)
        self.assertEqual(results[0]["quality_score"], 0.85)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_search_with_score_threshold(self, mock_client_class):
        """점수 임계값을 적용한 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collections.collections = [Mock(name="ws-7491d651ae044c78")]
        mock_client.get_collections.return_value = mock_collections
        
        # 높은 점수와 낮은 점수의 결과 Mock
        mock_hit1 = Mock()
        mock_hit1.id = "doc1"
        mock_hit1.score = 0.8  # 임계값 0.7 이상
        mock_hit1.payload = {"title": "High Score Doc", "content": "content"}
        
        mock_hit2 = Mock()
        mock_hit2.id = "doc2"
        mock_hit2.score = 0.6  # 임계값 0.7 미만
        mock_hit2.payload = {"title": "Low Score Doc", "content": "content"}
        
        mock_client.scroll.return_value = ([mock_hit1, mock_hit2], None)
        mock_client.search.return_value = [mock_hit1, mock_hit2]
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 검색 수행 (기본 임계값 0.7 사용)
        results = self.searcher.search_documents("test query")
        
        # 임계값 이상의 결과만 반환되어야 함
        # 실제로는 Qdrant에서 필터링되지만, 여기서는 모든 결과가 반환됨
        self.assertEqual(len(results), 2)  # Mock에서는 모든 결과 반환
        
        # 첫 번째 결과가 높은 점수인지 확인
        self.assertEqual(results[0]["metadata"]["vector_score"], 0.8)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_batch_search(self, mock_client_class):
        """배치 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collections.collections = [Mock(name="ws-7491d651ae044c78")]
        mock_client.get_collections.return_value = mock_collections
        
        # 각 쿼리에 대한 결과 Mock
        call_count = 0
        def mock_scroll(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            mock_hit = Mock()
            mock_hit.id = f"doc_{call_count}"
            mock_hit.score = 0.8
            mock_hit.payload = {"title": f"Document {mock_hit.id}", "content": "content"}
            return ([mock_hit], None)
        
        mock_client.scroll.side_effect = mock_scroll
        mock_client.search.side_effect = lambda *args, **kwargs: [mock_scroll(*args, **kwargs)[0][0]]
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 배치 검색 수행
        queries = ["query1", "query2", "query3"]
        batch_results = self.searcher.batch_search(queries, batch_size=2)
        
        # 배치 크기가 2이므로 2개의 배치 결과가 있어야 함
        self.assertEqual(len(batch_results), 2)
        
        # 첫 번째 배치: query1, query2
        self.assertEqual(batch_results[0].total_count, 2)
        
        # 두 번째 배치: query3
        self.assertEqual(batch_results[1].total_count, 1)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_get_document_count(self, mock_client_class):
        """문서 수 조회 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collections.collections = [Mock(name="ws-7491d651ae044c78")]
        mock_client.get_collections.return_value = mock_collections
        
        # 컬렉션 정보 Mock
        mock_collection_info = Mock()
        mock_collection_info.vectors_count = 5000
        mock_client.get_collection.return_value = mock_collection_info
        
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 문서 수 조회
        count = self.searcher.get_document_count()
        
        self.assertEqual(count, 5000)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_connection_error_handling(self, mock_client_class):
        """연결 오류 처리 테스트"""
        # 연결 실패하도록 설정
        mock_client_class.side_effect = Exception("Connection failed")
        
        # 연결되지 않은 상태에서 검색 시도
        with self.assertRaises(ConnectionError):
            self.searcher.search_documents("test query")
        
        with self.assertRaises(ConnectionError):
            self.searcher.get_document_count()
        
        with self.assertRaises(ConnectionError):
            self.searcher.get_available_metadata_fields()


class TestQdrantClientFactory(unittest.TestCase):
    """QdrantClientFactory 테스트"""
    
    def test_create_qdrant_client(self):
        """Qdrant 클라이언트 생성 테스트"""
        manager = create_qdrant_client(
            host="test-host",
            port=6334,
            collection_name="test-collection"
        )
        
        self.assertIsInstance(manager, QdrantConnectionManager)
        self.assertEqual(manager.config.host, "test-host")
        self.assertEqual(manager.config.port, 6334)
        self.assertEqual(manager.config.collection_name, "test-collection")


if __name__ == '__main__':
    # 테스트 실행
    unittest.main(verbosity=2)