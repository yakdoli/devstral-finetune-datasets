```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_248.jpeg
document_name: diagram
page_number: 248
page_id: diagram#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:45Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Open the Syncfusion Dashboard.
- Click the Windows Forms drop-down list and select Run Locally Installed Samples.
- Navigate to Diagram Samples > Product Showcase > Diagram Builder.

## Content

### 4.6.12 Dragging, Resizing, and Rotation Styles for Nodes

Essential Diagram for Windows Forms provides dragging, resizing, and rotation styles such as ghost copy, filled rectangle, solid outline, and dashed outline for nodes. These styles provide better visual effects for your diagram and increase the performance speed of the diagram while dragging, rotating, or resizing nodes.

#### Properties

Table 6: Properties Table

| Property       | Description                                | Type | Data Type             |
|----------------|--------------------------------------------|------|------------------------|
| ResizingStyle  | Gets or sets resizing style for the rendering helper | NA | RenderingHelperStyle |
| DraggingStyle  | Gets or sets dragging style for the rendering helper | NA | RenderingHelperStyle |
| RotatingStyle  | Gets or sets rotating style for the rendering helper | NA | RenderingHelperStyle |

#### Applying Styles to Rendering Helper

The following code example illustrates how to apply styles to the rendering helper while resizing, dragging, and rotating nodes.

```csharp
// Specify dragging, resizing, and rotation styles to the rendering helper
diagram1.Controller.DraggingStyle = RenderingHelperStyle.SolidOutline;
diagram1.Controller.ResizingStyle = RenderingHelperStyle.GhostCopy;
diagram1.Controller.RotatingStyle = RenderingHelperStyle.DashedOutline;
```

## RAG Annotations
<!-- tags: [essential-dictionary, windows-forms, dragging-resizing-rotation, rendering-helper] keywords: [dragging, resizing, rotation, nodes, ghost copy, filled rectangle, solid outline, dashed outline, diagram, performance speed, rendering helper] -->
```