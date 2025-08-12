```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_274.jpeg
document_name: pdf
page_number: 274
page_id: pdf#page_274
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:47Z
fidelity: lossless
-->

# Essential PDF

```csharp
foreach (PdfLoadedPage lpage in loadedPages)
{
    PdfImageInfo[] info = lpage.ImagesInfo;
    foreach (PdfImageInfo information in info)
    {
        RectangleF location = information.Bounds;
    }
}
```

## Overview
- The provided code snippets illustrate the use case for the `PdfLoadedPage` and `PdfImageInfo` APIs in handling images in a PDF document.

### Image Replacement Example

This example demonstrates how to replace an image within a PDF document.

```csharp
PdfLoadedDocument doc = new PdfLoadedDocument(@"imageDoc.pdf");
PdfBitmap bmp = new PdfBitmap(@"Water lilies.jpg");
doc.Pages[0].ReplaceImage(1, bmp);
doc.Save("Replace Sample.pdf");
System.Diagnostics.Process.Start("Replace Sample.pdf");
```

### Image Extraction Example

This example shows how to extract images from a PDF document and save them as individual files.

```csharp
// Load an existing PDF
PdfLoadedDocument ldoc = new PdfLoadedDocument(txtUrl.Text);

// Loading Page collections
PdfLoadedPageCollection loadedPages = ldoc.Pages;
int page = 0;

// Extract Image from PDF document pages
foreach (PdfLoadedPage lpage in loadedPages)
{
    PdfImageInfo[] info = lpage.ImagesInfo;

    if (info != null)
        foreach (PdfImageInfo information in info)
            information.Image.Save("Image" + page.ToString() + information.Bounds.ToString() + ".png", ImageFormat.Png);
    page++;
    Image image = info[0].Image;
    image.Save("test.png");
}
```

## Summary
- The provided code snippets illustrate the functionality to extract and replace images in a PDF document using Syncfusion Winforms APIs.
- These examples are useful for handling PDF documents programmatically, specifically for tasks involving image manipulation.

<!-- tags: [Syncfusion Winforms, PdfLoadedPage, PdfImageInfo, Image Manipulation, Version 11.4.0.26] keywords: [PdfLoadedPage, PdfImageInfo, Syncfusion Winforms, Programmatic Image Manipulation, PDF Document Handling] -->
```