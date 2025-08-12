```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_464.jpeg
document_name: grid
page_number: 464
page_id: grid#page_464
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
rec.X = (e.Bounds.Left + e.Bounds.Right) / 2
If e.Style.CellValue.ToString() = "1" Then
    e.Graphics.FillEllipse(Brushes.Gray, rect)
    GridImageCellRenderer.DrawImage(e.Graphics, Me.imageList1, 1, rect, False)
Else
    e.Graphics.FillEllipse(Brushes.LightGray, rect)
    GridImageCellRenderer.DrawImage(e.Graphics, Me.imageList1, 0, rect, False)
End If
End If
End Sub
```

The above code identifies the cells of the 6th column except the cell corresponding to the column header, using their index values, and customizes their appearance.

## 4.1.4.13.6 Formatting Drop-down List

Essential Grid has built-in support for displaying a Grid List control as a drop-down inside a grid cell. We can embed grid list controls into the grid cells and customize them.

The following screen shot shows a grid cell with Grid List control as its drop-down.

![Figure 177: Grid List control embedded in a Grid Cell](https://example.com/image-url-for-figure-177)

**Figure 177: Grid List control embedded in a Grid Cell**

Let us see how to add a Grid List control to a grid cell and bind some data.

## Page-level Navigation/TOC
- [unclear: unable to extract local TOC from image text]

## Cross References
- See also: [Essential Grid, GridListControl, GridListBinding, Grid, Cell Formatting, Drop-down List, Grid Control]

<!-- tags: [Essential Grid, GridListControl, GridListBinding, Grid, Cell Formatting, Drop-down List, Grid Control] keywords: [Essential Grid, grid list control, grid cell, cell formatting, drop-down list, GridListControl, GridImageCellRenderer, imageList1, GridListBinding, cellvalue, lightgray, fillellipse, drop-down, drop-down list, Grid] -->
```