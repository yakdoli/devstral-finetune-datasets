```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_512.jpeg
document_name: grid
page_number: 512
page_id: grid#page_512
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:12Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the merge cells feature in Essential Grid.
- Explains how to merge cells in a specific column using code.
- Illustrates the effect of merging cells before and after.

## Content

### WinForms-specific conventions
The following screen shots illustrate the merge cells feature in Essential Grid.

#### Example Code
```vb
' Merge cells in column 2.
Me.gridControl1.ColStyles(2).MergeCell = GridMergeCellDirection.RowsInColumn
```

#### Before Merging

![Figure 197: Before Merging](https://i.imgur.com/Fig197.png)

---

### References
- Syncfusion Winforms Documentation
- GridMergeCellDirection Enum
- ColStyles Property

<!-- tags: [Essential Grid, Windows Forms, Merge Cells, GridMergeCellDirection, ColStyles] keywords: [merge cells, grid, windows forms, syncfusion, colstyles, gridmergecelldirection] -->
```