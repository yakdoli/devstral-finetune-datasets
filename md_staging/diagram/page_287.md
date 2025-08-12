```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_287.jpeg
document_name: diagram
page_number: 287
page_id: diagram#page_287
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:05Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
outerRect.Labels[0].OffsetY = outerRect.Size.Height;
```

### VB.NET

```vb.net
' Adding Event Handler
AddHandler(CType(diagram1.Model.EventSink, DocumentEventSink)).SizeChanged, AddressOf Form1_SizeChanged
outerRect.Labels.Add(New Syncfusion.Windows.Forms.Diagram.Label())
outerRect.Labels(0).Text = "Rectangle"
outerRect.Labels(0).Position = Position.Custom
outerRect.Labels(0).OffsetX = outerRect.Size.Width / 2
outerRect.Labels(0).OffsetY = outerRect.Size.Height

' Resizing
Private Sub Form1_SizeChanged(ByVal evtArgs As Syncfusion.Windows.Forms.Diagram.SizeChangedEventArgs)
    outerRect.Labels(0).OffsetX = outerRect.Size.Width / 2
    outerRect.Labels(0).OffsetY = outerRect.Size.Height
End Sub
```

## 5.28 How To Retrieve the Port Information Of a Particular Symbol

You can retrieve port information of a particular symbol using the `HandlesHitTesting.GetConnectionPointAtPoint(Node, Point)` method.

This method has two parameters: `Node` and `Point`.

- `Node` specifies the symbol in which the port resides.
- `Point` specifies the `Point` object that holds the location of the port.

### C#

```csharp
ConnectionPoint port = HandlesHitTesting.GetConnectionPointAtPoint(circle, new Point(120, 120));
```

### VB.NET

```vb.net
```

<!-- tags: [Syncfusion, WinForms, Diagram, Port Information, Symbol, HandlesHitTesting, GetConnectionPointAtPoint] keywords: [Windows Forms, Symbol, Port, Retrieval, Position, Point] -->
```