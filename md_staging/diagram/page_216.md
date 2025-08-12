```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_216.jpeg
document_name: diagram
page_number: 216
page_id: diagram#page_216
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:44Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Code Examples

### C#

```csharp
private void Form1_VertexChanging(VertexChangingEventArgs vertexChange)
{
    MessageBox.Show("VertexChanging fired");
    model1.LineStyle.LineWidth = 2;
}

private void Form1_VertexChanged(VertexChangedEventArgs vertexChange)
{
    MessageBox.Show("Target Node - " + vertexChange.NodeAffected.FullName + "\n" +
                    vertexChange.VertexLocation.ToString());
}
```

### VB

```vb
Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).VertexChanged, AddressOf Form1_VertexChanged
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).VertexChanging, AddressOf Form1_VertexChanging
    Dim line As New LineConnector(circle.PinPoint, polygon.PinPoint)
    polygon.CentralPort.TryConnect(line.HeadEndPoint)
    circle.CentralPort.TryConnect(line.TailEndPoint)
    model1.AppendChild(line)
End Sub

Private Sub Form1_VertexChanging(ByVal vertexChange As VertexChangingEventArgs)
    MessageBox.Show("VertexChanging fired")
    model1.LineStyle.LineWidth = 2
End Sub

Private Sub Form1_VertexChanged(ByVal vertexChange As VertexChangedEventArgs)
    MessageBox.Show("Target Node - " & vertexChange.NodeAffected.FullName & vbCrLf) &
               vertexChange.VertexLocation.ToString()
End Sub
```

## Page-level Navigation/TOC (if applicable)
- The document focuses on handling vertex changing and vertex changed events in a Windows Forms application using Syncfusion's Essential Diagram component.

## Cross References
- See also: Diagramming, Vertex Events, Windows Forms, Syncfusion Winforms Documentation.

<!-- tags: [Syncfusion, Winforms, Diagram, Events, VertexChanging, VertexChanged] keywords: [Essential Diagram, Windows Forms, C#, VB, VertexChangingEventArgs, VertexChangedEventArgs, Vertex events, Event handling] -->
```