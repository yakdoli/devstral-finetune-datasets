```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_222.jpeg
document_name: pdf
page_number: 222
page_id: pdf#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:27Z
fidelity: lossless
-->

# Essential PDF

```csharp
PdfEllipse ellipse = new PdfEllipse(rect);

// Set layout property to make the element break across the pages.
PdfLayoutFormat format = new PdfLayoutFormat();
format.Break = PdfLayoutBreakType.FitPage;
format.Layout = PdfLayoutType.Paginate;
ellipse.Brush = PdfBrushes.Brown;

// Draw ellipse.
ellipse.Draw(page, 20, 20, format);
```

### [VB.NET]

```vb
Dim ellipse As PdfEllipse = New PdfEllipse(rect)

' Set layout property to make the element break across the pages.
Dim format As PdfLayoutFormat = New PdfLayoutFormat()
format.Break = PdfLayoutBreakType.FitPage
format.Layout = PdfLayoutType.Paginate
ellipse.Brush = PdfBrushes.Brown

' Draw ellipse.
ellipse.Draw(page, 20, 20, format)
```

## Code Examples

### C# Example

```csharp
PdfEllipse ellipse = new PdfEllipse(rect);
PdfLayoutFormat format = new PdfLayoutFormat();
format.Break = PdfLayoutBreakType.FitPage;
format.Layout = PdfLayoutType.Paginate;
ellipse.Brush = PdfBrushes.Brown;
ellipse.Draw(page, 20, 20, format);
```

### VB.NET Example

```vb
Dim ellipse As PdfEllipse = New PdfEllipse(rect)
Dim format As PdfLayoutFormat = New PdfLayoutFormat()
format.Break = PdfLayoutBreakType.FitPage
format.Layout = PdfLayoutType.Paginate
ellipse.Brush = PdfBrushes.Brown
ellipse.Draw(page, 20, 20, format)
```

<!-- tags: [Syncfusion, Winforms, PDF, Essential PDF, PdfEllipse, PdfLayoutFormat, PdfLayoutBreakType, PdfLayoutType] keywords: [pdf, ellipse, layout, pagination, break, fit page, draw, brown] -->
```