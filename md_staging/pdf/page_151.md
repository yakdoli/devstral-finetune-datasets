```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_151.jpeg
document_name: pdf
page_number: 151
page_id: pdf#page_151
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:10Z
fidelity: lossless
--> 

## Overview
- This page provides details on how to create and layout a `PdfGrid` in a PDF document using `Syncfusion` WinForms.
- Explains adding columns, headers, and rows to a `PdfGrid`.
- Details the layout options and two events associated with `PdfGrid`.

## Content

### `PdfGrid` Usage Example

```csharp
' Add three columns.
pdfGrid.Columns.Add(3)

' Add header.
pdfGrid.Headers.Add(1)
Dim pdfGridHeader As PdfGridRow = pdfGrid.Headers(0)
pdfGridHeader.Cells(0).Value = "Employee ID"
pdfGridHeader.Cells(1).Value = "Employee Name"
pdfGridHeader.Cells(2).Value = "Salary"

' Add rows.
Dim pdfGridRow As PdfGridRow = pdfGrid.Rows.Add()
pdfGridRow.Cells(0).Value = "E01"
pdfGridRow.Cells(1).Value = "Clay"
pdfGridRow.Cells(2).Value = "$10,000"

' Draw the PdfGrid.
pdfGrid.Draw(pdfPage, PointF.Empty)
```

#### Layout
This section discusses `PdfGrid` layout options and the two events associated with `PdfGrid`.

### `PdfGridLayoutFormat`

Layouting `PdfGrid` can be done using the `PdfGridLayoutFormat` class. Overloads accepting pages can accept standard formats as other layouting elements. However, they treat the `PdfLayoutBreakType.FitElement` value of `Format.Break` property as one, for a single row and not for the entire `PdfGrid`.

#### Properties

| Name                | Description                                      | Data Type           |
|---------------------|--------------------------------------------------|---------------------|
| `Break`            | Gets or sets the break type                      | `PdfLayoutBreakType`|
| `Layout`           | Gets or sets the layout type                      | `PdfLayoutType`     |
| `PaginateBounds`   | Gets or sets the `PdfGrid` bounds for the following page | `RectangleF`       |

## API Reference
- **Name**: `PdfGridLayoutFormat`
- **Description**: Setlayout properties for handling the layout of a PDF grid.
- **Properties**:
  - `Break`: Gets or sets the break type.
  - `Layout`: Gets or sets the layout type.
  - `PaginateBounds`: Gets or sets the bounds for pagination of the grid.

### Code Examples

In addition to the example above for creating and displaying a `PdfGrid`, the `PdfGridLayoutFormat` class can be utilized as shown:

```csharp
PdfGridLayoutFormat format = new PdfGridLayoutFormat();
format.Break = PdfLayoutBreakType.FitElement;
pdfGrid.Layout = format;
```

This sets up the layout for a single row.

## RAG Annotations
<!-- tags: [pdfgrid, pdf, layout, syncfusion, winforms, version: 11.4.0.26] keywords: [PdfGrid, headers, rows, drawing, layout options, events, layoutformat, conditionalbreaks] -->
```