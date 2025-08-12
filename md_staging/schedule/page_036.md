```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: schedule
page_number: 036
page_id: schedule#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:42Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- Demonstrates the display of a new appointment with a tooltip in the `ScheduleControl`.
- Explains how to manage and save changes made to the `ScheduleControl`.

## Content

### ScheduleControl User Interface

The form in Figure 25 showcases the `ScheduleControl` interface where you can visualize and manage appointments.

#### Figure: The New Appointment with a ToolTip Displayed

- **Calendar View**: The left panel displays the calendar view for November and December 2006, highlighting the week of November 8, 2006.
- **Time Slots**: The right panel shows a time slots format for the day, allowing the addition of events. Each time slot is color-coded, where an appointment is scheduled at **10 am: Dr Appt 10:00**.
- **Tooltip**: A tooltip is displayed for the appointment, indicating a "Regular checkup - make sure to bring insurance card."

#### Closing the Form and Saving Changes

13. Click the **Close** button on the form system menu in the upper-right corner of the form. Since the data has been modified in this `ScheduleControl`, a dialog will appear, asking whether you want to save these changes to a disk file. Click **Yes** to save the changes.

### WinForms-specific Conventions

- The `ScheduleControl` allows end-users to interact with date and time-based events visually, enabling scheduling and management functionalities.
- Appointments are added by either clicking on specific time slots or using double-click gestures. The tooltip serves as a quick reference for additional details about each event.

## API Reference

- **Namespace**: `Syncfusion.WinForms.Scheduling`
- **Class**: `ScheduleControl`
  - **Properties**
    - **Action**: Manages user interactions like adding, editing, or viewing appointments.
    - **CurrentView**: Determines how the schedule is displayed (e.g., day, week, month).
  - **Methods**
    - **SaveToFile**: Serializes the schedule details to a file, preserving user changes.

## Code Examples

### Example: Adding an Appointment to ScheduleControl

```csharp
using Syncfusion.WinForms.Scheduling;

// Assuming scheduleControl is an instance of ScheduleControl
DateTime appointmentDate = new DateTime(2006, 11, 8, 10, 0, 0);
string appointmentTitle = "Dr Appt 10:00";
string appointmentNotes = "Regular checkup - make sure to bring insurance card";

// Create an Appointment object
Appointment newAppointment = new Appointment(appointmentDate, appointmentTitle);
newAppointment.Description = appointmentNotes;

// Add the appointment to the ScheduleControl
scheduleControl.Appointments.Insert(newAppointment);

// Save the changes to a file
scheduleControl.SaveToFile("appointments.xap", ScheduleFileFormat.Xml);
```

## Page-level Navigation/TOC
- **Essential Schedule for Windows Forms**
- **Content**
    - ScheduleControl User Interface
    - Clicking and Saving Changes

## Cross References
- Refer to the "ScheduleControl Overview" section for detailed functionality and usage of the `ScheduleControl`.

## RAG Annotations
<!-- tags: [ScheduleControl, Windows Forms, Appointment Management, Tooltip Display, Save Changes] keywords: [ScheduleControl, Dr Appt, 10 am, Regular checkup, save changes] -->
```