```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_436.jpeg
document_name: tools
page_number: 436
page_id: tools#page_436
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:47Z
fidelity: lossless
-->

## Windows Forms Controls Overview

### Common Controls Properties

| Property   | Description |
|------------|-------------|
| MinValue | Specifies the minimum value selectable by the calendar. |
| MaxValue | Specifies the maximum value selectable by the calendar. |

### Setting Minimum and Maximum Dates

#### C#

```csharp
this.monthCalendarAdv1.Value = new System.DateTime(2008, 2, 19);
this.monthCalendarAdv1.MinValue = new System.DateTime(2000, 2, 21, 0, 0, 0);
this.monthCalendarAdv1.MaxValue = new System.DateTime(2008, 2, 21, 0, 0, 0);
```

#### VB.NET

```vb
Me.monthCalendarAdv1.Value = New Date(2008, 2, 19)
Me.monthCalendarAdv1.MinValue = New System.DateTime(2000, 2, 21, 0, 0)
Me.monthCalendarAdv1.MaxValue = New System.DateTime(2008, 2, 21, 0, 0, 0)
```

### Selecting Dates

When we drag and drop a `MonthCalendarAdv` control, the current system date, i.e., today's date, will be selected by default. To change the selected date, the `DateTime Collection Editor` is used, which is invoked using the `SelectedDates` property.

## API Reference

### MonthCalendarAdv Properties

- **MinValue**: Specifies the minimum selectable date.
- **MaxValue**: Specifies the maximum selectable date.
- **SelectedDates**: Collection of selected dates.

---

```html
<!-- tags: [Syncfusion, WinForms, MonthCalendarAdv, DateTime, minValue, maxValue, selectedDates] -->
```
```