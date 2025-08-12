```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_225.jpeg
document_name: pdf
page_number: 225
page_id: pdf#page_225
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:51Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This section demonstrates how to work with images in `PdfImage` and `PdfMetafile`.
- It includes setting quality, drawing images, handling pagination, and handling multi-frame TIFF images.

## Content

### Working with PdfMetafile

```csharp
PdfMetafile metafile = (PdfMetafile)PdfImage.FromImage(img);

// Specify the quality of the metafile
metafile.Quality = 50;
```

### Using VB.NET

#### Drawing Image with Image Size

```vb
'Draw bitmap image with image size
Dim image As PdfImage = New PdfBitmap(pngImage)
g.DrawImage(image, 0, 0, image.Width, image.Height)
```

#### Drawing Metafile

```vb
'Draw metafile
Dim metafile As PdfMetafile = New PdfMetafile(emfImage)
g.DrawImage(metafile, New PointF(0, 50))
```

#### Handling Image Pagination

```vb
'Image pagination jpg
Dim image = New PdfBitmap(jpgImage)

'Set layout format for paginate the image to multiple pages.
Dim format As PdfLayoutFormat = New PdfLayoutFormat()
format.Layout = PdfLayoutType.Page
Dim location As PointF = New PointF(0, 400)
Dim size As SizeF = New SizeF(400, -1)
Dim rect As RectangleF = New RectangleF(location, size)
image.Draw(page, rect, format)
```

#### Handling Multi-Frame TIFF Images

```vb
'Multi-frame TIFF image
Dim tiffImage As PdfBitmap = New PdfBitmap(multiframeImage)
Dim frameCount As Integer = tiffImage.FrameCount
Dim i As Integer = 0
Do While i < frameCount
    page = section.Pages.Add()
    section.PageSettings.Margins.All = 0
    g = page.Graphics
    tiffImage.ActiveFrame = i
    g.DrawImage(tiffImage, 0,
            0, page.ClientSize().Width, page.ClientSize().Height)
    i += 1
Loop
```

#### Setting Quality for Bitmap Images

```vb
'Specify the quality of bitmap image
Dim image1 As New PdfBitmap(Image.FromFile("image.bmp"))
image1.Quality = 50
page.Graphics.DrawImage(image1, New PointF(0, 0))
```

## Cross References
- For more information on `PdfMetafile` and `PdfImage`, refer to the [Syncfusion WinForms documentation](https://help.syncfusion.com/windowsforms/pdf-getting-started).

<!-- tags: [PDF, Images, Metafile, Quality, Pagination, TIFF, Format, WinForms, Syncfusion] keywords: [PdfImage, PdfMetafile, Quality, Image pagination, Multi-frame TIFF, Layout format, DrawImage, FrameCount] -->
```