```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_286.jpeg
document_name: diagram
page_number: 286
page_id: diagram#page_286
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:26:11Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

```csharp
// Set up the Source and Target ports for the Link.
linkcommand.SourcePort = symbol1.CenterPort;
linkcommand.TargetPort = symbol2.CenterPort;

// Execute the command to connect the two symbols.
this.diagram.Controller.ExecuteCommand(linkcommand);
```

### [VB.NET]

```vb
'Create a LinkCmd object.
Dim linkcommand As New LinkCmd()
linkcommand.Link = New Link(Link.Shapes.Line)

'Set up the Source and Target ports for the Link.
linkcommand.SourcePort = symbol1.CenterPort
linkcommand.TargetPort = symbol2.CenterPort

'Execute the command to connect the two symbols.
Me.diagram.Controller.ExecuteCommand(linkcommand)
```

### 5.27 How To Retain the Custom Position Of the Label While Resizing the Node

We can retain the label's offset value using the **SizeChanged** event. While resizing a node, the **SizeEvent** gets fired. Using this event we can retain the label's position.

```csharp
[C#]

// Adding Event Handler
((DocumentEventSink)diagram1.Model.EventSink).SizeChanged += new
SizeChangedEventHandler(Form1_SizeChanged);
outerRect.Labels.Add(new Syncfusion.Windows.Forms.Diagram.Label());
outerRect.Labels[0].Text = "Rectangle";
outerRect.Labels[0].Position = Position.Custom;
outerRect.Labels[0].OffsetX = outerRect.Size.Width / 2;
outerRect.Labels[0].OffsetY = outerRect.Size.Height;

// Resizing
void Form1_SizeChanged(SizeChangedEventArgs evtArgs)
{
    outerRect.Labels[0].OffsetX = outerRect.Size.Width / 2;
}
```

## Cross References

See also:
- [Product Documentation Link]

<!-- tags: [product, module, control, api, version?] keywords: [diagram, windows forms, link command, node resizing, label position, sizechanged event, syncfusion] -->
```