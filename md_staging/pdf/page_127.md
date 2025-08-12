```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: pdf
page_number: 127
page_id: pdf#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:09Z
fidelity: lossless
-->

# Using PdfLightTable with Essential PDF

## Overview
- Explains how to create and manipulate table elements using `PdfLightTable` in Essential PDF.
- Supports `IEnumerable` and `TableDirect` data sources in Silverlight.
- Covers properties, methods, and events for `PdfLightTable`.

## Content

### Properties, Methods and Events

#### Properties
The following table describes the properties of `PdfLightTable`:

| Name                        | Description                                                                 | Data Type                            |
|-----------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| `AllowRowBreakAcrossPages` | Gets or sets a value indicating whether the row break should be made or not. | `Boolean`                            |
| `Columns`                  | Gets the columns                                                            | `PdfColumnCollection`                |
| `DataMember`               | Gets or sets the data member                                                | `String`                             |
| `DataSource`               | Gets or sets the data source                                                | `Object`                             |
| `DataSourceType`           | Gets or sets the data source type of the `PdfLightTable`                     | `PdfLightTableDataSourceType`        |
| `IgnoreSorting`            | Gets or sets a value indicating whether `PdfLightTable` should ignore sorting in the `DataTable` | `Boolean`                            |
| `Rows`                     | Gets the rows                                                               | `PdfRowCollection`                   |
| `Style`                    | Gets or sets the properties                                                 | `PdfLightTableStyle`                 |

#### Methods
The following table describes the methods of `PdfLightTable`:

| Method   | Description                       | Parameters                                      | Return Type                     |
|----------|-----------------------------------|--------------------------------------------------|----------------------------------|
| `Draw`   | Draws `PdfLightTable`            | Overloads: <br> `(PdfGraphics graphics)` <br> `(PdfPage page, PointF location)` <br> `(PdfPage page, RectangleF bounds)` <br> `(PdfGraphics graphics, PointF location)` <br> `(PdfGraphics graphics, RectangleF bounds)` | `Void` <br> `PdfLightTableLayoutResult` <br> `PdfLightTableLayoutResult` <br> `Void` <br> `Void`           |

## API Reference

### `PdfLightTable`
#### Properties
- **`AllowRowBreakAcrossPages`** (`Boolean`): Gets or sets whether to allow row breaks across pages.
- **`Columns`** (`PdfColumnCollection`): Gets the collection of columns.
- **`DataMember`** (`String`): Gets or sets the data member.
- **`DataSource`** (`Object`): Gets or sets the data source.
- **`DataSourceType`** (`PdfLightTableDataSourceType`): Gets or sets the data source type.
- **`IgnoreSorting`** (`Boolean`): Gets or sets whether the `DataTable` sorting should be ignored.
- **`Rows`** (`PdfRowCollection`): Gets the collection of rows.
- **`Style`** (`PdfLightTableStyle`): Gets or sets the style properties of the table.

#### Methods
- **`Draw`**:
  - **Overload 1**: `(PdfGraphics graphics)` → `Void`
  - **Overload 2**: `(PdfPage page, PointF location)` → `PdfLightTableLayoutResult`
  - **Overload 3**: `(PdfPage page, RectangleF bounds)` → `PdfLightTableLayoutResult`
  - **Overload 4**: `(PdfGraphics graphics, PointF location)` → `Void`
  - **Overload 5**: `(PdfGraphics graphics, RectangleF bounds)` → `Void`

## Code Examples
### Example 1: Drawing a Table
```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.Interactive;
using Syncfusion.Pdf.Graphics;

// Create a new PDF document
PdfDocument document = new PdfDocument();
PdfPage page = document.Pages.Add();

// Create a new PdfLightTable
PdfLightTable table = new PdfLightTable();

// Set data sources
table.DataSource = dt;
table.DataMember = "SomeDataMember";

// Draw the table
RectangleF bounds = new RectangleF(0, 0, 500, 500);
PdfGraphics graphics = page.Graphics;
table.Draw(graphics, bounds);
```

## Cross References
- Refer to the Essential PDF documentation for more detailed information on drawing and styling tables.

<!-- tags: [syncfusion, winforms, essentialpdf, pdflighttable, drawing, properties, methods, events, data sources] keywords: [table, row break, columns, data member, data source, ignore sorting, rows, style, draw method, graphics, page, bounds, overloads] -->
```