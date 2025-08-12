```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_268.jpeg
document_name: diagram
page_number: 268
page_id: diagram#page_268
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:16Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
private void EventSink_NodeCollectionChanged(CollectionExEventArgs evtArgs)
{
    Node n = evtArgs.Element as Node;

    // ChangeType specifies whether the Collection change is Insertion/Removal
    if (evtArgs.ChangeType == CollectionExChangeType.Insert)
    {
        this.label2.ForeColor = Color.Blue;

        // Gets the Name of the inserted element
        this.label2.Text = "Last Node Added : " + n.Name.ToString();
    }
    else if (evtArgs.ChangeType == CollectionExChangeType.Remove)
    {
        this.label2.ForeColor = Color.Red;

        // Gets the Name of the removed element
        this.label2.Text = "Last Node Removed : " + n.Name.ToString();
    }
}
```

## [VB.NET]

```vb.net
EventSink.NodeCollectionChanged += New CollectionExEventHandler(EventSink_NodeCollectionChanged)

Me.Diagram1.Model.EventSink.NodeCollectionChanged += New CollectionExEventHandler(EventSink_NodeCollectionChanged)

' ChildrenChangeComplete Event
' Update Label2 depending on whether a Shape is added or deleted from the Diagram
Private Sub Model_ChildrenChangeComplete(ByVal evtArgs As CollectionExEventArgs)
    Dim n As Node = TryCast(evtArgs.Element, Node)
    ' ChangeType specifies whether the Collection change is Insertion/Removal
    If evtArgs.ChangeType = CollectionExChangeType.Insert Then
        Me.label2.ForeColor = Color.Blue

        ' Gets the Name of the inserted element
        Me.label2.Text = "Last Node Added: " + n.Name.ToString()
    End If
End Sub
```

---

## API Reference

- Namespace: EssentialDiagram
- Class: Diagram
- Event: `NodeCollectionChanged`
  - Parameters:
    - `evtArgs`: CollectionExEventArgs
    - ChangeType: Specifies whether the node change is an Insertion or Removal.
  - Description: Triggered when a node is added or removed from the collection.
- Properties:
  - FontColor: Changes the foreground color of the label based on the action (Insert or Remove).

---

## Code Examples

### C#

```csharp
private void EventSink_NodeCollectionChanged(CollectionExEventArgs evtArgs)
{
    Node n = evtArgs.Element as Node;

    if (evtArgs.ChangeType == CollectionExChangeType.Insert)
    {
        this.label2.ForeColor = Color.Blue;
        this.label2.Text = "Last Node Added : " + n.Name.ToString();
    }
    else if (evtArgs.ChangeType == CollectionExChangeType.Remove)
    {
        this.label2.ForeColor = Color.Red;
        this.label2.Text = "Last Node Removed : " + n.Name.ToString();
    }
}
```

### VB.NET

```vb.net
Private Sub Model_ChildrenChangeComplete(ByVal evtArgs As CollectionExEventArgs)
    Dim n As Node = TryCast(evtArgs.Element, Node)
    If evtArgs.ChangeType = CollectionExChangeType.Insert Then
        Me.label2.ForeColor = Color.Blue
        Me.label2.Text = "Last Node Added: " + n.Name.ToString()
    End If
End Sub
```

---

<!-- tags: [EssentialDiagram, Windows Forms, NodeCollectionChanged, Insert, Remove, Label, ChangeType] keywords: [insertion, removal, node, label, change, event] -->
```