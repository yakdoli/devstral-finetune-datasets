```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_058.jpeg
document_name: schedule
page_number: 058
page_id: schedule#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:43Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- Provides an overview of scheduling functionalities in Windows Forms.
- Lists various properties for customizing the appearance and behavior of components such as borders, captions, and item formats.
- Focuses on properties related to formatting and styling in `Syncfusion.Schedule`.

## Content

### Border
| Property                    | Description                                      |
|-----------------------------|--------------------------------------------------|
| ClickItemBorderColor        | Gets or sets the border color of a clicked item. |
| DragColor                   | Gets or sets the color of the item that is dragged. |
| SolidBordercolor            | Gets or sets the color of the solid lines in the  calendar. |

### Caption
| Property                    | Description                                      |
|-----------------------------|--------------------------------------------------|
| CaptionBackColor            | Gets or sets the color of the caption area above the calendar. |
| ShowCaption                 | Specifies whether the caption panel above the calendar is visible. |
| ShowCaptionButtons          | Specifies whether the navigation buttons are shown on the caption panel. |

### DisplayItemFormat
| Property                    | Description                                      |
|-----------------------------|--------------------------------------------------|
| AllDayItemFormat            | Gets or sets the display format of an all-day item. |
| DateFormat                  | Gets or sets the format string used when formatting any token from DisplayItemFormatStrings that represents a date only value. |
| DateTimeFormat              | Gets or sets the format string used when formatting any token from DisplayItemFormatStrings that represents the combined date and time values. |
| DayItemFormat               | Gets or sets the display format of a schedule item displayed in a day or workweek view. |
| FullWeekHeaderFormat        | Specifies the display format of the header of a day in a week view. |
| LongHeaderFormat            | Specifies the display format of the header in a day view. |
| SpanItemFormatLeftText      | Specifies the display format of text displayed on the interior left side of a multiday span. |

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Schedule  
- **Class**: ScheduleControl  
- **Properties**:
  - **ClickItemBorderColor**: `Color`
    - Gets or sets the border color of a clicked item.
  - **DragColor**: `Color`
    - Gets or sets the color of the item that is dragged.
  - **SolidBordercolor**: `Color`
    - Gets or sets the color of the solid lines in the calendar.
  - **CaptionBackColor**: `Color`
    - Gets or sets the color of the caption area above the calendar.
  - **ShowCaption**: `Boolean`
    - Specifies whether the caption panel above the calendar is visible.
  - **ShowCaptionButtons**: `Boolean`
    - Specifies whether the navigation buttons are shown on the caption panel.
  - **AllDayItemFormat**: `string`
    - Gets or sets the display format of an all-day item.
  - **DateFormat**: `string`
    - Gets or sets the format string used when formatting any token from DisplayItemFormatStrings that represents a date only value.
  - **DateTimeFormat**: `string`
    - Gets or sets the format string used when formatting any token from DisplayItemFormatStrings that represents the combined date and time values.
  - **DayItemFormat**: `string`
    - Gets or sets the display format of a schedule item displayed in a day or workweek view.
  - **FullWeekHeaderFormat**: `string`
    - Specifies the display format of the header of a day in a week view.
  - **LongHeaderFormat**: `string`
    - Specifies the display format of the header in a day view.
  - **SpanItemFormatLeftText**: `string`
    - Specifies the display format of text displayed on the interior left side of a multiday span.

## Code Examples (multi-language supported)
- Here’s a basic example of how to use some of these properties in C#:

```csharp
// Example of setting the caption background color
ScheduleControl schedule = new ScheduleControl();
schedule.CaptionBackColor = Color.LightGray;

// Example of showing/hiding the caption panel
schedule.ShowCaption = true;

// Example of setting the display format for date
schedule.DateFormat = "dddd, MMMM d, yyyy";
```

<!-- tags: [Windows Forms, ScheduleControl, Border, Caption, DisplayItemFormat, Syncfusion.Windows.Forms.Schedule, Customization, Formatting, Appearance, NavigationButtons] keywords: [ClickItemBorderColor, DragColor, SolidBordercolor, CaptionBackColor, ShowCaption, ShowCaptionButtons, AllDayItemFormat, DateFormat, DateTimeFormat, DayItemFormat, FullWeekHeaderFormat, LongHeaderFormat, SpanItemFormatLeftText] -->
```