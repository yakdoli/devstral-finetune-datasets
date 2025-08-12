```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_335.jpeg
document_name: pdf
page_number: 335
page_id: pdf#page_335
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:27Z
fidelity: lossless
-->

## Essential PDF

### Feature Overview Table

| Feature            | Availability |
|--------------------|--------------|
| SignatureDefinitions | No          |
| SigningLocation     | No          |
| SolidColorBrush     | Yes         |
| SpotLocation        | No          |
| Story               | No          |
| TableStructure      | No          |
| VisualBrush        | No          |

### 4.4.6 Tutorial

This tutorial will show you how easy it is to get started using Essential PDF. It will give you a basic introduction to the concepts you need to know before getting started with the product and some tips and ideas on how to implement PDF into your projects. The lessons in this tutorial are meant to introduce you to PDF with simple step-by-step procedures.

**Note:** Refer to the Class Reference documentation for comprehensive information on the classes.

#### 4.4.6.1 Importing

The integrated HTML to PDF Converter is implemented by using the `HtmlConverter` class. It basically includes the functionality of the HTML to PDF Converter product, and additionally offers the possibility to specify the position and the size of the PDF content.

The following code example illustrates this.

```csharp
[C#]
// Convert web page into image.
HtmlConverter html = new HtmlConverter();
Image img = html.ConvertToImage("www.syncfusion.com", ImageType.Metafile, 1024);

// Draw the image into the PDF document as metafile
// Create metafile image
PdfMetafile metafile = (PdfMetafile)PdfImage.FromImage(img);

// Specify the quality of the metafile
metafile.Quality = 100;
```

### API Reference

#### HtmlConverter Class
- `ConvertToImage(string url, ImageType type, int dpi)`
  - Converts the specified web page into an image.
  - **Parameters:**
    - `url`: The URL of the web page to convert.
    - `type`: The type of image to create.
    - `dpi`: The resolution of the image in dots per inch.
  - **Returns:** An `Image` object representing the web page.

#### PdfMetafile Class
- `Quality`
  - Sets the quality of the metafile image.
  - **Type:** `int`

### Code Examples

#### Converting HTML to PDF Image

```csharp
[C#]
// Convert web page into image.
HtmlConverter html = new HtmlConverter();
Image img = html.ConvertToImage("www.syncfusion.com", ImageType.Metafile, 1024);

// Draw the image into the PDF document as metafile
// Create metafile image
PdfMetafile metafile = (PdfMetafile)PdfImage.FromImage(img);

// Specify the quality of the metafile
metafile.Quality = 100;
```

<!-- tags: [Essential PDF, HtmlConverter, PdfMetafile, Importing, C#] keywords: [HTML to PDF, Convert to Image, Metafile, Quality, PdfImage, PdfMetafile] -->
```