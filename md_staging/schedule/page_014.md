```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: schedule
page_number: 014
page_id: schedule#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:08:31Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

The Schedule Windows Forms samples are installed in the following location:

```
...My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Schedule.Windows\Samples\2.0
```

## Viewing Samples

To view the samples, follow the steps below:

1. Click **Start->All Programs->Syncfusion->Essential Studio <version number> -- Dashboard**.
   - The Essential Studio Enterprise Edition window is displayed.

   **Figure 5: Syncfusion Essential Studio Dashboard**

   ![Syncfusion Essential Studio Dashboard](Dashboard_Image.png)

2. In the Dashboard window, click **Run Samples for Windows Forms** under **UI Edition**. The UI Windows Form Sample Browser window is displayed.

   **Note:** You can view the samples in any of the following three ways:
   
   - **Run Samples**: Click to view the locally installed samples
   - **Online Samples**: Click to view online samples
   - **Explore Samples**: Explore BI Web samples on disk

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Scheduling
- **Class**: ScheduleControl
  - **Methods**: 
    - `public void AddAppointment(Appointment appointment)`
    - `public void DeleteAppointment(Appointment appointment)`
  - **Properties**:
    - `AppointmentStart`: Gets or sets the start time of the appointment.
    - `AppointmentEnd`: Gets or sets the end time of the appointment.
  - **Events**:
    - `AppointmentAdded`: Fired when a new appointment is added.
    - `AppointmentDeleted`: Fired when an appointment is deleted.

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Scheduling;

ScheduleControl scheduleControl = new ScheduleControl();
Appointment newAppointment = new Appointment();
newAppointment.StartTime = DateTime.Now;
newAppointment.EndTime = DateTime.Now.AddHours(2);
scheduleControl.AddAppointment(newAppointment);
```

### VB

```vb
Imports Syncfusion.Windows.Forms.Scheduling

Dim scheduleControl As New ScheduleControl()
Dim newAppointment As New Appointment()
newAppointment.StartTime = DateTime.Now
newAppointment.EndTime = DateTime.Now.AddHours(2)
scheduleControl.AddAppointment(newAppointment)
```

## Cross References

- See also: [Scheduler Controls Overview](#scheduler-control-overview), [Appointment Operations](#appointment-operations)

<!-- tags: [schedule, windows forms, samples, run, online, explore, dashboard, api] keywords: [syncfusion, windows forms, essential schedule, sample viewer, appointment, run samples, online samples, explore samples, dashboard, windows forms samples] -->
```