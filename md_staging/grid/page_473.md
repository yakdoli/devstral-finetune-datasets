```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_473.jpeg
document_name: grid
page_number: 473
page_id: grid#page_473
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:45Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Instructions for explicitly setting column widths in GridDataBoundGrid while ensuring that `AllowResizeToFit` is disabled.
- Demonstrates how to set column and row sizes programmatically using `ColWidths` and `RowHeights`.

### Content

#### Note: Before using `GridDataBoundGrid.Model.ColWidths`
Before you can use `GridDataBoundGrid.Model.ColWidths` to explicitly set column widths in a Grid Data Bound Grid, you must first set `GridDataBoundGrid.AllowResizeToFit` to `false`. Otherwise, the grid will try to size columns based on the width of the header text.

```csharp
// Set the width of column 3.
this.gridControl1.ColWidths[3] = 40;

// Set the height of row 4.
this.gridControl1.RowHeights[4] = 40;
```

```vbnet
' Set the width of column 3.
Me.GridControl1.ColWidths(3) = 40

' Set the height of row 4.
Me.GridControl1.RowHeights(4) = 40
```

![Figure: Grid After Sizing Column 3 and Row 4](https://example.com/image.png)
*Figure 183: Grid After Sizing Column 3 and Row 4*

### 4.1.4.14.6 Setting Column Styles and Row Styles

### API Reference

#### Properties
- **ColWidths**: Array to set individual column widths in the grid.
- **RowHeights**: Array to set individual row heights in the grid.
- **AllowResizeToFit**: Boolean property to enable or disable automatic resizing of columns based on header text.

#### Methods
- **SetColWidth**: Method to programmatically set the width of a specific column.
- **SetRowHeight**: Method to programmatically set the height of a specific row.

### Code Examples

#### C#
```csharp
// Example of setting column and row sizes
this.gridControl1.ColWidths[3] = 80; // Set column 3 width to 80
this.gridControl1.RowHeights[4] = 30; // Set row 4 height to 30
```

#### VB.NET
```vbnet
' Example of setting column and row sizes
Me.GridControl1.ColWidths(3) = 80 ' Set column 3 width to 80
Me.GridControl1.RowHeights(4) = 30 ' Set row 4 height to 30
```

### See also
- GridDataBoundGrid properties and methods.
- Example of dynamic grid configurations.

<!-- tags: [syncfusion, grid, windows forms, column widths, row heights, column styles, row styles, data bound grid, essential grid] keywords: [column resizing, row resizing, grid configuration, allowresize, allowresizetofit, colwidths, rowheights] -->
```