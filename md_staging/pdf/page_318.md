```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_318.jpeg
document_name: pdf
page_number: 318
page_id: pdf#page_318
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:29Z
fidelity: lossless
-->

# Essential PDF

## Overview

- Converts HTML content to an image using the `FromString` method.
- Demonstrates how to render HTML as an image with various parameters like type, width, height, and aspect ratio.
- Includes both C# and VB.NET code examples for implementation.

## Content

### FromString

**FromString method** renders HTML from the string to an image. The following code example illustrates this:

#### C#

```csharp
public Image FromString(string html, ImageType type);
public Image FromString(string html, ImageType type, int width);
public Image FromString(string html, ImageType type, int width, int height);
public Image FromString(string html, ImageType type, int width, int height, AspectRatio aspectRatio);
```

#### VB.NET

```vbnet
Public Image FromString(String html, ImageType type)
Public Image FromString(String html, ImageType type, Integer width)
Public Image FromString(String html, ImageType type, Integer width, Integer height)
Public Image FromString(String html, ImageType type, Integer width, Integer height, AspectRatio aspectRatio)
```

### Sample code:

#### C#

```csharp
// Initialize the HTML converter
HtmlConverter converter = new HtmlConverter();
// Convert HTML to image
Image result = converter.FromString(html, ImageType.Metafile, (int)imgWidth, -1, AspectRatio.KeepWidth);

// Render the image in the PDF document
PdfImage pdfImage = PdfImage.FromImage(result);
pdfImage.Draw(pdfPage, PointF.Empty, format);
```

#### VB.NET

```vbnet
' Initialize the HTML Converter
Dim converter As New HtmlConverter()

' Convert the HTML file to Image
Dim result As Image = converter.FromString(htmlFilePath, ImageType.Metafile, CType(imgWidth, Integer), -1, AspectRatio.KeepWidth)

' Render the image in the Pdf document
```

## API Reference

### Methods

- **FromString**
  - **Parameters**:
    - `html`: `string` - The HTML content to convert.
    - `type`: `ImageType` - The type of the output image.
    - `width`: `int` - The width of the image.
    - `height`: `int` - The height of the image.
    - `aspectRatio`: `AspectRatio` - The aspect ratio to maintain.
  - **Returns**: `Image` - The rendered image.

## Code Examples

### C#

The provided C# example shows how to convert HTML content to an image and render it within a PDF document. This snippet demonstrates initializing the `HtmlConverter`, performing the conversion, and finally rendering the image.

### VB.NET

The VB.NET example mirrors the C# approach, initializing the converter, converting the HTML string to an image, and rendering it in the PDF document, maintaining consistency in functionality across languages.

## Cross References

- See also: Additional resources on HTML conversion and PDF rendering in the Syncfusion documentation.

<!-- tags: [PDF, conversion, image, Winforms, HTML, VB.NET, C#] keywords: [FromString, HtmlConverter, ImageType, AspectRatio, PdfImage] -->
```