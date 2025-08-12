```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_396.jpeg
document_name: XlsIO
page_number: 396
page_id: XlsIO#page_396
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:51Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Windows in a workbook with protection cannot be moved, resized, hidden, unhidden, or closed.
- Windows in a workbook with protection are sized and positioned the same way each time the workbook is opened.
- This can be done by selecting the `Protection` option from the `Tools` menu in Excel.

## Content

### Workbook Protection in Excel
Windows in a workbook with protection cannot be moved, resized, hidden, unhidden, or closed. These windows are consistently sized and positioned when the workbook is opened. Protection can be configured by selecting the `Protection` option from the `Tools` menu in Excel.

#### Figure 144: Tools Menu - Protection
![Figure 144: Tools menu - Protection](image/figure144.png)

#### Figure 145: Protect Workbook Dialog Box
The Protect Workbook dialog box allows users to secure a workbook with specific options and password protection.

![Figure 145: Protect Workbook Dialog Box](image/figure145.png)

### Protect Method in IWorkbook Interface
The `Protect` method of the `IWorkbook` interface provides options to protect and unprotect documents with a password in XlsIO. You can also set or reset the `Window` and `Structure` options using this method.

#### Protecting a Workbook with a Password

The following code example illustrates how to protect a workbook with a password.

### Protect Method
- **Purpose**: Provides options to protect and unprotect documents using a password.
- **Parameters**:
  - **Structure**: Protects the structure of the workbook.
  - **Windows**: Protects the windows of the workbook.
  - **Password**: An optional password to secure the workbook.

## Code Examples
Following is how you can protect a workbook with a password using the `Protect` method:

```csharp
// Assume workbook is already initialized and ready for protection
workbook.Protect("MyPassword");
```

## Cross References
- See also: [Syncfusion Documentation for XlsIO Protection](https://documentation.syncfusion.com/windowsforms/XlsIO/)

## API Reference
- **Namespace**: Syncfusion.XlsIO
- **Class**: IWorkbook
- **Method**: `Protect(string password)`

### Parameters
- **password**: Optional string that can be used to secure the workbook.

### Returns
- None.

### Exceptions
- Throws an exception if the password is invalid or if the workbook is already protected with a different password.

## RAG Annotations
<!-- tags: [XlsIO, workbook protection, Excel, IWorkbook, Syncfusion, WindowsForms, structure, windows, password] keywords: [protection, dialog box, password, structure, windows, workbook, tools menu, protect method, IWorkbook, Syncfusion] -->
```