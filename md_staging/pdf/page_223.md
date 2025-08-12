```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_223.jpeg
document_name: pdf
page_number: 223
page_id: pdf#page_223
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:05Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This section explains how to work with shapes and images in PDF documents using Essential PDF, specifically focusing on custom drawing and loading images.

## Content

### Drawing Shapes
**Figure 39: PDF Document drawn with Shapes**  
The image displays a PDF document containing shapes such as:
- Pie shape
- Simple rectangle
- Shape with pagination
- Ellipse with Gradient
- Transparent rectangles

### 4.1.7.3 Drawing Images

Essential PDF consists of a comprehensive set of APIs that are used to create Adobe PDF documents with text and rich graphics including custom drawing and images. It also has support for loading images from the following objects:
- Streams
- Files on disk
- System.Drawing.Bitmap

You can resize and insert images into the PDF document at the required size, and specify the image quality by using the **Quality** property.

## API Reference (if applicable)
- **Namespace**: Syncfusion.Pdf
- **Class**: PdfDocument
- **Methods/Properties**:
  - `PdfImage LoadImage(Stream stream)`
  - `PdfImage LoadImage(string filePath)`
  - `PdfImage LoadImage(System.Drawing.Bitmap bitmap)`
  - `PdfImage Quality`

## Code Examples (multi-language supported)
```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.Graphics;

// Create a new PDF document
PdfDocument doc = new PdfDocument();

// Create a page
PdfPage page = doc.Pages.Add();

// Set up the graphics for the page
PdfGraphics graphics = page.Graphics;

// Load an image from a file
PdfImage image = PdfImage.LoadImage("image.jpg");

// Resize the image
image.Height = 200;
image.Width = 200;

// Draw the image on the page
graphics.DrawImage(image, new PointF(100, 100));

// Set image quality
image.Quality = 90;

// Save the PDF document
doc.Save("output.pdf");

// Close the document
doc.Close(true);
```

## Page-level Navigation/TOC (if applicable)
- 4.1.7.3 Drawing Images

## Cross References
- Refer to the **API Reference** section for details on methods and properties related to image handling.

## RAG Annotations
<!-- tags: [pdf, essential pdf, drawing shapes, drawing images, custom drawing, image quality, pdf document] keywords: [shapes, images, custom drawing, image quality, streams, file on disk, System.Drawing.Bitmap] -->
```