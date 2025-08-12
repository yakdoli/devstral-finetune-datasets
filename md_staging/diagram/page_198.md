```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: diagram
page_number: 198
page_id: diagram#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:44Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Introduction to Essential Diagram's interactive zoom and selection features.
- Explanation of the ZoomTool UI tool for dynamic document manipulation.
- Description of zoom properties for restricting and specifying magnification levels.

## Content

### Mouse-based Zoom

The figure below illustrates the mouse-based interaction for zooming within Essential Diagram.

**Figure 122: Mouse-based Zoom**

### 4.6.7.2.5 ZoomTool

Essential Diagram supports a UI tool called ZoomTool, which is used to zoom and select the diagram document interactively. Users can utilize the ZoomTool's `MaximumMagnification` and `MinimumMagnification` properties to restrict the document's maximum or minimum zoom levels and the `ZoomIncrement` property to specify the amount to zoom each time the diagram is zoomed in or out.

### Zoom Tool Properties

| Property            | Description                                                                            | Data Type |
|---------------------|----------------------------------------------------------------------------------------|-----------|
| MaximumMagnification | Specifies the maximum magnification value for zooming. Default value is 1000. | float     |
| MinimumMagnification | Specifies the minimum magnification value for zooming. Default value is 10.  | float     |
| ZoomIncrement        | Specifies the amount to zoom each time the mouse is clicked.                  | float     |

## Code Examples

The following code demonstrates how to activate the zoom tool:

```csharp
// Example code snipped here.
```

## Page-level Navigation/TOC (if applicable)

- Previous section: [unclear]
- Next section: UI elements and customization options.

## Cross References

- Refer to section 4.6.7.2 for additional information on UI tools and their properties.
- Check the appendix for detailed zoom functionalities and best practices.

<!-- tags: [Windows Forms, ZoomTool, Essential Diagram, Winforms, Syncfusion] keywords: [ZoomTool, MaximumMagnification, MinimumMagnification, ZoomIncrement, UI tool, zoom, magnification, Essential Diagram, Windows Forms, diagram manipulation] -->
```