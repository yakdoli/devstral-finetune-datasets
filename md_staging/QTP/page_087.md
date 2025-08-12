```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_087.jpeg
document_name: QTP
page_number: 087
page_id: QTP#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:57Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview

- Demonstrates how to reschedule appointments in schedule control using the `ItemDrag` and `TimeDrag` methods.
- Explains the parameters and usage of the `ItemDrag` and `TimeDrag` methods in QTP testing.
- Provides code examples for applying `ItemDrag` and `TimeDrag` in QTP.

## Content

### Applying ItemDrag in QTP

The following code example illustrates how to reschedule the appointment in schedule control.

```csharp
[For Schedule Control]
SwfWindow("GridSchedulerDemo").SwfObject("Scheduler").
ItemDrag("Appointment1", "10/02/2012", "14/02/2013", "10/02/2013", "14/02/2014")
```

### 7.5.2 How to reschedule the timeline of an appointment

#### Supported method to reschedule the timeline of an appointment in the schedule control

The `TimeDrag` method is used to reschedule the timeline of the appointment in the schedule control. The appointments are rescheduled to another time based on the new start time and new end time.

#### Use Case Scenarios

This feature enables you to reschedule the timeline of appointments in the schedule control in QTP testing.

### Methods Table

| Method   | Description                                                                 | Parameters                                                                                      | Return Type |
|----------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------|
| TimeDrag | Reschedule the timeline to another appointment in the schedule control. | public void TimeDrag(string apptSubject, string oldStartTime, string oldEndTime, string newStartTime, string newEndTime) | void        |

### Applying TimeDrag in QTP

The following code example illustrates how to reschedule the timeline of the appointment in the schedule control.

---

<!-- tags: [syncfusion, qtp, itemdrag, timedrag, schedule control, appointments, timeline, rescheduling, qtp testing] -->
```