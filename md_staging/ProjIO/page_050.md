```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: ProjIO
page_number: 050
page_id: ProjIO#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:54Z
fidelity: lossless
-->

## Property-Detailed Descriptions

The following table lists various properties relevant to project scheduling and resource management, providing detailed descriptions of each property.

### Property List with Descriptions

| **Property**            | **Description**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| **WorkVariance**        | Gets or sets the variance of assignment work from the baseline work as minutes x 1000. |
| **HasFixedRateUnits**   | Whether the Units are Fixed Rate.                                              |
| **FixedMaterial**       | Whether the consumption of the assigned material resource occurs in a single, fixed amount. |
| **LevelingDelay**       | Gets or sets the delay caused by leveling.                                     |
| **LevelingDelayFormat** | Gets or sets the format for expressing the duration of the delay.              |
| **LinkedFields**        | Whether the Project is linked to another OLE object.                           |
| **Milestone**           | Whether the assignment is a milestone.                                         |
| **Notes**               | Gets or sets the text notes associated with the assignment.                   |
| **Overallocated**       | Whether the assignment is over allocated.                                      |
| **OvertimeCost**        | Gets or sets the sum of the actual and remaining overtime cost of the assignment. |
| **OvertimeWork**        | Gets or sets the scheduled overtime work scheduled for the assignment.         |
| **PeakUnits**           | Gets or sets the largest number of units that a resource is assigned for a task. |
| **RateScale**           | Gets or sets the time unit for the usage rate of the material resource assignment. |
| **RegularWork**         | Gets or sets the amount of non-overtime work scheduled for the assignment.      |
| **RemainingCost**       | Gets or sets the remaining projected cost of completing the assignment.         |
| **RemainingOvertimeCost** | Gets or sets the remaining projected overtime cost of completing the assignment. |
| **RemainingOvertimeWork** | Gets or sets the remaining overtime work scheduled to complete the assignment. |
| **RemainingWork**       | Gets or sets the remaining work scheduled to complete the assignment.           |

## Overarching Overview
- **Scheduling and Resource Management**: This page provides a comprehensive list of properties that are essential for managing and scheduling projects and tasks within a project management system.
- **Assignment Work Variance**: The `WorkVariance` property is crucial for understanding deviations in work schedules from the baseline.
- **Resource Consumption Tracking**: Properties like `FixedMaterial` and `OvertimeCost` help track the use of resources and associated costs effectively.

## API Reference
- **Methods**: No methods are explicitly mentioned in this section.
- **Properties**: Detailed descriptions of various properties related to scheduling and resource tracking as listed above.

## Code Examples

### Example: Retrieving Work Variance

```csharp
// Example of retrieving work variance
decimal workVariance = assignment.WorkVariance;
```

### Example: Assigning Notes

```csharp
// Example of setting assignment notes
assignment.Notes = "Completed initial review.";
```

## Cross References
- **Related Documentation**: For more information on scheduling and resource management, refer to the [Project Scheduling Guide](link_to_documentation).
- **API Documentation**: Consult the [Properties Overview](link_to_properties_overview) for additional details.

<!-- tags: Syncfusion, Winforms, Project Management, Assignment, Overtime, Variance keywords: WorkVariance, Overallocated, OvertimeCost, Milestone, Notes, PeakUnits -->
```