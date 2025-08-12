```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_197.jpeg
document_name: XlsIO
page_number: 197
page_id: XlsIO#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:36Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// Saving the workbook to disk.
destinationWorkbook.SaveAs("Sample.xls");

// Close the workbook.
destinationWorkbook.Close();
```

[VB.NET]

```vb
' Open the Source WorkBook.
Dim sourceWorkbook As IWorkbook = _
    application.Workbooks.Open(".....\Data\SourceWorkbookTemplate.xls")

' Open the Destination WorkBook.
Dim destinationWorkbook As IWorkbook = _
    application.Workbooks.Open(".....\Data\DestinationWorkbookTemplate.xls")

' Copy the first worksheet from the Source workbook to the destination workbook.
destinationWorkbook.Worksheets.AddCopy(sourceWorkbook.Worksheets(0))

' Activate the newly added worksheet in the destination workbook.
destinationWorkbook.ActiveSheetIndex = 1

' Saving the workbook to disk.
destinationWorkbook.SaveAs("Sample.xls")

' Close the workbook.
destinationWorkbook.Close()
```

## Overview

- Copying the first worksheet from a source workbook to a destination workbook.
- Specifying copy options for performance and formatting while copying.

## Content

You can also specify copy options while copying a worksheet, if you are interested in improving the performance, and if you are interested in ignoring certain formatting while copying through the `ExcelWorksheetCopyFlags` enumerator. Following are the values for this enumerator.

| Member name       | Description                     |
|-------------------|----------------------------------|
| None             | No flags.                       |
| ClearBefore      | Represents the ClearBefore copy flags. |
| CopyNames        | Copies Names.                   |
| CopyCells        | Copies whole Cells.             |
| CopyRowHeight    | Copies Row Height.              |

<!-- tags: [xlsio, workbook, worksheet, copy options, excelworksheetcopyflags] keywords: [source workbook, destination workbook, copy, save, close, worksheet copy options, performance, formatting, clearbefore, copynames, copycells, copyrowheight] -->
```