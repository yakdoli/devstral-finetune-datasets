```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: DocIo
page_number: 245
page_id: DocIo#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:32Z
fidelity: lossless
-->

## HTML Element Attributes Supported in Essential DocIO

### Overview
- Summary of the supported HTML elements, their style attributes, non-style attributes, and any limitations.
- Details on the attributes supported by each HTML element, including spacing, alignment, and dimension attributes.
- Clarification on the limitations, such as partial image path support for the `img` element.

### HTML Element Attributes Table

| **HTML Element** | **Style Attributes specific to this element (In addition to standard style attributes)** | **Non-Style Attributes supported (These attributes are applied directly to the element)** | **Limitations**                          |
|-------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------|
| `td`             | width, vertical-align                                            | width, rowspan, colspan, align, valign                                | -                                      |
| `th`             | width, vertical-align                                            | width, rowspan, colspan, align, valign                                | -                                      |
| `tr`             | -                                                                  | height, align                                                            | -                                      |
| `tt`             | -                                                                  | -                                                                      | -                                      |
| `u`              | -                                                                  | -                                                                      | -                                      |
| `ul`             | -                                                                  | -                                                                      | -                                      |
| `img`            | -                                                                  | height, width, src, align                                              | Currently Partial Image path is not supported. |
| `div`            | -                                                                  | -                                                                      | -                                      |

### Explanation of Columns

#### HTML Element
- Lists the specific HTML element that is being described.

#### Style Attributes specific to this element
- Lists attributes that can be applied directly to the element for styling purposes, in addition to standard CSS style attributes.

#### Non-Style Attributes supported
- Lists attributes that are applied directly to the element but are not related to styling. These include attributes like alignment, dimensions, and structural properties.

#### Limitations
- Indicates any constraints or unsupported features related to the use of the element, such as partial support for image paths.

### Page-level Navigation/TOC
- This page provides a detailed list of supported HTML elements and their attributes in the context of DocIO.

### Related References
- Refer to the main documentation for more detailed information about the usage and limitations of HTML elements in Syncfusion Winforms applications.

### RAG Annotations
<!-- tags: html_element, attributes, style_attributes, non_style_attributes, limitations, DocIO, Essential DocIO, Syncfusion Winforms keywords: html, attributes, style, width, height, alignment, image path, partial support -->
```