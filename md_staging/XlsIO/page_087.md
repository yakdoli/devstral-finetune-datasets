```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: XlsIO
page_number: 087
page_id: XlsIO#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:50Z
fidelity: lossless
-->

## Use Cases for Targeting Different Excel Versions

### Overview
- Demonstrates setting and saving Excel files in different versions, including "Excel 97 to 2003" format.
- Highlights operations such as accessing worksheets, writing data, and selecting versions for saving.

### Content

#### Code Example in C#
```csharp
workbook.Version = ExcelVersion.Excel97to2003;

// The first worksheet object in the worksheets collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];

// Write data
sheet.Range["C3:O28"].Text = "Hello world";

// Save it as "Excel 97 to 2003" format.
workbook.SaveAs("Sample.xls");
```

#### Code Example in VB.NET
```vb
' Open an existing Excel 2007 file. Note that you should select the
' ExcelOpenType when opening
' .xlsx files
Dim workbook As IWorkbook =
excelEngine.Excel.Workbooks.Open("Excel2007.xlsx", ExcelOpenType.Automatic)

' Select the version to be saved.
workbook.Version = ExcelVersion.Excel97to2003

' The first worksheet object in the worksheets collection is accessed.
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Write data
sheet.Range("C3:O28").Text = "Hello world"

' Save it as "Excel 97 to 2003" format.
workbook.SaveAs("Sample.xls")
```

#### Xlsx File Format Support List

| **Support for Excel 2007 file formats in XlsIO**                                          |
|--------------------------------------------------------------------------------------------|
| **XML-based File Format Support**                                                         |
|                                                                                             |
| Gets/sets cells (text, date time, time span, error, number, Boolean, formula).            |
| New dimensions: 2^20 x 2^14.                                                              |
| Range operations such as copy/move range, insert/remove row/column, formula updates after  |
| these operations.                                                                         |
|                                                                                             |

### Page-level Navigation/TOC (Local)
- [Overview of XlsIO](#overview)
- Supported Features in XlsIO
- Setting Excel Versions and File Formats

### Cross References
- See also: [Syncfusion XlsIO Documentation](https://www.syncfusion.com/documentation/xlsio)

<!-- tags: XlsIO, Excel, Syncfusion Winforms, file format, version, worksheet, range, data manipulation keywords: Excel, XlsIO, workbook, worksheet, cell, data, version, file format, text, formula -->
```