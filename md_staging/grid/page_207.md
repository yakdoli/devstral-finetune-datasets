```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_207.jpeg
document_name: grid
page_number: 207
page_id: grid#page_207
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Rightend
- Undo
- Up
- Image

### Content
You can also add custom buttons that you have created to the grid cells. This enables you to add custom buttons like split buttons to the grid.

The following code examples illustrate how to set the cell type to `ButtonEdit`.

### Using C#
```csharp
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.ButtonEdit);
ButtonEditStyleProperties sp;
this.gridControl1[rowIndex, colIndex].CellType = CustomCellTypes.ButtonEdit.ToString();
sp = new ButtonEditStyleProperties(this.gridControl1[rowIndex, colIndex]);
sp.ButtonEditInfo.ButtonEditType = ButtonType.Browse;
sp.ButtonEditInfo.Width = 50;
```

### Using VB.NET
```vb
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.ButtonEdit)
Private sp As ButtonEditStyleProperties
Me.gridControl1(rowIndex += 1, colIndex).CellType = "ButtonEdit";
Me.gridControl1(rowIndex, colIndex).CellType = CustomCellTypes.ButtonEdit.ToString()
sp = New ButtonEditStyleProperties(Me.gridControl1(rowIndex, colIndex))
sp.ButtonEditInfo.ButtonEditType = ButtonType.Browse
```

### API Reference
- **Namespace**: `Syncfusion.Windows.Forms.Grid`
- **Class**: `GridCellModel`
  - **Method**: `GridCellType(Control control, CustomCellTypes cellType)`
  - **Method**: `GetCellRangeStyle(Cell cell)`
- **Class**: `ButtonEditStyleProperties`
  - **Property**: `ButtonEditInfo`
    - **Property**: `ButtonEditType`
    - **Property**: `Width`

## Code Examples (Multi-language)

### C#
```csharp
using Syncfusion.Windows.Forms.Grid;

// Example of setting a custom button in a cell
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.ButtonEdit);
ButtonEditStyleProperties sp;
sp = new ButtonEditStyleProperties(gridControl1[rowIndex, colIndex]);
sp.ButtonEditInfo.ButtonEditType = ButtonType.Browse;
sp.ButtonEditInfo.Width = 50;
```

### VB.NET
```vb
Imports Syncfusion.Windows.Forms.Grid

' Example of setting a custom button in a cell
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.ButtonEdit)
Dim sp As ButtonEditStyleProperties = New ButtonEditStyleProperties(gridControl1(rowIndex, colIndex))
sp.ButtonEditInfo.ButtonEditType = ButtonType.Browse
sp.ButtonEditInfo.Width = 50
```

### Cross References
See also:
- [Grid onDataBound](grid#page_207#on-databound)
- [Custom Cell Types](custom-cell-types#page_207)

<!-- tags: [Essential Grid, Windows Forms, Custom Buttons, ButtonEdit, Cell Styling, WinForms, Syncfusion] keywords: [GridCellType, ButtonEditStyleProperties, ButtonType, CustomCellTypes, CellType, ButtonEditInfo, GridCellModel] -->
```
