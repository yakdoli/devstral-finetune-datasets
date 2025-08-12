```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_129.jpeg
document_name: pdf
page_number: 129
page_id: pdf#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:07Z
fidelity: lossless
-->

## Overview
- PdfLightTable Creation process and usage.
- Understanding and implementing the events raised during layout and data requests.
- Assigning data and drawing the table using the `Draw` method with different overloads.

## Content

### Table Events

| Event            | Description                                              |
|------------------|----------------------------------------------------------|
| EndRowLayout     | This event is raised on finishing row layout.          |
| QueryColumnCount | This event is raised when the column number is requested. |
| QueryNextRow     | This event is raised when the next row data is requested. |
| QueryRowCount    | This event is raised when the row number is requested. |

### PdfLightTable Creation

**Note:** You should add the `Syncfusion.Pdf.Tables` namespace to work with `PdfLightTable`.

You may create a `PdfLightTable` simply by specifying a new operator with the proper constructor. After assigning the data source, it can be drawn using one of the overloads of `Draw` method as follows:

#### Code Examples

```csharp
// Creating a PdfLightTable.
PdfLightTable pdfLightTable = new PdfLightTable();

// Assigning data source.
pdfLightTable.DataSource = dataSource;

// Drawing PdfLightTable.
pdfLightTable.Draw(graphics);
```

```vb
' Creating a PdfLightTable.
Dim pdfLightTable As New PdfLightTable()

' Assigning data source.
pdfLightTable.DataSource = dataSource

' Drawing PdfLightTable.
pdfLightTable.Draw(graphics)
```

Different types of data can be set to `PdfLightTable`. Also, the `Draw` method facilitates overloads that would help you to layout the `PdfLightTable` as required. The topics that discuss them are:

- **Data**
- **Layout**

## Cross References
- See also: Data, Layout

<!-- tags: [syncfusion, winforms, pdf, pdflighttable, tablecreation, events, drawmethod] keywords: [PdfLightTable, Draw, DataSource, EndRowLayout, QueryColumnCount, QueryNextRow, QueryRowCount, data, layout] -->
```