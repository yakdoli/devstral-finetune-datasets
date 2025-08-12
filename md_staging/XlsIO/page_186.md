```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_186.jpeg
document_name: XlsIO
page_number: 186
page_id: XlsIO#page_186
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:42Z
fidelity: lossless
-->

## Autofit Techniques in XlsIO

### Overview
- XlsIO provides support to autofit contents in a worksheet by adjusting the size of cells, ranges, columns, or rows.
- Demonstrates various autofit techniques supported by XlsIO.

### Autofit Single Row/Column

XlsIO allows you to resize cells in a column or row based on the given row/column index. The following code example illustrates autofitting a single row or column.

#### C# Example

```csharp
sheet.Range["E1"].Text = "This is the Long Text";

// AutoFit applied to a Single Column.
sheet.AutoFitColumn(5);

// AutoFit applied to a Single Row.
sheet.AutoFitRow(1);
```

#### VB.NET Example

```vb.net
sheet.Range("E1").Text = "This is the Long Text"

' AutoFit applied to a Single Column.
sheet.AutoFitColumn(5)

' AutoFit applied to a Single Row.
sheet.AutoFitRow(1)
```

**Note:** These indexes are "one based".

##### Alternative Autofit for Single Row/Column

You can also autofit single row/column as follows.

```csharp
sheet.Rows[0].AutoFitRows();
sheet.Columns[0].AutoFitColumns();
```

### Summary

This section provides a clear explanation of how to use the autofit feature in XlsIO to adjust the dimensions of rows and columns dynamically based on their content, ensuring optimal worksheet display.

<!-- tags: [xlsio, worksheet, autofit, cells, rows, columns] keywords: [AutoFit, C#, VB.NET, XlsIO, cell size, worksheet formatting] -->
```