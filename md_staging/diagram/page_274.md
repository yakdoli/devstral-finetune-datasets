```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_274.jpeg
document_name: diagram
page_number: 274
page_id: diagram#page_274
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:21Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to create a customized resize handle appearance in a Windows Forms application using Syncfusion Diagram.
- Provides code for rendering and styling the resize handle, including enabling/disabling functionality.
- Includes a figure showcasing the customized appearance of the resize handle.

## Content

### Code Example

```vb
Dim rect As RectangleF = Geometry.CreateRect(location, handleSize)
Return PathFactory.CreateRoundRectangle(rect, 2)
End Function

''' <summary>
''' Renders resize handle.
''' Override this method to change appearance of resize handle.
''' </summary>
''' <param name="gfx">Target Graphics</param>
''' <param name="size">size of outlining rectangle</param>
Public Overloads Sub OnDrawResizeHandleShape(ByVal gfx As Graphics, ByVal handle As Syncfusion.Windows.Forms.Diagram.BoxPosition, ByVal node As Syncfusion.Windows.Forms.Diagram.Node, ByVal rectHandle As RectangleF)
    Using pen As New Pen(m_handleOutlineColor)
        pen.Width = 1.0F / gfx.PageScale
        pen.DashStyle = DashStyle.Solid
        pen.Color = HandleOutlineColor

        ' Create brush to fill PinPoint interiors
        Using brush As Brush = (Not Enabled(handle, node) ? New SolidBrush(Color.Red) : New SolidBrush(Color.Green))
            Using gp As Drawing2D.GraphicsPath = PathFactory.CreateRoundRectangle(rectHandle, 3)
                gfx.FillPath(brush, gp)
                ' Outline handle
                gfx.DrawPath(pen, gp)
            End Using
        End Using
    End Using
End Sub
End Class
```

### Customized Appearance

![Figure 156: Customized Appearance](https://example.com/image_156.png)

The figure above illustrates the customized appearance of a resize handle for a Windows Forms Diagram. The handle is rendered with a solid green interior for enabled nodes and a red interior for disabled nodes, along with surrounding red outlines.

## Sample Installation

A sample which demonstrates this feature is available in the below sample installation location.

## API Reference

The code snippet provided uses the following key elements:

- **Graphics:** The target graphics surface for rendering.
- **BoxPosition:** Specifies the position of the resize handle.
- **Node:** Represents the diagram node to which the handle belongs.
- **RectangleF:** Defines the bounding rectangle of the resize handle.

### Methods
- **OnDrawResizeHandleShape:** Overloaded method to draw the resize handle with custom styling.
- **CreateRoundRectangle:** Creates a rounded rectangle path for the handle.

### Properties
- **m_handleOutlineColor:** Color used for the outline of the handle.
- **HandleOutlineColor:** Property to set the outline color of the handle.

### Constants
- **DashStyle.Solid:** Used for defining the solid line style of the handle's outline.

### Conditional Logic
- **Enabled(handle, node):** A method to determine whether the node is enabled, affecting the fill color of the handle.

## Code Examples

The provided code allows customization of the resize handle's appearance by overriding the `OnDrawResizeHandleShape` method. It demonstrates how to create a rounded rectangle path, apply different colors based on node status, and draw the handle's outline.

## Cross References

- See also: [Syncfusion Diagram Documentation](https://www.syncfusion.com/documentation/windowsforms/diagram)
- [Handling Events in Diagram Control](https://www.syncfusion.com/documentation/windowsforms/diagram/events)

<!-- tags: [Syncfusion, Windows Forms, Diagram, Resize Handle, Customization, Appearance, Graphics] keywords: [OnDrawResizeHandleShape, BoxPosition, Node, RectangleF, DashStyle.Solid, HandleOutlineColor, Enabled] -->
```