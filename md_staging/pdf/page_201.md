```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_201.jpeg
document_name: pdf
page_number: 201
page_id: pdf#page_201
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:26Z
fidelity: lossless
-->

# Essential PDF

## Overview
- ISO 19005-1 Level B conformance (PDF/A-1b) ensures the visual appearance of a document is preservable over the long term.
- ISO 19005-1 Level A conformance (PDF/A-1a): It builds on Level B, adding crucial properties from Tagged PDF. PDF/A-1a requires structure information and reliable text semantics to preserve the document's logical structure and natural reading order.

## Content

### PDF/A-1b

Creating a PDF/A-1b document is straightforward. You must set `PdfConformanceLevel` to `PdfA1B` while creating a PDF document. PDF/A standard imposes certain restrictions on the usage of color, fonts, annotations, and other elements. These restrictions include:

- The use of JavaScript is forbidden.
- Attaching any file to a PDF document is prohibited.
- Hyperlinking to a non-PDF file is forbidden.
- Security features are not allowed.
- The use of Form Fields is forbidden.
- Text containing HTML tags is forbidden.
- Supports TrueType fonts only; does not support Type1 font.
- Supports the use of RGB color only; does not support CMYK color.

### Validating PDF/A-1b

Adobe Acrobat's Preflight tool is utilized to ensure compliance of a PDF document with the PDF/A standard. To verify compliance, you can use the Preflight tool from the menu: select `Advanced > Preflight > PDF/A compliance > Verify compliance with PDF/A-1b`.

#### Example Code: Creating PDF/A-1b Compliant Output

```csharp
// Create a new document with PDF/A standard.
PdfDocument doc = new PdfDocument(PdfConformanceLevel.Pdf_A1B);
```

### Notes
- **Note:** PDF/A-1a and PDF/A-1b differ primarily with respect to text extraction.
```html

<!-- tags: [syncfusion, winforms, pdf, pdf/a-1b, pdf/a-1a, pdf/a, pdf document, pdf conformance, adobe acrobat, validation, tagged pdf] keywords: [iso 19005-1, pdf/a, level b, level a, restriction, text extraction, javascript, security features, html tags, true type fonts, cmyk color, rgb color, adobe acrobat, preflight tool, advanced menu, syntax highlight] -->
```