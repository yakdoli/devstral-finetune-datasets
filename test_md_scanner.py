#!/usr/bin/env python3
"""
MD 파일 스캐너 단위 테스트
MDFileScanner 클래스의 기능을 테스트합니다.
"""

import unittest
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
import json

from md_processor.scanner import MDFileScanner, FileMetadata, create_scanner


class TestFileMetadata(unittest.TestCase):
    """FileMetadata 클래스 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        
        # 테스트 MD 파일 생성
        self.test_md_content = """# Test Document

## Section 1
This is a test section with some content.

```python
def test_function():
    return "Hello, World!"
```

## Section 2
- Item 1
- Item 2

[Link to example](https://example.com)

![Test Image](test.png)

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
"""
        
        self.test_md_file = self.temp_dir / "test_component.md"
        with open(self.test_md_file, 'w', encoding='utf-8') as f:
            f.write(self.test_md_content)
    
    def tearDown(self):
        """테스트 정리"""
        shutil.rmtree(self.temp_dir)
    
    def test_file_metadata_creation(self):
        """파일 메타데이터 생성 테스트"""
        metadata = FileMetadata(self.test_md_file)
        
        # 기본 속성 확인
        self.assertEqual(metadata.file_path, self.test_md_file)
        self.assertGreater(metadata.file_size, 0)
        self.assertIsInstance(metadata.last_modified, datetime)
        self.assertIsInstance(metadata.file_hash, str)
        self.assertGreater(len(metadata.file_hash), 0)
    
    def test_component_name_extraction(self):
        """컴포넌트명 추출 테스트"""
        # output 디렉토리 패턴
        output_file = self.temp_dir / "output" / "grid.md"
        output_file.parent.mkdir(exist_ok=True)
        output_file.write_text("test content")
        
        metadata = FileMetadata(output_file)
        self.assertEqual(metadata.component_name, "grid")
        
        # md_staging 디렉토리 패턴
        staging_file = self.temp_dir / "md_staging" / "chart" / "page_001.md"
        staging_file.parent.mkdir(parents=True, exist_ok=True)
        staging_file.write_text("test content")
        
        metadata = FileMetadata(staging_file)
        self.assertEqual(metadata.component_name, "chart")
    
    def test_page_number_extraction(self):
        """페이지 번호 추출 테스트"""
        # page_XXX 패턴
        page_file = self.temp_dir / "page_042.md"
        page_file.write_text("test content")
        
        metadata = FileMetadata(page_file)
        self.assertEqual(metadata.page_number, 42)
        
        # 숫자만 있는 패턴
        num_file = self.temp_dir / "123.md"
        num_file.write_text("test content")
        
        metadata = FileMetadata(num_file)
        self.assertEqual(metadata.page_number, 123)
    
    def test_content_structure_analysis(self):
        """콘텐츠 구조 분석 테스트"""
        metadata = FileMetadata(self.test_md_file)
        structure = metadata.content_structure
        
        # 구조 요소 확인
        self.assertTrue(structure["has_headers"])
        self.assertTrue(structure["has_code_blocks"])
        self.assertTrue(structure["has_tables"])
        self.assertTrue(structure["has_images"])
        self.assertTrue(structure["has_links"])
        self.assertEqual(structure["estimated_sections"], 3)  # # + ## + ##
    
    def test_to_dict_conversion(self):
        """딕셔너리 변환 테스트"""
        metadata = FileMetadata(self.test_md_file)
        metadata_dict = metadata.to_dict()
        
        # 필수 키 확인
        required_keys = [
            "file_path", "file_size", "last_modified", "file_hash",
            "component_name", "page_number", "content_structure"
        ]
        
        for key in required_keys:
            self.assertIn(key, metadata_dict)
        
        # 타입 확인
        self.assertIsInstance(metadata_dict["file_path"], str)
        self.assertIsInstance(metadata_dict["file_size"], int)
        self.assertIsInstance(metadata_dict["last_modified"], str)
        self.assertIsInstance(metadata_dict["file_hash"], str)
        self.assertIsInstance(metadata_dict["content_structure"], dict)


class TestMDFileScanner(unittest.TestCase):
    """MDFileScanner 클래스 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        
        # 테스트 디렉토리 구조 생성
        self.output_dir = self.temp_dir / "output"
        self.staging_dir = self.temp_dir / "md_staging"
        
        self.output_dir.mkdir()
        self.staging_dir.mkdir()
        
        # 컴포넌트 파일 생성 (output 디렉토리)
        component_files = ["grid.md", "chart.md", "gauge.md"]
        for filename in component_files:
            file_path = self.output_dir / filename
            component_name = Path(filename).stem
            file_path.write_text(f"# {component_name} Component\n\nThis is the {component_name} component documentation.")
        
        # 페이지 파일 생성 (md_staging 디렉토리)
        components = ["grid", "chart"]
        for component in components:
            component_dir = self.staging_dir / component
            component_dir.mkdir()
            
            for i in range(1, 4):  # page_001.md ~ page_003.md
                md_file = component_dir / f"page_{i:03d}.md"
                json_file = component_dir / f"page_{i:03d}.json"
                
                md_content = f"# {component} Page {i}\n\nContent for page {i} of {component} component."
                md_file.write_text(md_content)
                
                json_content = {
                    "document_name": component,
                    "page_number": i,
                    "title": f"{component} Page {i}"
                }
                json_file.write_text(json.dumps(json_content, indent=2))
        
        # 스캐너 생성
        self.scanner = MDFileScanner([str(self.output_dir), str(self.staging_dir)])
    
    def tearDown(self):
        """테스트 정리"""
        shutil.rmtree(self.temp_dir)
    
    def test_scanner_initialization(self):
        """스캐너 초기화 테스트"""
        self.assertEqual(len(self.scanner.base_paths), 2)
        self.assertIn(self.output_dir, self.scanner.base_paths)
        self.assertIn(self.staging_dir, self.scanner.base_paths)
        self.assertEqual(self.scanner.supported_extensions, {'.md', '.markdown'})
    
    def test_scan_files(self):
        """파일 스캔 테스트"""
        files = list(self.scanner.scan_files())
        
        # 총 파일 수 확인 (컴포넌트 3개 + 페이지 6개)
        self.assertEqual(len(files), 9)
        
        # 모든 파일이 MD 파일인지 확인
        for file_path, metadata in files:
            self.assertTrue(file_path.suffix == '.md')
            self.assertIsInstance(metadata, FileMetadata)
    
    def test_find_md_json_pairs(self):
        """MD-JSON 쌍 찾기 테스트"""
        pairs = list(self.scanner.find_md_json_pairs())
        
        # 모든 파일에 대한 쌍이 있는지 확인
        self.assertEqual(len(pairs), 9)
        
        # JSON 파일이 있는 경우와 없는 경우 확인
        json_exists_count = sum(1 for _, json_path, _, json_metadata in pairs if json_path.exists())
        self.assertEqual(json_exists_count, 6)  # 페이지 파일들만 JSON이 있음
    
    def test_get_component_files(self):
        """컴포넌트 파일 가져오기 테스트"""
        component_files = list(self.scanner.get_component_files())
        
        # 컴포넌트 파일 수 확인
        self.assertEqual(len(component_files), 3)
        
        # 컴포넌트명 확인
        component_names = {metadata.component_name for _, metadata in component_files}
        expected_names = {"grid", "chart", "gauge"}
        self.assertEqual(component_names, expected_names)
    
    def test_get_page_files(self):
        """페이지 파일 가져오기 테스트"""
        page_files = list(self.scanner.get_page_files())
        
        # 페이지 파일 수 확인
        self.assertEqual(len(page_files), 6)
        
        # JSON 파일이 모두 존재하는지 확인
        for md_path, json_path, md_metadata, json_metadata in page_files:
            self.assertTrue(json_path.exists())
            self.assertIsNotNone(json_metadata)
            self.assertIsNotNone(md_metadata.page_number)
    
    def test_extract_metadata_from_files(self):
        """파일에서 메타데이터 추출 테스트"""
        metadata_list = self.scanner.extract_metadata_from_files()
        
        # 메타데이터 수 확인
        self.assertEqual(len(metadata_list), 9)
        
        # 파일 타입 확인
        component_count = sum(1 for meta in metadata_list if meta["file_type"] == "component")
        page_count = sum(1 for meta in metadata_list if meta["file_type"] == "page")
        
        self.assertEqual(component_count, 3)
        self.assertEqual(page_count, 6)
    
    def test_get_components_summary(self):
        """컴포넌트 요약 정보 테스트"""
        summary = self.scanner.get_components_summary()
        
        # 컴포넌트 수 확인
        self.assertEqual(len(summary), 3)  # grid, chart, gauge
        
        # grid와 chart는 페이지가 있어야 함
        self.assertEqual(len(summary["grid"]["pages"]), 3)
        self.assertEqual(len(summary["chart"]["pages"]), 3)
        
        # gauge는 컴포넌트 파일만 있어야 함
        self.assertEqual(len(summary["gauge"]["pages"]), 0)
        
        # 페이지 정렬 확인
        for component_name, component_info in summary.items():
            if component_info["pages"]:
                page_numbers = [page["page_number"] for page in component_info["pages"]]
                self.assertEqual(page_numbers, sorted(page_numbers))
    
    def test_get_scan_statistics(self):
        """스캔 통계 테스트"""
        stats = self.scanner.get_scan_statistics()
        
        # 기본 통계 확인
        self.assertEqual(stats["total_md_files"], 9)
        self.assertEqual(stats["total_json_files"], 6)
        self.assertEqual(stats["component_files"], 3)
        self.assertEqual(stats["page_files"], 6)
        self.assertEqual(stats["directories_scanned"], 2)
        self.assertEqual(stats["components_count"], 3)
        
        # 컴포넌트 목록 확인
        expected_components = {"grid", "chart", "gauge"}
        self.assertEqual(set(stats["components_found"]), expected_components)
        
        # 파일 크기 총합이 0보다 큰지 확인
        self.assertGreater(stats["file_size_total"], 0)
        
        # 콘텐츠 구조 요약 확인
        structure_summary = stats["content_structure_summary"]
        self.assertGreaterEqual(structure_summary["files_with_headers"], 0)
        self.assertIsInstance(structure_summary, dict)


class TestScannerFactory(unittest.TestCase):
    """스캐너 팩토리 함수 테스트"""
    
    def test_create_scanner_default(self):
        """기본 스캐너 생성 테스트"""
        scanner = create_scanner()
        
        self.assertIsInstance(scanner, MDFileScanner)
        self.assertEqual(len(scanner.base_paths), 2)
    
    def test_create_scanner_custom_paths(self):
        """커스텀 경로로 스캐너 생성 테스트"""
        custom_paths = ["/tmp/test1", "/tmp/test2"]
        scanner = create_scanner(custom_paths)
        
        self.assertIsInstance(scanner, MDFileScanner)
        # 경로가 존재하지 않아도 정규화되어 저장됨
        self.assertGreaterEqual(len(scanner.base_paths), 0)


if __name__ == "__main__":
    # 로깅 설정
    import logging
    logging.basicConfig(level=logging.WARNING)  # 테스트 중 로그 최소화
    
    # 테스트 실행
    unittest.main(verbosity=2)