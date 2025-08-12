```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_187.jpeg
document_name: XlsIO
page_number: 187
page_id: XlsIO#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:22Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to auto-fit rows and columns in a spreadsheet.
- Explains the use of `AutoFitRows` and `AutoFitColumns` methods for adjusting row and column dimensions based on content.

## Content

### AutoFit Multiple Rows/Columns
It is also possible to auto-fit multiple rows/columns based on the range specified as follows.

```vb
[VB.NET]
sheet.Rows(0).AutoFitRows()
sheet.Columns(0).AutoFitColumns()
```

#### Note: Here column and row indexes are "zero based".

#### AutoFit Multiple Rows/Columns

It is also possible to auto-fit multiple rows/columns based on the range specified as follows.

```csharp
[C#]
// Entering text inside the Cells.
sheet.Range["A1:D1"].Text = "This is the Long Text";
sheet.Range["E1"].Text = "This is the Long Text";
sheet.Range["A2:A5"].Text = "This is the Long Text using Autofit Columns and Rows";

// AutoFit Applied to a Range.
sheet.Range["A1:D1"].AutofitColumns();
sheet.Range["A2:A5"].AutofitRows();

// Autofits all the columns used in the worksheet.
sheet.UsedRange.AutofitColumns();
```

```vb
[VB.NET]
' Entering text inside the Cells.
sheet.Range("A1:D1").Text = "This is the Long Text"
sheet.Range("E1").Text = "This is the Long Text"
sheet.Range("A2:A5").Text = "This is the Long Text using Autofit Columns and Rows"

' AutoFit Applied to a Range .
sheet.Range("A1:D1").AutofitColumns()
sheet.Range("A2:A5").AutofitRows()

' Autofits all the columns used in the worksheet.
sheet.UsedRange.AutofitColumns()
```

### AutoFit within a Range of Cells

## API Reference

### `AutofitRows`

- **Namespace:** `Syncfusion.XlsIO`
- **Class:** `Worksheet`
- **Method:** `Void AutofitRows()`

Adjusts the height of all the rows in the worksheet based on the content.

### `AutofitColumns`

- **Namespace:** `Syncfusion.XlsIO`
- **Class:** `Worksheet`
- **Method:** `Void AutofitColumns()`

Adjusts the width of all the columns in the worksheet based on the content.

### `AutofitRows`

- **Namespace:** `Syncfusion.XlsIO`
- **Class:** `Range`
- **Method:** `Void AutofitRows()`

Adjusts the height of the specified rows in the worksheet based on the content.

### `AutofitColumns`

- **Namespace:** `Syncfusion.XlsIO`
- **Class:** `Range`
- **Method:** `Void AutofitColumns()`

Adjusts the width of the specified columns in the worksheet based on the content.

## Code Examples

### Example: AutoFitting Rows and Columns

```csharp
[C#]
// AutoFit Applied to a Range.
sheet.Range["A1:D1"].AutofitColumns();
sheet.Range["A2:A5"].AutofitRows();
```

```vb
[VB.NET]
' AutoFit Applied to a Range .
sheet.Range("A1:D1").AutofitColumns()
sheet.Range("A2:A5").AutofitRows()
```

### Example: AutoFitting All Columns in the Worksheet

```csharp
[C#]
// Autofits all the columns used in the worksheet.
sheet.UsedRange.AutofitColumns();
```

```vb
[VB.NET]
' Autofits all the columns used in the worksheet.
sheet.UsedRange.AutofitColumns()
```

## See also
- [Adjust Row Heights](#adjust-row-heights)
- [Adjust Column Widths](#adjust-column-widths)

<!-- tags: XlsIO, autofit, rows, columns, worksheet, range, Syncfusion, Winforms keywords: autofitrows, autofitcolumns, adjustrowheights, adjustcolumnwidths, usedrange, xlsx -->
```