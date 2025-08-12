```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_269.jpeg
document_name: diagram
page_number: 269
page_id: diagram#page_269
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:10Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```vb
ElseIf evtArgs.ChangeType = CollectionExChangeType.Remove Then
    Me.label2.ForeColor = Color.Red

    ' Gets the Name of the removed element
    Me.label2.Text = "Last Node Removed: " + n.Name.ToString()
End If
End Sub
```

## 5.14 How To Display ToolTips For the Symbols

ToolTips can be displayed using the Model's `MouseEnter` and `MouseLeave` events. Here is a sample where tooltips are displayed only for nodes of the type 'MySymbol'.

### C#
```csharp
private void Model_MouseEnter(object sender, NodeMouseEventArgs evtArgs)
{
    if (evtArgs.Node.GetType() == typeof(MySymbol))
    {
        this.toolTip1.SetToolTip(this.diagram1, evtArgs.Node.Name.ToString());
        this.toolTip1.Active = true;
    }
}

private void Model_MouseLeave(object sender, NodeMouseEventArgs evtArgs)
{
    this.toolTip1.Active = false;
}
```

### VB.NET
```vb
Private Sub Model_MouseEnter(ByVal sender As Object, ByVal evtArgs As Syncfusion.Windows.Forms.Diagram.NodeMouseEventArgs)
    If evtArgs.Node.Name.StartsWith("MySymbol") Then
        Me.toolTip1.SetToolTip(Me.Diagram1, evtArgs.Node.Name.ToString())
        Me.toolTip1.Active = True
    End If
End Sub
```

## Footer
© 2013 Syncfusion. All rights reserved. 269 | Page
```

<!-- tags: [product, module, control, api, version?] keywords: [Tooltip, MouseEnter, MouseLeave, Syncfusion Winforms, Diagram, type, MySymbol] -->
