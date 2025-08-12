```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_197.jpeg
document_name: diagram
page_number: 197
page_id: diagram#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:57Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to set the `ZoomType` to `TopLeft` using C# and VB.NET code.
- Explains zooming the diagram to the pointer position using Ctrl and the mouse wheel.

## Content

### Setting ZoomType to TopLeft

#### C#

```csharp
this.diagram1.View.ZoomType = ZoomType.TopLeft;
```

#### [VB]

```vb
' Sets the ZoomType as TopLeft.
Me.diagram1.View.ZoomType = ZoomType.TopLeft
```

#### Figure 121: Top-Left Zoom
![Figure 121: Top-Left Zoom](https://i.imgur.com/rSz3mF4.png)

### Zooming to the Pointer Position

Essential Diagram supports zooming the diagram document to the pointer position using Ctrl and the mouse wheel.

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Diagram
- **Class:** DiagramView
- **Property:**
  - `ZoomType`: Specifies the zoom type for the diagram.
    - Type: `ZoomType`
    - Description: Gets or sets the zoom type for the diagram.
    - Default: `TopLeft`

## Code Examples

### C# Example

```csharp
// Set the ZoomType to TopLeft
this.diagram1.View.ZoomType = ZoomType.TopLeft;
```

### VB.NET Example

```vb
' Set the ZoomType to TopLeft
Me.diagram1.View.ZoomType = ZoomType.TopLeft
```

## RAG Annotations
<!-- tags: [Syncfusion, Windows Forms, Diagram, Zoom, WholeDocumentZoom, ZoomType, Version 11.4.0.26] keywords: [Essential Diagram, Whole Document Zoom, Zoom Type, TopLeft, C#, VB.NET, Mouse Wheel Zoom] -->
```