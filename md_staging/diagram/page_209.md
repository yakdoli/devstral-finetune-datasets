```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_209.jpeg
document_name: diagram
page_number: 209
page_id: diagram#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:39Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
nodeStack.Count.ToString();

    textBox1.Text = model4.Nodes.Last.Name;

    this.diagram1.HScroll = true;
    this.diagram1.VScroll = true;
}
```

```csharp
private void Form1_OriginChanged(ViewOriginEventArgs e)
{
    textBox1.Text = "X = " + e.OriginalOrigin.X + "," + "Y = " + e.OriginalOrigin.Y + " " + "New X = " + e.NewOrigin.X + "," + "New Y = " + e.NewOrigin.Y;

}
```

## [VB]

```vb
Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)

    AddHandler DirectCast(diagram1.EventSink, DiagramViewerEventSink).OriginChanged, AddressOf Form1_OriginChanged
    Dim nodeStack As New NodeCollection()

    ' Circle

    Dim circle As New Syncfusion.Windows.Forms.Diagram.Ellipse(0, 0, 96, 72)
    circle.Name = "Circle"
    circle.FillStyle.Type = FillStyleType.LinearGradient
    circle.FillStyle.ForeColor = Color.AliceBlue
    circle.ShadowStyle.Visible = True
    nodeStack.Add(circle)

    ' Polygon

    Dim pts As PointF() = {New Point(6, 36), New Point(48, 6), New Point(90, 36), New Point(48, 66)}
    Dim polygon As New Polygon(pts)
    polygon.Name = "Polygon"
    polygon.FillStyle.ForeColor = Color.DarkSeaGreen
    polygon.FillStyle.Color = Color.DarkSeaGreen
    nodeStack.Add(polygon)

    Dim i As Integer = 0
    Me.model4.AppendChildren(nodeStack, i)
```

<!-- tags: [syncfusion, winforms, essential-diagram, diagram-viewer, origin-change, vscroll, hscroll, ellipse, polygon, fillstyle, shadowstyle] keywords: [diagram, form1, originchanged, nodecollection, circle, polygon, fillstyletype, shadowstyle, appendchildren, eventargs, diagramviewereventsink] -->
```