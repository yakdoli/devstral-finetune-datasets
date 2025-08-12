```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_071.jpeg
document_name: schedule
page_number: 071
page_id: schedule#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:05Z
fidelity: lossless
-->

## Overview
- This page discusses essential schedule formatting for Windows Forms, including settings for display formats, tooltips, and item tips.
- It covers properties like `WeekMonthItemFormat`, `ScheduleAppointmentTipFormat`, and `ScheduleAppointmentTipsEnabled` with their descriptions, data types, and usage in C# code examples.

### Formatting Options

- **WeekMonthItemFormat**
  - Specifies the display format of a schedule item shown in a week or month view. 
  - Data Type: `string`
  - Example Format: `[subject] [starttime][endtime]`

- **ScheduleAppointmentTipFormat**
  - Defines the text displayed for schedule item tips.
  - Data Type: `string`
  - Example Format: `[subject] [starttime][endtime]`

- **ScheduleAppointmentTipsEnabled**
  - Determines whether to show item tips.
  - Data Type: `Boolean`

### Format Examples

| TimeFormat       | t | WeekHeaderFormat | MMMM dd                                    |
|------------------|---|------------------|-------------------------------------------|
| WeekMonthFullFormat | dddd, dd MMMM yyyy |
| WeekMonthItemFormat | [subject] [starttime][endtime] |
| WeekMonthNewMonth   | MMMM d                                   |

### C# Code Examples

```csharp
// Show the appointment time.
this.scheduleControl.Appearance.ShowTime = true;

// To show the appointment time based on this format.
this.ScheduleControl1.Appearance.WeekMonthItemFormat = "[subject] [starttime][endtime]";

// Tooltip format.
this.ScheduleControl.Appearance.ScheduleAppointmentTipFormat = "[subject] [starttime][endtime]";

// Enable the appointment tooltip.
this.ScheduleControl1.Appearance.ScheduleAppointmentTipsEnabled = true;
```

## API Reference

- **WeekMonthItemFormat**
  - Property that specifies the display format of a schedule item shown in a week or month view.
  - Type: `string`

- **ScheduleAppointmentTipFormat**
  - Property that defines the text displayed for schedule item tips.
  - Type: `string`

- **ScheduleAppointmentTipsEnabled**
  - Property that determines whether item tips are shown.
  - Type: `Boolean`

## Code Examples (Continued)

The C# code examples demonstrate how to configure various schedule formatting properties to control the display of appointments, tooltips, and item tips in a Windows Forms application.

```html
<!-- tags: [Syncfusion, Windows Forms, schedule, formatting, tooltips, C#] keywords: [WeekMonthItemFormat, ScheduleAppointmentTipFormat, ScheduleAppointmentTipsEnabled, Windows Forms, C#] -->
```