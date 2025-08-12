```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_003.jpeg
document_name: schedule
page_number: 003
page_id: schedule#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:46Z
fidelity: lossless
-->

## Essential Schedule for Windows Forms

### Time Interval
- **4.5 Time Interval** (Page 66)
- **4.5.1 Setting the Time Interval in Seconds Format** (Page 66)

### Frequently Asked Questions

#### How to disable the drag behavior of schedule appointments in the ScheduleControl
- **5.1 How to disable the drag behavior of schedule appointments in the ScheduleControl** (Page 67)

#### How to set the schedule appointments as read-only
- **5.2 How to set the schedule appointments as read-only** (Page 68)

#### How to change the current display to a desired Schedule View Type
- **5.3 How to change the current display to a desired Schedule View Type** (Page 68)

#### How to obtain the date that is clicked in the ScheduleControl
- **5.4 How to obtain the date that is clicked in the ScheduleControl** (Page 69)

#### How to prevent the switching of schedule view type
- **5.5 How to prevent the switching of schedule view type** (Page 70)

#### How to show the start and end time with scheduled appointments
- **5.6 How to show the start and end time with scheduled appointments** (Page 70)

#### How to set the Transparency Level of a Span Appointment
- **5.7 How to set the Transparency Level of a Span Appointment** (Page 72)

## Code Examples

#### Disable Drag Behavior
```csharp
scheduleControl.AllowDragDrop -= true;
```

#### Set Schedule Appointments as ReadOnly
```csharp
scheduleControl.ReadOnly = true;
```

#### Change Schedule View Type
```csharp
scheduleControl.CurrentView = ScheduleViewType.DayView;
```

#### Obtain Clicked Date
```csharp
private void scheduleControl_SelectedDateChanged(object sender, Syncfusion.Windows.Forms.Tools.DateTimePickerSelectedDateChangedEventArgs e)
{
    // Handle the clicked date here
}
```

#### Prevent View Type Switching
```csharp
scheduleControl.AllowEndUserViewChanging = false;
```

#### Show Start and End Time
```csharp
appointmentBase kfAppointment = new appointmentBase();
kfAppointment.StartTime = new DateTime(2023, 8, 9, 10, 0, 0);
kfAppointment.EndTime = new DateTime(2023, 8, 9, 12, 0, 0);
kfAppointment.Description = "Start: " + kfAppointment.StartTime.ToString("HH:mm") + " End: " + kfAppointment.EndTime.ToString("HH:mm");
scheduleControl.Appointments.Add(kfAppointment);
```

#### Set Transparency Level
```csharp
appointmentsBase kfSpanAppointment = new appointmentBase();
kfSpanAppointment.Text = "Span appointment";
kfSpanAppointment.StartTime = new DateTime(2023, 8, 9, 10, 0, 0);
kfSpanAppointment.EndTime = new DateTime(2023, 8, 10, 10, 0, 0);
kfSpanAppointment.AllowSpan = true;
kfSpanAppointment.Transparency = 0.5;
scheduleControl.Appointments.Add(kfSpanAppointment);
```

## Cross References

See also:
- Additional topics on managing schedule appointments and properties.
- Documentation on other ScheduleControl functionalities.

<!-- tags: [product, Syncfusion Winforms, ScheduleControl, Essential Schedule] keywords: [appointment, drag behavior, read-only, Schedule View, transparency, appointments, appointments as ReadOnly, change Schedule View Type, prevent view switching, start and end time, span appointment] -->
```