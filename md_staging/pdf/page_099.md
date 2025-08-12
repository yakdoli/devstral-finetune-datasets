```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: pdf
page_number: 099
page_id: pdf#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:24Z
fidelity: lossless
-->

## Essential PDF

### Content

The following example shows how to create an indexed color space `PdfIndexedColorSpace` and how to use it to draw.

```csharp
colorsapce7.IndexedColorTable = new byte[] { 150, 0, 222, 255, 0, 0, 255, 0, 0, 0, 255 };
PdfIndexedColor color7 = new PdfIndexedColor(colorspace7);
color7.SelectColorIndex = 3;

brush2 = new PdfSolidBrush(color7);
rect = new RectangleF(180, 110, 30, 30);

// Draw using the PdfBrush
g.DrawRectangle(brush2, rect);
```

### VB.NET

```vb
' page1 has default color space.
Dim page1 As Syncfusion.Pdf.PdfPage = doc.Pages.Add()

doc.ColorSpace = PdfColorSpace.CMYK

' page2 has CMYK color space.
Dim page2 As Syncfusion.Pdf.PdfPage = doc.Pages.Add()

page = doc.Pages.Add()
g = page.Graphics

' Create CalRGB color space
Dim calRgbCS As PdfCalRGBColorSpace = New PdfCalRGBColorSpace()

' Update color values
calRgbCS.Gamma = New Double() { 1.6, 1.1, 2.5 }
calRgbCS.Matrix = New Double() { 1, 0, 0, 0, 1, 0, 0, 0, 1 }
calRgbCS.WhitePoint = New Double() { 0.2, 1, 0.8 }
Dim red As PdfCalRGBColor = New PdfCalRGBColor(calRgbCS)
red.Red = 0
red.Green = 1
red.Blue = 0

Dim brush2 As PdfBrush = New PdfSolidBrush(red)
Dim rect As RectangleF = New RectangleF(20, 30, 30, 30)

' Draw using the PdfBrush
g.DrawRectangle(brush2, rect)

' Create CalGray color space
Dim calGrayCS As PdfCalGrayColorSpace = New PdfCalGrayColorSpace()
```

<!-- tags: [pdf, color space, drawing, WinForms, Syncfusion, version: 11.4.0.26] keywords: [Essential PDF, PdfIndexedColorSpace, PdfCalRGBColorSpace, PdfCalGrayColorSpace, DrawRectangle, CMYK, CalRGB, CalGray] -->
```