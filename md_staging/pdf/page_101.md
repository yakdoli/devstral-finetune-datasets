```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_101.jpeg
document_name: pdf
page_number: 101
page_id: pdf#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:09Z
fidelity: lossless
-->

# Essential PDF

```vb
IccBasedCS4.ColorComponents = 3
IccBasedCS4.Range = New Double() { 0.0, 1.0, 0.0, 1.0, 0.0, 1.0 }

Dim red4 As PdfICCCColor = New PdfICCCColor(IccBasedCS4)
red4.ColorComponents = New Double() { 1, 0, 1 }
rect = New RectangleF(20, 110, 30, 30)
brush2 = New PdfSolidBrush(red4)

' Draw using the PdfBrush
g.DrawRectangle(brush2, rect)

' Create Separation color space
Dim exFunction As PdfExponentialInterpolationFunction = New PdfExponentialInterpolationFunction(True)
Dim numArray As Single() = New Single(2) {90.0F, 0.5F, 20.0F}
exFunction.C1 = numArray

Dim calLabCS8 As PdfLabColorSpace = New PdfLabColorSpace()
calLabCS8.Range = New Double() { 0.2, 1, 0.8, 23.5 }
calLabCS8.WhitePoint = New Double() { 0.2, 1, 0.8 }

' Instantiate Separation color space
Dim colorspace8 As PdfSeparationColorSpace = New PdfSeparationColorSpace()
colorspace8.AlternateColorSpaces = calLabCS8
colorspace8.TintTransform = exFunction
colorspace8.Colorant = "PANTONE Orange 021 C"
Dim color8 As PdfSeparationColor = New PdfSeparationColor(colorspace8)
color8.Tint = 0.7

brush2 = New PdfSolidBrush(color8)
rect = New RectangleF(100, 110, 30, 30)

' Draw using the PdfBrush
g.DrawRectangle(brush2, rect)

' Create Indexed color space
Dim colorspace7 As PdfIndexedColorSpace = New PdfIndexedColorSpace()

' Updated color values
colorspace7.BaseColorSpace = New PdfDeviceColorSpace(PdfColorSpace.RGB)
colorspace7.MaxColorIndex = 3
colorspace7.IndexedColorTable = New Byte() { 150, 0, 222, 255, 0, 0, 255, 0, 0, 0, 255 }

Dim color7 As PdfIndexedColor = New PdfIndexedColor(colorspace7)
color7.SelectColorIndex = 3
```

## Page-Level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [pdf brush, color components, color spaces, tint transform, separation color space, indexed color space, icc-based color space, pdf icccolor, pdf solid brush, exponential interpolation function, pdf lab color space] -->
```