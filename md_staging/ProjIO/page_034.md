```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_034.jpeg
document_name: ProjIO
page_number: 034
page_id: ProjIO#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:48Z
fidelity: lossless
-->

## Property and Description Table

The following table lists various properties and their descriptions related to task management in a scheduling or project management context.

### Property Descriptions

| Property                    | Description                                                                                   |
|-----------------------------|---------------------------------------------------------------------------------------------|
| RemainingOvertimeWork      | Gets or sets the remaining overtime work scheduled to finish the task.                       |
| ACWP                        | Gets or sets the actual cost of work performed on the task to-date.                          |
| CV                          | Gets or sets the earned value cost variance.                                                 |
| ConstraintType              | Gets or sets the constraint on the start or finish date of the task.                        |
| CalendarUID                | Gets or sets the task calendar. Refers to a valid UID in the Calendars collection.            |
| ConstraintDate              | Gets or sets the date argument for the task constraint type.                                |
| Deadline                   | Gets or sets the deadline for the task to be completed.                                      |
| LevelAssignments           | True if leveling can adjust assignments.                                                     |
| LevelingCanSplit           | True if leveling can split the task.                                                         |
| LevelingDelay              | Gets or sets the delay caused by leveling the task.                                          |
| LevelingDelayFormat        | Gets or sets the format for expressing the duration of the delay.                           |
| PreLevelStart              | Gets or sets the start date of the task before it was leveled.                              |
| PreLevelFinish             | Gets or sets the finish date of the task before it was leveled.                             |
| Hyperlink                   | Gets or sets the title of the hyperlink associated with the task.                           |
| HyperlinkAddress            | Gets or sets the hyperlink associated with the task.                                       |
| HyperlinkSubAddress        | Gets or sets the document bookmark of the hyperlink associated with the task.                |
| IgnoreResourceCalendar     | True if the task ignores the resource calendar.                                              |
| Notes                      | Gets or sets the text notes associated with the task.                                         |
| HideBar                    | True if the GANTT bar of the task is hidden when displayed in Microsoft Project.              |

## Notes
- The `CalendarUID` refers to a valid UID in the Calendars collection, indicating that the task is associated with a specific calendar.
- The leveling-related properties (`LevelAssignments`, `LevelingCanSplit`, `PreLevelStart`, etc.) are used to manage task scheduling when resource leveling is applied.
- The `Hyperlink` properties provide ways to associate URLs or document bookmarks with tasks for additional references or documentation.

### Related Properties and Methods
- **ACWP**: Actual Cost Work Performed
- **CV**: Cost Variance
- **ConstraintType**: Constraint types include Start No Earlier Than, Start No Later Than, etc.
- **PreLevelStart`, `PreLevelFinish`: These properties store the task's start and finish dates before leveling is applied.

## RAG Annotations

The document provides a detailed listing of properties related to task management and scheduling, particularly useful for understanding various attributes and functionalities within project management software like Microsoft Project.

<!-- tags: [Syncfusion, Winforms, TaskManagement, ProjectManagement] keywords: [task, resource leveling, GANTT bar, cost variance, calendar UID, hyperlink, deadline, overtime work] -->
```