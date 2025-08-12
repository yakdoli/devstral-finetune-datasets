```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: XlsIO
page_number: 082
page_id: XlsIO#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:05Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This page describes how to save workbooks using Essential XlsIO in Windows Forms, Web Forms, and WPF applications.
- Covers saving files to different formats and implementing the `SaveAs` method for disk and stream support.
- Provides sample code for saving workbooks to disk and streaming them to the client browser in both Windows (C# and VB.NET) and Web applications.

## Content

### 3.7 Saving a Workbook
Essential XlsIO is a Non-UI component that can be used on Windows Forms, Web Forms, and WPF applications.

Any changes made in a new or existing worksheet will be affected only if the workbook is saved to a disk or a stream. XlsIO supports saving files to different formats in stream and disk by using the `SaveAs` method of `IWorkbook`. The workbook can be saved to stream/disk/response. The only code that is specific for the usage of XlsIO in a Windows Forms application and WPF application is the saving of the spreadsheet to disk, and for Web Forms applications, it is the streaming of the spreadsheet to the client browser.

#### The following is the code sample to save the document to disk:

#### Saving Worksheet in Windows and WPF Applications

```csharp
[C#]
// Saving the workbook to disk.
workbook.SaveAs("Sample.xls");
```

```vbnet
[VB.NET]
'Saving the workbook to disk.
workbook.SaveAs("Sample.xls");
```

#### Saving Worksheet in Web Applications

```csharp
[C#]
// Stream the workbook to the client browser.
workbook.SaveAs("Sample.xls", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.Open);
```

```vbnet
[VB.NET]
'Stream the workbook to the client browser.
workbook.SaveAs("Sample.xls", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.Open)
```

#### Similarly, you can open an xlsx file inside the browser by using the following code sample.
```markdown

<!-- tags: [Essential XlsIO, workbook saving, disk saving, stream saving, Windows Forms, WPF, Web Applications, C#, VB.NET] keywords: [Essential XlsIO, SaveAs, IWorkbook, Windows Forms, WPF, Web Applications, workbook, stream, disk, ExcelSaveType, ExcelDownloadType, Sample.xls, C#, VB.NET, xlsx file, browser] -->
```