```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_215.jpeg
document_name: grid
page_number: 215
page_id: grid#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This page explains the use of `GridInCell` in the Grid control.
- Demonstrates how to set the cell type to `GridInCell` using C# code.

## Content

### 4.1.4.4.7 GridInCell

The GridInCell cell type provides a covered range of cells to embed the grid, which is added as a control to the cells. The registered cell model will initialize the range by calculating the size of the grid control to be embedded, and add some style such as borders and scroll bar to have the control within the range.

The following code examples illustrate how to set the cell type to `GridInCell`.

#### Using C#

```csharp
[C#]

RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.GridinCell);
gridControl1.BackColor = Color.FromArgb(0xda, 0xe5, 0xf5);
GridControl grid;

this.gridControl1[3, 2].CellType = CustomCellTypes.GridinCell.ToString();
this.gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(3, 2, 7, 4));
grid = new CellEmbeddedGrid(this.gridControl1);
grid.BackColor = Color.FromArgb(0xb4, 0xe7, 0xf2);
grid.RowCount = 10;
grid.ColCount = 4;
grid[1, 1].Text = "this is a 10x4 grid";
grid.ThemesEnabled = true;
this.gridControl1[3, 2].Control = grid;
this.gridControl1.Controls.Add(grid);
```

### Figure: Enhanced Numeric Up Down Cells

![Figure 112: Enhanced Numeric Up Down Cells](./images/Enhanced_Numeric_Up_Down_Cells.png)

## API Reference (if applicable)
- No specific API reference is mentioned in this section.

## Code Examples (multi-language supported)
- Example code for setting `GridInCell` in C# is provided.

## Page-level Navigation/TOC (if applicable)
- Local navigation within the section on `GridInCell`.

## Cross References
- Refer to other sections or pages for additional details on Grid controls.

<!-- tags: [product, module, control, api, version?] keywords: [Grid, GridInCell, cell model, embedded grid, cell type, numeric up down, C#] -->
```