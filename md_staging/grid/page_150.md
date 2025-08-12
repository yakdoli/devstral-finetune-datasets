```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: grid
page_number: 150
page_id: grid#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:57:28Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- A detailed explanation of checkbox cells supporting triState/disabled states in the grid control.
- Instructions on setting up a Color Edit control in the grid using CellType properties.

## Content

### Checkbox Cells - supports triState/disabled states
The image below illustrates checkbox cells that support triState and disabled states, as well as standard enabled states.

![Figure 76: Check Box Cells](https://example.com/fig76-checkbox-cells.png)

#### 4.1.4.1.2 Color Edit

The Color Edit cell type allows you to pick colors and set a color object as the `CellValue`. To do this, you have to set the `CellType` property to `ColorEdit`.

The following code example illustrates how to set the cell type to `ColorEdit`:

```csharp
// Set up a Color Edit control.
gridControl1[rowIndex, colIndex].CellType = "ColorEdit";
gridControl1[rowIndex, colIndex].CellValue = Color.Aqua;
```

```vb.net
' Set up a Color Edit control.
gridControl1(rowIndex, colIndex).CellType = "ColorEdit"
gridControl1(rowIndex, colIndex).CellValue = Color.Aqua
```

## Page-level Navigation/TOC (if applicable)
- [unclear]

## Cross References
See also: [unclear]

## RAG Annotations
<!-- tags: [Essential Grid, WinForms, Checkbox Cells, Color Edit, CellType, CellValue] keywords: [ColorEdit, triState, disabled states, grid control, checkbox cells, color object, CellType property] -->
```