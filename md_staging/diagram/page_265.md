```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_265.jpeg
document_name: diagram
page_number: 265
page_id: diagram#page_265
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:59Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
EndPointDecoratorModel decoratorMdl =
    Global.EndPointDecoratorPalette["Filled Arrow"];

if (decoratorMdl != null)
{
    link.EndPoints.LastEndPointDecorator = decoratorMdl.CreateInstance();
}
```

[VB.NET]

```vb
' Create a directional link.
Dim link As New LinkLabel.Link(pts)
Dim decoratorMdl As EndPointDecoratorModel =
    Global.EndPointDecoratorPalette("Filled Arrow")
If Not (decoratorMdl Is Nothing) Then
    link.EndPoints.LastEndPointDecorator = decoratorMdl.CreateInstance()
End If
```

## 5.12 How To Detect Whether a New Link Has Been Added / Removed From a Diagram

You can use the `Diagram.Model.ConnectionsChangeComplete` event to detect whether a new link has been added / removed from a diagram.

The following code snippet illustrates how to detect a new link that has been added to the diagram, and the symbols connected by the new link. It also illustrates how to remove a link that connects symbols of the same type.

### Detecting a New Link Added to the Diagram

```csharp
// Use the Diagram.ConnectionsChangeComplete event to be notified of the creation of a new Link.
// The Link.FromNode and Link.ToNode properties provide access to the symbols that the link connects.
private void diagram1_ConnectionsChangeComplete(object sender,
    Syncfusion.Windows.Forms.Diagram.ConnectionCollectionEventArgs evtArgs)
{
    if ((evtArgs.ChangeType == Syncfusion.Windows.Forms.Diagram.CollectionExChangeType.Insert) &&
        (evtArgs.Connection != null))
    {
        Connection newconn = evtArgs.Connection;
    }
}
```
```