```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_316.jpeg
document_name: DocIo
page_number: 316
page_id: DocIo#page_316
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:06Z
fidelity: lossless
-->

## Overview
- Compares features supported by "Doc" format and Microsoft Word versions 2007, 2010, and 2013 for read and write operations.
- Highlights capabilities such as auto shapes, document variables, encryption, mail merge, OLE objects, hyperlinks, view setup, line numberings, styles, and document properties.

## Content

### Feature Comparison Table

Below is a detailed comparison of various elements supported in the "Doc" format and Microsoft Word (2007, 2010, and 2013) for both reading and writing operations.

| Element                     | **Doc**        | **Word 2007 / Word 2010 / Word 2013** |
|-----------------------------|----------------|------------------------------------------|
|                             | **Read**       | **Write**                               | **Read**       | **Write**                               |
|-----------------------------|----------------|------------------------------------------|----------------|------------------------------------------|
| Auto shapes                 | Yes            | No                                      | Yes            | No                                      |
| Document variables          | Yes            | Yes                                     | Yes            | Yes                                     |
| Encryption and Decryption   | Yes            | Yes                                     | Yes            | Yes                                     |
| Chart                       | No             | No                                      | No             | No                                      |
| Mail merge                  | Yes            | Yes                                     | Yes            | Yes                                     |
| OLE object                  | Yes            | Yes                                     | Yes            | Yes                                     |
| Hyperlinks                  | Yes            | Yes                                     | Yes            | Yes                                     |
| View Setup                  | Yes            | Yes                                     | Yes            | Yes                                     |
| Line numberings             | Yes            | Yes                                     | Yes            | Yes                                     |
| Built-in Styles (Paragraph and Character styles) | Yes            | Yes                                     | Yes            | Yes                                     |
| Custom Styles (Paragraph and Character styles) | Yes            | Yes                                     | Yes            | Yes                                     |
| Document Properties         | No             | No                                      | Yes            | Yes                                     |

### Analysis
- **Auto shapes**: Readable in both formats but writeable only in Word.
- **Document variables**: Fully supported in both read and write in both formats.
- **Encryption and Decryption**: Both reading and writing are supported in all formats.
- **Chart**: Neither read nor write is supported in any of the formats.
- **Mail merge**: Fully supported for both read and write.
- **OLE object**: Reads and writes are supported across all formats.
- **Hyperlinks**: Supported for both operations in all formats.
- **View Setup**: Fully supported in all features and formats.
- **Line numberings**: Supported for both reading and writing in all.
- **Built-in Styles and Custom Styles**: Full support for both read and write operations.
- **Document Properties**: Only supported in reading and writing in Word, not in the "Doc" format.

## API Reference
This section is intentionally left blank as there are no specific APIs referenced in the provided content.

## Code Examples
This section is intentionally left blank as there are no specific code examples provided in the content.

## Page-level Navigation/TOC
This section is intentionally left blank as there is no Table of Contents present on this page.

## Cross References
See also:
- Related documentation on Microsoft Word file formats
- Information on document encryption and decryption
- Support for OLE objects and hyperlinks in document processing

## RAG Annotations
<!-- tags: DocIO, Syncfusion, Word, Document Processing, File Formats, Microsoft Word, Document Management keywords: Doc, Word 2007, Word 2010, Word 2013, Auto shapes, Document variables, Encryption, Mail merge, OLE object, Hyperlinks, View Setup, Line numberings, Built-in Styles, Custom Styles, Document Properties -->

```