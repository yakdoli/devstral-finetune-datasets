```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: schedule
page_number: 020
page_id: schedule#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:08:32Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- A Custom view allows up to eight individual days to be displayed in the ScheduleGrid.
- Views can be easily switched using the ScheduleControl.PerformSwitchToScheduleViewType method.
- Screen shots illustrate different types of views.

## Content

### Schedule Grid Views

#### Custom View
A Custom view enables you to display up to eight individual days in the ScheduleGrid. You can easily switch views by using the ScheduleControl.PerformSwitchToScheduleViewTypeClick method. Below are screen shots illustrating these different views.

**Figure 10: ScheduleControl Day View**

![ScheduleControl Day View](https://)

The Day view shows the schedule for Friday, 03 November 2006. It includes the following events:
- **Dr's Appt – Checkup** at 10:00
- **Lunch with George** at 12:30
- **Pick up laundry** at 13:30
- **Pick up James at airport** at 15:30
- **Jay coming over** at 17:00
- **Joint meeting with Al, Joe** and John at 18:00
- **Meeting with John and Joe** at 18:30
- **Meeting with John** at 19:00

#### WorkWeek View

Notice in the WorkWeek view snapshot below, there is a Vacation entry at the top of 10/31/2006. This entry is an All-Day entry which has no specific time assigned to it. It is simply associated with the particular date. For the Day, WorkWeek, and Custom views, All-Day entries are displayed in a frozen row at the top of the ScheduleGrid. For Week and Month views, All-Day entries are listed with the time entries.

### All-Day Entry Display

- **Day, WorkWeek, Custom Views**: All-Day entries are displayed in a frozen row at the top of the ScheduleGrid.
- **Week and Month Views**: All-Day entries are listed with the time entries.

## Code Examples

```csharp
// Example: Switching to a Custom View
scheduler.ScheduleControl.PerformSwitchToScheduleViewType(ScheduleViewType.Custom);
```

## Related Information

See also:
- ScheduleControl APIs
- ScheduleGrid properties and methods

<!-- tags: [schedule, windows forms, custom view, all-day event, workweek view, api reference] keywords: [custom view, schedulegrid, schedulecontrol, all-day event, workweek view, switch view] -->
```