```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: schedule
page_number: 042
page_id: schedule#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:10:15Z
fidelity: lossless
-->

## Overview

- This section describes the properties related to an item in the Schedule Control.
- It explains details about the Owner, Start and End times, Subject, Content, and other properties of an appointment item.
- It also outlines the `ScheduleAppointmentList` class, which manages a collection of `IScheduleAppointments` as a wrapper for an `ArrayList`.

## Content

### Properties of an Item in the Schedule Control

- **Owner**: Gets or sets an integer that can be used to identify the owner (if any) of this item.
- **StartTime**: Gets or sets the start time for this item.
- **EndTime**: Gets or sets the end time for this item.
- **Subject**: Gets or sets a text string identifying the topic of this item.
- **Content**: Gets or sets a text string holding the details or comments for this appointment item.
- **AllDay**: Gets or sets whether this appointment is an all-day appointment.
- **LabelValue**: Gets or sets an integer categorizer value for this item.
- **MarkerValue**: Gets or sets an integer categorizer value for this item.
- **Reminder**: Gets or sets whether you want a reminder event raised when the `StartTime` of this item gets close.
- **ReminderValue**: Gets or sets the type of reminder event raised when the `StartTime` of this item gets close.
- **LocationValue**: Gets or sets a string associated with this item.
- **Version**: Gets in integer format the version number (used to support data format versioning).
- **Tag**: Gets or sets an arbitrary object associated with this item.
- **Dirty**: Gets or sets whether this item has been modified.
- **IgnoreChanges**: Gets or sets whether changes to this item affect the `Dirty` property.

### ScheduleAppointmentList Class

#### Overview

The `ScheduleAppointmentList` is a collection of `IScheduleAppointments` that serves as the data for the Schedule Control. This class acts as a wrapper class for an `ArrayList` and implements the `IComparer` interface to order this list by the item's `StartTime`. If two items start at the same time, the `EndTime` is used to determine the order. Longer appointments rank higher.

#### Details of the ScheduleAppointmentList

- The `ScheduleAppointmentList` class uses an `ArrayList` internally to manage the collection of appointments.
- It implements the `IComparer` interface to sort the appointments based on their start times.
- For appointments starting at the same time, the `EndTime` is used to compare and order them.
- Longer appointments (those with a greater time span) are given priority in the order.
- Below are the properties and methods exposed in `ScheduleAppointmentList`.

## API Reference (if applicable)

None specified in the current context.

## Code Examples (multi-language supported)

No code examples are provided in the current context.

## Page-level Navigation/TOC (if applicable)

None specified in the current context.

## Cross References

None specified in the current context.

## RAG Annotations

<!-- tags: [syncfusion, winforms, schedule, api, version:11.4.0.26] keywords: [schedule control, owner, start time, end time, subject, content, appointment, reminder, location, version, tag, dirty, ignorechanges, arrays, list, comparator, sorter, comparer, ntsTime, endTime, longer appointments, priority] -->
```