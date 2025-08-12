```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_216.jpeg
document_name: grid
page_number: 216
page_id: grid#page_216
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to use VB.NET to register custom cell types and embed grids within Grid cells.
- Explains the functionality of Link Label Cell used for linking embedded content in cells.

## Content

### Using VB.NET

Register a custom cell type and embed a grid within a cell using VB.NET:

```vb
'Register custom cell type
RegisterCellModel.GridCellType(Me.gridControl1, CustomCellTypes.GridinCell)

Dim grid As GridControl

Me.gridControl1(3, 2).CellType = CustomCellTypes.GridinCell.ToString()
Me.gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(3, 2, 7, 4))

'Create a new embedded grid
grid = New CellCellEmbeddedGrid(Me.gridControl1)

'Configure the embedded grid
grid.BackColor = Color.FromArgb(&H4, &HE7, &HF2)
grid.RowCount = 10
grid.ColCount = 4
grid(1, 1).Text = "this is a 10x4 grid"
grid.ThemesEnabled = True

'Link the embedded grid to the specified cell
Me.gridControl1(3, 2).Control = grid
Me.gridControl1.Controls.Add(grid)
```

#### Figure 113: "GridinCell" Cells

![GridinCell cells](https://i.imgur.com/6baDQdU.png)

#### Description
- The first example shows a 10x4 grid embedded in a cell, with the text "this is a 10x4 grid" prominently displayed.
- The second example demonstrates a 20x20 grid configuration.

#### Link Label Cell

The Link Label Cell cell type holds the link that has been provided in the **Tag** property. This displays ordinary text in the cell which links to the specified location.

### WinForms-specific conventions
- The example showcases how to embed a GridControl within another Grid cell, treating the cell as a container for dynamic content.
- Properties like `CellType`, `CoveredRanges`, and `ThemesEnabled` are key to configuring this functionality.

### API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridControl
- **Methods/Properties**:
  - `RegisterCellModel.GridCellType`: Registers a custom cell type.
  - `CoveredRanges.Add`: Adds a range covered by a custom cell type.
  - `GridRangeInfo.Cells`: Specifies the covered range for the custom cell type.
  - `ThemesEnabled`: Enables/disables the application of themes.
  - `CellEmbeddedGrid`: Class for embedding a GridControl within a cell.

### Code Examples (multi-language supported)
- The provided VB.NET example demonstrates how to embed a grid within a Grid cell. This flexibility can be applied to various Grid Control scenarios to enhance user interaction and data presentation.

<!-- tags: [syncfusion, windows forms, grid control, vb.net, cell embedding] -->
```