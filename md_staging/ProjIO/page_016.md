```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: ProjIO
page_number: 016
page_id: ProjIO#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:48Z
fidelity: lossless
-->

## Essential ProjIO

### Properties and Descriptions

| Property                      | Description                                                                                                                                                                   |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InsertedProjectsLikeSummary   | True if subtasks are calculated as summary tasks.                                                                                                                            |
| MultipleCriticalPaths         | True if multiple critical paths are calculated.                                                                                                                              |
| NewTasksEffortDriven          | True if new tasks are effort-driven.                                                                                                                                         |
| NewTasksEstimated             | True to show the estimated duration by default.                                                                                                                              |
| SplitsInProgressTasks         | True if in-progress tasks can be split.                                                                                                                                      |
| SpreadActualCost               | True if actual costs are spread to the status date.                                                                                                                         |
| SpreadPercentComplete         | True if percent complete is spread to the status date.                                                                                                                      |
| TaskUpdatesResource           | True if updates to tasks update resources.                                                                                                                                   |
| FiscalYearStart               | True to use fiscal year numbering.                                                                                                                                           |
| WeekStartDay                  | Gets or sets the Start day of the week.                                                                                                                                      |
| MoveCompletedEndsBack         | True if the end of completed portions of tasks scheduled to begin after the status date but begun early should be moved back to the status date.                           |
| MoveRemainingStartsBack       | True if the beginning of remaining portions of tasks scheduled to begin after the status date but began early should be moved back to the status date.                       |
| MoveRemainingStartsForward    | True if the beginning of remaining portions of tasks scheduled to begin late should be moved up to the status date.                                                          |
| MoveCompleteEndsForward       | True if the end of completed portions of tasks scheduled to get completed before the status date but began late should be moved up to the status date.                        |
| BaselineForEarnedValue        | Gets or sets the specific baseline used to calculate Variance values.                                                                                                       |
| AutoAddNewResourcesAndTasks   | True to automatically add new resources to the resource pool.                                                                                                                |
| StatusDate                    | Gets or sets the date used for calculation and reporting.                                                                                                                   |
| CurrentDate                   | Gets or sets the system date that the XML was generated.                                                                                                                    |
| MicrosoftProjectServerURL     | True if the project was created by a Project Server user as opposed to an NT user.                                                                                           |
| Autolink                      | True to auto-link inserted or moved tasks.                                                                                                                                   |

### API Reference

For detailed API information related to the properties listed above, refer to the Syncfusion Winforms documentation for version 11.4.0.26. The properties listed in this section are part of the `ProjIO` module, which provides essential functionality for managing project schedules and task dependencies within the WinForms framework.

## Code Examples

Example of setting and retrieving the `StatusDate` property in C#:

```csharp
// Setting the StatusDate
project.StatusDate = new DateTime(2023, 10, 5);

// Retrieving the StatusDate
DateTime statusDate = project.StatusDate;
```

### RAG Annotations

- **Tags:** Essential ProjIO, properties, task scheduling, cost estimation
- **Keywords:** status date, critical paths, effort-driven tasks, fiscal year, project server, auto-link
```