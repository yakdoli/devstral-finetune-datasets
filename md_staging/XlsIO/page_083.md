```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: XlsIO
page_number: 083
page_id: XlsIO#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:53:35Z
fidelity: lossless
-->

# Essential XlsIO

### Overview
- Describes code samples for streaming Excel workbooks to the client browser.
- Demonstrates saving Excel files in various formats.
- Explains saving files in the Excel 97-2003 format.

## Content

### C#

```csharp
[C#]
workbook.Version = ExcelVersion.Excel2007;
// Stream the workbook to the client browser.
workbook.SaveAs("Sample.xlsx", Response, ExcelDownloadType.Open);
```

### VB.NET

```vbnet
[VB.NET]
workbook.Version = ExcelVersion.Excel2007
'Stream the workbook to the client browser.
workbook.SaveAs("Sample.xlsx", Response, ExcelDownloadType.Open);
```

Following code sample allows to prompt for the Save dialog box, to save the created file in some location in disk.

### C#

```csharp
[C#]
// Stream the workbook to the client browser.
workbook.SaveAs("Sample.xls", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.PromptDialog);
```

### VB.NET

```vbnet
[VB.NET]
'Stream the workbook to the client browser.
workbook.SaveAs("Sample.xls", ExcelSaveType.SaveAsXLS, Response, ExcelDownloadType.PromptDialog)
```

For more information on overloads of the workbook's Save method, refer Class Reference in the online documentation.

This section explains saving the files to the below formats.

### 3.7.1 Excel97to2003

XlsIO provides various overloads to save an Excel workbook. By default, when you save a workbook with `.xls` extension, it is saved to the Biff8 format [Excel97to2003 format].

### C#

```csharp
[C#]
```

## API Reference

### Save Method Overloads
- Refer to the Class Reference in the online documentation for more information on the overloads of the workbook's Save method.

## Code Examples

### Excel 97-2003 Format
- Demonstrates saving a workbook with `.xls` extension in the Biff8 format.

<!-- tags: [XlsIO, Excel, Workbook, Save, Stream, File Format, Excel97to2003] keywords: [Excel, Workbook, SaveAs, DownloadType, PromptDialog, Biff8, Excel2007, Excel2003, C#, VB.NET] -->
```