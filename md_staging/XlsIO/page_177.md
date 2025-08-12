```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_177.jpeg
document_name: XlsIO
page_number: 177
page_id: XlsIO#page_177
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:22Z
fidelity: lossless
-->

## Overview
- Figure shows the Insert Menu in Excel.
- Examples demonstrate inserting rows and columns in Excel using C# and VB.NET.
- Illustrates inserting multiple rows and columns.

## Content

### Inserting Rows and Columns

#### Figure 58: Insert Menu in Excel
![Insert Menu in Excel](https://i.imgur.com/example/image.png)

The following code example demonstrates how to insert rows and columns in Excel.

#### [C#]

```csharp
// Inserting Rows.
sheet.InsertRow(3);

// Inserting Columns.
sheet.InsertColumn(2);
```

#### [VB.NET]

```vbnet
' Inserting Rows.
sheet.InsertRow(3)

' Inserting Columns.
sheet.InsertColumn(2)
```

#### Inserting Multiple Rows and Columns

XlsIO allows you to insert multiple rows and columns. The following code example illustrates this.

#### [C#]

```csharp
// Inserting multiple columns.
sheet.InsertColumn(colIndex, colCount);
```

## API Reference

- **Methods**
  - `InsertRow(index: int)`
    - **Parameters**
      - `index`: Integer specifying the row index where the new row is to be inserted.
    - **Returns**: None.
  - `InsertColumn(index: int)`
    - **Parameters**
      - `index`: Integer specifying the column index where the new column is to be inserted.
    - **Returns**: None.
  - `InsertColumn(colIndex: int, colCount: int)`
    - **Parameters**
      - `colIndex`: Integer specifying the starting column index.
      - `colCount`: Integer specifying the number of columns to insert.
    - **Returns**: None.

## Code Examples

#### C# Example: Inserting Rows and Columns

```csharp
// Inserting a row at index 3.
sheet.InsertRow(3);

// Inserting a column at index 2.
sheet.InsertColumn(2);
```

#### VB.NET Example: Inserting Rows and Columns

```vbnet
' Inserting a row at index 3.
sheet.InsertRow(3)

' Inserting a column at index 2.
sheet.InsertColumn(2)
```

#### C# Example: Inserting Multiple Columns

```csharp
// Inserting multiple columns starting at colIndex with colCount columns.
sheet.InsertColumn(colIndex, colCount);
```

## Page-level Navigation/TOC

- **Figure 58: Insert Menu in Excel**
- **Inserting Rows and Columns**
  - C# Example
  - VB.NET Example
- **Inserting Multiple Rows and Columns**
  - C# Example

## Cross References

- For more details on Excel operations, refer to the [XlsIO Documentation](https://docs_syncfusion_com/XlsIO).

<!-- tags: [XlsIO, Insert Menu, Rows, Columns, Excel, VB.NET, C#] keywords: [inserting, multiple, operations, examples, rows, columns] -->
```