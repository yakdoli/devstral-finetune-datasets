```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_277.jpeg
document_name: diagram
page_number: 277
page_id: diagram#page_277
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:42Z
fidelity: lossless
-->

## Diagram Image for Windows Forms

### Getting a Thumbnail Image of a Diagram

The following snippets demonstrate how to generate a thumbnail image of a diagram and display it in a PictureBox using both C# and VB.NET.

#### C#

```csharp
Image.GetThumbnailImageAbort myCallback = new Image.GetThumbnailImageAbort(ThumbnailCallback);
this.pictureBox1.Image = (Bitmap) diagramimage.GetThumbnailImage(150, 75, myCallback, IntPtr.Zero);
```

#### VB.NET

```vb.net
Public Function ThumbnailCallback() As Boolean
    Return False
End Function

' Generate Thumbnail and set it to be image of the PictureBox
Dim myCallback As Image.GetThumbnailImageAbort = New Image.GetThumbnailImageAbort(AddressOf ThumbnailCallback)
Me.pictureBox1.Image = CType(diagramimage.GetThumbnailImage(150, 75, myCallback, IntPtr.Zero), Bitmap)
```

## 5.18 How to Get a Connector Vertex Point?

Connector has a method called `GetPoint` to get its vertex point.

This method has two parameters: `int` and `bool`

- `int` specifies the vertex point in the local coordinates
- `bool` specifies the path of the connector

Set the `bool` parameter to `True` to get the connector vertex point based on its graphical path and `False` to get the connector point based on its relative path.

The following code snippet illustrates this:

#### C#

```csharp
// LineConnector
ConnectorBase Connector = new LineConnector(new Drawing.PointF(0F, 0F), new Drawing.PointF(10F, 10F));

// set points
Connector.SetPoints(new PointF[2] { Connector.GetPoint(0), Connector.GetPoint(Connector.GetPoints().GetLength(0) - 1, false) });
```

#### VB.NET

```vb.net
' LineConnector
Dim Connector As ConnectorBase = New LineConnector(New Drawing.PointF(0F, 0F), New Drawing.PointF(10F, 10F))

' set points
Connector.SetPoints(New PointF(2) { Connector.GetPoint(0), Connector.GetPoint(Connector.GetPoints().GetLength(0) - 1, False) })
```
```html
<!-- tags: [Syncfusion, Winforms, Connector, Vertex, Diagram, GetThumbnailImage, PictureBox] keywords: [connector, vertex point, getpoint, thumbnail, image, graphical path, relative path] -->
``` 
