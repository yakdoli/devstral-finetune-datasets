#!/usr/bin/env python3
"""
MD 프로세서 통합 테스트
전체 MD 처리 파이프라인의 통합 기능을 테스트합니다.
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import json
import logging

from md_processor.processor import MDProcessor, ProcessingConfig, create_processor
from md_processor.scanner import create_scanner
from md_processor.parser import create_parser


class TestMDProcessorIntegration(unittest.TestCase):
    """MD 프로세서 통합 테스트"""
    
    def setUp(self):
        """테스트 설정"""
        self.temp_dir = Path(tempfile.mkdtemp())
        
        # 테스트 디렉토리 구조 생성
        self.output_dir = self.temp_dir / "output"
        self.staging_dir = self.temp_dir / "md_staging"
        
        self.output_dir.mkdir()
        self.staging_dir.mkdir()
        
        # 테스트 데이터 생성
        self._create_test_data()
        
        # 프로세서 설정
        self.config = ProcessingConfig(
            batch_size=10,
            min_quality_score=0.1,
            max_content_length=10000,
            remove_duplicates=True,
            output_format="json",
            include_metadata=True,
            progress_interval=5
        )
        
        # 스캐너 경로 설정
        scanner = create_scanner([str(self.output_dir), str(self.staging_dir)])
        parser = create_parser()
        
        self.processor = MDProcessor(self.config)
        self.processor.scanner = scanner
        self.processor.parser = parser
    
    def tearDown(self):
        """테스트 정리"""
        shutil.rmtree(self.temp_dir)
    
    def _create_test_data(self):
        """테스트 데이터 생성"""
        # 컴포넌트 파일 생성
        components = [
            {
                "name": "grid",
                "content": """# Grid Component

The Grid component provides powerful data display and manipulation capabilities.

## API Reference

```csharp
public class GridControl : Control
{
    public object DataSource { get; set; }
    public bool AllowSorting { get; set; }
    
    public void RefreshData()
    {
        // Refresh the grid data
    }
    
    public void ExportToExcel(string fileName)
    {
        // Export grid data to Excel
    }
}
```

## Features

- Data binding
- Sorting and filtering
- Export functionality
- Custom cell rendering

| Feature | Description | Supported |
|---------|-------------|-----------|
| Sorting | Column sorting | Yes |
| Filtering | Row filtering | Yes |
| Export | Excel export | Yes |
"""
            },
            {
                "name": "chart",
                "content": """# Chart Component

Create beautiful and interactive charts with the Chart component.

## Usage

```javascript
const chart = new ChartComponent({
    type: 'line',
    data: chartData,
    options: {
        responsive: true,
        animation: true
    }
});

chart.render('#chart-container');
chart.updateData(newData);
```

## Chart Types

- Line charts
- Bar charts  
- Pie charts
- Area charts

Use `chart.setType(type)` to change chart type dynamically.
"""
            }
        ]
        
        for comp in components:
            comp_file = self.output_dir / f"{comp['name']}.md"
            comp_file.write_text(comp['content'])
        
        # 페이지 파일 생성
        page_data = [
            {
                "component": "grid",
                "page": 1,
                "title": "Grid Getting Started",
                "content": """# Grid Getting Started

Learn how to use the Grid component in your applications.

## Installation

```bash
npm install @syncfusion/grid
```

## Basic Usage

```csharp
GridControl grid = new GridControl();
grid.DataSource = GetData();
grid.AllowSorting = true;
```

The grid supports various data sources and provides rich functionality.
"""
            },
            {
                "component": "grid", 
                "page": 2,
                "title": "Grid Advanced Features",
                "content": """# Grid Advanced Features

Explore advanced features of the Grid component.

## Custom Cell Templates

```csharp
grid.Columns.Add(new GridColumn
{
    FieldName = "Status",
    CellTemplate = new CustomStatusTemplate()
});
```

## Event Handling

```csharp
grid.SelectionChanged += (sender, e) => {
    // Handle selection change
};
```

Advanced features include custom templates and event handling.
"""
            },
            {
                "component": "chart",
                "page": 1, 
                "title": "Chart Basics",
                "content": """# Chart Basics

Introduction to Chart component fundamentals.

## Creating Charts

```javascript
function createChart(data) {
    return new Chart({
        type: 'bar',
        data: data,
        options: {
            responsive: true
        }
    });
}
```

