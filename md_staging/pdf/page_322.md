```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_322.jpeg
document_name: pdf
page_number: 322
page_id: pdf#page_322
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:46Z
fidelity: lossless
-->

# Essential PDF

```csharp
Dim mf As PdfMetafile = New PdfMetafile(TryCast(result.RenderedImage, Metafile))
mf.Quality = 100

Dim format As PdfMetafileLayoutFormat = New PdfMetafileLayoutFormat()
format.Break = PdfLayoutBreakType.FitPage
format.Layout = PdfLayoutType.Paginate

' Render the image in PDF document
mf.Draw(page, New PointF(0, 0), format)
```

**Note:** The custom page breaks is supported only when converting MetaFile to PDF. They are not supported when converting Bitmap to PDF.

## Rendering HTML page without Splitting

To avoid the images and text split across the page breaks, while rendering a large meta file with images and text in a PDF document, disable the `SplitTextLines` and `SplitImages` properties of the `PdfMetafileLayoutFormat` class. The following code illustrates this:

### [C#]

```csharp
PdfMetafileLayoutFormat format = new PdfMetafileLayoutFormat();
format.SplitTextLines = false;
format.SplitImages = false;
```

### [VB.NET]

```vb
Dim format As New PdfMetafileLayoutFormat()
format.SplitTextLines = False
format.SplitImages = False
```

### 4.4.1.1 HTML to PDF Conversion using Gecko Rendering Engine

Gecko is a free and open source layouting engine used in many applications developed by the Mozilla Foundation and the Mozilla Corporation (notably the Firefox web browser), as well as in many other open source software projects. Essential PDF also supports converting Webpages to PDF using Mozilla's Gecko rendering engine.

<!-- tags: [essential pdf, pdf conversion, gecko, html to pdf, winforms, syncfusion, 11.4.0.26] keywords: [gecko rendering engine, pdf metafile, page breaks, split text lines, split images, pdf conversion, html to pdf, syncfusion] -->
```