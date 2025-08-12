```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: XlsIO
page_number: 045
page_id: XlsIO#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:30Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates inserting sample text into a cell.
- Explains saving and closing the workbook.
- Details disposing the Excel engine.

## Content

### Inserting Text into a Cell

```csharp
// Inserting sample text into the first cell of the first worksheet.
sheet.Range["A1"].Text = "Hello World";
```

```vb
' The first worksheet object in the worksheets collection is accessed.
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Inserting sample text into the first cell of the first worksheet.
sheet.Range("A1").Text = "Hello World"
```

The string "Hello World" is written to the cell **A1** of the document.

### Saving and Closing the Workbook

```csharp
// Saving the workbook to disk.
workbook.SaveAs("Sample.xls");

// Closing the workbook.
workbook.Close();
```

```vb
' Saving the workbook to disk.
workbook.SaveAs("Sample.xls")

' Closing the workbook.
workbook.Close()
```

The Workbook is saved and closed.

### Disposing the Excel Engine

```csharp
// Dispose the Excel engine
excelEngine.Dispose();
```

The engine should be disposed after completing workbook operations.

## API Reference

### Methods

- `SaveAs(string fileName)`
  - **Parameters:**
    - `fileName`: The file name and path to save the workbook.

- `Close()`
  - Closes the workbook.

- `Dispose()`
  - Disposes the Excel engine.

## Code Examples

### C#
- Demonstrates writing text, saving, and closing a workbook.

### VB
- Demonstrates equivalent functionality in VB.NET.

## Cross References
- Refer to the "Workbook Operations" section for more details.
- See also: "Workbook Saving and Closing" documentation.
- Additional documentation on disposing engine resources.

<!-- tags: [XlsIO, Syncfusion, WinForms, Excel, workbook, cell, text, save, close, dispose] keywords: [workbook, cell, text, save, close, dispose, engine] -->
```