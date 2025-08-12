```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: diagram
page_number: 194
page_id: diagram#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:31Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Zoom to the center of the diagram.
- Zoom to the top left of the diagram.
- Zoom to the pointer position using Ctrl and the mouse wheel.

## Use Case Scenarios
Users can zoom in and out of diagram content based on their requirements.

### Properties

| Property     | Description                                                                 | Data Type |
|--------------|-----------------------------------------------------------------------------|-----------|
| ZoomType     | Gets or sets the type of zooming to be performed.                          | enum      |
| ZoomIncrement| Specifies the amount to zoom each time the diagram is zoomed in or out.   | float     |

### Methods

| Method          | Description                                                                 | Parameters | Return Type |
|-----------------|-----------------------------------------------------------------------------|------------|-------------|
| ZoomIn          | Zoom in on the diagram document.                                           | NA         | void        |
| ZoomOut         | Zoom out of the diagram document.                                          | NA         | void        |
| ZoomToSelection | Zoom the diagram document to the specified selection bounds.             | RectangleF | void        |
| ZoomToActual    | Zoom the document to its actual size.                                      | NA         | void        |

### 4.6.7.2.1 ZoomIn, ZoomOut, ZoomToActual, ZoomToSelection

The diagram document can be zoomed in, zoomed out, zoomed to its original size, and zoomed to a selected area based on the ZoomIncrement. You can use the following methods to zoom in the diagram document.

- ZoomIn()
- ZoomOut()
- ZoomToSelection(RectangleF)

## Page-level Navigation/TOC (if applicable)

## Cross References

See also: WinForms, Diagram, Zooming, Windows Forms, User Guide, 194, page

<!-- tags: [Syncfusion Winforms, Diagram, Zooming, User Guide] keywords: [diagram, ZoomIn, ZoomOut, ZoomToActual, ZoomToSelection, Windows Forms] -->
```