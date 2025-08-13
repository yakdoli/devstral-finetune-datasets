#!/usr/bin/env python3
"""
MD 파일 파서 단위 테스트
MDParser, ContentPreprocessor, APISignatureExtractor 클래스의 기능을 테스트합니다.
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import json

from md_processor.parser import (
    MDParser, ContentPreprocessor, APISignatureExtractor, 
    MetadataExtractor, DocumentMetadata, create_parser
)


class TestAPISignatureExtractor(unittest.TestCase):
    """API 시그니처 추출기 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.extractor = APISignatureExtractor()
    
    def test_csharp_api_extraction(self):
        """C# API 추출 테스트"""
        csharp_code = """
public class GridControl : Control
{
    public string DataSource { get; set; }
    public event EventHandler SelectionChanged;
    
    public void RefreshData()
    {
        // Implementation
    }
    
    private bool ValidateData(string data)
    {
        return !string.IsNullOrEmpty(data);
    }
}
"""
        
        content = f"```csharp\n{csharp_code}\n```"
        signatures = self.extractor.extract_api_signatures(content)
        
        # API가 추출되었는지 확인
        self.assertGreater(len(signatures), 0)
        
        # 클래스, 프로퍼티, 이벤트, 메서드가 포함되어 있는지 확인
        api_types = {sig['type'] for sig in signatures}
        expected_types = {'class', 'property', 'event', 'method'}
        self.assertTrue(expected_types.issubset(api_types))
    
    def test_javascript_api_extraction(self):
        """JavaScript API 추출 테스트"""
        js_code = """
class ChartComponent {
    constructor(options) {
        this.options = options;
    }
    
    render() {
        // Implementation
    }
    
    updateData(data) {
        // Implementation
    }
}

function createChart(type, data) {
    return new ChartComponent({type, data});
}
"""
        
        content = f"```javascript\n{js_code}\n```"
        signatures = self.extractor.extract_api_signatures(content)
        
        # API가 추출되었는지 확인
        self.assertGreater(len(signatures), 0)
        
        # 클래스와 함수가 포함되어 있는지 확인
        api_types = {sig['type'] for sig in signatures}
        self.assertIn('class', api_types)
        self.assertIn('function', api_types)
    
    def test_generic_api_extraction(self):
        """일반적인 API 패턴 추출 테스트"""
        content = """
# Grid Component

Use `grid.setData(data)` to set the data source.
Call `grid.refresh()` to update the display.
The `validateInput(value)` function checks input validity.
"""
        
        signatures = self.extractor.extract_api_signatures(content)
        
        # 함수 호출 패턴이 추출되었는지 확인
        self.assertGreater(len(signatures), 0)
        
        # 함수명 확인
        function_names = {sig['name'] for sig in signatures}
        expected_names = {'setData', 'refresh', 'validateInput'}
        self.assertTrue(expected_names.issubset(function_names))
    
    def test_duplicate_removal(self):
        """중복 제거 테스트"""
        content = """
```csharp
public void TestMethod() { }
public void TestMethod() { }
public void AnotherMethod() { }
```
"""
        
        signatures = self.extractor.extract_api_signatures(content)
        
        # 중복이 제거되었는지 확인
        signature_texts = [sig['signature'] for sig in signatures]
        self.assertEqual(len(signature_texts), len(set(signature_texts)))


class TestContentPreprocessor(unittest.TestCase):
    """콘텐츠 전처리기 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.preprocessor = ContentPreprocessor()
    
    def test_basic_preprocessing(self):
        """기본 전처리 테스트"""
        content = """---
title: Test Document
author: Test Author
---

# Test Document   

This is a test document with   multiple   spaces.


And multiple blank lines.

```python
def test_function():
    return "Hello, World!"
```

- Item 1
- Item 2
  - Nested item

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
"""
        
        processed = self.preprocessor.preprocess_content(content)
        
        # YAML 프론트매터가 제거되었는지 확인
        self.assertNotIn('title: Test Document', processed)
        self.assertNotIn('author: Test Author', processed)
        
        # 코드 블록이 보존되었는지 확인
        self.assertIn('```python', processed)
        self.assertIn('def test_function():', processed)
        
        # 과도한 공백이 정리되었는지 확인
        self.assertNotIn('   multiple   spaces', processed)
        
        # 과도한 빈 줄이 정리되었는지 확인
        self.assertNotIn('\n\n\n', processed)
    
    def test_code_block_preservation(self):
        """코드 블록 보존 테스트"""
        content = """
# Test

Here's some code:

```csharp
public class TestClass
{
    public string Property { get; set; }
}
```

And inline code: `var x = 10;`
"""
        
        processed = self.preprocessor.preprocess_content(content)
        
        # 코드 블록이 그대로 보존되었는지 확인
        self.assertIn('```csharp', processed)
        self.assertIn('public class TestClass', processed)
        self.assertIn('`var x = 10;`', processed)
    
    def test_table_processing(self):
        """테이블 처리 테스트"""
        content = """
