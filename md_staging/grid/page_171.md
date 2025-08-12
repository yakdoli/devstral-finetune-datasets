```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_171.jpeg
document_name: grid
page_number: 171
page_id: grid#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:56Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to create Rich Text Cells in a Windows Forms Grid.
- Explains how to configure font and color attributes for individual characters within a rich text cell.
- Introduces the use of Slider cells in grid cells.
- Describes setting up a single Slider control shared among multiple grid cells using `SliderStyleProperties`.

## Content

### Rich Text Cells

To set up a Rich Text Cell in a Windows Forms Grid, follow this example:

```csharp
' Set up a Rich Text Cell.
gridControl1(rowIndex, 1).CellType = "RichText"
gridControl1(rowIndex, 1).Text = rtf
gridControl1.RowHeights(rowIndex) = 50
gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(rowIndex, 1, rowIndex, 5))
```

This configuration allows for text formatting such as font and color changes for individual characters. Here is an illustrative example:

```plaintext
{\f1\froman\fcharset2 Symbol;} + 
{\f2\fswiss\fprq2 System;} + 
{\f3\fswiss\fprq2 Arial;} + 
{\f4\froman Bookman Old Style;} + 
"} + 
{\colortbl\red0\green0\blue0;\red255\green0\blue0;} + 
\deflang1033\cfpat1\pard\plain\f3\fs16\cf0 * Change the " + 
\plain\f4\fs24\cf0\b\i\ul font \plain\f3\fs16\cf0 or " + 
\plain\f4\fs24\cf1\b\ul color\plain\f3\fs16\cf0   " + 
"for individual characters.\par " + 
"}
```

**Figure: Rich Text Cells**

The following grid cell configuration demonstrates setting font and color attributes:
- Column headers: A, B, C, D, E
- Row 3: Content: "* Change the **font** or **color** for individual characters."

### Slider

#### 4.1.4.1.15 Slider

You can use slider cells in grid cells. You can also share a single Slider control among multiple cells. To set the slider properties for a cell, make use of the `SliderStyleProperties` object.

The following code example illustrates how to set the cell type to Slider.

```csharp
// Set up a Slider control.
GridStyleInfo style = gridControl[row, 3];
SliderStyleProperties sp = new SliderStyleProperties(style);
style.CellType = "Slider";
```

## API Reference

### SliderStyleProperties
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: `SliderStyleProperties`
- **Constructor**: `SliderStyleProperties(GridStyleInfo style)`

### Properties
- **CellType**: Sets or gets the cell type for the Grid cell.

## Code Examples

### Example 1: Creating a Rich Text Cell
```csharp
gridControl1(rowIndex, 1).CellType = "RichText"
gridControl1(rowIndex, 1).Text = rtf
gridControl1.RowHeights(rowIndex) = 50
gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(rowIndex, 1, rowIndex, 5))
```

### Example 2: Configuring a Slider Cell
```csharp
GridStyleInfo style = gridControl[row, 3];
SliderStyleProperties sp = new SliderStyleProperties(style);
style.CellType = "Slider";
```

<!-- tags: [Syncfusion, WindowsForms, Grid, RichTextCells, SliderCells, SliderStyleProperties, CellType] keywords: [rich text, individual characters, grid cell, slider control, font color, formatting] -->
```