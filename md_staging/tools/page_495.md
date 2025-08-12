```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_495.jpeg
document_name: tools
page_number: 495
page_id: tools#page_495
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:56Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to create and implement a custom calendar for a dateTime picker in Windows Forms.
- Explains the use of the `IDateTimePickerAdvCalendar` interface for customizing calendar-related functionalities.
- Highlights the implementation of properties like `Active`, `CalendarFont`, `CalendarForeColor`, `CalendarMonthBackground`, and `Value`.

## Content

```csharp
[C#]

//Creating Calendar which implements the IDateTimePickerAdvCalendar
private MyCustomCalendar MonthCalendar;

//Initializing the Calendar
this.MonthCalendar = new MyCustomCalendar();

//Defining the Calendar Class which implements IDateTimePickerAdvCalendar
public class MyCustomCalendar : MonthCalendar, IDateTimePickerAdvCalendar
{
    private bool active;

    public bool Active
    {
        get { return active; }
        set { active = value; }
    }

    public System.Drawing.Font CalendarFont
    {
        get { return Font; }
        set { Font = value; }
    }

    public Color CalendarForeColor
    {
        get { return ForeColor; }
        set { ForeColor = value; }
    }

    public Color CalendarMonthBackground
    {
        get { return BackColor; }
        set { BackColor = value; }
    }

    public DateTime Value
    {
        get { return SelectionStart; }
        set { SelectionStart = SelectionEnd = value; }
    }
}
```

### Explanation
- **MyCustomCalendar**: A custom class implementing both `MonthCalendar` and `IDateTimePickerAdvCalendar`. It includes properties to customize and control the visual and functional aspects of the calendar.
- **Active Property**: Used to determine whether the calendar is active.
- **CalendarFont**: Sets the font for the calendar's text.
- **CalendarForeColor**: Sets the foreground color for the calendar's text.
- **CalendarMonthBackground**: Sets the background color for the calendar's month view.
- **Value**: Represents the currently selected date.

## API Reference

### Implemented Interface: `IDateTimePickerAdvCalendar`
The `IDateTimePickerAdvCalendar` interface allows for the customization of a calendar for a dateTime picker. The `MyCustomCalendar` class implements this interface by providing specific property getters and setters.

#### Properties
- **Active**: 
  - Type: `bool`
  - Description: Indicates whether the calendar is active.
  - Get: Returns the current value of `active`.
  - Set: Updates the value of `active`.

- **CalendarFont**: 
  - Type: `System.Drawing.Font`
  - Description: Sets the font for the calendar's text.
  - Get: Returns the current font setting.
  - Set: Updates the font setting.

- **CalendarForeColor**: 
  - Type: `Color`
  - Description: Sets the foreground color for the calendar's text.
  - Get: Returns the current foreground color.
  - Set: Updates the foreground color.

- **CalendarMonthBackground**: 
  - Type: `Color`
  - Description: Sets the background color for the calendar's month view.
  - Get: Returns the current background color.
  - Set: Updates the background color.

- **Value**: 
  - Type: `DateTime`
  - Description: Represents the currently selected date in the calendar.
  - Get: Returns the selected start date.
  - Set: Updates both `SelectionStart` and `SelectionEnd` to the specified date.

## Code Examples

The example above demonstrates how to create a custom calendar class that implements the `IDateTimePickerAdvCalendar` interface. This allows developers to customize the appearance and behavior of calendars used in dateTime pickers.

```csharp
// Usage example
MyCustomCalendar customCalendar = new MyCustomCalendar();
customCalendar.Active = true;
customCalendar.CalendarFont = new System.Drawing.Font("Arial", 12);
customCalendar.CalendarForeColor = Color.Blue;
customCalendar.CalendarMonthBackground = Color.LightGray;
customCalendar.Value = DateTime.Now;
```

## Cross References

See also:
- `MonthCalendar` class for base functionality.
- `IDateTimePickerAdvCalendar` interface for more details on the required methods and properties.

<!-- tags: [Syncfusion, WinForms, DateTimePicker, Calendar] keywords: [custom calendar, IDateTimePickerAdvCalendar, MonthCalendar, Active, CalendarFont, CalendarForeColor, CalendarMonthBackground, Value] -->
```