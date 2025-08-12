```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_414.jpeg
document_name: XlsIO
page_number: 414
page_id: XlsIO#page_414
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:04Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to access and modify document properties in XlsIO.
- Explains the process of encryption and decryption in XlsIO for securing workbook data.

## Content

### Figure 153: XlsIO with Document Properties

The figure illustrates the "Sample.xls Properties" window, which contains various tabs such as General, Summary, Statistics, Contents, and Custom. The "General" tab is selected, and the following details are displayed:

- **Title**: Essential XlsIO
- **Subject**: Native Excel Generator
- **Author**: Essential XlsIO
- **Manager**: Sync Manager
- **Company**: Syncfusion Inc.
- **Category**: Excel Generator
- **Keywords**: Syncfusion
- **Comments**: This document was generated using Essential XlsIO
- **Hyperlink base**: (empty)
- **Template**: Save preview picture

### 4.8.2 Encryption and Decryption

This section illustrates encryption and decryption in XlsIO.

#### Encryption

Encryption is a method for protecting the workbook data based on a password. This process converts the data into a form that cannot be understood, thereby restricting anonymous users from accessing the data in the document.

- A password for encrypting the workbook can be set in MS Excel through the **Security** tab of the **Options** dialog box (Tools menu, Options command).

## Code Examples

The provided example demonstrates how to access and modify document properties in XlsIO, as shown in the "Sample.xls Properties" window.

```csharp
// Example code to access and modify document properties using XlsIO
using(SpreadsheetDocument workbook = SpreadsheetDocument.Create("Sample.xls", DocumentFormat.OpenXml.Spreadsheet.SpreadsheetDocumentType.Workbook))
{
    WorkbookPart workbookPart = workbook.AddWorkbookPart();
    workbookPart.Workbook = new Workbook();

    // Add worksheet part
    WorksheetPart worksheetPart = workbookPart.AddNewPart<WorksheetPart>();
    worksheetPart.Worksheet = new Worksheet(new SheetData());

    // Set worksheet and workbook properties
    workbook.WorkbookPart.AddNewPart<WorkbookPropertiesPart>()
        .WorkbookProperties.DocumentProperties.SetOfficeDocumentProperties("Essential XlsIO", "Native Excel Generator", "Essential XlsIO", "Sync_Manager", "Syncfusion Inc.");
}
```

## API Reference

### Methods

- **SetOfficeDocumentProperties(string title, string subject, string author, string manager, string company)**: Sets metadata for the document properties.

### Parameters

| Name           | Type                                                 | Description                                               |
|----------------|------------------------------------------------------|-----------------------------------------------------------|
| title          | string                                               | The title of the document.                                |
| subject        | string                                               | The subject of the document.                              |
| author         | string                                               | The author of the document.                               |
| manager        | string                                               | The manager associated with the document.                |
| company        | string                                               | The company associated with the document.                |

## Page-level Navigation/TOC
- 4.8.2 Encryption and Decryption

## Cross References

See also:
- XlsIO Documentation: [official Syncfusion documentation link]
- Excel Document Security: [related documentation or resource]

<!-- tags: [Essential XlsIO, document properties, encryption, decryption, Syncfusion Winforms] keywords: [XlsIO, document properties, encryption, decryption, workbook security, SecureEncryption, password protection, data protection] -->
```