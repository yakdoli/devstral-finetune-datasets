```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_921.jpeg
document_name: grid
page_number: 921
page_id: grid#page_921
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the functionality to draw Alpha Blending and Inverted Cells over selected rows in a grid control.
- Includes examples in both C# and VB.NET for configuring the ListBoxSelectionColorOptions.

## Content

### Drawing Alpha Blending over the Selected Row

- **InvertCells**
  Inverts the cells in the selected row. As a result, the back color of the cell is used to draw the text, and the CellTextColor becomes its BackColor.

#### C#
```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.InvertCells;
```

#### VB.NET
```vb
Me.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.InvertCells
```

**Figure 337: Drawing Alpha Blending over the Selected Row**

### Inverting Cells in the Selected Row

- **None**
  Does not change the appearance of the cells. The cell appearance could be specified manually by handling `TableControlPrepareViewStyleInfo` and `TableControlCellDrawn` events.

#### C#
```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.None;
```

#### VB.NET
```vb
Me.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.None
```

**Figure 338: Inverting Cells in the Selected Row**

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid

- **GridListBoxSelectionColorOptions**
  - **InvertCells**: Option to invert the cells in the selected row.
  - **None**: No change in the appearance of the cells, allowing manual specification through events.

## Code Examples

### Example 1: Configuring InvertCells in C#
```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.InvertCells;
```

### Example 2: Configuring None in VB.NET
```vb
Me.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.None
```

<!-- tags: [syncfusion, winforms, grid, gridcontrol, selectioncolor, invertcells, none, coloroptions] keywords: [grid, selection, color, invertcells, none, row, alpha blending, drawing, cell] -->
```