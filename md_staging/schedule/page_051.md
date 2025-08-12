```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: schedule
page_number: 051
page_id: schedule#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:49Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## API Reference

### WinForms-specific properties

The following properties are associated with the data schema and tags for scheduling items:

- **Tag**: An arbitrary object associated with this item.
  ```csharp
  object Tag { get; set; }
  ```

- **Version**: A version associated with the data schema for this item.
  ```csharp
  int Version { get; }
  ```

### IScheduleAppointmentList Interface

#### Overview
The `IScheduleAppointmentList` interface represents a collection of `IScheduleAppointments` that serve as the data for the `ScheduleControl`.

#### Declaration
```csharp
public interface IScheduleAppointmentList
{
    /// An IScheduleAppointment referenced through an indexer.
    IScheduleAppointment this[int i] { get; set; }

    /// The number of IScheduleAppointments in this list.
    int Count { get; }

    /// Arranges the IScheduleAppointments in this list according to IScheduleAppointment.StartTime.
    void SortStartTime();

    /// Adds an IScheduleAppointment at the end of this collection.
    void Add(IScheduleAppointment item);

    /// Inserts the given IScheduleAppointment at a particular position in this collection.
    void Insert(int index, IScheduleAppointment item);

    /// Removes a given IScheduleAppointment from this collection.
    void Remove(IScheduleAppointment item);

    /// Removes an IScheduleAppointment at the given index from this collection.
    void RemoveAt(int index);

    /// Locates the index of a particular IScheduleAppointment in this collection.
    int IndexOf(IScheduleAppointment item);
}
```

### Summary
- **IScheduleAppointmentList** is an interface that provides functionality to manage a collection of scheduling appointments.
- It supports adding, inserting, removing, and locating scheduling appointments within the collection.
- The interface includes methods to sort appointments based on their start time.

<!-- tags: [schedule, windows forms, data schema, version control, tagging, interface, collection management, start time sorting] keywords: [schedule list, schedule appointments, collection interface, tag, version, indexing, adding, inserting, removing] -->
```