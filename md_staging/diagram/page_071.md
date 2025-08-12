```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: diagram
page_number: 071
page_id: diagram#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:57Z
fidelity: lossless
-->

### Drawing Tools in Windows Forms

## Overview
- The `diagram` namespace in Syncfusion WinForms provides tools for drawing various shapes and elements in a Windows Forms application.
- These tools include options for selecting, drawing lines, polylines, rectangles, ellipses, polygons, curves, and text.

## Content

### WinForms Drawing Tools Overview

The following table lists the various drawing tools available in the `diagram` namespace, along with their descriptions and corresponding code snippets for activating these tools:

| Tool Name          | Description                                                         | Code Snippet                                                                 |
|--------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------|
| SelectTool         | Specifies the selection mode.                                      | `diagram1.Controller.ActivateTool("SelectTool");`                              |
| LineTool           | Draws straight line with start and end point.                     | `diagram1.Controller.ActivateTool("LineTool");`                                |
| PolyLineTool       | Interactive tool for drawing polylines.                           | `diagram1.Controller.ActivateTool("PolyLineTool");`                            |
| RectangleTool      | Interactive tool for drawing rectangles.                           | `diagram1.Controller.ActivateTool("RectangleTool");`                           |
| RectangleTool      | Interactive tool for drawing rounded rectangles.                   | `diagram1.Controller.ActivateTool("RectangleTool");`                           |
| EllipseTool        | Interactive tool for drawing ellipses.                             | `diagram1.Controller.ActivateTool("EllipseTool");`                             |
| PolygonTool        | Interactive tool for drawing polygons.                             | `diagram1.Controller.ActivateTool("PolygonTool");`                             |
| CurveTool          | Interactive tool for drawing curves.                               | `diagram1.Controller.ActivateTool("CurveTool");`                               |
| ClosedCurveTool    | Interactive tool for drawing closed curves.                        | `diagram1.Controller.ActivateTool("ClosedCurveTool");`                         |
| PencilTool         | Draws the user defined shape similar to Microsoft Paint.          | `diagram1.Controller.ActivateTool("PencilTool");`                              |
| SplineTool         | Interactive tool for drawing spline.                               | `diagram1.Controller.ActivateTool("SplineTool");`                              |
| BezierTool         | Interactive tool for drawing bezier.                               | `diagram1.Controller.ActivateTool("BezierTool");`                              |
| TextTool           | Interactive tool for inserting text nodes into a diagram and editing | `diagram1.Controller.ActivateTool("TextTool");`                                |

### Figure: Drawing Tools

![Drawing Tools](https://example.com/drawing-tools.png)  
*Figure 42: Drawing Tools*

This figure illustrates the various drawing tools available, represented by icons corresponding to each tool listed in the table above.

## API Reference

### Available Tools

The following tools can be activated using the `ActivateTool` method of the `Controller` class in the `diagram` namespace:

- `SelectTool`
- `LineTool`
- `PolyLineTool`
- `RectangleTool`
- `EllipseTool`
- `PolygonTool`
- `CurveTool`
- `ClosedCurveTool`
- `PencilTool`
- `SplineTool`
- `BezierTool`
- `TextTool`

### Code Snippets

Each tool can be activated by calling the `ActivateTool` method, passing the tool name as a string parameter. For example:

```csharp
diagram1.Controller.ActivateTool("LineTool");
```

This snippet activates the `LineTool`, allowing users to draw straight lines.

### Cross References

For more details on using these tools in a WinForms application, refer to the official Syncfusion documentation on [WinForms Diagram Tools](https://www.syncfusion.com/documentation/windowsforms/diagram-tools).

## RAG Annotations

<!-- tags: [winforms, diagram, tools, drawing, syncfusion] keywords: [diagram, line, ellipse, polygon, bezier, text, controller, activate] -->
```