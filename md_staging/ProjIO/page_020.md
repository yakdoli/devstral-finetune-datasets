```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: ProjIO
page_number: 020
page_id: ProjIO#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:06Z
fidelity: lossless
-->

## Overview
- Demonstrates how to retrieve and display project properties using the `Project` class in C#. 
- Explains reading projects from XML files.
- Includes sample code for accessing start date, finish date, scheduling information, current date, status date, and calendar.

## Content

### Retrieving Project Properties

#### Overview
The project properties can be retrieved using the `Project` class, which provides access to various properties of a project. This section shows how to get and display these properties.

#### C# Code Example

```csharp
// Calling Open method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Displaying Project information
Console.WriteLine("Project Start Date: " + project.StartDate);

if (project.ScheduleFromStart)
{
    Console.WriteLine("Project Finish Date: " + project.StartDate);
}
else
{
    Console.WriteLine("Project Finish Date: " + project.FinishDate);
}

Console.WriteLine("Project Schedule From: " +
(project.ScheduleFromStart ? "Project Start Date" : "Project Finish Date"));

Console.WriteLine("Current Date: " + project.CurrentDate);
Console.WriteLine("Status Date: " + project.StatusDate);
Console.WriteLine("Calendar: " + project.Calendar.Name);
```

#### Explanation
1. **Opening the Project**: The `ProjectReader.Open` method reads the project details from an XML file (`Sample Project.xml`) and returns a `Project` object.
2. **Displaying Start Date**: The `project.StartDate` property retrieves the start date of the project.
3. **Determining Finish Date**: Depending on whether the project is scheduled from the start date (`project.ScheduleFromStart`), the finish date is fetched either from the start date or the `FinishDate` property.
4. **Displaying Scheduling Type**: The condition checks whether the scheduling is based on the start date or the finish date.
5. **Displaying Current and Status Dates**: The `CurrentDate` and `StatusDate` properties provide the current and status dates of the project, respectively.
6. **Displaying Calendar**: The `project.Calendar.Name` retrieves the name of the calendar associated with the project.

#### Output Example
Based on the project data, the output might look something like:
```
Project Start Date: 1/1/2023
Project Finish Date: 3/31/2023
Project Schedule From: Project Start Date
Current Date: 3/15/2023
Status Date: 3/10/2023
Calendar: Standard
```

## API Reference
### Project Properties
- **Start Date**: Retrieves the start date of the project.
  ```csharp
  DateTime StartDate
  ```
- **Finish Date**: Retrieves the finish date of the project.
  ```csharp
  DateTime FinishDate
  ```
- **ScheduleFromStart**: Indicates whether the project is scheduled from the start date or the finish date.
  ```csharp
  bool ScheduleFromStart
  ```
- **Current Date**: Retrieves the current date of the project.
  ```csharp
  DateTime CurrentDate
  ```
- **Status Date**: Retrieves the status date of the project.
  ```csharp
  DateTime StatusDate
  ```
- **Calendar**: Retrieves the calendar associated with the project.
  ```csharp
  Calendar Calendar
  ```

## Code Examples (C#)
The example provided above demonstrates how to read and display project properties using the `Project` class.

## Related Topics
- **ProjectReader.Open(String)**: Explains the method used to open a project from an XML file.
- **Project Properties**: Describes other properties of the `Project` class beyond those shown in the example.

### Parameters (ProjectReader.Open)
- **FileName (String)**:
  + **Type**: String
  + **Description**: The path to the XML file containing the project data.
  + **Default**: None
  + **Required**: Yes

#### Returns
- **Type**: `Project`
- **Description**: A `Project` object representing the project data.

#### Exceptions
- **FileNotFoundException**: Thrown if the specified XML file does not exist.
- **InvalidDataException**: Thrown if the data in the XML file is invalid and cannot be parsed.

## Page-level Navigation/TOC (if applicable)

- [4.1.4 General Project Properties](#general-project-properties)
  - [4.1.4.1 Retrieving Project Properties](#retrieving-project-properties)

## Cross References

- See also: [ProjectReader Methods](#projectreader-methods), [Project Class Properties](#project-class-properties)

<!-- tags: [ProjectReader, Project, ProjectProperties, CSharp, XML, StartDate, FinishDate, ScheduleFromStart, CurrentDate, StatusDate, Calendar, Syncfusion Winforms, ProjectIO, version 11.4.0.26] keywords: [project properties, project start date, project finish date, schedule from start, current date, status date, calendar, project reader, XML file] -->
```