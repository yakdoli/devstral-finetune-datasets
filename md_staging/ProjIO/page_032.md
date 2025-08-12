```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: ProjIO
page_number: 032
page_id: ProjIO#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:00Z
fidelity: lossless
-->

## Overview

- Explains the properties of a task in a project management context.
- Describes attributes such as OverAllocated, Estimated, Milestone, Summary, and more.
- Includes information about scheduling and task dependencies like EarlyStart, LateFinish, FreeSlack, and others.

## Content

| Property                   | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| OverAllocated              | True if the task is overallocated.                                         |
| Estimated                  | True if the task is estimated.                                             |
| Milestone                  | True if the task is a milestone.                                           |
| Summary                    | True if the task is a summary task.                                        |
| DisplayAsSummary           | True if the task should be displayed as a summary task.                   |
| Critical                   | True if the task is in the critical chain.                                 |
| IsSubProject               | True if the task is an inserted project.                                  |
| IsSubProjectReadOnly       | True if the inserted project is read-only.                                |
| SubProjectName             | Gets or sets the source location of the inserted project.                 |
| ExternalTask               | True if the task is external.                                              |
| ExternalTaskProject        | Gets or sets the source location and task identifier of the external task. |
| EarlyStart                 | Gets or sets the early start date of the task.                             |
| EarlyFinish                | Gets or sets the early finish date of the task.                           |
| LateStart                  | Gets or sets the late start date of the task.                             |
| LateFinish                 | Gets or sets the late finish date of the task.                            |
| StartVariance              | Gets or sets the variance of the task start date from the baseline start date as minutes × 1000. |
| FinishVariance             | Gets or sets the variance of the task finish date from the baseline finish date as minutes × 1000. |
| WorkVariance               | Gets or sets the variance of task work from the baseline task work as minutes × 1000. |
| FreeSlack                  | Gets or sets the amount of free slack.                                    |
| StartSlack                 | Gets or sets the amount of free slack at the start of the task.           |
| FinishSlack                | Gets or sets the amount of free slack at the end of the task.             |
| TotalSlack                 | Gets or sets the amount of total slack.                                   |

## API Reference

- **Namespace**: Essential ProjIO
- **Properties**:
  - `OverAllocated`: Boolean
  - `Estimated`: Boolean
  - `Milestone`: Boolean
  - `Summary`: Boolean
  - `DisplayAsSummary`: Boolean
  - `Critical`: Boolean
  - `IsSubProject`: Boolean
  - `IsSubProjectReadOnly`: Boolean
  - `SubProjectName`: String
  - `ExternalTask`: Boolean
  - `ExternalTaskProject`: String
  - `EarlyStart`: DateTime
  - `EarlyFinish`: DateTime
  - `LateStart`: DateTime
  - `LateFinish`: DateTime
  - `StartVariance`: Integer
  - `FinishVariance`: Integer
  - `WorkVariance`: Integer
  - `FreeSlack`: Double
  - `StartSlack`: Double
  - `FinishSlack`: Double
  - `TotalSlack`: Double

## Tags and Keywords

<!-- tags: Essential ProjIO, task properties, project management attributes, critical chain, free slack, variance, subproject, milestone, estimated task, overallocated task keywords: OverAllocated, Estimated, Milestone, Summary, DisplayAsSummary, Critical, IsSubProject, IsSubProjectReadOnly, SubProjectName, ExternalTask, ExternalTaskProject, EarlyStart, EarlyFinish, LateStart, LateFinish, StartVariance, FinishVariance, WorkVariance, FreeSlack, StartSlack, FinishSlack, TotalSlack -->
```