```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_159.jpeg
document_name: pdf
page_number: 159
page_id: pdf#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:45Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Demonstrates how to merge row cells and set row styles for PdfGrid rows.
- Explains the precedence order when style properties are applied to both `PdfGridCell` and `PdfGridRow`.

## Content

### Merging row cells

```csharp
// Merging row cells.
pdfGridRow.Cells(0).RowSpan = 2;
```

### Style

The `PdfGridRowStyle` class, accessed through the `Style` property of the `PdfGridRow` class, is used to specify the row style for the `PdfGrid` rows.

#### Precedence of Style Properties

**Note:** If the style properties are applied to both `PdfGridCell` and `PdfGridRow`, `PdfGridCell` takes over the precedence. Following is an example for the exact order of precedence:

- `PdfBrush backgroundBrush = Cell.BackgroundBrush ?? Row.Style.BackgroundBrush ?? Row.Grid.Style.BackgroundBrush`

The following code example illustrates how to specify the row style for the `PdfGrid` rows:

---

#### C#

```csharp
// Create an instance of PdfGridRowStyle
PdfGridRowStyle pdfGridRowStyle = new PdfGridRowStyle();
pdfGridRowStyle.BackgroundBrush = PdfBrushes.LightYellow;
pdfGridRowStyle.Font = new PdfStandardFont(PdfFontFamily.Courier, 10);
pdfGridRowStyle.TextBrush = PdfBrushes.Blue;
pdfGridRowStyle.TextPen = PdfPens.Pink;

// Set style for the PdfGridRow.
pdfGrid.Rows[0].Style = pdfGridRowStyle;
```

---

#### VB.NET

```vb
' Create an instance of PdfGridRowStyle
Dim pdfGridRowStyle As New PdfGridRowStyle()
pdfGridRowStyle.BackgroundBrush = PdfBrushes.LightYellow
pdfGridRowStyle.Font = New PdfStandardFont(PdfFontFamily.Courier, 10)
pdfGridRowStyle.TextBrush = PdfBrushes.Blue
pdfGridRowStyle.TextPen = PdfPens.Pink

' Set style for the PdfGridRow.
pdfGrid.Rows(0).Style = pdfGridRowStyle
```

You may also apply `PdfGridCellStyle` to a `PdfGridRow` using the `ApplyStyle` property. The following code snippet illustrates this:

## API Reference

### Properties

- **PdfGridRow.Rows**  
  Accesses the style of a specific row.

## Code Examples

### C#

```csharp
// Example of setting row style using ApplyStyle

```

### VB.NET

```vb
' Example of setting row style using ApplyStyle

```

## See also

- [PdfGridRowStyle documentation](#)
- [PdfGridRow.Rows reference](#)

<!-- tags: [syncfusion, winforms, pdf, grid, row styles, merging cells] keywords: [pdfgridrow, pdfgridcell, rowspan, style precedence, pdfgridrowstyle, applystyle, cellbackgroundbrush, textbrush, textpen] -->
```