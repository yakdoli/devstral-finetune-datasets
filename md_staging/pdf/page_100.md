```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: pdf
page_number: 100
page_id: pdf#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:38Z
fidelity: lossless
-->

## Content

```vb
' Update color values
calGrayCS.Gamma = 0.7
calGrayCS.WhitePoint = New Double() { 0.2, 1, 0.8 }
Dim red1 As PdfCalGrayColor = New PdfCalGrayColor(calGrayCS)
red1.Gray = 0.1
brush2 = New PdfSolidBrush(red1)
rect = New RectangleF(100, 30, 30, 30)

' Draw using the PdfBrush
g.DrawRectangle(brush2, rect)

' Create Lab color space
Dim calGrayCS1 As PdfLabColorSpace = New PdfLabColorSpace()

' Update color values
calGrayCS1.Range = New Double() { 0.2, 1, 0.8, 23.5 }
calGrayCS1.WhitePoint = New Double() { 0.2, 1, 0.8 }
Dim red2 As PdfLabColor = New PdfLabColor(calGrayCS1)
red2.L = 90
red2.A = 0.5
red2.B = 20

brush2 = New PdfSolidBrush(red2)
rect = New RectangleF(180, 30, 30, 30)

' Draw using the PdfBrush
g.DrawRectangle(brush2, rect)

' Creating ICCBased color space
Dim calRgbCS3 As PdfCalRGBColorSpace = New PdfCalRGBColorSpace()
calRgbCS3.Gamma = New Double() { 7.6, 5.1, 8.5 }
calRgbCS3.Matrix = New Double() { 1, 0, 0, 0, 1, 0, 0, 0, 1 }
calRgbCS3.WhitePoint = New Double() { 0.7, 1, 0.8 }

' Read the ICC profile.
Dim fs As FileStream = New FileStream("rgb.icc", FileMode.Open, FileAccess.Read)
Dim profileData As Byte() = New Byte(fs.Length - 1) {}
fs.Read(profileData, 0, profileData.Length)
fs.Close()

' Instantiate ICC color space
Dim ICCBasedCS4 As PdfICCColorSpace = New PdfICCColorSpace()
ICCBasedCS4.ProfileName = "rgb.icc"
ICCBasedCS4.AlternteColorSpace = calRgbCS3
```

<!-- tags: [Syncfusion Winforms, Pdf Color Spaces, C#] keywords: [calGrayCS, PdfCalGrayColor, PdfSolidBrush, RectangleF, PdfBrush, PdfLabColorSpace, PdfLabColor, ICC, ICCBasedCS, ProfileData, AlternateColorSpace] -->
```