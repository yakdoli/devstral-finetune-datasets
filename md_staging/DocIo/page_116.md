```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: DocIo
page_number: 116
page_id: DocIo#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:21Z
fidelity: lossless
-->

# Essential DocIO

## Content

### Table Properties Dialog Box

#### Figure 38: Table Properties Dialog Box

The Table Properties Dialog Box allows you to adjust the size and options for table rows, columns, and cells. Here is a breakdown of the options available under the **Row** tab:

- **Size:**
  - **Rows 1-83:** Specifies the height of the rows.
  - **Specify height:** Allows you to set the exact height of the rows. The height can be set to "At least" a certain value.
- **Options:**
  - **Allow row to break across pages:** Enables rows to break across pages if they exceed the page boundaries.
  - **Repeat as header row at the top of each page:** Repeats the selected row as a header at the top of each page.

### Adding Cells

You can use the `AddCell` and `AddCell(bool isCopyFormat)` functions to add new cells to the table row, where the `isCopyFormat` parameter defines whether to apply the formatting of the upper cell to the added cell.

#### Key Points:
- `AddCell` function without parameters is the same as `AddCell(true)`.

## Public Constructors

| Name                                       | Description                                                |
|--------------------------------------------|-------------------------------------------------------------|
| `WTableRow.WTableRow(IWordDocument)`      | Initializes a new instance of the `WTableRow` class.       |

## Public Properties

[unclear]

## API Reference

- **Namespace:** `Syncfusion.DocIO`
- **Class:** `WTableRow`
- **Methods:**
  - `AddCell(bool isCopyFormat)` - Adds a new cell to the table row and optionally applies the formatting of the upper cell.
  - `AddCell()` - Equivalent to `AddCell(true)`.

## Code Examples

```csharp
using Syncfusion.DocIO;

// Example of adding cells to a table row
WTableRow newRow = new WTableRow(document);
newRow.AddCell(true); // Adds a new cell and copies the formatting of the upper cell
newRow.AddCell(false); // Adds a new cell without copying the formatting
```

## Page-level Navigation/TOC

- Table Properties Dialog Box
- Adding Cells
- Public Constructors
- API Reference
- Code Examples

## Cross References

See also:
- Table Properties in Document Processing
- Working with Tables in DocIO

## RAG Annotations

<!-- tags: [DocIO, Table Properties, Adding Cells, WTableRow, Public Constructors, Public Properties, WinForms] keywords: [Table, Rows, Columns, Cells, AddCell, WTableRow, Syncfusion, DocIO] -->
```