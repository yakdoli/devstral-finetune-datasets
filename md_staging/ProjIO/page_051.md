```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: ProjIO
page_number: 051
page_id: ProjIO#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:42Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Lists properties and their descriptions for managing assignments and tasks in a project.
- Includes details such as response status, scheduling, progress tracking, and financial variance.

## Content

### Property Descriptions
The following table outlines the properties and their functions for managing assignments and tasks:

| Property                | Description                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
| ResponsePending         | Whether a response has been received for a TeamAssign message.                                           |
| Start                   | Gets or sets the scheduled start date of the assignment.                                                   |
| Stop                    | Gets or sets the date that the assignment was stopped.                                                      |
| Resume                  | Gets or sets the date that the assignment resumed.                                                          |
| StartVariance           | Gets or sets the variance of the assignment start date from the baseline start date.                      |
| Summary                 | Whether the task is a summary task.                                                                           |
| SV                      | Gets or sets the earned value schedule variance, through the project status date.                          |
| Units                   | Gets or sets the number of units for the assignment.                                                        |
| UpdateNeeded            | Whether the resource assigned to a task needs to be updated as to the status of the task.                  |
| VAC                     | Gets or sets the difference between baseline cost and total cost.                                          |
| Work                    | Gets or sets the amount of scheduled work for the assignment.                                               |
| WorkContour             | Gets or sets the work contour of the assignment.                                                             |
| BCWS                    | Gets or sets the budgeted cost of work on the assignment.                                                   |
| BCWP                    | Gets or sets the budgeted cost of work performed on the assignment to-date.                                |
| BookingType             | Gets or sets the booking type of the assignment.                                                            |
| ActualWorkProtected     | Gets or sets the duration through which actual work is protected.                                          |
| ActualOvertimeWorkProtected | Gets or sets the duration through which actual overtime work is protected.                             |
| CreationDate            | Gets or sets the date the assignment was created.                                                           |

## API Reference
### Properties
- `ResponsePending`: Boolean indicating if a response has been received.
- `Start`: DateTime representing the scheduled start of the assignment.
- `Stop`: DateTime representing the date the assignment was stopped.
- `Resume`: DateTime representing the date the assignment resumed.
- `StartVariance`: Double indicating the variance from the baseline start date.
- `Summary`: Boolean indicating if the task is a summary task.
- `SV`: Double representing the schedule variance.
- `Units`: Integer representing the number of units.
- `UpdateNeeded`: Boolean indicating if the task resource needs updates.
- `VAC`: Double representing the variance in actual cost.
- `Work`: Double representing the scheduled work.
- `WorkContour`: Double representing the work contour.
- `BCWS`: Double representing the budgeted cost of work.
- `BCWP`: Double representing the budgeted cost of work performed.
- `BookingType`: Enum representing the booking type.
- `ActualWorkProtected`: Double representing the duration of protected actual work.
- `ActualOvertimeWorkProtected`: Double representing the duration of protected actual overtime work.
- `CreationDate`: DateTime representing the creation date of the assignment.

## Code Examples

### CSharp Example
```csharp
// Example of setting properties
assignment.Start = DateTime.Now;
assignment.Work = 40.0;
assignment.ActualWorkProtected = 5.0;
```

## Page-level Navigation/TOC (if applicable)
- [ ] Property Descriptions
- [ ] API Reference
- [ ] Code Examples

## Cross References
- Related properties and methods in the Syncfusion WinForms documentation.

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, ProjIO, properties, task management, assignment, cost variance, schedule variance, work contour, budgeted cost] keywords: [ResponsePending, Start, Stop, Resume, StartVariance, Summary, SV, Units, UpdateNeeded, VAC, Work, WorkContour, BCWS, BCWP, BookingType, ActualWorkProtected, ActualOvertimeWorkProtected, CreationDate] -->
```