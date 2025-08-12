```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_229.jpeg
document_name: grid
page_number: 229
page_id: grid#page_229
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Implementing custom cell types in a grid.
- Registering a custom cell type for a specific grid.
- Setting the `CellType` property of individual cells.

## Content

### Registering a Custom Cell Type
#### Overview
To make a custom cell type available across the grid, you need to register it using `GridCellModel`. This allows the custom cell type to be used in any cell within the grid.

#### C#
```csharp
RegisterCellModel.GridCellType(this.gridControl1, CustomCellTypes.PercentTextBox);
this.gridControl1[5, 2].CellType = CustomCellTypes.PercentTextBox.ToString();
```

#### VB
```vb
RegisterCellModel.GridCellType(Me.gridControl1, CustomCellTypes.PercentTextBox)
Me.gridControl1(4, 2).CellType = CustomCellTypes.PercentTextBox.ToString()
```

### Setting the CellType for a Specific Cell
The `CellType` property of a cell can be set directly by referencing the cell's coordinates.

#### C#
```csharp
this.gridControl1[5, 2].CellType = CustomCellTypes.PercentTextBox.ToString();
```

#### VB
```vb
Me.gridControl1(4, 2).CellType = CustomCellTypes.PercentTextBox.ToString()
```

### Visual Representation

![Figure 123: Percent Text Box](figures/percent_text_box.png)

**Figure 123: Percent Text Box**

This figure illustrates the grid with cells formatted as percentage text boxes. The cells display values like `54.00 %`, `84.00 %`, among others.

## Cross References
- For more information on custom cell types, refer to the section on [Custom Cells](#custom-cells).

## RAG Annotations
<!-- tags: [product, essential grid, cell types, winforms, custom cell types, syncfusion] keywords: [essential grid, custom cell types, gridcelltype, percenttextbox, celltype, grid, cell, custom cell, registration, grid control] -->
```