Charts can be customized with various options and styles.
"""
            }
        ]
        
        for page in page_data:
            # 컴포넌트 디렉토리 생성
            comp_dir = self.staging_dir / page["component"]
            comp_dir.mkdir(exist_ok=True)
            
            # MD 파일 생성
            md_file = comp_dir / f"page_{page['page']:03d}.md"
            md_file.write_text(page['content'])
            
            # JSON 메타데이터 파일 생성
            json_file = comp_dir / f"page_{page['page']:03d}.json"
            json_data = {
                "document_name": page["component"],
                "page_number": page["page"],
                "title": page["title"],
                "category": "documentation",
                "version": "1.0"
            }
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2)
        
        # 빈 파일 생성 (오류 테스트용)
        empty_file = self.staging_dir / "grid" / "empty.md"
        empty_file.write_text("")
        
        # 잘못된 인코딩 파일 생성 (오류 테스트용)
        invalid_file = self.staging_dir / "chart" / "invalid.md"
        with open(invalid_file, 'wb') as f:
            f.write(b'\xff\xfe# Invalid encoding\n')
        
        # 권한 없는 파일 생성 (Unix 시스템에서만 작동)
        try:
            restricted_file = self.staging_dir / "grid" / "restricted.md"
            restricted_file.write_text("# Restricted file")
            restricted_file.chmod(0o000)  # 읽기 권한 제거
        except:
            pass  # Windows에서는 권한 설정이 다를 수 있음
    
    def test_full_pipeline_processing(self):
        """전체 파이프라인 처리 테스트"""
        output_path = self.temp_dir / "processed_documents.json"
        
        # 처리 실행
        documents = self.processor.process_documents(output_path)
        
        # 기본 검증
        self.assertGreater(len(documents), 0)
        self.assertTrue(output_path.exists())
        
        # 통계 검증
        self.assertGreater(self.processor.stats.total_files, 0)
        self.assertGreater(self.processor.stats.successful_files, 0)
        self.assertGreaterEqual(self.processor.stats.success_rate, 0.0)
        
        # 문서 구조 검증
        for doc in documents:
            self.assertIn('id', doc)
            self.assertIn('title', doc)
            self.assertIn('component', doc)
            self.assertIn('content', doc)
            self.assertIn('api_signatures', doc)
            self.assertIn('content_structure', doc)
            self.assertIn('quality_score', doc)
            self.assertIn('processing_timestamp', doc)
    
    def test_metadata_files_generation(self):
        """메타데이터 파일 생성 테스트"""
        output_path = self.temp_dir / "processed_documents.json"
        
        # 처리 실행
        documents = self.processor.process_documents(output_path)
        
        # 메타데이터 파일들이 생성되었는지 확인
        metadata_path = output_path.with_suffix('.metadata.json')
        stats_path = output_path.with_suffix('.stats.json')
        summary_path = output_path.with_suffix('.summary.json')
        
        self.assertTrue(metadata_path.exists())
        self.assertTrue(stats_path.exists())
        self.assertTrue(summary_path.exists())
        
        # 메타데이터 파일 내용 검증
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        self.assertIn('document_count', metadata)
        self.assertIn('components', metadata)
        self.assertIn('api_signatures', metadata)
        self.assertIn('content_statistics', metadata)
        self.assertIn('quality_distribution', metadata)
        
        # 통계 파일 내용 검증
        with open(stats_path, 'r', encoding='utf-8') as f:
            stats = json.load(f)
        
        self.assertIn('processing_stats', stats)
        self.assertIn('config', stats)
        self.assertIn('errors', stats)
        
        # 요약 파일 내용 검증
        with open(summary_path, 'r', encoding='utf-8') as f:
            summary = json.load(f)
        
        self.assertIn('processing_summary', summary)
        self.assertIn('quality_analysis', summary)
        self.assertIn('content_analysis', summary)
    
    def test_api_signature_extraction_integration(self):
        """API 시그니처 추출 통합 테스트"""
        output_path = self.temp_dir / "processed_documents.json"
        
        # 처리 실행
        documents = self.processor.process_documents(output_path)
        
        # API 시그니처가 추출되었는지 확인
        total_api_signatures = sum(len(doc.get('api_signatures', [])) for doc in documents)
        self.assertGreater(total_api_signatures, 0)
        
        # C# API가 추출되었는지 확인
        csharp_apis = []
        for doc in documents:
            for sig in doc.get('api_signatures', []):
                if sig.get('language') == 'csharp':
                    csharp_apis.append(sig)
        
        self.assertGreater(len(csharp_apis), 0)
        
        # JavaScript API가 추출되었는지 확인
        js_apis = []
        for doc in documents:
            for sig in doc.get('api_signatures', []):
                if sig.get('language') == 'javascript':
                    js_apis.append(sig)
        
        self.assertGreater(len(js_apis), 0)
    
    def test_quality_filtering(self):
        """품질 필터링 테스트"""
        # 낮은 품질 점수로 설정
        config = ProcessingConfig(
            min_quality_score=0.8,  # 높은 임계값
            max_content_length=10000,
            remove_duplicates=True
        )
        
        processor = MDProcessor(config)
        processor.scanner = self.processor.scanner
        processor.parser = self.processor.parser
        
        output_path = self.temp_dir / "filtered_documents.json"
        
        # 처리 실행
        documents = processor.process_documents(output_path)
        
        # 모든 문서가 높은 품질 점수를 가져야 함
        for doc in documents:
            self.assertGreaterEqual(doc.get('quality_score', 0.0), 0.8)
    
    def test_error_handling(self):
        """오류 처리 테스트"""
        output_path = self.temp_dir / "processed_with_errors.json"
        
        # 처리 실행 (오류가 있는 파일들 포함)
        documents = self.processor.process_documents(output_path)
        
        # 일부 파일은 성공적으로 처리되었는지 확인
        self.assertGreater(self.processor.stats.successful_files, 0)
        
        # 전체 파일 수가 처리된 파일 수보다 많은지 확인 (일부 파일이 스킵됨)
        self.assertGreaterEqual(self.processor.stats.total_files, self.processor.stats.processed_files)
        
        # 성공률이 100%가 아닌지 확인 (일부 파일에 문제가 있음)
        self.assertLess(self.processor.stats.success_rate, 100.0)
    
    def test_batch_processing(self):
        """배치 처리 테스트"""
        output_path = self.temp_dir / "batch_processed.json"
        
        # 배치 처리 실행
        all_batches = []
        for batch in self.processor.process_documents_batch(output_path):
            all_batches.append(batch)
            self.assertLessEqual(len(batch), self.config.batch_size)
        
        # 배치가 생성되었는지 확인
        self.assertGreater(len(all_batches), 0)
        
        # 전체 문서 수 확인
        total_docs = sum(len(batch) for batch in all_batches)
        self.assertGreater(total_docs, 0)
    
    def test_component_organization(self):
        """컴포넌트별 조직화 테스트"""
        output_path = self.temp_dir / "organized_documents.json"
        
        # 처리 실행
        documents = self.processor.process_documents(output_path)
        
        # 컴포넌트별 그룹화
        components = {}
        for doc in documents:
            component = doc.get('component')
            if component:
                if component not in components:
                    components[component] = []
                components[component].append(doc)
        
        # 예상 컴포넌트가 있는지 확인
        self.assertIn('grid', components)
        self.assertIn('chart', components)
        
        # 각 컴포넌트에 문서가 있는지 확인
        self.assertGreater(len(components['grid']), 0)
        self.assertGreater(len(components['chart']), 0)
    
    def test_content_structure_analysis(self):
        """콘텐츠 구조 분석 테스트"""
        output_path = self.temp_dir / "structured_documents.json"
        
        # 처리 실행
        documents = self.processor.process_documents(output_path)
        
        # 모든 문서에 구조 분석이 있는지 확인
        for doc in documents:
            structure = doc.get('content_structure', {})
            
            self.assertIn('word_count', structure)
            self.assertIn('character_count', structure)
            self.assertIn('header_count', structure)
            self.assertIn('code_block_count', structure)
            self.assertIn('complexity_score', structure)
            
            # 구조 정보가 합리적인지 확인
            self.assertGreaterEqual(structure.get('word_count', 0), 0)
            self.assertGreaterEqual(structure.get('character_count', 0), 0)
            self.assertGreaterEqual(structure.get('complexity_score', 0.0), 0.0)
            self.assertLessEqual(structure.get('complexity_score', 0.0), 1.0)
    
    def test_processing_statistics(self):
        """처리 통계 테스트"""
        output_path = self.temp_dir / "stats_test.json"
        
        # 처리 실행
        documents = self.processor.process_documents(output_path)
        
        stats = self.processor.stats
        
        # 기본 통계 검증
        self.assertGreater(stats.total_files, 0)
        self.assertEqual(stats.processed_files, stats.successful_files + stats.failed_files)
        self.assertGreaterEqual(stats.success_rate, 0.0)
        self.assertLessEqual(stats.success_rate, 100.0)
        self.assertGreater(stats.processing_time, 0.0)
        
        # 콘텐츠 통계 검증
        if stats.successful_files > 0:
            self.assertGreater(stats.total_content_length, 0)


class TestProcessorFactory(unittest.TestCase):
    """프로세서 팩토리 함수 테스트"""
    
    def test_create_processor_default(self):
        """기본 프로세서 생성 테스트"""
        processor = create_processor()
        
        self.assertIsInstance(processor, MDProcessor)
        self.assertIsNotNone(processor.config)
        self.assertIsNotNone(processor.scanner)
        self.assertIsNotNone(processor.parser)
    
    def test_create_processor_custom_config(self):
        """커스텀 설정으로 프로세서 생성 테스트"""
        config = ProcessingConfig(
            batch_size=50,
            min_quality_score=0.5,
            max_content_length=5000
        )
        
        processor = create_processor(config)
        
        self.assertEqual(processor.config.batch_size, 50)
        self.assertEqual(processor.config.min_quality_score, 0.5)
        self.assertEqual(processor.config.max_content_length, 5000)


if __name__ == "__main__":
    # 로깅 설정
    logging.basicConfig(level=logging.INFO)
    
    # 테스트 실행
    unittest.main(verbosity=2)