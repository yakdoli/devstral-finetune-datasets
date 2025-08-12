```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: ProjIO
page_number: 049
page_id: ProjIO#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:57Z
fidelity: lossless
-->

## Overview
- This page details the properties and their descriptions related to project assignments and resource management in a software project management context.
- It includes information on various financial, temporal, and resource-related parameters pertinent to task management.

## Content

### Table of Properties

| Property              | Description                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------|
| ActualFinish         | Gets or sets the actual finish date of the assignment.                                              |
| ActualOvertimeCost   | Gets or sets the actual overtime cost incurred on the assignment.                                  |
| ActualOvertimeWork   | Gets or sets the actual amount of overtime work incurred on the assignment.                        |
| ActualStart          | Gets or sets the actual start date of the assignment.                                               |
| ActualWork           | Gets or sets the actual amount of work incurred on the assignment.                                 |
| ACWP                 | Gets or sets the actual cost of work performed on the assignment to-date.                          |
| Confirmed            | Whether the Resource has accepted all of his or her assignments.                                   |
| Cost                 | Gets or sets the projected or scheduled cost of the assignment.                                    |
| CostRateTable        | Gets or sets the cost rate table used for the assignment.                                         |
| CostVariance         | Gets or sets the difference between the cost and baseline cost for a resource.                    |
| CV                   | Gets or sets the earned value cost variance.                                                        |
| Delay                | Gets or sets the amount that the assignment is delayed.                                            |
| Finish               | Gets or sets the scheduled finish date of the assignment.                                          |
| FinishVariance       | Gets or sets the variance of the assignment finish date from the baseline finish date.           |
| Hyperlink            | Gets or sets the title of the hyperlink associated with the assignment.                           |
| HyperlinkAddress     | Gets or sets the hyperlink associated with the assignment.                                        |
| HyperlinkSubAddress  | Gets or sets the document bookmark of the hyperlink associated with the assignment.               |

## API Reference

### Properties

- **ActualFinish**  
  - **Description**: Gets or sets the actual finish date of the assignment.
- **ActualOvertimeCost**  
  - **Description**: Gets or sets the actual overtime cost incurred on the assignment.
- **ActualOvertimeWork**  
  - **Description**: Gets or sets the actual amount of overtime work incurred on the assignment.
- **ActualStart**  
  - **Description**: Gets or sets the actual start date of the assignment.
- **ActualWork**  
  - **Description**: Gets or sets the actual amount of work incurred on the assignment.
- **ACWP**  
  - **Description**: Gets or sets the actual cost of work performed on the assignment to-date.
- **Confirmed**  
  - **Description**: Whether the Resource has accepted all of his or her assignments.
- **Cost**  
  - **Description**: Gets or sets the projected or scheduled cost of the assignment.
- **CostRateTable**  
  - **Description**: Gets or sets the cost rate table used for the assignment.
- **CostVariance**  
  - **Description**: Gets or sets the difference between the cost and baseline cost for a resource.
- **CV**  
  - **Description**: Gets or sets the earned value cost variance.
- **Delay**  
  - **Description**: Gets or sets the amount that the assignment is delayed.
- **Finish**  
  - **Description**: Gets or sets the scheduled finish date of the assignment.
- **FinishVariance**  
  - **Description**: Gets or sets the variance of the assignment finish date from the baseline finish date.
- **Hyperlink**  
  - **Description**: Gets or sets the title of the hyperlink associated with the assignment.
- **HyperlinkAddress**  
  - **Description**: Gets or sets the hyperlink associated with the assignment.
- **HyperlinkSubAddress**  
  - **Description**: Gets or sets the document bookmark of the hyperlink associated with the assignment.

## Code Examples

The following example demonstrates how to access and set the `ActualFinish` property:

```csharp
// Accessing the ActualFinish property
DateTime actualFinish = assignment.ActualFinish;

// Setting the ActualFinish property
assignment.ActualFinish = new DateTime(2023, 12, 31);
```

## Cross References

See also:
- [Other related documentation on project management](#)
- [Resource management guidelines](#)

<!-- tags: Syncfusion, Winforms, Project Management, Assignment Properties, Cost, Timeline, Overtime, Resource Management keywords: Project, Assignment, Cost, Timeline, Overtime, Resource, Management, Properties -->
```