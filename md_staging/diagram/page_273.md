```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_273.jpeg
document_name: diagram
page_number: 273
page_id: diagram#page_273
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:22Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Methods to Customize Endpoint Appearance

### `OnDrawEndpointOutline` Method

```vb
''' Draws endpoint outline and background.
''' Override this method to change endpoint outline and 
''' background. 
''' </summary>
''' <param name="gfx"></param>
''' <param name="rectHandle"></param>
''' <param name="endpoint"></param>
Public Overloads Sub OnDrawEndpointOutline(ByVal gfx As Graphics, ByVal rectHandle As RectangleF, ByVal endpoint As Net.EndPoint)
    Using pen As New Pen(Color.Black)
        pen.Width = 1.0F / gfx.PageScale
        pen.DashStyle = DashStyle.Dot
        ' Create brush to fill PinPoint interiors 
        Using brush As New SolidBrush(Color.Yellow)
            ' if endpoint is connected with port -- fill its
            ' interiors with red 
            If endpoint.Port IsNot Nothing Then
                brush.Color = Color.Orange
            End If

            If Not endpoint.AllowMoveX AndAlso Not endpoint.AllowMoveY Then
                brush.Color = Color.Gray
            End If
            ' Fill handle interiors 
            gfx.FillRectangle(brush, rectHandle)
        End Using
        ' Outline handle 
        gfx.DrawRectangle(pen, rectHandle.X, rectHandle.Y, rectHandle.Width, rectHandle.Height)
    End Using
End Sub
```

### `CreateRotationHandleShape` Method

```vb
''' <summary>
''' Method creates and returns GraphicsPath that represents 
''' rotation handle 
''' Override this method to change rotationhandle appearance 
''' </summary>
''' <param name="location">Location of rotation handle</param>
''' <param name="handleSize">size of rotation handle</param>
''' <returns></returns>
Public Overloads Function CreateRotationHandleShape(ByVal location As PointF, ByVal handleSize As SizeF) As Drawing2D.GraphicsPath
```

## API Reference

### `OnDrawEndpointOutline`

- **Parameters**:
  - `gfx` - Type: `Graphics`
  - `rectHandle` - Type: `RectangleF`
  - `endpoint` - Type: `Net.EndPoint`

- **Description**: Draws the endpoint outline and background. This method can be overridden to customize the appearance of endpoint outlines and backgrounds.

### `CreateRotationHandleShape`

- **Parameters**:
  - `location` - Type: `PointF`
  - `handleSize` - Type: `SizeF`

- **Returns**: `Drawing2D.GraphicsPath`
- **Description**: Creates and returns a `GraphicsPath` that represents the rotation handle. This method can be overridden to modify the appearance of the rotation handle.

## Code Examples

### Example of Overriding `OnDrawEndpointOutline`

```vb
Public Class MyDiagram
    Inherits Diagram

    Protected Overrides Sub OnDrawEndpointOutline(ByVal gfx As Graphics, ByVal rectHandle As RectangleF, ByVal endpoint As Net.EndPoint)
        Using pen As New Pen(Color.Red)
            pen.Width = 2.0F / gfx.PageScale
            pen.DashStyle = DashStyle.Dash
            Using brush As New SolidBrush(Color.Blue)
                If endpoint.Port IsNot Nothing Then
                    brush.Color = Color.LightBlue
                End If
                gfx.FillRectangle(brush, rectHandle)
                gfx.DrawRectangle(pen, rectHandle.X, rectHandle.Y, rectHandle.Width, rectHandle.Height)
            End Using
        End Using
    End Sub
End Class
```

## Related Topics

- **Customization of Diagram Handles**
- **Override Methods for Custom Drawing**
- **GraphicsPath for Shape Representation**

<!-- tags: [diagram, windows forms, customization, endpoints, rotation, handles] keywords: [endpoint, background, outline, rotation handle, graphics, fill, stroke, override methods, customization, user interface] -->
```