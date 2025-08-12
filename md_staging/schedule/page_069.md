```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_069.jpeg
document_name: schedule
page_number: 069
page_id: schedule#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:02Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

```csharp
scheduleControl1.PerformSwitchToScheduleViewTypeClick(ScheduleViewType.Month);
```

```vb.net
' Switches the display to Month View.
scheduleControl1.PerformSwitchToScheduleViewTypeClick(ScheduleViewType.Month)
```

## 5.4 How to obtain the date that is clicked in the ScheduleControl

The Clicked DateTime value of a Schedule Control can be obtained by handling the `ScheduleAppointmentClick` event as shown in the following code snippet.

### Code Example in C#

```csharp
// Subscribe to item click event.
this.scheduleControl1.ScheduleAppointmentClick += new ScheduleAppointmentClickEventHandler(scheduleControl1_ScheduleAppointmentClick);

// Sample event handler to catch clicks on the schedule control.
private void scheduleControl1_ScheduleAppointmentClick(object sender, ScheduleAppointmentClickEventArgs e)
{
    Console.WriteLine("scheduleControl1_ScheduleAppointmentClick: {0} {1}", e.ClickType, e.ClickDateTime);
}
```

### Code Example in VB.NET

```vb.net
' Subscribe to item click event
AddHandler scheduleControl1.ScheduleAppointmentClick, AddressOf scheduleControl1_ScheduleAppointmentClick

' Sample event handler to catch clicks on the schedule control.
Private Sub scheduleControl1_ScheduleAppointmentClick(ByVal sender As Object, ByVal e As ScheduleAppointmentClickEventArgs)
    Console.WriteLine("scheduleControl1_ScheduleAppointmentClick: {0} {1}", e.ClickType, e.ClickDateTime)
End Sub
```

## API Reference

### Methods
- `PerformSwitchToScheduleViewTypeClick(ScheduleViewType.Month)`: Changes the display of the Schedule Control to the specified view type.
- `ScheduleAppointmentClick`: Event that is triggered when a specific date or time is clicked in the Schedule Control.

### Properties
- `ClickType`: Indicates the type of click that occurred.
- `ClickDateTime`: Represents the DateTime value of the clicked date or time.

## Code Examples

The provided examples demonstrate how to:
1. Switch the Schedule Control to different view types using the `PerformSwitchToScheduleViewTypeClick` method.
2. Handle the `ScheduleAppointmentClick` event to capture the clicked DateTime and ClickType information.

## Cross References

For more information on the Schedule Control and its various features, refer to the following sections:
- Schedule Control Overview
- Customizing Schedule Views
- Handling Schedule Events

<!-- tags: [syncfusion-windows-forms, schedule-control, event-handling, c#, vb.net, datetime-click] keywords: [scheduleviewtype, scheduleappointmentclick, performswitchtoscheduleviewtypeclick, clickdatetime, clicktype] -->
```