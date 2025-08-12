```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_226.jpeg
document_name: pdf
page_number: 226
page_id: pdf#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:40Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Specifies the quality of Metafile images.
- Creates a metafile image and sets its quality.

## Code Example: Creating and Setting Metafile Quality

```vb
' Specify the quality of Metafile image
' Create metafile image
Dim metafile As PdfMetafile = DirectCast(PdfImage.FromImage(img), PdfMetafile)
' Specify the quality of the metafile
metafile.Quality = 50
```

## Content

### Drawing PNG Image

The following image illustrates how a PNG image is rendered in a PDF document. The image discusses creating and specifying the quality of a metafile image using the `PdfMetafile` class.

![Drawing PNG Image](https://i.imgur.com/Figure_40.png)

*Figure 40: Drawing PNG Image*

## RAG Annotations

<!-- tags: [pdf, image, metafile, quality, adobe reader] keywords: [PNG, PDFImage, PdfMetafile, DirectCast, Quality, Specify] -->
```