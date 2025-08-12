```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_511.jpeg
document_name: grid
page_number: 511
page_id: grid#page_511
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:27Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Merge Options

- **MergeRowsInColumn**:
  - Enables merging of neighboring cells among rows in the same column.
- **MergeColumnsInRow**:
  - Enables merging of neighboring cells among columns in the same row.
- **SkipHiddenCells**:
  - Skips hidden rows and columns while merging the cells. This means that the hidden rows or columns in the grid are not considered during the merge process.

### GridMergeCellDirection Enumeration

2. The `GridMergeCellDirection` enumeration specifies the merge behavior for an individual cell when merging cells feature has been enabled. Here is the list of options offered:

- **None**:
  - Merging cells is disabled.
- **ColumnsInRow**:
  - Merges with neighboring columns in the same row.
- **RowsInColumn**:
  - Merges with neighboring rows in the same column.

The following code examples illustrate how to set the `MergeCellsMode` and `MergeCell` properties.

#### a. Using C#

```csharp
[C#]

this.gridControl1.Model.Options.MergeCellsMode = 
    GridMergeCellsMode.OnDemandCalculation | 
    GridMergeCellsMode.MergeRowsInColumn;

// Merge cells in column 2.
this.gridControl1 ColStyles[2] .MergeCell = 
    GridMergeCellDirection.RowsInColumn;
```

#### b. Using VB.NET

```vb
[VB.NET]

Me.gridControl1.Model.Options.MergeCellsMode = 
    GridMergeCellsMode.OnDemandCalculation Or 
    GridMergeCellsMode.MergeRowsInColumn
```

## API Reference

### Summary

Properties and methods related to `GridMergeCellsMode` and `GridMergeCellDirection` allow customization of cell merging behavior in the grid control.

<!-- tags: [Syncfusion Winforms, GridMergeCellsMode, GridMergeCellDirection] keywords: [grid, winforms, cell merging, hidden cells, row, column] -->
```