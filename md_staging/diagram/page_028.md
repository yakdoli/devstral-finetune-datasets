```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: diagram
page_number: 028
page_id: diagram#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:08:41Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
Syncfusion.Windows.Forms.Diagram.Rectangle rectangle
    = new Syncfusion.Windows.Forms.Diagram.Rectangle(120, 120, 100, 70);

//Style the rectangular node
rectangle.FillStyle.Type = FillStyleType.LinearGradient;
rectangle.FillStyle.Color = Color.FromArgb(128, 0, 0);
rectangle.FillStyle.ForeColor = Color.FromArgb(225, 0, 0);
rectangle.ShadowStyle.Visible = true;

//Border style
rectangle.LineStyle.LineColor = Color.RosyBrown;
rectangle.LineStyle.LineWidth = 2.0f;
rectangle.LineStyle.LineJoin = LineJoin.Miter;

//Add a label to the rectangular node
Syncfusion.Windows.Forms.Diagram.Label label
    = new Syncfusion.Windows.Forms.Diagram.Label();
label.Text = "Hello!";
label.FontStyle.Family = "Arial";
label.FontColorStyle.Color = Color.White;
rectangle.Labels.Add(label);

//Add the rectangular node to the model
diagram.Model.AppendChild(rectangle);
```

### VB

```vb
'Enable diagram rulers
diagram.ShowRulers = True

'Create a rectangular node
Dim rectangle As New Rectangle(120, 120, 100, 70)
```

## API Reference

### Methods
- **AppendChild**: Adds a child node to the diagram model.

### Properties
- **Model**: Represents the model of the diagram.
- **ShowRulers**: Enables or disables the rulers for the diagram. 

## Code Examples

- **C# Example**: Demonstrates how to create and style a rectangular node in a Windows Forms Diagram.
- **VB Example**: Shows equivalent functionality in VB for enabling diagram rulers and creating a rectangular node.

## See also
- [Diagram Controls in Syncfusion](#)
- [Customizing Appearance](#)

<!-- tags: [syncfusion, winforms, diagram, nodes, styling, vb, rectangle] keywords: [diagram, Windows Forms, Syncfusion, rectangle, fill style, border, label, rulers, C#, VB] -->
```