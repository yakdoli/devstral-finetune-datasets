```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_226.jpeg
document_name: grid
page_number: 226
page_id: grid#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:43Z
fidelity: lossless
-->

## Overview
- Demonstrates how to use custom cell types, such as `DropDownForm` and `Integer Text Box`, within the `Essential Grid for Windows Forms`.
- Explains how to register custom cell models and assign them to specific grid cells for enhanced user interaction.

## Content

### Custom Drop-Down Grid Form

```vb
Me.gridControl1(2, 2).CellType = "DropDownForm"

' Register your custom cell type.
Me.gridControl1.CellModels.Add("DropDownUserControl", New DropDownUserCellModel(Me.gridControl1.Model, New DropDownUser()))

' Set the style.CellType for the cells.
Me.gridControl1(6, 2).CellType = "DropDownUserControl"
```

#### Drop-Down Grid Form Example

![Figure 120: Drop-Down Grid Form](https://i.imgur.com/example_image.png)

**Figure 120: Drop-Down Grid Form**

### `4.1.4.15 Integer Text Box`

#### Overview
- The Integer text box is a cell type used to display integer data-type values within grid cells.
- This cell type can be added to grid cells by registering its cell model using the `RegisterCellModel` class.

#### Code Example: Adding Integer Text Box to Grid Cells

##### C#
```csharp
RegisterCellModel.GridCellType(this.gridControl1,
    CustomCellTypes.IntegerTextBox);
this.gridControl1[4, 2].CellType =
    CustomCellTypes.IntegerTextBox.ToString();
```

##### VB
```vb
RegisterCellModel.GridCellType(Me.gridControl1,
    CustomCellTypes.IntegerTextBox)
Me.gridControl1(4, 2).CellType =
    CustomCellTypes.IntegerTextBox.ToString()
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid
- **Class**: GridCellModel
  - **Methods**:
    - `GridCellType` (static method) used to register custom cell types.
- **Class**: RegisterCellModel
  - **Purpose**: Registers custom cell models for the grid.

### Parameters
- `gridControl1`: The grid control where cells are populated.
- `CustomCellTypes.IntegerTextBox`: Reference to the custom integer text box cell type.

## Code Examples

### C# Example
```csharp
RegisterCellModel.GridCellType(this.gridControl1,
    CustomCellTypes.IntegerTextBox);
this.gridControl1[4, 2].CellType =
    CustomCellTypes.IntegerTextBox.ToString();
```

### VB Example
```vb
RegisterCellModel.GridCellType(Me.gridControl1,
    CustomCellTypes.IntegerTextBox)
Me.gridControl1(4, 2).CellType =
    CustomCellTypes.IntegerTextBox.ToString()
```

## Cross References
- **Related Topics**: For more information on customizing grid cells, refer to the documentation on `Custom Cell Models` and `Grid Cell Control`.

<!-- tags: [Syncfusion, WinForms, Grid, CustomCell, IntegerTextBox] keywords: [RegisterCellModel, GridCellType, CustomCellTypes, DropDownForm, DropDownUserControl, gridControl1] -->
```