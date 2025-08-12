```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_471.jpeg
document_name: tools
page_number: 471
page_id: tools#page_471
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:15:13Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

We can specify the visibility of the None button using the `NoneButtonVisible` property. Default value is `true`.

### Specifying NoneButtonVisibility

```csharp
this.dateTimePickerAdv1.NoneButtonVisible = false;
```

```vb
Me.dateTimePickerAdv1.NoneButtonVisible = False
```

**Note:** None button will not be visible when the `EnableNullDate` property is set to false. See [Null Value Settings](#null-value-settings) to know about the `EnableNullDate` property.

### 3.5.3.2.3.2 Customizing the Calendar

The `DateTimePickerAdv` control has properties that can improve the look and feel of the popup calendar. This section discusses various appearance settings available for the calendar.

#### Background Settings

The background of the Calendar can be customized using the following properties:

| DateTimePickerAdv Properties          | Description                               |
|----------------------------------------|-------------------------------------------|
| CalendarMonthBackground               | Sets the background color for the popup calendar. |
| CalendarTitleBackColor                | Sets the background of the calendar header. |

```csharp
this.dateTimePickerAdv1.CalendarMonthBackground = System.Drawing.Color.OldLace;
this.dateTimePickerAdv1.CalendarTitleBackColor = System.Drawing.Color.Wheat;
```

```vb
Me.dateTimePickerAdv1.CalendarMonthBackground = System.Drawing.Color.OldLace
Me.dateTimePickerAdv1.CalendarTitleBackColor =
```

---

## API Reference

### Properties
- `NoneButtonVisible`: Determines whether the None button is visible.
- `EnableNullDate`: When set to false, makes the None button invisible.
- `CalendarMonthBackground`: Sets the background color for the popup calendar.
- `CalendarTitleBackColor`: Sets the background of the calendar header.

### Sample Code

```csharp
// Setting NoneButtonVisibility
this.dateTimePickerAdv1.NoneButtonVisible = false;

// Customizing Calendar Background
this.dateTimePickerAdv1.CalendarMonthBackground = System.Drawing.Color.OldLace;
this.dateTimePickerAdv1.CalendarTitleBackColor = System.Drawing.Color.Wheat;
```

```vb
' Setting NoneButtonVisibility
Me.dateTimePickerAdv1.NoneButtonVisible = False

' Customizing Calendar Background
Me.dateTimePickerAdv1.CalendarMonthBackground = System.Drawing.Color.OldLace
Me.dateTimePickerAdv1.CalendarTitleBackColor =
```

<!-- tags: [DateTimePickerAdv, WinForms, NullValueSettings] keywords: [NoneButtonVisible, EnableNullDate, CalendarMonthBackground, CalendarTitleBackColor, Customization] -->
```