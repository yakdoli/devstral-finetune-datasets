```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_291.jpeg
document_name: DocIo
page_number: 291
page_id: DocIo#page_291
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:47Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Converts Word documents to PDF using Syncfusion libraries.

### Dependencies

- Syncfusion.Pdf.Base.dll
- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll

### Code Examples

#### C#

```csharp
WordDocument wordDoc = new WordDocument("sample.doc");
DocToPDFConverter converter = new DocToPDFConverter();

// Convert word document into PDF document
PdfDocument pdfDoc = converter.ConvertToPDF(wordDoc);

// Save the pdf file
pdfDoc.Save("DoctoPDF.pdf");
```

#### VB.NET

```vb
Dim wordDoc As New WordDocument("sample.doc")
Dim converter As New DocToPDFConverter()

' Convert word document into PDF document
Dim pdfDoc As PdfDocument = converter.ConvertToPDF(wordDoc)

' Save the pdf file
pdfDoc.Save("DoctoPDF.pdf")
```

## Supported Elements

With the initial version of the feature, this feature provides support for the following elements.

- Paragraph and character formatting
- Multi-Column Texts
- Headers and Footers
- Bulleted, numbered and multi-level lists
- Images (both simple and nested)
- Tables (both simple and nested)
- Table styles for docx formats (Word 2007 and Word 2010 formats)
- Breaks (page, section, linebreak, etc)
- OLEObject
- Textbox
- Page Settings and background image
- Document Properties

## Page Footer

- **©** 2013 Syncfusion. All rights reserved.
- **291** | Page

<!-- tags: [DocIo, Word to PDF conversion, C#, VB.NET, Syncfusion.Pdf.Base.dll, Syncfusion.Core.dll, Syncfusion.Compression.Base.dll] keywords: [Word document, PDF document, DocToPDFConverter, paragraph formatting, multi-column texts, headers and footers, bulleted lists, numbered lists, multi-level lists, images, tables, OLEObject, textbox, page settings, document properties] -->
```