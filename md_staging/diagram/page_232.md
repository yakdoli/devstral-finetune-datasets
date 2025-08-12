```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_232.jpeg
document_name: diagram
page_number: 232
page_id: diagram#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:54Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Instructions on handling events programmatically in Diagram.
- Implementation in both C# and VB.NET.
- Example of handling `PortsChanged` event.

## Content

Programmatically, the events are handled as follows.

### Handling Events in C#

```csharp
[C#]

public void Form1_Load(object sender, EventArgs e)
{
    ((DocumentEventSink)modell.EventSink).PortsChanged += new CollectionExEventHandler(Form1_PortsChanged);
    node.EnableCentralPort = false;
}

void Form1_PortsChanged(CollectionExEventArgs evtArgs)
{
    MessageBox.Show("Port is changed");
}
```

### Handling Events in VB.NET

```vb
[VB]

Public Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(modell.EventSink, DocumentEventSink).PortsChanged, AddressOf Form1_PortsChanged
    node.EnableCentralPort = False
End Sub

Private Sub Form1_PortsChanged(ByVal evtArgs As CollectionExEventArgs)
    MessageBox.Show("Port is changed")
End Sub
```

Sample diagram is as follows.

<!-- tags: [diagram, event handling, portschanged, windows forms, syncfusion, c#, vb.net] keywords: [portschange event, enable central port, message box, visual basic] -->
```