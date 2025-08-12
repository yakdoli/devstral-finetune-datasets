```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_253.jpeg
document_name: tools
page_number: 253
page_id: tools#page_253
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:10Z
fidelity: lossless
-->

## 3.4.4.2 Dock State

This property gets / sets the value indicating whether the event should be canceled.

---

### C#

```csharp
// The DockAllow event occurs when a docking window is dragged over a potential dock target.
private void dockingManager1_DockAllow(object sender, Syncfusion.Windows.Forms.Tools.DockAllowEventArgs arg)
{
    // Checks if the each controls are trying to dock with each other, by DragControl and DockControl property
    if ((arg.DragControl == this.panel1) && (arg.TargetControl == this.panel2) ||
        (arg.DragControl == this.panel2) && (arg.TargetControl == this.panel1))
    {
        // Cancel the Docking Action.
        arg.Cancel = true;
    }
}
```

---

### VB.NET

```vb
' The DockAllow event occurs when a docking window is dragged over a potential dock target.

Private Sub dockingManager1_DockAllow(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DockAllowEventArgs) Handles dockingManager1.DockAllow

    ' Checks if the each controls are trying to dock with each other, by DragControl and DockControl property
    If ((arg.DragControl Is Me.panel1) AndAlso (arg.TargetControl Is Me.panel2)) OrElse ((arg.DragControl Is Me.panel2) AndAlso (arg.TargetControl Is Me.panel1)) Then
        ' Cancel the Docking Action.
        arg.Cancel = True
    End If
End Sub
```

---

### This section covers the following topics:

This section covers the following topics:

---

<!-- tags: [syncfusion, winforms, dock manager, dock state, cancel event, c#, vb.net] keywords: [DockAllow, DockControl, DragControl, panel1, panel2, Syncfusion.Windows.Forms.Tools.DockAllowEventArgs, event handling] -->
```