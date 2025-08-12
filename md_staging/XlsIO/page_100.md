```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: XlsIO
page_number: 100
page_id: XlsIO#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:16Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates the instantiation process for XlsIO in both C# and VB.NET.
- Explains the steps involved in creating and using a spreadsheet template.
- Highlights the performance capabilities of XlsIO for generating large reports.

## Content

### Code Example in C#

```csharp
[C#]

// New instance of XlsIO is created. [Equivalent to launching MS Excel with no workbooks open].
// The instantiation process consists of two steps.

// Step 1: Instantiate the spreadsheet creation engine.
ExcelEngine excelEngine = new ExcelEngine();

// Step 2: Instantiate the Excel application object.
IApplication application = excelEngine.Excel;

// Open an existing spreadsheet which will be used as a template for generating the new spreadsheet.
// After opening the spreadsheet, the workbook object represents the complete in-memory object model of the template spreadsheet.
IWorkbook workbook = application.Workbooks.OpenReadOnly("SpreadsheetFromTemplate.xls");
```

### Code Example in VB.NET

```vb
[VB.NET]

' New instance of XlsIO is created. [Equivalent to launching MS Excel with no workbooks open].
' The instantiation process consists of two steps.

' Step 1: Instantiate the spreadsheet creation engine.
Dim excelEngine As ExcelEngine = New ExcelEngine()

' Step 2: Instantiate the Excel application object.
Dim application As IApplication = excelEngine.Excel

' Open an existing spreadsheet which will be used as a template for generating the new spreadsheet.
' After opening the spreadsheet, the workbook object represents the complete in-memory object model of the template spreadsheet.
Dim workbook As IWorkbook = application.Workbooks.OpenReadOnly("SpreadsheetFromTemplate.xls")
```

### 3.9 Improving Performance

Essential XlsIO can create large reports in few seconds.

## Cross References
- Referenced sections: instantiation process, template usage, performance benchmarks.

## RAG Annotations
<!-- tags: [XlsIO, C#, VB.NET, instantiation, template, performance, Essential XlsIO] keywords: [XlsIO, C#, VB.NET, instantiation, template, performance, large reports, essential] -->
```
