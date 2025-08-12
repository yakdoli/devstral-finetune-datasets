```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: schedule
page_number: 060
page_id: schedule#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:12:10Z
fidelity: lossless
-->

## Essential Schedule for Windows Forms

### Navigation Calendar Properties

| Property                          | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| NavigationCalendarArrowColor      | Specifies the color of arrows in the navigation calendar.                |
| NavigationCalendarBackColor       | Specifies the back color of the navigation calendar.                     |
| NavigationCalendarDisabledTextColor | Specifies the color of disabled text in the navigation calendar.        |
| NavigationCalendarHeaderColor     | Gets or sets the color of the header in the navigation calendar.          |
| NavigationCalendarSelectionColor  | Gets or sets the selection color in the navigation calendar.              |
| NavigationCalendarStartDayOfWeek  | Specifies the DayOfWeek that is shown in the leftmost column of the navigation calendar. |
| NavigationCalendarTextColor       | Specifies the text color of the navigation calendar.                     |
| NavigationCalendarTodayColor      | Specifies the color of today's text in the navigation calendar.           |
| NavigationCalendarWeekNumberColor | Specifies the color of week numbers in the navigation calendar.          |

### Prime Time

| Property          | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| NonPrimeTimeCellColor | Gets or sets the color of non-prime time cells in the calendar. |
| PrimeTimeCellColor    | Gets or sets the color of prime time cells in the calendar.    |
| PrimeTimeEnd          | Specifies the time when the prime time color stops being used in the display. |
| PrimeTimeStart        | Specifies the time when the prime time color starts being used in the display. |

### Time Column

| Property         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Hours24          | Determines whether the time column is displayed using a 24-hour format.    |
| MarkColumnColor   | Gets or sets the color of the thick solid line next to                    |

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Schedule
- **Class**: ScheduleControl
- **Members**:
  - Properties:
    - NavigationCalendarArrowColor
    - NavigationCalendarBackColor
    - NavigationCalendarDisabledTextColor
    - NavigationCalendarHeaderColor
    - NavigationCalendarSelectionColor
    - NavigationCalendarStartDayOfWeek
    - NavigationCalendarTextColor
    - NavigationCalendarTodayColor
    - NavigationCalendarWeekNumberColor
    - NonPrimeTimeCellColor
    - PrimeTimeCellColor
    - PrimeTimeEnd
    - PrimeTimeStart
    - Hours24
    - MarkColumnColor

## Code Examples

```csharp
// Example of setting properties for the navigation calendar
scheduleControl1.NavigationCalendarArrowColor = Color.Blue;
scheduleControl1.NavigationCalendarBackColor = Color.LightGray;

// Example of setting properties for prime time
scheduleControl1.PrimeTimeCellColor = Color.Yellow;
scheduleControl1.PrimeTimeStart = new DateTime(1900, 1, 1, 9, 0, 0); // 9:00 AM
scheduleControl1.PrimeTimeEnd = new DateTime(1900, 1, 1, 17, 0, 0);  // 5:00 PM
```

## Page-level Navigation/TOC
- Navigation Calendar Properties
- Prime Time
- Time Column

<!-- tags: [Syncfusion Winforms, Schedule, Navigation Calendar, Prime Time, Time Column] keywords: [NavigationCalendarArrowColor, PrimeTimeCellColor, Hours24, MarkColumnColor] -->
```