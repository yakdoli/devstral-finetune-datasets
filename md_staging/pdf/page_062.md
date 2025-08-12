```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: pdf
page_number: 062
page_id: pdf#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:27:42Z
fidelity: lossless
-->

## Content

### Overview

- A page inherits settings from its parent section.
- All pages within the same section have the same dimensions.
- Different page settings require creating a new section.
- Documents can specify page settings.
- New sections inherit settings from the parent document.
- Documents can be saved using the `Save` method.

### Details

A page does not contain any self-settings, but it inherits them from its parent section instead. It means that all the pages in the same section have the same dimensions. If a new page with different settings has to be created, then a new section should be created. A document also has capabilities to specify page settings. When a new section is created, it inherits page settings from the parent document.

#### Saving Documents

You can save a document either to a file or stream through its `Save` method.

<!-- tags: [document, save, page settings, section] keywords: [Syncfusion Winforms, document handling, page dimensions, inheritance, Save method, section settings] -->
```