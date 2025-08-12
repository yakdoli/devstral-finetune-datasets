```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_494.jpeg
document_name: tools
page_number: 494
page_id: tools#page_494
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the handling of events and creating a custom popup window for DateTimePickerAdv.
- Guides user through adding a Windows MonthCalendar control as the Popup for DateTimePickerAdv.
- Demonstrates the use of IDateTimePickerAdvCalendar interface implementation.

## Content

### Event Handling

The following table describes the handling of specific events:

| Event       | Description                                                                                                                                                          |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [unclear]   | is handled when the user selects a date on the control implementing the interface or the control wants the popup to close and set the picker's date to the Value member. |
| DateChange  | Event is similar to the `DateTimePickerAdv.DateChangedEventHandler`. It is handled when the user has changed the date of the control implementing the interface and doesn't want the popup to close, just update the picker's date to the Value member. |

### Creating a Custom Popup Window for DateTimePickerAdv

Follow the below steps to add a Windows MonthCalendar control as the Popup for the DateTimePickerAdv, using `PopupControlContainer`.

1. Drag a DateTimePickerAdv, `PopupControlContainer`, and a button onto the form designer from the toolbox.

   ![Figure 288: Control added to the Form](attachment)

   **Figure 288: Control added to the Form**

2. Create a control that implements the `IDateTimePickerAdvCalendar` interface using the below code.

## API Reference (if applicable)
- **Interface:** IDateTimePickerAdvCalendar
  - Methods/Events: Not specified in the current content.

## Code Examples (multi-language supported)
No explicit code examples provided in the current content.

## RAG Annotations
<!-- tags: [datetimepickeradv, user interface, event handling, custom popup, window forms, control implementation, WinForms] keywords: [datetimepickeradv, datechange, popupcontrolcontainer, monthcalendar, idatetpickeradvcalendar, eventhandler] -->
```