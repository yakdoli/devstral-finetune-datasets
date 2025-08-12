```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_332.jpeg
document_name: pdf
page_number: 332
page_id: pdf#page_332
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:44:05Z
fidelity: lossless
-->

## Essential PDF

The following are the list of unsupported elements, which will not be preserved in the generated PDF document.

- Shapes and AutoShapes
- Comments
- Hyperlinks
- Bookmarks
- Footnotes and Endnotes
- Dynamic Fields
- Charts
- Table of Contents

### Known Limitations - Pagination

**Pagination**  
Essential DocIO, when generating the PDF document, makes sensible decisions while laying out the text and its supported elements. However, pagination is not guaranteed with all the documents.

## 4.4.5 XPS to PDF

An XPS (XML Paper Specification) document, standardized by Ecma International, can be now converted to PDF.

The XPS document format consists of XML structured markup that defines the layout of a document and the visual appearance of each page, along with rendering rules for distributing, archiving, rendering, processing, and printing the documents. Similar to PDF, XPS is also a fixed-layout document format which helps to preserve document fidelity and to achieve device-independent document appearance.

XPS documents can be converted to PDF using the `Convert` method of the `XPSToPdfConverter` class.

**Note:** You need to add the `Syncfusion.XPS` namespace to work with the `XPSToPdfConverter` class.

### Syntax

```csharp
[Export("Convert")]
public PdfDocument Convert(byte[] file);
public PdfDocument Convert(string fileName);
public PdfDocument Convert(Stream file);
```

```html
<!-- tags: [Syncfusion Winforms, XPS, PDF, XPSToPdfConverter, Essential DocIO] keywords: [XPS to PDF, XML Paper Specification, document conversion, fixed-layout document format, Syncfusion.XPS namespace, essentialdocio, pagination limitations] -->
```