#!/usr/bin/env python3
"""
Syncfusion Tool Calling Generator
Syncfusion WinForms 컴포넌트에 대한 Tool calling 데이터셋을 생성합니다.
"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ToolCallingTemplate:
    """Tool calling 템플릿"""
    name: str
    description: str
    parameters: Dict[str, Any]
    component: str
    category: str
    code_example: str
    api_signature: str
    complexity: str = "medium"
    tags: Optional[List[str]] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []

@dataclass
class ComponentInfo:
    """컴포넌트 정보"""
    name: str
    description: str
    category: str
    api_count: int
    page_count: int
    features: List[str]
    
class SyncfusionToolCallingGenerator:
    """Syncfusion Tool calling 데이터셋 생성기"""
    
    def __init__(self, api_signatures_file: str = "api_signatures.json"):
        self.api_signatures_file = api_signatures_file
        self.api_signatures = {}
        self.templates = []
        self.components = {}
        
        # 컴포넌트별 카테고리 정의
        self.component_categories = {
            "grid": "Data Grid",
            "chart": "Data Visualization", 
            "calculate": "Calculation",
            "common": "Common",
            "diagram": "Diagram",
            "DICOM": "Medical Imaging",
            "DocIo": "Document Processing",
            "edit": "Text Editor",
            "Gauge": "Gauges",
            "grouping": "Data Grid",
            "HTMLUI": "UI Framework",
            "Olap-Common": "Business Intelligence",
            "pdf": "PDF Processing",
            "PDF-Viewer": "PDF Viewer",
            "PivotGrid": "Business Intelligence",
            "ProjIO": "Project Management",
            "QTP": "Testing",
            "schedule": "Scheduling",
            "tools": "Development Tools",
            "XlsIO": "Spreadsheet"
        }
        
        # 컴포넌트별 기능 정의
        self.component_features = {
            "grid": ["Data Binding", "Sorting", "Filtering", "Grouping", "Paging", "Editing"],
            "chart": ["Data Visualization", "Multiple Chart Types", "Customization", "Animation"],
            "calculate": ["Formula Engine", "Calculation Functions", "Spreadsheet Functions"],
            "common": ["Common Controls", "Utilities", "Helper Classes"],
            "diagram": ["Diagram Controls", "Shape Libraries", "Layout Algorithms"],
            "DICOM": ["Medical Imaging", "DICOM Viewer", "Image Processing"],
            "DocIo": ["Word Processing", "Document Manipulation", "Mail Merge"],
            "edit": ["Text Editor", "Syntax Highlighting", "Code Completion"],
            "Gauge": ["Gauge Controls", "Real-time Data", "Customization"],
            "grouping": ["Advanced Grid Features", "Grouping", "Summaries"],
            "HTMLUI": ["HTML-based UI", "Web Controls", "Responsive Design"],
            "Olap-Common": ["OLAP Data", "Business Intelligence", "Data Analysis"],
            "pdf": ["PDF Generation", "PDF Manipulation", "Security"],
            "PDF-Viewer": ["PDF Viewer", "Annotation", "Search"],
            "PivotGrid": ["Pivot Tables", "Data Analysis", "OLAP Integration"],
            "ProjIO": ["Project Management", "Project Files", "Scheduling"],
            "QTP": ["Testing Framework", "Automation", "UI Testing"],
            "schedule": ["Scheduling", "Calendar", "Appointment Management"],
            "tools": ["Development Tools", "Utilities", "Code Generation"],
            "XlsIO": ["Excel Processing", "Spreadsheet", "Data Import/Export"]
        }
        
        # 컴포넌트별 페이지 수 정보
        self.component_page_counts = {
            "calculate": 255,
            "chart": 649,
            "common": 145,
            "diagram": 291,
            "DICOM": 12,
            "DocIo": 387,
            "edit": 303,
            "Gauge": 31,
            "grid": 1466,
            "grouping": 71,
            "HTMLUI": 182,
            "Olap-Common": 125,
            "pdf": 384,
            "PDF-Viewer": 29,
            "PivotGrid": 41,
            "ProjIO": 65,
            "QTP": 92,
            "schedule": 73,
            "tools": 2434,
            "XlsIO": 454
        }
        
    def load_api_signatures(self):
        """API 시그니처 로드"""
        try:
            with open(self.api_signatures_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.api_signatures = data.get('components', {})
            logger.info(f"Loaded {len(self.api_signatures)} component API signatures")
        except FileNotFoundError:
            logger.error(f"API signatures file not found: {self.api_signatures_file}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing API signatures file: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error loading API signatures: {e}")
            raise
    
    def create_component_info(self, component_name: str, api_count: int) -> ComponentInfo:
        """컴포넌트 정보 생성"""
        category = self.component_categories.get(component_name, "Uncategorized")
        features = self.component_features.get(component_name, [])
        page_count = self.component_page_counts.get(component_name, 0)
        
        return ComponentInfo(
            name=component_name,
            description=f"Syncfusion {component_name} WinForms Component",
            category=category,
            api_count=api_count,
            page_count=page_count,
            features=features
        )
    
    def generate_basic_templates(self, component_name: str, api_signatures: Dict[str, Any]) -> List[ToolCallingTemplate]:
        """기본 템플릿 생성"""
        templates = []
        component_info = self.create_component_info(component_name, len(api_signatures))
        
        # 컴포넌트 초기화 템플릿
        init_template = ToolCallingTemplate(
            name=f"initialize_{component_name}",
            description=f"Initialize and configure {component_name} control",
            parameters={
                "component_name": {"type": "string", "description": f"Name of the {component_name} component"},
                "width": {"type": "integer", "description": "Width of the component", "optional": True},
                "height": {"type": "integer", "description": "Height of the component", "optional": True},
                "properties": {"type": "object", "description": "Additional properties", "optional": True}
            },
            component=component_name,
            category=component_info.category,
            code_example=f"var {component_name} = new {component_name}();\n{component_name}.Width = width;\n{component_name}.Height = height;",
            api_signature=f"new {component_name}()",
            complexity="low",
            tags=["initialization", "configuration"]
        )
        templates.append(init_template)
        
        # 데이터 바인딩 템플릿 (데이터 관련 컴포넌트용)
        if component_name in ["grid", "chart", "PivotGrid", "grouping"]:
            binding_template = ToolCallingTemplate(
                name=f"bind_data_{component_name}",
                description=f"Bind data to {component_name} control",
                parameters={
                    "component_name": {"type": "string", "description": f"Name of the {component_name} component"},
                    "data_source": {"type": "object", "description": "Data source to bind"},
                    "data_member": {"type": "string", "description": "Data member", "optional": True}
                },
                component=component_name,
                category=component_info.category,
                code_example=f"{component_name}.DataSource = data_source;\n{component_name}.DataMember = data_member;",
                api_signature=f"{component_name}.DataSource",
                complexity="medium",
                tags=["data-binding", "datasource"]
            )
            templates.append(binding_template)
        
        # 속성 설정 템플릿
        property_template = ToolCallingTemplate(
            name=f"set_properties_{component_name}",
            description=f"Set properties for {component_name} control",
            parameters={
                "component_name": {"type": "string", "description": f"Name of the {component_name} component"},
                "properties": {"type": "object", "description": "Properties to set"}
            },
            component=component_name,
            category=component_info.category,
            code_example=f"foreach (var prop in properties)\n{{\n    {component_name}[prop.Key] = prop.Value;\n}}",
            api_signature=f"{component_name}[property]",
            complexity="medium",
            tags=["properties", "configuration"]
        )
        templates.append(property_template)
        
        return templates
    
    def generate_component_specific_templates(self, component_name: str, api_signatures: Dict[str, Any]) -> List[ToolCallingTemplate]:
        """컴포넌트별 특화된 템플릿 생성"""
        templates = []
        
        # Grid 컴포넌트 특화 템플릿
        if component_name == "grid":
            grid_templates = [
                ToolCallingTemplate(
                    name="add_grid_column",
                    description="Add column to grid control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the grid component"},
                        "column_name": {"type": "string", "description": "Name of the column"},
                        "header_text": {"type": "string", "description": "Header text"},
                        "data_field": {"type": "string", "description": "Data field name"}
                    },
                    component=component_name,
                    category="Data Grid",
                    code_example="gridControl1.Columns.Add(new GridColumn(\"ColumnName\", \"Header\", \"DataField\"));",
                    api_signature="gridControl1.Columns.Add",
                    complexity="medium",
                    tags=["grid", "column", "add"]
                ),
                ToolCallingTemplate(
                    name="enable_grid_editing",
                    description="Enable editing in grid control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the grid component"},
                        "allow_edit": {"type": "boolean", "description": "Whether to allow editing"}
                    },
                    component=component_name,
                    category="Data Grid",
                    code_example="gridControl1.AllowEditing = allow_edit;",
                    api_signature="gridControl1.AllowEditing",
                    complexity="low",
                    tags=["grid", "editing", "allow"]
                ),
                ToolCallingTemplate(
                    name="set_grid_sorting",
                    description="Enable sorting in grid control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the grid component"},
                        "allow_sorting": {"type": "boolean", "description": "Whether to allow sorting"}
                    },
                    component=component_name,
                    category="Data Grid",
                    code_example="gridControl1.AllowSorting = allow_sorting;",
                    api_signature="gridControl1.AllowSorting",
                    complexity="low",
                    tags=["grid", "sorting", "enable"]
                ),
                ToolCallingTemplate(
                    name="set_grid_filtering",
                    description="Enable filtering in grid control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the grid component"},
                        "allow_filtering": {"type": "boolean", "description": "Whether to allow filtering"}
                    },
                    component=component_name,
                    category="Data Grid",
                    code_example="gridControl1.AllowFiltering = allow_filtering;",
                    api_signature="gridControl1.AllowFiltering",
                    complexity="low",
                    tags=["grid", "filtering", "enable"]
                )
            ]
            templates.extend(grid_templates)
        
        # Chart 컴포넌트 특화 템플릿
        elif component_name == "chart":
            chart_templates = [
                ToolCallingTemplate(
                    name="add_chart_series",
                    description="Add series to chart control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the chart component"},
                        "series_name": {"type": "string", "description": "Name of the series"},
                        "series_type": {"type": "string", "description": "Type of series (line, bar, pie, etc.)"},
                        "data_source": {"type": "object", "description": "Data source for the series"}
                    },
                    component=component_name,
                    category="Data Visualization",
                    code_example="chartControl1.Series.Add(new Series(\"SeriesName\", SeriesType.Line, data_source));",
                    api_signature="chartControl1.Series.Add",
                    complexity="medium",
                    tags=["chart", "series", "add"]
                ),
                ToolCallingTemplate(
                    name="set_chart_title",
                    description="Set title for chart control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the chart component"},
                        "title": {"type": "string", "description": "Chart title"},
                        "subtitle": {"type": "string", "description": "Chart subtitle", "optional": True}
                    },
                    component=component_name,
                    category="Data Visualization",
                    code_example="chartControl1.Title.Text = title;\nchartControl1.Subtitle.Text = subtitle;",
                    api_signature="chartControl1.Title.Text",
                    complexity="low",
                    tags=["chart", "title", "set"]
                ),
                ToolCallingTemplate(
                    name="set_chart_legend",
                    description="Configure legend for chart control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the chart component"},
                        "visible": {"type": "boolean", "description": "Whether legend is visible"},
                        "position": {"type": "string", "description": "Legend position (top, bottom, left, right)", "optional": True}
                    },
                    component=component_name,
                    category="Data Visualization",
                    code_example="chartControl1.Legend.Visible = visible;\nchartControl1.Legend.Position = position;",
                    api_signature="chartControl1.Legend.Visible",
                    complexity="low",
                    tags=["chart", "legend", "configure"]
                )
            ]
            templates.extend(chart_templates)
        
        # PDF 컴포넌트 특화 템플릿
        elif component_name == "pdf":
            pdf_templates = [
                ToolCallingTemplate(
                    name="create_pdf_document",
                    description="Create new PDF document",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the PDF component"},
                        "file_path": {"type": "string", "description": "Path to save the PDF"}
                    },
                    component=component_name,
                    category="PDF Processing",
                    code_example="PdfDocument document = new PdfDocument();\ndocument.Save(file_path);",
                    api_signature="new PdfDocument()",
                    complexity="medium",
                    tags=["pdf", "create", "document"]
                ),
                ToolCallingTemplate(
                    name="add_pdf_page",
                    description="Add page to PDF document",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the PDF component"},
                        "page_size": {"type": "string", "description": "Page size (A4, Letter, etc.)"},
                        "orientation": {"type": "string", "description": "Page orientation (Portrait, Landscape)"}
                    },
                    component=component_name,
                    category="PDF Processing",
                    code_example="PdfPage page = document.Pages.Add(PdfPageSize.A4, PdfPageOrientation.Portrait);",
                    api_signature="document.Pages.Add",
                    complexity="medium",
                    tags=["pdf", "page", "add"]
                ),
                ToolCallingTemplate(
                    name="add_pdf_text",
                    description="Add text to PDF page",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the PDF component"},
                        "page_index": {"type": "integer", "description": "Index of the page"},
                        "text": {"type": "string", "description": "Text to add"},
                        "font": {"type": "string", "description": "Font name", "optional": True},
                        "font_size": {"type": "integer", "description": "Font size", "optional": True}
                    },
                    component=component_name,
                    category="PDF Processing",
                    code_example="PdfTextElement textElement = new PdfTextElement(text, font, fontSize);\ndocument.Pages[pageIndex].Graphics.DrawString(textElement);",
                    api_signature="document.Pages[pageIndex].Graphics.DrawString",
                    complexity="medium",
                    tags=["pdf", "text", "add"]
                )
            ]
            templates.extend(pdf_templates)
        
        # XlsIO 컴포넌트 특화 템플릿
        elif component_name == "XlsIO":
            xlsio_templates = [
                ToolCallingTemplate(
                    name="create_excel_workbook",
                    description="Create new Excel workbook",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the XlsIO component"},
                        "file_path": {"type": "string", "description": "Path to save the Excel file"}
                    },
                    component=component_name,
                    category="Spreadsheet",
                    code_example="ExcelEngine excelEngine = new ExcelEngine();\nIWorkbook workbook = excelEngine.Excel.Workbooks.Create(1);\nworkbook.SaveAs(file_path);",
                    api_signature="new ExcelEngine()",
                    complexity="medium",
                    tags=["excel", "workbook", "create"]
                ),
                ToolCallingTemplate(
                    name="add_excel_worksheet",
                    description="Add worksheet to Excel workbook",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the XlsIO component"},
                        "sheet_name": {"type": "string", "description": "Name of the worksheet"},
                        "sheet_index": {"type": "integer", "description": "Index of the worksheet", "optional": True}
                    },
                    component=component_name,
                    category="Spreadsheet",
                    code_example="IWorksheet worksheet = workbook.Worksheets.Add(sheet_name);",
                    api_signature="workbook.Worksheets.Add",
                    complexity="low",
                    tags=["excel", "worksheet", "add"]
                ),
                ToolCallingTemplate(
                    name="set_excel_cell_value",
                    description="Set value for Excel cell",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the XlsIO component"},
                        "sheet_name": {"type": "string", "description": "Name of the worksheet"},
                        "row": {"type": "integer", "description": "Row index"},
                        "column": {"type": "integer", "description": "Column index"},
                        "value": {"type": "object", "description": "Cell value"}
                    },
                    component=component_name,
                    category="Spreadsheet",
                    code_example="worksheet.Cells[row, column].Value = value;",
                    api_signature="worksheet.Cells[row, column].Value",
                    complexity="low",
                    tags=["excel", "cell", "value"]
                )
            ]
            templates.extend(xlsio_templates)
        
        # DocIo 컴포넌트 특화 템플릿
        elif component_name == "DocIo":
            docio_templates = [
                ToolCallingTemplate(
                    name="create_word_document",
                    description="Create new Word document",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the DocIo component"},
                        "file_path": {"type": "string", "description": "Path to save the Word document"}
                    },
                    component=component_name,
                    category="Document Processing",
                    code_example="WordDocument document = new WordDocument();\ndocument.Save(file_path, FormatType.Docx);",
                    api_signature="new WordDocument()",
                    complexity="medium",
                    tags=["word", "document", "create"]
                ),
                ToolCallingTemplate(
                    name="add_paragraph",
                    description="Add paragraph to Word document",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the DocIo component"},
                        "text": {"type": "string", "description": "Paragraph text"},
                        "style": {"type": "string", "description": "Paragraph style", "optional": True}
                    },
                    component=component_name,
                    category="Document Processing",
                    code_example="WParagraph paragraph = document.Sections[0].AddParagraph(text);\nparagraph.ApplyStyle(style);",
                    api_signature="document.Sections[0].AddParagraph",
                    complexity="medium",
                    tags=["word", "paragraph", "add"]
                )
            ]
            templates.extend(docio_templates)
        
        # Gauge 컴포넌트 특화 템플릿
        elif component_name == "Gauge":
            gauge_templates = [
                ToolCallingTemplate(
                    name="create_linear_gauge",
                    description="Create linear gauge control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the Gauge component"},
                        "width": {"type": "integer", "description": "Width of the gauge"},
                        "height": {"type": "integer", "description": "Height of the gauge"}
                    },
                    component=component_name,
                    category="Gauges",
                    code_example="LinearGauge linearGauge = new LinearGauge();\nlinearGauge.Width = width;\nlinearGauge.Height = height;",
                    api_signature="new LinearGauge()",
                    complexity="medium",
                    tags=["gauge", "linear", "create"]
                ),
                ToolCallingTemplate(
                    name="create_circular_gauge",
                    description="Create circular gauge control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the Gauge component"},
                        "width": {"type": "integer", "description": "Width of the gauge"},
                        "height": {"type": "integer", "description": "Height of the gauge"}
                    },
                    component=component_name,
                    category="Gauges",
                    code_example="CircularGauge circularGauge = new CircularGauge();\ncircularGauge.Width = width;\ncircularGauge.Height = height;",
                    api_signature="new CircularGauge()",
                    complexity="medium",
                    tags=["gauge", "circular", "create"]
                )
            ]
            templates.extend(gauge_templates)
        
        # Schedule 컴포넌트 특화 템플릿
        elif component_name == "schedule":
            schedule_templates = [
                ToolCallingTemplate(
                    name="create_schedule_control",
                    description="Create schedule control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the Schedule component"},
                        "width": {"type": "integer", "description": "Width of the schedule"},
                        "height": {"type": "integer", "description": "Height of the schedule"}
                    },
                    component=component_name,
                    category="Scheduling",
                    code_example="Schedule schedule = new Schedule();\nschedule.Width = width;\nschedule.Height = height;",
                    api_signature="new Schedule()",
                    complexity="medium",
                    tags=["schedule", "create", "control"]
                ),
                ToolCallingTemplate(
                    name="add_appointment",
                    description="Add appointment to schedule",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the Schedule component"},
                        "subject": {"type": "string", "description": "Appointment subject"},
                        "start_time": {"type": "string", "description": "Start time"},
                        "end_time": {"type": "string", "description": "End time"},
                        "location": {"type": "string", "description": "Appointment location", "optional": True}
                    },
                    component=component_name,
                    category="Scheduling",
                    code_example="Appointment appointment = new Appointment();\nappointment.Subject = subject;\nappointment.StartTime = startTime;\nappointment.EndTime = endTime;\nschedule.Appointments.Add(appointment);",
                    api_signature="schedule.Appointments.Add",
                    complexity="medium",
                    tags=["schedule", "appointment", "add"]
                )
            ]
            templates.extend(schedule_templates)
        
        # Tools 컴포넌트 특화 템플릿
        elif component_name == "tools":
            tools_templates = [
                ToolCallingTemplate(
                    name="create_toolbar",
                    description="Create toolbar control",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the Tools component"},
                        "width": {"type": "integer", "description": "Width of the toolbar"},
                        "height": {"type": "integer", "description": "Height of the toolbar"}
                    },
                    component=component_name,
                    category="Development Tools",
                    code_example="ToolBar toolbar = new ToolBar();\ntoolbar.Width = width;\ntoolbar.Height = height;",
                    api_signature="new ToolBar()",
                    complexity="medium",
                    tags=["toolbar", "create", "tools"]
                ),
                ToolCallingTemplate(
                    name="add_toolbar_button",
                    description="Add button to toolbar",
                    parameters={
                        "component_name": {"type": "string", "description": "Name of the Tools component"},
                        "toolbar_name": {"type": "string", "description": "Name of the toolbar"},
                        "button_text": {"type": "string", "description": "Button text"},
                        "button_image": {"type": "string", "description": "Button image path", "optional": True}
                    },
                    component=component_name,
                    category="Development Tools",
                    code_example="Button button = new Button();\nbutton.Text = buttonText;\nbutton.Image = buttonImage;\ntoolbar.Items.Add(button);",
                    api_signature="toolbar.Items.Add",
                    complexity="medium",
                    tags=["toolbar", "button", "add"]
                )
            ]
            templates.extend(tools_templates)
        
        return templates
    
    def generate_templates_for_component(self, component_name: str, api_signatures: Dict[str, Any]) -> List[ToolCallingTemplate]:
        """컴포넌트별 템플릿 생성"""
        templates = []
        
        # 기본 템플릿 생성
        basic_templates = self.generate_basic_templates(component_name, api_signatures)
        templates.extend(basic_templates)
        
        # 컴포넌트별 특화 템플릿 생성
        specific_templates = self.generate_component_specific_templates(component_name, api_signatures)
        templates.extend(specific_templates)
        
        # API 시그니처 기반 템플릿 생성
        api_signature_list = api_signatures.get('api_signatures', [])
        for api_signature in api_signature_list[:20]:  # 상위 20개 API만 사용
            # API 시그니처 이름을 사용
            signature_name = api_signature.get('name', 'Unknown')
            template = ToolCallingTemplate(
                name=f"call_api_{component_name}_{hash(signature_name) % 10000}",
                description=f"Call API: {signature_name}",
                parameters={
                    "component_name": {"type": "string", "description": f"Name of the {component_name} component"},
                    "parameters": {"type": "object", "description": "Parameters for the API call"}
                },
                component=component_name,
                category=self.component_categories.get(component_name, "Uncategorized"),
                code_example=f"{component_name}.{signature_name} = parameters;",
                api_signature=signature_name,
                complexity="high",
                tags=["api", "call", component_name]
            )
            templates.append(template)
        
        return templates
    
    def generate_all_templates(self):
        """모든 템플릿 생성"""
        logger.info("Generating templates for all components...")
        
        for component_name, api_signatures in self.api_signatures.items():
            logger.info(f"Generating templates for {component_name}...")
            templates = self.generate_templates_for_component(component_name, api_signatures)
            self.templates.extend(templates)
            
            # 컴포넌트 정보 저장
            component_info = self.create_component_info(component_name, len(api_signatures))
            self.components[component_name] = component_info
        
        logger.info(f"Generated {len(self.templates)} templates total")
    
    def save_dataset(self, output_file: str = "syncfusion_winforms_comprehensive_dataset.json"):
        """데이터셋 저장"""
        dataset = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "total_templates": len(self.templates),
                "total_components": len(self.components),
                "generator_version": "1.0.0"
            },
            "components": {
                name: {
                    "name": info.name,
                    "description": info.description,
                    "category": info.category,
                    "api_count": info.api_count,
                    "page_count": info.page_count,
                    "features": info.features
                }
                for name, info in self.components.items()
            },
            "templates": [
                {
                    "name": template.name,
                    "description": template.description,
                    "parameters": template.parameters,
                    "component": template.component,
                    "category": template.category,
                    "code_example": template.code_example,
                    "api_signature": template.api_signature,
                    "complexity": template.complexity,
                    "tags": template.tags
                }
                for template in self.templates
            ]
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Dataset saved to {output_file}")
        return output_file
    
    def generate_dataset(self, output_file: str = "syncfusion_winforms_comprehensive_dataset.json"):
        """데이터셋 생성"""
        try:
            self.load_api_signatures()
            self.generate_all_templates()
            return self.save_dataset(output_file)
        except Exception as e:
            logger.error(f"Error generating dataset: {e}")
            raise

def main():
    """메인 함수"""
    generator = SyncfusionToolCallingGenerator()
    output_file = generator.generate_dataset()
    logger.info(f"Dataset generation completed: {output_file}")

if __name__ == "__main__":
    main()