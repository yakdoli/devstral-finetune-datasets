```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_315.jpeg
document_name: DocIo
page_number: 315
page_id: DocIo#page_315
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:13Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Comparison of supported elements between various document formats like Doc and Word 2007/2010/2013.
- Features such as paragraph borders, bullets, lists, background color, and fill effect are consistently supported across formats.

## Content

### Feature Comparison Table

| Element                     | Doc             | Word 2007 / Word 2010 / Word 2013 |
|-----------------------------|------------------|------------------------------------|
| **Paragraph border**        | **Read**        | **Read**                          |
|                             | **Write**       | **Write**                         |
| **Bullets and lists**      | **Yes**         | **Yes**                           |
| **Background Color**       | **Yes**         | **Yes**                           |
| **Fill effect and Watermark** | **Yes**       | **Yes**                           |
| **Table with formatting**   | **Yes**         | **Yes**                           |
| **Table styles**           | **No**          | **No**                            |
| **Form field objects**     | **Yes**         | **Yes**                           |
| **Header/Footer with images** | **Yes**    |                                    |
| **Drawing Objects**        | **Yes**         | **Yes Limited [Cannot create new container]** |
| **Page Setup**             | **Yes**         | **Yes**                           |
| **Hyperlink**              | **Yes**         | **Yes**                           |
| **Font Settings**          | **Yes**         | **Yes**                           |
| **Paragraph Settings**     | **Yes**         | **Yes**                           |
| **Border and Shading**     | **Yes**         | **Yes**                           |
| **Textbox**                | **Yes**         | **Yes**                           |
| **Text direction**         | **Yes**         | **Yes**                           |
| **Theme settings**         | **Yes**         | **No**                            |
| **Track changes**          | **Yes**         | **Yes – limited [can only accept/reject]** |
| **Macros**                 | **No**          | **No**                            |

## Notes
- The table above provides a detailed comparison of which elements can be read and written in different document formats.
- Note that some elements like "Table styles" and "Macros" are not supported across all formats, and "drawing objects" have limitations.

## API Reference
- This page provides a reference for the capabilities of `DocIo` in handling different document features and formats.

## Code Examples
```csharp
// Example: Performing read/write operations on a Word document
using Syncfusion.DocIO;

Document document = new Document();
// ... further operations to add elements to the document
```

## Page-level Navigation/TOC
- This page is part of the `DocIo` documentation, focusing on the comparison of document features across formats.

## Cross References
- This section can reference other pages in the `DocIo` documentation or related `Syncfusion Winforms` features.

## RAG Annotations
<!-- tags: DocIo, document formats, Word, document features, Read/Write capabilities, Syncfusion Winforms, version: 11.4.0.26 keywords: paragraph border, bullets and lists, background color, fill effect, table formatting, form field objects, header/footer, drawing objects, page setup, hyperlink, font settings, paragraph settings, border and shading, textbox, text direction, track changes, macros -->
```