```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_146.jpeg
document_name: pdf
page_number: 146
page_id: pdf#page_146
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:32Z
fidelity: lossless
-->

## Essential PDF

### End Sub

#### `EndCellLayout`

This event is raised when cell layout finishes. The arguments of this event are as follows:

- **RowIndex** (read-only): Index of the current row
- **CellIndex** (read-only): Index of the current cell within the row
- **Value** (read-only): Text value of the cell
- **Bounds** (read-only): Bounds of the cell
- **Graphics**: Graphics on which the cell should be drawn

### `PdfGrid`

`PdfGrid` class, based on cell model, helps to draw tables of complex structures. Data from DataTables, arrays or other entity classes can be given as input. In Silverlight platform, `IEnumerable` data objects can be set as data source. Formatting can be done at all levels and it provides direct API for this. It also supports row, column spanning and drawing of nested tables. This section explains how a table can be drawn using PdfGrid. It includes the following sections:

---

### Properties, Methods, and Events

#### Properties

| Name                     | Description                                    | Data Type                  |
|--------------------------|-----------------------------------------------|-----------------------------|
| AllowRowBreakAcrossPages | Gets or sets whether to split or move rows that overflow a page. | Boolean                      |
| Columns                  | Gets the columns.                              | PdfGridColumnCollection     |
| DataMember               | Gets or sets the data member.                  | String                      |
| DataSource               | Gets or sets the data source.                  | Object                      |
| Headers                  | Gets the headers.                              | PdfGridHeaderCollection     |
| RepeatHeader             | Gets or sets a value indicating whether to repeat header. | Boolean                      |
| Rows                     | Gets the rows.                                 | PdfGridRowCollection       |
| Style                    | Gets or sets the style.                        | PdfGridStyle                |

---

## Code Examples

### Example: Using `PdfGrid`

```csharp
// Example usage of PdfGrid

// Create a new PdfGrid instance
PdfGrid grid = new PdfGrid();

// Set the data source
grid.DataSource = dataSource;

// Configure the grid
grid.AlllowRowBreakAcrossPages = true;

// Add custom styling
PdfGridStyle style = new PdfGridStyle();
style.BackgroundColor = new PdfColor(0, 0, 255);
grid.Style = style;

// Draw the grid on the PDF document
pdfDocument.Pages[0].Graphics.DrawPdfGrid(grid, new Point(0, 0));
```

---

### Summary

This section provides detailed information about the `PdfGrid` class and its various properties and methods. It explains how to use `PdfGrid` to draw tables with complex structures in a PDF document. The `EndCellLayout` event is also discussed, detailing its arguments and usage.

---

<!-- tags: [PdfGrid, EndCellLayout, PdfGridProperties, WinForms, Syncfusion, 11.4.0.26] keywords: [cell model, complex structures, row spanning, column spanning, nested tables, PDF, drawing, filter, data source, Silverlight, PDFGrid class] -->
```