```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_477.jpeg
document_name: grid
page_number: 477
page_id: grid#page_477
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:04Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Resizing Columns and Rows

#### Overview

- Automatically adjust column widths and row heights to fit the content, ensuring optimal data visualization.

#### Content

```vb.net
' Resize the column widths.
Me.gridControl1.ColWidths.ResizeToFit(GridRangeInfo.Cols(1, 5))

' Resize the row heights.
Me.gridControl1.RowHeights.ResizeToFit(GridRangeInfo.Rows(1, 5))
```

##### Note

The parameter passed to the `ResizeToFit` method is either `GridRangeInfo.Cols` or `GridInfo.Rows` method, which in turn has two parameters:
1. The first parameter corresponds to the starting row/column that is to be resized to fit.
2. The second parameter corresponds to the ending row/column up to which the resize has to be done.

The following image shows the application of resize to fit operation to the first five rows of the grid.

![Resizing grid example](https://i.imgur.com/resize-grid-example.png)

#### Explanation of the Parameters

- The `GridRangeInfo.Cols` and `GridRangeInfo.Rows` methods specify the range of columns or rows to be resized.
- `GridRangeInfo.Cols(1, 5)` indicates resizing from column 1 to column 5.
- Similarly, `GridRangeInfo.Rows(1, 5)` indicates resizing from row 1 to row 5.

#### Visual Demonstration

The grid in the image demonstrates how the columns and rows have been resized to fit the content, ensuring better readability and efficient use of space.

---

### API Reference

**Namespace:** Syncfusion.Windows.Forms.Grid

#### Methods

- **ResizeToFit**: 
  - **Description**: Automatically adjusts the width or height of the specified range of columns or rows to fit the content.
  - **Parameters**:
    - **GridRangeInfo**: Specifies the range of rows or columns to resize (either start and end column/row numbers or a specific range).
  - **Returns**: None
  - **Exceptions**: None explicitly mentioned.

---

### Code Examples

#### VB.NET Example

```vb.net
' Resizing columns to fit their content.
Me.gridControl1.ColWidths.ResizeToFit(GridRangeInfo.Cols(1, 5))

' Resizing rows to fit their content.
Me.gridControl1.RowHeights.ResizeToFit(GridRangeInfo.Rows(1, 5))
```

#### See Also

- [Grid Control Overview](#grid-control-overview)
- [Row and Column Manipulation](#row-and-column-manipulation)

---

<!-- tags: [grid, windows forms, resizing, columns, rows, vb.net, syncfusion, 11.4.0.26] keywords: [resize to fit, gridrangeinfo, colwidths, rowheights, essential grid, windows forms, vb.net, syncfusion] -->
```