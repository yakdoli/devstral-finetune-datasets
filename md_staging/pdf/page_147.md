```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_147.jpeg
document_name: pdf
page_number: 147
page_id: pdf#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:40Z
fidelity: lossless
-->

# Methods

The `Draw` method, part of the Essential PDF library, is used to render a `PdfGrid` on a `PdfGraphics` or `PdfPage`. The method has multiple overloads, each taking different parameters to specify the drawing location, bounds, or layout options. The return type varies based on the overload, either returning `void` or `PdfGridLayoutResult` for layout confirmation.

## Summary

- The `Draw` method renders a `PdfGrid` with various formatting options.
- Multiple overloads allow for drawing at specific locations or within bounds.
- Parameters include `PdfGraphics` for general rendering, `PdfPage` with specific location or bounds, and format options for layout.

## Content

### Draw Method

#### Parameters and Return Types

| Method | Description           | Parameters                                                                                  | Return Type            |
|--------|-----------------------|---------------------------------------------------------------------------------------------|------------------------|
| Draw   | Draws `PdfGrid`      | (PdfGraphics graphics)                                                                      | Void                   |
| Draw   |                       | (PdfPage page, PointF location)                                                             | PdfGridLayoutResult    |
| Draw   |                       | (PdfPage page, RectangleF bounds)                                                          | PdfGridLayoutResult    |
| Draw   |                       | (PdfGraphics graphics, PointF location)                                                   | Void                   |
| Draw   |                       | (PdfGraphics graphics, RectangleF bounds)                                                 | Void                   |
| Draw   |                       | (PdfPage page, float x, float y)                                                           | PdfGridLayoutResult    |
| Draw   |                       | (PdfPage page, PointF location, PdfGridLayoutFormat format)                              | PdfGridLayoutResult    |
| Draw   |                       | (PdfPage page, PointF location, PdfLayoutFormat format)                                   | PdfLayoutResult        |
| Draw   |                       | (PdfPage page, RectangleF bounds, PdfGridLayoutFormat format)                             | PdfGridLayoutResult    |
| Draw   |                       | (PdfPage page, PointF location, PdfLayoutFormat format)                                    | PdfLayoutResult        |
| Draw   |                       | (PdfGraphics graphics, float x, float y)                                                  | void                   |
| Draw   |                       | (PdfGraphics graphics, PointF location, float width)                                       | void                   |
| Draw   |                       | (PdfPage page, float x, float y, float width)                                              | PdfGridLayoutResult    |
| Draw   |                       | (PdfPage page, float x, float y, PdfGridLayoutFormat format)                              | PdfGridLayoutResult    |
| Draw   |                       | (PdfPage page, float x, float y, PdfLayoutFormat format)                                   | PdfLayoutResult        |
| Draw   |                       | (PdfGraphics graphics, float x, float y, float width)                                      | void                   |
| Draw   |                       | (PdfPage page, float x, float y, float width, PdfGridLayoutFormat format)                  | PdfGridLayoutResult    |

## API Reference

### Method Overloads

- **(PdfGraphics graphics):** Draws the grid using the provided graphic object.
- **(PdfPage page, PointF location):** Draws the grid at a specific point on a PDF page.
- **(PdfPage page, RectangleF bounds):** Draws the grid within the specified rectangular bounds.
- **(PdfGraphics graphics, PointF location):** Draws the grid at a specific point on the graphic object.
- **(PdfGraphics graphics, RectangleF bounds):** Draws the grid within the specified bounds on the graphic object.
- **(PdfPage page, float x, float y):** Draws the grid at specified coordinates.
- **(PdfPage page, PointF location, PdfGridLayoutFormat format):** Draws the grid with the specified format options.
- **(PdfPage page, RectangleF bounds, PdfGridLayoutFormat format):** Draws the grid within bounds with format options.
- **(PdfGraphics graphics, PointF location, float width):** Draws the grid at a specific point without height restriction.
- **(PdfGraphics graphics, float x, float y, float width):** Draws the grid at specific coordinates with width.
- **(PdfPage page, float x, float y, float width, PdfGridLayoutFormat format):** Draws the grid at specific coordinates with width and format options.

## Code Examples

### C# Example

```csharp
PdfGrid grid = new PdfGrid();
// Populate grid data

PdfDocument document = new PdfDocument();
PdfPage page = document.Pages.Add();

// Draw grid on the page
grid.Draw(page, new PointF(10, 10));

// Save the document
document.Save("GridExample.pdf");
document.Close(true);
```

### VB.NET Example

```vb
Dim grid As New PdfGrid()
' Populate grid data

Dim document As New PdfDocument()
Dim page As PdfPage = document.Pages.Add()

' Draw grid on the page
grid.Draw(page, New PointF(10, 10))

' Save the document
document.Save("GridExample.pdf")
document.Close(True)
```

## Related Topics

- **Document Overview:** General introduction to `Essential PDF` capabilities.
- **Handling Layouts:** Techniques for managing the layout of elements in PDF documents.
- **Core Features:** Overview of core features provided by the `Essential PDF` library.

<!-- tags: [syncfusion, winforms, essential pdf, pdfgrid, draw method, pdfdocument, pdfpage] keywords: [pdfgrid, draw, pdfdocument, pdfpage, pdfgraphics, layout, bounds, coordinates, pointf, rectanglef, format] -->
```