```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_128.jpeg
document_name: pdf
page_number: 128
page_id: pdf#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:21Z
fidelity: lossless
-->

## Overview
- Parameters and methods for PDF table layout are described here.
- Events related to cell, row, and page layouts are listed with their descriptions.

## Content

### Methods and Parameters

The following table outlines the various parameter combinations used in PDF table layout methods:

| Parameters | Return Type |
| --- | --- |
| (PdfPage page, float x, float y) | PdfLightTableLayoutResult |
| (PdfPage page, PointF location, PdfLightTableLayoutFormat format) | PdfLightTableLayoutResult |
| (PdfPage page, PointF location, PdfLayoutFormat format) | PdfLayoutResult |
| (PdfPage page, RectangleF bounds, PdfLightTableLayoutFormat format) | PdfLightTableLayoutResult |
| (PdfPage page, PointF location, PdfLayoutFormat format) | PdfLayoutResult |
| (PdfGraphics graphics, float x, float y) | void |
| (PdfGraphics graphics, PointF location, float width) | void |
| (PdfPage page, float x, float y, float width) | PdfLightTableLayoutResult |
| (PdfPage page, float x, float y, PdfLightTableLayoutFormat format) | PdfLightTableLayoutResult |
| (PdfPage page, float x, float y, PdfLayoutFormat format) | PdfLayoutResult |
| (PdfGraphics graphics, float x, float y, float width) | void |
| (PdfPage page, float x, float y, float width, PdfLightTableLayoutFormat format) | PdfLightTableLayoutResult |

### Events

The following table lists the events associated with PDF layout operations, along with their descriptions:

| Name | Description |
| --- | --- |
| BeginCellLayout | This event is raised on starting cell layout. |
| BeginPageLayout | This event is raised before the element is printed on the page. (Inherited from PdfLayoutElement.) |
| BeginRowLayout | This event is raised on starting row layout. |
| EndCellLayout | This event is raised on having finished cell layout. |
| EndPageLayout | This event is raised after the element is printed on the page. (Inherited from PdfLayoutElement.) |

## API Reference
### Events

- **BeginCellLayout**: Triggered when cell layout begins.
- **BeginPageLayout**: Triggered before the element is printed on the page.
- **BeginRowLayout**: Triggered when row layout begins.
- **EndCellLayout**: Triggered after cell layout is completed.
- **EndPageLayout**: Triggered after the element is printed on the page.

## Code Examples

Example usage of the methods and events can be found in the Syncfusion documentation or code samples.

## Page-level Navigation/TOC (if applicable)
- Methods
- Parameters
- Events

## Cross References
- Refer to the Syncfusion WinForms documentation for more details on PDF layout operations.
- See also related sections on PDFElement and PdfLayoutElement for additional context.

<!-- tags: [syncfusion, winforms, pdftable, layout, event, pdfpage, pdflayoutresult, pdflighttablelayoutresult] keywords: [pdfpage, pdflayoutelement, beginpage, endpage, cell, row, layout, event, method, parameter, format] -->
```