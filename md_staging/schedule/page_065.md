<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: schedule
page_number: 065
page_id: schedule#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:50Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Draggable Scheduling

The following code snippet demonstrates how to track the `ItemDrag` action in a scheduling control and determine the drop area during the drag action.

### C#

```csharp
{
    if (e.Action == ItemAction.ItemDrag)
    {
        Console.WriteLine("Dropped Area :" + e.ItemDragHitContext);
    }
}
```

### VB.NET

```vb
[VB]

Private Sub scheduleControl1_ItemChanging(ByVal sender As Object, ByVal e As ScheduleAppointmentCancelEventArgs)
    If e.Action = ItemAction.ItemDrag Then
        Console.WriteLine("Dropped Area :" + e.ItemDragHitContext.ToString())
    End If
End Sub
```

### Cancelling the Dropped Item

You can cancel the dropped item using the `ItemDragHitContext` property as shown below.

#### C#

```csharp
[VB]
void scheduleControl1_ItemChanging(object sender,
    ScheduleAppointmentCancelEventArgs e)
{
    if (e.ItemDragHitContext == ItemDragHitContext.Calendar)
        e.Cancel = true;
}
```

#### VB.NET

```vb
[VB]
Private Sub scheduleControl1_ItemChanging(ByVal sender As Object, ByVal e As ScheduleAppointmentCancelEventArgs)
    If e.ItemDragHitContext = ItemDragHitContext.Calendar Then
        e.Cancel = True
    End If
End Sub
```

## Related Information

See also: [Syncfusion Windows Forms Documentation](https://www.syncfusion.com/products/windowsforms)

<!-- tags: [schedule, windowsforms, itemdrag, itemdraghitcontext, cancelling, draganddrop, synchronize, functionality, eventactions] keywords: [schedulecontrol, itemdrag, itemdraghitcontext, draganddrop, cancellingdrag] -->