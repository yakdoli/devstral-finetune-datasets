```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: pdf
page_number: 164
page_id: pdf#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:49Z
fidelity: lossless
-->

# Essential PDF

## Customizing Cell Content

### Table: Cell Style Properties

| Property       | Description                                         | Type              |
|----------------|-----------------------------------------------------|-------------------|
| Font           | Gets or sets the font.                             | PdfFont           |
| StringFormat   | Gets or sets the string format.                   | PdfStringFormat   |
| TextBrush      | Gets or sets the text brush.                      | PdfBrush          |
| TextPen        | Gets or sets the text pen.                        | PdfPen            |

### Overview

- The following code example demonstrates how to customize the content of a cell in a grid.

### C#

```csharp
// Specify the style for the PdfPCell.
PdfGridCellStyle pdfGridCellStyle = new PdfGridCellStyle();
pdfGridCellStyle.BackgroundImage = new PdfBitmap("pdf_button.png");
pdfGridCellStyle.TextPen = PdfPens.Red;
pdfGridCellStyle.Borders.All = PdfPens.Red;

PdfGridCell pdfGridCell = pdfGrid.Rows[0].Cells[0];

// Apply style
pdfGridCell.Style = pdfGridCellStyle;

// Set image position for the background image in the style.
pdfGridCell.ImageLayout = PdfGridImagePosition.Fit;
```

### VB.NET

```vb
' Specify the style for the PdfPCell.
Dim pdfGridCellStyle As New PdfGridCellStyle()
pdfGridCellStyle.BackgroundImage = New PdfBitmap("pdf_button.png")
pdfGridCellStyle.TextPen = PdfPens.Red
pdfGridCellStyle.Borders.All = PdfPens.Red

Dim pdfGridCell As PdfPCell = pdfGrid.Rows(0).Cells(0)

' Apply style
pdfGridCell.Style = pdfGridCellStyle

' Set image position for the background image in the style.
pdfGridCell.ImageLayout = PdfGridImagePosition.Fit
```

### Explanation

- The example illustrates setting the style properties of a cell in a grid.
- The background image, text pen, and borders are customized using a `PdfGridCellStyle` object.
- The `ImageLayout` property is set to `Fit` to adjust the image size within the cell.

## References

- Syncfusion Winforms Documentation: [Syncfusion Winforms](https://www.syncfusion.com/products/windowsforms)
- Version: 11.4.0.26

<!-- tags: [syncfusion, winforms, grid, cellstyle, pdfformat] keywords: [pdfgridcell, backgroundimage, textpen, borders, imagelayout, fit] -->
```