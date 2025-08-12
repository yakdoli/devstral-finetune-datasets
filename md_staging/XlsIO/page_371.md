```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_371.jpeg
document_name: XlsIO
page_number: 371
page_id: XlsIO#page_371
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:03Z
fidelity: lossless
-->

## Overview
- Preserves Excel sheet Page Setup options, including Orientation and Center On Page.
- Supports Unicode and other languages.
- Preserves background images with tiling based on the PDF document size.
- Keeps comments present in Excel cells.
- Handles encrypted Excel documents with password protection.

## Content

### Excel sheet Page Setup options
The Page setup option of the input Excel sheet will be preserved in the generated PDF document. The following are the Excel page setup options that are preserved.
- Orientation
- Center On Page

### Unicode Support
The other language and unicode present in the input Excel document will be preserved in the generated PDF document.

### Background Images
The Background image present in the Excel document will be preserved in the generated PDF document.

**Note:** The image will be get tiled based on the size of the output pdf document.

### Comments
Comments present in the Excel document cells will also be preserved in the generated PDF document.

### Encryption
An encrypted Excel document will also be preserved and generated as an encrypted PDF document by passing the password for the encrypted Excel document.

### Unsupported Elements
The following list contains unsupported elements that presently will not be preserved in the generated PDF document.
- Shapes and auto-shapes
- Charts
- Grouping columns
- OLE Objects
- Text rotations
- Background images

### Printing Titles when Converting the Excel to PDF
Title rows and columns in the Excel sheet can be printed on the PDF page, using this feature. By setting the print titles for rows and columns in the Excel sheet, the same will get reflected in the PDF when converting the Excel to PDF.

### Page Break Support

## Page-level Navigation/TOC
- [Unclear]
<!-- tags: [XlsIO, page setup, unicode support, background images, comments, encryption, unsupported elements, printing titles, page breaks, Excel, PDF conversion, Syncfusion Winforms] keywords: [Excel sheet, Page Setup options, Unicode, Background images, Comments, Encryption, Unsupported elements, Printing Titles, Page Break Support, PDF document, document conversion] -->
```