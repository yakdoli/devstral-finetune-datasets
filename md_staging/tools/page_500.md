```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_500.jpeg
document_name: tools
page_number: 500
page_id: tools#page_500
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of `MonthCalendar` control with custom events.
- Explains the `FireNullEvent` method to trigger events.
- Provides examples in both C# and VB.NET to illustrate functionality.
- Guides through creating and using custom popups with `DateTimePickerAdv`.

## Content

### Code Examples

#### C#
```csharp
private void buttonAdv1_Click(object sender, EventArgs e)
{
    // Calling the below method to fire the Null Event of the Calendar control created
    MonthCalendar.FireNullEvent();
}
```

#### VB.NET
```vb
Private Sub buttonAdv1_Click(ByVal sender As Object, ByVal e As EventArgs)
    ' Calling the below method to fire the Null Event of the Calendar control created
    MonthCalendar.FireNullEvent()
End Sub
```

### Instructions for Demonstration

5. **Run the application and click the dropdown button of the DateTimePickerAdv control to display the custom popup.**

- **Figure 289: CustomPopup for the DateTimePickerAdv Control**
![CustomPopup for the DateTimePickerAdv Control](https://i.imgur.com/placeholder.png)

6. **When you click the button, the DateTimePickerAdv will display the `NullString` specified in the `NullString` property.**

## API Reference

- **Method: FireNullEvent**
  - **Description:** Triggers a custom null event for the `MonthCalendar` control.
  - **Parameters:** None
  - **Returns:** None
  - **Usage:** Useful for debugging or custom event handling.

<!-- tags: [winforms, monthcalendar, datetimepicker, firenull-event, custom-popup, event-handling] keywords: [datetimepickeradv, custompopup, nullevent, monthcalendar, flicker-free, syncfusion winforms] -->
```