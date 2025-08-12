```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_472.jpeg
document_name: grid
page_number: 472
page_id: grid#page_472
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:52Z
fidelity: lossless
-->

## Moving Rows and Columns

The methods `GridControl.Rows.MoveRange` and `GridControl.Cols.MoveRange` are used to move rows and columns in a grid. The `MoveRange` method takes three parameters that are used to determine the start position, number of items to move, and the target position.

### Code Examples

#### C#

```csharp
// Starting at row 7, move 2 rows to row 4.
this.gridControl1.Rows.MoveRange(7, 2, 4);
```

#### VB.NET

```vbnet
' Starting at row 7, move 2 rows to row 4.
Me.GridControl1.Rows.MoveRange(7, 2, 4)
```

### Figure: Grid After Moving Rows 7 and 8 to Row 4

![Grid After Moving Rows 7 and 8 to Row 4](image.png)

## Setting Column Widths and Row Heights

The `GridControl.ColWidths` and `GridControl.RowHeights` collections will allow you to programmatically set the width of a column and / or the height of a row.

<!-- tags: [syncfusion, grid, essential grid, moving rows, moving columns, setting column widths, setting row heights, gridcontrol, rows, cols, moveRange, windows forms, c#, vb.net] -->
```