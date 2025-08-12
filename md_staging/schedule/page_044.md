```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_044.jpeg
document_name: schedule
page_number: 044
page_id: schedule#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:17Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

The second role is to provide the DropList data. For this second role, the ScheduleDataProvider does provide concrete implementations for the virtual methods it exposes. So, in your derived class, you would have populated droplists without doing further work, though you can choose to customize these droplists through virtual overrides. Here is a list of the stub methods exposed by ScheduleDataProvider in its first role.

```csharp
[C#]

/// <summary>
/// Returns an IScheduleAppointmentList holding the schedule items for the given date.
/// </summary>
public virtual IScheduleAppointmentList GetScheduleForDay(DateTime day)

/// <summary>
/// Returns an IScheduleAppointmentList holding the schedule items between the given dates.
/// </summary>
public virtual IScheduleAppointmentList GetSchedule(DateTime startDate, DateTime endDate)

/// <summary>
/// Returns an IScheduleAppointmentList holding the schedule items for a particular owner on the given date.
/// </summary>
public virtual IScheduleAppointmentList GetScheduleForDay(DateTime day, int owner)

/// <summary>
/// Returns an IScheduleAppointmentList holding the schedule items for a particular owner between the given dates.
/// </summary>
public virtual IScheduleAppointmentList GetSchedule(DateTime startDate, DateTime endDate, int owner)

/// <summary>
/// Saves any modified ScheduleAppointments.
/// </summary>
public virtual void CommitChanges()

/// <summary>
/// Gets or sets whether CommitChanges is called when the ScheduleControl is disposed.
/// </summary>
public SaveOnCloseBehavior SaveOnCloseBehaviorAction

/// <summary>
/// Gets or sets whether data source is modified or not.
/// </summary>
public virtual bool IsDirty

/// <summary>
/// Returns a new ScheduleAppointment populated with default values.
/// </summary>
public virtual IScheduleAppointment NewScheduleAppointment()

/// <summary>
/// Adds a ScheduleAppointment to the list.
/// </summary>
public virtual void AddItem(IScheduleAppointment item)

/// <summary>
/// Removes a ScheduleAppointment from the list.
/// </summary>
public virtual void RemoveItem(IScheduleAppointment item)
```

<!-- tags: [schedule, windows forms, data provider, drop list, virtual methods, customizations] keywords: [schedule data provider, virtual overrides, droplists, role, interface implementations, schedulecontrol, data source] -->
```