<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_063.jpeg
document_name: pdf
page_number: 063
page_id: pdf#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:00Z
fidelity: lossless
-->

# Essential PDF

## Overview

- This section describes the structure of a PDF document and its components in detail.
- It includes the hierarchical breakdown of elements within a PDF document.
- The image depicts the DOM (Document Object Model) structure of a PDF document.

## Content

### PDF Document Structure

The following image illustrates the hierarchical structure of a PDF document:

```plaintext
Document
├── Sections
│   ├── Pages
│   │   ├── Layers
│   │   ├── Graphics
│   │   ├── Annotations
│   │   ├── Page Settings
│   │   ├── Section Template
├── Document Information
│   ├── Xmp
├── Viewer Preferences
├── Document Template
├── Security
├── Actions
├── Bookmarks
├── Attachments
└── Form Fields
```

**Figure 25: DOM**

This illustration shows the structure of a PDF document in terms of its components and their relationships. Each component is interconnected, forming a comprehensive representation of a PDF document.

#### Components Explained

- **Document**: The root element that encapsulates all sections of the document.
- **Sections**: Logical divisions within the document.
- **Pages**: Individual pages contained within the sections.
  - **Layers**: Layers that can be displayed or hidden on a page.
  - **Graphics**: Graphical elements such as images and shapes.
  - **Annotations**: Notes, highlights, and stamps added to the document.
  - **Page Settings**: Settings related to the layout and appearance of a page.
  - **Section Template**: Template used for structuring sections.
- **Document Information**: Metadata related to the document.
  - **Xmp**: Extensible Metadata Platform (XMP) data.
- **Viewer Preferences**: Settings to control the viewer's behavior.
- **Document Template**: Template used for generating the document.
- **Security**: Security settings for restricting access to the document.
- **Actions**: Actions that can be triggered when certain events occur.
- **Bookmarks**: Navigation bookmarks for easier document navigation.
- **Attachments**: Files attached to the document.
- **Form Fields**: Interactive form fields for user input.

## API Reference

This section provides details about the API used to manipulate PDF documents, but specific API references are not visible in the provided image. Developers can refer to the Syncfusion documentation for more details on using the API.

## Code Examples

The image does not include any code examples. However, developers can use Syncfusion’s Essential PDF API to work with PDF documents programmatically. Examples can be found in the official documentation or SDK samples.

## Page-level Navigation/TOC

- This page focuses on the DOM structure of a PDF document and its components.

## Cross References

- For more information on individual components and their usage, refer to specific sections in the Syncfusion documentation.

## RAG Annotations

<!-- tags: pdf, document structure, essential pdf, dom, document object model, syncfusion winforms keywords: pdf, document, structure, layers, graphics, annotations, page settings, document information, viewer preferences, security, actions, bookmarks, attachments, form fields, DOM, document object model -->

