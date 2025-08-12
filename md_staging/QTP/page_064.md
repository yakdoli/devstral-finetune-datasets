```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: QTP
page_number: 064
page_id: QTP#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:23Z
fidelity: lossless
-->

## Overview
- Describes the `Scroll(double x, double y)` method for scrolling the diagram view.

## Content

### Scroll Method

The `Scroll(double x, double y)` method is used to scroll the diagram view based on the provided `x` and `y` coordinates. This method facilitates interactive navigation within the diagram by adjusting the view position.

#### Parameters

| Name  | Type   | Description                          |
|-------|--------|--------------------------------------|
| `x`   | double | The horizontal scrolling increment.  |
| `y`   | double | The vertical scrolling increment.    |

#### Description

This method scrolls the diagram view by the specified horizontal (`x`) and vertical (`y`) amounts. It is useful for implementing interactive panning or zooming functionalities within the application.

## API Reference

### Namespace and Class
- **Namespace**: Syncfusion.Windows.Forms.Diagram
- **Class**: Diagram

### Method
- **Name**: Scroll
- **Signature**: `public void Scroll(double x, double y)`
- **Parameters**:
  - `x`: A `double` representing the horizontal scroll increment.
  - `y`: A `double` representing the vertical scroll increment.
- **Returns**: None
- **Exceptions**: None explicitly mentioned.

## Code Examples

### Example: Scrolling the Diagram View

```csharp
// Assuming 'diagram' is an instance of the Diagram class
diagram.Scroll(100.0, 50.0); // Scrolls the diagram by 100 units horizontally and 50 units vertically.
```

## See also
- [Diagram Class Documentation](#)
- [Interactive Navigation Methods](#)

<!-- tags: Essential QuickTest Professional, scroll, diagram, method, parameter, winforms, 11.4.0.26 -->
```