```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_249.jpeg
document_name: diagram
page_number: 249
page_id: diagram#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:59Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Set dragging, resizing, and rotation styles for the rendering helper using VB.NET.
- Customize the rendering style for specific operations like dragging, resizing, and rotating.

## Content

### Setting Rendering Styles for Diagram Operations

The following VB.NET code demonstrates how to specify the rendering styles for dragging, resizing, and rotating operations in a `Diagram` control.

```vb
' Specify dragging, resizing, and rotation styles to the rendering helper
diagram1.Controller.DraggingStyle = RenderingHelperStyle.SolidOutline
diagram1.Controller.ResizingStyle = RenderingHelperStyle.GhostCopy
diagram1.Controller.RotatingStyle = RenderingHelperStyle.DashedOutline
```

### Explanation

- **DraggingStyle**: Configures the visual feedback when dragging nodes. Here, it is set to `RenderingHelperStyle.SolidOutline`, which draws a solid outline during dragging.
- **ResizingStyle**: Defines the visual effect during node resizing. It is set to `RenderingHelperStyle.GhostCopy`, indicating a ghost copy is displayed.
- **RotatingStyle**: Specifies the visual behavior during node rotation. The setting `RenderingHelperStyle.DashedOutline` results in a dashed outline for rotation.

### Usage Context

This code is typically used in a Windows Forms application to enhance user interaction with a diagram. By setting these styles, you can provide a more intuitive and responsive user experience.

## API Reference

- **Diagram.Controller.DraggingStyle**: Property to set the dragging style.
- **Diagram.Controller.ResizingStyle**: Property to set the resizing style.
- **Diagram.Controller.RotatingStyle**: Property to set the rotating style.
- **RenderingHelperStyle**: Enumeration for different styles such as `SolidOutline`, `GhostCopy`, and `DashedOutline`.

## Code Examples

### VB.NET Example

```vb
' Setting dragging, resizing, and rotation styles
diagram1.Controller.DraggingStyle = RenderingHelperStyle.SolidOutline
diagram1.Controller.ResizingStyle = RenderingHelperStyle.GhostCopy
diagram1.Controller.RotatingStyle = RenderingHelperStyle.DashedOutline
```

### Cross References

- For more information on the `Diagram` control and its properties, refer to the official Syncfusion documentation.

<!-- tags: [syncfusion, windows forms, diagram, rendering helper, winforms, vb.net] keywords: [dragging, resizing, rotation, rendering style, ghost copy, solid outline, dashed outline] -->
```