```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_497.jpeg
document_name: tools
page_number: 497
page_id: tools#page_497
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:05Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
set { throw new Exception("The method or operation is not implemented."); }
    }
}
```

## Using Advanced Calendars in DateTimePicker

### Implementing a Custom Calendar in VB.NET

By implementing the `IDateTimePickerAdvCalendar` interface, you can create custom calendars for the DateTimePicker control. This section provides an example of creating and initializing a custom calendar.

#### Code Example

```vb
' Creating Calendar which implements the IDateTimePickerAdvCalendar
Private MonthCalendar As MyCustomCalendar

' Initializing the Calendar
Me.MonthCalendar = New MyCustomCalendar()
```

#### Definition of the Custom Calendar Class

```vb
Public Class MyCustomCalendar
    Inherits MonthCalendar
    Implements IDateTimePickerAdvCalendar

    Private m_active As Boolean

    Public Property Active() As Boolean
        Get
            Return m_active
        End Get
        Set(ByVal value As Boolean)
            m_active = value
        End Set
    End Property

    Public Property CalendarFont() As System.Drawing.Font
        Get
            Return Font
        End Get
        Set(ByVal value As System.Drawing.Font)
            Font = value
        End Set
    End Property

    Public Property CalendarForeColor() As Color
        Get
            Return ForeColor
        End Get
        Set(ByVal value As Color)
            ForeColor = value
        End Set
    End Property
End Class
```

### Explanation

- **Creating the Custom Calendar**: The `MyCustomCalendar` class is defined to inherit from `MonthCalendar` and implement the `IDateTimePickerAdvCalendar` interface.
- **Properties**: The custom calendar includes properties such as `Active`, `CalendarFont`, and `CalendarForeColor` to customize the appearance and functionality of the calendar.

By following these steps, you can effectively use custom calendars with the DateTimePicker control in your Windows Forms applications.

## API Reference

### Interfaces

- **IDateTimePickerAdvCalendar**
  - **Methods**
    - `Active`: Gets or sets whether the calendar is active.
    - `CalendarFont`: Gets or sets the font of the calendar.
    - `CalendarForeColor`: Gets or sets the foreground color of the calendar.

## Code Examples

### VB.NET Example

```vb
Public Class MyCustomCalendar
    Inherits MonthCalendar
    Implements IDateTimePickerAdvCalendar

    Private m_active As Boolean

    Public Property Active() As Boolean
        Get
            Return m_active
        End Get
        Set(ByVal value As Boolean)
            m_active = value
        End Set
    End Property

    Public Property CalendarFont() As System.Drawing.Font
        Get
            Return Font
        End Get
        Set(ByVal value As System.Drawing.Font)
            Font = value
        End Set
    End Property

    Public Property CalendarForeColor() As Color
        Get
            Return ForeColor
        End Get
        Set(ByVal value As Color)
            ForeColor = value
        End Set
    End Property
End Class
```

### Note

- Ensure that the `MyCustomCalendar` class properly implements all methods and properties defined in the `IDateTimePickerAdvCalendar` interface.
- The `Active` property can be used to enable or disable specific functionality within the calendar.

## See also

- [DateTimePickerAdv (Syncfusion WinForms)](https://syncfusion.com/products/windows-forms/scheduler)
- [Advanced Calendar Support](https://help.syncfusion.com/windowsforms/scheduler/calendar)

<!-- tags: [syncfusion, winforms, datetimepicker, calendar, advanced calendars] keywords: [custom calendar, iDateTimePickerAdvCalendar, monthcalendar, active property, calendarfont, calendarforecolor] -->
```