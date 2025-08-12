```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_327.jpeg
document_name: pdf
page_number: 327
page_id: pdf#page_327
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:03Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Example demonstrating how to load and extract text from a PDF document.
- Highlighting the use of the `PdfLoadedDocument` and `PdfLoadedPage` classes.
- Instructions on extracting images using the `ExtractImages` method.

## Content

### 4.4.3 Image Extraction

Essential PDF provides support to extract images from an existing PDF document. You can extract images by using the **ExtractImages** method in the **PdfLoadedPage** class.

The following code example illustrates how to extract images from a PDF document.

#### C#
```csharp
// Load an existing PDF
PdfLoadedDocument ldoc = new PdfLoadedDocument("Sample.pdf");

// Loading first page
PdfLoadedPage page = ldoc.Pages[0];

// Extract images from first page
Image[] img = page.ExtractImages();
```

#### VB.NET
```vb
' Load an existing PDF
Dim ldoc As PdfLoadedDocument = New PdfLoadedDocument("Sample.pdf")

' Loading first page
Dim page As PdfLoadedPage = ldoc.Pages(0)

' Extract images from first page
Dim img As Image() = page.ExtractImages()
```

### Note
The note indicates that the text will be extracted in the order in which it is written in the document stream. It is not in the order in which it is viewed in the PDF viewer.

```html
<!-- 
tags: [Essential PDF, Text Extraction, Image Extraction, Syncfusion, Winforms]
keywords: [PdfLoadedDocument, PdfLoadedPage, ExtractText, ExtractImages]
--> 
```