|Column1|Column2|Column3|
|---|---|---|
|Data1|Data2|Data3|
"""
        
        processed = self.preprocessor.preprocess_content(content)
        
        # 테이블이 정리되었는지 확인
        lines = processed.split('\n')
        table_lines = [line for line in lines if '|' in line]
        
        for line in table_lines:
            if line.strip():
                # 각 셀 주위에 공백이 있는지 확인
                self.assertTrue(line.startswith('| '))
                self.assertTrue(line.endswith(' |'))
    
    def test_list_processing(self):
        """리스트 처리 테스트"""
        content = """
*   Item 1
+   Item 2
-   Item 3
    *   Nested item

1.   First item
2.   Second item
"""
        
        processed = self.preprocessor.preprocess_content(content)
        
        # 리스트 마커가 통일되었는지 확인
        import re
        lines = processed.split('\n')
        unordered_items = [line for line in lines if re.match(r'^\s*-\s+', line)]
        self.assertGreater(len(unordered_items), 0)
        
        # 순서 있는 리스트가 정리되었는지 확인
        import re
        ordered_items = [line for line in lines if re.match(r'^\s*\d+\.\s+', line)]
        self.assertGreater(len(ordered_items), 0)


class TestMetadataExtractor(unittest.TestCase):
    """메타데이터 추출기 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.extractor = MetadataExtractor()
    
    def tearDown(self):
        """테스트 정리"""
        shutil.rmtree(self.temp_dir)
    
    def test_json_metadata_extraction(self):
        """JSON 메타데이터 추출 테스트"""
        json_data = {
            "document_name": "grid",
            "page_number": 5,
            "title": "Grid Component Page 5",
            "author": "Test Author",
            "version": "1.0"
        }
        
        json_file = self.temp_dir / "test.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)
        
        metadata = self.extractor.extract_from_json(json_file)
        
        self.assertIsNotNone(metadata)
        self.assertEqual(metadata.component, "grid")
        self.assertEqual(metadata.page, 5)
        self.assertIn("author", metadata.additional_metadata)
        self.assertIn("version", metadata.additional_metadata)
    
    def test_path_metadata_extraction(self):
        """경로 메타데이터 추출 테스트"""
        # output 디렉토리 패턴
        output_file = self.temp_dir / "output" / "chart.md"
        output_file.parent.mkdir(exist_ok=True)
        output_file.write_text("test content")
        
        metadata = self.extractor.extract_from_path(output_file)
        self.assertEqual(metadata.component, "chart")
        
        # md_staging 디렉토리 패턴
        staging_file = self.temp_dir / "md_staging" / "gauge" / "page_010.md"
        staging_file.parent.mkdir(parents=True, exist_ok=True)
        staging_file.write_text("test content")
        
        metadata = self.extractor.extract_from_path(staging_file)
        self.assertEqual(metadata.component, "gauge")
        self.assertEqual(metadata.page, "page_010")
    
    def test_api_signature_extraction_from_content(self):
        """콘텐츠에서 API 시그니처 추출 테스트"""
        content = """
# Grid Component

```csharp
public class GridControl
{
    public void SetData(object data) { }
}
```

Use `grid.refresh()` to update the display.
"""
        
        signatures = self.extractor.extract_api_signatures_from_content(content)
        
        self.assertGreater(len(signatures), 0)
        
        # C# 클래스와 메서드가 추출되었는지 확인
        api_types = {sig['type'] for sig in signatures}
        self.assertIn('class', api_types)


class TestDocumentMetadata(unittest.TestCase):
    """DocumentMetadata 클래스 테스트"""
    
    def test_metadata_creation(self):
        """메타데이터 생성 테스트"""
        metadata = DocumentMetadata(
            component="grid",
            page="page_001",
            source_path="/test/path.md",
            file_size=1024,
            custom_field="custom_value"
        )
        
        self.assertEqual(metadata.component, "grid")
        self.assertEqual(metadata.page, "page_001")
        self.assertEqual(metadata.source_path, "/test/path.md")
        self.assertEqual(metadata.file_size, 1024)
        self.assertIn("custom_field", metadata.additional_metadata)
    
    def test_to_dict_conversion(self):
        """딕셔너리 변환 테스트"""
        metadata = DocumentMetadata(
            component="chart",
            page=5,
            author="Test Author"
        )
        
        metadata_dict = metadata.to_dict()
        
        self.assertEqual(metadata_dict["component"], "chart")
        self.assertEqual(metadata_dict["page"], 5)
        self.assertIn("author", metadata_dict["additional_metadata"])


class TestMDParser(unittest.TestCase):
    """MDParser 클래스 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.parser = MDParser()
        
        # 테스트 MD 파일 생성
        self.test_content = """---
title: Test Grid Component
version: 1.0
---

# Grid Component

The Grid component provides data display functionality.

## Methods

```csharp
public class GridControl : Control
{
    public void SetData(object data)
    {
        // Set the data source
    }
    
    public void Refresh()
    {
        // Refresh the display
    }
}
```

## Usage

