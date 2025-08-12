```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: XlsIO
page_number: 095
page_id: XlsIO#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:33Z
fidelity: lossless
-->

# XlsIO

## Overview
- Demonstrates how to create and manipulate Excel files using the Syncfusion XlsIO library.
- Includes examples in both C# and VB.NET for creating and saving an Excel file as SpreadsheetML.
- Example of opening an existing SpreadsheetML file and modifying its content.

## Content

### Creating and Saving an Excel File as SpreadsheetML

The following code examples illustrate how to create a new Excel file, write data, and save it as a SpreadsheetML file.

#### C# Example
```csharp
// The first worksheet object in the worksheets collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];

// Write data
sheet.Range["C3:O28"].Text = "Hello world";

// Save as SpreadsheetML.
workbook.SaveAsXml("Sample.xml", ExcelXmlSaveType.MSExcel);
```

#### VB.NET Example
``` vb
' Create a new workbook
Dim workbook As IWorkbook = excelEngine.Excel.Workbooks.Create(3)

' The first worksheet object in the worksheets collection is accessed.
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Write data
sheet.Range("C3:O28").Text = "Hello world"

' Save as SpreadsheetML.
workbook.SaveAsXml("Sample.xml", ExcelXmlSaveType.MSExcel)
```

### Opening an Existing SpreadsheetML File

The following code example illustrates how to open an existing SpreadsheetML file, modify its content, and save it.

#### C# Example
```csharp
// Open an existing SpreadsheetML file.
IWorkbook workbook = excelEngine.Excel.Workbooks.Open("spreadsheetml.xml", ExcelXmlOpenType.MSExcel);

// The first worksheet object in the worksheets collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];

// Write data
sheet.Range["C3:O28"].Text = "Hello world";

// Save as SpreadsheetML.
workbook.SaveAsXml("Sample.xml", ExcelXmlSaveType.MSExcel);
```

#### VB.NET Example
```vb
' Open an existing SpreadsheetML file.
' Additional VB.NET code to open and modify the file would follow here.
```

## Notes
- Ensure that the `excelEngine` object is properly initialized before executing these code snippets.
- The `ExcelXmlSaveType.MSExcel` parameter specifies that the file should be saved in a format compatible with Microsoft Excel.

<!-- tags: [Syncfusion, Winforms, XlsIO, Excel, SpreadheetML] keywords: [workbook, worksheet, Range, Text, SaveAsXml, ExcelXmlSaveType, OpenType, C#, VB.NET] -->
```