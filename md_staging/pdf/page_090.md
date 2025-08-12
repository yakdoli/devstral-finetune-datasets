```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: pdf
page_number: 090
page_id: pdf#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:40Z
fidelity: lossless
-->

# Essential PDF

```csharp
textLink.Text = "Google Search";
textLink.Brush = brush;
textLink.Font = font;
textLink.Pen = PdfPens.Brown;
textLink.DrawTextWebLink(page, new PointF(10, 40));
```

### [VB.NET]

```vb
' Create the Text Web Link
Dim textLink As PdfTextWebLink = New PdfTextWebLink()
textLink.Url = "http://www.google.com"
textLink.Text = "Google Search"
textLink.Brush = brush
textLink.Font = font
textLink.Pen = PdfPens.Brown
textLink.DrawTextWebLink(page, New PointF(10, 40))
```

## 4.1.2.2 Graphics

### Primitives

The general class `PdfGraphics` enables drawing a wide range of primitives like lines, curves, paths, and text. For each such operation, there is a set of methods called `Draw<primitive>()` (e.g., `DrawLine()`). Each set of methods accepts parameters specific to each primitive type (for example: pen, brush, boundaries, etc.). If a pen is used, the primitive is drawn, and if a brush is used, the primitive is filled. You can also use `Null` value instead of pen or brush.

The following are the public members exposed by the `PdfGraphics` class.

## Methods

| Name                     | Description               |
|--------------------------|---------------------------|
| CheckCorrectLayoutRectangle | Creates laid            |
| ClipTranslateMargins      | Sets the drawing area and translates the origin |
| DrawArc                  | Draws an arc             |
| DrawBezier               | Draws a Bezier curve     |
| DrawEllipse              | Draws an ellipse         |
```

<!-- tags: [product, module, control, api, version?] keywords: [K1, K2, ...] -->
```