Use `grid.setData(data)` to set data and `grid.refresh()` to update.

### Features

- Data binding
- Sorting
- Filtering

| Feature | Supported |
|---------|-----------|
| Sorting | Yes       |
| Filtering | Yes     |
"""
        
        self.md_file = self.temp_dir / "md_staging" / "grid" / "page_001.md"
        self.md_file.parent.mkdir(parents=True, exist_ok=True)
        self.md_file.write_text(self.test_content)
        
        # 테스트 JSON 파일 생성
        self.json_data = {
            "document_name": "grid",
            "page_number": 1,
            "title": "Grid Component Page 1"
        }
        
        self.json_file = self.temp_dir / "md_staging" / "grid" / "page_001.json"
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(self.json_data, f)
    
    def tearDown(self):
        """테스트 정리"""
        shutil.rmtree(self.temp_dir)
    
    def test_parse_file_with_json(self):
        """JSON 메타데이터와 함께 파일 파싱 테스트"""
        result = self.parser.parse_file(self.md_file, self.json_file)
        
        # 기본 필드 확인
        self.assertIn("id", result)
        self.assertIn("title", result)
        self.assertIn("component", result)
        self.assertIn("page", result)
        self.assertIn("content", result)
        self.assertIn("raw_content", result)
        self.assertIn("api_signatures", result)
        self.assertIn("content_structure", result)
        self.assertIn("metadata", result)
        self.assertIn("quality_score", result)
        
        # 값 확인
        self.assertEqual(result["component"], "grid")
        self.assertEqual(result["page"], 1)
        self.assertGreater(len(result["content"]), 0)
        self.assertGreater(len(result["api_signatures"]), 0)
        self.assertGreater(result["quality_score"], 0.0)
    
    def test_parse_file_without_json(self):
        """JSON 메타데이터 없이 파일 파싱 테스트"""
        result = self.parser.parse_file(self.md_file)
        
        # 기본 필드가 있는지 확인
        self.assertIn("id", result)
        self.assertIn("component", result)
        self.assertEqual(result["component"], "grid")
    
    def test_api_signature_extraction(self):
        """API 시그니처 추출 테스트"""
        result = self.parser.parse_file(self.md_file, self.json_file)
        
        api_signatures = result["api_signatures"]
        self.assertGreater(len(api_signatures), 0)
        
        # C# API가 추출되었는지 확인
        csharp_apis = [sig for sig in api_signatures if sig['language'] == 'csharp']
        self.assertGreater(len(csharp_apis), 0)
        
        # 클래스와 메서드가 포함되어 있는지 확인
        api_types = {sig['type'] for sig in csharp_apis}
        self.assertIn('class', api_types)
        self.assertIn('method', api_types)
    
    def test_content_structure_analysis(self):
        """콘텐츠 구조 분석 테스트"""
        result = self.parser.parse_file(self.md_file, self.json_file)
        
        structure = result["content_structure"]
        
        # 구조 정보 확인
        self.assertGreater(structure["word_count"], 0)
        self.assertGreater(structure["header_count"], 0)
        self.assertGreater(structure["code_block_count"], 0)
        self.assertGreater(structure["list_item_count"], 0)
        self.assertGreater(structure["table_count"], 0)
        
        # 헤더 정보 확인
        self.assertIn("headers", structure)
        self.assertGreater(len(structure["headers"]), 0)
        
        # 복잡도 점수 확인
        self.assertIn("complexity_score", structure)
        self.assertGreater(structure["complexity_score"], 0.0)
    
    def test_quality_score_calculation(self):
        """품질 점수 계산 테스트"""
        result = self.parser.parse_file(self.md_file, self.json_file)
        
        quality_score = result["quality_score"]
        
        # 품질 점수가 적절한 범위에 있는지 확인
        self.assertGreaterEqual(quality_score, 0.0)
        self.assertLessEqual(quality_score, 1.0)
        
        # 콘텐츠가 풍부하므로 높은 점수를 받아야 함
        self.assertGreater(quality_score, 0.5)
    
    def test_error_handling(self):
        """오류 처리 테스트"""
        # 존재하지 않는 파일
        non_existent_file = self.temp_dir / "non_existent.md"
        result = self.parser.parse_file(non_existent_file)
        
        # 오류 결과가 반환되는지 확인
        self.assertIn("error", result["metadata"])
        self.assertEqual(result["quality_score"], 0.0)


class TestParserFactory(unittest.TestCase):
    """파서 팩토리 함수 테스트"""
    
    def test_create_parser(self):
        """파서 생성 테스트"""
        parser = create_parser()
        
        self.assertIsInstance(parser, MDParser)
        self.assertIsInstance(parser.preprocessor, ContentPreprocessor)
        self.assertIsInstance(parser.metadata_extractor, MetadataExtractor)


if __name__ == "__main__":
    # 로깅 설정
    import logging
    logging.basicConfig(level=logging.WARNING)  # 테스트 중 로그 최소화
    
    # 테스트 실행
    unittest.main(verbosity=2)