```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: schedule
page_number: 050
page_id: schedule#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:56Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- Interfaces for managing appointments in a schedule control.
- Defines properties like `UniqueID`, `Owner`, `StartTime`, `EndTime`, etc., for scheduling items.
- Supports categorization, reminders, and modification tracking.

## Content

### IScheduleAppointment Interface Definition

The `IScheduleAppointment` interface defines a contract for scheduling items with various properties and behaviors. Here is the complete interface definition:

```csharp
public interface IScheduleAppointment : IComparable, ICloneable
{
    /// <summary>
    /// A unique identifier for this schedule item.
    /// </summary>
    int UniqueID { get; set; }

    /// <summary>
    /// Identifies the owner of this schedule item.
    /// </summary>
    int Owner { get; set; }

    /// <summary>
    /// The start time of this item.
    /// </summary>
    DateTime StartTime { get; set; }

    /// <summary>
    /// The end time for this item.
    /// </summary>
    DateTime EndTime { get; set; }

    /// <summary>
    /// The subject or topic title for this schedule item.
    /// </summary>
    string Subject { get; set; }

    /// <summary>
    /// The text displayed as the main content of this schedule item.
    /// </summary>
    string Content { get; set; }

    /// <summary>
    /// Whether or not this item is to appear as an all day item.
    /// </summary>
    bool AllDay { get; set; }

    /// <summary>
    /// A categorizer value for this item.
    /// </summary>
    int LabelValue { get; set; }

    /// <summary>
    /// A categorizer value for this item.
    /// </summary>
    int MarkerValue { get; set; }

    /// <summary>
    /// Whether or not some reminder action should be taken as this item becomes current.
    /// </summary>
    bool Reminder { get; set; }

    /// <summary>
    /// Indicates when the reminder action should be taken.
    /// </summary>
    int ReminderValue { get; set; }

    /// <summary>
    /// Some item dependent string-like the location of a meeting.
    /// </summary>
    string LocationValue { get; set; }

    /// <summary>
    /// Whether or not this item has been modified.
    /// </summary>
    bool Dirty { get; set; }

    /// <summary>
    /// Whether or not changes to this item should be ignored.
    /// </summary>
    bool IgnoreChanges { get; set; }
}
```

### Key Properties and Behavior Overview
- **UniqueID**: A unique identifier for each schedule item.
- **Owner**: Identifies the owner or user associated with the schedule item.
- **StartTime` and `EndTime**: Define the time range for the schedule item.
- **Subject** and **Content**: The title and main body content of the schedule item.
- **AllDay**: Indicates whether the item is an all-day event.
- **LabelValue** and **MarkerValue**: Used for categorizing or marking the schedule item.
- **Reminder** and **ReminderValue**: Specifies if and when a reminder should be triggered.
- **LocationValue**: Provides additional information like the location of the event.
- **Dirty** and **IgnoreChanges**: Track modifications and control whether changes should be ignored.

### Methods and Interfaces
- Implements `IComparable` to allow sorting of schedule items.
- Implements `ICloneable` to facilitate creation of duplicates.

## API Reference
### Namespace
- `Syncfusion.Windows.Forms.Schedule`

### Properties
- `UniqueID`: int
- `Owner`: int
- `StartTime`: DateTime
- `EndTime`: DateTime
- `Subject`: string
- `Content`: string
- `AllDay`: bool
- `LabelValue`: int
- `MarkerValue`: int
- `Reminder`: bool
- `ReminderValue`: int
- `LocationValue`: string
- `Dirty`: bool
- `IgnoreChanges`: bool

### Methods from Interfaces
- `CompareTo`: from `IComparable`
- `Clone`: from `ICloneable`

## Code Examples
Here is an example of how the `IScheduleAppointment` interface can be implemented:

```csharp
public class ScheduleAppointment : IScheduleAppointment
{
    public int UniqueID { get; set; }
    public int Owner { get; set; }
    public DateTime StartTime { get; set; }
    public DateTime EndTime { get; set; }
    public string Subject { get; set; }
    public string Content { get; set; }
    public bool AllDay { get; set; }
    public int LabelValue { get; set; }
    public int MarkerValue { get; set; }
    public bool Reminder { get; set; }
    public int ReminderValue { get; set; }
    public string LocationValue { get; set; }
    public bool Dirty { get; set; }
    public bool IgnoreChanges { get; set; }

    public int CompareTo(object obj)
    {
        if (obj == null) return 1;
        ScheduleAppointment other = obj as ScheduleAppointment;
        if (other == null) throw new ArgumentException("Object is not a ScheduleAppointment");
        return this.StartTime.CompareTo(other.StartTime);
    }

    public object Clone()
    {
        return this.MemberwiseClone();
    }
}
```

## Page-level Navigation/TOC
- Overview
- IScheduleAppointment Interface Definition
- Key Properties and Behavior Overview
- API Reference
- Code Examples

## Cross References
- See also:
  - `IComparable`
  - `ICloneable`
  - Schedule control documentation

<!-- tags: [syncfusion, winforms, schedule, interface, IScheduleAppointment, Windows Forms] keywords: [uniqueID, owner, start time, end time, subject, content, all day, label value, marker value, reminder, reminder value, location value, dirty, ignore changes] -->
```
