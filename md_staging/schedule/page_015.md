```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: schedule
page_number: 015
page_id: schedule#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:08:28Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- This page provides an introduction to the Schedule control in Syncfusion WinForms, which offers scheduling support to Windows Forms applications through a robust class library.

## Content

### WinForms Sample Browser
The following screenshot shows the Syncfusion Tools UI component suite, which provides various tools for developing robust and flexible application interfaces in Windows Forms applications.

**Figure 6: User Interface Edition Windows Forms Sample Browser**

#### Essential Tools Overview
- Essential Tools is a comprehensive collection of UI components that facilitate rapid application development.
- It supports robust interfaces such as:
  - .NET-style docking
  - .NET-style tabbed-MDI interfaces
  - Fully customizable menus
  - Office 2007-like UIs
- Included components:
  - Tabs
  - Task menus
  - Outlook-like group bars
  - A range of text editors

#### Featured Samples
The screenshot highlights some featured samples for various UI components, including:
- Ribbon ControlAdv
- MDI Demo
- VS 2008 Tab Splitter
- Group Bar Demo
- Editor Control
- Office Style Custom Colors
- VS 2008 Drag Provider

### Schedule Samples in Windows Forms

#### Schedule Overview
- **Step 3:** Click **Schedule** from the bottom-left pane.
- Schedule samples will be displayed, showcasing scheduling functionalities in Windows Forms applications.

**Figure 7: Schedule Samples for Windows**

- **Syncfusion Essential Schedule**
- Essential Schedule is a Windows Forms class library designed to add scheduling capabilities. It is built around the grid control functionality, allowing applications to manage schedules effectively.
- **Featured Samples**
  - Scheduler Demo
  - Scheduler With Recurrence Demo

The screenshots show two samples for scheduling:
1. **Scheduler Demo**
   - Displays a basic scheduling interface with appointments like "Meeting with client" and "Lunch with John."
2. **Scheduler With Recurrence Demo**
   - Demonstrates schedules with recurring appointments, showcasing advanced scheduling features.

## Cross References
See also:
- [Syncfusion Windows Forms Documentation](#)
- [Essential Schedule Features](#)

## API Reference

### Namespace: Syncfusion.Windows.Forms.Schedule
#### Members
- **Projects**
  - **Methods**: AddAppointment(), RemoveAppointment()
  - **Events**: AppointmentAdded, AppointmentRemoved
  - **Properties**: Appointments, AppointmentColors

### Parameters
| Name         | Type         | Description                                       | Default | Required |
|--------------|--------------|---------------------------------------------------|---------|----------|
| Appointment  | Appointment   | The appointment object to be added or removed   | null    | Yes      |

### Returns
- **Appointment** - Returns the added or removed appointment object.

### Exceptions
- AppointmentAlreadyExistsException
- InvalidAppointmentException

## Code Examples

### C# Example for Adding an Appointment
```csharp
using Syncfusion.Windows.Forms.Schedule;

Scheduler scheduler = new Scheduler();

Appointment newAppointment = new Appointment();
newAppointment.StartTime = DateTime.Now;
newAppointment.EndTime = DateTime.Now.AddHours(1);
newAppointment.Subject = "Meet with team";

scheduler.AddAppointment(newAppointment);
```

### VB.NET Example for Adding an Appointment
```vb
Imports Syncfusion.Windows.Forms.Schedule

Dim scheduler As New Scheduler()

Dim newAppointment As New Appointment()
newAppointment.StartTime = DateTime.Now
newAppointment.EndTime = DateTime.Now.AddHours(1)
newAppointment.Subject = "Meet with team"

scheduler.AddAppointment(newAppointment)
```

## Footer
© 2013 Syncfusion. All rights reserved.

<!-- tags: [Essential Schedule, Windows Forms, UI Components, Scheduling] keywords: [Essential Schedule, Features, C#, VB.NET, API Reference, Scheduler Demo, Recurrence] -->
```