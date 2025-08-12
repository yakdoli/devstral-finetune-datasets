```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: XlsIO
page_number: 109
page_id: XlsIO#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:55:39Z
fidelity: lossless
-->

# Essential XlsIO

## Overview

- Comparison of features between `.xls` and `.xlsx` formats.
- Focus on read and write capabilities for various elements in Excel.

## Content

The following table compares the capabilities of different Excel elements between `.xls` and `.xlsx` formats:

| Element                          | **xls**   | **xls**   | **xlsx**  | **xlsx**  |
|----------------------------------|-----------|-----------|-----------|-----------|
|                                   | Read      | Write     | Read      | Write     |
| Template marker                  | Yes       | Yes       | Yes       | Yes       |
| Outlines (group/ungroup, summary settings) | Yes       | Yes       | Yes       | Yes       |
| Comments                         | Yes       | Yes       | Yes       | Yes       |
| Freeze pane, split pane          | Yes       | Yes       | Yes       | Yes       |
| View (Zoom, show/hide gridline, show/hide headings), horizontal/vertical scroll bars | Yes       | Yes       | Yes       | Yes       |
| Macros                           | No        | No        | No        | No        |
| Encryption                        | Yes       | Yes       | Yes       | Yes       |
| Decryption                        | No        | No        | No        | No        |
| OLE Objects                       | No        | No        | No        | No        |
| Track changes                     | No        | No        | No        | No        |
| Streams                           | Yes       | Yes       | Yes       | Yes       |
| Themes                            | -         | -         | Yes       | Yes       |
| Cell gradient                     | -         | -         | Yes       | Yes       |
| Advanced CF (icon, databars, Color scales) | -         | -         | Yes       | Yes       |
| Tables                            | -         | -         | Yes       | Yes       |

## API Reference

This section provides information on the APIs related to handling Excel files in `.xls` and `.xlsx` formats. For detailed API references, refer to the Syncfusion documentation.

### Methods and Properties

- `LoadStream`: Loads an Excel file from a stream into a workbook.
- `Save`: Saves the current workbook to a file or stream.

## Code Examples

### Example: Reading and Writing Excel Files

```csharp
using Syncfusion.XlsIO;
using System.IO;

// Create a new Workbook instance.
using (ExcelEngine excelEngine = new ExcelEngine())
{
    IWorkbook workbook = excelEngine.Excel.Workbooks.Create(1);
    IWorksheet worksheet = workbook.Worksheets[0];

    // Write data to the worksheet.
    worksheet.CreateTextRange("A1", "Hello, World!");

    // Save the workbook to a file.
    FileStream fileStream = new FileStream("output.xlsx", FileMode.Create, FileAccess.Write);
    workbook.SaveAs(fileStream);
    fileStream.Close();
}

// Reading the workbook.
using (ExcelEngine excelEngine = new ExcelEngine())
{
    using (IWorkbook workbook = excelEngine.Excel.Workbooks.Open("output.xlsx"))
    {
        IWorksheet worksheet = workbook.Worksheets[0];
        string data = worksheet.CreateTextRange("A1").Text;
        Console.WriteLine(data);
    }
}
```

This example demonstrates how to write to and read from an `.xlsx` file using the `XlsIO` API.

<!-- tags: [xlsio, essentialxlsio, excel, xls, xlsx, read, write, api, version:11.4.0.26] keywords: [excel, formatting, templates, outlines, comments, freeze, scrollbars, macros, encryption, streams, themes, gradients, color scales, tables] -->
```