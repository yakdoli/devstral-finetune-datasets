```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_195.jpeg
document_name: grid
page_number: 195
page_id: grid#page_195
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Below is the code snippet provided in the image:

```vb
' Allocate and cache bitmap and texture brush.
If tb Is Nothing Then
    If backBmp Is Nothing Then
        backBmp = GetImage("back3.jpg")
    End If
    tb = New TextureBrush(backBmp)
End If

' Use TextureBrush for top-left cells.
If colIndex < 6 AndAlso rowIndex < 12 Then
    brush = tb
Else

    ' Otherwise use a gradient brush.
    brush = New System.Drawing.Drawing2D.LinearGradientBrush(e.TargetBounds, Color.FromArgb(204, 212, 230), Color.FromArgb(252, 172, 38), 45.0F)
End If

' Draw custom border for the cell.
' Space has been reserved for this area with the TableStyle.BorderMargins property.
Dim rect As Rectangle = e.TargetBounds
rect.Inflate(-2, -2)
Dim rects() As Rectangle = New Rectangle() {New Rectangle(rect.X, rect.Y, rect.Width, 4), New Rectangle(rect.X, rect.Y, 4, rect.Height), New Rectangle(rect.Right - 4, rect.Y, 4, rect.Height), New Rectangle(rect.X, rect.Bottom - 4, rect.Width, 4)}
g.FillRectangles(brush, rects)

' Disallow grid's default drawing of cell frame for this cell.
e.Cancel = True
End If
End Sub
```

## Overview

- This code snippet demonstrates how to customize the background and borders of cells in a grid.
- It uses either a texture brush from an image or a gradient brush based on the cell's position.
- The custom border is drawn by inflating the target bounds and filling specific rectangles.
- The grid's default cell frame drawing is disabled for this custom customization.

## Content

The code snippet above performs the following tasks:

1. **Allocate and Cache Bitmap and Texture Brush:**
   - If `tb` (texture brush) is `Nothing`, it checks for a bitmap (`backBmp`).
   - If `backBmp` is `Nothing`, it loads an image named `"back3.jpg"` and creates a new `TextureBrush` from it.
   - The texture brush (`tb`) is then assigned and cached for later use.

2. **Use TextureBrush for Top-Left Cells:**
   - For cells where `colIndex < 6` and `rowIndex < 12`, a `TextureBrush` is applied as the background.

3. **Use Gradient Brush for Other Cells:**
   - For cells outside the top-left section, a `LinearGradientBrush` is created with a gradient between two colors:
     - Starting color: `Color.FromArgb(204, 212, 230)`
     - Ending color: `Color.FromArgb(252, 172, 38)`
     - Gradient angle: `45.0F` degrees.

4. **Draw Custom Border for the Cell:**
   - The custom border is drawn by inflating the `e.TargetBounds` rectangle by `-2,-2` on all sides.
   - The border is composed of four separate rectangles, each thick (`4` pixels) along the edges of the cell.
   - These rectangles are filled using the brush created earlier.

5. **Disabling Default Cell Frame Drawing:**
   - Setting `e.Cancel = True` prevents the grid from drawing its default cell frame, allowing the custom drawing to take precedence.

## API Reference

- **System.Drawing.Drawing2D.LinearGradientBrush**
  - **Signature:** `public LinearGradientBrush(Rectangle r, Color color1, Color color2, float angle)`
  - **Parameters:**
    - `r`: Rectangle defining the bounds.
    - `color1`: Starting color.
    - `color2`: Ending color.
    - `angle`: Angle in degrees for the gradient.
  - **Purpose:** Creates a gradient brush to fill areas with a linear gradient between two colors.

- **System.Drawing.Drawing2D.TextureBrush**
  - **Signature:** `public TextureBrush(Image img)`
  - **Parameters:**
    - `img`: Image to be used as the texture.
  - **Purpose:** Creates a brush that fills areas with a texture derived from the specified image.

## Code Examples

The provided code snippet is a complete example demonstrating how to customize cell backgrounds and borders in a grid control using texture and gradient brushes. It handles different cases for different cell positions and disables the default grid drawing for the custom frames.

## Cross References

- See also: Grid customization, Custom cell rendering, Gradient and texture brushes, Border margins in Syncfusion Grid for Windows Forms.

<!-- tags: [syncfusion, grid, windowsforms, customization, rendering, texturebrush, lineargradientbrush] keywords: [cell background, custom border, texture brush, gradient brush, border margins, grid customization, windows forms, Syncfusion] -->
```