```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: diagram
page_number: 239
page_id: diagram#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:20Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

```vb
Private Sub Form1_LabelsChanged(ByVal evtArgs As CollectionExEventArgs)
    MessageBox.Show("LabelsChanged event is fired" & 
        evtArgs.ChangeType.ToString() + evtArgs.Owner.ToString())
End Sub
```

### Layers Events

Programmatically, the events are written as follows:

#### [C#]

```csharp
public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)model1.EventSink).LayersChanged += new
        CollectionExEventHandler(Form1_LayersChanged);
    Layer layer0 = new Layer();
    this.diagram1.Model.Layers.Add(layer0);
    layer0.Enabled = true;
    layer0.Visible = true;
}

void Form1_LayersChanged(CollectionExEventArgs evtArgs)
{
    MessageBox.Show("LayersChanged event is fired." + "\n" + "Owner: " +
        evtArgs.Owner.ToString());
}
```

#### [VB]

```vb
Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(model1.EventSink,
        DocumentEventSink).LayersChanged, AddressOf Form1_LayersChanged
    Dim layer0 As New Layer()
    Me.diagram1.Model.Layers.Add(layer0)
    layer0.Enabled = True
    layer0.Visible = True
End Sub

Private Sub Form1_LayersChanged(ByVal evtArgs As CollectionExEventArgs)
    MessageBox.Show("LayersChanged event is fired." & vbLf & "Owner: " & 
        evtArgs.Owner.ToString())
End Sub
```

### Sample diagram is as follows,

---

© 2013 Syncfusion. All rights reserved.  **239** | Page
```