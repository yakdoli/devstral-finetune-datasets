```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_098.jpeg
document_name: pdf
page_number: 098
page_id: pdf#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:12Z
fidelity: lossless
-->

## Overview
- Demonstrates the instantiation and usage of various color spaces in PDF documents.
- Includes ICC, separation, and indexed color spaces, as well as the creation of functions and color components.
- Features code examples for applying these color spaces to draw objects on a PDF page.

## Content

### Instantiating ICC Color Space

This section shows how to create an ICC color space and use it to draw a rectangle on a PDF page.

```csharp
// Instantiate ICC color space
PdfICCColorSpace IccBasedCS4 = new PdfICCColorSpace();
IccBasedCS4.ProfileData = profileData;
IccBasedCS4.AlternateColorSpace = calRgbCS3;
IccBasedCS4.ColorComponents = 3;
IccBasedCS4.Range = new double[] { 0.0, 1.0, 0.0, 1.0, 0.0, 1.0 };

PdfICCColor red4 = new PdfICCColor(IccBasedCS4);
red4.ColorComponents = new double[] { 1, 0, 1 };
rect = new RectangleF(20, 110, 30, 30);
brush2 = new PdfSolidBrush(red4);

// Draw using the PdfBrush
g.DrawRectangle(brush2, rect);
```

### Creating Separation Color Space

This section explains the creation of a separation color space and its usage to draw a rectangle on a PDF page.

```csharp
// Create Separation color space
PdfExponentialInterpolationFunction function = new PdfExponentialInterpolationFunction(true);
float[] numArray = new float[3] { 90f, 0.5f, 20f };
function.C1 = numArray;

PdfLabColorSpace calLabCS8 = new PdfLabColorSpace();
calLabCS8.Range = new double[] { 0.2, 1, 0.8, 23.5 };
calLabCS8.WhitePoint = new double[] { 0.2, 1, 0.8 };

// Instantiate Separation color space
PdfSeparationColorSpace colorspace8 = new PdfSeparationColorSpace();
colorspace8.AlternateColorSpaces = calLabCS8;
colorspace8.TintTransform = function;
colorspace8.Colorant = "PANTONE Orange 021 C";
PdfSeparationColor color8 = new PdfSeparationColor(colorspace8);
color8.Tint = 0.7;

brush2 = new PdfSolidBrush(color8);
rect = new RectangleF(100, 110, 30, 30);

// Draw using the PdfBrush
g.DrawRectangle(brush2, rect);
```

### Creating Indexed Color Space

This section illustrates the creation of an indexed color space, though it is left incomplete in the snippet.

```csharp
// Create Indexed color space
PdfIndexedColorSpace colorspace7 = new PdfIndexedColorSpace();

// Updated color values
colorspace7.BaseColorSpace = new PdfDeviceColorSpace(PdfColorSpace.RGB);
colorspace7.MaxColorIndex = 3;
```

## Code Examples

### Complete Example

Combining all the above color spaces into a cohesive example for demonstration purposes.

```csharp
// Instantiate ICC color space
PdfICCColorSpace IccBasedCS4 = new PdfICCColorSpace();
// ... (other ICC setup)

// Create Separation color space
PdfExponentialInterpolationFunction function = new PdfExponentialInterpolationFunction(true);
// ... (other separation setup)

// Create Indexed color space
PdfIndexedColorSpace colorspace7 = new PdfIndexedColorSpace();
// ... (other indexed setup)

rect = new RectangleF(50, 150, 40, 40);
brush2 = new PdfSolidBrush(red4);
g.DrawRectangle(brush2, rect);
```

## API Reference

- **Classes**: `PdfICCColorSpace`, `PdfICCColor`, `PdfExponentialInterpolationFunction`, `PdfLabColorSpace`, `PdfSeparationColorSpace`, `PdfSeparationColor`, `PdfIndexedColorSpace`
- **Methods**: `DrawRectangle`, `PdfSolidBrush`

## Cross References

See also:
- [Syncfusion PDF Library Documentation](https://www.syncfusion.com/products/file-formats/pdf-library)
- [PDF Color Spaces Overview](#pdf-color-spaces-overview)

<!-- tags: [Syncfusion, WinForms, PDF, ColorSpace, ICC, SeparationColorSpace, IndexedColorSpace] keywords: [pdf, color, color space, ICC, separation, indexed, function, device color space, brush, rectangle, draw, pdf library] -->
```