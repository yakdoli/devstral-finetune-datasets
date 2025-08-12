```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: schedule
page_number: 068
page_id: schedule#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:41Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview

- Demonstrates how to set the schedule appointments as read-only.
- Explains how to change the current display to a desired Schedule View Type.

## Content

### 5.2 How to set the schedule appointments as read-only

You can achieve this by canceling the **ScheduleAppointmentClick** event of the ScheduleControl. Please refer the below code snippet which illustrates this.

```csharp
[C#]

// Handle the ScheduleAppointmentClick event.
this.scheduleControl1.ScheduleAppointmentClick += new
ScheduleAppointmentClickEventHandler(scheduleControl1_ScheduleAppointmentClick);

private void scheduleControl1_ScheduleAppointmentClick(object sender,
ScheduleAppointmentClickEventArgs e)
{
    // Cancel the event.
    e.Cancel = true;
}
```

```vb.net
[VB.NET]

' Handle the ScheduleAppointmentClick event.
AddHandler ScheduleControl1.ScheduleAppointmentClick, AddressOf
ScheduleControl1_ScheduleAppointmentClick

Private Sub scheduleControl1_ScheduleAppointmentClick(ByVal sender As Object, ByVal e As ScheduleAppointmentClickEventArgs)
    ' Cancel the event.
    e.Cancel = True
End Sub
```

### 5.3 How to change the current display to a desired Schedule View Type

The current display of a ScheduleControl can be changed to a desired view type by invoking the **PerformSwitchToScheduleViewTypeClick** method and passing the desired view as parameter.

```csharp
[C#]

// Switches the display to Month View.
```

## Page-level Navigation/TOC (if applicable)

- 5.2 How to set the schedule appointments as read-only
- 5.3 How to change the current display to a desired Schedule View Type

## Cross References

- Refer to the ScheduleControl documentation for more details on its properties and methods.
- See also: ScheduleAppointmentClick, PerformSwitchToScheduleViewTypeClick

<!-- tags: [Essential Schedule, Windows Forms, ScheduleControl, ScheduleAppointmentClick, PerformSwitchToScheduleViewTypeClick] keywords: [ScheduleControl, ScheduleAppointmentClick, read-only, Schedule View Type, Month View] -->
```