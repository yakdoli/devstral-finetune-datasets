```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_475.jpeg
document_name: grid
page_number: 475
page_id: grid#page_475
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Figure 184 demonstrates the Grid after setting the styles for Column 2 and Row 3.
- Explains the functionality of controlling the resize behavior of the Grid control.
- Details the use of `ResizeColsBehavior` and `ResizeRowsBehavior` properties.
- Lists various options from the `GridResizeCellsBehavior` enumeration for resizing behavior control.

---

## Content

### 4.1.4.14.7 Controlling the Resize Behavior

Essential Grid supports the resizing behavior of columns and rows in the Grid control. This is achieved by using the `ResizeColsBehavior` and `ResizeRowsBehavior` properties.

The `GridResizeCellsBehavior` enumeration provides the following options to control the resizing behavior:

- **AllowDragOutside**: Allows the user to drag the cell boundary outside the grid client area and resize the specific row or column.

#### Note:
The Grid client area is the area where the cells along with row and column headers are visible to the client. Dragging outside the client area means dragging beyond the boundary of the grid.

#### Options:
- **InsideGrid**: Allows the user to resize rows or columns from anywhere inside the grid by dragging the divider between any two row or column headers.
- **None**: Turns off the mouse control over the resizing rows and columns.
- **OutlineBounds**: Highlights the original cell boundaries of resizing row or column.
- **OutlineHeaders**: Highlights the header boundaries when the user resizes the associated row or column.
- **ResizeAll**: Resizes all rows or columns automatically when the user resizes one row or column with the mouse. All rows and columns are resized to the same size as the current row/column being resized.
- **ResizeSingle**: Resizes the row or column being resized by the user using the mouse.

---

<!-- tags: [product, Essential Grid, Windows Forms, Grid control, resize behavior, Syncfusion Winforms] keywords: [GridResizeCellsBehavior, AllowDragOutside, InsideGrid, None, OutlineBounds, OutlineHeaders, ResizeAll, ResizeSingle] -->
```