```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: pdf
page_number: 096
page_id: pdf#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:25Z
fidelity: lossless
-->

# Device Color Spaces

- DeviceGray
- DeviceRGB
- DeviceCMYK

## CIE-based Color Spaces

- CalGray
- CalRGB
- Lab

## ICC-based Color Spaces

- Special color spaces
- Indexed
- Separation

## Color Spaces in C#

```csharp
[C#]

// page1 has default color space.
PdfPage page1 = doc.Pages.Add();
doc.ColorSpace = PdfColorSpace.CMYK;

// page2 has CMYK color space.
PdfPage page2 = doc.Pages.Add();

// Create CalRGB color space
PdfCalRGBColorSpace calRgbCS = new PdfCalRGBColorSpace();

// Update color values
calRgbCS.Gamma = new double[] { 1.6, 1.1, 2.5 };
calRgbCS.Matrix = new double[] { 1, 0, 0, 0, 1, 0, 0, 1 };
calRgbCS.WhitePoint = new double[] { 0.2, 1, 0.8 };
PdfCalRGBColor red = new PdfCalRGBColor(calRgbCS);
red.Red = 0;
red.Green = 1;
red.Blue = 0;

PdfBrush brush2 = new PdfSolidBrush(red);
RectangleF rect = new RectangleF(20, 30, 30, 30);
```

## Page-level Navigation/TOC (if applicable)

Not applicable on this page.

### Cross References

Not applicable on this page.

<!-- tags: [syncfusion, winforms, color spaces, c#, pdf, essential pdf, device color spaces, cie-based color spaces, icc-based color spaces, calrgb, cmyk] keywords: [device color spaces, cie-based color spaces, icc-based color spaces, calrgb, cmyk, pdf color manipulation, winforms implementation, c# code example, essential pdf, syncfusion, version 11.4.0.26] -->
```