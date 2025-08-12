```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: schedule
page_number: 061
page_id: schedule#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:25Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview

- Describes the properties in the Essential Schedule Control for Windows Forms.
- Focuses on time column settings and visual styles.
- Includes miscellaneous scheduling properties and control settings.

## Content

### Time Column Settings

| Property                 | Description                                                                        |
|--------------------------|--------------------------------------------------------------------------------------|
| ShowTime                 | Indicates whether the time column should appear.                                   |
| TimeBackColor            | Specifies the back color of the time column.                                      |
| TimeBigFontSize          | Determines the size of larger font used in the time column.                       |
| TimeLittleFontSize       | Determines the size of smaller font used in the time column.                       |
| TimeTextColor            | Specifies the color of text in the time column.                                   |

### Visual Style

| Property               | Description                                                            |
|------------------------|--------------------------------------------------------------------------|
| VisualStyle            | Specifies the visual style for the ScheduleControl.                       |

### Miscellaneous

| Property                        | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| DayMonthCutOff                  | Gets or sets the maximum number of days that can appear side-by-side in a day style calendar. |
| DivisionsPerHour                | Gets or sets the number of time divisions that appear in a day, custom or workweek view.     |
| MonthCalendarStartDayOfWeek     | Gets or sets the DayOfWeek that is shown in the left-most column of the month calendar.        |
| MonthShowFullWeek                | Specifies whether the month view shows 7 columns or 6 columns with Saturday or Sunday stacked. |
| ScheduleAppointmentTipFormat     | Defines the text that is displayed for schedule item tips.                                      |
| ScheduleAppointmentTipsEnabled   | Determines whether to show item tips.                                                       |
| SplitterBackColor               | Specifies the back color of the two splitters in the ScheduleControl.                         |
| TextColor                       | Specifies the color of basic text shown in the calendar.                                      |
| ThemesEnabled                   | Specifies whether the themes are enabled.                                                    |

## API Reference (if applicable)

- **Namespace**: Syncfusion.Windows.Forms.Schedule
- **Class**: ScheduleControl
- **Properties**:
  - `ShowTime`: Boolean
  - `TimeBackColor`: Color
  - `TimeBigFontSize`: FontSize
  - `TimeLittleFontSize`: FontSize
  - `TimeTextColor`: Color
  - `VisualStyle`: VisualStyleType
  - `DayMonthCutOff`: Int32
  - `DivisionsPerHour`: Int32
  - `MonthCalendarStartDayOfWeek`: DayOfWeek
  - `MonthShowFullWeek`: Boolean
  - `ScheduleAppointmentTipFormat`: String
  - `ScheduleAppointmentTipsEnabled`: Boolean
  - `SplitterBackColor`: Color
  - `TextColor`: Color
  - `ThemesEnabled`: Boolean

## Code Examples (multi-language supported)

```csharp
ScheduleControl schedule = new ScheduleControl();
schedule.ShowTime = true;
schedule.TimeBackColor = Color.Gray;
schedule.TimeBigFontSize = 14;
schedule.TimeLittleFontSize = 10;
schedule.TimeTextColor = Color.Black;
schedule.VisualStyle = VisualStyleType.Default;
schedule.DayMonthCutOff = 7;
schedule.DivisionsPerHour = 2;
schedule.MonthCalendarStartDayOfWeek = DayOfWeek.Monday;
schedule.MonthShowFullWeek = true;
schedule.ScheduleAppointmentTipFormat = "Appointment: {0}";
schedule.ScheduleAppointmentTipsEnabled = true;
schedule.SplitterBackColor = Color.LightGray;
schedule.TextColor = Color.Black;
schedule.ThemesEnabled = true;
```

## Cross References

- **See also:**
  - [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms/schedule)
  - [ScheduleControl Class](https://help.syncfusion.com/windowsforms/schedule/)

## RAG Annotations

<!-- tags: [Syncfusion Winforms, ScheduleControl, time column settings, visual style, miscellaneous scheduling properties, control settings, properties, font size, text color, themes, appointment tips] keywords: [ShowTime, TimeBackColor, TimeBigFontSize, TimeLittleFontSize, TimeTextColor, VisualStyle, DayMonthCutOff, DivisionsPerHour, MonthCalendarStartDayOfWeek, MonthShowFullWeek, ScheduleAppointmentTipFormat, ScheduleAppointmentTipsEnabled, SplitterBackColor, TextColor, ThemesEnabled] -->
```