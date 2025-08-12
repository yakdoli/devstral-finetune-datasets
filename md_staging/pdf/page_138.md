```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_138.jpeg
document_name: pdf
page_number: 138
page_id: pdf#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:04Z
fidelity: lossless
-->

# Essential PDF

## Overview

- The border for the entire `PdfLightTable` can be set using the `BorderPen` property.
- Border styles applied to individual cells might override the `BorderPen` value.
- The `PdfPen` can be used to draw borders with any color.

## Content

### Setting the Border for the Entire Table

The border for the entire `PdfLightTable` can be set using the `BorderPen` property. Also, border styles applied to individual cells might override this value. You can specify the `PdfPen` to be used to draw border with any color.

#### Code Examples

[C#]

```csharp
pdfLightTable.Style.BorderPen = PdfPens.Khaki;
```

[VB.NET]

```vb.net
pdfLightTable.Style.BorderPen = PdfPens.Khaki
```

### BorderOverlapStyle

This property determines whether the cell border overlaps with neighboring cells or if it should be drawn inside the cell.

**Note:** This property applies for all cells in the `PdfLightTable`. You need to be careful when using overlapping borders, because they may produce bad results if they are not of the same width and color.

#### Code Examples

[C#]

```csharp
pdfLightTable.Style.BorderOverlapStyle = PdfBorderOverlapStyle.Overlap;
```

[VB.NET]

```vb.net
pdfLightTable.Style.BorderOverlapStyle = PdfBorderOverlapStyle.Overlap
```

### Padding and Spacing

You can also specify the cell spacing (distance between cells) and cell padding (distance between cell text and border) for all cells.

#### Code Examples

[C#]

```csharp
pdfLightTable.Style.CellPadding = 4;
pdfLightTable.Style.CellSpacing = 10;
```

[VB.NET]

```vb.net
pdfLightTable.Style.CellPadding = 4
pdfLightTable.Style.CellSpacing = 10
```

## Page-level Navigation/TOC

- **Border for the Entire Table**
- **BorderOverlapStyle**
- **Padding and Spacing**

## Cross References

See also:

- [PdfLightTable API Documentation]
- [PdfPen API Documentation]
- [PdfBorderOverlapStyle API Documentation]

<!-- tags: [PdfLightTable, BorderPen, PdfPen, BorderOverlapStyle, CellPadding, CellSpacing] keywords: [Syncfusion, Winforms, PDF, Table, Border, Padding, Spacing] -->
```