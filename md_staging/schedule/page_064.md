```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: schedule
page_number: 064
page_id: schedule#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:29Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Content

### Events

| Event                | Parameters                                     | Description                               |
|----------------------|-----------------------------------------------|-------------------------------------------|
| ItemChanging        | object sender, <br> ScheduleAppointmentCancelEventArgs | Occurs after an <br> IScheduleAppointment is modified |

### Sample Link

You can get the schedule sample from the following online location,

http://asp.syncfusion.com/sfwinrepsamplebrowser/8.4.0.10/Windows/Schedule.Windows/Sample s/2.0/Schedule%20Samples/Scheduler%20With%20Recurrence%20Demo/Sample.aspx?args=0

### Adding this support to an Application

The following steps help you to get the target part in the Schedule control while dragging:

1. Create a schedule control enabled sample application
2. Add appointments in that schedule grid
3. Hook the 'ItemChanging' event

#### Code Examples

[C#]

```csharp
this.scheduleControl1.ItemChanging += new ScheduleAppointmentChangingEventHandler(scheduleControl1_ItemChanging);
```

[VB]

```vb
AddHandler scheduleControl1.ItemChanging, AddressOf scheduleControl1_ItemChanging
```

#### Get the drag hit context with the below code.

[C#]

```csharp
void scheduleControl1_ItemChanging(object sender, ScheduleAppointmentCancelEventArgs e)
```

## Copyright

© 2013 Syncfusion. All rights reserved.

---

<!-- tags: [Syncfusion Winforms, Schedule Control, Event Handlers, API Reference, Version 11.4.0.26] keywords: [ItemChanging, ScheduleAppointmentCancelEventArgs, Drag hit context, C# example, VB example, Windows Forms, Syncfusion] -->
```