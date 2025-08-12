```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: ProjIO
page_number: 021
page_id: ProjIO#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:14Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Demonstrates accessing and modifying Project properties programmatically.
- Includes examples in both VB and C# for creating and setting Project properties.

## Content

### 4.1.4.2 Setting Project Properties
The `Project` class can be used to set Project properties such as Start Date, Finish Date, Calendar, and more.

The following code snippet shows how to set the `Project` properties:

#### VB

```vb
' Creating an instance of Project
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Displaying Project information
Console.WriteLine("Project Start Date: " & project.StartDate)

If (project.ScheduleFromStart) Then
    Console.WriteLine("Project Finish Date: " & project.StartDate)
Else
    Console.WriteLine("Project Finish Date: " & project.FinishDate)
End If

Console.WriteLine("Project Schedule From: " &
    If(project.ScheduleFromStart = True, "Project Start Date", "Project Finish Date"))

Console.WriteLine("Current Date: " & project.CurrentDate)
Console.WriteLine("Status Date: " & project.StatusDate)
Console.WriteLine("Calendar: " & project.Calendar.Name)
```

#### C#

```csharp
// Creating a new instance of the Project object
Project project = new Project();

// Setting Project information
project.ScheduleFromStart = true;
project.StartDate = new DateTime(2011, 7, 9);
```

## API Reference

### Properties
- `ScheduleFromStart`: Determines whether scheduling is based on the Start Date or Finish Date.
- `StartDate`: Sets the Start Date of the Project.
- `FinishDate`: Sets the Finish Date of the Project if scheduling is not from the Start Date.
- `CurrentDate`: Represents the current date in the Project timeline.
- `StatusDate`: Represents the status date in the Project timeline.
- `Calendar.Name`: Retrieves the name of the calendar associated with the Project.

## Code Examples

The examples above demonstrate how to:
1. Load a project file and access its details.
2. Dynamically set and retrieve key properties of a Project object.

## Cross References
See also:
- ProjectReader documentation for loading project files.
- Additional settings and properties available for the Project class in the Syncfusion Winforms SDK.

<!-- tags: essential projio, project properties, vb examples, c# examples, start date, finish date, syncfusion winforms, version: 11.4.0.26 -->
```