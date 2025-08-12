```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: XlsIO
page_number: 106
page_id: XlsIO#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:38Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Compares support for various Excel elements in Xls (Excel 97 to 2003) and Xlsx (Excel 2007 and Excel 2010) formats.
- Details the capability of reading, writing, and preserving features in both formats.

## Content

### Comparison of Features in Xls and Xlsx Formats

| Element            | xls     | xlsx    | xls to xlsx |
|--------------------|---------|---------|-------------|
|                    | Read    | Write   | Preserve    | Read   | Write   | Preserve   |            |
| Algorithm          |         |         |             |        |         |             |            |
| Ole Objects        | No      | No      | No          | No     | No      | No         | No         |
| Track changes      | No      | No      | No          | No     | No      | No         | No         |
| Themes             | -       | -       | -           | Yespartial | No      | Yespartial | -         |
| Cell gradient      | -       | -       | -           | Yes    | Yes     | Yes        | -         |
| Advanced CF [icon, databars, Color scales] | -       | -       | -       | Yes    | Yes     | Yes        | -         |
| Tables             | No      | No      | No          | Yes    | Yes     | Yes        | No        |
| RGB colors         | Yes     | Yes     | Indexed color | Yes    | Yes     | Yes        | Yes       |
| OLE Objects        | No      | No      | Yes (Full Trust Only) | Yes (Full Trust Only) | No      | No         | No        |

---

### 3.10.2 Silverlight

The list of various supported and non-supported Excel elements of Essential XlsIO in Silverlight platform is given in the following table. Xls represents Excel 97 to 2003 format and XLSX represents both Excel 2007 and Excel 2010 file formats.

## Page-level Navigation/TOC (if applicable)
- If applicable, this section provides a local Table of Contents for the page, including links to other sections on this page.

## Cross References
- No specific cross-references are visible in the provided image.

## RAG Annotations
<!-- tags: [xlsio, excel elements, xlsx, xls, silverlight, file formats] keywords: [xls, xlsx, silverlight, essential xlsio, ole objects, track changes, themes, cell gradient, advanced conditional formatting, tables, rgb colors, ole objects, reading, writing, preserving] -->
```