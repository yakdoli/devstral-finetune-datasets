```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_272.jpeg
document_name: diagram
page_number: 272
page_id: diagram#page_272
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:37Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### Custom Handle Rendering

The following code snippet demonstrates how to create and render a rotation handle shape and a resize handle shape using the `GraphicsPath` and `Pen` classes in Windows Forms.

#### Code Example: C#

```csharp
public override GraphicsPath CreateRotationHandleShape(PointF location, SizeF handleSize)
{
    RectangleF rect = Geometry.CreateRect(location, handleSize);
    return PathFactory.CreateRoundRectangle(rect, 2);
}

/// <summary>
/// Renders resize handle.
/// Override this method to change appearance of resize handle.
/// </summary>
/// <param name="gfx">Target Graphics</param>
/// <param name="size">size of outlining rectangle</param>
public override void OnDrawResizeHandleShape(Graphics gfx, BoxPosition handle, Node node, RectangleF rectHandle)
{
    using (Pen pen = new Pen(m_handleOutlineColor))
    {
        pen.Width = 1f / gfx.PageScale;
        pen.DashStyle = DashStyle.Solid;
        pen.Color = HandleOutlineColor;

        // Create brush to fill PinPoint interiors
        using (Brush brush =
            (!Enabled(handle, node) ? new SolidBrush(Color.Red) : new SolidBrush(Color.Green)))
        {
            using (GraphicsPath gp = PathFactory.CreateRoundRectangle(rectHandle, 3))
            {
                gfx.FillPath(brush, gp);
                // Outline handle
                gfx.DrawPath(pen, gp);
            }
        }
    }
}
```

#### Code Example: VB.NET

```vb
Public Class MyHandleRenderer
    Inherits UserHandleRenderer
    '
    ' <summary>
    '
```

## API Reference

### Classes and Methods
- **GraphicsPath**: Represents a series of connected lines and curves. Used for rendering custom shapes.
- **Pen**: Represents a pen used for drawing lines and outlines.
- **PathFactory.CreateRoundRectangle**: Creates a rounded rectangle contour.
- **BoxPosition**: Represents the position of a box. Used to determine the placement of the handle.
- **Node**: Represents a node in the diagram. Used to determine the state of the handle (enabled or disabled).
- **Enabled(handle, node)**: Method to determine if the handle is enabled for the specified node.
- **HandleOutlineColor**: Property representing the color of the handle outline.

### Parameters
- **gfx**: Target `Graphics` object for rendering.
- **handle**: `BoxPosition` specifying the position of the handle.
- **node**: `Node` object associated with the handle.
- **rectHandle**: `RectangleF` specifying the size and position of the handle.

### Outputs
- **GraphicsPath**: Returns a path representing the shape of the rotation handle.
- **void**: Method to draw the resize handle shape on the specified `Graphics` object.

## Code Examples

The provided code examples demonstrate how to:
1. **Create a Rotation Handle Shape**:
   - The `CreateRotationHandleShape` method creates a rounded rectangle using the `Geometry` and `PathFactory` classes.
   - The `RectangleF` is constructed based on the `location` and `handleSize` parameters.

2. **Render a Resize Handle Shape**:
   - The `OnDrawResizeHandleShape` method overrides the default rendering of the resize handle.
   - It uses a `Pen` to define the outline and a `Brush` to fill the interior of the handle.
   - The color of the handle is determined by the `Enabled` method, which checks the state of the handle for the specified node.

### Note
- The `HandleOutlineColor` property is used to set the color of the handle outline.
- The `Enabled` method is used to determine whether the handle is enabled, affecting the fill color of the handle.

## Cross References
- The code examples can be used in conjunction with the Syncfusion Diagram control to customize the appearance and behavior of handles.

## RAG Annotations

<!-- tags: [diagram, windows forms, controls, custom rendering, C#, VB.NET, handles, rotation, resize] keywords: [GraphicsPath, Pen, PathFactory, BoxPosition, Node, Enabled, HandleOutlineColor] -->
```