```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_176.jpeg
document_name: XlsIO
page_number: 176
page_id: XlsIO#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:46Z
fidelity: lossless
-->

## Cells

### Overview
- Spreadsheets are composed of cells, and Excel provides functionalities to manipulate these cells to tailor the sheet to user requirements.
- This section details methods for changing cell dimensions, inserting and deleting rows/columns, and controlling spreadsheet visibility.

### Content

#### 4.1.3 Cells
##### Overview
Spreadsheets are made up of cells. Excel allows to manipulate these cells to customize the sheet for user needs.

This section explains the following cell manipulations:
- Cell Size
- Insert
- Delete
- Visibility

##### 4.1.3.1 Insert
XlsIO has support for dynamically inserting rows and columns into a new/existing worksheet. Inserting rows/columns will allow the other rows/columns to move down/right by one step, and accommodate the new rows/columns.

MS Excel allows to insert rows/columns through the Insert menu option.

```csharp
sheet.Replace("DataTable", table, True)
```

### API Reference (if applicable)

### Code Examples (multi-language supported)

### RAG Annotations
<!-- tags: [xlsio, cell-manipulation, insert, delete, visibility, cell-size, spreadhseets] keywords: [cells, Excel, user needs, customization, cell size, rows, columns, visibility, XlsIO] -->
```