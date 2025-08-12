```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_136.jpeg
document_name: pdf
page_number: 136
page_id: pdf#page_136
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:57Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Introduction to PdfLightTableLayoutFormat for managing table drawing parameters.
- Explanation of PdfLayoutType and its role in defining pagination.
- Overview of PdfLayoutBreakType for controlling how elements are broken across pages.
- Discussion on retrieving table layout details using PdfLightTableLayoutResult.

## Content

### PdfLightTableLayoutFormat

The `PdfLightTableLayoutFormat` class is utilized to define the format for drawing a `PdfLightTable`. It allows specifying the range of columns to be drawn.

#### Example: Drawing a Table from Specific Columns

`[VB.NET]`
```vb
Dim format As PdfLightTableLayoutFormat = New PdfLightTableLayoutFormat()
format.StartColumnIndex = 0
format.EndColumnIndex = 3

' Drawing the PdfLightTable from the first to the fourth column
pdfLightTable.Draw(page, PointF.Empty, format)
```

### Specifying Pagination Type

The `PdfLayoutType` class is used to specify the type of pagination for the `PdfLightTable`. The `Paginate` layout type draws the table on the (immediate) following pages if the table exceeds the height of a single page. The `OnePage` layout type ensures the table is drawn entirely on one page.

#### Example: Drawing a Table with Pagination

`[C#]`
```csharp
PdfLightTableLayoutFormat format = new PdfLightTableLayoutFormat();
format.Layout = PdfLayoutType.Paginate;
format.Break = PdfLayoutBreakType.FitElement;
format.StartColumnIndex = 1;
format.EndColumnIndex = 2;

// Drawing the PdfLightTable with the layout format
pdfLightTable.Draw(page, PointF.Empty, format);
```

`[VB.NET]`
```vb
Dim format As PdfLightTableLayoutFormat = New PdfLightTableLayoutFormat()
format.Layout = PdfLayoutType.Paginate
format.Break = PdfLayoutBreakType.FitElement
format.StartColumnIndex = 1
format.EndColumnIndex = 2

' Drawing the PdfLightTable with the layout format
pdfLightTable.Draw(page, PointF.Empty, format)
```

### PdfLightTableLayoutResult

The `PdfLightTableLayoutResult` class is used to retrieve the layout settings of the drawn `PdfLightTable`. It provides information such as the bounds and the last page where the table was drawn, which is useful for placing additional content, such as text or elements, below the table to indicate the number of pages.

## API Reference

### PdfLightTableLayoutFormat

#### Properties
- **StartColumnIndex**: Specifies the index of the first column to be drawn.
- **EndColumnIndex**: Specifies the index of the last column to be drawn.
- **Layout**: Defines the type of pagination (e.g., `Paginate`, `OnePage`).
- **Break**: Determines how the table is broken across pages (e.g., `FitElement`).

### PdfLayoutType
- **Paginate**: Allows the table to span across multiple pages.
- **OnePage**: Ensures the table fits on a single page.

### PdfLayoutBreakType
- **FitElement**: Ensures the entire table element is kept intact and not split across pages.

## Code Examples

The examples demonstrate how to use the `PdfLightTableLayoutFormat` class to manage the drawing and pagination of tables in a PDF document.

---

<!-- tags: [Syncfusion, Winforms, PdfLightTable, TableLayout, Pagination, LayoutResult] keywords: [PdfLightTable, PdfLayoutType, PdfLayoutBreakType, TableDrawing, Pagination, LayoutSettings, PdfLightTableLayoutFormat, PdfLightTableLayoutResult] -->
```