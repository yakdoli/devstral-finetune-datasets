```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_224.jpeg
document_name: diagram
page_number: 224
page_id: diagram#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:15Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms  

### C#

```csharp
void Form1_FlipChanging(FlipChangingEventArgs evtArgs)
{
    MessageBox.Show("FlipChanging event is fired");
    textBox1.Text = evtArgs.NodeAffected.BoundingRectangle.ToString();
}

void Form1_FlipChanged(FlipChangedEventArgs evtArgs)
{
    MessageBox.Show("FlipChanged event is fired" + "\n" + "Flip Axis:" + evtArgs.FlipAxis.ToString() + "\n" + "Node: " + evtArgs.NodeAffected.Name.ToString());
    evtArgs.NodeAffected.EditStyle.Enabled = false;
}
```

### [VB]

```vb
Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).FlipChanged, AddressOf Form1_FlipChanged
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).FlipChanging, AddressOf Form1_FlipChanging
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).RotationChanged, AddressOf Form1_RotationChanged
    AddHandler DirectCast(model1.EventSink, DocumentEventSink).RotationChanging, AddressOf Form1_RotationChanging
    ' Circle
    Dim circle As New Syncfusion.Windows.Forms.Diagram.Ellipse(0, 0, 96, 72)
    circle.Name = "Circle"
    circle.FillStyle.Type = FillStyleType.LinearGradient
    circle.FillStyle.ForeColor = Color.AliceBlue
    circle.ShadowStyle.Visible = True
    model4.AppendChild(circle)
End Sub

Private Sub Form1_RotationChanged(ByVal evtArgs As RotationChangedEventArgs)
    MessageBox.Show(("RotationChanged event is fired" & vbLf) + evtArgs.RotationOffset.ToString())
End Sub

Private Sub Form1_FlipChanging(ByVal evtArgs As FlipChangingEventArgs)
    MessageBox.Show("FlipChanging event is fired")
    textBox1.Text = evtArgs.NodeAffected.BoundingRectangle.ToString()
End Sub

Private Sub Form1_FlipChanged(ByVal evtArgs As FlipChangedEventArgs)
    MessageBox.Show((("FlipChanged event is fired" & vbLf & "Flip Axis:") + evtArgs.FlipAxis.ToString() & vbLf & "Node: ") + evtArgs.NodeAffected.Name.ToString())
    evtArgs.NodeAffected.EditStyle.Enabled = False
End Sub
```

## API Reference  

### Members Referenced
- `FlipChangingEventArgs`
- `FlipChangedEventArgs`
- `EventSink`
- `Diagram`
- `Ellipse`
- `FillStyle`
- `ShadowStyle`
- `RotationChangedEventArgs`
- `Model`

## Code Examples  

### Example: Handling Flip and Rotation Events  

#### C#

```csharp
// Event Handler for FlipChanging
void FlipChangingHandler(FlipChangingEventArgs evtArgs)
{
    // Display message and update UI
    MessageBox.Show("FlipChanging event is fired");
    textBox1.Text = evtArgs.NodeAffected.BoundingRectangle.ToString();
}

// Event Handler for FlipChanged
void FlipChangedHandler(FlipChangedEventArgs evtArgs)
{
    MessageBox.Show("FlipChanged event is fired" + "\n" + "Flip Axis:" + evtArgs.FlipAxis.ToString() + "\n" + "Node: " + evtArgs.NodeAffected.Name.ToString());
    evtArgs.NodeAffected.EditStyle.Enabled = false;
}
```

#### VB.NET

```vb
' Event Handler for RotationChanged
Private Sub RotationChangedHandler(ByVal evtArgs As RotationChangedEventArgs)
    MessageBox.Show(("RotationChanged event is fired" & vbLf) + evtArgs.RotationOffset.ToString())
End Sub

' Event Handler for FlipChanging
Private Sub FlipChangingHandler(ByVal evtArgs As FlipChangingEventArgs)
    MessageBox.Show("FlipChanging event is fired")
    textBox1.Text = evtArgs.NodeAffected.BoundingRectangle.ToString()
End Sub

' Event Handler for FlipChanged
Private Sub FlipChangedHandler(ByVal evtArgs As FlipChangedEventArgs)
    MessageBox.Show((("FlipChanged event is fired" & vbLf & "Flip Axis:") + evtArgs.FlipAxis.ToString() & vbLf & "Node: ") + evtArgs.NodeAffected.Name.ToString())
    evtArgs.NodeAffected.EditStyle.Enabled = False
End Sub
```

<!-- tags: [Syncfusion Winforms, Diagram Control, Events, FlipChanging, FlipChanged, RotationChanged, RotationChanging] keywords: [Diagram, Flip, Rotation, EventHandling, EventArgs, Model, UI, EventSink, EventHandler, Object, EventArgs, MessageBox, C#, VB.NET] -->
```