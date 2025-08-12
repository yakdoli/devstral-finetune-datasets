```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: schedule
page_number: 070
page_id: schedule#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:29Z
fidelity: lossless
-->

## Essential Schedule for Windows Forms

### How to prevent the switching of schedule view type

The schedule type can be changed at any time by using the `ScheduleViewType` property. Switching of view style can be prevented by making the view type as constant in the Schedule control by disabling the `SwitchViewStyle` property. By default, this property value is true.

#### Properties

| Property         | Description                                                                 | Data Type |
|------------------|-----------------------------------------------------------------------------|-----------|
| `SwitchViewStyle` | Gets/sets whether the view style should be changed in the Schedule control. The default value is `true`. | `bool`    |

The following codes are used to disable the `SwitchViewStyle` property.

#### C#
```csharp
this.ScheduleControl1.ScheduleType = ScheduleViewType.Month;
this.ScheduleControl1.SwitchViewStyle = false;
```

#### VB
```vb
Me.ScheduleControl1.ScheduleType = ScheduleViewType.Month
Me.ScheduleControl1.SwitchViewStyle = False
```

### How to show the start and end time with scheduled appointments

To show or hide the time of an appointment in the schedule window, the `ShowTime` property can be set to `true` or `false`. The time shown in the appointment can also be formatted by setting the time format through the `WeekMonthItemFormat` property.

#### Properties

**Table 1: Properties Table**

| Property   | Description                                  | Type       | Data Type | Reference links |
|------------|----------------------------------------------|------------|-----------|----------------|
| `ShowTime` | Indicates whether the time column should appear or not | ShowTime  | Boolean     |                |

<!-- tags: [Syncfusion, Windows Forms, Schedule, ScheduleViewType, SwitchViewStyle, ShowTime] keywords: [schedule, view type, time column, month view, appointment, formatting, week month] -->
```