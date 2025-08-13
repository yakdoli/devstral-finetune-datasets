#!/usr/bin/env python3
"""
Qdrant 검색 결과 변환 및 통합 처리기 단위 테스트
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from qdrant_connector.transformer import QdrantDataTransformer, DocumentTransformConfig
from qdrant_connector.integration import IntegratedDocumentProcessor, create_integrated_processor


class TestQdrantDataTransformer(unittest.TestCase):
    """QdrantDataTransformer 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.config = DocumentTransformConfig()
        self.transformer = QdrantDataTransformer(self.config)
    
    def test_transform_single_document(self):
        """단일 문서 변환 테스트"""
        # 테스트 Qdrant 문서
        qdrant_doc = {
            "id": "test_doc_001",
            "title": "Test Grid Document",
            "component": "Grid",
            "page": "page_001",
            "content": "This is a test document about Syncfusion Grid component.",
            "metadata": {
                "source": "qdrant",
                "collection": "ws-7491d651ae044c78",
                "vector_score": 0.85,
                "original_payload": {
                    "content": "This is a test document about Syncfusion Grid component.",
                    "filename": "grid_test.md",
                    "author": "test_user"
                }
            },
            "quality_score": 0.85
        }
        
        # 문서 변환
        transformed_doc = self.transformer.transform_document(qdrant_doc)
        
        # 검증
        self.assertIsNotNone(transformed_doc)
        self.assertEqual(transformed_doc["id"], "test_doc_001")
        self.assertEqual(transformed_doc["title"], "Test Grid Document")
        self.assertEqual(transformed_doc["component"], "Grid")
        self.assertEqual(transformed_doc["page"], "page_001")
        self.assertEqual(transformed_doc["quality_score"], 0.85)
        self.assertIn("metadata", transformed_doc)
        self.assertEqual(transformed_doc["metadata"]["source"], "qdrant")
    
    def test_transform_multiple_documents(self):
        """다중 문서 변환 테스트"""
        # 테스트 문서 목록
        qdrant_docs = [
            {
                "id": "doc1",
                "title": "Grid Document",
                "component": "Grid",
                "content": "Grid content",
                "quality_score": 0.8,
                "metadata": {"source": "qdrant"}
            },
            {
                "id": "doc2",
                "title": "Chart Document",
                "component": "Chart",
                "content": "Chart content",
                "quality_score": 0.9,
                "metadata": {"source": "qdrant"}
            }
        ]
        
        # 문서 변환
        transformed_docs = self.transformer.transform_documents(qdrant_docs)
        
        # 검증
        self.assertEqual(len(transformed_docs), 2)
        self.assertEqual(transformed_docs[0]["component"], "Grid")
        self.assertEqual(transformed_docs[1]["component"], "Chart")
    
    def test_quality_score_filtering(self):
        """품질 점수 필터링 테스트"""
        # 낮은 품질 점수 문서
        low_quality_doc = {
            "id": "low_quality",
            "title": "Low Quality Document",
            "content": "Low quality content",
            "quality_score": 0.05,  # 기본 임계값 0.1보다 낮음
            "metadata": {"source": "qdrant"}
        }
        
        # 변환 시도
        transformed_doc = self.transformer.transform_document(low_quality_doc)
        
        # 낮은 품질 점수로 인해 None 반환
        self.assertIsNone(transformed_doc)
    
    def test_content_normalization(self):
        """콘텐츠 정규화 테스트"""
        # 정규화가 필요한 문서
        messy_doc = {
            "id": "messy_doc",
            "title": "Messy Document",
            "content": "  This   has    multiple   spaces\n\n\nand   newlines  ",
            "quality_score": 0.8,
            "metadata": {"source": "qdrant"}
        }
        
        # 문서 변환
        transformed_doc = self.transformer.transform_document(messy_doc)
        
        # 정규화된 콘텐츠 확인
        self.assertIsNotNone(transformed_doc)
        normalized_content = transformed_doc["content"]
        self.assertNotIn("   ", normalized_content)  # 다중 공백 제거
        self.assertTrue(normalized_content.strip())  # 양 끝 공백 제거
    
    def test_component_inference(self):
        """컴포넌트 추론 테스트"""
        # 컴포넌트 정보가 없는 문서
        doc_without_component = {
            "id": "no_component",
            "title": "Document without component",
            "content": "This document talks about grid functionality and data table features.",
            "quality_score": 0.8,
            "metadata": {"source": "qdrant"}
        }
        
        # 문서 변환
        transformed_doc = self.transformer.transform_document(doc_without_component)
        
        # 컴포넌트 추론 확인
        self.assertIsNotNone(transformed_doc)
        self.assertEqual(transformed_doc["component"], "grid")  # 콘텐츠에서 추론
    
    def test_merge_with_local_documents(self):
        """로컬 문서와 병합 테스트"""
        # Qdrant 문서
        qdrant_docs = [
            {
                "id": "shared_doc",
                "title": "Shared Document (Qdrant)",
                "component": "Grid",
                "content": "Qdrant version",
                "quality_score": 0.8,
                "metadata": {"source": "qdrant", "vector_score": 0.85}
            },
            {
                "id": "qdrant_only",
                "title": "Qdrant Only Document",
                "component": "Chart",
                "content": "Only in Qdrant",
                "quality_score": 0.9,
                "metadata": {"source": "qdrant"}
            }
        ]
        
        # 로컬 문서
        local_docs = [
            {
                "id": "shared_doc",
                "title": "Shared Document (Local)",
                "component": "Grid",
                "content": "Local version",
                "quality_score": 0.9,
                "metadata": {"source": "local"}
            },
            {
                "id": "local_only",
                "title": "Local Only Document",
                "component": "PDF",
                "content": "Only in local",
                "quality_score": 0.7,
                "metadata": {"source": "local"}
            }
        ]
        
        # 문서 병합
        merged_docs = self.transformer.merge_with_local_documents(qdrant_docs, local_docs)
        
        # 검증
        self.assertEqual(len(merged_docs), 3)  # shared_doc, qdrant_only, local_only
        
        # ID로 문서 찾기
        merged_map = {doc["id"]: doc for doc in merged_docs}
        
        # 공유 문서는 로컬 버전 우선
        shared_doc = merged_map["shared_doc"]
        self.assertEqual(shared_doc["title"], "Shared Document (Local)")
        self.assertIn("qdrant_equivalent", shared_doc["metadata"])
        
        # Qdrant 전용 문서
        qdrant_only_doc = merged_map["qdrant_only"]
        self.assertEqual(qdrant_only_doc["metadata"]["source_type"], "qdrant_only")
        
        # 로컬 전용 문서
        local_only_doc = merged_map["local_only"]
        self.assertEqual(local_only_doc["metadata"]["source_type"], "local_only")
    
    def test_format_context_for_generation(self):
        """대화 생성용 컨텍스트 포맷팅 테스트"""
        # 테스트 문서들
        documents = [
            {
                "id": "doc1",
                "title": "Grid Basics",
                "component": "Grid",
                "page": "page_001",
                "content": "Grid component provides data visualization capabilities.",
                "quality_score": 0.9,
                "metadata": {"source": "qdrant", "vector_score": 0.85}
            },
            {
                "id": "doc2",
                "title": "Chart Features",
                "component": "Chart",
                "page": "page_002",
                "content": "Chart component supports various chart types.",
                "quality_score": 0.8,
                "metadata": {"source": "local"}
            }
        ]
        
        # 컨텍스트 포맷팅
        formatted_context = self.transformer.format_context_for_generation(
            documents=documents,
            max_context_length=1000,
            include_metadata=True
        )
        
        # 검증
        self.assertIsInstance(formatted_context, str)
        self.assertIn("Grid Basics", formatted_context)
        self.assertIn("Chart Features", formatted_context)
        self.assertIn("Component:", formatted_context)
        self.assertIn("Quality:", formatted_context)
        self.assertTrue(len(formatted_context) <= 1000)
    
    def test_create_conversation_context(self):
        """대화 컨텍스트 생성 테스트"""
        # 테스트 문서들
        documents = [
            {
                "id": "api_doc",
                "title": "Grid API Reference",
                "component": "Grid",
                "page": "api_001",
                "content": "```csharp\nGrid.SetData(data);\n```\nThis method sets the grid data.",
                "quality_score": 0.9,
                "metadata": {"source": "qdrant"}
            }
        ]
        
        # API 컨텍스트 생성
        context = self.transformer.create_conversation_context(
            documents=documents,
            query="How to set grid data?",
            context_type="api"
        )
        
        # 검증
        self.assertIn("formatted_context", context)
        self.assertIn("metadata", context)
        self.assertIn("source_documents", context)
        
        # 메타데이터 확인
        metadata = context["metadata"]
        self.assertEqual(metadata["document_count"], 1)
        self.assertEqual(metadata["context_type"], "api")
        self.assertEqual(metadata["query"], "How to set grid data?")
        self.assertIn("Grid", metadata["components"])
    
    def test_extract_api_examples(self):
        """API 예제 추출 테스트"""
        content = """
        Here's how to use the Grid component:
        
        ```csharp
        var grid = new Grid();
        grid.SetData(data);
        grid.Refresh();
        ```
        
        You can also call grid.UpdateColumns() method.
        """
        
        # API 예제 추출
        api_examples = self.transformer._extract_api_examples(content)
        
        # 검증
        self.assertIn("var grid = new Grid();", api_examples)
        self.assertIn("grid.UpdateColumns()", api_examples)
    
    def test_extract_key_points(self):
        """핵심 포인트 추출 테스트"""
        content = """
        Key features of the Grid component:
        
        • Data binding support
        • Sorting and filtering
        • **Custom cell rendering**
        
        1. First, initialize the grid
        2. Then, set the data source
        3. Finally, configure columns
        """
        
        # 핵심 포인트 추출
        key_points = self.transformer._extract_key_points(content)
        
        # 검증
        self.assertIn("Data binding support", key_points)
        self.assertIn("First, initialize the grid", key_points)
        self.assertIn("Custom cell rendering", key_points)


