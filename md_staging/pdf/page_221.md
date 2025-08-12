```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_221.jpeg
document_name: pdf
page_number: 221
page_id: pdf#page_221
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:40Z
fidelity: lossless
-->

# Essential PDF

PdfGraphics class allows drawing a wide range of primitives like

- Lines
- Curves
- Paths
- Text

For each such operation there is a set of methods like Draw\(<\)primitive\(>\)() (for example: DrawLine).

Each set of methods accepts parameters specific to each primitive type (for example: pen, brush, boundaries, etc.).

- If pen is used, the primitive will be drawn
- If brush is used, the primitive will be filled.

**Note**: You must add the Syncfusion.Pdf.Graphics namespace to work with graphic objects.

## Code Example

The following code example illustrates how to draw shapes.

### [C#]

```csharp
// Draws polygon with pen and brush.
PdfGraphics g = page.Graphics;
PdfPen pen = new PdfPen(Color.Brown);
PdfSolidBrush brush = new PdfSolidBrush(Color.Green);
g.DrawPolygon(pen, brush, points);
```

### [VB.NET]

```vb
' Draws polygon with pen and brush.
Dim g As PdfGraphics = page.Graphics
Dim pen As PdfPen = New PdfPen(Color.Brown)
Dim brush As PdfSolidBrush = New PdfSolidBrush(Color.Green)
g.DrawPolygon(pen, brush, points)
```

You can paginate the element as follows.

### [C#]


## API Reference


## Code Examples (multi-language supported)


## Page-level Navigation/TOC (if applicable)


## Cross References


<!-- tags: [pdf, graphics, primitives,Syncfusion Winforms,11.4.0.26] keywords: [PdfGraphics, DrawLine, DrawPolygon, pen, brush, primitive, Syncfusion.Pdf.Graphics] -->
```