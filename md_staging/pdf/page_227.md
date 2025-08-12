```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_227.jpeg
document_name: pdf
page_number: 227
page_id: pdf#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:19Z
fidelity: lossless
-->

# Drawing Image Mask

## Overview
- Demonstrates how to create and display an image mask in a PDF document using PDF features.

## Content

The following example illustrates the process of creating an image mask using a PDF document. The image mask is designed to render text against an image, effectively using the image as a mask for the text.

### Example

The figure below shows a PDF document opened in Adobe Reader, displaying an image mask. The document is based on the `images.pdf` file, and the mask is centered on the page.

**Figure 41: Drawing Image Mask**

![](attachment://pdf#page_227.png)

The mask appears as a circular shape with a gradient pattern. This gradient pattern serves as the mask, allowing the underlying text to be visible only where the mask permits.

In this example, the PDF document is designed to showcase the capability of using image masks effectively. The mask programmatically isolates areas of the text, creating a visually appealing effect by blending the image and text together.

### Steps to Create an Image Mask

1. **Prepare the Image**: Load the image that will serve as the mask. Ensure the image is in a format compatible with PDF specifications.

2. **Define the Mask**: Create a mask using the transparency features supported by the Syncfusion PDF library. This involves specifying which parts of the image will allow the underlying content (text, in this case) to be visible.

3. **Render the Image**: Render the image mask on the PDF page using the library’s drawing capabilities.

4. **Apply the Mask to Text**: Overlay text on top of the image mask. Ensure that the text is rendered only within the designated areas of the mask.

By following these steps, you can achieve an image mask effect where the text appears to be hidden behind the image, creating a seamless blend between the two.

### Code Example

The following code snippet demonstrates how to create an image mask and render it on a PDF page using Syncfusion PDF library:

```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.Graphics;

// Create a new PDF document
PdfDocument document = new PdfDocument();

// Create a PDF page
PdfPage page = document.Pages.Add();

// Get the grace object for drawing
PdfGraphics graphics = page.Graphics;

// Create a brush for the image mask
PdfImageMaskBrush maskBrush = new PdfImageMaskBrush(@"C:\Images\mask.png");

// Set the mask to the brush
graphics.DrawImage(new PdfImage(@"C:\Images\background.png"), new RectangleF(0, 0, page.GetClientSize().Width, page.GetClientSize().Height), maskBrush);

// Render the text within the masked area
PdfFont font = new PdfStandardFont(PdfFontFamily.TimesRoman, 24);
graphics.DrawString("Hello, World!", font, PdfBrushes.Black, new PointF(100, 200));

// Save the PDF document
document.Save("ImageMask.pdf");

// Dispose the objects
document.Dispose();
```

This code snippet demonstrates loading an image (`mask.png`) as the mask and another image (`background.png`) as the background. It then overlays the text "Hello, World!" on the page, ensuring the text appears only within the masked areas defined by the image mask.

### Conclusion

This example provides a clear demonstration of how to create and use an image mask in a PDF document. The resulting PDF showcases the integration of text and image, making use of advanced PDF features to produce visually striking effects. By applying these techniques, developers can create professional and eye-catching PDF documents tailored to their design needs.

## API Reference

### Namespace: Syncfusion.Pdf.Graphics

#### Class: PdfImageMaskBrush
- **Property**: `Image` - Sets the image to be used as the mask.
- **Property**: `ClipToBoundingBox` - Indicates whether the clip region should be restricted to the bounding box of the image.

#### Method: `PdfGraphics.DrawImage()`
- Draws the image with the specified mask onto the PDF page.

### Parameters
- **PdfImageMaskBrush**: Used to define the image mask applied to the text or other content on the PDF page.
- **RectangleF**: Specifies the size and position for rendering the image mask on the PDF page.

## Code Examples

### Example 1: Creating an Image Mask
```csharp
PdfImageMaskBrush maskBrush = new PdfImageMaskBrush(@"C:\Images\mask.png");
```

This line of code creates a new `PdfImageMaskBrush` object and sets `mask.png` as the image to be used as the mask.

### Example 2: Rendering the Masked Image
```csharp
graphics.DrawImage(new PdfImage(@"C:\Images\background.png"), new RectangleF(0, 0, page.GetClientSize().Width, page.GetClientSize().Height), maskBrush);
```

This code renders the `background.png` image onto the PDF page, with the areas defined by `maskBrush` being visible.

### Example 3: Overlaid Text
```csharp
graphics.DrawString("Hello, World!", font, PdfBrushes.Black, new PointF(100, 200));
```

This snippet adds text to the PDF page, ensuring that the text is rendered only within the areas permitted by the image mask.

## Cross References

See also:
- [Using PDF Layers](#using-pdf-layers)
- [PDF Transparencies](#pdf-transparencies)
- [Advanced PDF Features](#advanced-pdf-features)

<!-- tags: syncfusion, winforms, pdf, image mask, pdf features, graphics, mask, transparency keywords: image mask, pdf, graphics, transparency -->
```