```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: ProjIO
page_number: 059
page_id: ProjIO#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:24Z
fidelity: lossless
-->

## Creating a Standard Calendar

To create a standard calendar, you can use the `Calendar.StandardCalendar` method by passing the calendar name. Below is an example of how to create a standard calendar:

```vb
Dim calendar1 As Calendar = Calendar.StandardCalendar("Standard")
```

### Overview

- Creates a standard calendar using the `Calendar.StandardCalendar` method.
- The `Standard` calendar name is passed as a parameter to the method.

### Description

The `Calendar.StandardCalendar` method is used to create a calendar instance based on the specified calendar name. In this example, the "Standard" calendar is being created. This is useful in applications where you need to work with different calendar systems, such as the Gregorian calendar, Islamic calendar, or other custom calendar systems.

### Code Example

```vb
' Creating a standard calendar by passing the calendar name
Dim calendar1 As Calendar = Calendar.StandardCalendar("Standard")
```

### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Method**: `Calendar.StandardCalendar(name As String)`
  - **Parameters**:
    - `name` (String): The name of the calendar to create.
  - **Returns**: A `Calendar` object representing the specified calendar.

### Notes

- Ensure that the calendar system supports the specified calendar name to avoid errors.
- The "Standard" calendar typically refers to the Gregorian calendar.

### Cross References

- For more information on different calendar systems and their usage, refer to the [Syncfusion documentation on calendars](https://www.syncfusion.com/documentation/windows-forms/calendars).

<!-- tags: [syncfusion, winforms, calendar, standardcalendar, api, 11.4.0.26] keywords: [calendar, standard, calendar creation, standardcalendar method, winforms controls] -->
```