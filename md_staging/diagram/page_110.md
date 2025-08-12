```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: diagram
page_number: 110
page_id: diagram#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:09Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to create and style a diagram with various node property settings in Windows Forms using Syncfusion.
- Illustrates configuring fill styles, gradient settings, and edit styles for a node in a diagram.

## Content

### Configuring Node Properties

#### [VB]

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    Dim ellipse As New Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 110, 70)
    diagram1.Model.AppendChild(ellipse)
    ellipse.FillStyle.Color = System.Drawing.Color.AliceBlue
    ellipse.FillStyle.ColorAlphaFactor = 100
    ellipse.FillStyle.ForeColor = System.Drawing.Color.Aquamarine
    ellipse.FillStyle.ForeColorAlphaFactor = 70
    ellipse.FillStyle.Type = FillStyleType.PathGradient
    ellipse.FillStyle.PathBrushStyle = PathGradientBrushStyle.RectangleCenter
    ellipse.FillStyle.Type = FillStyleType.LinearGradient
    ellipse.FillStyle.GradientAngle = 95
    ellipse.FillStyle.GradientCenter = 0.5F

    ellipse.EditStyle.AllowChangeHeight = True
    ellipse.EditStyle.AllowChangeWidth = True
    ellipse.EditStyle.AllowDelete = False
    ellipse.EditStyle.AllowMoveX = True
    ellipse.EditStyle.AllowMoveY = False
    ellipse.EditStyle.AllowRotate = False
    ellipse.EditStyle.AllowSelect = True
End Sub
```

**Figure 64: Diagram With Node Property Settings**

---

### Creating Nodes and Links

#### Description
The following code example illustrates how to create nodes and links in a diagram using Windows Forms.

#### [C#]
---

## API Reference

### Methods
- `Form1_Load`: Event handler for initializing the diagram with node properties.
- `Ellipse`: Creates an ellipse node in the diagram.
- `FillStyle`: Configures the fill style of the node, including gradient and color properties.
- `EditStyle`: Defines the edit behavior of the node, such as allowing changes in height, width, or selection.

### Properties
- `Color`: Sets the fill color of the node.
- `ColorAlphaFactor`: Specifies the transparency level of the fill color.
- `ForeColor`: Sets the foreground color of the node.
- `ForegroundAlphaFactor`: Specifies the transparency level of the foreground color.
- `Type`: Defines the type of fill style (e.g., PathGradient, LinearGradient).
- `PathBrushStyle`: Configures the style of the path gradient brush.
- `GradientAngle`: Specifies the angle for the linear gradient.
- `GradientCenter`: Defines the center point for the gradient in the node.

### Events
- `Load`: Triggered when the form loads, used to initialize the diagram and node properties.

## Code Examples

### VB Example
The VB code provided configures an ellipse node with specific fill styles and edit behaviors within a Syncfusion diagram.

### C# Example
The C# section starts here but is not fully provided in the image. It would typically include similar code to create and style nodes and links.

## Cross References
See also:  
- Documentation on Syncfusion Diagram API for Windows Forms.
- Examples on creating and customizing nodes and links in diagrams.

<!-- tags: [Syncfusion, Windows Forms, Diagram, Node, FillStyle,>EditStyle, Gradient, PathGradient, LinearGradient, VB, C#] keywords: [node, fill style, gradient, diagram, windows forms, VB, C#, ellipse, path gradient, linear gradient, edit style] -->
```