#!/usr/bin/env python3
"""
간소화된 Syncfusion Tool Calling Dataset Generator
HTTP 요청 없이 로컬로 테스트 가능한 버전
"""

import json
import os
import asyncio
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import logging
import re
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ToolCallingSample:
    """Tool calling 형태의 데이터셋 샘플"""
    instruction: str
    input: str
    output: str
    tools: List[Dict[str, Any]]
    tool_calls: List[Dict[str, Any]]

class SimpleSyncfusionToolCallingGenerator:
    """간소화된 Syncfusion Tool calling 데이터셋 생성기"""
    
    def __init__(self):
        # Syncfusion 관련 도구 정의
        self.syncfusion_tools = [
            {
                "type": "function",
                "function": {
                    "name": "create_grid_control",
                    "description": "Syncfusion GridControl을 생성하고 기본 설정을 적용합니다",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "datasource": {
                                "type": "string",
                                "description": "데이터 소스 경로 또는 데이터"
                            },
                            "columns": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "field": {"type": "string"},
                                        "header": {"type": "string"},
                                        "format": {"type": "string"}
                                    }
                                }
                            },
                            "skin": {
                                "type": "string",
                                "description": "그리드 스킨 (예: 'Office2007Blue', 'Sandune')"
                            }
                        }
                    }
                }
            },
            {
                "type": "function", 
                "function": {
                    "name": "create_chart_control",
                    "description": "Syncfusion ChartControl을 생성하고 데이터를 바인딩합니다",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "chart_type": {
                                "type": "string",
                                "description": "차트 종류 (예: 'SplineArea', 'Column', 'Line')"
                            },
                            "datasource": {
                                "type": "string", 
                                "description": "데이터 소스"
                            },
                            "x_field": {
                                "type": "string",
                                "description": "X축 필드명"
                            },
                            "y_field": {
                                "type": "string",
                                "description": "Y축 필드명"
                            }
                        }
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "create_excel_export",
                    "description": "Syncfusion XlsIO를 사용하여 데이터를 Excel로 내보냅니다",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "string",
                                "description": "내보낼 데이터"
                            },
                            "filename": {
                                "type": "string",
                                "description": "저장할 파일명"
                            },
                            "worksheet_name": {
                                "type": "string",
                                "description": "워크시트 이름"
                            }
                        }
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "create_olap_grid",
                    "description": "Syncfusion OlapGrid을 생성하고 OLAP 데이터를 표시합니다",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "connection_string": {
                                "type": "string",
                                "description": "OLAP 데이터베이스 연결 문자열"
                            },
                            "cube_name": {
                                "type": "string", 
                                "description": "큐브 이름"
                            },
                            "measures": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "측정값 목록"
                            }
                        }
                    }
                }
            }
        ]
    
    def _extract_code_snippets(self, content: str) -> List[Dict[str, Any]]:
        """코드 스니펫 추출"""
        snippets = []
        
        # C# 코드 블록 추출
        csharp_pattern = r'```csharp\n(.*?)\n```'
        csharp_matches = re.findall(csharp_pattern, content, re.DOTALL)
        
        for i, code in enumerate(csharp_matches):
            snippets.append({
                "language": "csharp",
                "code": code.strip(),
                "index": i
            })
        
        # VB.NET 코드 블록 추출
        vbnet_pattern = r'```vbnet\n(.*?)\n```'
        vbnet_matches = re.findall(vbnet_pattern, content, re.DOTALL)
        
        for i, code in enumerate(vbnet_matches):
            snippets.append({
                "language": "vbnet", 
                "code": code.strip(),
                "index": len(csharp_matches) + i
            })
        
        return snippets
    
    def _generate_tool_calls(self, snippets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """코드 스니펫을 기반으로 tool calls 생성"""
        tool_calls = []
        
        for snippet in snippets:
            code = snippet["code"]
            
            # 코드 내용에 따라 적절한 tool call 생성
            if "GridControl" in code or "gridControl" in code:
                tool_calls.append({
                    "function": {
                        "name": "create_grid_control",
                        "arguments": {
                            "datasource": "sample_data",
                            "columns": [
                                {"field": "OrderID", "header": "Order ID"},
                                {"field": "CustomerID", "header": "Customer ID"}
                            ],
                            "skin": "Office2007Blue"
                        }
                    }
                })
            elif "ChartControl" in code or "chartControl" in code:
                tool_calls.append({
                    "function": {
                        "name": "create_chart_control", 
                        "arguments": {
                            "chart_type": "Column",
                            "datasource": "chart_data",
                            "x_field": "Category",
                            "y_field": "Value"
                        }
                    }
                })
            elif "ExcelEngine" in code or "XlsIO" in code:
                tool_calls.append({
                    "function": {
                        "name": "create_excel_export",
                        "arguments": {
                            "data": "export_data",
                            "filename": "output.xlsx",
                            "worksheet_name": "Sheet1"
                        }
                    }
                })
            elif "OlapGrid" in code or "OlapDataManager" in code:
                tool_calls.append({
                    "function": {
                        "name": "create_olap_grid",
                        "arguments": {
                            "connection_string": "DataSource=localhost;Initial Catalog=Adventure Works DW",
                            "cube_name": "Adventure Works",
                            "measures": ["Sales Amount", "Quantity"]
                        }
                    }
                })
            else:
                # 기본 tool call
                tool_calls.append({
                    "function": {
                        "name": "create_grid_control",
                        "arguments": {
                            "datasource": "sample_data",
                            "columns": [],
                            "skin": "Default"
                        }
                    }
                })
        
        return tool_calls
    
    def _generate_mock_samples(self, content: str, page_info: Dict[str, Any]) -> List[ToolCallingSample]:
        """Mock 샘플 생성 (실제 LLM 호출 대체)"""
        samples = []
        
        # 페이지 정보에 따라 다양한 샘플 생성
        component = page_info.get('document_name', 'Unknown').lower()
        
        if 'grid' in component:
            samples.extend([
                ToolCallingSample(
                    instruction="How to create a Syncfusion GridControl with data binding?",
                    input="",
                    output="To create a Syncfusion GridControl with data binding, you need to:\n\n1. Create a new GridControl instance\n2. Set the DataSource property to your data\n3. Configure columns as needed\n4. Call DataBind() to load the data\n\n```csharp\nGridControl gridControl = new GridControl();\ngridControl.DataSource = GetData();\ngridControl.DataBind();\n```",
                    tools=self.syncfusion_tools,
                    tool_calls=[{
                        "function": {
                            "name": "create_grid_control",
                            "arguments": {
                                "datasource": "sample_data",
                                "columns": [
                                    {"field": "OrderID", "header": "Order ID"},
                                    {"field": "CustomerID", "header": "Customer ID"}
                                ],
                                "skin": "Office2007Blue"
                            }
                        }
                    }]
                ),
                ToolCallingSample(
                    instruction="How to customize GridControl columns?",
                    input="",
                    output="To customize GridControl columns, you can use the GridColumnDescriptor to set various properties:\n\n```csharp\nGridColumnDescriptor column = gridControl.TableDescriptor.Columns.Add(\"OrderID\");\ncolumn.HeaderText = \"Order ID\";\ncolumn.Width = 100;\ncolumn.AllowResize = true;\n```",
                    tools=self.syncfusion_tools,
                    tool_calls=[{
                        "function": {
                            "name": "create_grid_control",
                            "arguments": {
                                "datasource": "custom_data",
                                "columns": [
                                    {"field": "OrderID", "header": "Order ID", "format": "0"},
                                    {"field": "OrderDate", "header": "Order Date", "format": "MM/dd/yyyy"}
                                ],
                                "skin": "Sandune"
                            }
                        }
                    }]
                )
            ])
        elif 'chart' in component:
            samples.extend([
                ToolCallingSample(
                    instruction="How to create a Syncfusion ChartControl?",
                    input="",
                    output="To create a Syncfusion ChartControl, follow these steps:\n\n1. Create a new ChartControl instance\n2. Set the DataSource property\n3. Add series with appropriate data mapping\n4. Configure chart properties\n\n```csharp\nChartControl chartControl = new ChartControl();\nchartControl.DataSource = chartData;\nchartControl.Series.Add(\"Series1\", \"Sales\", \"Category\", \"Value\");\n```",
                    tools=self.syncfusion_tools,
                    tool_calls=[{
                        "function": {
                            "name": "create_chart_control",
                            "arguments": {
                                "chart_type": "Column",
                                "datasource": "chart_data",
                                "x_field": "Category",
                                "y_field": "Value"
                            }
                        }
                    }]
                )
            ])
        elif 'xlsio' in component:
            samples.extend([
                ToolCallingSample(
                    instruction="How to export data to Excel using Syncfusion XlsIO?",
                    input="",
                    output="To export data to Excel using Syncfusion XlsIO:\n\n1. Create an ExcelEngine instance\n2. Create a workbook and worksheet\n3. Write data to cells\n4. Save the workbook\n\n```csharp\nExcelEngine excelEngine = new ExcelEngine();\nIWorkbook workbook = excelEngine.Excel.Workbooks.Create(1);\nIWorksheet worksheet = workbook.Worksheets[0];\nworksheet[\"A1\"].Text = \"Product\";\nworksheet[\"B1\"].Text = \"Price\";\nworkbook.SaveAs(\"output.xlsx\");\n```",
                    tools=self.syncfusion_tools,
                    tool_calls=[{
                        "function": {
                            "name": "create_excel_export",
                            "arguments": {
                                "data": "export_data",
                                "filename": "output.xlsx",
                                "worksheet_name": "Sheet1"
                            }
                        }
                    }]
                )
            ])
        else:
            # 일반 샘플
            samples.append(ToolCallingSample(
                instruction=f"How to use {page_info.get('document_name', 'Syncfusion component')}?",
                input="",
                output=f"This is a sample implementation for {page_info.get('document_name', 'Syncfusion component')}.\n\n```csharp\n// Sample implementation code\nvar component = new SyncfusionComponent();\ncomponent.Initialize();\n```",
                tools=self.syncfusion_tools,
                tool_calls=[{
                    "function": {
                        "name": "create_grid_control",
                        "arguments": {
                            "datasource": "sample_data",
                            "columns": [],
                            "skin": "Default"
                        }
                    }
                }]
            ))
        
        return samples
    
    def process_page(self, md_path: Path, json_path: Path) -> List[ToolCallingSample]:
        """단일 페이지 처리"""
        try:
            # Markdown 내용 읽기
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # JSON 메타데이터 읽기
            with open(json_path, 'r', encoding='utf-8') as f:
                page_info = json.load(f)
            
            # Mock 샘플 생성
            samples = self._generate_mock_samples(md_content, page_info)
            
            logger.info(f"Generated {len(samples)} tool calling samples from {md_path.name}")
            return samples
            
        except Exception as e:
            logger.error(f"Error processing {md_path}: {e}")
            return []
    
    def process_section(self, section_path: Path) -> List[ToolCallingSample]:
        """섹션의 모든 페이지 처리"""
        all_samples = []
        
        # MD/JSON 쌍 찾기
        md_files = list(section_path.glob("page_*.md"))
        md_files.sort()
        
        logger.info(f"Processing {len(md_files)} pages in section {section_path.name}")
        
        # 페이지 처리
        for md_file in md_files:
            json_file = md_file.with_suffix('.json')
            if json_file.exists():
                page_samples = self.process_page(md_file, json_file)
                all_samples.extend(page_samples)
        
        return all_samples
    
    def integrate_context7_data(self, context7_path: Path) -> List[ToolCallingSample]:
        """Context7 데이터 통합"""
        context7_samples = []
        
        try:
            if context7_path.exists():
                with open(context7_path, 'r', encoding='utf-8') as f:
                    context7_data = json.load(f)
                
                # Context7 코드 스니펫 처리
                if 'code_snippets' in context7_data:
                    for snippet in context7_data['code_snippets']:
                        # Tool calls 생성
                        tool_calls = self._generate_tool_calls([{
                            "language": snippet.get('language', 'csharp'),
                            "code": snippet.get('code', ''),
                            "index": 0
                        }])
                        
                        sample = ToolCallingSample(
                            instruction=f"How to use {snippet.get('title', 'Syncfusion component')}?",
                            input="",
                            output=snippet.get('description', '') + "\n\n" + snippet.get('code', ''),
                            tools=self.syncfusion_tools,
                            tool_calls=tool_calls
                        )
                        context7_samples.append(sample)
                
                logger.info(f"Integrated {len(context7_samples)} samples from Context7 data")
        
        except Exception as e:
            logger.error(f"Error integrating Context7 data: {e}")
        
        return context7_samples
    
    def generate_dataset(self, 
                         md_staging_path: Path,
                         context7_path: Path,
                         output_path: Path,
                         sections: Optional[List[str]] = None):
        """완전한 Tool calling 데이터셋 생성"""
        
        all_samples = []
        available_sections = [d.name for d in md_staging_path.iterdir() if d.is_dir()]
        
        if sections is None:
            sections = available_sections
        else:
            sections = [s for s in sections if s in available_sections]
        
        logger.info(f"Processing sections: {sections}")
        
        # md_staging 데이터 처리
        for section in sections:
            section_path = md_staging_path / section
            logger.info(f"Processing section: {section}")
            
            section_samples = self.process_section(section_path)
            all_samples.extend(section_samples)
            
            logger.info(f"Section {section}: {len(section_samples)} samples")
        
        # Context7 데이터 통합
        logger.info("Integrating Context7 data...")
        context7_samples = self.integrate_context7_data(context7_path)
        all_samples.extend(context7_samples)
        
        # 데이터셋 변환
        dataset_data = []
        for sample in all_samples:
            dataset_item = {
                "instruction": sample.instruction,
                "input": sample.input,
                "output": sample.output,
                "tools": sample.tools,
                "tool_calls": sample.tool_calls
            }
            dataset_data.append(dataset_item)
        
        # 데이터셋 저장
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(dataset_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Tool calling dataset saved: {output_path}")
        logger.info(f"Total samples: {len(all_samples)}")
        
        return dataset_data

def main():
    generator = SimpleSyncfusionToolCallingGenerator()
    
    # 경로 설정
    md_staging_path = Path("md_staging")
    context7_path = Path("context7_syncfusion_specific.json")
    output_path = Path("syncfusion_tool_calling_dataset.json")
    
    if not md_staging_path.exists():
        logger.error(f"md_staging path does not exist: {md_staging_path}")
        return
    
    # 데이터셋 생성
    dataset_data = generator.generate_dataset(
        md_staging_path=md_staging_path,
        context7_path=context7_path,
        output_path=output_path,
        sections=["grid", "chart", "xlsio"]
    )
    
    # 샘플 출력
    print(f"\n=== 생성된 데이터셋 샘플 ===")
    for i, sample in enumerate(dataset_data[:3]):  # 첫 3개 샘플 출력
        print(f"\n[샘플 {i+1}]")
        print(f"Instruction: {sample['instruction']}")
        print(f"Tools: {[t['function']['name'] for t in sample['tools']]}")
        print(f"Tool Calls: {[tc['function']['name'] for tc in sample['tool_calls']]}")
        print(f"Output: {sample['output'][:100]}...")

if __name__ == "__main__":
    main()