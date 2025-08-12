```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_291.jpeg
document_name: diagram
page_number: 291
page_id: diagram#page_291
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:18Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- How to programmatically move nodes on a diagram.
- Steps to remove the gray area around a diagram.

## Content

### How to Move Nodes on a Diagram Programmatically?
You can move the desired collection of nodes to a diagram using the `MoveNodes` method. The following code example illustrates this.

```csharp
[C#]

// Move the selected nodes by 20 pixels in both horizontally and vertically.
diagram1.MoveNodes(diagram1.Controller.SelectionList, 20, 20, MeasureUnits.Pixel);
```

```vb.net
[VB.NET]

' Move the selected nodes by 20 pixels in both horizontally and vertically.
diagram1.MoveNodes(diagram1.Controller.SelectionList, 20, 20, MeasureUnits.Pixel)
```

### How to Remove the Gray Area around a Diagram?
You can remove the unnecessary gray area added around a diagram by setting the `ScrollVirtualBounds` property as `Empty`. The following code example illustrates this.

```csharp
[C#]

// Remove the unwanted gray area around a diagram.
diagram1.View.ScrollVirtualBounds = RectangleF.Empty;
```

```vb.net
[VB.NET]

' Remove the unwanted gray area around a diagram.
diagram1.View.ScrollVirtualBounds = RectangleF.Empty;
```

## API Reference

### Parameters for `MoveNodes` Method
- **Node Selection**: The collection of nodes to move, typically obtained from `diagram1.Controller.SelectionList`.
- **Horizontal Offset**: The number of pixels to move horizontally.
- **Vertical Offset**: The number of pixels to move vertically.
- **Measure Unit**: The unit of measurement, specified as `MeasureUnits.Pixel`.

### Properties
- **ScrollVirtualBounds**: Property of the diagram's view that defines the bounds of the diagram area.

<!-- tags: [windows forms, diagram, node movement, gray area, scroll virtual bounds, programmatically moving nodes] keywords: [MoveNodes, measure units, selection list, empty bounds, selection, diagram, nodes, gray area removal] -->
```