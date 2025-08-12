```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_336.jpeg
document_name: pdf
page_number: 336
page_id: pdf#page_336
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:17Z
fidelity: lossless
-->

## Essential PDF

```csharp
// Set the layout format
PdfMetafileLayoutFormat format = new PdfMetafileLayoutFormat();
format.Break = PdfLayoutBreakType.FitPage;
format.Layout = PdfLayoutType.Paginate;

// Prevent text getting break at the page breaks
format.SplitTextLines = false;

// Draw the converted image to PDF
metafile.Draw(page, new RectangleF(0, 0, img.Width, img.Height), format);

// Draw the image into the PDF document as bitmap
PdfImage image = new PdfBitmap(img);
PdfLayoutFormat format = new PdfLayoutFormat();
format.Break = PdfLayoutBreakType.FitPage;
format.Layout = PdfLayoutType.Paginate;
image.Draw(page, new RectangleF(0, 0, pageSize.Width, pageSize.Height), format);
```

### [VB.NET]

```vb
' Convert web page into image.
Dim html As HtmlConverter = New HtmlConverter()
Dim img As Image = html.ConvertToImage("www.syncfusion.com", ImageType.Metafile, 1024)

' Draw the image into the PDF document as metafile
' Create metafile image
Dim metafile As PdfMetafile = CType(PdfImage.FromImage(img), PdfMetafile)

' Specify the quality of the metafile
metafile.Quality = 100

' Set the layout format
Dim format As PdfMetafileLayoutFormat = New PdfMetafileLayoutFormat()
format.Break = PdfLayoutBreakType.FitPage
format.Layout = PdfLayoutType.Paginate

' Prevent text getting break at the page breaks
format.SplitTextLines = False

' Draw the converted image to PDF
metafile.Draw(page, New RectangleF(0, 0, img.Width, img.Height), format)
```

<!-- tags: [Essential PDF, Essential PDF, Essential PDF, Syncfusion Winforms, version: 11.4.0.26] keywords: [Essential PDF, PdfMetafileLayoutFormat, PdfLayoutBreakType, PdfLayoutType, PdfImage, Image, HtmlConverter, metafile, image, Draw, ConvertToImage, web page, text break, page breaks, quality, layout, fit page, paginate, split text lines, converted image, text, page, width, height, document, bitmap, rectangle, namespace, class, method, property, event, version, text break, prevent, text, break, page breaks] -->
```