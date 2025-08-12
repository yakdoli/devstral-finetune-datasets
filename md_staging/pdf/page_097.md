```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_097.jpeg
document_name: pdf
page_number: 097
page_id: pdf#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:29:47Z
fidelity: lossless
-->

## Essential PDF

### Content

#### Code Example: Drawing with Color Spaces

The following code demonstrates how to create and use different color spaces (CalGray and Lab) to draw rectangles in PDF documents.

```csharp
// Draw using the PdfBrush
g.DrawRectangle(brush2, rect);

// Create CalGray color space
PdfCalGrayColorSpace calGrayCS = new PdfCalGrayColorSpace();

// Update color values
calGrayCS.Gamma = 0.7;
calGrayCS.WhitePoint = new double[] { 0.2, 1, 0.8 };
PdfCalGrayColor red1 = new PdfCalGrayColor(calGrayCS);
red1.Gray = 0.1;
brush2 = new PdfSolidBrush(red1);
rect = new RectangleF(100, 30, 30, 30);

// Draw using the PdfBrush
g.DrawRectangle(brush2, rect);

// Create Lab color space
PdfLabColorSpace calGrayCS1 = new PdfLabColorSpace();

// Update color values
calGrayCS1.Range = new double[] { 0.2, 1, 0.8, 23.5 };
calGrayCS1.WhitePoint = new double[] { 0.2, 1, 0.8 };
PdfLabColor red2 = new PdfLabColor(calGrayCS1);
red2.L = 90;
red2.A = 0.5;
red2.B = 20;

brush2 = new PdfSolidBrush(red2);
rect = new RectangleF(180, 30, 30, 30);

// Draw using the PdfBrush
g.DrawRectangle(brush2, rect);

// Creating ICCBased color space
PdfCalRGBColorSpace calRgbCS3 = new PdfCalRGBColorSpace();
calRgbCS3.Gamma = new double[] { 7.6, 5.1, 8.5 };
calRgbCS3.Matrix = new double[] { 1, 0, 0, 0, 1, 0, 0, 0, 1 };
calRgbCS3.WhitePoint = new double[] { 0.7, 1, 0.8 };

// Read the ICC profile.
FileStream fs = new FileStream(@"rgb.icc", FileMode.Open, FileAccess.Read);
byte[] profileData = new byte[fs.Length];
fs.Read(profileData, 0, profileData.Length);
fs.Close();
```

### Explanation

1. **Creating and Configuring CalGray Color Space**:
   - A `PdfCalGrayColorSpace` is created.
   - The `Gamma` and `WhitePoint` properties are updated to customize the color space.
   - A `PdfCalGrayColor` object is created using the defined color space, and its `Gray` value is set to `0.1`.
   - A `PdfSolidBrush` is created using the `PdfCalGrayColor` object, and a rectangle is drawn.

2. **Creating and Configuring Lab Color Space**:
   - A `PdfLabColorSpace` is created.
   - The `Range` and `WhitePoint` properties are updated.
   - A `PdfLabColor` object is created using the defined color space, and its `L`, `A`, and `B` values are set.
   - A `PdfSolidBrush` is created using the `PdfLabColor` object, and a second rectangle is drawn.

3. **Creating ICCBased Color Space**:
   - An `PdfCalRGBColorSpace` is created.
   - The `Gamma`, `Matrix`, and `WhitePoint` properties are configured.
   - An ICC profile file (`rgb.icc`) is read to further define the color space.

### Notes
- The `PdfCalGrayColorSpace` and `PdfLabColorSpace` allow for precise control over color rendering based on detailed specifications.
- The ICC profile provides a standard way to define and apply color spaces, ensuring consistency across devices.

### See also:
- PDF Color Spaces Documentation
- Syncfusion PDF SDK Documentation

<!-- tags: pdf, color spaces, CalGray, Lab, ICCBased, Syncfusion Winforms, version:11.4.0.26 -->  
```