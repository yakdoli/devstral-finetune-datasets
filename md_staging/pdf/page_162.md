```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: pdf
page_number: 162
page_id: pdf#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:32Z
fidelity: lossless
-->

## Overview

- Overview of properties to modify Grid cell appearance and structure.
- Explanation of how to set column span, row span, cell size, and alignment.
- Instructions on customizing cell values, style, and string formatting.

## Content

### Properties of Grid Cell

| Property Name     | Description                                   | Type             |
|-------------------|-----------------------------------------------|------------------|
| **ColumnSpan**    | Gets or sets the column span.                | Integer          |
| **Height**        | Gets the height.                             | Float            |
| **ImagePosition** | Gets or sets the image alignment type of the background image. | PdfGridImagePosition |
| **RowSpan**       | Gets or sets the row span.                   | Integer          |
| **StringFormat**  | Gets or sets the string format.              | PdfStringFormat  |
| **Style**         | Gets or sets the cell style.                 | PdfGridCellStyle |
| **Value**         | Gets or sets the value.                      | Object           |
| **Width**         | Gets the width.                              | float            |

### Cell Size

The width and height cannot be modified for a single cell, but for the entire column or row. Please check `PdfGridColumn` and `PdfGridRow` for more details.

### Value

You can specify the value for an individual cell using the `Value` property. Also, you can specify another `PdfGrid` as the cell value to make a nested table.

The following code snippet illustrates this:

```csharp
// Set the value to the specific cell.
parentPdfGrid.Rows[0].Cells[0].Value = "Nested Table";
parentPdfGrid.Rows[0].Cells[1].RowSpan = 2;
parentPdfGrid.Rows[0].Cells[1].ColumnSpan = 2;

PdfGrid childPdfGrid = new PdfGrid();
childPdfGrid.Columns.Add(5);
for (int i = 0; i < 5; i++)
{
    PdfGridRow row = childPdfGrid.Rows.Add();
    for (int j = 0; j < 5; j++)
    {
        // Perform operations for each cell in the nested table
    }
}
```

## API Reference (if applicable)

- **Properties**
  - `ColumnSpan`
  - `Height`
  - `ImagePosition`
  - `RowSpan`
  - `StringFormat`
  - `Style`
  - `Value`
  - `Width`

## Code Examples

### Example: Using Nested Tables in a PdfGrid

```csharp
// Create a parent PdfGrid and initialize rows and columns.
PdfGrid parentPdfGrid = new PdfGrid();
parentPdfGrid.Rows.Add();
parentPdfGrid.Columns.Add(3);

// Set up nested table.
PdfGrid childPdfGrid = new PdfGrid();
childPdfGrid.Columns.Add(5);
for (int i = 0; i < 5; i++)
{
    PdfGridRow row = childPdfGrid.Rows.Add();
    for (int j = 0; j < 5; j++)
    {
        row.Cells[j].Value = $"Cell {i},{j}";
    }
}

// Assign the nested PdfGrid as cell value.
parentPdfGrid.Rows[0].Cells[1].Value = childPdfGrid;
```

## Cross References

- See also: `PdfGridColumn`, `PdfGridRow`
- Refer to documentation on `PdfGridImagePosition`, `PdfStringFormat`, and `PdfGridCellStyle` for more details on customization options.

<!-- tags: [PdfGrid, Syncfusion Winforms, Grid, Table, Cell, Nested Table, ColumnSpan, RowSpan, ImagePosition, StringFormat, Style, Value, Width, Height] keywords: [Grid cell customization, PdfGrid properties, Table structure, Nested tables, Row/column span, Image alignment, String formatting, Cell style, Cell value, Width height limitations] -->
```