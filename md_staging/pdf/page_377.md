```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_377.jpeg
document_name: pdf
page_number: 377
page_id: pdf#page_377
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:24Z
fidelity: lossless
-->

# Essential PDF

## Content

### How To Extract Images From an Existing PDF Document?

You can extract images from an existing PDF document page by page, using the `ExtractImages` method of the `PdfLoadedPage` class. The following code example illustrates how to extract images from a document.

#### Code Example: C#

```csharp
// Load an existing PDF
PdfLoadedDocument ldoc = new PdfLoadedDocument("Sample.pdf");

// Loading Page collections
PdfLoadedPageCollection loadedPages = ldoc.Pages;

// Extract Image from PDF document pages
foreach (PdfLoadedPage lpage in loadedPages)
{
    Image[] img = lpage.ExtractImages();
    foreach (Image img1 in img)
    {
        img1.Save("Image" + Guid.NewGuid().ToString() + ".png", ImageFormat.Png);
    }
}
```

#### Code Example: VB.NET

```vb
' Load an existing PDF
Dim ldoc As PdfLoadedDocument = New PdfLoadedDocument("Sample.pdf")

' Loading Page collections
Dim loadedPages As PdfLoadedPageCollection = ldoc.Pages
```

## Footer
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [Syncfusion, Essential PDF, Image Extraction, PdfLoadedPage, Visio, ExtractImages, C#, VB.NET, DocumentLoadInfo, Syncfusion.Windows.Forms, Syncfusion.Windows.Forms.Grid] keywords: [PDF, Image Extraction, Syncfusion, Essential PDF, Visio, C#, VB.NET, ExtractImages, PdfLoadedPage, Syncfusion Winforms, Syncfusion.Windows.Forms.Grid] -->
```