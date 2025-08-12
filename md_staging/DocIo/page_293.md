```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_293.jpeg
document_name: DocIo
page_number: 293
page_id: DocIo#page_293
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:54Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- 1-3 bullets summarizing the page scope using only visible text.
- Overview of support for bulleted, numbered, and multi-level lists in generated PDF documents.
- Handling of images and tables within the document, including limitations and specific features for table styles.

## Content

### Bulleted, Numbered, and Multi-level Lists
![Figure 82: Bulleted, Numbered and Multi-level Lists](<image-reference>)

This figure illustrates the conversion process for bulleted, numbered, and multi-level lists from the source document to the generated PDF format.

### Images

The images present in the document are supported along with their corresponding positions and sizes.

**Known Limitations**:  
- However, the images placed inside a shape will not be preserved in the generated PDF document.

### Tables

Both simple and nested tables are supported with proper preservation of text formatting and images present inside the table cell. Text directions are also supported.

**Known Limitations**:
- Tables making use of patterns and 3D borders will not be retained in the output document.
- Absolutely positioned tables are not supported.

### Doc to PDF Conversion Support for Table Styles for Word 2007 and Word 2010 Documents

Support is now added for table styles in Doc to PDF conversion for Word 2007 and Word 2010 documents. During Doc to PDF conversion, Table-style support provides a unique look and feel to tables in the converted PDF documents, similar to the tables in Word documents.

## API Reference (if applicable)
- This section would typically include details about namespace, class, and members (if applicable).

## Code Examples (multi-language supported)
- This section would typically include examples in C#, VB, XML, or other relevant languages.

<!-- tags: [Syncfusion, Winforms, DocIO, Table styles, Images, Tables, List styles, PDF conversion] keywords: [DocIO, table styles, image preservation, nested tables, text formatting, 3D borders, absolutely positioned tables, document conversion, Word 2007, Word 2010] -->
```