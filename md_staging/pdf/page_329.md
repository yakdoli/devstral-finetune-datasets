```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_329.jpeg
document_name: pdf
page_number: 329
page_id: pdf#page_329
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:14Z
fidelity: lossless
-->

# Essential PDF

```csharp
// Convert word document into PDF document
PdfDocument pdfDoc = converter.ConvertToPDF(wordDoc);

// Save the pdf file
pdfDoc.Save("DoctoPDF.pdf");
```

### [VB.NET]

```vb
Dim wordDoc As New WordDocument("sample.doc")
Dim converter As New DocToPDFConverter()

' Convert word document into PDF document
Dim pdfDoc As PdfDocument = converter.ConvertToPDF(wordDoc)

' Save the pdf file
pdfDoc.Save("DoctoPDF.pdf")
```

## Supported Elements

This feature provides support for the following elements.

- Paragraph and Character Formatting
- MultiColumn Text
- Headers and Footers
- Bulleted, Numbered and MultiLevel Lists
- Images
- Tables (both simple and nested)
- Breaks (page, section, linebreak, etc.)
- OLEObject
- Text Box
- Page Settings and Background Image
- Document Properties

### Paragraph and Character Formatting

This feature supports almost all the paragraph formatting options except Full-Justification. The supported paragraph formatting options are as follows.

- Paragraph and Character Fonts
- Font styles (Bold, Italic, Underline and Strike through)
- Subscript and Superscript
- Paragraph and Text Highlighting
- Indents, tabs and spaces

```html
<!-- tags: [essential pdf, word document, pdf conversion, supported elements, formatting, paragraph, character, multi-column, headers, footers, lists, images, tables, breaks, oleobject, text box, page settings, background image, document properties] keywords: [word document conversion, pdf document, paragraph formatting, character formatting, multi-column text, headers and footers, bulleted lists, numbered lists, multi-level lists, images, tables, breaks, oleobject, text box, page settings, background image, document properties] -->
```