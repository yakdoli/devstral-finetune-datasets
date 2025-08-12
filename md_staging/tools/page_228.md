```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_228.jpeg
document_name: tools
page_number: 228
page_id: tools#page_228
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:46:33Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### DragAllow Event

The DragAllow event occurs when a docking window is about to be dragged.

```vb
'The DragAllow event occurs when a docking window is about to be dragged.
Private Sub dockingManager1_DragAllow(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DragAllowEventArgs)
    Console.WriteLine("DragAllow Event has been triggered")
    'arg.Control property gives the reference to be dragged.
    If arg.Control = Me.panel1 Then
        'arg.Cancel is the property used to cancel the drag operation when it's in true state.
        arg.Cancel = True
    End If
End Sub
```

#### DragFeedbackStart Event

**3.4.3.8.7.2 DragFeedbackStart Event**

The DragFeedbackStart event is fired just before the start of the feedback of a drag operation. When the docked control is dragged from its position to locate some position, this event will be raised.

| Member   | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| Control  | Gets the docked control which is about to be dragged.                     |

---

### DragFeedbackStart Event in C#

```csharp
// The DragFeedbackStart event occurs just before the start of feedback of a drag operation.
// It occurs after the DragAllow Event.
private void dockingManager1_DragFeedbackStart(object sender, System.EventArgs e)
{
    Console.WriteLine("DragFeedbackStart Event has been ");
    // The following code is used to display all control names which are in the Docking Manager.
    Syncfusion.Windows.Forms.Tools.DockingManager ctrl = sender as Syncfusion.Windows.Forms.Tools.DockingManager;
    IEnumerator ienum = ctrl.Controls;
    ArrayList dockedctrls = new ArrayList();
    while (ienum.MoveNext())
        dockedctrls.Add(ienum.Current);
    foreach (Control c in dockedctrls)
    {
        Console.WriteLine("Control Name :" + c.Name);
    }
}
```

## Page-level Navigation/TOC (if applicable)
- **DragAllow Event**
- **DragFeedbackStart Event**

## RAG Annotations
<!-- tags: [DragAllow, DragFeedbackStart, Windows Forms, Syncfusion, Docking Manager] keywords: [DragAllow, DragFeedbackStart, Docked Control, Drag Operation, Feedback, Windows Forms, Syncfusion Winforms, DockManager] -->
```