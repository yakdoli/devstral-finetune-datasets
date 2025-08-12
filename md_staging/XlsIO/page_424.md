```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_424.jpeg
document_name: XlsIO
page_number: 424
page_id: XlsIO#page_424
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:36Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
IRange src = sheet1.Range["A3"];
IRange dest = sheet1.Range["B1"];
src.CopyTo(dest, ExcelCopyRangeOptions.None);
```

```vb
[VB.NET]

Dim src As IRange = sheet1.Range("A3")
Dim dest As IRange = sheet1.Range("B1")
src.CopyTo(dest, ExcelCopyRangeOptions.None)
```

## Overview
- This section describes how to copy a range within the same worksheet.
- It includes examples in C# and VB.NET to demonstrate the `CopyTo` method usage for copying data between ranges in the same worksheet.

## Content

### 5.1.3 How to copy a range from one workbook to another?

The Range and CopyTo methods include overloads for copying the Source Worksheet range to the Destination Worksheet range. The following code example illustrates how to copy a range from one workbook to another workbook.

- **C# Example:**

```csharp
// The first worksheet object in the worksheets collection in the Source
// Workbook is accessed.
IWorksheet SourceWorksheet = SourceWorkbook.Worksheets[0];

// The first worksheet object in the worksheets collection in the
// Destination Workbook is accessed.
IWorksheet DestinationWorksheet = DestinationWorkbook.Worksheets[0];

// Assigning an object to the range of cells (90 rows) both for source and
// destination.
IRange source = SourceWorksheet.Range[1, 1, 90, 100];
IRange des = DestinationWorksheet.Range[1, 1, 90, 100];

// Copying (90 rows) from Source to Destination worksheet.
source.CopyTo(des);
```

- **VB.NET Example:**

```vb
' The first worksheet object in the worksheets collection in the Source
' Workbook is accessed.
Dim SourceWorksheet As Syncfusion.XlsIO.IWorksheet = 
SourceWorkbook.Worksheets(0)

' The first worksheet object in the worksheets collection in the Destination
```

<!-- tags: [Syncfusion, Winforms, XlsIO, worksheet, range, copyto, workbook, c#, vb.net] keywords: [IRange, IWorksheet, CopyTo, ExcelCopyRangeOptions, SourceWorkbook, DestinationWorkbook, Range, C#, VB.NET] -->
```