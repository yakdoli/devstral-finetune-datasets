```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_224.jpeg
document_name: grid
page_number: 224
page_id: grid#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:56Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Demonstrates how to create and configure drop-down grid cells in a Windows Forms application using the Essential Grid control.
- Explains the process of registering custom drop-down grid cell models and setting them up in the grid.

### Content

#### [C#]
The following C# code creates and registers drop-down grid cells for a Windows Forms application:

```csharp
// Create and register drop-down grid cells.
DropDownGridCellModel aModel = new DropDownGridCellModel(this.gridControl1.Model);
aModel_embeddedGrid = GridA;
gridControl1.CellModels.Add("GridADropCell", aModel);

// Set the drop-downs in the cell.
this.gridControl1[rowIndex, 1].Text = "Grid A";
this.gridControl1[rowIndex, 1].CellType = "GridADropCell";
```

#### Using VB.NET
The following VB.NET code accomplishes the same task:

```vb
' Create and register drop-down grid cells.
Dim aModel As DropDownGridCellModel = New DropDownGridCellModel(Me.gridControl1.Model)
aModel.EmbeddedGrid = GridA
gridControl1.CellModels.Add("GridADropCell", aModel)

' Set the drop-downs in the cell.
Me.gridControl1(rowIndex, 1).Text = "Grid A"
Me.gridControl1(rowIndex, 1).CellType = "GridADropCell"
```

#### Figure: Drop-Down Grid Cell
![Drop-Down Grid Cell](image.png)

**Figure 119: Drop-Down Grid Cell**

This figure illustrates the drop-down grid cell functionality, showing a drop-down menu in which the selected item is linked to an embedded grid.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** DropDownGridCellModel
  - **Properties**
    - **EmbeddedGrid**: Specifies the embedded grid associated with the drop-down cell.
    - **CellType**: Specifies the type of cell to use for the drop-down.
  - **Methods**
    - **SetDropDownList**: Configures the drop-down list for the cell.
  - **Events**
    - **DropDownClosing**: Triggered when the drop-down list is about to close.
  
## Code Examples

The provided code examples demonstrate how to integrate drop-down grid cells into a Windows Forms application using both C# and VB.NET. These examples include creating a `DropDownGridCellModel`, associating it with an embedded grid, and setting up the cell type and text in the grid.

### Cross References
- See also: [Essential Grid Documentation](https://www.syncfusion.com/documentation/windows-forms) for more details on configuring and customizing grid cells.

<!-- tags: [grid, windows forms, drop-down, Essential Grid, C#, VB.NET] keywords: [drop-down grid cells, embedded grid, custom cell types, grid configuration, Windows Forms application] -->
```