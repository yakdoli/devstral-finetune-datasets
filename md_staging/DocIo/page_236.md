```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_236.jpeg
document_name: DocIo
page_number: 236
page_id: DocIo#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:26Z
fidelity: lossless
-->

## Overview
- This document explains the various alignment options available for setting the Horizontal and Vertical alignment of a picture in a document. It includes details about the `ShapeHorizontalAlignment` and `ShapeVerticalAlignment` types, along with their respective properties like `HorizontalOrigin` and `VerticalOrigin`.
  
## Content

### HorizontalAlignment
HorizontalAlignment returns an object of type, ShapeHorizontalAlignment. The following are the variants for setting the Horizontal alignment of a picture.

- **None**: no horizontal alignment
- **Left**: left horizontal alignment
- **Center**: center horizontal alignment
- **Right**: right horizontal alignment
- **Inside**: inside horizontal alignment
- **Outside**: outside horizontal alignment

### VerticalAlignment
VerticalAlignment returns an object of type, ShapeVerticalAlignment. The following are the variants for setting the Vertical alignment of a picture.

- **Bottom**: picture is aligned to the bottom of the reference origin
- **Center**: picture is centered relative to the reference origin
- **Inline**: inline vertical alignment
- **Inside**: inside vertical alignment
- **None**: picture is explicitly positioned by using position properties
- **Outside**: outside vertical alignment
- **Top**: picture is aligned to the top of the reference origin

### HorizontalOrigin and VerticalOrigin
The `HorizontalOrigin` and `VerticalOrigin` properties define the reference origin which is used for relative positioning of the picture.

#### HorizontalOrigin
The `HorizontalOrigin` property returns a value of type, HorizontalOrigin. The following are the variants for setting the Horizontal origin of a picture.

- **Margin**
- **Page**
- **Column**
- **Character**

#### VerticalOrigin
The `VerticalOrigin` property returns a value of type, VerticalOrigin. The following are the variants for setting the Vertical origin of a picture.

- **Margin**
- **Page**
- **Paragraph**
- **Line**

### Border Style
This section introduces the concept of Border Style but does not provide further details in the current image.

## Page-level Navigation/TOC (if applicable)
- This page likely pertains to a section or chapter within the User Guide, detailing specific functionalities related to image placement and alignment settings in DocIO. The structure suggests a broader topic on styling elements in documents.

## Cross References
- See also: related sections on image insertion, document formatting, and other layout controls within the Syncfusion Winforms User Guide.

<!-- tags: [winforms, docio, image alignment, horizontal alignment, vertical alignment, horizontal origin, vertical origin, border style] keywords: [HorizontalAlignment, VerticalAlignment, ShapeHorizontalAlignment, ShapeVerticalAlignment, HorizontalOrigin, VerticalOrigin, None, Left, Center, Right, Inside, Outside, Bottom, Inline, None (vertical), Outside (vertical), Top, Margin, Page, Column, Paragraph, Border Style, DocIO, Syncfusion] -->
```