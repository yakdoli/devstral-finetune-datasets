```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: pdf
page_number: 158
page_id: pdf#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:14Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Explains how to specify the row height for PdfGrid using the `PdfGridRow.Height` property.
- Demonstrates how to merge cells within a row using the `PdfGridCell.RowSpan` property.
- Includes examples in both C# and VB.NET.

## Height

The Height property of the PdfGridRow class is used to specify the row height for the PdfGrid rows. The following code example illustrates how to set this property.

### C#

```csharp
// Access the row in PdfGrid.
PdfGridRow pdfGridRow = pdfGrid.Rows[0];

// Set the height for a row.
pdfGridRow.Height = 20;
```

### VB.NET

```vbnet
' Access the row in PdfGrid.
Dim pdfGridRow As PdfGridRow = pdfGrid.Rows(0)

' Set the height for a row.
pdfGridRow.Height = 20
```

**Note:** The unit of the Height property is always points. You can set the PDF units only as points. Also, you can use the PdfUnitConverter class to convert the other units to points.

### Row Span

PdfGrid enables you to merge cells within a row. You can specify the number of cells to be merged using the RowSpan property of the PdfGridCell class. The following code example illustrates this.

### C#

```csharp
// Merging row cells.
pdfGridRow.Cells[0].RowSpan = 2;
```

### VB.NET

```vbnet
pdfGridRow.Cells(0).RowSpan = 2
```

## API Reference

### Members

- **Height**
  - **Type:** Property
  - **Description:** Specifies the height of the row.
  - **Parameter:** `float`
  - **Returns:** The height of the row.

- **RowSpan**
  - **Type:** Property
  - **Description:** Specifies the number of rows a cell should span.
  - **Parameter:** `int`
  - **Returns:** The number of rows the cell should span.

## Code Examples

### C#
```csharp
// Example: Setting row height
PdfGridRow pdfGridRow = pdfGrid.Rows[0];
pdfGridRow.Height = 20;

// Example: Merging cells
pdfGridRow.Cells[0].RowSpan = 2;
```

### VB.NET
```vbnet
' Example: Setting row height
Dim pdfGridRow As PdfGridRow = pdfGrid.Rows(0)
pdfGridRow.Height = 20

' Example: Merging cells
pdfGridRow.Cells(0).RowSpan = 2
```

## See also
- [PDF Unit Converter](https://docs.syncfusion.com/windowsforms/PdfUnitConverter)
- [PdfGrid Documentation](https://docs.syncfusion.com/windowsforms/PdfGrid)

<!-- tags: [syncfusion, windowsforms, pdfgrid, pdfunitconverter, version:11.4.0.26] keywords: [pdfgridrow, pdfgridcell, row height, row span, pdfunitconverter, c#, vb.net, code examples] -->
```