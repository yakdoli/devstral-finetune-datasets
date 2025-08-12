```html
<!-- sourcedata {json} {"image": "page_195.jpeg", "metadata": {"source": "image", "domain": "syncfusion-sdk", "task": "pdf-ocr-to-markdown", "language": "en", "source_filename": "page_195.jpeg", "document_name": "diagram", "page_number": "195", "page_id": "diagram#page_195", "product": "Syncfusion Winforms", "version": "11.4.0.26", "timestamp": "2025-08-09T04:19:22Z", "fidelity": "lossless"}, "content": {} -->
# Essential Diagram for Windows Forms

- ZoomToActual()

## Overview
The following code samples explain how to use the zoom methods to zoom in the diagram programmatically:

## Content

### C#
```csharp
// Sets the zoom increment value.
this.diagram1.View.ZoomIncrement = 20;
// Zoom in on the document.
this.diagram1.View.ZoomIn();
// Zoom out of the document.
this.diagram1.View.ZoomOut();
// Zoom the document to its actual size.
this.diagram1.View.ZoomToActual();
// Zoom the document to the selection.
this.diagram1.View.ZoomToSelection(new RectangleF(100,100,100,100));
```

### VB
```vb
' Sets the zoom increment value.
Me.diagram1.View.ZoomIncrement = 20
' Zoom in on the document.
Me.diagram1.View.ZoomIn()
' Zoom out of the document.
Me.diagram1.View.ZoomOut()
' Zoom the document to its actual size.
Me.diagram1.View.ZoomToActual()
' Zoom the document to the selection.
Me.diagram1.View.ZoomToSelection(New RectangleF(100,100,100,100))
```

### Zooming to the Center of the Diagram

The diagram document can be zoomed to the center of the current viewport by setting the **ZoomType** as **Center**. The default value of **ZoomType** is **Center**.

The following code sample demonstrates how to use the zoom to center feature in a diagram:

## Code Examples

The code examples provided demonstrate how to programmatically control the zoom of a diagram in both C# and VB.NET. The examples include setting the zoom increment, zooming in and out, zooming to actual size, and zooming to a specific selection on the diagram.

<!-- tags: [syncfusion, winforms, diagram, zoom, essential diagram, windows forms, vb.net, csharp, implementation guide] keywords: [syncfusion, winforms, diagram control, zoom methods, zoom increment, zoom to actual, zoom to selection, ZoomType, Center] -->
``` 
```