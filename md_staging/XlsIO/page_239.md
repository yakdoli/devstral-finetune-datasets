```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: XlsIO
page_number: 239
page_id: XlsIO#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:09Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Create a spreadsheet using the `ExcelEngine` and `IApplication` objects.
- Set the default version of Excel to Excel 2010.
- Create a workbook, access the first worksheet, and insert product and month data into specific cells.

## Content

### Setup and Data Insertion

```csharp
'Step 1: Instantiate the spreadsheet creation engine.
Dim excelEngine As New ExcelEngine()

'Step 2: Instantiate the Excel application object.
Dim application As IApplication = excelEngine.Excel
application.DefaultVersion = ExcelVersion.Excel2010

'The first worksheet object in created.
Dim workbook As IWorkbook = application.Workbooks.Create(1)
Dim sheet As IWorksheet = workbook.Worksheets(0)

'Insert the data in sheet-1.
sheet.Range("B1").Text = "Product-A"
sheet.Range("C1").Text = "Product-B"
sheet.Range("D1").Text = "Product-C"
sheet.Range("E1").Text = "Product-D"
sheet.Range("A2").Text = "Jan"
sheet.Range("A3").Text = "Feb"
sheet.Range("A4").Text = "Mar"
sheet.Range("A5").Text = "Apr"
sheet.Range("A6").Text = "May"

sheet.Range("B2").Number = 25
sheet.Range("B3").Number = 20
sheet.Range("B4").Number = 35
sheet.Range("B5").Number = 67
sheet.Range("B6").Number = 23
sheet.Range("C2").Number = 35
sheet.Range("C3").Number = 25
sheet.Range("C4").Number = 14
sheet.Range("C5").Number = 78
sheet.Range("C6").Number = 45
sheet.Range("D2").Number = 40
sheet.Range("D3").Number = 55
sheet.Range("D4").Number = 51
```

## API Reference

### Classes
- **ExcelEngine**: Used to instantiate the spreadsheet creation engine.
- **IApplication**: Represents the interface for the Excel application.
- **IWorkbook**: Represents an Excel workbook object.
- **IWorksheet**: Represents an Excel worksheet object.
- **Range**: Accesses and modifies the content of specific cells.

### Properties and Methods
- **DefaultVersion**: Sets the default version of Excel for the application.
- **Workbooks.Create(1)**: Creates a new workbook.
- **Worksheets(0)**: Accesses the first worksheet in the workbook.
- **Text**: Sets the text content of a cell.
- **Number**: Sets the numeric value of a cell.

## Code Examples

The example demonstrates basic operations such as creating an Excel application instance, setting its default version, creating a workbook, accessing a worksheet, and inserting data into specific cells.

```csharp
' Create the Excel engine and application
Dim excelEngine As New ExcelEngine()
Dim application As IApplication = excelEngine.Excel
application.DefaultVersion = ExcelVersion.Excel2010

' Create a workbook and access the first worksheet
Dim workbook As IWorkbook = application.Workbooks.Create(1)
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Insert product and month data
sheet.Range("B1").Text = "Product-A"
sheet.Range("C1").Text = "Product-B"
sheet.Range("D1").Text = "Product-C"
sheet.Range("E1").Text = "Product-D"

sheet.Range("A2").Text = "Jan"
sheet.Range("A3").Text = "Feb"
sheet.Range("A4").Text = "Mar"
sheet.Range("A5").Text = "Apr"
sheet.Range("A6").Text = "May"

' Insert numerical data
sheet.Range("B2").Number = 25
sheet.Range("B3").Number = 20
sheet.Range("B4").Number = 35
sheet.Range("B5").Number = 67
sheet.Range("B6").Number = 23
sheet.Range("C2").Number = 35
sheet.Range("C3").Number = 25
sheet.Range("C4").Number = 14
sheet.Range("C5").Number = 78
sheet.Range("C6").Number = 45
sheet.Range("D2").Number = 40
sheet.Range("D3").Number = 55
sheet.Range("D4").Number = 51
```

## Cross References
- See also: More advanced usage of ExcelEngine, creating charts, and formatting cells.

<!-- tags: [Syncfusion, XlsIO, Excel, Spreadsheet, WinForms, SDK, V11.4.0.26] keywords: [ExcelEngine, IApplication, IWorkbook, IWorksheet, Range, DefaultVersion, Text, Number, Create, Worksheet, Cell, Data] -->
```