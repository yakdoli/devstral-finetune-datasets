```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_331.jpeg
document_name: pdf
page_number: 331
page_id: pdf#page_331
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:14Z
fidelity: lossless
-->

## Overview
- Support for simple and nested tables with proper text formatting and images in cells.
- Known limitations related to patterned borders and absolute positioning of tables.
- Support for columns, section, line, and page breaks.
- Partial support for OLEObjects, with the associated object not converting.
- Rendering of text box content in its actual position.
- Preservation of page settings, including size, orientation, and background images.
- Preservation of document properties in Word documents.

## Content

### Tables

Both simple and nested tables are supported with proper preservation of text formatting and images present inside the table cell.

#### Known Limitations
- Tables making use of patterns and 3D borders will not be retained in the output document.
- Absolutely positioned tables are not supported.

### Breaks

Columns, section, line, and page breaks are fully supported.

### OLEObject

OLEObjects are partially supported, i.e., the image, which represents a particular document that will be available in the generated PDF document. But the object associated with the object will not be converted into the generated document.

### Text Box

The text value present in the text box will be rendered as text in its actual position in the generated PDF document.

### Page Settings

The actual page settings will be preserved in the generated PDF document which includes page size, orientation, page borders and its background image, if available.

### Document Properties

The document properties present in the Word document will also be preserved in the generated PDF Document.

---

## Unsupported Elements

There are no additional details mentioned about unsupported elements in this section.

### Notes

The document notes that certain features are not supported, but no specific unsupported elements are listed beyond the known limitations.

---

## Copyright Notice

© 2013 Syncfusion. All rights reserved.

## RAG Annotations
<!-- tags: [tables, breaks, oleobjects, text_box, page_settings, document_properties, unsupported_elements] keywords: [simple_tables, nested_tables, patterned_borders, absolute_positioning, columns, section_breaks, line_breaks, page_breaks, oledocument, text_position, page_size, orientation, background_images, word_document_properties] -->
```