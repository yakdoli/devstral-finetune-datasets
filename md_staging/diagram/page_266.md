```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_266.jpeg
document_name: diagram
page_number: 266
page_id: diagram#page_266
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:52Z
fidelity: lossless
-->

### Essential Diagram for Windows Forms

```csharp
Link newlink = null;
if (newconn.SourcePort is LinkPort)
{
    newlink = newconn.SourcePort.Container as Link;
}
else if (newconn.TargetPort is LinkPort)
{
    newlink = newconn.TargetPort.Container as Link;
}
if ((newlink != null) && (newlink.FromNode != null) &&
    (newlink.ToNode != null))
{
    Trace.WriteLine("A new link was added to the Diagram");
    Symbol tailsymbol = newlink.FromNode as Symbol;
    Symbol headsymbol = newlink.ToNode as Symbol;
    if ((tailsymbol.Nodes.Count == headsymbol.Nodes.Count) &&
        (tailsymbol.Nodes[0].Name == headsymbol.Nodes[0].Name))
    {
        // Comparing the symbol's child nodes count and child
        // node type is a simplistic way
        // to determine whether the two symbols are of the same
        // type.
        Trace.WriteLine("The two symbols are of the same type.");
        
        // Use the RemoveNodesCmd to delete the new link
        RemoveNodesCmd removecmd = new RemoveNodesCmd();
        removecmd.Nodes.Add(newlink);
        this.diagram1.Controller.ExecuteCommand(removecmd);
    }
}
}
```

**[VB.NET]**

```vb
Private Sub diagram1_ConnectionsChangeComplete(ByVal sender As Object, _
    ByVal evtArgs As Syncfusion.Windows.Forms.Diagram.ConnectionCollectionEventArgs) Handles diagram1.ConnectionsChangeComplete
    If evtArgs.ChangeType = Syncfusion.Windows.Forms.Diagram.CollectionExChangeType.Insert AndAlso Not (evtArgs.Connection Is Nothing) Then
        Dim newconn As Connection = evtArgs.Connection
        Dim newlink As Link = Nothing
        If TypeOf newconn.SourcePort Is LinkPort Then
            newlink = newconn.SourcePort.Container
        End If
        If TypeOf newconn.TargetPort Is LinkPort Then
            newlink = newconn.TargetPort.Container
        End If
    End If
End Sub
```

---

<!-- tags: [Syncfusion, Winforms, Diagram] keywords: [Essential Diagram, Windows Forms, LinkPort, Connection, Symbol, RemoveNodesCmd, Controller, ExecuteCommand] -->
```