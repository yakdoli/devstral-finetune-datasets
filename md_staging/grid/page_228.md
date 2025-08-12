```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_228.jpeg
document_name: grid
page_number: 228
page_id: grid#page_228
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:13Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of custom cell types in a grid control.
- Focuses on registering and using `CustomCellTypes.DoubleTextBox` and `CustomCellTypes.PercentTextBox`.
- Includes code examples for setting up and utilizing these custom cells.

## Content

### CustomCellTypes.DoubleTextBox

#### Example Code

```vb
[VB]
RegisterCellModel.GridCellType(Me.gridControl1, CustomCellTypes.DoubleTextBox)
Me.gridControl1(4, 2).CellType = CustomCellTypes.DoubleTextBox.ToString()
```

#### Visual Representation

![Figure 122: Double Text Box](image.png)
*Figure 122: Double Text Box*

### 4.1.4.4.17 Percent Text Box

Percent text box is used to display percentage values in the grid cell. This cell type can be added to the grid cells by registering its cell model using the `RegisterCellModel` class.

The following code example illustrates how to add the percent text box to grid cells using the `RegisterCellModel` class.

#### Example Code in C#

```csharp
[C#]
```

## Code Examples

- The previous section includes a VB example for setting up the `DoubleTextBox`.
- The current section provides a placeholder for the C# code example to set up the `PercentTextBox`, which is not yet populated.

## Page-level Navigation/TOC (if applicable)

- This page is part of the Essential Grid for Windows Forms documentation, focusing on custom cell types.

## Cross References

- Refer to the main documentation for more details on `RegisterCellModel` and grid customization.

## RAG Annotations
<!-- tags: [grid, customcelltypes, textbox, doobbuetextbox, percenttextbox, syncfusionwindowsforms] keywords: [custom cell types, grid control, cell models, double textbox, percent textbox, registration] -->
```