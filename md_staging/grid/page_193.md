```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_193.jpeg
document_name: grid
page_number: 193
page_id: grid#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
gridControl1[3, 4].Font.Orientation = 270
```

A sample demonstrating this feature is available under the following sample installation path.

### Sample Installation Path

**C:\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Appearance\Cell Style Demo**

## 4.1.4.2.10.2 Custom Borders

You can draw custom borders around cells by using the **DrawCellFrameAppearance** event of the Grid.

### Drawing Custom Borders

The **DrawCellFrameAppearance** event is triggered for every cell, before the grid draws the frame of a specified cell and after the cell's background is drawn. This event can be used with any cell type such as TextBox, CheckBox, and so on. You can draw texture-brush border and gradient borders.

The following code examples illustrate drawing custom borders by using the **DrawCellFrameAppearance** event:

### Using C#

1. **Using C#**

```csharp
[C#]
private void grid_DrawCellFrameAppearance(object sender, GridDrawCellBackgroundEventArgs e)
{
    // Draw a custom cell frame/border.
    int rowIndex = e.Style.CellIdentity.RowIndex;
    int colIndex = e.Style.CellIdentity.ColIndex;
    if (rowIndex > 0 && colIndex > 0)
    {
        Brush brush;
        Graphics g = e.Graphics;

        // Allocate and cache bitmap and texture brush.
        if (tb == null)
        {
            if (backBmp == null)
                backBmp = GetImage("back3.jpg");
            tb = new TextureBrush(backBmp);
        }
        brush = new SolidBrush(e.Style.BackColor);
        g.FillRectangle(brush, e.Bounds);
        g.DrawRectangle(tb as Pen, e.Bounds);
    }
}
```

<!-- tags: [grid, cell style, custom borders, drawcellframeappearance, texture brush, gradient border] keywords: [gridControl, cellIdentity, rowIndex, colIndex, texturebrush, gradient, custom borders] -->
```