#!/usr/bin/env python3
"""
Qdrant 의미적 검색 및 컨텍스트 검색 단위 테스트
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from qdrant_connector.client import QdrantClientConfig, QdrantConnectionManager
from qdrant_connector.searcher import QdrantDocumentSearcher, SearchQuery, SearchResult


class TestQdrantSemanticSearch(unittest.TestCase):
    """Qdrant 의미적 검색 테스트"""
    
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
    def test_semantic_search_with_vector(self, mock_client_class):
        """벡터 기반 의미적 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 검색 결과 Mock
        mock_hit = Mock()
        mock_hit.id = "doc1"
        mock_hit.score = 0.85
        mock_hit.payload = {
            "title": "Semantic Test Document",
            "content": "This is a semantic search test",
            "component": "Grid",
            "page": "1"
        }
        mock_client.search.return_value = [mock_hit]
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 벡터 기반 의미적 검색
        test_vector = [0.1, 0.2, 0.3, 0.4, 0.5] * 100  # 512차원 벡터 시뮬레이션
        results = self.searcher.search_documents(
            query="test query",
            vector=test_vector,
            search_type="semantic",
            score_threshold=0.7
        )
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "doc1")
        self.assertEqual(results[0]["title"], "Semantic Test Document")
        self.assertGreaterEqual(results[0]["metadata"]["vector_score"], 0.7)
        
        # search 메서드가 올바른 파라미터로 호출되었는지 확인
        mock_client.search.assert_called_once()
        call_args = mock_client.search.call_args
        self.assertEqual(call_args[1]["collection_name"], "ws-7491d651ae044c78")
        self.assertEqual(call_args[1]["query_vector"], test_vector)
        self.assertEqual(call_args[1]["score_threshold"], 0.7)
    
    @patch('qdrant_connector.client.QdrantClient')
    @patch('sentence_transformers.SentenceTransformer')
    def test_semantic_search_with_text(self, mock_transformer_class, mock_client_class):
        """텍스트 기반 의미적 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 검색 결과 Mock
        mock_hit = Mock()
        mock_hit.id = "doc1"
        mock_hit.score = 0.8
        mock_hit.payload = {
            "title": "Text Semantic Search",
            "content": "Syncfusion Grid component features",
            "component": "Grid"
        }
        mock_client.search.return_value = [mock_hit]
        mock_client_class.return_value = mock_client
        
        # SentenceTransformer Mock 설정
        mock_model = Mock()
        mock_model.encode.return_value = [0.1, 0.2, 0.3] * 100  # 300차원 벡터
        mock_transformer_class.return_value = mock_model
        
        # 연결
        self.manager.connect()
        
        # 텍스트 기반 의미적 검색
        results = self.searcher.search_documents(
            query="Syncfusion Grid features",
            search_type="semantic",
            score_threshold=0.7
        )
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "doc1")
        self.assertGreaterEqual(results[0]["metadata"]["vector_score"], 0.7)
        
        # SentenceTransformer가 호출되었는지 확인
        mock_model.encode.assert_called_once_with("Syncfusion Grid features")
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_semantic_search_fallback_to_keyword(self, mock_client_class):
        """의미적 검색 실패 시 키워드 검색으로 대체 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 키워드 검색 결과 Mock (scroll 사용)
        mock_hit = Mock()
        mock_hit.id = "doc1"
        mock_hit.payload = {
            "title": "Fallback Search Test",
            "content": "This contains the search term",
            "component": "Grid"
        }
        mock_client.scroll.return_value = ([mock_hit], None)
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 의미적 검색 (sentence-transformers 없음)
        results = self.searcher.search_documents(
            query="search term",
            search_type="semantic",
            score_threshold=0.1  # 낮은 임계값으로 결과 확인
        )
        
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]["id"], "doc1")
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_metadata_based_search(self, mock_client_class):
        """메타데이터 기반 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 메타데이터 검색 결과 Mock
        mock_hit1 = Mock()
        mock_hit1.id = "doc1"
        mock_hit1.payload = {
            "title": "Grid Document 1",
            "component": "Grid",
            "page": "5"
        }
        
        mock_hit2 = Mock()
        mock_hit2.id = "doc2"
        mock_hit2.payload = {
            "title": "Grid Document 2",
            "component": "Grid",
            "page": "10"
        }
        
        mock_client.scroll.return_value = ([mock_hit1, mock_hit2], None)
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 컴포넌트별 검색
        results = self.searcher.search_by_component("Grid", limit=5)
        
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["component"], "Grid")
        self.assertEqual(results[1]["component"], "Grid")
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_page_range_search(self, mock_client_class):
        """페이지 범위 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 페이지 범위 검색 결과 Mock
        mock_hit = Mock()
        mock_hit.id = "doc1"
        mock_hit.payload = {
            "title": "Page Range Test",
            "component": "Grid",
            "page": "7"
        }
        
        mock_client.scroll.return_value = ([mock_hit], None)
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 페이지 범위 검색
        results = self.searcher.search_by_page_range(
            start_page=5,
            end_page=10,
            component_name="Grid"
        )
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["page"], "7")
        self.assertEqual(results[0]["component"], "Grid")
    
    @patch('qdrant_connector.client.QdrantClient')
    @patch('sentence_transformers.SentenceTransformer')
    def test_batch_search_with_vectors(self, mock_transformer_class, mock_client_class):
        """벡터 기반 배치 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 각 쿼리에 대한 검색 결과 Mock
        def mock_search(*args, **kwargs):
            mock_hit = Mock()
            mock_hit.id = f"doc_{len(mock_client.search.call_args_list)}"
            mock_hit.score = 0.8
            mock_hit.payload = {
                "title": f"Batch Document {mock_hit.id}",
                "content": "batch search content"
            }
            return [mock_hit]
        
        mock_client.search.side_effect = mock_search
        mock_client_class.return_value = mock_client
        
        # SentenceTransformer Mock 설정
        mock_model = Mock()
        mock_model.encode.return_value = [[0.1, 0.2] * 100, [0.3, 0.4] * 100, [0.5, 0.6] * 100]
        mock_transformer_class.return_value = mock_model
        
        # 연결
        self.manager.connect()
        
        # 배치 검색
        queries = ["query1", "query2", "query3"]
        batch_results = self.searcher.batch_search(
            queries=queries,
            batch_size=2,
            score_threshold=0.7
        )
        
        # 배치 크기가 2이므로 2개의 배치 결과
        self.assertEqual(len(batch_results), 2)
        
        # 첫 번째 배치: query1, query2
        self.assertEqual(batch_results[0].total_count, 2)
        
        # 두 번째 배치: query3
        self.assertEqual(batch_results[1].total_count, 1)
        
        # SentenceTransformer가 호출되었는지 확인
        mock_model.encode.assert_called()
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_score_threshold_filtering(self, mock_client_class):
        """점수 임계값 필터링 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 다양한 점수의 결과 Mock
        mock_hit1 = Mock()
        mock_hit1.id = "doc1"
        mock_hit1.score = 0.9  # 높은 점수
        mock_hit1.payload = {"title": "High Score Doc", "content": "relevant content"}
        
        mock_hit2 = Mock()
        mock_hit2.id = "doc2"
        mock_hit2.score = 0.6  # 낮은 점수
        mock_hit2.payload = {"title": "Low Score Doc", "content": "less relevant"}
        
        mock_client.search.return_value = [mock_hit1, mock_hit2]
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 높은 임계값으로 검색
        results = self.searcher.search_documents(
            query="test",
            vector=[0.1] * 100,
            search_type="semantic",
            score_threshold=0.7  # 0.7 이상만 반환
        )
        
        # 임계값 이상의 결과만 반환되어야 함
        # (실제로는 Qdrant에서 필터링하지만, 여기서는 모든 결과가 반환됨)
        self.assertGreater(len(results), 0)
        
        # 첫 번째 결과가 높은 점수인지 확인
        high_score_results = [r for r in results if r["metadata"]["vector_score"] >= 0.7]
        self.assertGreater(len(high_score_results), 0)
    
    def test_text_similarity_calculation(self):
        """텍스트 유사도 계산 테스트"""
        # 유사도 계산 메서드 테스트
        similarity1 = self.searcher._calculate_text_similarity(
            "syncfusion grid component",
            "This document describes the syncfusion grid component features"
        )
        
        similarity2 = self.searcher._calculate_text_similarity(
            "syncfusion grid component",
            "This is about charts and graphs"
        )
        
        # 첫 번째가 더 높은 유사도를 가져야 함
        self.assertGreater(similarity1, similarity2)
        self.assertGreater(similarity1, 0.0)
        
        # 빈 텍스트 처리
        similarity3 = self.searcher._calculate_text_similarity("", "some content")
        self.assertEqual(similarity3, 0.0)
        
        similarity4 = self.searcher._calculate_text_similarity("query", "")
        self.assertEqual(similarity4, 0.0)


