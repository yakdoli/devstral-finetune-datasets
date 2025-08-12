```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_035.jpeg
document_name: ProjIO
page_number: 035
page_id: ProjIO#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:27Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Lists key properties related to task management and project tracking.
- Focuses on budgeted costs, task status, scheduling, and earned value calculations.
- Provides detailed descriptions of each property's purpose and usage.

## Content

### Properties and Descriptions

| Property                   | Description                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------|
| **Rollup**                 | True if the task is rolled up.                                                                 |
| **BCWS**                   | Gets or sets the budgeted cost of work scheduled for the task.                                |
| **BCWP**                   | Gets or sets the budgeted cost of work performed on the task to-date.                          |
| **PhysicalPercentComplete** | Gets or sets the percentage complete value entered by the Project Manager.                    |
| **EarnedValueMethod**      | Gets or sets the method for calculating earned value.                                         |
| **PredecessorLink**        | Gets or sets the predecessor task of the task that contains it.                               |
| **ActualWorkProtected**    | Gets or sets the duration through which actual work is protected.                              |
| **ActualOvertimeWorkProtected** | Gets or sets the duration through which actual overtime work is protected.                 |
| **ExtendedAttribute**      | Gets or sets the value of an extended attribute.                                             |
| **Baseline**               | Gets or sets the collection of baseline values of the task.                                   |
| **OutlineCode**            | Gets or sets the value of an outline code.                                                   |
| **IsPublished**            | True if the task is published.                                                                 |
| **StatusManager**          | Gets or sets the name of the task status manager.                                             |
| **CommitmentStart**        | Gets or sets the start date of the deliverable.                                              |
| **CommitmentFinish**       | Gets or sets the finish date of the deliverable.                                             |
| **CommitmentType**         | Gets or sets the commitment type of the deliverable.                                         |
| **Active**                 | True if the task is active.                                                                   |
| **Pinned**                 | True if the task is in manually scheduled mode.                                              |
| **PinnedStart**            | Gets or sets text displayed in start field when the task is in Manually Scheduled mode.       |
| **PinnedFinish**           | Gets or sets text displayed in finish field when the task is in Manually Scheduled mode.      |

## API Reference

### Properties

- **Rollup**: Bool
- **BCWS**: Double
- **BCWP**: Double
- **PhysicalPercentComplete**: Double
- **EarnedValueMethod**: Enum
- **PredecessorLink**: Object
- **ActualWorkProtected**: DateTime
- **ActualOvertimeWorkProtected**: DateTime
- **ExtendedAttribute**: String
- **Baseline**: Object
- **OutlineCode**: String
- **IsPublished**: Bool
- **StatusManager**: String
- **CommitmentStart**: DateTime
- **CommitmentFinish**: DateTime
- **CommitmentType**: Enum
- **Active**: Bool
- **Pinned**: Bool
- **PinnedStart**: String
- **PinnedFinish**: String

<!-- tags: [Syncfusion, Winforms, Task Management, Project Tracking, Cost Management,Earned Value Method, Predecessor Task] keywords: [Rollup, BCWP, BCWS, PhysicalPercentComplete, ActualWorkProtected, Manual Scheduling, Deliverable] -->
```