```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_052.jpeg
document_name: schedule
page_number: 052
page_id: schedule#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:44Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

```csharp
/// Finds an IScheduleAppointment in the collection using its
/// IScheduleAppointment.UniqueID.
IScheduleAppointment Find(object uniqueID);

/// Returns an instance of a new schedule item.
IScheduleAppointment NewScheduleAppointment();

/// Returns an IEnumerator that iterates through this list.
IEnumerator GetEnumerator();
}
```

## Overview
- **IScheduleDataProvider Interface**
  - **IScheduleDataProvider** has two functional roles. One is to manage the list of Appointment data needed by the ScheduleControl. The second role is to provide the DropList data.

## IScheduleDataProvider Interface

```csharp
public interface IScheduleDataProvider
{
    /// Provides a list of schedule items for a particular day.
    IScheduleAppointmentList GetScheduleForDay(DateTime day);

    /// Provides a list of schedule items for a range of dates.
    IScheduleAppointmentList GetSchedule(DateTime startDate, DateTime endDate);

    /// Provides a list of schedule items for a particular day and owner.
    IScheduleAppointmentList GetScheduleForDay(DateTime day, int owner);

    /// Provides a list of schedule items for a range of dates and a
    /// specified owner.
    IScheduleAppointmentList GetSchedule(DateTime startDate, DateTime endDate, int owner);

    /// Called when the ScheduleControl needs to save modifications to
    /// the schedule items back to the data store.
    void CommitChanges();

    /// Determines whether CommitChanges is called when the top-level
    /// Form holding the ScheduleControl is closed.
    SaveOnCloseBehavior SaveOnCloseBehaviorAction

    /// Gets or sets whether the data store is modified.
    bool IsDirty
}
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- See also: \[Unclear, no specific references visible\]

<!-- tags: [syncfusion, winforms, schedule, ischeduledataprovider, interface, c#] keywords: [schedulecontrol, dataprovider, ischeduleappointment, getenumerator, find, newscheduleappointment, getscheduleforday, getschedule, commitchanges, isdirty, droplist] -->
```