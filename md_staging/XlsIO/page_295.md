```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_295.jpeg
document_name: XlsIO
page_number: 295
page_id: XlsIO#page_295
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:12Z
fidelity: lossless
-->

## Overview

- Demonstrates adding Option Button controls to a spreadsheet using Essential XlsIO.
- Explains the usage of OLE Objects for embedding or linking data in Excel documents.
- Highlights the support for reading and writing OLE Objects in XLSX format using the `I OleObject` interface.

## Content

### Example Code for Adding Option Buttons

The following code snippet illustrates how to add and manage Option Button controls in a spreadsheet:

```csharp
optionButton2.CheckState = ExcelCheckState.Unchecked
workbook.SaveAs("Unchecked.xlsx")
workbook.Close()
excelEngine.Dispose()
```

### Visual Representation of Option Buttons

The figure below shows how the Option Button control has been added to the spreadsheet using Essential XlsIO.

![Figure 99: Option Button control added to the Spreadsheet by using Essential XlsIO](attachment:OptionButtonControl.png)

**Figure 99: Option Button control added to the Spreadsheet by using Essential XlsIO**

### 4.2.9 OLE Objects

#### Overview of OLE Objects

**Object Linking and Embedding (OLE):**

Object Linking and Embedding (OLE) is one of the most widely used methods for inserting data into Microsoft Office documents. Although embedding or linking objects increases the size of the original document, it enhances document readability by providing offline access to content. Before reading the content of the object, the associated software must be installed in the machine. For example, to read a PDF file linked or embedded in an Excel document, Adobe Reader is required.

Essential XlsIO provides read and write support for OLE Objects in XLSX format. These objects can be linked or embedded in Excel documents using the `I OleObject` interface.

#### Note on Platform Support

**Note:** Currently, the read and write functions for OLE Objects are supported in Windows, ASP.NET, and WPF platforms only.

## API Reference

### Namespaces and Classes

- **Namespace:** Syncfusion.XlsIO
- **Class:** OleDb
- **Interface:** `I OleDbObject`

#### Parameters and Methods

- Use `I OleDbObject` for reading and writing OLE Objects.
- Ensure the associated software is installed for linked or embedded OLE Objects.

## Code Examples

### Example: Embedding an OLE Object

```csharp
// Embedding an OLE Object
using (var excelEngine = new ExcelEngine())
{
    var workbook = excelEngine.Excel.Workbooks.Create(1);
    IWorksheet worksheet = workbook.Worksheets[0];

    // Add OLE object
    I OleObject oleObject = worksheet.OleObjects.Add("Excel.Sheet.12", 10, 10, "C:\\Path\\To\\Your\\Document.xlsx");

    // Save and dispose
    workbook.SaveAs("EmbeddedOLEObject.xlsx");
    workbook.Close();
}

excelEngine.Dispose();
```

## Cross References

See also:

- Appendix: Guide to Embedding Documents and Objects
- Section: Managing Document Formats in Microsoft Office

<!-- tags: [Essential XlsIO, OLE Objects, Excel, XlsIO, Winforms, C#, I OleObject] keywords: [OLE, Object Linking, Embedding, Excel, XLSX, I OleObject, documentation] -->
```