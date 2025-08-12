```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_224.jpeg
document_name: pdf
page_number: 224
page_id: pdf#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:24Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Advanced features like transparency and soft masking are supported.
- The following code snippets illustrate drawing images of different formats in a PDF document.

## Content
[C#]

```csharp
//Draw bitmap image with image size
PdfImage image = new PdfBitmap(pngImage);
g.DrawImage(image, 0, 0, image.Width, image.Height);

//Draw metafile
PdfMetafile metafile = new PdfMetafile(emfImage);
g.DrawImage(metafile, new PointF(0, 50));

//Image pagination jpg
image = new PdfBitmap(jpgImage);

//Set layout format for paginate the image to multiple pages.
PdfLayoutFormat format = new PdfLayoutFormat();
format.Layout = PdfLayoutType.Paginate;
PointF location = new PointF(0, 400);
SizeF size = new SizeF(400, -1);
RectangleF rect = new RectangleF(location, size);
image.Draw(page, rect, format);

//Multiframe Tiff image
PdfBitmap tiffImage = new PdfBitmap(multiframeImage);
int frameCount = tiffImage.FrameCount;
for (int i = 0; i < frameCount; i++)
{
    page = section.Pages.Add();
    section.PageSettings.Margins.All = 0;
    g = page.Graphics;
    tiffImage.ActiveFrame = i;
    g.DrawImage(tiffImage, 0, 0, page.GetClientSize().Width, page.GetClientSize().Height);
}

//Specify the quality of bitmap image
PdfBitmap image1 = new PdfBitmap(Image.FromFile("image.bmp"));
image1.Quality = 50;
page.Graphics.DrawImage(image1, new PointF(0, 0));

//Specify the quality of Metafile image
// Create metafile image
```

## API Reference
- `PdfBitmap` and `PdfMetafile` classes are used to handle bitmap and metafile images in a PDF document.
- `PdfLayoutFormat` class is used to define layout settings for images.
- `PdfLayoutType.Paginate` is used to specify the pagination of images across multiple pages.
- The `FrameCount` property of `PdfBitmap` is used to retrieve the number of frames in a multiframe image.
- The `ActiveFrame` property of `PdfBitmap` is used to set the active frame for display.
- The `Quality` property of `PdfBitmap` is used to specify the quality of the image.

<!-- tags: [essential pdf, Syncfusion Winforms, image handling, pdf bitmap, pdf metafile, pagination, multiframe tiff, quality specification, api reference] keywords: [Essential PDF, image rendering, layout format, pagination, multiframe image, quality, Syncfusion Winforms, api, version 11.4.0.26] -->
```