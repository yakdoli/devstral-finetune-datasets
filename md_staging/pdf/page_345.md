<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_345.jpeg
document_name: pdf
page_number: 345
page_id: pdf#page_345
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:10Z
fidelity: lossless
-->

# Essential PDF

```
' Create a new document class object.
Private doc As PdfDocument = New PdfDocument()

' Create few sections with few pages in each.
For i As Integer = 0 To 2
    Dim section As PdfSection = doc.Sections.Add()
    Dim label As PdfPageLabel = New PdfPageLabel()
        label.Prefix = "Sec" & i & "-"
    section.PageLabel = label

    Dim page As PdfPage
        For j As Integer = 0 To 9
            page = section.Pages.Add()
        Next j
Next i
doc.Save(filename)
```

## 5.1.1.5 How To Draw a SoftMask Image Into a PDF Document?

Essential PDF supports drawing mask images over other images. The `Mask` property of the `PdfBitmap` class is used for drawing masked images.

### [C#]

```csharp
// Bitmap with Tiff image mask.
PdfBitmap image = new PdfBitmap(tifImage);
(image as PdfBitmap).Mask = new PdfImageMask(new PdfBitmap(bmpImage));
page.Graphics.DrawString("Image mask", font, brush, new PointF(10, 350));
g.DrawImage(image, 10, 450);
```

### [VB.NET]

```vb
' Bitmap with Tiff image mask.
Dim image As PdfBitmap = New PdfBitmap(tifImage)
(TryCast(image, PdfBitmap)).Mask = New PdfImageMask(New PdfBitmap(bmpImage))
page.Graphics.DrawString("Image mask", font, brush, New PointF(10, 350))
g.DrawImage(image, 10, 450)
```

## 5.1.1.6 How To Embed 3D Files In a PDF Document?

```
```

---

<!-- tags: [syncfusion, winforms, pdf, embedding, 3d files] keywords: [essential pdf, softmask, masked images, embedding 3d files] -->