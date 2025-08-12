```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: pdf
page_number: 094
page_id: pdf#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:53Z
fidelity: lossless
-->

# Essential PDF

To apply different settings to text output, `PdfStringFormat` class is used. It contains a variety of properties that allow setting different text output settings.

## Overview
- The `PdfStringFormat` class is used for text output settings.
- Requires the `Syncfusion.Pdf.Graphics` namespace for working with Graphics and graphic elements.
- Provides functionality to draw graphic elements on the canvas (`PdfGraphics`).

### Graphic Elements

These include the basic functionality of drawing elements on the canvas (`PdfGraphics`). As a result, you can draw such objects on pages or any other object that has a graphics context (`PdfTemplate` etc.). Graphics elements are simple and do not span several pages.

#### Layout

The `PdfLayoutElement` class provides the ability to draw contents on several pages. This functionality is described in the **Pagination** section.

#### Shapes

The `PdfShapeElement` class provides the basic functionality of simple graphics primitives (like lines, rectangles, etc.). It is derived from `LayoutElement`, which enables every shape to span several pages. The basic graphics primitives are as follows:

- Line
- Rectangle
- Polygon
- Arc
- Bezier Curve
- Ellipse
- Path
- PdfTemplate
- Pie
- Image

Each shape can be drawn by its own `Draw` method or by using an appropriate method of the `PdfGraphics` class (like `DrawLine`, `DrawRectangle`, etc.). Each shape has its own coordinate system (which is equal to a page coordinate system). Coordinates of the shape are set in that coordinate system. When the shape is going to be drawn by using its `Draw` method, its coordinate system is translated by the coordinates set to the `Draw` method. So, whenever the shape is going to be drawn, take its own coordinate system into consideration.

## API Reference (if applicable)

### PdfStringFormat
- Namespace: `Syncfusion.Pdf.Graphics`
- Properties for setting text output settings.

### PdfGraphics
- Methods for drawing graphic elements on the canvas.

### PdfLayoutElement
- Ability to draw contents on several pages.

### PdfShapeElement
- Derived from `LayoutElement`
- Methods for drawing simple graphics primitives.
  - `Draw` method
  - `PdfGraphics` class methods

### PdfShapeElement Coordinate System
- Each shape has its own coordinate system, which is equal to the page coordinate system.
- Coordinates of the shape are set in that coordinate system.

## Code Examples (multi-language supported)

```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.Graphics;

// Example of using PdfStringFormat
PdfStringFormat format = new PdfStringFormat();
format.Font = new PdfTrueTypeFont(new FontFamily("Arial"), 12);
format.Color = PdfColor.Black;
format.TextAlign = PdfTextAlignment.Left;

// Example of using PdfGraphics to draw shapes
PdfFixedDocument document = new PdfFixedDocument();
PdfPage page = document.Pages.Add();
PdfGraphics graphics = page.Graphics;

// Drawing a line
graphics.DrawLine(PdfBrushes.Black, new PointF(50, 50), new PointF(150, 50));

// Drawing a rectangle
graphics.DrawRectangle(PdfBrushes.Blue, new RectangleF(50, 75, 100, 50));
```

## Cross References

- See also: **Pagination** section for more information on content spanning multiple pages.

<!-- tags: [pdf, syncfusion winforms, graphic elements, text output, shapes, layout] keywords: [PdfStringFormat, PdfGraphics, PdfLayoutElement, PdfShapeElement, Draw, PdfTemplate, Line, Rectangle, Polygon, Arc, Bezier Curve, Ellipse, Path, Image] -->
```