```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_156.jpeg
document_name: pdf
page_number: 156
page_id: pdf#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:09Z
fidelity: lossless
-->

# Essential PDF

```csharp
pdfGrid.Style.CellSpacing = 0.5f;
```

```vb.net
pdfGrid.Style.CellSpacing = 0.5f
```

## 4.1.2.3.2.3.1 Header

### Overview
- A **Header** is a set of rows that can be optionally repeated on each page and has its own style.
- You can add headers in the following ways:
  - **Directly from column captions.**
  - **By using the `Add` method of the `PdfGridHeaderCollection` class.**

### Key Notes
- **When you bind a data source to `PdfGrid`, column captions will be automatically added to the header collection.**
- **The header can be removed at any time using the `Clear` method of `PdfGridHeaderCollection`.**

### Adding Headers Using the Add Method

The following code example illustrates how to add headers to `PdfGrid` by using the `Add` method.

#### C#
```csharp
// Add a new header to PdfGrid.
pdfGrid.Headers.Add(1);

// Get the first header row.
PdfGridCellCollection collection = pdfGrid.Headers[0].Cells;

// Set the header names.
collection[0].Value = "Header1";
collection[1].Value = "Header2";
collection[2].Value = "Header3";
collection[3].Value = "Header4";
```

#### VB.NET
```vb.net
' Add a new header to PdfGrid.
pdfGrid.Headers.Add(1)

' Get the first header row.
Dim collection As PdfGridCellCollection = pdfGrid.Headers(0).Cells
```

## API Reference

### Properties
- `PdfGrid.Headers`: A collection of headers in the grid.
- `PdfGridHeaderCollection`: A collection that manages the headers for `PdfGrid`.

### Methods
- `Add(int rowNumber)`: Adds a new header row to the grid.
- `Clear()`: Removes all headers from the `PdfGridHeaderCollection`.

### Classes
- `PdfGridCellCollection`: Represents a collection of cells in a header row.

## Code Examples

The code examples demonstrate how to programmatically add headers to a `PdfGrid` instance.

### C#
```csharp
// Example: Adding a header with custom values
pdfGrid.Headers.Add(1);
var headerRow = pdfGrid.Headers[0].Cells;
headerRow[0].Value = "Product Name";
headerRow[1].Value = "Quantity";
headerRow[2].Value = "Price";
headerRow[3].Value = "Total";
```

### VB.NET
```vb.net
' Example: Adding a header with custom values
pdfGrid.Headers.Add(1)
Dim headerRow As PdfGridCellCollection = pdfGrid.Headers(0).Cells
headerRow(0).Value = "Product Name"
headerRow(1).Value = "Quantity"
headerRow(2).Value = "Price"
headerRow(3).Value = "Total"
```

### Notes
- Ensure that the `PdfGrid` object is properly initialized and bound to data before adding headers.
- Adjust the number of columns in the header row to match the number of columns in the grid.

## Cross References
- See also: [PdfGrid Documentation](#)
- See also: [PdfGridHeaderCollection Methods](#)

<!-- tags: [syncfusion, winforms, pdfgrid, header, cellspacing, pdfgridheadercollection, addmethod] keywords: [pdfgrid, headers, cell spacing, add, clear, column captions, grid, api, vb.net, c#] -->
```