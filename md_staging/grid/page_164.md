```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: grid
page_number: 164
page_id: grid#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:05Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of Masked Edit Cells in a grid.
- Explains how to use the MonthCalendar cell type for date selection.

## Content

### 4.1.4.1.10 Month Calendar

The MonthCalendar cell type lets you pick dates. To make use of this cell type in grid, set the CellType property to `MonthCalendar` and `CellValue` property to `DateTime` object.

The following code example illustrates how to set the cell type to MonthCalendar.

#### C#
```csharp
// Set Cell Type.
gridControl1[rowIndex, colIndex].CellType = "MonthCalendar";

// Assign initial value.
gridControl1[rowIndex, colIndex].CellValue = DateTime.Now;
```

#### VB.NET
```vb
' Set Cell Type.
gridControl1(rowIndex, colIndex).CellType = "MonthCalendar"

' Assign initial value.
gridControl1(rowIndex, colIndex).CellValue = DateTime.Now
```

### Captioned Figure
- **Figure 85: Masked Edit Cells**
  ![Masked Edit Cells](https://i.imgur.com/figure85.png)
  
<!-- tags: [grid, masked edit cells, monthcalendar, celltype, datetime, date selection, windows forms, syncfusion] keywords: [masked edit cells, monthcalendar, celltype, datetime object, date selection, winforms, grid control] -->
```