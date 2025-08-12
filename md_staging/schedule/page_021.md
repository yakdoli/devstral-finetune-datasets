```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: schedule
page_number: 021
page_id: schedule#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:08:53Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- The page introduces the ScheduleControl in the Essential Schedule for Windows Forms, showcasing a week view.
- It details the WorkWeek view and mentions a Snapshot of the Week view.
- The NavigationCalendar is highlighted, with an emphasis on week numbers appearing on the left side of each week.

## Content

### ScheduleControl in Windows Forms
- **Figure 11: ScheduleControl showing a WorkWeek View**
  - This figure illustrates the ScheduleControl displaying a workweek, equipped with scheduling details and events for each day.
  - The left section features a NavigationCalendar that includes week numbers, which can be turned off using the `ScheduleControl.Calendar.ShowWeekNumbers` property.

### NavigationCalendar
- The NavigationCalendar on the left side of the figure shows the weeks in November 2006, December 2006, and January 2007.
- Each week's number is displayed on the left side, providing an overview of the months.
- Users have the option to disable these week numbers using the property `ScheduleControl.Calendar.ShowWeekNumbers`.

### Schedule Details
- The right section of the image displays a detailed schedule for a week starting October 30, 2006.
- Key events and appointments are color-coded and grouped by specific times.
- Notable entries include:
  - **Vacation** on October 31
  - **MMM 10:00** 
  - **Aspect design** at 10:00 on November 1
  - **Dr's Appt** at 10:00 on November 1
  - **Call Joe** at 13:00 on November 2
  - **Pick up James** noted on November 2

### Time Slots in the Schedule
- The schedule is divided into hourly slots, ranging from 10:00 am to 8:00 pm.
- Each time slot can contain one or more appointments or events, color-coded for easy identification.
- The manner in which the schedule is organized facilitates efficient time management and event tracking.

### Optional Customization
- The property `ScheduleControl.Calendar.ShowWeekNumbers` provides users with the ability to control the visibility of week numbers in the NavigationCalendar.
- If users prefer a cleaner view without week numbers, they can disable this feature.

## Summary
- The ScheduleControl provides a comprehensive scheduling interface in Windows Forms, featuring a detailed workweek view.
- The NavigationCalendar helps in managing multiple months with the option to display or hide week numbers.
- The scheduling grid effectively organizes events, ensuring effective time management.

## Page-level Navigation/TOC (if applicable)
- This section provides a structured view of the schedule control for Windows Forms, specifically focusing on the WorkWeek view and the customizability of the NavigationCalendar.

## Cross References
- For more detailed information on the ScheduleControl and its properties, refer to the "ScheduleControl Reference" section in the documentation.
- Additional resources on using the NavigationCalendar can be consulted in the "Calendar Component Guide."

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [workweekview, weeknumbers, navigationcalendar, schedulecontrol, windowsforms, syncfusion] -->
```