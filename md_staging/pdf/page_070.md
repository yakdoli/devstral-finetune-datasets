<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_070.jpeg
document_name: pdf
page_number: 070
page_id: pdf#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:16Z
fidelity: lossless
-->

## Content

### Adding Layers and Drawing Arcs

This section demonstrates how to add a layer to a PDF page and draw arcs on it using different colors and widths.

#### C# Implementation

```csharp
// Add the layer
PdfPageLayer layer = page.Layers.Add("Layer1");
PdfGraphics graphics = layer.Graphics;
graphics.TranslateTransform(100, 60);

// Draw Arc
PdfPen pen = new PdfPen(Color.Red, 50);
RectangleF rect = new RectangleF(0, 0, 50, 50);
graphics.DrawArc(pen, rect, 360, 360);

pen = new PdfPen(Color.Blue, 30);
graphics.DrawArc(pen, 0, 0, 50, 50, 360, 360);

pen = new PdfPen(Color.Yellow, 20);
graphics.DrawArc(pen, rect, 360, 360);

pen = new PdfPen(Color.Green, 10);
graphics.DrawArc(pen, 0, 0, 50, 50, 360, 360);
```

#### VB.NET Implementation

```vb
' Add the layer
Dim layer As PdfPageLayer = page.Layers.Add("Layer1")
Dim graphics As PdfGraphics = layer.Graphics
graphics.TranslateTransform(100, 60)

' Draw Arc
Dim pen As New PdfPen(Color.Red, 50)
Dim rect As New RectangleF(0, 0, 50, 50)
graphics.DrawArc(pen, rect, 360, 360)
```

## Explanation

1. **Adding a Layer**:
   - The `PdfPageLayer` object is used to add a new layer to the PDF page with the name "Layer1".
   - The `PdfGraphics` object is obtained from the layer to perform drawing operations.

2. **Transforming the Graphics**:
   - The `TranslateTransform` method is used to move the origin of the graphics object to the specified coordinates `(100, 60)`.

3. **Drawing Arcs**:
   - A `PdfPen` object is created for each arc with different colors and widths.
   - The `DrawArc` method is used to draw arcs, specifying the pen, the bounding rectangle, and the start and sweep angles.

4. **Color and Width Variation**:
   - Different colors (`Color.Red`, `Color.Blue`, `Color.Yellow`, `Color.Green`) and widths (`50`, `30`, `20`, `10`) are used to draw arcs, demonstrating how to customize the appearance of the arcs.

## Notes

- Ensure that the appropriate namespaces (`Syncfusion.Pdf`) are imported to use the `PdfPageLayer`, `PdfGraphics`, `PdfPen`, and `PdfPage` classes.
- The `RectangleF` object defines the bounding box for the arc, and the angles are specified in degrees.

<!-- tags: [Syncfusion, WinForms, PDF, graphics, drawing, arcs, layers] keywords: [PdfPageLayer, PdfGraphics, PdfPen, DrawArc, TranslateTransform, RectangleF] -->