```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_290.jpeg
document_name: diagram
page_number: 290
page_id: diagram#page_290
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:26:23Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Explains how to protect links from user selection or manipulation using the `EditStyle` class.
- Demonstrates disabling the selection of a node link by setting the `Enabled` property to `False`.
- Explains how to smooth out the edges of shapes in a diagram using the `RenderingStyle.SmootherMode` property.

## Content

### Protecting Links from User Selection
You can protect links from user selection / manipulation by making use of the `EditStyle` class. By setting the `Enabled` property of the `EditStyle` class to `False`, you can disable the selection of a node link.

#### C#
```csharp
// Creating Line connector.
LineConnector conn = new LineConnector(new PointF(1, 1), new PointF(2, 2));

// Disabling selection of the line connector.
conn.EditStyle.Enabled = false;
```

#### VB.NET
```vb.net
' Creating Line connector.
Dim conn As LineConnector = New LineConnector(New PointF(1, 1), New PointF(2, 2))

' Disabling selection of the line connector.
conn.EditStyle.Enabled = False
```

### Smoothing Out the Edges of Shapes in a Diagram
#### 5.32 How To Smooth-out the Edges Of the Shapes In a Diagram
You can use the `Diagram.Model.RenderingStyle.SmoothingMode` property to smooth-out the edges, lines and curves of the shapes in a diagram.

#### C#
```csharp
this.diagram1.Model.RenderingStyle.SmoothingMode = System.Drawing.Drawing2D.SmootherMode.HighQuality;
```

#### VB.NET
```vb.net
Me.diagram1.Model.RenderingStyle.SmoothingMode = System.Drawing.Drawing2D.SmootherMode.HighQuality
```

## API Reference
- Namespace: `System.Drawing.Drawing2D`
- Class: `SmootherMode`
- Property:
  - `Enabled`: Controls the selection of a node link.
  - `SmoothingMode`: Determines the rendering quality of edges, lines, and curves in diagrams.

## Code Examples
- The examples demonstrate how to disable link selection and apply high-quality smoothing to shapes.

<!-- tags: [diagrams, windowsforms, link-protection, smoothingmode, winforms] keywords: [EditStyle, Enabled, SmoothingMode, LineConnector, RenderingStyle, HighQuality] -->
```