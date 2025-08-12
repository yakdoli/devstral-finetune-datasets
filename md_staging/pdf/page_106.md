```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: pdf
page_number: 106
page_id: pdf#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:30:52Z
fidelity: lossless
-->

## Essential PDF

Using grayscale or monochrome images in PdfImageMask enables to create transparent images depending on the pixel format.

### Overview
- Soft Mask
- Hard Mask
- Image Quality

### PdfImageMask

#### Soft Mask
A soft mask specifies a transparency level for each pixel of the image. You can create these masks from a grayscale image. The level of gray indicates the level of transparency.

#### Hard Mask
A hard mask classifies pixels based on their transparency. You can create these masks from a monochrome image.

**Note:** Image masks should be of the same width and height as the base image.

### PdfColorMask
This mask enables masking colors (making them transparent) by specifying the range of colors. All colors that exist between the start color and the end color will be transparent.

**Note:** According to PDF References, it is recommended not to use JPEG images with color key masking.

### Image Quality
The **Quality** property is used to specify the quality value for images. An image can have its quality set from 0 through 100; 100 is the default value, which increases the resultant file size and quality. Reducing the quality of an image will reduce the corresponding file size.

This property is also used as an encoding parameter while saving an image to PDF format.

### Code Examples

#### C#
```csharp
//Setting the quality of the image.
PdfBitmap image = new PdfBitmap(fileName);
image.Quality = 80;
```

#### VB.NET
```vb
' Setting the quality of the image.
Dim image As New PdfBitmap(fileName)
image.Quality = 80
```

### API Reference
- **Property:** Quality
  - Description: Specifies the quality value for images.
  - Type: Integer
  - Range: 0 to 100
  - Default: 100

### Code Examples (Reiteration)
The sample code demonstrates setting the quality of an image to 80 in both C# and VB.NET.

---

<!-- tags: [Essential PDF, Image Transparency, Soft Mask, Hard Mask, Color Mask, Image Quality, PdfBitmap] keywords: [grayscale, monochrome, transparency level, grayscale image, monochrome image, mask, color key, file size] -->
```