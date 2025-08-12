```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_205.jpeg
document_name: diagram
page_number: 205
page_id: diagram#page_205
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:22Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
}
private void DiagramForm_ToolActivated(ToolEventArgs e)
{
    MessageBox.Show("Activated Tool Name: " + e.Tool.Name + "\n" +
    "Status: " + e.Tool.InAction);
}
}
```

### Example 1: C# Implementation
```csharp
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(diagram1.EventSink,
    DiagramViewerEventSink).ToolActivated, AddressOf
    DiagramForm_ToolActivated

    AddHandler DirectCast(diagram1.EventSink,
    DiagramViewerEventSink).ToolDeactivated, AddressOf
    Form1_ToolDeactivated

        diagram1.Controller.ActivateTool("ZoomTool")
End Sub

Private Sub Form1_ToolDeactivated(ByVal e As ToolEventArgs)
    MessageBox.Show("Deactivated Tool Name: " & e.Tool.Name)
End Sub
Private Sub DiagramForm_ToolActivated(ByVal e As ToolEventArgs)
    MessageBox.Show("Activated Tool Name: " & e.Tool.Name & vbLf & 
    "Status: ") + e.Tool.InAction)
End Sub
```

### Example 2: VB Implementation
```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    AddHandler DirectCast(diagram1.EventSink,
    DiagramViewerEventSink).ToolActivated, AddressOf
    DiagramForm_ToolActivated

    AddHandler DirectCast(diagram1.EventSink,
    DiagramViewerEventSink).ToolDeactivated, AddressOf
    Form1_ToolDeactivated

        diagram1.Controller.ActivateTool("ZoomTool")
End Sub

Private Sub Form1_ToolDeactivated(ByVal e As ToolEventArgs)
    MessageBox.Show("Deactivated Tool Name: " & e.Tool.Name)
End Sub
Private Sub DiagramForm_ToolActivated(ByVal e As ToolEventArgs)
    MessageBox.Show("Activated Tool Name: " & e.Tool.Name & vbLf & 
    "Status: ") + e.Tool.InAction)
End Sub
```

## Sample diagrams are as follows,

---

### Conclusion
The code examples demonstrate how to handle tool activation and deactivation events in a diagram control, providing notifications and status updates for the activated and deactivated tools.

<!-- tags: [Syncfusion Winforms, diagram control, event handling, diagram forms, C#, VB] keywords: [diagram, tool activation, tool deactivated, status updates, message box, event handling, C#, VB] -->
```