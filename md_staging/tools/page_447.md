```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_447.jpeg
document_name: tools
page_number: 447
page_id: tools#page_447
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains event handling in the MonthCalendarAdv control.
- Details the events that are triggered when the date is selected or changed.
- Lists commonly used events and their descriptions.

## Content

### 3.5.3.1.5 Event Handling

**MonthCalendarAdv** triggers events whenever the date is selected and changed. The most widely used events are discussed below.

| MonthCalendarAdv Events         | Description                                                                                                                                                                                                                      |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Border3DStyleChanged            | Event is raised when Border3DStyle property is changed.                                                                                                                                                                       |
| BorderColorChanged              | Event is raised when BorderColor property is changed.                                                                                                                                                                         |
| BorderSidesChanged              | Event is raised when BorderSides property is changed.                                                                                                                                                                         |
| BorderStyleChanged              | Event is raised when BorderStyle property is changed.                                                                                                                                                                         |
| DateCellQueryInfo               | It can be handled to provide custom formatting for calendar cells. The event handler receives an argument of type DateCellQueryInfoEventArgs. The following are the event properties associated with DateCellQueryInfoEventArgs argument. |
| DateSelected                    | It occurs when a date is selected from the calendar. It can be handled to retrieve the selected date of the MonthCalendarAdv. The event handler receives an argument of type EventArgs.                                            |
| DateChanged                     | Handled when a selected date is changed.                                                                                                                                                                                       |
| FirstDayOfWeekChanged           | Handled when the first day of the week is changed using FirstDayOfWeek property.                                                                                                                                             |
| NoneButtonClick                 | Handled when the None button is clicked.                                                                                                                                                                                       |
| ShowWeekNumbersChanged          | Handled when ShowWeekNumbers property is changed. We can customize the appearance of the week numbers within this handler.                                                                                                   |

## Page-level Navigation/TOC (if applicable)
- None

## Cross References
- None

<!-- tags: [MonthCalendarAdv, Event Handling, Windows Forms, Syncfusion] keywords: [MonthCalendarAdv, events, DateSelected, DateCellQueryInfo, ShowWeekNumbersChanged, Border3DStyleChanged, BorderColorChanged, BorderSidesChanged, BorderStyleChanged, DateSelected, DateChanged, FirstDayOfWeekChanged, NoneButtonClick] -->
```