```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: schedule
page_number: 053
page_id: schedule#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:58Z
fidelity: lossless
-->

## Essential Schedule for Windows Forms

```csharp
/// Returns an instance of a new schedule item.
IScheduleAppointment NewScheduleAppointment();

/// Adds a schedule item to this list.
void AddItem(IScheduleAppointment item);

/// Removes a schedule item from this list.
void RemoveItem(IScheduleAppointment item);

/// Initializes the contents of the ILookUpObjectList lists.
void InitLists();

/// Returns a list holding the possible values for the <see cref="IScheduleAppointment.LocationValue"/> property.
ILookUpObjectList GetLocations();

/// Returns a list holding the possible values for the <see cref="IScheduleAppointment.MarkerValue"/> property.
ILookUpObjectList GetMarkers();

/// Returns a list holding the possible values for the <see cref="IScheduleAppointment.LabelValue"/> property.
ILookUpObjectList GetLabels();

/// Returns a list holding the possible values for the <see cref="IScheduleAppointment.ReminderValue"/> property.
/// </summary>
ILookUpObjectList GetReminders();

/// Returns a list holding the possible values for the <see cref="IScheduleAppointment.Owner"/> property.
/// </summary>
ILookUpObjectList GetOwners();
```

## 3.4.2.2 The DropLists

Two of the five data interfaces work directly with the `DropList` data. Here are the two interfaces.

### ILookUpObject Interface

`ILookUpObject` is part of the data support to provide the `DropList` data. This interface defines the object that may appear in a droplist.

## API Reference

- **Name**: ILookUpObject
- **Description**: Provides the object that may appear in a droplist.

### ILookUpObject Members

- **Methods**:
  - `ILookUpObjectList GetLocations()`
  - `ILookUpObjectList GetMarkers()`
  - `ILookUpObjectList GetLabels()`
  - `ILookUpObjectList GetReminders()`
  - `ILookUpObjectList GetOwners()`

### Sample Code

```csharp
// Example usage of ILookUpObject

ILookUpObjectList locations = GetLocations();
// Further processing of locations list
```

### See also
- **DropList Support**: Detailed documentation on how `DropList` is supported in the schedule control.
- **IScheduleAppointment**: Reference to the interface that represents a schedule item.

<!-- tags: [schedule, windows forms, droplists, ILookUpObject, ILookUpObjectList] keywords: [schedule, windows, forms, drop list, lookup object, look up object, list, ILookUpObject, ILookUpObjectList] -->
```