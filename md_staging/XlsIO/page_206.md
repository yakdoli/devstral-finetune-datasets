```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_206.jpeg
document_name: XlsIO
page_number: 206
page_id: XlsIO#page_206
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:57Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Locking and unlocking cells using the `Locked` property in XlsIO.
- Manipulating the `Locked` property to control cell editability in protected worksheets.
- The importance of worksheet protection for guarded editing scenarios.

## Content

### Cell Locking and Unlocking

XlsIO supports locking and unlocking cells by using the cell's **Locked** property, which can be manipulated to make certain cells editable in a protected worksheet. Please note that locking/unlocking a cell in an unprotected worksheet has no effect. For protecting the worksheet, see [Worksheet Protection](#).

**[C#]**

```csharp
// Opening the Existing (Protected) Worksheet from a Workbook
IWorkbook workbook = application.Workbooks.Open("CellProtectionTemplate.xls");

// Unlocking the cell which, need to be edited.
sheet.Range["A1"].CellStyle.Locked = false;
```

**[VB.NET]**

```vbnet
' Opening the Existing (Protected) Worksheet from a Workbook
Dim workbook As IWorkbook = application.Workbooks.Open("CellProtectionTemplate.xls")

' Unlocking the cells which, need to be edited.
sheet.Range("A1").CellStyle.Locked = False
```

### 4.1.4 Clipboard

The office clipboard in Excel is an extension of the Windows clipboard, and allows for easy transfer of data, by using the **Copy** and **Paste** commands. XlsIO provides support to copy a worksheet or workbook to the clipboard. It can be done by using the **CopyToClipboard** method as follows.

**[C#]**

```csharp
sheet.CopyToClipboard();
workbook.CopyToClipboard();
```

**[VB.NET]**

```vbnet
sheet.CopyToClipboard();
workbook.CopyToClipboard();
```

## API Reference (if applicable)

---

```html
<!-- tags: [xlsio, cell-locking, unlocking, worksheet-protection, clipboard, copy-to-clipboard, cell-protection, editability-configuration] keywords: [XlsIO, celllocked, cellUnlocking, worksheetProtection, clipboardIntegration, copyToClipboard] -->
``` 
```