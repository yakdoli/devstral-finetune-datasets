```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_397.jpeg
document_name: XlsIO
page_number: 397
page_id: XlsIO#page_397
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:53Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explanatory content related to protecting and unprotecting workbooks using password mechanisms.
- Demonstrates both C# and VB.NET code examples for workbook protection and unprotection.
- Highlights the functionality to disable sheet max/close/min button and prevent adding/removing sheets.

## Content

### Workbook Protection and Unprotection

#### C#

```csharp
// Protect Workbook.
workbook.Protect(isProtectWindow, isProtectContent, "syncfusion");

// Unprotect workbook.
// Opening a Existing(Protected) Workbook.
IWorkbook workbook = application.Workbooks.Open(@"ProtectedWorkbook.xls");

// Unprotecting( unlocking) Workbook by using the Password.
workbook.Unprotect("syncfusion");
```

#### VB.NET

```vbnet
' Protect Workbook.
workbook.Protect(isProtectWindow, isProtectContent, "syncfusion")

' Unprotect workbook.
' Opening a Existing(Protected) Workbook.
Dim workbook As IWorkbook = application.Workbooks.Open("ProtectedWorkbook.xls")

' Unprotecting (unlocking) Workbook by using the Password.
workbook.Unprotect("syncfusion")
```

### Key Features Illustrated

Following illustration shows a protected document with the sheet max/close/min button disabled, also no sheets can be added/removed to the document.

## API Reference

### Workbook Protection Methods

- **Protect**: Protects the workbook with specified settings and a password.
  - Parameters:
    - `isProtectWindow`: Boolean indicating whether to protect the window.
    - `isProtectContent`: Boolean indicating whether to protect the content.
    - `password`: String representing the password for protection.

- **Unprotect**: Unprotects the workbook using the provided password.
  - Parameters:
    - `password`: String representing the password to unprotect the workbook.

## Code Examples

The provided code examples illustrate how to:
- Protect a workbook with a password.
- Open an existing protected workbook.
- Unlock the workbook using the correct password.

## Related Features

The functionality described here is part of the broader suite of Excel workbook manipulation features provided by the XlsIO library in Syncfusion Winforms.

### Remarks

The example code demonstrates a secure way to handle workbook protection, ensuring that only authorized users can access or modify the contents of the workbook.

<!-- tags: [xlsio, workbooks, protection, unprotection, password, syncfusion, winforms, 11.4.0.26] keywords: [workbook, excel, protection, unprotection, password, syncfusion, winforms, protect, unprotect, workbook methods] -->
```