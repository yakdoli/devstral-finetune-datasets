```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: diagram
page_number: 033
page_id: diagram#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:09:37Z
fidelity: lossless
-->

## Overview
- Demonstrates how to create and style a process node using the Syncfusion Windows Forms Diagram control.
- Explains setting fill style, border style, and label customization for process and decision nodes.
- Includes code examples in VB for creating nodes and adding them to the diagram model.

## Content

### Creating and Styling Nodes

The following code demonstrates the process of creating and styling a process node in a Windows Forms Diagram.

#### Code Example in VB

```vb
' Create a process node
Dim process As New Rectangle(50, 50, 100, 70)

' Style the process node
process.FillStyle.Type = FillStyleType.LinearGradient
process.FillStyle.Color = Color.FromArgb(128, 0, 0)
process.FillStyle.ForeColor = Color.FromArgb(225, 0, 0)

' Border style
process.LineStyle.LineColor = Color.RosyBrown
process.LineStyle.LineWidth = 2.0F
process.LineStyle.LineJoin = Drawing2D.LineJoin.Miter

' Add a label to the process node
Dim label As New Syncfusion.Windows.Forms.Diagram.Label()
label.Text = "Process"
label.FontStyle.Family = "Arial"
label.FontColorStyle.Color = Color.White
process.Labels.Add(label)

' Add process node to the model
diagram.Model.AppendChild(process)

' Create a decision node
Dim decision As New Polygon(
    New PointF() {
        New PointF(0, 50),
        New PointF(50, 0),
        New PointF(100, 50),
    }
)
```

### Explanation
- **Process Node Creation**: A `Rectangle` is used to represent the process node, defined by its coordinates and dimensions.
- **Styling**: The fill style is set to a linear gradient with a specific color range and foreground color.
- **Border Style**: The border color, width, and line join type are customized to enhance the visual appearance.
- **Label Addition**: A label with specific text, font, and color is added to the process node.
- **Adding to the Model**: The process node is added to the diagram model using `AppendChild`.

### Decision Node
A decision node is created using a `Polygon` shape, defined by an array of `PointF` coordinates.

## API Reference

### Classes and Properties Used
- **Rectangle**: Represents a rectangular node.
- **Polygon**: Represents a polygonal node.
- **FillStyleType**: Defines the type of fill style, such as gradient.
- **Color**: Used for setting fill and border colors.
- **Diagram.Label**: Used for adding labels to nodes.
- **FontStyle**: Sets the font properties for labels.

### Methods
- **Diagram.Model.AppendChild**: Adds a child node to the diagram model.

## Code Examples (Multi-Language)

### VB Code Example (Partial)
```vb
' Add process node to the model
diagram.Model.AppendChild(process)
```

## Cross References
See also:
- [Syncfusion Diagram Control Documentation](https://help.syncfusion.com/windowsforms/diagram/getting-started)
- [Customizing Node Styles in Diagram](https://help.syncfusion.com/windowsforms/diagram/elements/node-style)

<!-- tags: [Syncfusion Winforms, Diagram Control, Node Styling, VB, Version 11.4.0.26] keywords: [Syncfusion, Windows Forms, Diagram, Node, Styling, Process, Decision, Label, FillStyle, BorderStyle, Polygon] -->
```
