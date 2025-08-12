```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_480.jpeg
document_name: grid
page_number: 480
page_id: grid#page_480
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Introduction to `ResizeToFitOptimized` and `ResizeToFit` behavior in `AutoSize`.
- Detailed explanation of how columns and rows resize based on their content.

## Content

### Figure 186: Applying ResizeToFitOptimized to first column

#### Description of Figure
The figure demonstrates the resizing behavior of the first column under two different methods:
- **Row Heights - ResizeToFitOptimized**
- **Row Heights - ResizeToFit**
- **Colwidths - ResizeToFitOptimized**
- **Colwidths - ResizeToFit**

#### 4.1.4.14.10 ResizeToFit Behavior in AutoSize

**Objective:** To explain how the `ResizeToFit()` method and `AutoSize` property work together to adjust column and row sizes based on the content of cells.

**Key Points:**
1. **ResizeToFit Behavior:**
   - Essential Grid supports resizing columns and rows based on the content of cells.
   - This is achieved using the `ResizeToFit()` method.

2. **AutoSize Functionality:**
   - **AutoHeight Adjustment:** When `WrapText` is set to `true`, `AutoSize` enables the cell height to automatically increase if the edited text does not fit within the cell.
   - **AutoWidth Adjustment:** If `WrapText` is set to `false`, `AutoSize` affects the column width but does not automatically adjust rows or columns after text input as `ResizeToFit()` does.

3. **Content-Based Resizing:**
   - `AutoSize` supports resizing rows and columns based on cell content during data binding to the grid.
   - Users can enter content in the grid, and then apply the `AutoSize` property to resize altered rows and columns.

#### Implementation Example

```csharp
this.gridGroupingControl.Appearance.AnyCell.AutoSize = true;
```

- This line of code sets the `AutoSize` property to `true`, ensuring that rows and columns adjust their size dynamically based on the content.

### Note
- The above implementation is specific to the `gridGroupingControl` control and should be used in conjunction with the `Appearance` property to achieve content-based resizing.

---

### Footer
- **Copyright Notice:** © 2013 Syncfusion. All rights reserved.
- **Page Number:** 480

<!-- tags: [Essential Grid, Windows Forms, AutoSize, ResizeToFit, ResizeToFitOptimized, AutoHeight, AutoWidth, data binding, Syncfusion Winforms, version 11.4.0.26] keywords: [ResizeToFit behavior, AutoSize functionality, content-based resizing, gridGroupingControl, Appearance property, Content-Based Resizing, text wrapping, cell adjustment] -->
```