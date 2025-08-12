```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_466.jpeg
document_name: grid
page_number: 466
page_id: grid#page_466
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Handles the **CurrentCellShowedDropDown** event when the drop-down of a specified grid cell is displayed by clicking the downward arrow at the end of the cell.
- Provides examples in **C#** and **VB.NET** for customizing the appearance of the drop-down list control.

## Content

### Handling the CurrentCellShowedDropDown Event

#### Note
The **CurrentCellShowedDropDown** event is triggered when the drop-down of the specified grid cell is made visible by clicking the downward arrow at the end of the cell.

The following code illustrates this event:

```csharp
// [C#]

private void gridControl1_CurrentCellShowedDropDown(object sender, EventArgs e)
{
    // Retrieve the DropDownList Cell Renderer.
    GridDropDownGridListControlCellRenderer listRenderer =
        (GridDropDownGridListControlCellRenderer)this.gridControl1.CellRenderers["GridListControl"];

    // Apply styles to Grid List control in the drop-down.
    listRenderer.ListControlPart.Grid.TableStyle.Font.Size = 17.8f;
    listRenderer.ListControlPart.BorderStyle = BorderStyle.FixedSingle;
    listRenderer.ListControlPart.Grid.BackColor = Color.FromArgb(250, 240, 230);
    listRenderer.ListControlPart.Grid.DefaultGridBorderStyle = GridBorderStyle.Solid;
    listRenderer.ListControlPart.Grid.TableStyle.TextColor = Color.MidnightBlue;
    listRenderer.ListControlPart.Grid.Properties.GridLineColor = Color.FromArgb(208, 215, 229);
    listRenderer.ListControlPart.FillLastColumn = false;
}
```

```vb
' [VB.NET]

Private Sub gridControl1_CurrentCellShowedDropDown(ByVal sender As Object, ByVal e As EventArgs)

    ' Retrieve the DropDownList Cell Renderer.
    Dim listRenderer As GridDropDownGridListControlCellRenderer = CType(Me.gridControl1.CellRenderers("GridListControl"), GridDropDownGridListControlCellRenderer)

    ' Apply styles to Grid List control in the drop-down.
    listRenderer.ListControlPart.Grid.TableStyle.Font.Size = 17.8F
    listRenderer.ListControlPart.BorderStyle = BorderStyle.FixedSingle
    listRenderer.ListControlPart.Grid.BackColor = Color.FromArgb(250, 240, 230)
    listRenderer.ListControlPart.Grid.DefaultGridBorderStyle = GridBorderStyle.Solid
End Sub
```

### Customizing the Drop-Down Grid List Control

The code examples demonstrate how to customize the appearance of the grid list control in the drop-down, including:

- Font size and color.
- Border style and background color.
- Text color and grid line color.
- Grid border style.

## API Reference

### Members

#### GridDropDownGridListControlCellRenderer
- **Properties**
  - `ListControlPart`: Accesses the grid list control part.
  - `Grid`: The grid control within the drop-down.
  - `TableStyle`: Styles the table appearance.
  - `Font`: Controls the font size and style.
  - `BorderColor`: Sets the border color.
  - `Properties`: Contains additional grid properties like `GridLineColor`.
  - `FillLastColumn`: Determines if the last column should be filled.

---

<!-- tags: [grid, drop-down, cell-renderer, windows-forms, syncfusion] keywords: [CurrentCellShowedDropDown, GridDropDownGridListControlCellRenderer, Grid, TableStyle, Font, BorderStyle] -->
``` 
