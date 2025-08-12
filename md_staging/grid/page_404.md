```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_404.jpeg
document_name: grid
page_number: 404
page_id: grid#page_404
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to export a Grid content to an Excel spreadsheet.
- Includes examples of text color, background color, font styles, and alignment in a grid.
- Provides code examples for exporting a Grid Data Bound Grid control to an Excel spreadsheet using C# and VB.NET.

## Content

### Screenshot of the Grid to be Exported

<figure>
    <img src="grid_export_demo.png" alt="Grid to be Exported">
    <figcaption>Figure 147: Grid to be Exported</figcaption>
</figure>

The following code example illustrates how to convert the content in Grid Data Bound Grid control to an Excel spreadsheet.

### Using C#

```csharp
[C#]

Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = new Syncfusion.GridExcelConverter.GridExcelConverterControl();
gecc.GridToExcel(this.gridDataBoundGrid1.Model, @"C:\MyGC.xls");
```

### Using VB.NET

```vb
[VB.NET]
```

## Page-level Navigation/TOC (if applicable)

- Overview
- Content
  - Screenshot of the Grid to be Exported
  - Using C#
  - Using VB.NET

## Cross References

See also:
- Related documentation on Syncfusion Grid components
- Additional examples and tutorials for working with Excel export functionality

<!-- tags: [Essential Grid, Windows Forms, Excel Export, Grid Data Bound Grid, C#, VB.NET] keywords: [Syncfusion, Grid control, Windows Forms, Excel, export, C#, VB.NET, Grid Data Bound Grid, text color, background color, font styles, alignment] -->
```