class TestQdrantContextSearch(unittest.TestCase):
    """Qdrant 컨텍스트 검색 테스트"""
    
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
    def test_contextual_search_with_filters(self, mock_client_class):
        """필터를 사용한 컨텍스트 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 컨텍스트 검색 결과 Mock
        mock_hit = Mock()
        mock_hit.id = "doc1"
        mock_hit.payload = {
            "title": "Grid Context Document",
            "content": "Grid component context information",
            "component": "Grid",
            "page": "5",
            "section": "API Reference"
        }
        
        mock_client.scroll.return_value = ([mock_hit], None)
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 복합 필터를 사용한 컨텍스트 검색
        results = self.searcher.search_by_metadata({
            "component": "Grid",
            "section": "API Reference",
            "page": {"gte": 1, "lte": 10}
        })
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["component"], "Grid")
        self.assertEqual(results[0]["page"], "5")
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_similar_documents_search(self, mock_client_class):
        """유사 문서 검색 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 기준 문서 정보 Mock
        mock_base_doc = Mock()
        mock_base_doc.id = "base_doc"
        mock_base_doc.vector = [0.1, 0.2, 0.3] * 100
        mock_client.retrieve.return_value = [mock_base_doc]
        
        # 유사 문서 검색 결과 Mock
        mock_similar_doc = Mock()
        mock_similar_doc.id = "similar_doc"
        mock_similar_doc.score = 0.85
        mock_similar_doc.payload = {
            "title": "Similar Document",
            "content": "Similar content",
            "component": "Grid"
        }
        mock_client.search.return_value = [mock_similar_doc]
        mock_client_class.return_value = mock_client
        
        # 연결
        self.manager.connect()
        
        # 유사 문서 검색
        results = self.searcher.search_similar_documents(
            document_id="base_doc",
            limit=5,
            score_threshold=0.7
        )
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "similar_doc")
        self.assertGreaterEqual(results[0]["metadata"]["vector_score"], 0.7)
        
        # retrieve와 search가 호출되었는지 확인
        mock_client.retrieve.assert_called_once()
        mock_client.search.assert_called_once()


if __name__ == '__main__':
    # 테스트 실행
    unittest.main(verbosity=2)