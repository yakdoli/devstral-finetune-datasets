```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: schedule
page_number: 072
page_id: schedule#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:54Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview

- Demonstrates how to configure the appearance and formatting of appointments in the Schedule Control.
- Explains how to enable and set transparency levels for span appointments.

## Content

### How to set the Transparency Level of a Span Appointment

The `EnableTransparentSpan` property is used to enable transparency in Span appointments. Once you have enabled this property, you can set the transparency level (from 0 through 255) by using the `SpanTransparencyLevel` property.

#### Code Example: C#
```csharp
this.scheduleControl.Appearance.EnableTransparentSpan = true;
this.scheduleControl.Appearance.SpanTransparencyLevel = 220;
```

#### Code Example: VB
```vb
Me.scheduleControl.Appearance.EnableTransparentSpan = True
Me.scheduleControl.Appearance.SpanTransparencyLevel = 220
```

#### Code Example: VB.NET
```vb
' Show the appointment time.
Me.ScheduleControl1.Appearance.ShowTime = True

// To show the appointment time based on this format.
Me.ScheduleControl1.Appearance.WeekMonthItemFormat = "[subject] [starttime][endtime]"

// Tooltip format.
Me.ScheduleControl1.Appearance.ScheduleAppointmentTipFormat = "[subject] [starttime][endtime]"

// Enable the appointment tooltip.
Me.ScheduleControl1.Appearance.ScheduleAppointmentTipsEnabled = True
```

#### Example Image
![](attachment:19)

## API Reference

- **Property**: `EnableTransparentSpan`
  - Type: `Boolean`
  - Description: Enables or disables transparency for span appointments.
  - Default: `False`

- **Property**: `SpanTransparencyLevel`
  - Type: `Int32`
  - Description: Sets the transparency level for span appointments (range: 0-255).
  - Default: `0`

## Code Examples

### How to Enable Transparency for Span Appointments

#### C#
```csharp
this.scheduleControl.Appearance.EnableTransparentSpan = true;
this.scheduleControl.Appearance.SpanTransparencyLevel = 220;
```

#### VB
```vb
Me.scheduleControl.Appearance.EnableTransparentSpan = True
Me.scheduleControl.Appearance.SpanTransparencyLevel = 220
```

### How to Configure Appointment Appearance

#### VB.NET
```vb
' Display the appointment time.
Me.ScheduleControl1.Appearance.ShowTime = True

// Format for displaying the appointment time.
Me.ScheduleControl1.Appearance.WeekMonthItemFormat = "[subject] [starttime][endtime]"

// Tooltip format.
Me.ScheduleControl1.Appearance.ScheduleAppointmentTipFormat = "[subject] [starttime][endtime]"

// Enable tooltips for appointments.
Me.ScheduleControl1.Appearance.ScheduleAppointmentTipsEnabled = True
```

## Page-level Navigation/TOC (if applicable)

- **Overview**
- **5.7 How to set the Transparency Level of a Span Appointment**

## Cross References

- Related Topics: [Properties of Schedule Control](#properties-of-schedule-control)
- Related Topics: [Appointment Appearance Settings](#appointment-appearance-settings)

<!-- tags: [syncfusion-sdk, winforms, schedule, transparency, span appointments, appointment appearance] keywords: [EnableTransparentSpan, SpanTransparencyLevel, Schedule Control, appointment formatting, transparency level] -->
```