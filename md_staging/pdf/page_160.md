```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_160.jpeg
document_name: pdf
page_number: 160
page_id: pdf#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:28Z
fidelity: lossless
-->

## Overview
- This page explains how to set styles and adjust column widths for PDF grids in Syncfusion Winforms using C# and VB.NET.
- It discusses applying styles to individual rows and all rows in a PDF grid.
- It includes details on setting the width for a particular column and provides corresponding code examples.

## Content

### Setting Styles for Rows in PdfGrid

**C#**
```csharp
// Set style for the PdfGridRow.
pdfGrid.Rows[0].ApplyStyle(pdfGridCellStyle);
```

**VB.NET**
```vbnet
// Set style for the PdfGridRow.
pdfGrid.Rows(0).ApplyStyle(pdfGridCellStyle)
```

All rows in the PdfGrid can be set with the same style using the `ApplyStyle` method of `PdfGridRowCollection`. This style can be a `PdfGridRowStyle` or `PdfGridCellStyle`. The following is the code snippet:

**C#**
```csharp
// Set style for all rows in PdfGrid.
pdfGrid.Rows.ApplyStyle(style);
```

**VB.NET**
```vbnet
// Set style for all rows in PdfGrid.
pdfGrid.Rows.ApplyStyle(style)
```

Refer to the following topic for more details:  
[**PdfGridCellStyle**](https://)

### Column

#### Width

By default, all the columns in PdfGrid have equal width, and the columns automatically fill the entire width of the PdfGrid. If the width of the PdfGrid is increased or decreased, the column width also changes appropriately.

You can specify the width for a particular column by using the `Width` property. The following code example illustrates how to set the width.

**C#**
```csharp
[Unclear]
```

## Page-level Navigation/TOC (if applicable)

- Setting Styles for Rows in PdfGrid
- ApplyStyle Method
- Column
  - Width

## Cross References

See also:  
- [**PdfGridCellStyle**](https://)

## API Reference (if applicable)

### Properties

- **Width**
  - Type: `double`
  - Description: Specifies the width of a particular column.

### Methods

- **ApplyStyle**
  - Parameters:
    - `style`: `PdfGridCellStyle` or `PdfGridRowStyle`
  - Description: Applies the specified style to the rows of the PdfGrid.

## Code Examples (multi-language supported)

**C#**
```csharp
// Setting style for a specific row
pdfGrid.Rows[0].ApplyStyle(pdfGridCellStyle);

// Setting style for all rows
pdfGrid.Rows.ApplyStyle(style);

// Setting column width
pdfGrid.Columns[0].Width = 100;
```

**VB.NET**
```vbnet
// Setting style for a specific row
pdfGrid.Rows(0).ApplyStyle(pdfGridCellStyle)

// Setting style for all rows
pdfGrid.Rows.ApplyStyle(style)

// Setting column width
pdfGrid.Columns(0).Width = 100
```

<!-- tags: [Syncfusion Winforms, PdfGrid, Grid, PdfGridRow, Column, Width, ApplyStyle, PdfGridCellStyle, method, property, version: 11.4.0.26] keywords: [PdfGrid, applyStyle, column width, grid, set style, PdfGridRow, PdfGridCellStyle, Columns] -->
```