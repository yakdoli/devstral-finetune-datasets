```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_194.jpeg
document_name: grid
page_number: 194
page_id: grid#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:22Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### WinForms-specific conventions
- The provided code examples show how to customize cell appearance using different brushes and borders in a Windows Forms Grid.
- The example demonstrates how to use both a `TextureBrush` for top-left cells and a `LinearGradientBrush` for other cells.
- Custom borders are drawn using `Rectangle` definitions, and default cell frame drawing is disabled by setting `e.Cancel = true`.

#### C# Example
```csharp
}
// Use TextureBrush for top-left cells.
if (colIndex < 6 && rowIndex < 12)
    brush = tb;
else

// Otherwise use a gradient brush.
brush = new
System.Drawing.Drawing2D.LinearGradientBrush(e.TargetBounds,
    Color.FromArgb(204, 212, 230), Color.FromArgb(252, 172, 38), 45f);

// Draw custom border for the cell.
// Space has been reserved for this area with the
// TableStyle.BorderMargins property.
Rectangle rect = e.TargetBounds;
rect.Inflate(-2, -2);
Rectangle[] rects = new Rectangle[]
{
    new Rectangle(rect.X, rect.Y, rect.Width, 4),
    new Rectangle(rect.X, rect.Y, 4, rect.Height),
    new Rectangle(rect.Right - 4, rect.Y, 4, rect.Height),
    new Rectangle(rect.X, rect.Bottom - 4, rect.Width, 4),
};
g.FillRectangles(brush, rects);

// Disallow grid's default drawing of cell frame for this cell.
e.Cancel = true;
}
}
```

### 2. Using VB.NET

#### VB.NET Example
```vbnet
Private Sub grid_DrawCellFrameAppearance(ByVal sender As Object, ByVal e As GridDrawCellBackgroundEventArgs)

    ' Draw a custom cell frame/border.
    Dim rowIndex As Integer = e.Style.CellIdentity.RowIndex
    Dim colIndex As Integer = e.Style.CellIdentity.ColIndex
    If rowIndex > 0 AndAlso colIndex > 0 Then
        Dim brush As Brush
        Dim g As Graphics = e.Graphics
```

## API Reference (if applicable)
- The snippet demonstrates the use of the following:
  - `TextureBrush`
  - `LinearGradientBrush`
  - `Rectangle`
  - `Graphics.FillRectangles`
  - `e.Cancel` to disable default cell rendering

## Code Examples (multi-language supported)
The provided examples illustrate how to apply custom rendering to grid cells, showcasing the use of drawing classes and methods to enhance the visual appearance of specific cells.

### Cross References
See also:
- [Custom Cell Appearance in Windows Forms Grid](#)
- [Using Brushes for Custom Rendering](#)

<!-- tags: [syncfusion, winforms, grid, customcellappearance, lineargradientbrush, texturebrush, drawing] keywords: [cell rendering, winforms, grid, custom borders, brushes] -->
```