class TestIntegratedDocumentProcessor(unittest.TestCase):
    """IntegratedDocumentProcessor 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.processor = create_integrated_processor(
            qdrant_host="100.88.88.88",
            qdrant_port=6333,
            qdrant_collection="ws-7491d651ae044c78"
        )
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_connect_qdrant(self, mock_client_class):
        """Qdrant 연결 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        mock_client_class.return_value = mock_client
        
        # 연결 테스트
        success = self.processor.connect_qdrant()
        
        # 검증
        self.assertTrue(success)
        self.assertIsNotNone(self.processor.qdrant_searcher)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_create_conversation_context(self, mock_client_class):
        """대화 컨텍스트 생성 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 검색 결과 Mock
        mock_hit = Mock()
        mock_hit.id = "context_doc"
        mock_hit.payload = {
            "title": "Context Test Document",
            "content": "This is context for conversation generation.",
            "component": "Grid",
            "page": "page_001"
        }
        mock_client.scroll.return_value = ([mock_hit], None)
        mock_client_class.return_value = mock_client
        
        # 연결
        self.processor.connect_qdrant()
        
        # 컨텍스트 생성
        context = self.processor.create_conversation_context(
            query="How to use Grid component?",
            context_type="tutorial",
            max_documents=3
        )
        
        # 검증
        self.assertIn("formatted_context", context)
        self.assertIn("metadata", context)
        self.assertIn("source_documents", context)
        self.assertEqual(context["metadata"]["context_type"], "tutorial")
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_batch_create_contexts(self, mock_client_class):
        """배치 컨텍스트 생성 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 검색 결과 Mock
        mock_hit = Mock()
        mock_hit.id = "batch_doc"
        mock_hit.payload = {
            "title": "Batch Test Document",
            "content": "Batch context content.",
            "component": "Grid"
        }
        mock_client.scroll.return_value = ([mock_hit], None)
        mock_client_class.return_value = mock_client
        
        # 연결
        self.processor.connect_qdrant()
        
        # 배치 컨텍스트 생성
        queries = ["Grid usage", "Chart features", "PDF export"]
        contexts = self.processor.batch_create_contexts(
            queries=queries,
            context_type="general",
            max_documents=2
        )
        
        # 검증
        self.assertEqual(len(contexts), 3)
        for context in contexts:
            self.assertIn("formatted_context", context)
            self.assertIn("metadata", context)
    
    @patch('qdrant_connector.client.QdrantClient')
    def test_get_component_specific_context(self, mock_client_class):
        """컴포넌트별 컨텍스트 생성 테스트"""
        # Mock 클라이언트 설정
        mock_client = Mock()
        mock_collections = Mock()
        mock_collection = Mock()
        mock_collection.name = "ws-7491d651ae044c78"
        mock_collections.collections = [mock_collection]
        mock_client.get_collections.return_value = mock_collections
        
        # 컴포넌트별 검색 결과 Mock
        mock_hit = Mock()
        mock_hit.id = "grid_doc"
        mock_hit.payload = {
            "title": "Grid Component Guide",
            "content": "Comprehensive Grid component documentation.",
            "component": "Grid",
            "page": "grid_001"
        }
        mock_client.scroll.return_value = ([mock_hit], None)
        mock_client_class.return_value = mock_client
        
        # 연결
        self.processor.connect_qdrant()
        
        # 컴포넌트별 컨텍스트 생성
        context = self.processor.get_component_specific_context(
            component_name="Grid",
            context_type="api",
            max_documents=5
        )
        
        # 검증
        self.assertIn("formatted_context", context)
        self.assertIn("Grid", context["metadata"]["components"])
    
    def test_health_check(self):
        """상태 확인 테스트"""
        # 상태 확인
        health = self.processor.health_check()
        
        # 검증
        self.assertIn("qdrant", health)
        self.assertIn("md_processor", health)
        self.assertIn("auto_merge", health)
        self.assertIn("merge_strategy", health)


if __name__ == '__main__':
    # 테스트 실행
    unittest.main(verbosity=2)