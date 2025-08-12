```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_476.jpeg
document_name: grid
page_number: 476
page_id: grid#page_476
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Demonstrates how to control the mouse behavior during column and row resizing using events.
- Explains the usage of the `ResizeToFit` method in the Grid control.

## Content

### 1. Using C#

```csharp
this.gridControl1.ResizeColsBehavior = GridResizeCellsBehavior.InsideGrid;
this.gridControl1.ResizeRowsBehavior = GridResizeCellsBehavior.InsideGrid;
```

### 2. Using VB.NET

```vbnet
Me.gridControl1.ResizeColsBehavior = GridResizeCellsBehavior.InsideGrid
Me.gridControl1.ResizeRowsBehavior = GridResizeCellsBehavior.InsideGrid
```

### 4.1.4.14.8 Resize To Fit

#### Overview
Essential Grid supports the ability to resize columns and rows based on the content of cells. The `ResizeToFit` method is utilized for this purpose.

#### Code Examples

##### 1. Using C#

```csharp
// Resize the column widths.
this.gridControl1.ColWidths.ResizeToFit(GridRangeInfo.Cols(1, 5));

// Resize the row heights.
this.gridControl1.RowHeights.ResizeToFit(GridRangeInfo.Rows(1, 5));
```

##### 2. Using VB.NET
No VB.NET example provided in this section.

## API Reference

### Methods
- **ResizeToFit**: Adjusts the dimensions of grid elements based on their content.

### Properties
- **ResizeColsBehavior**
- **ResizeRowsBehavior**

## Code Examples (continued)

### 1. C# Example for ResizeToFail (Note: Likely intended as ResizeToFit)

```csharp
// Resize the column widths.
this.gridControl1.ColWidths.ResizeToFit(GridRangeInfo.Cols(1, 5));

// Resize the row heights.
this.gridControl1.RowHeights.ResizeToFit(GridRangeInfo.Rows(1, 5));
```

### 2. VB.NET Example
No VB.NET example provided for this section.

## Cross References

- Refer to the section on handling events for column and row resizing.
- More details can be found in the Grid control documentation.

<!-- tags: [grid, windows forms, syncfusion, resize, behavior, columns, rows, C#, VB.NET] keywords: [resize behavior, resize to fit, inside grid, columns, rows, essential grid, syncfusion, windows forms] -->
```