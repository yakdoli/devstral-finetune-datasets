```xml
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_229.jpeg
document_name: tools
page_number: 229
page_id: tools#page_229
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:48:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vbnet
[VB.NET]

Private Sub dockingManager1_DragFeedbackStart(ByVal sender As Object, ByVal e As System.EventArgs)
    Console.WriteLine("DragFeedbackStart Event has been ")
    Dim ctrl As Syncfusion.Windows.Forms.Tools.DockingManager = CType(ConversionHelpers.ASWorkaround(sender, GetType(Syncfusion.Windows.Forms.Tools.DockingManager)), Syncfusion.Windows.Forms.Tools.DockingManager)
    Dim ienum As IEnumerator = ctrl.Controls
    Dim dockedctrls As ArrayList = New ArrayList
    While ienum.MoveNext
        dockedctrls.Add(ienum.Current)
    End While
    For Each c As Control In dockedctrls
        Console.WriteLine("Control Name :" + c.Name)
    Next
End Sub
```

## DragFeedbackStop Event

The DragFeedbackStop event occurs immediately after the end of the feedback of a drag operation. When the docked control is dragged from its position and locates another position, this event will be raised. Whenever the mouse click is released from dragging, the drag feedback is stopped and DragFeedbackStop event will be triggered.

| Member | Description |
|--------|-------------|
| Control | Gets the docked control which is dragged. |

```json
{
  "Copyright": "2013 Syncfusion. All rights reserved.",
  "Page Number": "229"
}
```
```