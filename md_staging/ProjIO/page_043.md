```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: ProjIO
page_number: 043
page_id: ProjIO#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:07Z
fidelity: lossless
-->

Essential ProjIO

## Overview
- This page lists properties and their descriptions related to resource management in software projects using Syncfusion Winforms.
- Key sections include details on work allocation, overtime tracking, cost accrual, and percentage completion.
- Focuses on various parameters that influence scheduling and budgeting in project management.

## Content

### Resource Management Properties

| Property               | Description                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------------|
| AccrueAt              | Gets or sets how cost is accrued against the resource.                                                |
| Work                  | Gets or sets the total work assigned to the resource across all assigned tasks.                      |
| RegularWork           | Gets or sets the amount of non-overtime work assigned to the resource.                               |
| OvertimeWork          | Gets or sets the amount of overtime work assigned to the resource.                                   |
| ActualWork            | Gets or sets the amount of actual work performed by the resource.                                    |
| RemainingWork         | Gets or sets the amount of remaining work required to complete all assigned tasks.                  |
| ActualOvertimeWork    | Gets or sets the amount of actual overtime work performed by the resource.                           |
| RemainingOvertimeWork | Gets or sets the amount of remaining overtime work required to complete all tasks.                  |
| PercentWorkComplete   | Gets or sets the percentage of work completed across all tasks.                                      |
| StandardRate          | Gets or sets the standard rate of the resource. This value is as of the current date if a rate table exists for the resource. |
| StandardRateFormat    | Gets or sets the units used by Microsoft Project to display the standard rate.                      |
| Cost                  | Gets or sets the total project cost for the resource across all assigned tasks.                      |
| OvertimeRate          | Gets or sets the overtime rate of the resource. This value is as of the current date if a rate table exists for the resource. |
| OvertimeRateFormat    | Gets or sets the units used by Microsoft Project to display the overtime rate.                      |
| OvertimeCost          | Gets or sets the total overtime cost for the resource including actual and remaining overtime costs. |

## API Reference (if applicable)
- The table above can be directly mapped to API references for properties and their functionalities in project resource management.

## Code Examples (multi-language supported)
- No direct code examples are provided in this table, but the properties listed can be used in various programming contexts, such as:
  ```csharp
  // Example of setting a property
  project.Resource[resourceName].StandardRate = newRate;
  ```

## Page-level Navigation/TOC (if applicable)
- This page does not contain a Table of Contents (TOC) section. However, it is indexed under 'Resource Management Properties.'

## Cross References
- This content may be cross-referenced with detailed sections on project scheduling and financial management within the software.

## RAG Annotations
<!-- tags: resource management, project budgeting, task scheduling, overtime tracking, project cost, Winforms SDK, Syncfusion SDK keywords: AccrueAt, Work, RegularWork, OvertimeWork, ActualWork, RemainingWork, ActualOvertimeWork, RemainingOvertimeWork, PercentWorkComplete, StandardRate, OvertimeRate, OvertimeCost -->
```