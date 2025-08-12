```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: XlsIO
page_number: 069
page_id: XlsIO#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:54Z
fidelity: lossless
-->

## Overview
- This page discusses the `IWorkbooks` interface and its methods related to managing workbooks in the XlsIO library.
- Methods include adding, closing, creating, opening, and pasting workbooks, providing flexibility for programmatic interactions with Excel documents.

## Content

### 3.6.2 Workbook

#### IWorkbooks
- **Description**:  
  `IWorkbooks` is a collection of all the workbook objects that are currently open in the Excel application. This is responsible for adding new workbooks, opening existing workbooks, creating new workbooks, and pasting workbooks.

- **Public Methods**:  
  Public methods exposed by this interface are given in the following table:

##### Public Methods

| **Methods**         | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| Add                | Add another workbook to the collection.                                       |
| Close              | Closes the workbook object.                                                    |
| Create             | Creates new workbook with three worksheets, by default.                       |
| Open               | Opens an existing document.                                                    |
| OpenFromXml       | Opens SpreadsheetML document.                                                  |
| OpenReadOnly       | Opens the workbook as read-only, when the workbook is already opened.        |
| PasteWorkbook      | Pastes workbook from the clipboard.                                           |

### Additional Notes
- There are various options for opening an existing workbook that allows us to skip parsing, select the version of the files, provide password, and open as a stream.
- Opening from disk. `ExcelOpenType` has an option `Automatic` that enables the automatic selection of the version, as given below:

#### Code Example

```csharp
// [C#]
```

## RAG Annotations
<!-- tags: [xlsio, workbook, iworkbooks, methods, excelfile, syncfusion winforms] keywords: [workbook management, iworkbooks interface, add, close, create, open, openfromxml, openreadonly, pasteworkbook, excelopenautomatic, csharp code example] -->
```