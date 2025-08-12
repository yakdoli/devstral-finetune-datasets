```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_114.jpeg
document_name: diagram
page_number: 114
page_id: diagram#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:28Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Overview
- A guide on customizing connector appearance in Syncfusion Diagrams for Windows Forms through code.

## Content

### Figure: Connection Property Settings
![](image.png)
*Figure 66: Connection Property Settings*

#### Customizing Connector Appearance
You can change the appearance of the connectors using its properties through code. The following code example illustrates the line properties.

#### C# Code Example
```csharp
[C#]

protected void Page_Load(object sender, EventArgs e)
{
    Syncfusion.Windows.Forms.Diagram.Ellipse ellipse = new Syncfusion.Windows.Forms.Diagram.Ellipse(160, 60, 100, 60);
    Syncfusion.Windows.Forms.Diagram.Rectangle rectangle = new Syncfusion.Windows.Forms.Diagram.Rectangle(150, 250, 120, 100);
    Syncfusion.Windows.Forms.Diagram.LineConnector lineconnector = new Syncfusion.Windows.Forms.Diagram.LineConnector(new System.Drawing.PointF(10, 200), new System.Drawing.PointF(300, 250));
    this.diagram1.Model.AppendChild(ellipse);
    this.diagram1.Model.AppendChild(rectangle);
    ellipse.CentralPort.TryConnect(lineconnector.TailEndPoint);
    rectangle.CentralPort.TryConnect(lineconnector.HeadEndPoint);
    this.diagram1.Model.AppendChild(lineconnector);
    lineconnector.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
    lineconnector.LineStyle.LineColor = Color.MidnightBlue;
    lineconnector.HeadDecorator.FillStyle.Color = Color.MidnightBlue;
    lineconnector.HeadDecorator.Size = new SizeF(10, 5);
}
```

#### VB Code Example
```vb
[VB]
```

## Page-Level Navigation/TOC (if applicable)

This page focuses on customizing the appearance of connectors in Syncfusion Diagrams for Windows Forms, providing both C# and VB examples for implementing these customizations.

## Cross References

See also:
- Diagram Properties
- Syncfusion Windows Forms API documentation

<!-- tags: Syncfusion, WinForms, Diagram, Connector, Customization, Properties, C#, VB keywords: connector appearance, code example, line properties, customizing, Windows Forms, Syncfusion Diagrams -->
```