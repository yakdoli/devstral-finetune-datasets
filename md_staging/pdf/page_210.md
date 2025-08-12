```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_210.jpeg
document_name: pdf
page_number: 210
page_id: pdf#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:48Z
fidelity: lossless
-->

# Content Compression in PDFs

## Overview
- Just the data content, or
- Entire transmission unit.
- Details of how content compression operates in PDF documents.

## Content

### Content Compression

**Content compression involves the following:**

- **Removing all extra space characters**
- **Inserting a single repeat character to indicate a string of repeated characters**
- **Substituting smaller bit strings for frequently occurring characters**

### Advantages of Content Compression

- Reduces a text file to 50 percent of its original size.

**Note:** Compression is performed by a program that uses a formula or algorithm to determine how to compress or decompress data. The algorithm is one of the critical factors to determine the compression quality. This is elaborated below.

### Controlling the Compression Levels

Essential PDF controls the compression level of the document by using the `PdfCompressionLevel` class with the help of the LZW and zlib/deflate compression algorithms. Both LZW and Flate algorithms compress either binary data or ASCII text and always produce the binary data.

**The following compression levels are supported by Essential PDF:**

- **None**: Packs without compression
- **BestSpeed**: Performs high-speed compression; reduction of data size is lesser
- **BelowNormal**: Performs compression that is rated between Normal and BestSpeed compressions
- **Normal**: Performs compression at normal speed; normal reduction of data size
- **AboveNormal**: Performs enhanced compression compared to the normal compression; time consumption exceeds the normal compression
- **Best**: Performs the best compression; time consuming

### 4.1.7 Tutorial

This section guides users through setting compression levels and utilizing the PDF compression features in Syncfusion Winforms.

## References

- See also:
  - [Compression Algorithms in PDF](#compression-algorithms-in-pdf)
  - [PDF Compression in Essential PDF](#pdf-compression-in-essential-pdf)

<!-- tags: [pdf, compression, essential-pdf, syncfusion, winforms, version 11.4.0.26] keywords: [content compression, pdf compression, compression levels, essential pdf, winforms, data reduction, file size, pdf algorithms] -->
```