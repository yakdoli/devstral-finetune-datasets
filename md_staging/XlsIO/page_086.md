```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: XlsIO
page_number: 086
page_id: XlsIO#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:19Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates setting the default Excel version using Syncfusion's `ExcelEngine`.
- Includes C# and VB.NET code examples for handling Excel files.
- Supports saving and converting between .xls and .xlsx formats.

## Content

### Setting the Default Excel Version

#### C#
```csharp
ExcelEngine excelEngine = new ExcelEngine();
IApplication application = excelEngine.Excel;

// Select the default version as Excel 2007 or Excel 2010;
application.DefaultVersion = ExcelVersion.Excel2007; // or
// application.DefaultVersion = ExcelVersion.Excel2010;

// Open an existing Excel 2007 file.
IWorkbook workbook = excelEngine.Excel.Workbooks.Open("Excel2007.xlsx");

// Save it as "Excel2007" format.
workbook.SaveAs("Sample.xlsx");
```

#### VB.NET
```vbnet
Dim excelEngine As ExcelEngine = New ExcelEngine()
Dim application As IApplication = excelEngine.Excel

' Set the default version as Excel 2007;
application.DefaultVersion = ExcelVersion.Excel2007 ' Or
' application.DefaultVersion = ExcelVersion.Excel2010

' Open an existing Excel 2007 file.
Dim workbook As IWorkbook = _
    excelEngine.Excel.Workbooks.Open("Excel2007.xlsx")

' Save it as "Excel 2007" format.
workbook.SaveAs("Sample.xlsx")
```

### File Conversion Between .xls and .xlsx

Essential XlsIO also allows to open an existing .xls file and save it to the .xlsx format [with supported elements], or open an .xlsx file and save it to the .xls format.

#### C#
```csharp
// Open an existing Excel 2007 file. Note that you should select the
// ExcelOpenType when opening .xlsx files
IWorkbook workbook = excelEngine.Excel.Workbooks.Open("Excel2007.xlsx", ExcelOpenType.Automatic);

// Select the version to be saved.
```

## API Reference

### `ExcelEngine` Class

- **Properties**
  - `DefaultVersion`: Specifies the default version of Excel to use when creating new workbooks or saving them.

- **Methods**
  - `Excel`: Returns the `IApplication` interface for interacting with Excel documents.

### `IApplication` Interface

- **Properties**
  - `DefaultVersion`: Gets or sets the default version of Excel.

### `IWorkbook` Interface

- **Methods**
  - `Open(string fileName, ExcelOpenType openType)`: Opens an existing Excel file.
  - `SaveAs(string fileName)`: Saves the workbook with the specified file name.

### Enums

- **ExcelVersion**
  - `Excel2007`
  - `Excel2010`

- **ExcelOpenType**
  - `Automatic`

## Code Examples

### Opening and Saving Excel Files

The following C# example demonstrates how to open an existing Excel 2007 file and save it as an Excel 2007 format (.xlsx) file.

#### Opening an Excel File
```csharp
// Open an existing Excel 2007 file.
IWorkbook workbook = excelEngine.Excel.Workbooks.Open("Excel2007.xlsx", ExcelOpenType.Automatic);
```

#### Saving an Excel File
```csharp
// Save it as "Excel2007" format.
workbook.SaveAs("Sample.xlsx");
```

### Handling File Format Conversion
Essential XlsIO supports converting between .xls and .xlsx formats, allowing users to work seamlessly with both legacy and modern Excel files.

## See also
- [Excel Version Support in Essential XlsIO](#)
- [Working with Excel Files](#)

<!-- tags: [Essential XlsIO, ExcelEngine, IApplication, IWorkbook, ExcelVersion, ExcelOpenType, file conversion, .xls, .xlsx] keywords: [default version, Excel 2007, Excel 2010, file format conversion, C#, VB.NET, open, save, supported elements] -->
```