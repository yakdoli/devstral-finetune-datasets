```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: diagram
page_number: 212
page_id: diagram#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:33Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

---

### [C#]

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    ((DiagramViewerEventSink)diagram1.EventSink).MagnificationChanged += new ViewMagnificationEventHandler(Form1_MagnificationChanged);
}

[EventHandlerPriorityAttribute(true)]
private void Form1_MagnificationChanged(ViewMagnificationEventArgs evtArgs)
{
    MessageBox.Show("Old Factor: " + evtArgs.OriginalMagnification.ToString() + " New Factor: " + evtArgs.NewMagnification.ToString());
}
```

### [VB]

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(diagram1.EventSink, DiagramViewerEventSink).MagnificationChanged, AddressOf Form1_MagnificationChanged
End Sub

<EventHandlerPriorityAttribute(True)> _
Private Sub Form1_MagnificationChanged(ByVal evtArgs As ViewMagnificationEventArgs)
    MessageBox.Show("Old Factor: " & evtArgs.OriginalMagnification.ToString() & " New Factor: " & evtArgs.NewMagnification.ToString())
End Sub
```

Sample diagrams are as follows,

---

### Page-level Navigation/TOC (if applicable)

- **Essential Diagram for Windows Forms**
  - Overview
  - [C#] Example Code
  - [VB] Example Code
  - Sample diagrams

---

### Cross References

- See also: *Diagram Controls*, *Windows Forms*, *Magnification Events*, *Diagram Viewer*

---

<!-- tags: [diagram, windows forms, magnification] keywords: [event handlers, essential diagram, winforms, attendee priority] -->
```