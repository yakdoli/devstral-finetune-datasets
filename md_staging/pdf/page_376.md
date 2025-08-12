```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_376.jpeg
document_name: pdf
page_number: 376
page_id: pdf#page_376
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:10Z
fidelity: lossless
--> 

## Essential PDF

### C#

```csharp
// Convert web page into image.
HtmlConverter html = new HtmlConverter();
System.Drawing.Image img = html.ConvertToImage("www.syncfusion.com", ImageType.Metafile, (int)width, -1, AspectRatio.KeepWidth, "UserName", "Password");

// Draw the image into the PDF document as metafile
PdfMetafile metafile = (PdfMetafile) (PdfImage.FromImage(img));
metafile.Quality = 100;
PdfMetafileLayoutFormat format = new PdfMetafileLayoutFormat();
format.Break = PdfLayoutBreakType.FitPage;
format.Layout = PdfLayoutType.Paginate;
doc.PageSettings.Height = img.Height;
format.SplitTextLines = false;
metafile.Draw(page, new RectangleF(0F, 0F, (float)(pageSize.Width), -1F), format);

// Draw the image into the PDF document as Bitmap
PdfImage image = new PdfBitmap(img);
PdfLayoutFormat format = new PdfLayoutFormat();
format.Break = PdfLayoutBreakType.FitPage;
format.Layout = PdfLayoutType.Paginate;
image.Draw(page, new RectangleF(0F, 0F, (float)(img.Width), (float)(img.Height)), format);
```

### VB.NET

```vbnet
' Convert web page into image.
Dim html As HtmlConverter = New HtmlConverter()
Dim img As System.Drawing.Image = html.ConvertToImage("www.syncfusion.com", ImageType.Metafile, CInt(Fix(Width)), -1, AspectRatio.KeepWidth, "UserName", "Password")

' Draw the image into the PDF document as metafile
Dim metafile As Syncfusion.Pdf.Graphics.PdfMetafile = CType(PdfImage.FromImage(img), Syncfusion.Pdf.Graphics.PdfMetafile)
metafile.Quality = 100
Dim format As Syncfusion.Pdf.Graphics.PdfMetafileLayoutFormat = New Syncfusion.Pdf.Graphics.PdfMetafileLayoutFormat()
format.Break = PdfLayoutBreakType.FitPage
format.Layout = PdfLayoutType.Paginate
doc.PageSettings.Height = img.Height
format.SplitTextLines = False
metafile.Draw(page, New RectangleF(0F, 0F, CSng(pageSize.Width), -1F),
```

<!-- tags: [Essential PDF, HTML to Image, Web Page Conversion, PDF Document, Metafile Drawing, Bitmap Drawing, Split Text Lines, Fit Page] keywords: [HtmlConverter, ConvertToImage, PdfMetafile, PdfImage, AspectRatio.KeepWidth, PdfMetafileLayoutFormat, PdfLayoutBreakType, PdfLayoutType, RectangleF, PageSettings, Convert Web Page to Image, Draw Metafile to PDF, Draw Bitmap to PDF] -->
```