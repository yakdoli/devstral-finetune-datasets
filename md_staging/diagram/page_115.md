```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_115.jpeg
document_name: diagram
page_number: 115
page_id: diagram#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:10Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Diagram with Connector Property Settings

```vb
Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs)
    Dim ellipse As New Syncfusion.Windows.Forms.Diagram.Ellipse(160, 60, 100, 60)
    Dim rectangle As New Syncfusion.Windows.Forms.Diagram.Rectangle(150, 250, 120, 100)
    Dim lineconnector As New Syncfusion.Windows.Forms.Diagram.LineConnector(New System.Drawing.PointF(10, 200), New System.Drawing.PointF(300, 250))
    Me.diagram1.Model.AppendChild(ellipse)
    Me.diagram1.Model.AppendChild(rectangle)
    ellipse.CentralPort.TryConnect(lineconnector.TailEndPoint)
    rectangle.CentralPort.TryConnect(lineconnector.HeadEndPoint)
    Me.diagram1.Model.AppendChild(lineconnector)
    lineconnector.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow
    lineconnector.LineStyle.LineColor = Color.MidnightBlue
    lineconnector.HeadDecorator.FillStyle.Color = Color.MidnightBlue
    lineconnector.HeadDecorator.Size = New SizeF(10, 5)
End Sub
```

![](attachment:Diagram_with_Connector_Property_Settings.png)

**Figure 67: Diagram with Connector Property Settings**

### Summary
- This section demonstrates how to create a diagram in Windows Forms using Syncfusion's Diagram control.
- It showcases the addition of shapes such as an ellipse and a rectangle, along with connecting them using a LineConnector.
- Properties like connector style, color, and size are illustrated to enhance the visual representation of the connection.

### Implementation Details
- The `Page_Load` event is used to initialize the diagram with the required components.
- The `Ellipse` and `Rectangle` are instantiated with specific dimensions and positions.
- The `LineConnector` connects the central ports of the ellipse and rectangle.
- Decorator properties are set to customize the appearance of the connector.

### Cross References
See also:  
- [Syncfusion Diagram Documentation](https://www.syncfusion.com/documentation/windowsforms/diagram/overview)
- [Connector Properties in Windows Forms](https://www.syncfusion.com/documentation/windowsforms/diagram/connector)

<!-- tags: [diagram, windows forms, connector, syncfusion, 11.4.0.26] keywords: [ellipse, rectangle, lineconnector, connector properties, midway attributes, Coloring, size settings, Visual Studio, Windows Forms] -->
```