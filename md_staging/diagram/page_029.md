```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: diagram
page_number: 029
page_id: diagram#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:09:17Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

The code snippet below demonstrates how to style a rectangular node, define its border attributes, add a label to the node, and append the node to the diagram model in a Windows Forms application.

## Content

```vb
'Style the rectangular node
rectangle.FillStyle.Type = FillStyleType.LinearGradient
rectangle.FillStyle.Color = Color.FromArgb(128, 0, 0)
rectangle.FillStyle.ForeColor = Color.FromArgb(225, 0, 0)
rectangle.ShadowStyle.Visible = True

'Border style
rectangle.LineStyle.LineColor = Color.RosyBrown
rectangle.LineStyle.LineWidth = 2.0F
rectangle.LineStyle.LineJoin = Drawing2D.LineJoin.Miter

'Add a label to the rectangular node
Dim label As New Syncfusion.Windows.Forms.Diagram.Label()
label.Text = "Hello!"
label.FontStyle.Family = "Arial"
label.FontColorStyle.Color = Color.White
rectangle.Labels.Add(label)

'Add the rectangular node to the model
diagram.Model.AppendChild(rectangle)
```

This code snippet illustrates the following steps:
1. **Styling the Rectangular Node**: Configures the fill style to use a linear gradient, sets the fill color and foreground color, and enables shadows.
2. **Defining Border Style**: Sets the border color, width, and join style.
3. **Adding a Label**: Creates a label with a specified font family and color, adds it to the rectangular node.
4. **Appending the Node to the Diagram**: Adds the styled rectangular node to the diagram model.

## API Reference

- **Classes**
  - `Syncfusion.Windows.Forms.Diagram.Label`
  - `Syncfusion.Windows.Forms.Diagram.FillStyleType`
  - `Drawing2D.LineJoin`
  - `Syncfusion.Windows.Forms.Diagram.RectangularNode`

- **Properties**
  - `FillStyleType`
  - `Color`
  - `ForeColor`
  - `ShadowStyle.Visible`
  - `LineStyle.LineColor`
  - `LineStyle.LineWidth`
  - `LineStyle.LineJoin`
  - `Labels`

- **Methods**
  - `AppendChild`

## Code Examples

The provided VB.NET code demonstrates the setup and styling of a rectangular node in a Windows Forms Diagram component.

### Overview
- Configures the fill, border, and label properties of a rectangular node.
- Adds the styled node to the diagram model using the `AppendChild` method.

### Design-Time vs. Runtime
- These configurations can be done both at design time through the property grid or at runtime programmatically as shown in the code snippet.

###见:
```markdown
See also:
- [Syncfusion Windows Forms Documentation](http://docs.syncfusion.com/windowsforms/)
- [Diagram Components](http://docs.syncfusion.com/windowsforms/diagram/overview)
- [Styling and Appearance](http://docs.syncfusion.com/windowsforms/diagram/styling)
- [Adding Elements to a Diagram](http://docs.syncfusion.com/windowsforms/diagram/elements)
```

<!-- tags: [Syncfusion, WinForms, Diagram, Styling, Labels, Windows Forms, Linear Gradient, Border Style] keywords: [rectangular node, fill style, linear gradient, border, label, diagram model, shadow, AppendChild, Windows Forms, Syncfusion, Diagram] -->
```