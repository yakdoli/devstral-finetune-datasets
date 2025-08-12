```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_463.jpeg
document_name: grid
page_number: 463
page_id: grid#page_463
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Identifier and style applicator for row and column indices.
- Handling the CellDrawn Event to customize grid cell appearance.
- Two language examples: C# and VB.NET with corresponding code blocks.

## Content

The above code identifies the 1st row, 1st column, and the even rows using their index values, and paints them with unique interior styles.

**Following code example illustrates handling the CellDrawn Event.**

### Using C#

```csharp
// Handling CellDrawn Event to customize the appearance of grid cells.
private void gridControl1_CellDrawn(object sender, GridDrawCellEventArgs e)
{
    if (e-ColIndex==6 &&e.RowIndex>0)
    {
        Rectangle rec = e.Bounds, rect=e.Bounds;
        rec.X=(e.Bounds.Left+e.Bounds.Right)/2;
        if(e.Style.CellValue.ToString()==1"")
        {
            e.Graphics.FillEllipse(Brushes.Gray,rect);
            
            GridImageCellRenderer.DrawImage(e.Graphics,this.imageList1,1,rec,false);
        }
        else
        {
            e.Graphics.FillEllipse(Brushes.LightGray,rect);
            
            GridImageCellRenderer.DrawImage(e.Graphics,this.imageList1,0,rec,false);
        }
    }
}
```

### Using VB.NET

```vb
' Handling CellDrawn Event to customize the appearance of grid cells.
Private Sub gridControl1_CellDrawn(ByVal sender As Object, ByVal e As GridDrawCellEventArgs)
    If e-ColIndex = 6 AndAlso e.RowIndex > 0 Then
        Dim rec As Rectangle = e.Bounds, rect As Rectangle = e.Bounds
```

## API Reference

This section does not highlight specific APIs, but the code examples demonstrate event handling methods such as `gridControl1_CellDrawn`.

## Code Examples

- **C# Example:** The example shows how to use the `CellDrawn` event to customize the visual appearance of cells in the grid.
- **VB.NET Example:** Demonstrates equivalent functionality, allowing developers to customize the grid based on cell values and positions.

<!-- tags: [Syncfusion, WinForms, CellDrawn, event handling, Grid controls] keywords: [grid, cell styling, CellDrawn, event, C#, VB.NET, even rows, first column, interior style, customization, essential grid] -->
``` 
