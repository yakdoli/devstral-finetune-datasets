```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_426.jpeg
document_name: XlsIO
page_number: 426
page_id: XlsIO#page_426
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:08Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Learn how to merge multiple Excel files into a single file.
- Discover how to open Excel files from a stream.

## Content

### 5.1.5 How to merge several Excel files to a single file?

XlsIO provides support to merge several Excel files to a single file. The following code example illustrates how to do this.

#### C#

```csharp
// Merging worksheets.
destinationWorkbook.Worksheets.AddCopy(sourceWorkbook.Worksheets);
```

#### VB.NET

```vb
' Merging worksheets.
destinationWorkbook.Worksheets.AddCopy(sourceWorkbook.Worksheets)
```

### 5.1.6 How to open an Excel file from Stream?

XlsIO provides support for opening a template spreadsheet that is stored as a stream. The following code example illustrates this.

#### C#

```csharp
// Opening a File from a Stream.
FileStream fs = new FileStream(@"...\..\...\Data\OpenFromStreamTemplate.xls", FileMode.Open, FileAccess.ReadWrite, FileShare.ReadWrite);
fs.Seek(0, SeekOrigin.Begin);
IWorkbook workbook = application.Workbooks.Open(fs);
```

#### VB.NET

```vb
' Opening a File from a Stream.
Dim fs As FileStream = New FileStream("...\..\...\Data\OpenFromStreamTemplate.xls", FileMode.Open, FileAccess.ReadWrite, FileShare.ReadWrite)
fs.Seek(0, SeekOrigin.Begin)
Dim workbook As IWorkbook = application.Workbooks.Open(fs)
```

## Cross References
- See also: "How to merge several Excel files to a single file" and "How to open an Excel file from Stream."

<!-- tags: [XlsIO, Excel merging, Excel stream] keywords: [XlsIO, merge, Excel files, stream] -->
```