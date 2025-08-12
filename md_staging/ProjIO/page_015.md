```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: ProjIO
page_number: 015
page_id: ProjIO#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:53Z
fidelity: lossless
-->

## Overview

- This page provides a detailed list of properties and their descriptions related to project management and scheduling in the `ProjIO` class.
- These properties allow the customization of project settings such as dates, calendars, financial parameters, task types, and earned value methods.
- Each property is designed to either get or set specific attributes, enabling precise control over project configurations.

## Content

### Property Descriptions

| Property                   | Description                                                                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| FinishDate                 | Gets or sets the finish date of the project. Required if ScheduleFromStart is false.                                                                 |
| FYStartDate                | Gets or sets the Fiscal Year starting month.                                                                                                          |
| CriticalSlackLimit         | Gets or sets the number of days past its end date that a task can go before Microsoft Project marks that task as a critical task.                      |
| CurrencyDigits             | Gets or sets the number of digits after the decimal symbol.                                                                                         |
| CurrencySymbol             | Gets or sets the currency symbol used in the project.                                                                                                |
| CurrencyCode               | Gets or sets the three-letter currency character code as defined in ISO 4217. Only USD is supported.                                                  |
| CurrencySymbolPosition     | Gets or sets the position of the currency symbol.                                                                                                    |
| CalendarUID                | Gets or sets the project calendar UID. Refers to a valid UID in the Calendars collection.                                                             |
| Calendar                   | Gets or sets the project calendar.                                                                                                                    |
| DefaultStartTime           | Gets or sets the default start time of new tasks.                                                                                                    |
| DefaultFinishTime          | Gets or sets the default finish time of new tasks.                                                                                                   |
| MinutesPerDay              | Gets or sets the number of minutes per day.                                                                                                          |
| MinutesPerWeek             | Gets or sets the number of minutes per week.                                                                                                         |
| DaysPerMonth               | Gets or sets the number of days per month.                                                                                                           |
| DefaultTaskType            | Gets or sets the default type of new tasks.                                                                                                          |
| DefaultFixedCostAccrual    | Gets or sets the default from where fixed costs are accrued.                                                                                        |
| DefaultStandardRate        | Gets or sets the default standard rate for new resources.                                                                                           |
| DefaultOvertimeRate        | Gets or sets the default overtime rate for new resources.                                                                                           |
| DurationFormat             | Gets or sets the format for expressing the bulk duration.                                                                                           |
| WorkFormat                 | Gets or sets the default work unit format.                                                                                                           |
| EditableActualCosts        | True if actual costs are editable.                                                                                                                    |
| HonorConstraints           | True if tasks honor their constraint dates.                                                                                                          |
| EarnedValueMethod          | Gets or sets the default method for calculating earned value.                                                                                       |

### Explanation

These properties provide comprehensive control over various aspects of a project, including scheduling, financial settings, and task management. They allow developers to tailor project configurations to meet specific needs, ensuring that all aspects of the project are managed efficiently.

#### Calendar and Time-related Properties
- **FinishDate**: Essential for setting completion milestones.
- **FYStartDate**: Useful for aligning projects with fiscal years.
- **CalendarUID/Calendar**: Allows selection of specific calendars, such as standard working hours or custom schedules.

#### Financial and Cost-related Properties
- **CurrencyDigits/CurrencySymbol/CurrencyCode**: Ensures accurate monetary representations in reports and projects.
- **DefaultFixedCostAccrual**: Useful for defining cost accrual policies.

#### Task and Schedule-related Properties
- **DefaultStartTime/DefaultFinishTime**: Simplifies the setup of new tasks by providing default timing.
- **MinutesPerDay/MinutesPerWeek/DaysPerMonth**: Used for configuring the duration and availability of work days.

#### Project Management Properties
- **HonorConstraints**: Ensures that tasks respect their specified constraints.
- **EarnedValueMethod**: Enables tracking project performance against planned values.

## API Reference (if applicable)

```csharp
// Example usage of some properties
using Syncfusion.ProjIO;

void ConfigureProject(Project proj)
{
    proj.FinishDate = new DateTime(2023, 12, 31);
    proj.FYStartDate = 4; // First fiscal quarter starts in April
    proj.DefaultTaskType = TaskType.FMTask; // Fixed Duration Task
    proj.DefaultStandardRate = 100; // Default hourly rate
    proj.CalendarUID = 1; // Use the default calendar
    proj.DurationFormat = "h"; // Use hours for duration format
    proj.HonorConstraints = true; // Ensure tasks adhere to constraints
    proj.EarnedValueMethod = EarnedValueMethod.PercentComplete; // Calculate based on task progress
}
```

## Code Examples

### Demonstrating Setting Project Properties

```csharp
using Syncfusion.ProjIO;

// Initialize a new project
Project project = new Project();

// Configure project properties
project.FinishDate = new DateTime(2023, 12, 31);
project.FYStartDate = 4;
project.DefaultTaskType = TaskType.FMTask;
project.DefaultStandardRate = 100;
project.CalendarUID = 1;
project.DurationFormat = "h";
project.HonorConstraints = true;
project.EarnedValueMethod = EarnedValueMethod.PercentComplete;

// Save the project
project.Save("project.mpp");
```

### Retrieving Project Properties

```csharp
using Syncfusion.ProjIO;

// Load an existing project
Project project = Project.Load("existingProject.mpp");

// Retrieve and display some project properties
Console.WriteLine("Finish Date: " + project.FinishDate);
Console.WriteLine("Fiscal Year Start Month: " + project.FYStartDate);
Console.WriteLine("Default Task Type: " + project.DefaultTaskType);
Console.WriteLine("Default Standard Rate: " + project.DefaultStandardRate);
Console.WriteLine("Calendar UID: " + project.CalendarUID);
Console.WriteLine("Duration Format: " + project.DurationFormat);
Console.WriteLine("Honors Constraints: " + project.HonorConstraints);
Console.WriteLine("Earned Value Method: " + project.EarnedValueMethod);
```

## Summary

This page provides a detailed overview of various properties that developers can leverage to manage and configure projects effectively. By utilizing these properties, projects can be customized to meet specific scheduling, financial, and task management requirements, ensuring efficient project execution and management.

<!-- tags: project management, scheduling, calendar, financial, task types, earned value method, Syncfusion Winforms, ProjIO class, properties keywords: FinishDate, FYStartDate, CriticalSlackLimit, CurrencyDigits, CurrencySymbol, CurrencyCode, CurrencySymbolPosition, CalendarUID, Calendar, DefaultStartTime, DefaultFinishTime, MinutesPerDay, MinutesPerWeek, DaysPerMonth, DefaultTaskType, DefaultFixedCostAccrual, DefaultStandardRate, DefaultOvertimeRate, DurationFormat, WorkFormat, EditableActualCosts, HonorConstraints, EarnedValueMethod -->
```