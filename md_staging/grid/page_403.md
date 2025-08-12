```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_403.jpeg
document_name: grid
page_number: 403
page_id: grid#page_403
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Exporting data to an Excel spreadsheet is a commonly preferred feature in the .NET world.
- The Essential Grid control offers in-built support for exporting to Excel.
- The class `GridExcelConverterControl` is used for exporting grid or Grid Data Bound Grid control data to an Excel spreadsheet for verification and computation.
- This class automatically copies grid styles and formats to an Excel spreadsheet.
- The `GridExcelConverterControl` class is derived from the `GridExcelConverterBase` class.
- The XlsIO libraries are used for converting grid contents to Excel.

## Content

### Exporting Grid Data to Excel

#### Requirements for the Control to Function

For the control to function, the following dll files should be added along with the default dll files in the reference folder:

- **Syncfusion.GridConverter.Base**
- **Syncfusion.XlsIO.Base**

#### Exporting Grid to Excel

The `GridToExcel` method is used to export the grid content to an Excel sheet. Below are examples demonstrating how to convert the content in Grid control to an Excel spreadsheet in C# and VB.NET.

### Using C#

```csharp
[ C# ]

Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = new Syncfusion.GridExcelConverter.GridExcelConverterControl();
gecc.GridToExcel(this.gridControl1.Model, @"C:\MyGC.xls");
```

### Using VB.NET

```vb
[ VB.NET ]

Dim gecc As Syncfusion.GridExcelConverter.GridExcelConverterControl = New Syncfusion.GridExcelConverter.GridExcelConverterControl()
gecc.GridToExcel(Me.gridControl1.Model, "C:\MyGC.xls")
```

## API Reference (if applicable)

### Summary

- **Class**: `GridExcelConverterControl`
- **Base Class**: `GridExcelConverterBase`
- **DLLs Required**: 
  - `Syncfusion.GridConverter.Base`
  - `Syncfusion.XlsIO.Base`
- **Method**: `GridToExcel`
  - **Parameters**:
    - `Model`: Grid model to export.
    - `FilePath`: Path to the Excel file to export.

## Code Examples (if applicable)

### C# Code Example

```csharp
[ C# ]

Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = new Syncfusion.GridExcelConverter.GridExcelConverterControl();
gecc.GridToExcel(this.gridControl1.Model, @"C:\MyGC.xls");
```

### VB.NET Code Example

```vb
[ VB.NET ]

Dim gecc As Syncfusion.GridExcelConverter.GridExcelConverterControl = New Syncfusion.GridExcelConverter.GridExcelConverterControl()
gecc.GridToExcel(Me.gridControl1.Model, "C:\MyGC.xls")
```

## Page-level Navigation/TOC (if applicable)

### Section Summary

This section covers the functionality and usage of the `GridExcelConverterControl` to export grid data to an Excel spreadsheet.

## RAG Annotations

<!-- tags: [grid, excel, export, windows forms, Syncfusion] keywords: [GridExcelConverterControl, GridExcelConverterBase, XlsIO, GridData, ExportToExcel, ExcelFile, GridConverter, Model] -->
```