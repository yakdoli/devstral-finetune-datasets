```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: XlsIO
page_number: 041
page_id: XlsIO#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:18Z
fidelity: lossless
-->

## Overview
- Describes the instantiation process and creation of an Excel document using the ExcelEngine in Syncfusion Winforms.
- Provides a walkthrough for creating a new workbook, specifying the number of sheets, and inserting text into a cell.
- Demonstrates saving the workbook and properly disposing of the Excel engine resources.

## Content

The instantiation process consists of two steps:

### Step 1: Instantiating the Spreadsheet Creation Engine
```csharp
ExcelEngine excelEngine = new ExcelEngine();
```

### Step 2: Instantiating the Excel Application Object
```csharp
IApplication application = excelEngine.Excel;
```

A new workbook is created, which will have 3 worksheets:
```csharp
IWorkbook workbook = application.Workbooks.Create(3);
```

Accessing the first worksheet object in the worksheets collection:
```csharp
IWorksheet sheet = workbook.Worksheets[0];
```

Inserting sample text into the first cell of the first worksheet:
```csharp
sheet.Range["A1"].Text = "Hello World";
```

Saving the workbook to disk:
```csharp
workbook.SaveAs("Sample.xls", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.Open);
```

Closing the workbook:
```csharp
workbook.Close();
```

Disposing the Excel engine:
```csharp
excelEngine.Dispose();
```

### Sample Document
The sample Excel document created through the above procedure is shown below.

<!-- tags: [syncfusion, winforms, xlsio, excelsengine, workbook, worksheet, cell, text, save, dispose] keywords: [instantiation, spreadsheet, application object, workbook, worksheet, range, saveas, close, dispose] -->
```