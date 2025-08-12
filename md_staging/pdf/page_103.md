```html
<!-- Backend data: {"source":"image","domain":"syncfusion-sdk","task":"pdf-ocr-to-markdown","language":"en","source_filename":"page_103.jpeg","document_name":"pdf","page_number":"103","page_id":"pdf#page_103","product":"Syncfusion Winforms","version":"11.4.0.26","timestamp":"2025-08-09T07:30:42Z","fidelity":"lossless"} -->
# Essential PDF

```vb
Dim brush As Syncfusion.Pdf.Graphics.PdfBrush = New Syncfusion.Pdf.Graphics.PdfSolidBrush(Color.Blue)

' Default color space.
graphics.DrawRectangle(pen, brush, rectangle)

graphics.Save()

' GrayScale color space.
graphics.ColorSpace = PdfColorSpace.GrayScale
graphics.DrawRectangle(pen, brush, rectangle)

' CMYK color space.
graphics.ColorSpace = PdfColorSpace.CMYK
graphics.DrawRectangle(pen, brush, rectangle)
graphics.Restore()

' Default color space.
graphics.DrawRectangle(pen, brush, rectangle)
```

> Note: You may change the color space as many times as you wish, however, you cannot alternate the color space for objects that have been saved before.

## 4.1.2.2.3 Images

Essential PDF supports both raster and vector images. It supports the following image formats:

- Bmp
- Jpeg
- Gif
- Png
- Tif
- Wmf
- Emf and
- Emf+

Images are supported through the `PdfImage` class, which is an abstract base class that provides the common functionality for `PdfBitmap` and `PdfMetafile` classes. There are static methods in `PdfImage` providing the capability to create a `PdfImage` instance from different sources.

<!-- tags: [PDF, color space, images, raster, vector, PdfImage, PdfBitmap, PdfMetafile] keywords: [Essential PDF, color space, DrawRectangle, pen, brush, rectangle, graphics.Save, graphics.Restore, Bmp, Jpeg, Gif, Png, Tif, Wmf, Emf] -->
```