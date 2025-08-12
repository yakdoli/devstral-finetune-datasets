```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: diagram
page_number: 130
page_id: diagram#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:35Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to create and customize labels for nodes in a Diagram.
- Explains how to position labels using predefined or custom positions.
- Details the application of font styles, text alignment, and wrapping.

## Content

### C#

```csharp
// Create a label with custom position
Syncfusion.Windows.Forms.Diagram.Label lbl_Custom = new Syncfusion.Windows.Forms.Diagram.Label(node, "Label_Custom");
// Position the label
lbl_Custom.Position = Position.Custom;
lbl_Custom.OffsetX = 0;
lbl_Custom.OffsetY = 0;
// Apply font style
lbl_Custom.FontStyle.Bold = true;
lbl_Custom.FontStyle.Family = "Corbel";
lbl_Custom.FontStyle.Size = 9;
// Format the label text
lbl_Custom.HorizontalAlignment = StringAlignment.Center;
lbl_Custom.VerticalAlignment = StringAlignment.Far;
// WrapText is set to true by default

// Add the label to node's label collection
node.Labels.Add(lbl_Custom);
// Add the node to diagram model
diagram1.Model.AppendChild(node);
```

### VB

```vb
Dim node As New RoundRect(0, 0, 170, 100, MeasureUnits.Pixel)

    ' Create a label with predefined position
    Dim lbl_TopCenter As New Syncfusion.Windows.Forms.Diagram.Label(node, "Label_TopCenter")
    ' Position the label
    lbl_TopCenter.Position = Position.TopCenter
    ' Position enum has the values Center, TopLeft, TopCenter, TopRight, MiddleLeft, MiddleRight, BottomLeft, BottomCenter, BottomRight and Custom

    ' Apply font style
    lbl_TopCenter.FontStyle.Bold = True
    lbl_TopCenter.FontStyle.Family = "Corbel"
    lbl_TopCenter.FontStyle.Size = 9
    ' Add the label to node's label collection
    node.Labels.Add(lbl_TopCenter)

    ' Create a label with custom position
    Dim lbl_Custom As New Syncfusion.Windows.Forms.Diagram.Label(node, "Label_Custom")
    ' Position the label
    lbl_Custom.Position = Position.Custom
    lbl_Custom.OffsetX = 0
    lbl_Custom.OffsetY = 0
    ' Apply font style
    lbl_Custom.FontStyle.Bold = True
    lbl_Custom.FontStyle.Family = "Corbel"
    lbl_Custom.FontStyle.Size = 9
```

## Cross References
- **See also:** Labeling nodes, Positioning labels, Font customization, Text alignment, Diagram nodes.

<!-- tags: [product, module, control, api, version?] keywords: [diagram, node, label, positioning, font style, text alignment, node labels, custom position, predefined position] -->
```