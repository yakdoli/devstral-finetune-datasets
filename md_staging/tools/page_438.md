```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_438.jpeg
document_name: tools
page_number: 438
page_id: tools#page_438
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:45Z
fidelity: lossless
-->

## Overview
- Features multi-selection options for dates in the MonthCalendarAdv control.
- Includes setting properties like `AllowMultipleSelection` and `MouseDragMultiSelect` programmatically.
- Demonstrates how to select a range of dates using both mouse dragging and programmatic methods.

## Content

### Date Selection Features
The table below outlines the multi-selection options for the MonthCalendarAdv control:

| Property Name          | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| AllowMultipleSelection | Indicates whether multiple date selections are allowed. i.e., by holding the Ctrl key and selecting the dates using mouse. |
| MouseDragMultiSelect   | Indicates whether selection of dates are allowed using mouse down and dragging at run time. |

#### Configuring Multi-Selection
Below are the code snippets to configure multi-selection:

[C#]

```csharp
this.monthCalendarAdv1.AllowMultipleSelection = true;
this.monthCalendarAdv1.MouseDragMultiselect = true;
```

[VB.NET]

```vb
this.monthCalendarAdv1.AllowMultipleSelection = True
Me.monthCalendarAdv1.MouseDragMultiselect = True
```

#### Figure: Selection of Dates by Mouse Dragging
![Selection of Dates by Mouse Dragging](https://image.png)
**Figure 237: Selection of Dates by Mouse Dragging**

### Select Date Range Programmatically
Using the `SelectedDates` property, range of dates can be selected in the MonthCalendarAdv control. The dates should be given in array format using the DateTime Array list.

[C#]

```csharp
DateTime[] dateTimes = new DateTime[] { new DateTime(2010, 11, 2), new DateTime(2010, 11, 3) };
DateTime[] dateTotal = new DateTime[] {  };
```

[VB.NET]

```vb
Dim dateTimes As DateTime() = New DateTime() {New DateTime(2010, 11, 2), New DateTime(2010, 11, 3)}
Dim dateTotal As DateTime() = {}
```

## API Reference

### Properties
- **AllowMultipleSelection**: Type: `Boolean`<br />
  Indicates whether multiple date selections are allowed. Default is `false`.

- **MouseDragMultiSelect**: Type: `Boolean`<br />
  Indicates whether selection of dates are allowed using mouse down and dragging at run time. Default is `false`.

- **SelectedDates**: Type: `DateTime[]`<br />
  Gets or sets the array of selected dates. Default is an empty array.

## Code Examples

[C#]

```csharp
// Selecting dates programmatically
DateTime[] selectedDates = new DateTime[] { new DateTime(2022, 6, 1), new DateTime(2022, 6, 5) };
this.monthCalendarAdv1.SelectedDates = selectedDates;
```

[VB.NET]

```vb
' Selecting dates programmatically
Dim selectedDates() As DateTime = {New DateTime(2022, 6, 1), New DateTime(2022, 6, 5)}
Me.monthCalendarAdv1.SelectedDates = selectedDates
```

<!-- tags: [Syncfusion Winforms, MonthCalendarAdv, Multiple Date Selection, Mouse Dragging, Date Range Selection, DateTime Array, API Reference, C#, VB.NET] keywords: [month calendar, date selection, multi-selection, mouse drag, programmatic selection, selected dates, datetime array] -->
```