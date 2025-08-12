```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_034.jpeg
document_name: diagram
page_number: 034
page_id: diagram#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:28Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates configuring a decision node in a flowchart diagram.
- Covers styling, positioning, and connecting a decision node in a Windows Forms application.

## Content

### Creating and Configuring a Decision Node

#### Code Example

```vb
New PointF (50, 100),
New PointF (0, 50)
})

' Style the decision node
decision.FillStyle.Type = FillStyleType.LinearGradient
decision.FillStyle.Color = Color.FromArgb(128, 0, 0)
decision.FillStyle.ForeColor = Color.FromArgb(225, 0, 0)

' Border style
decision.LineStyle.LineColor = Color.RosyBrown
decision.LineStyle.LineWidth = 2.0F
decision.LineStyle.LineJoin = Drawing2D.LineJoin.Miter

' Add a label to the decision node
label = New Syncfusion.Windows.Forms.Diagram.Label()
label.Text = "Decision"
label.FontStyle.Family = "Arial"
label.FontColorStyle.Color = Color.White
decision.Labels.Add(label)

' Position the decision node
decision.PinPoint = New PointF (250, 250)
' Add decision node to the model
diagram.Model.AppendChild(decision)

' Create an orthogonal connector
Dim link As New OrthogonalConnector(process.PinPoint,
    decision.PinPoint)

' Style the link
link.LineStyle.LineColor = Color.RosyBrown
link.LineStyle.LineWidth = 2.0F
```

### Explanation

1. **Decision Node Configuration**
   - **Fill Style**: The decision node is styled with a linear gradient filled in dark red shades (RGB values: 128, 0, 0, and 225, 0, 0). This creates a visually distinct appearance for the node.
   - **Border Style**: The border is set to RosyBrown color with a width of 2.0F, and the line join property is set to Miter, ensuring sharp, clean borders.

2. **Adding Labels**
   - A label is added to the decision node. The label text is "Decision," styled with Arial font and white text color, ensuring readability against the dark background fill.

3. **Positioning**
   - The decision node is positioned at the coordinates (250, 250) using the PinPoint property.

4. **Connecting Nodes**
   - An orthogonal connector is created between a `process` node and the decision node. 
   - The connector is styled with a RosyBrown color and a width of 2.0F, matching the border style of the decision node.

### API Reference

#### Classes Used
- **Syncfusion.Windows.Forms.Diagram.Label**: Used for adding labels to nodes.
- **Syncfusion.Windows.Forms.Diagram.OrthogonalConnector**: Used to create orthogonal connectors between nodes.

### Code Examples

The provided code snippet demonstrates the complete process of creating a decision node in a Windows Forms application using the Syncfusion libraries. It includes styling, positioning, labeling, and connecting the node.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Decision Node, Flowchart Diagram, OrthogonalConnector, Label, FillStyle] keywords: [decision node, orthogonal connector, linear gradient, RosyBrown, Arial, PinPoint] -->
```