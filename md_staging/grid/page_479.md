```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_479.jpeg
document_name: grid
page_number: 479
page_id: grid#page_479
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:24Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Applying ResizeToFitOptimized to an Application

The following code example illustrates how to use this `ResizeToFitOptimized` method in Grid control.

```csharp
[C#]

// Resize the column width
this.gridControl1.ColWidths.ResizeToFitOptimized(GridRangeInfo.Col(1));

// Resize the row height
this.gridControl1.RowHeights.ResizeToFitOptimized(GridRangeInfo.Rows(1, 8));
```

```vb
[VB.NET]

' Resize the column width
Me.gridControl1.ColWidths.ResizeToFitOptimized(GridRangeInfo.Col(1))

' Resize the row height
Me.gridControl1.RowHeights.ResizeToFitOptimized(GridRangeInfo.Rows(1, 8))
```

The following image shows the application of `ResizeToFitOptimized` to the first column of the grid.

```markdown
### Understanding the Code Example

The `ResizeToFitOptimized` method is used to adjust the size of the grid columns and rows to fit their content optimally. In the provided example:

- **Column Width Adjustment:**
  ```csharp
  this.gridControl1.ColWidths.ResizeToFitOptimized(GridRangeInfo.Col(1));
  ```
  - This line resizes the first column (index 1) to fit its content optimally.

- **Row Height Adjustment:**
  ```csharp
  this.gridControl1.RowHeights.ResizeToFitOptimized(GridRangeInfo.Rows(1, 8));
  ```
  - This line resizes all rows from index 1 to 8 (inclusive) to fit their content optimally.

### Additional Notes

The `GridRangeInfo` is a utility class that specifies the range of cells to be affected by the `ResizeToFitOptimized` method. In the provided example:
- `GridRangeInfo.Col(1)` specifies the single column at index 1.
- `GridRangeInfo.Rows(1, 8)` specifies a range of rows from index 1 to 8.

### Conclusion

The `ResizeToFitOptimized` method simplifies the process of dynamically adjusting the dimensions of grid columns and rows to ensure that the content is displayed clearly and efficiently, enhancing the overall user experience.

### See also:
- [Grid Cell Models: Adjusting Dimensions](#)
- [Syncfusion Grid Controls: Best Practices](#)
```

<!-- tags: [Syncfusion Winforms, Grid Control, ResizeToFitOptimized, GridCellModels, DesignTimeAdjustments] keywords: [grid, resize, fit, optimized, content, dimensions, visual layout, user experience, design tools, automatic adjustment] -->
```