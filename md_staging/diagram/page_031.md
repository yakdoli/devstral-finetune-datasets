```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: diagram
page_number: 031
page_id: diagram#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:08:44Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates creating and styling nodes in a Windows Forms Diagram.
- Displays properties for configuring the appearance of process and decision nodes.
- Includes the addition of labels to enhance node readability.

## Creating and Styling Nodes

### Process Node

#### Style the process node
```csharp
process.FillStyle.ForeColor = Color.FromArgb(225, 0, 0);
```

#### Border Style
```csharp
process.LineStyle.LineColor = Color.RosyBrown;
process.LineStyle.LineWidth = 2.0f;
process.LineStyle.LineJoin = LineJoin.Miter;
```

#### Add a label to the process node
```csharp
Syncfusion.Windows.Forms.Diagram.Label label
    = new Syncfusion.Windows.Forms.Diagram.Label();
label.Text = "Process";
label.FontStyle.Family = "Arial";
label.FontColorStyle.Color = Color.White;
process.Labels.Add(label);
```

#### Add the process node to the model
```csharp
diagram.Model.AppendChild(process);
```

### Decision Node

#### Create a decision node
```csharp
Polygon decision = new Polygon(new PointF[] {
    new PointF(0, 50), new PointF(50, 0),
    new PointF(100, 50), new PointF(50, 100),
    new PointF(0, 50)
});
```

#### Style the decision node
```csharp
decision.FillStyle.Type = FillStyleType.LinearGradient;
decision.FillStyle.Color = Color.FromArgb(128, 0, 0);
decision.FillStyle.ForeColor = Color.FromArgb(225, 0, 0);
```

#### Border Style
```csharp
decision.LineStyle.LineColor = Color.RosyBrown;
decision.LineStyle.LineWidth = 2.0f;
decision.LineStyle.LineJoin = LineJoin.Miter;
```

## API Reference

### Namespace: `Syncfusion.Windows.Forms.Diagram`

#### Properties
- `FillStyle`: Controls the fill properties of the node.
  - `ForeColor`: Foreground color of the fill.
- `LineStyle`: Manages the border properties of the node.
  - `LineColor`: Color of the border.
  - `LineWidth`: Width of the border.
  - `LineJoin`: Join style for lines (e.g., Miter).
- `Labels`: Collection of labels added to the node.

### Methods
- `AppendChild(Node node)`: Adds a child node to the Diagram Model.

## Code Examples

Creating and styling nodes in a Windows Forms Diagram:
```csharp
// Create a process node
// Style the process node
process.FillStyle.ForeColor = Color.FromArgb(225, 0, 0);

// Border style
process.LineStyle.LineColor = Color.RosyBrown;
process.LineStyle.LineWidth = 2.0f;
process.LineStyle.LineJoin = LineJoin.Miter;

// Add a label to the process node
Syncfusion.Windows.Forms.Diagram.Label label
    = new Syncfusion.Windows.Forms.Diagram.Label();
label.Text = "Process";
label.FontStyle.Family = "Arial";
label.FontColorStyle.Color = Color.White;
process.Labels.Add(label);

// Add the process node to the model
diagram.Model.AppendChild(process);

// Create a decision node
Polygon decision = new Polygon(new PointF[] {
    new PointF(0, 50), new PointF(50, 0),
    new PointF(100, 50), new PointF(50, 100),
    new PointF(0, 50)
});

// Style the decision node
decision.FillStyle.Type = FillStyleType.LinearGradient;
decision.FillStyle.Color = Color.FromArgb(128, 0, 0);
decision.FillStyle.ForeColor = Color.FromArgb(225, 0, 0);

// Border style
decision.LineStyle.LineColor = Color.RosyBrown;
decision.LineStyle.LineWidth = 2.0f;
decision.LineStyle.LineJoin = LineJoin.Miter;
```

## Page-level Navigation/TOC (if applicable)
- Styles for nodes
- Adding labels to nodes
- Integration with Windows Forms Diagram Model

## Cross References
- This page references the `Syncfusion.Windows.Forms.Diagram` namespace.
- Related topics include configuring `FillStyle` and `LineStyle` properties.

<!-- tags: [Syncfusion, Windows Forms, Diagram, Control, PROPERTY, METHOD] keywords: [process node, decision node, border style, gradient, label, appendchild] -->
```