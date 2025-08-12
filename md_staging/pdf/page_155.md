```
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: pdf
page_number: 155
page_id: pdf#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:27Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This page explains how to configure cell borders, padding, and spacing in a `PdfGrid`.
- Demonstrates techniques to manage overlaps, pad cell contents, and adjust spacing between cells.
- Provides examples in both C# and VB.NET.

## Content

### Border Overlap

This property determines if the cell border should overlap with neighboring cells or draw inside the cell.

**Note:** This property applies to all cells in the `PdfGrid`. Exercise caution when using overlapping borders, as they may result in poor rendering if not uniform in width and color.

#### Code Examples

```csharp
[C#]
pdfGrid.Style.BorderOverlapStyle = PdfBorderOverlapStyle.Overlap;
```

```vb.net
[VB.NET]
pdfGrid.Style.BorderOverlapStyle = PdfBorderOverlapStyle.Overlap
```

### CellPadding

The distance between text and border inside a cell, known as CellPadding, can be set for all cells in the `PdfGrid`. The `PdfPaddings` class allows configuring padding for individual or all sides.

```csharp
[C#]
// Padding will be applied for all four sides of cells in PdfGrid.
pdfGrid.Style.CellPadding.All = 0.3f;

// Padding will be applied only at the top of all cells in PdfGrid.
pdfGrid.Style.CellPadding.Top = 0.3f;
```

```vb.net
[VB.NET]
' Padding will be applied for all four sides of cells in PdfGrid.
pdfGrid.Style.CellPadding.All = 0.3f

' Padding will be applied only at the top for all cells in PdfGrid.
pdfGrid.Style.CellPadding.Top = 0.3f
```

### CellSpacing

The distance between cells, known as CellSpacing, can be set for all cells in the `PdfGrid` using the `CellSpacing` property.

### Code Examples

This section illustrates how to configure the various cell properties in detail for developers working with `PdfGrid`.

## API Reference

- **PdfBorderOverlapStyle**
  - `Overlap`: Specifies whether the border overlaps neighboring cells.
- **PdfPaddings**
  - All: Padding applied to all four sides.
  - Top: Padding applied to the top side.
- **CellSpacing**: Configures the spacing between cells.

### Code Examples

#### C#
```csharp
pdfGrid.Style.BorderOverlapStyle = PdfBorderOverlapStyle.Overlap;
pdfGrid.Style.CellPadding.All = 0.3f;
pdfGrid.Style.CellPadding.Top = 0.3f;
```

#### VB.NET
```vb.net
pdfGrid.Style.BorderOverlapStyle = PdfBorderOverlapStyle.Overlap
pdfGrid.Style.CellPadding.All = 0.3f
pdfGrid.Style.CellPadding.Top = 0.3f
```

## Cross References

- Refer to the `PdfGrid` class documentation for additional styling and configuration options.

## RAG Annotations
```html
<!-- tags: [product: Syncfusion Winforms, module: Essential PDF, control: PdfGrid, api: PdfBorderOverlapStyle, version: 11.4.0.26] keywords: [cell border, cell padding, cell spacing, overlap style, pdfgrid, PdfPaddings] -->
``` 
```