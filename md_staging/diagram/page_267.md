```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_267.jpeg
document_name: diagram
page_number: 267
page_id: diagram#page_267
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:44Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```Visual Basic
If Not (newlink Is Nothing) AndAlso Not (newlink.FromNode Is Nothing) AndAlso Not (newlink.ToNode Is Nothing) Then
    Trace.WriteLine("A new link was added to the Diagram")
    Dim tailsymbol As Symbol = newlink.FromNode
    Dim headsymbol As Symbol = newlink.ToNode
    If tailsymbol.Nodes.Count = headsymbol.Nodes.Count AndAlso tailsymbol.Nodes(0).Name = headsymbol.Nodes(0).Name Then
        ' Comparing the symbol's child nodes count and child
        ' node type is a simplistic way
        ' to determine whether the two symbols are of the same
        ' type.
        Trace.WriteLine("The two symbols are of the same type.")
    End If

    ' Use the RemoveNodesCmd to delete the new link
    Dim removecmd As New RemoveNodesCmd
    removecmd.Nodes.Add(newlink)
    Me.diagram1.Controller.ExecuteCommand(removecmd)
End If
End If
End If
End Sub
```

## 5.13 How To Detect Whether a New Symbol Or Shape Has Been Added / Removed From A Diagram

You can make use of the `Diagram.Model.EventSink.NodeCollectionChanged` to detect whether a new node (symbol, shape or link) has been added/removed from a diagram. The event's `CollectionExEventArgs` argument provides information about the node ensuing the add / remove operation.

The following code snippet updates a label with information on the type of the node that is added/deleted from the diagram.

```C#
diagram1.Model.EventSink.NodeCollectionChanged += new CollectionExEventHandler(EventSink_NodeCollectionChanged);

//ChildrenChangeComplete Event
//Update Label2 depending on whether a Shape is added or deleted from the Diagram
```

## API Reference (if applicable)

### Methods
- `EventSink_NodeCollectionChanged`
  - **Parameters**: 
    - `object sender`: The source of the event.
    - `EventArgs e`: Event data indicating the operation (add or delete) and the node type.

## Code Examples (multi-language supported)

### C#
```csharp
diagram1.Model.EventSink.NodeCollectionChanged += new CollectionExEventHandler(EventSink_NodeCollectionChanged);

void EventSink_NodeCollectionChanged(object sender, EventArgs e)
{
    // Implementation to handle node addition or deletion
}
```

### VB.NET
```vb
diagram1.Model.EventSink.NodeCollectionChanged += New CollectionExEventHandler(AddressOf EventSink_NodeCollectionChanged)

Sub EventSink_NodeCollectionChanged(ByVal sender As Object, ByVal e As EventArgs)
    ' Implementation to handle node addition or deletion
End Sub
```

<!-- tags: [Diagram, Windows Forms, NodeCollectionChanged, Syncfusion.Windows.Forms.Diagram, EventHandling, Shape] keywords: [detect node addition, node deletion, diagram events, node collection changed, windows forms diagram, Syncfusion, version 11.4.0.26] -->
```