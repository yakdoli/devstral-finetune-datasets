```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_178.jpeg
document_name: XlsIO
page_number: 178
page_id: XlsIO#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:08Z
fidelity: lossless
-->

## Overview

- Demonstrates how to insert multiple rows and columns in an Excel sheet using the XlsIO library.
- Explains how to preserve the previous or next row/column formats during insertion operations.
- Provides examples in both C# and VB.NET for inserting rows and columns with formatting options.

## Content

### Insert Rows and Columns

#### Inserting Multiple Rows and Columns

You can insert multiple rows and columns in an Excel sheet using the following methods:

- **C#**
  ```csharp
  ' Inserting multiple rows.
  sheet.InsertRow(rowIndex, rowCount);

  ' Inserting multiple columns.
  sheet.InsertColumn(colIndex, colCount);
  ```

- **VB.NET**
  ```vb
  ' Inserting multiple columns.
  sheet.InsertColumn(colIndex, colCount)

  ' Inserting multiple rows.
  sheet.InsertRow(rowIndex, rowCount)
  ```

**Preserving Row/Column Formats**

You can also preserve the previous or next row/column formats by using XlsIO. The following code example illustrates this:

- **C#**
  ```csharp
  sheet.InsertRow(rowIndex, count, ExcelInsertOptions.FormatAsBefore);
  ```

- **VB.NET**
  ```vb
  sheet.InsertRow(rowIndex, count, ExcelInsertOptions.FormatAsBefore)
  ```

**Note:** Here, the row and column index of the `Insert` methods are "one based".

### ExcelInsertOptions Enumerator

The following table lists the options provided by the `ExcelInsertOptions` enumerator.

| **Member name**   | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| FormatAsBefore    | Indicates that after the insert operation, the inserted rows/columns must be formatted as the row above or column left. |
| FormatAsAfter     | Indicates that after the insert operation, the inserted rows/columns must be formatted as the row below or column right. |
| FormatDefault     | Indicates that after the insert operation, the inserted rows/columns must have the default format.                          |

### 4.1.3.2 Delete
<!-- anchor: XlsIO#page_178#delete -->

## API Reference (if applicable)

### Namespace: Syncfusion.XlsIO

#### Methods
- InsertRow(rowIndex, rowCount, [ExcelInsertOptions])
- InsertColumn(colIndex, colCount)

#### Enum: ExcelInsertOptions
- FormatAsBefore
- FormatAsAfter
- FormatDefault

## Code Examples

### Insert Rows with Format Preservation

#### C# Example
```csharp
sheet.InsertRow(rowIndex, count, ExcelInsertOptions.FormatAsBefore);
```

#### VB.NET Example
```vb
sheet.InsertRow(rowIndex, count, ExcelInsertOptions.FormatAsBefore)
```

## Page-level Navigation/TOC

- [Insert Rows and Columns](#insert-rows-and-columns)
- [Preserving Row/Column Formats](#preserving-rowcolumn-formats)
- [ExcelInsertOptions Enumerator](#excelinsertoptions-enumerator)
- [Delete](#delete)

## Cross References

See also:

- **[4.1.3.1 Insert Operations](#insert-operations)**

<!-- tags: [XlsIO, Syncfusion, Insert, Delete, Rows, Columns, Formats, C#, VB.NET] keywords: [rowIndex, rowCount, colIndex, colCount, ExcelInsertOptions, FormatAsBefore, FormatAsAfter, FormatDefault, C#, VB.NET, Excel, XlsIO, InsertRow, InsertColumn] -->
```