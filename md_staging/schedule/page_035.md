```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: schedule
page_number: 035
page_id: schedule#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:09:41Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- This page demonstrates the process of entering and saving appointments in the ScheduleControl using the WinForms interface.
- It explains how to fill out the appointment details in the "Enter Appointment" screen, including subject, location, time, and other fields.
- The section details the behavior of the "Save and Close" button and the tooltip functionality when hovering over an appointment in the ScheduleGrid.

## Content

### Enter Appointment Screen

#### Figure 24: A filled-in New Appointment Screen

The "Enter Appointment" screen allows users to input details for a new appointment. The filled-in fields are as follows:
- **Subject**: Dr Appt
- **Location**: Asheville Med Center
- **Label**: Important
- **Start Time**: 11/ 9/2006 at 10:00 AM
- **End Time**: 11/ 9/2006 at 11:00 AM (1 hours)
- **All Day Event**: Not selected
- **Reminder**: Not set
- **Show time as**: Busy
- **Description**: Regular checkup - make sure to bring insurance card

#### Button Actions
12. Clicking the **Save and Close** button on the Appointment screen will re-display the Day view ScheduleControl with the new appointment displayed. If you hover over the appointment in the ScheduleGrid, a tooltip will display as shown below.

## API Reference (if applicable)
- **Method**: `SaveAndClose()`
  - **Behavior**: Saves the appointment details and closes the appointment editor.
  - **Returns**: None
  - **Purpose**: Updates the ScheduleControl with the new appointment and stores it in the schedule.

## Code Examples (multi-language supported)
```csharp
// Example of saving an appointment
private void SaveAppointment()
{
    var appointment = new EventInfo();
    appointment.StartTime = new DateTime(2006, 11, 9, 10, 0, 0);
    appointment.EndTime = new DateTime(2006, 11, 9, 11, 0, 0);
    appointment.Subject = "Dr Appt";
    appointment.Location = "Asheville Med Center";
    appointment.IsAllDay = false;
    appointment.Label = "Important";
    appointment.BusyStatus = BusyStatus.Busy;
    appointment.Description = "Regular checkup - make sure to bring insurance card";

    scheduleControl1.CurrentViewSettings.Appointments.Add(appointment);
    scheduleControl1.SaveAndClose();
}
```

## Page-level Navigation/TOC (if applicable)
- **Overview**
- **Enter Appointment Screen**
  - Button Actions
- **API Reference**
- **Code Examples**

## Cross References
- See also: [ScheduleControl Overview](#schedulecontrol-overview), [Appointment Editing](#appointment-editing), [Tooltip Configuration](#tooltip-configuration)

## RAG Annotations
<!-- tags: [ScheduleControl, Windows Forms, Appointment Editor, Tooltip, Save and Close] keywords: [Enter Appointment, Subject, Location, Label, Start Time, End Time, Reminder, Show time as] -->
```