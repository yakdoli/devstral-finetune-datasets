```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_714.jpeg
document_name: grid
page_number: 714
page_id: grid#page_714
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:48Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
e.Style.Enabled = false;
}
// Setting color to the drop area.
else if (e.Style.Text.StartsWith("Drag a"))
{
    e.Style.Text = "Drag and Drop Parent Table Column headers";
    e.Style.BackColor = Color.White;
}
// Setting color to the dropped columns.
else if (e.Style.Text.StartsWith("Par"))
{
    e.Style.BackColor = Color.Tomato;
    e.Style.Themed = false;
}
// Setting color to the remaining part.
else
{
    e.Style.BackColor = Color.YellowGreen;
}
}
```

```csharp
private void ChildTable_PrepareViewStyleInfo(object sender, GridPrepareViewStyleInfoEventArgs e)
{
    // Setting color to the text displaying the table name.
    if (e.ColIndex == 2 && e.RowIndex == 2)
    {
        e.Style.Text = "ChildTable ";
        e.Style.Font.Bold = true;
        e.Style.BackColor = Color.YellowGreen;
        e.Style.TextColor = Color.Yellow;
        e.Style.CellType = "Static";
        e.Style.HorizontalAlignment = GridHorizontalAlignment.Left;
        e.Style.Enabled = false;
    }
    // Setting color to the drop area.
    else if (e.Style.Text.StartsWith("Drag a"))
    {
        e.Style.Text = "Drag and Drop Parent Table Column headers";
        e.Style.BackColor = Color.Orange;
        e.Style.TextColor = Color.White;
    }
    // Setting color to the dropped columns.
    else if (e.Style.Text.StartsWith("Child"))
    {
        e.Style.BackColor = Color.Orange;
    }
}
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid

#### Properties
- `CellStyle.Text`: Gets or sets the text content of the cell.
- `CellStyle.Font.Bold`: Gets or sets whether the font is bold.
- `CellStyle.BackColor`: Gets or sets the background color of the cell.
- `CellStyle.TextColor`: Gets or sets the text color of the cell.
- `CellStyle.CellType`: Gets or sets the type of the cell.
- `CellStyle.HorizontalAlignment`: Gets or sets the horizontal alignment of the cell.
- `CellStyle.Enabled`: Gets or sets whether the cell is enabled.

---

## Code Examples

#### Example: Styling Grid Cells Based on Specific Conditions

```csharp
private void Grid_PrepareViewStyleInfo(object sender, GridPrepareViewStyleInfoEventArgs e)
{
    // Example: Setting specific styles for a child table.
    if (e.ColIndex == 2 && e.RowIndex == 2)
    {
        e.Style.Text = "ChildTable";
        e.Style.Font.Bold = true;
        e.Style.BackColor = Color.YellowGreen;
        e.Style.TextColor = Color.Yellow;
        e.Style.CellType = "Static";
        e.Style.HorizontalAlignment = GridHorizontalAlignment.Left;
        e.Style.Enabled = false;
    }
    
    // Example: Handling drag-and-drop operations in the Grid.
    else if (e.Style.Text.StartsWith("Drag and Drop Parent Table Column headers"))
    {
        e.Style.Text = "Drag and Drop Parent Table Column headers";
        e.Style.BackColor = Color.Orange;
        e.Style.TextColor = Color.White;
    }
    
    // Example: Styling cells with dropped column headers.
    else if (e.Style.Text.StartsWith("Child"))
    {
        e.Style.BackColor = Color.Orange;
    }
}
```

---

### Notes:
- The `PrepareViewStyleInfo` event is used to customize the visual appearance of grid cells.
- The conditions in the code determine the application of different styles based on the content or positioning of the cells.

## See also:
- [Grid Layout and Styling in Windows Forms](#)
- [Handling Drag and Drop Operations in the Grid](#)

#### Tags and Keywords:

<!-- tags: [grid, winforms, styling, drag and drop, cell customization] keywords: [Color, GridPrepareViewStyleInfoEventArgs, CellStyle.Text, CellStyle.BackColor, CellStyle.Font.Bold, CellType, HorizontalAlignment] -->
```