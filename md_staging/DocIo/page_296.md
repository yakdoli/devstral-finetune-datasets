```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_296.jpeg
document_name: DocIo
page_number: 296
page_id: DocIo#page_296
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:46Z
fidelity: lossless
-->

# Essential DocIO

## PageSettings

The actual page settings will be preserved in the generated PDF documents, which includes page size, orientation, page borders, and its background image if available.

## Document Properties

The document properties present in the word documents will also be preserved in the generated PdfDocument.

## Un-Supported Elements

The following are the list of un-supported elements, which will be supported in the future releases and will not be preserved in the generated PDF document.

- Shapes and auto shapes
- Comments
- Hyperlinks
- Bookmarks
- Foot note and end note
- Dynamic Fields
- Charts
- Table of Contents

## Known Limitations - Pagination

### Pagination

Essential DocIO makes sensible decisions while laying out the text, and its supported elements while generating the PDF documents. But however, we cannot guarantee pagination with all the documents.

### Note: Currently Doc to Pdf conversion is not supported in Silverlight application.

## 4.8.4 RTF to Doc

Essential DocIO allows to import the RTF document directly into the word document.

The following code illustrates how RTF file can be opened and saved as a word document.
```cs
The following code illustrates how RTF file can be opened and saved as a word document.
```

```html
<!-- tags: [DocIO, page settings, document properties, un-supported elements, pagination, limitations, RTF to Doc, conversion, Silverlight] keywords: [Essential DocIO, page size, orientation, page borders, background image, document properties, shapes, comments, hyperlinks, bookmarks, foot note, end note, dynamic fields, charts, table of contents, pagination, RTF document, word document] -->
```