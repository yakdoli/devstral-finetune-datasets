```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: ProjIO
page_number: 057
page_id: ProjIO#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:38Z
fidelity: lossless
-->

# Essential ProjIO

## 4.5 Calendar

The Calendar class is used to create calendars and add them to the project. Using the Calendar class, one can create calendar exceptions (holidays, different working times and working days), define working days, working times, and so on. It can also add a standard calendar to the project. The Calendar class contains properties that can be used to retrieve information of all calendars present in a project.

### 4.5.1 Properties, Methods, and Events Tables for Task

#### 4.5.1.1 Constructors

**Table 16: Calendar Constructors**

| Name                        | Description                              |
|-----------------------------|------------------------------------------|
| `Calendar.Calendar()`      | Initializes a new instance of Calendar class. |
| `Calendar.Calendar(string calendarName)` | Initializes a new instance of Calendar class with the calendar name. |

#### 4.5.1.2 Properties

**Table 17: Calendar Properties**

| Property            | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `UID`              | Gets or sets the unique identifier of the calendar.                        |
| `Name`             | Gets or sets the name of the calendar.                                     |
| `IsBaseCalendar`   | True if the calendar is a base calendar.                                   |
| `IsBaselineCalendar` | True if the calendar is a baseline calendar.                             |
| `BasecalendarUID`  | Gets or sets the unique identifier of the base calendar on which this calendar depends. Only applicable if the calendar is not a base calendar. |
| `WeekDays`         | Gets or sets the collection of weekdays that defines this calendar.         |
| `Exceptions`       | Gets or sets the collection of exceptions that is associated with the calendar. |
| `WorkWeeks`        | Gets or sets the collection of effective work weeks associated with the calendar. |
```