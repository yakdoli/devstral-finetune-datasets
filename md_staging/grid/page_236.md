```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_236.jpeg
document_name: grid
page_number: 236
page_id: grid#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:44Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Demonstrates the implementation of frozen rows and columns using VB.NET.
- Explains how to unfreeze frozen rows and columns through the UI.
- Highlights the Freeze Pane feature in the Essential Grid.

### Content

#### Using VB.NET
This section illustrates the usage of VB.NET to freeze rows and columns in a grid.

```vb
[VB.NET]
Me.gridControl1.Model.Rows.FrozenCount = 4
Me.gridControl1.Model.Cols.FrozenCount = 3
```

**Note:** You can unfreeze the frozen rows/columns by clicking the **Unfreeze Current Row/Col** button on the UI.

![Figure 128: Freeze Pane feature Illustrated](2025-08-09-06-04-44.png)

#### 4.1.4.5.6 MultiLevel Undo and Redo
This section introduces the MultiLevel Undo and Redo feature.

---

## MultiLevel Undo and Redo

### Overview
- Explains the functionality of MultiLevel Undo and Redo in the grid control.
- Describes how the grid can handle multiple undo and redo operations.

---

<!-- tags: [essential-grid, windows-forms, frozen-rows-columns, vb-net, grid-control, multi-level-undo-redo] keywords: [freeze-pane, unfreeze, undo, redo, grid, windows-forms, vb.net] -->
```