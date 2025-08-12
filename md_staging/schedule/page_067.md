```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: schedule
page_number: 067
page_id: schedule#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:53Z
fidelity: lossless
-->

# 5 Frequently Asked Questions

This section comprises the following topics:

## 5.1 How to disable the drag behavior of schedule appointments in the ScheduleControl

You can do this by invoking the **ItemChanging** event of the ScheduleControl, and canceling the **ItemDrag** action, as shown in the below code snippet.

### C#

```csharp
// Handle the ItemChanging event.
this.scheduleControl1.ItemChanging += new
ScheduleAppointmentChangingEventHandler(scheduleControl1_ItemChanging);

private void scheduleControl1_ItemChanging(object sender,
    Syncfusion.Schedule.ScheduleAppointmentCancelEventArgs e)
{
    // Cancel the ItemDrag action.
    if (e.Action == ItemAction.ItemDrag)
    {
        e.Cancel = true;
    }
}
```

### VB.NET

```vb
' Handle the ItemChanging event.
AddHandler Me.scheduleControl1.ItemChanging, AddressOf
scheduleControl1_ItemChanging

Private Sub scheduleControl1_ItemChanging(ByVal sender As Object, ByVal
    e As Syncfusion.Schedule.ScheduleAppointmentCancelEventArgs)
    ' Cancel the ItemDrag action.
    If e.Action = ItemAction.ItemDrag Then
        e.Cancel = True
    End If
End Sub
```

### Page-Level Navigation/TOC
This section focuses on removing scheduling behavior from appointments in the ScheduleControl through event handling and coding examples in both C# and VB.NET.

### Cross References
See also: 
- ScheduleControl documentation
- Event handling in Windows Forms

<!-- tags: [Syncfusion, ScheduleControl, Windows Forms, Drag Behavior, Event Handling] keywords: [ItemChanging, ScheduleControl, ItemDrag, C#, VB.NET, appointments] -->
```