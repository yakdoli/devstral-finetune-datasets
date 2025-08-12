```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: ProjIO
page_number: 044
page_id: ProjIO#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:46Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Provides details about resource-related properties in a project management context.
- Includes cost, work, and variance metrics for resource utilization.
- Describes the status and characteristics of resources such as generic, inactive, and enterprise status.

## Content

The following table lists the properties associated with resource management, along with their descriptions:

| Property                   | Description                                                                                                                    |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| CostPerUse                | Gets or sets the cost per use of the resource.<br>This value is as of the current date if a rate table exists for the resource. |
| ActualCost                | Gets or sets the actual cost incurred by the resource across all assigned tasks.                                              |
| ActualOvertimeCost        | Gets or sets the actual overtime cost incurred by the resource across all assigned tasks.                                      |
| RemainingCost             | Gets or sets the remaining projected cost of the resource to complete all assigned tasks.                                     |
| RemainingOvertimeCost     | Gets or sets the remaining projected overtime cost of the resource to complete all assigned tasks.                           |
| WorkVariance              | Gets or sets the difference between the baseline work and the work as minutes x 1000.                                        |
| CostVariance              | Gets or sets the difference between the baseline cost and the cost.                                                          |
| SV                        | Gets or sets the earned value schedule variance, through the project status date.                                            |
| CV                        | Gets or sets the earned value cost variance, through the project status date.                                                |
| ACWP                      | Gets or sets the actual cost of the work performed by the resource for the project to-date.                                   |
| CalendarUID               | Gets or sets the resource calendar. Refers to a valid UID in the Calendars collection.                                       |
| Notes                     | Gets or sets the text notes associated with the resource.                                                                    |
| BCWS                      | Gets or sets the budget cost of work scheduled for the resource.                                                             |
| BCWP                      | Gets or sets the budgeted cost of the work performed by the resource for the project to-date.                                 |
| IsGeneric                 | True if the resource is generic.                                                                                              |
| IsInactive                | True if the resource is set to inactive.                                                                                     |
| IsEnterprise              | True if the resource is an Enterprise resource.                                                                             |

## API Reference
- The table above provides details about the properties that can be used to manage and track resource costs, work, and status in a project management context.
- These properties can be accessed and modified as needed to maintain accurate project data and resource utilization.

## Code Examples

```csharp
// Example: Accessing the ActualCost property for a resource
using Syncfusion.ProjIO;

// assuming rp is a Resource object
double actualCost = rp.ActualCost;
Console.WriteLine($"Actual Cost: {actualCost}");
```

## Cross References
- See also: Essential ProjIO documentation for more information on resource management and variance reporting.

<!-- tags: [projio, resource management, cost, work, variance, project status, csharp] keywords: [resource properties, actual cost, overtime cost, remaining cost, resource status] -->
```