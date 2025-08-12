```html
<!-- source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_113.jpeg
document_name: diagram
page_number: 113
page_id: diagram#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:58Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Open45Arrow
- Open60Arrow
- OpenFancyArrow
- ReverseArrow
- ReverseDoubleArrow
- Square

## Connecting Two Nodes with Line Connector

The following code example illustrates how to create links between two nodes.

### C#

```csharp
protected void Page_Load(object sender, EventArgs e)
{
    Syncfusion.Windows.Forms.Diagram.Ellipse ellipse = new Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 110, 70);
    Syncfusion.Windows.Forms.Diagram.Rectangle rectangle = new Syncfusion.Windows.Forms.Diagram.Rectangle(300, 50, 50, 80);
    Syncfusion.Windows.Forms.Diagram.LineConnector lineconnector = new Syncfusion.Windows.Forms.Diagram.LineConnector(new System.Drawing.PointF(10, 200), new System.Drawing.PointF(300, 250));
    this.DiagramWebControl1.Model.AppendChild(ellipse);
    this.DiagramWebControl1.Model.AppendChild(rectangle);
    ellipse.CentralPort.TryConnect(lineconnector.HeadEndPoint);
    rectangle.CentralPort.TryConnect(lineconnector.TailEndPoint);
    this.DiagramWebControl1.Model.AppendChild(lineconnector);
}
```

### VB

```vb
Protected Sub Page_Load(ByVal sender As Object, ByVal e As EventArgs)
    Dim ellipse As New Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 110, 70)
    Dim rectangle As New Syncfusion.Windows.Forms.Diagram.Rectangle(300, 50, 50, 80)
    Dim lineconnector As New Syncfusion.Windows.Forms.Diagram.LineConnector(New System.Drawing.PointF(10, 200), New System.Drawing.PointF(300, 250))
    Me.DiagramWebControl1.Model.AppendChild(ellipse)
    Me.DiagramWebControl1.Model.AppendChild(rectangle)
    ellipse.CentralPort.TryConnect(lineconnector.HeadEndPoint)
    rectangle.CentralPort.TryConnect(lineconnector.TailEndPoint)

    Me.DiagramWebControl1.Model.AppendChild(lineconnector)
End Sub
```
<!-- tags: [diagram, windows forms, line connector, nodes, syncfusion winforms, program guide] keywords: [diagram, windows forms, line connector, nodes, syncfusion, winforms, example, C#, VB, page load, control, append child, try connect] -->
```