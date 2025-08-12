```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_271.jpeg
document_name: diagram
page_number: 271
page_id: diagram#page_271
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:01Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Draws endpoint outline and background.
- Overrides the method to change endpoint outline and background.

## OnDrawEndPointOutline Method

### Summary

```csharp
/// <summary>
/// Draws endpoint outline and background.
/// Override this method to change endpoint outline and background.
/// </summary>
/// <param name="gfx"></param>
/// <param name="rectHandle"></param>
/// <param name="endpoint"></param>
public override void OnDrawEndPointOutline(Graphics gfx, RectangleF rectHandle, EndPoint endpoint)
{
    using (Pen pen = new Pen(Color.Black))
    {
        pen.Width = 1f / gfx.PageScale;
        pen.DashStyle = DashStyle.Dot;
        // Create brush to fill PinPoint interiors
        using (SolidBrush brush = new SolidBrush(Color.Yellow))
        {
            // if endpoint is connected with port -- fill its interiors with red
            if (endpoint.Port != null)
            {
                brush.Color = Color.Orange;
            }

            if (!endpoint.AllowMoveX && !endpoint.AllowMoveY)
                brush.Color = Color.Gray;
            // Fill handle interiors
            gfx.FillRectangle(brush, rectHandle);

            // Outline handle
            gfx.DrawRectangle(pen,
                rectHandle.X, rectHandle.Y, rectHandle.Width,
                rectHandle.Height);
        }
    }
}
```

### Parameters

- `gfx`: A `Graphics` object used for drawing.
- `rectHandle`: A `RectangleF` representing the handle's dimensions.
- `endpoint`: An `EndPoint` object representing the endpoint to be drawn.

### Description

The `OnDrawEndPointOutline` method is used to draw the outline and background of the endpoint handle. It provides the flexibility to customize the appearance of the endpoint by overriding the method. The method uses a dashed black pen and a solid yellow brush by default. If the endpoint is connected to a port, the interior is filled with orange. If the endpoint is not allowed to move in either the X or Y direction, the interior is filled with gray.

### Code Example

```csharp
protected override void OnDrawEndPointOutline(Graphics gfx, RectangleF rectHandle, EndPoint endpoint)
{
    using (Pen pen = new Pen(Color.Black))
    {
        pen.Width = 1f / gfx.PageScale;
        pen.DashStyle = DashStyle.Dot;
        using (SolidBrush brush = new SolidBrush(Color.Yellow))
        {
            if (endpoint.Port != null)
            {
                brush.Color = Color.Orange;
            }

            if (!endpoint.AllowMoveX && !endpoint.AllowMoveY)
                brush.Color = Color.Gray;
            gfx.FillRectangle(brush, rectHandle);
            gfx.DrawRectangle(pen,
                rectHandle.X, rectHandle.Y, rectHandle.Width,
                rectHandle.Height);
        }
    }
}
```

## Creating a Rotation Handle

### Summary

```csharp
/// <summary>
/// Method creates and returns GraphicsPath that represents rotation handle
/// Override this method to change rotationhandle appearance
/// </summary>
/// <param name="location">Location of rotation handle</param>
/// <param name="handleSize">size of rotation handle</param>
/// <returns></returns>
```

### Parameters

- `location`: The location of the rotation handle.
- `handleSize`: The size of the rotation handle.

### Description

This method is responsible for creating and returning a `GraphicsPath` that represents the rotation handle. It provides the flexibility to customize the appearance of the rotation handle by overriding the method.

### Code Example

```csharp
protected override GraphicsPath CreateRotationHandle(PointF location, SizeF handleSize)
{
    // Implement the logic to create and return the GraphicsPath
    // Example:
    var path = new GraphicsPath();
    path.AddEllipse(location.X, location.Y, handleSize.Width, handleSize.Height);
    return path;
}
```

## Conclusion

This section outlines the methods and parameters used to draw endpoint outlines and backgrounds, as well as to create rotation handles in Windows Forms. These methods provide the flexibility to customize the appearance of endpoints and rotation handles by overriding them, allowing for greater control over the visual aspects of the application.

## Cross References

- [Getting Started with Syncfusion Diagram Controls](#getting-started)
- [Customizing Endpoint Appearance](#customizing-endpoint-appearance)
- [Rotation Handle Customization](#rotation-handle-customization)

<!-- tags: [Windows Forms, Diagram, Controls, Customization, Appearance, Rotation Handle, EndPoint] keywords: [Windows Forms, diagram, controls, customization, appearance, rotation handle, endpoint] -->
```