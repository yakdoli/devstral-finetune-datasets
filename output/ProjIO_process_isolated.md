---
title: "ProjIO - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754726482.9674318"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: ProjIO
page_number: 001
page_id: ProjIO#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:58Z
fidelity: lossless
-->
# Essential Studio 2013 Volume 4 - v.11.4.0.26

## Overview
- Introduction to Syncfusion's Essential Studio.
- Focus on the Essential ProjIO component.
- Overview of version 11.4.0.26 and its enhancements.

## Content

### WinForms-specific conventions
- Explanation of how to integrate the ProjIO component into .NET WinForms projects.
- Details on using C# for implementation examples.

### Features
- Detailed exploration of ProjIO's functionalities.
- Instructions on handling file operations and project file management.

## Code Examples

```csharp
// Example usage of ProjIO in a WinForms application
using Syncfusion.ProjIO;

// Create a new project file
Project project = new Project();
project.Save(@"C:\Project.sln");

// Load an existing project file
Project loadedProject = Project.Load(@"C:\Project.sln");
```

<!-- tags: [Syncfusion, Essential Studio, Winforms, ProjIO, version 11.4.0.26] keywords: [Syncfusion ProjectIO, file operations, WinForms integration, C#, project management, essential studio 2013, volume 4] -->
```

---

<!-- 페이지 2 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: ProjIO
page_number: 005
page_id: ProjIO#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:09Z
fidelity: lossless
-->

## Overview

- Essential ProjIO is a library that enables .NET applications to read and write Microsoft Project XML format documents.
- It is a 100% native .NET library that does not use Microsoft Project or COM Interop.
- The library is built from scratch using C# and is designed for compatibility with any .NET environment, including C# and VB.NET.

## Content

### 1.1 Introduction to Essential ProjIO

Essential ProjIO is a 100% native .NET library that enables .NET applications to read and write Microsoft Project XML format documents without utilizing Microsoft Project. It does not use COM Interop and is built from scratch using C#. The ProjIO library can be used in any .NET environment including C# and VB. It is a Non-UI component that is used both on Windows Forms Applications and Web Applications.

### 1.2 Use Case Scenario

Essential ProjIO is used by Managers and Project Leads in companies to manage their projects. It helps them to effectively utilize the resources and increase productivity. It also helps them to complete tasks well before timelines.

### 1.3 Prerequisites and Compatibility

This section covers the requirements that are mandatory for using Essential ProjIO. It also lists operating systems and browsers compatible with the product.

#### Prerequisites:

The prerequisites details are tabulated as follows:

| Development Environments                                                                                   | .NET Framework Versions        |
|----------------------------------------------------------------------------------------------------------|---------------------------------|
| - Visual Studio 2010 (Ultimate, Premium, Professional and Express)                                          | - .NET 4.0                     |
| - Visual Studio 2008 (Team System, Professional, Standard & Express)                                           | - .NET 3.5 SP1                 |
| - Visual Studio 2005 (Professional, Standard & Express)                                                     | - .NET 2.0                     |

#### Compatibility:

The compatibility details are tabulated as follows:

| Compatibility |
|---------------|
| Table 2: Compatibility |

### 1.4 Additional Information

The document also includes information about the compatibility of Essential ProjIO with various operating systems and web browsers, but this data is not visible in the current image content.

## Page-level Navigation/TOC

The content follows a structured format with sections for introduction, use case scenarios, prerequisites, and compatibility. This provides a comprehensive overview of Essential ProjIO, its use cases, and system requirements.

## Others

The document is subject to the copyright of Syncfusion and specifically references the year 2013. It is tailored for developers working with .NET environments, including Windows Forms and Web Applications.

<!-- 
tags: [Essential ProjIO, .NET library, Microsoft Project XML, C#, VB.NET, Windows Forms, Web Applications] 
keywords: [Essential ProjIO, Microsoft Project XML, .NET environment, C#, VB.NET, COM Interop, Visual Studio, .NET Framework] 
-->
```

---

<!-- 페이지 3 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: ProjIO
page_number: 009
page_id: ProjIO#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:27Z
fidelity: lossless
-->

# Essential ProjIO

## Overview

- A demonstration of using Syncfusion's Essential ProjIO library to read and write Microsoft Project xml files.
- Focuses on navigating through the ProjIO samples within the Essential Studio Reporting Windows Forms Dashboard.
- Steps to access and explore features in ProjIO using the Windows Forms interface.

## Content

### Essential Studio Reporting Windows Forms Dashboard

#### Figure 2: Essential Studio Reporting Windows Forms Dashboard

- The dashboard provides an overview of the functionalities available in the Essential Studio for Windows Forms, including support for generating reports and interacting with various document formats.
- The sidebar on the left lists categories like DocIO, Mail Merge, and Import & Export, indicating the variety of tasks that can be performed.
- A central panel displays the features of the selected category, with sample images and links to further details.

#### Exploring ProjIO

1. **Accessing ProjIO Samples**
   
   - **Step 1:** Open the Windows Forms Dashboard.
   - **Step 2:** Click on **ProjIO** from the bottom-left pane to access the ProjIO samples. This action will display the various ProjIO functionalities.

#### Figure 3: Essential Studio Reporting ProjIO Samples

- This figure highlights the ProjIO samples available in the dashboard.
- The sidebar shows options like **Getting Started**, **Resources**, and **Tasks**, which suggest different aspects of ProjIO that users can explore.
- The main section provides a brief introduction to Essential ProjIO, emphasizing its capabilities to read and write Microsoft Project xml files without relying on COM interop.

#### Browsing ProjIO Features

1. **Step 3:** Select any of the samples from the displayed options to navigate through their specific features.

### Key Features of Essential ProjIO

- **Read and Write XML Files:** Essential ProjIO is designed to manipulate Microsoft Project xml files directly, offering full control over project management tasks.
- **Non-Dependency on COM Interop:** It does not require COM interop, providing flexibility to use ProjIO on systems without Microsoft Project installed.
- **Self-Contained Library:** Built entirely in C#, it ensures compatibility and portability across .NET environments.

## API Reference

### Namespaces and Classes

- **Syncfusion.ProjIO**
  - **Syncfusion.ProjIO.ProjectManager**: Handles operations related to managing and manipulating Microsoft Project xml files.
  - **Syncfusion.ProjIO.ResourceManager**: Functions related to managing resources within a project.

### Methods and Properties

- **ProjectManager**
  - **Load(string filePath)**: Loads a Microsoft Project file from the specified path.
  - **Save(string filePath)**: Saves the current state of the project to the specified path.
  - **Resources**: A collection of all resources in the project.

- **ResourceManager**
  - **AddResource(string name, DateTime start, DateTime finish)**: Adds a new resource to the project with specified name and time duration.
  - **RemoveResource(string resourceId)**: Removes a resource from the project based on its unique identifier.

## Code Examples

### Example 1: Basic Project Management

```csharp
using Syncfusion.ProjIO;

// Load a project file
ProjectManager projectManager = new ProjectManager();
projectManager.Load("path_to_project.mpp");

// Access resources
foreach (var resource in projectManager.Resources)
{
    Console.WriteLine($"Resource Name: {resource.Name}");
}

// Save the project
projectManager.Save("updated_project.mpp");
```

### Example 2: Adding a New Resource

```csharp
using Syncfusion.ProjIO;

ProjectManager projectManager = new ProjectManager();
projectManager.Load("path_to_project.mpp");

// Create a new resource manager
ResourceManager resourceManager = projectManager.ResourceManager;

// Add a resource
resourceManager.AddResource("New Resource", new DateTime(2023, 1, 1), new DateTime(2023, 12, 31));

// Save the project
projectManager.Save("updated_project.mpp");
```

## Page-level Navigation/TOC

- **Windows Forms Dashboard Overview**
- **Accessing ProjIO Samples**
- **Navigating ProjIO Features**
- **API and Code Examples**

## Cross References

- See also: [Essential DocIO](#essential-docio), [Essential Mail Merge](#essential-mail-merge), [Essential Import & Export](#essential-import-export)

<!-- tags: [syncfusion, projio, windowsforms, msproject, xml, net-framework] keywords: [ProjIO, Essential Studio, Windows Forms, Microsoft Project, XML, COM Interop, DocIO, Mail Merge] -->
```

---

<!-- 페이지 4 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: ProjIO
page_number: 013
page_id: ProjIO#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:50Z
fidelity: lossless
-->

## Getting Started

### Feature Summary

Important Features of Essential ProjIO are:

- Support to create and edit a new Project xml format documents
- Support to modify existing Project documents (XML format alone)
- Support to change project settings like Start and Finish dates
- Support to change default project settings like Default Standard Rate, Default Overtime Rate, Default Fixed Cost Accrual, Default Task Type and so on
- Support to read and write calendars for tasks and resources
- Support to define Calendar exceptions
- Support to manage task baselines
- Support to create and manage links between tasks
- Support to create and manage resources
- Support to assign and manage resources to tasks
```

---

<!-- 페이지 5 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: ProjIO
page_number: 017
page_id: ProjIO#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:57Z
fidelity: lossless
-->

## Overview
- Lists the properties and methods related to a project in the Syncfusion Winforms environment.
- Describes how to manage and configure various aspects of a project, such as start dates, earned value methods, and synchronization status.
- Provides details on handling project tasks, resources, assignments, and custom fields, among other features.

## Content

### Properties
The following table outlines the properties available for configuring a project:

| Property | Description |
| --- | --- |
| NewTaskStartDate | Gets or sets the default date for new tasks start. |
| DefaultTaskEVMeth | Gets or sets the default earned value method for tasks. |
| ProjectExternallyEdited | True if the project XML was edited. |
| ExtendedCreationDate | Gets or sets date used for calculation and reporting. |
| ActualInSync | True if all actual work has been synchronized with the project. |
| RemoveFileProperties | True to remove all file properties on save. |
| AdminProject | True if the project is an administrative project. |
| BaselineCalendar | Gets or sets the name of the Baseline Calendar. |
| NewTasksAreManual | True if new tasks should be made in Manual mode. |
| UpdateManuallyScheduledTasksWhenEditingLinks | True to update manually scheduled tasks when editing links. |
| KeepTaskOnNearestWorkingTimeWhenMadeAutoScheduled | True if tasks moving from Manual to Auto Scheduled should be moved to the nearest working time. |
| OutlineCodes | Gets or sets the collection of outline code definitions associated with the project. |
| WBSMasks | Gets or sets the table of entries that define the outline code mask. |
| ExtendedAttributes | Gets or sets the collection of extended attribute (custom field) definitions associated with the project. |
| Calendars | Gets or sets the collection of calendars that are associated with the project. |
| Tasks | Gets or sets the collection of tasks that make up the project. |
| Resources | Gets or sets the collection of resources that make up the project. |
| Assignments | Gets or sets the collection of assignments that make up the project. |

### Methods

#### 4.1.1.3 Methods
The following table lists the methods associated with a project.

**Table 6: Project Methods**

| Method | Description |
| --- | --- |

## API Reference (if applicable)
This section would typically include detailed descriptions of each property and method, including parameters, returns, and exceptions. However, the given content does not provide this level of detail. 

## Code Examples (multi-language supported)
No code examples are visible in the provided content.

## Page-level Navigation/TOC (if applicable)
This page appears to be part of a larger document structure, but no explicit TOC is visible.

## Cross References
See also:
- Relevant sections of the Syncfusion Winforms documentation for additional configuration details.

<!-- tags: Syncfusion, Winforms, Project Configuration, Task Management, Resource Assignment, Project Attributes, Version: 11.4.0.26 -->
```

---

<!-- 페이지 6 -->

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

---

<!-- 페이지 7 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: ProjIO
page_number: 025
page_id: ProjIO#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:31Z
fidelity: lossless
-->

## 4.1.6 Writing Project Summary Information

Project class contains properties that can get or set the summary information of a project file in XML format. Using this class, the summary information can be updated and the file can be written back in XML format. The following code shows how this can be done.

```csharp
// C#

// Calling Read method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Setting Project Default information
project.SaveVersion = 14;
project.Author = "Sam Anderson";
project.Manager = "John Henson";
project.Company = "Syncfusion";
project.CreationDate = new DateTime(2011, 10, 8);
project.Subject = "Essential ProjIO";
project.Title = "Sample Project";

// Saving the Project
project.Save("Empty Project.xml");
```

```vb
' VB

' Calling Read method of ProjectReader to get the Project object
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Retrieving Project information
project.SaveVersion = 14
project.Author = "Sam Anderson"
project.Manager = "John Henson"
project.Company = "Syncfusion"
project.CreationDate = New DateTime(2011, 10, 8)
project.Subject = "Essential ProjIO"
```

## API Reference

### Namespace: Syncfusion.ProjIO

#### Class: Project
- Properties:
  - **SaveVersion**: Sets or gets the version number of the project file.
  - **Author**: Sets or gets the author name of the project. Type: string.
  - **Manager**: Sets or gets the manager name of the project. Type: string.
  - **Company**: Sets or gets the company name of the project. Type: string.
  - **CreationDate**: Sets or gets the date the project was created. Type: DateTime.
  - **Subject**: Sets or gets the subject of the project. Type: string.
  - **Title**: Sets or gets the title of the project. Type: string.
- Method:
  - **Save(string filename)**: Saves the project to the specified XML file path.

## Code Examples

The provided C# and VB.NET code examples demonstrate how to:

1. Open an existing project file using the `ProjectReader.Open` method.
2. Update the project properties such as `SaveVersion`, `Author`, `Manager`, `Company`, `CreationDate`, `Subject`, and `Title`.
3. Save the updated project to a new XML file using the `Save` method.

The code snippets provided illustrate the process of reading, modifying, and writing project summary information using the `Project` class from Syncfusion's ProjIO library.

## Cross References

- See also: [4.1 Basic Operations](#4.1-basic-operations)

<!-- tags: [projio, project, xml, summary information, winforms, syncfusion] keywords: [project class, project summary, xml format, project file, version number, author, manager, company, creation date, subject, title, project save] -->
```

---

<!-- 페이지 8 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: ProjIO
page_number: 029
page_id: ProjIO#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:51Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
Console.WriteLine("Weeks starts on: " + project.WeekStartDay);
Console.WriteLine("No. of working days per month: " + 
project.DaysPerMonth);
Console.WriteLine("No.of minutes per day: " + project.MinutesPerDay);
Console.WriteLine("No. of minutes per week: " + 
project.MinutesPerWeek);
```

### VB
```vb
' Opening the project file
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Retrieving Week day properties
Console.WriteLine("Weeks starts on: " + project.WeekStartDay)
Console.WriteLine("No. of working days per month: " + 
project.DaysPerMonth)
Console.WriteLine("No.of minutes per day: " + project.MinutesPerDay)
Console.WriteLine("No. of minutes per week: " + project.MinutesPerWeek)
```

### 4.1.8.2 Setting Week Day Properties
The following code snippet illustrates how to set the Week day properties of a project.

#### C#
```csharp
// Creating a new Project instance
Project project = new Project();

// Setting week day properties
project.WeekStartDay = WeekStartDay.Monday;
project.DaysPerMonth = 24;
project.MinutesPerDay = 480;
project.MinutesPerWeek = 2880;
```

## Page-level Navigation/TOC (if applicable)
- 
```html
<!-- tags: [project file, project properties, week start day, working days, minutes per day, minutes per week, setting properties, syncfusion winforms, projectReader, sample project] keywords: [work day properties, start day, working days per month, minutes per day, minutes per week, project properties, projectReader, sample project.xml] -->
``` 
```

---

<!-- 페이지 9 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: ProjIO
page_number: 033
page_id: ProjIO#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:03Z
fidelity: lossless
-->

## Properties and Descriptions

The following table lists the properties related to task management and their descriptions:

### Properties

| Property               | Description                                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| FixedCost              | Gets or sets the fixed cost of the task.                                                                       |
| FixedCostAccrual       | Gets or sets how the fixed cost is accrued against the task. Values are: 1=Start, 2=Prorated and 3=End.        |
| PercentComplete        | Gets or sets the percentage of the task duration completed.                                                    |
| PercentWorkComplete    | Gets or sets the percentage of the task work completed.                                                       |
| Cost                   | Gets or sets the projected or scheduled cost of the task.                                                     |
| OvertimeCost           | Gets or sets the sum of the actual and remaining overtime cost of the task.                                   |
| OvertimeWork           | Gets or sets the amount of overtime work scheduled for the task.                                              |
| ActualStart            | Gets or sets the actual start date of the task.                                                                |
| ActualFinish           | Gets or sets the actual finish date of the task.                                                              |
| ActualDuration         | Gets or sets the actual duration of the task.                                                                 |
| ActualCost             | Gets or sets the actual cost of the task.                                                                     |
| ActualOvertimeCost     | Gets or sets the actual overtime cost of the task.                                                           |
| ActualWork             | Gets or sets the actual work for the task.                                                                    |
| ActualOvertimeWork     | Gets or sets the actual overtime work for the task.                                                          |
| RegularWork            | Gets or sets the amount of non-overtime work scheduled for the task.                                         |
| RemainingDuration      | Gets or sets the amount of time required to complete the unfinished portion of the task.                    |
| RemainingCost          | Gets or sets the remaining projected cost of completing the task.                                           |
| RemainingWork          | Gets or sets the remaining work scheduled to complete the task.                                              |
| RemainingOvertimeCost  | Gets or sets the remaining overtime cost projected to finish the task.                                      |

## Page-Level Summary

This page enumerates various properties relevant to task management, focusing on cost, work, and time-related attributes. These properties provide the ability to monitor and adjust both projections and actuals for tasks within a project.

<!-- tags: [task management, properties, cost, scheduling, time tracking, overtime, work progress] keywords: [FixedCost, FixedCostAccrual, PercentComplete, PercentWorkComplete, OvertimeCost, OvertimeWork, ActualStart, ActualFinish, ActualDuration, ActualCost, RemainingDuration, RemainingCost, RemainingWork, RemainingOvertimeCost] -->
```

---

<!-- 페이지 10 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: ProjIO
page_number: 037
page_id: ProjIO#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:19Z
fidelity: lossless
-->

## Creating a summary task

### Overview

- The section explains how to create a summary task using the `IsSummary` property of the Task class.
- Demonstrates making a task a summary task with sample code in C# and VB.

### Content

#### 4.2.3 Creating a summary task

To make a task as the summary task, you need to make use of the `IsSummary` property of the Task class.

The following example illustrates making a task as Summary task.

```csharp
Task task1 = new Task("Main Task");
task1.Start = DateTime.Now;
task1.Finish = DateTime.Now;
task1.IsSummary = true;
```

```vb
Dim task1 As Task = New Task("Main Task")
task1.Start = DateTime.Now
task1.Finish = DateTime.Now
task1.IsSummary = True
```

The summary task created using the above code will look like as shown below when viewed in Microsoft Project.

#### Code Examples (C#)

```csharp
Task task1 = new Task("Main Task");
task1.Start = DateTime.Now;
task1.Finish = DateTime.Now;
task1.IsSummary = true;
```

#### Code Examples (VB)

```vb
Dim task1 As Task = New Task("Main Task")
task1.Start = DateTime.Now
task1.Finish = DateTime.Now
task1.IsSummary = True
```

### Summary Task Visualization

The summary task will appear as shown below when viewed in Microsoft Project.

<!-- tags: [Syncfusion Winforms, Task class, IsSummary property, summary task,Microsoft Project] keywords: [Task, IsSummary, summary, DateTime, Project] -->
```

---

<!-- 페이지 11 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: ProjIO
page_number: 041
page_id: ProjIO#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:30Z
fidelity: lossless
-->

# Essential ProjIO

## Figure 10: Project File Created

### 4.3 Resource

The **Resource class** can be used to create resources and add them to Projects. However, creating resources does not automatically assign them to tasks. One must explicitly assign the resources to tasks using the **Assignment class** (4.4). Using the Resources class, one can create, add, and modify resources within projects. It can also be used to retrieve resource information.

#### 4.3.1 Properties, Methods, and Events Tables for Task

##### 4.3.1.1 Constructors

**Table 10: Resource Constructor**

| Name             | Description                                           |
|------------------|-------------------------------------------------------|
| Resource.Resource() | Initializes a new instance of the Resource class. |

##### 4.3.1.2 Properties

**Table 11: Resource Properties**

| Property   | Description                                           |
|------------|-------------------------------------------------------|
| UID        | Gets or sets the unique identifier of the resource    |
| ID         | Gets or sets the position identifier of the resource within the list of resources |
| Name       | Gets or sets the name of the resource                 |
| Type       | Gets or sets the type of resource                     |
| IsNull     | True if the resource is null                          |
| Initials   | Gets or sets the initials of the resource            |
| Phonetics  | Gets or sets the phonetic spelling of the resource   |

## Copyright

© 2013 Syncfusion. All rights reserved.
```

---

<!-- 페이지 12 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: ProjIO
page_number: 045
page_id: ProjIO#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:42Z
fidelity: lossless
-->

## Content

### Properties

Property | Description
--- | ---
BookingType | Gets or sets the booking type of the resource.
ActualWorkProtected | Gets or sets the duration through which actual work is protected.
ActualOvertimeWorkProtected | Gets or sets the duration through which actual overtime work is protected.
ActiveDirectoryGUID | Gets or sets the Active Directory GUID for the resource.
CreationDate | Gets or sets the date the resource was created.
ExtendedAttribute | Gets or sets the value of an extended attribute.
Baseline | Gets or sets the baseline values for the resources.
OutlineCode | Gets or sets the value of an outline code.
IsCostResource | True if the resource is a cost resource.
AssnOwner | Gets or sets the name of the assignment owner.
AssnOwnerGuid | Gets or sets the GUID of the assignment owner.
IsBudget | True if the resource is a budget resource.
AvailabilityPeriods | Gets or sets the collection of periods during which the resource is available.
Rates | Gets or sets the collection of periods and the rates associated with each one.
TimePhasedData | Gets or sets the time phased data.

### 4.3.1.3 Methods

**Table 12: Resource Methods**

Method | Description
--- | ---
Equals | Returns a value indicating whether this instance is equal to a specified object.
GetHashCode | Serves as a hash function for Resource type.
GetType | Gets the type of the current instance.
```

<!-- tags: [syncfusion, projio, properties, methods, resource, bookingtype, active_directory, creationdate, extendsattribute, baseline, outlinecode, iscostresource, assnowner, assnownerguid, isbudget, availabilityperiods, rates, timephaseddata, object, hashfunction, type] keywords: [bookingtype, actualworkprotected, activeovertimeworkprotected, creationdate, extendedattribute, baseline, outlinecode, iscostresource, assnowner, assnownerguid, isbudget, availabilityperiods, rates, timephaseddata, equals, gethashcode, gettype] -->
```

---

<!-- 페이지 13 -->

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

---

<!-- 페이지 14 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: ProjIO
page_number: 053
page_id: ProjIO#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:20Z
fidelity: lossless
-->

# Essential ProjIO

## Overview

- Creating an instance of the Project in C#.
- Adding tasks and calculating task IDs.
- Managing resources and calculating resource IDs.
- Assigning resources to tasks.

## Content

### Project and Task Management

```csharp
// Creating an instance of the Project
Project project = new Project();

// Creating a task
Task task = new Task();
task.Name = "Task1";

// Adding the task to project
project.RootTask.Children.Add(task);

// Calculating Task ID
project.CalculateTaskIDs();
```

### Resource Management

```csharp
// Creating a resource
Resource resource = new Resource();
resource.Name = "Resource1";

// Adding resource to project
project.Resources.Add(resource);

// Calculating Resource ID
project.CalculateResourceIDs();
```

### Assignment Management

```csharp
// Creating an instance of Assignment
Assignment assignment = new Assignment();
assignment.UID = 1;

// Assigning resource to task
assignment.Task = task;
assignment.Resource = resource;
```

## API Reference

### Project Class

- **Method**: `CalculateTaskIDs()`
- **Method**: `CalculateResourceIDs()`

### Task Class

- **Property**: `Name` - Sets the name of the task.

### Resource Class

- **Property**: `Name` - Sets the name of the resource.

### Assignment Class

- **Property**: `UID` - Unique identifier for the assignment.
- **Property**: `Task` - Task to which the resource is assigned.
- **Property**: `Resource` - Resource assigned to the task.

## Code Examples

### C#

```csharp
[C#]

// Creating an instance of the Project
Project project = new Project();

// Creating a task
Task task = new Task();
task.Name = "Task1";

// Adding the task to project
project.RootTask.Children.Add(task);

// Calculating Task ID
project.CalculateTaskIDs();

// Creating a resource
Resource resource = new Resource();
resource.Name = "Resource1";

// Adding resource to project
project.Resources.Add(resource);

// Calculating Resource ID
project.CalculateResourceIDs();

// Creating an instance of Assignment
Assignment assignment = new Assignment();
assignment.UID = 1;

// Assigning resource to task
assignment.Task = task;
assignment.Resource = resource;
```

## Cross References

- See also: [Unclear]

<!-- tags: [project, task, resource, assignment, calculate IDs] keywords: [project management, task management, resource management, assignment management, calculate IDs] -->
```

---

<!-- 페이지 15 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: ProjIO
page_number: 057
page_id: ProjIO#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:38Z
fidelity: lossless
-->

# Essential ProjIO

## 4.5 Calendar

The Calendar class is used to create calendars and add them to the project. Using the Calendar class, one can create calendar exceptions (holidays, different working times and working days), define working days, working times, and so on. It can also add a standard calendar to the project. The Calendar class contains properties that can be used to retrieve information of all calendars present in a project.

### 4.5.1 Properties, Methods, and Events Tables for Task

#### 4.5.1.1 Constructors

**Table 16: Calendar Constructors**

| Name                        | Description                              |
|-----------------------------|------------------------------------------|
| `Calendar.Calendar()`      | Initializes a new instance of Calendar class. |
| `Calendar.Calendar(string calendarName)` | Initializes a new instance of Calendar class with the calendar name. |

#### 4.5.1.2 Properties

**Table 17: Calendar Properties**

| Property            | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `UID`              | Gets or sets the unique identifier of the calendar.                        |
| `Name`             | Gets or sets the name of the calendar.                                     |
| `IsBaseCalendar`   | True if the calendar is a base calendar.                                   |
| `IsBaselineCalendar` | True if the calendar is a baseline calendar.                             |
| `BasecalendarUID`  | Gets or sets the unique identifier of the base calendar on which this calendar depends. Only applicable if the calendar is not a base calendar. |
| `WeekDays`         | Gets or sets the collection of weekdays that defines this calendar.         |
| `Exceptions`       | Gets or sets the collection of exceptions that is associated with the calendar. |
| `WorkWeeks`        | Gets or sets the collection of effective work weeks associated with the calendar. |
```

---

<!-- 페이지 16 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: ProjIO
page_number: 061
page_id: ProjIO#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:51Z
fidelity: lossless
-->

## Essential ProjIO

### Working with Tasks

```vb
' Opening the project file
Dim project As Project = ProjectReader.Open("ProjectWithTasks.xml")

' Retrieving a task by UID
Dim task As Task = project.GetTaskByUID(2)

' Viewing retrieved task information
Console.WriteLine("Task Name: " + task.Name)
Console.WriteLine("Task Start Date: " + task.Start)
Console.WriteLine("Task Finish Date: " + task.Finish)
Console.WriteLine("No. of Sub Tasks: " + task.Children.Count)
```

### 5.5 How to retrieve resources from a project?

The resources present in a project can be retrieved using the `GetResourceByUID` method. The following code snippet illustrates how to retrieve tasks using this method:

```csharp
// Opening the project file
Project project = ProjectReader.Open("ProjectWithResources.xml");

// Retrieving a resource by UID
Resource resource = project.GetResourceByUID(1);

// Viewing retrieved resource information
Console.WriteLine("Resource Name: " + resource.Name);
Console.WriteLine("Type: " + resource.Type);
Console.WriteLine("Work: " + resource.Work);
Console.WriteLine("Remaining Work: " + resource.RemainingWork);
Console.WriteLine("Resource Calendar ID: " + resource.CalendarUID);
```

### API Reference

- **Namespace**: [Project Reading and Writing APIs]
  - **Method**: `ProjectReader.Open(string filePath)`
    - **Parameters**: 
      - `filePath`: The path to the project file to be opened.
    - **Returns**: A `Project` object representing the opened project.
  - **Method**: `Project.GetTaskByUID(int uid)`
    - **Parameters**:
      - `uid`: The unique identifier (UID) of the task to be retrieved.
    - **Returns**: A `Task` object representing the task with the given UID.
  - **Property**: `Task.Name`
    - **Type**: `string`
    - **Description**: The name of the task.
  - **Property**: `Task.Start`
    - **Type**: `DateTime`
    - **Description**: The start date of the task.
  - **Property**: `Task.Finish`
    - **Type**: `DateTime`
    - **Description**: The finish date of the task.
  - **Property**: `Task.Children`
    - **Type**: `ICollection<Task>`
    - **Description**: The sub-tasks of the task.
  - **Method**: `Project.GetResourceByUID(int uid)`
    - **Parameters**:
      - `uid`: The unique identifier (UID) of the resource to be retrieved.
    - **Returns**: A `Resource` object representing the resource with the given UID.
  - **Property**: `Resource.Name`
    - **Type**: `string`
    - **Description**: The name of the resource.
  - **Property**: `Resource.Type`
    - **Type**: `ResourceType`
    - **Description**: The type of the resource.
  - **Property**: `Resource.Work`
    - **Type**: `decimal`
    - **Description**: The total work for the resource.
  - **Property**: `Resource.RemainingWork`
    - **Type**: `decimal`
    - **Description**: The remaining work for the resource.
  - **Property**: `Resource.CalendarUID`
    - **Type**: `int`
    - **Description**: The unique identifier (UID) of the calendar associated with the resource.

<!-- tags: [Syncfusion, WinForms, ProjIO, Projects, Resources, Tasks, APIs, Version 11.4.0.26] keywords: [project file, resource retrieval, task retrieval, UID, work, remaining work, calendar ID] -->
```

---

<!-- 페이지 17 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: ProjIO
page_number: 065
page_id: ProjIO#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:10Z
fidelity: lossless
-->

## Content

### W
- Week Day Properties 28
- Where to Find Samples? 7
- Will it be possible to view the generated project<br> \[.xml file\] using ProjIO? 60
- Writing Project Summary Information 25
- Writing Resources to a Project 46
- Writing Tasks to Projects 39

## API Reference (if applicable)
- (No explicit API references on this page, but related functional descriptions are mentioned, relevant for understanding ProjIO usage.)

## Code Examples (multi-language supported)
- (No explicit code examples on this page, but references to ProjIO and XML files suggest potential use of code in the context of Project Management functionalities.)

## Page-level Navigation/TOC (if applicable)
- This page lists topics and their corresponding page numbers, serving as a local TOC for specific functionalities related to ProjIO in the context of Syncfusion Winforms.

## Cross References
- (No explicit cross-references on this page, but related concepts and features are listed for ProjIO.)

## RAG Annotations
<!-- tags: [ProjIO, Syncfusion Winforms, Control properties, Project file handling, Task management, Resource allocation, Design summary, Version 11.4.0.26] keywords: [Week Day Properties, Sample code, XML file, ProjIO, Project Summary, Resources, Tasks, Writing tasks, .xml file] -->
```

---

<!-- 페이지 18 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: ProjIO
page_number: 002
page_id: ProjIO#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:58Z
fidelity: lossless
-->

# Contents

## 1 Overview
- **1.1 Introduction to Essential ProjIO** ..... 5
- **1.2 Use Case Scenario** ..... 5
- **1.3 Prerequisites and Compatibility** ..... 5
- **1.4 Documentation** ..... 6

## 2 Installation and Deployment
- **2.1 Installation** ..... 7
- **2.2 Where to Find Samples?** ..... 7
  - **2.2.1 Sample Installation Location** ..... 7
  - **2.2.2 Viewing Samples** ..... 7
- **2.3 Deployment Procedures** ..... 12
  - **2.3.1 DLLs** ..... 12

## 3 Getting Started
- **3.1 Feature Summary** ..... 13

## 4 Concepts and Features
- **4.1 Project** ..... 14
  - **4.1.1 Properties, Methods, and Events Tables for Project** ..... 14
    - **4.1.1.1 Constructors** ..... 14
    - **4.1.1.2 Properties** ..... 14
    - **4.1.1.3 Methods** ..... 17
  - **4.1.2 Creating a simple project** ..... 18
  - **4.1.3 Reading a project file** ..... 19
  - **4.1.4 General Project Properties** ..... 20
    - **4.1.4.1 Retrieving Project Properties** ..... 20
    - **4.1.4.2 Setting Project Properties** ..... 21
  - **4.1.5 Default Project Properties** ..... 22
    - **4.1.5.1 Retrieving Default Project Properties** ..... 22
    - **4.1.5.2 Setting Default Project Properties** ..... 23
  - **4.1.6 Writing Project Summary Information** ..... 25
  - **4.1.7 Fiscal Year Properties** ..... 26

<!-- tags: [ProjIO, installation, deployment, concepts, features, project, methods, properties, events, DLLs, samples, overview, documentation] keywords: [Essential ProjIO, Use Case Scenario, Prerequisites, Installation, Samples, Deployment, Project, Properties, Methods, Events, Fiscal Year Properties] -->
```

---

<!-- 페이지 19 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_006.jpeg
document_name: ProjIO
page_number: 006
page_id: ProjIO#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:14Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Lists compatible operating systems and MS Project versions.
- Provides documentation locations and access methods for Essential ProjIO.

## Content

### 1.4 Documentation

Syncfusion provides the following documentation segments to provide all the necessary information pertaining to Essential ProjIO.

#### Table 3: Documentation

| Type of Documentation      | Location                                                                                                                                                                                                                                                                                                      |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Readme                     | Windows Forms-[drive:]\Program Files\Syncfusion\Essential Studio\x.x.x\Infrastructure\Data\Release Notes\readme.htm                                                                                                                              |
| Release Notes             | Windows Forms-[drive:]\Program Files\Syncfusion\Essential Studio\x.x.x\Infrastructure\Data\Release Notes\readme.htm                                                                                                                              |
| User Guide (this document) | **Online**<br>http://help.syncfusion.com/resources (Navigate to the ProjIO User Guide.)<br><img src="edit"> **Note:** Click Download as PDF to access a PDF version.<br>**Installed Documentation**<br>Dashboard -> Documentation -> Installed Documentation. |
| Class Reference           | **Online**<br>http://help.syncfusion.com/resources (Navigate to the Reporting User Guide. Select ProjIO, and then click the Class Reference link found in the upper right section of the page.)<br>**Installed Documentation**<br>Dashboard -> Documentation -> Installed Documentation. |

## API Reference (if applicable)
- No specific API reference is listed in the provided content.

## Code Examples (multi-language supported)
- No code examples are present in the provided content.

## Page-level Navigation/TOC (if applicable)
- None.

## Cross References
- None.

## RAG Annotations
<!-- tags: [produt, essential-projio, documentation, operating-systems, ms-project, user-guide, class-reference, windows-forms] keywords: [essential projio, syncfusion, windows server, windows 7, windows vista, windows xp, windows 2003, ms project 2007, ms project 2010, documentation segments, user guide, class reference] -->
```

---

<!-- 페이지 20 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: ProjIO
page_number: 010
page_id: ProjIO#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:27Z
fidelity: lossless
-->

## Overview

- Instructions to access and run WPF samples within the Essential Studio Reporting dashboard.
- Information on integrating Reporting solutions into WPF applications.
- Features of WPF Reporting, including libraries for manipulating Word, PDF, and Excel formats.
- Explanation of RDLC reporting and transitioning away from proprietary formats.

## Content

### WPF

1. **Accessing WPF Samples**
   - In the dashboard window, click **Run Samples for WPF** under the **Reporting** edition panel.
   - The **WPF Sample Browser window** will be displayed.
   - The screenshot shows the dashboard interface, highlighting the **Reporting** category and the **WPF** option within it.
   - A section describes the **Reporting Edition for WPF**, including:
     - Integration of Reporting solutions into WPF applications.
     - High-performance libraries for manipulating Word, PDF, and Excel formats.
     - Transitioning to **RDLC reporting** for告别 proprietary reporting formats.

   Figure: **Figure 4: Essential Studio Reporting Dashboard**
   - The default WPF sample will be displayed when **Run Samples** is selected.

2. **Selecting WPF Samples**
   - After selecting **Run Samples**, the **WPF** section is highlighted.
   - The default WPF sample is displayed upon selection.

### Screen Layout Details
- **Menu Bar**: Includes options such as **File**, **Edition**, **Tools**, and **Help**.
- **Navigation Panel**:
  - **User Interface**:
    - Contains options like **Reporting**, **ASP.NET**, **ASP.NET MVC**, **Windows Forms**, **WPF**, and **Silverlight**.
  - **Business Intelligence**, **Add-ons**, **Utilities**, and **License Management** are also visible.
- **Main Content Area**:
  - Displays a preview of the **Run Samples** button and a description of the WPF Reporting Edition.
- **Footer**: Contains links to **Sales**, **Contact Support**, **www.syncfusion.com**, **Recheck**, and additional resources like **Online Samples**, **Explore Samples**, **Download Source Code**, **Online Documentation**, **Read Me**, and **What's New**.

## API Reference

### Reporting Features for WPF
- **Integration**:
  - Integrating Reporting solutions into WPF applications with ease.
- **Libraries**:
  - High-performance libraries for manipulating **Word, PDF, and Excel** formats.
- **RDLC Reporting**:
  - Support for **RDLC reporting**, enabling flexibility and reducing reliance on proprietary formats.

## Code Examples

Unclear specific code examples are mentioned in this section. The focus is on the functional behavior and user interface provided by the Essential Studio Reporting platform.

## Page-level Navigation/TOC

- This page focuses on WPF-specific features and integration within the Essential Studio Reporting dashboard.
- References the navigational elements like File, Edition, Tools, and Help to guide users through the process.

## Cross References

See also:
- Essential Studio Documentation
- Syncfusion Online Samples
- WPF Integration Guides

## RAG Annotations

<!-- tags: WPF, Reporting, Essential Studio, RDLC Reporting, Reporting Dashboard, Syncfusion Winforms, WPF Samples keywords: WPF, Reporting, Integration, Libraries, Word, PDF, Excel, RDLC reporting, proprietary formats, user interface, edition panel, dashboard, run samples -->
```

---

<!-- 페이지 21 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_014.jpeg
document_name: ProjIO
page_number: 014
page_id: ProjIO#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:46Z
fidelity: lossless
-->

# 4 Concepts and Features

## 4.1 Project

You can open, modify, and create Project files using the Project Class. The Project class has a structure similar to the MS Project document. The Project class is useful in creating MS Projects in XML format. It can also be used to open or modify the existing Project files in XML format.

### 4.1.1 Properties, Methods, and Events Tables for Project

#### 4.1.1.1 Constructors

Table 4: Project Constructor

| Name             | Description                          |
|------------------|--------------------------------------|
| Project.Project() | Initializes a new instance of the Project class |

#### 4.1.1.2 Properties

Table 5: Project Properties

| Property      | Description                               |
|---------------|-------------------------------------------|
| SaveVersion   | Gets or sets the version of Microsoft Office Project from which the project was saved. |
| UID           | Gets or sets the unique ID of the project. |
| Name          | Gets or sets the name of the project.     |
| Title         | Gets or sets the title of the project.    |
| Subject       | Gets or sets the subject of the project.  |
| Category      | Gets or sets the category of the project. |
| Company       | Gets or sets the company that owns the project. |
| Manager       | Gets or sets the manager of the project.  |
| Author        | Gets or sets the author of the project.   |
| CreationDate  | Gets or sets the date when the project was created. |
| Revision      | Gets or sets the number of times a project has been saved. |
| LastSaved     | Gets or sets the date the project was last saved. |
| ScheduleFromStart | True if the project is scheduled from the start date. |
| StartDate     | Gets or sets the start date of the project. Required if ScheduleFromStart is true. |
```

---

<!-- 페이지 22 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: ProjIO
page_number: 018
page_id: ProjIO#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:59Z
fidelity: lossless
-->

# Essential ProjIO

| Method/Property       | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Save                 | Saves Project instance to disk                                              |
| CalculateResourceIDs | Recalculates UIDs and IDs of resources starting from 0                      |
| CalculateTaskIDs     | Recalculates UIDs and IDs of tasks starting from 0                          |
| Equals               | Returns a value indicating whether this instance is equal to a specified object |
| GetHashCode          | Serves as a hash function for Project type                                     |
| GetType              | Gets the type of the current instance                                          |
| ToString             | Returns a string that represents the current object                           |

## 4.1.2 Creating a simple project

**Project** is the main class of Essential ProjIO. We can only create project files in XML format. The following lines of code create a simple project.

### [C#]

```csharp
// Creating an instance of Project
Project project = new Project();

// Saving the project – Creates an empty project
project.Save("Empty Project.xml");
```

### [VB]

```vb
' Creating an instance of Project
Dim project As Project = New Project()

' Saving the Project – Creates an empty project
project.Save("Empty Project.xml")
```

The XML project file can be viewed in Microsoft Project using the option **File – Open** and then selecting the XML format (*.xml) option from the file types. Select ‘Project Information’ option from the **Projects** menu and the options will look as follows:

<!-- tags: [projio, essential projio, project class, xml project file, creating a simple project, c#, vb, code samples, api reference, microsoft project plugin, syncfusion winforms, version 11.4.0.26] keywords: [project, xml, creating projects, project class, essential projio, code examples, project information, file management, save method, calculate methods, equals method, project type, string representation] -->
```

---

<!-- 페이지 23 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: ProjIO
page_number: 022
page_id: ProjIO#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:12Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
project.CurrentDate = new DateTime(2011, 7, 9);
project.StatusDate = new DateTime(2011, 7, 9);

// Saving the Project
project.Save("ProjectProperties.xml");
```

```vb
' Creating an instance of Project
Dim project As Project = New Project()

' Setting Project information
project.ScheduleFromStart = True
project.StartDate = New DateTime(2011, 7, 9)
project.CurrentDate = New DateTime(2011, 7, 9)
project.StatusDate = New DateTime(2011, 7, 9)

' Saving the Project
project.Save("ProjectProperties.xml")
```

## 4.1.5 Default Project Properties

The Project class is used to get/set Project Default Properties. The default properties of a project can be viewed using the **Tools – Options** menu in MS Project.

### 4.1.5.1 Retrieving Default Project Properties

The following example illustrates how to retrieve default project properties.

```csharp
// Calling Open method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Retrieving Project Default information
Console.WriteLine("Default Start Time: " + project.DefaultStartTime);
```

## 4.1.5 Default Project Properties (Continued)

The `Project` class is used to get/set Project Default Properties. The default properties of a project can be viewed using the **Tools – Options** menu in MS Project.

### Code Example: Retrieving Default Project Properties

```csharp
// Calling Open method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Retrieving Project Default information
Console.WriteLine("Default Start Time: " + project.DefaultStartTime);
```

<!-- tags: [prodjio, project properties, retrieval, default properties, user guide, winforms] keywords: [project class, default start time, retrieving properties, tools options menu, project default properties, sample project, project reader] -->
```

---

<!-- 페이지 24 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_026.jpeg
document_name: ProjIO
page_number: 026
page_id: ProjIO#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:25Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
project.Title = "Sample Project"

' Saving the Project
project.Save("Empty Project.xml")
```

The project summary information added through the above code can be viewed by checking the **Project Information – Advanced Properties** in the **File** menu.

## Empty Project Properties

![Figure: Empty Project Properties](<assets/empty_project_properties.png>)

The **Project** class properties **FYStartDate** and **FiscalYearStart** are used to get or set the Fiscal Year properties. **FYStartDate** defines the fiscal year start month and the **FiscalYearStart** property determines whether the fiscal year numbering has been used in the project.

## 4.1.7 Fiscal Year Properties

The **Project** class properties **FYStartDate** and **FiscalYearStart** are used to get or set the Fiscal Year properties. **FYStartDate** defines the fiscal year start month and the **FiscalYearStart** property determines whether the fiscal year numbering has been used in the project.

## API Reference

### Properties

- **FYStartDate**: Defines the fiscal year start month.
- **FiscalYearStart**: Determines whether the fiscal year numbering has been used in the project.

## Code Examples

```csharp
// Setting Fiscal Year Properties
project.FYStartDate = new DateTime(year, month, day);
project.FiscalYearStart = true;
```

<!-- tags: [Syncfusion, Winforms, ProjIO, Fiscal Year Properties] keywords: [FYStartDate, FiscalYearStart, Project class, fiscal year, start month, numbering] -->
```

---

<!-- 페이지 25 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: ProjIO
page_number: 030
page_id: ProjIO#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:36Z
fidelity: lossless
-->

# Essential ProjIO

```markdown
//Saving the project
project.Save("WeekDayProperties.xml");
```

```vb
[VB]

' Creating a new Project instance
Dim project As Project = New Project()

' Setting Week day properties
project.WeekStartDay = WeekStartDay.Monday
project.DaysPerMonth = 24
project.MinutesPerDay = 480
project.MinutesPerWeek = 2880

' Saving the Project
project.Save("WeekDayProperties.xml")
```

## 4.2 Task

Task class exposes ways to create a task for a Project. Task is useful in creating tasks and adding them to the Project. Using Task class, one can create, add and modify tasks. It can also be used to obtain task information.

### 4.2.1 Properties, Methods, and Events Tables for Task

#### 4.2.1.1 Constructors

| Name                         | Description                                                |
|------------------------------|------------------------------------------------------------|
| Task.Task()                  | Initializes a new instance of the Task class.              |
| Task.Task(string taskName)   | Initializes a new instance of the Task class with the task name. |

```markdown
© 2013 Syncfusion. All rights reserved.
30 |
```

<!-- tags: [product, module, control, ProjIO, Task class, version, 11.4.0.26] keywords: [project, task, WeekDayProperties.xml, Synfusion Winforms, saving project, methods, properties, events, constructors, InitializeTask, TaskName, task properties] -->
```

---

<!-- 페이지 26 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_034.jpeg
document_name: ProjIO
page_number: 034
page_id: ProjIO#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:48Z
fidelity: lossless
-->

## Property and Description Table

The following table lists various properties and their descriptions related to task management in a scheduling or project management context.

### Property Descriptions

| Property                    | Description                                                                                   |
|-----------------------------|---------------------------------------------------------------------------------------------|
| RemainingOvertimeWork      | Gets or sets the remaining overtime work scheduled to finish the task.                       |
| ACWP                        | Gets or sets the actual cost of work performed on the task to-date.                          |
| CV                          | Gets or sets the earned value cost variance.                                                 |
| ConstraintType              | Gets or sets the constraint on the start or finish date of the task.                        |
| CalendarUID                | Gets or sets the task calendar. Refers to a valid UID in the Calendars collection.            |
| ConstraintDate              | Gets or sets the date argument for the task constraint type.                                |
| Deadline                   | Gets or sets the deadline for the task to be completed.                                      |
| LevelAssignments           | True if leveling can adjust assignments.                                                     |
| LevelingCanSplit           | True if leveling can split the task.                                                         |
| LevelingDelay              | Gets or sets the delay caused by leveling the task.                                          |
| LevelingDelayFormat        | Gets or sets the format for expressing the duration of the delay.                           |
| PreLevelStart              | Gets or sets the start date of the task before it was leveled.                              |
| PreLevelFinish             | Gets or sets the finish date of the task before it was leveled.                             |
| Hyperlink                   | Gets or sets the title of the hyperlink associated with the task.                           |
| HyperlinkAddress            | Gets or sets the hyperlink associated with the task.                                       |
| HyperlinkSubAddress        | Gets or sets the document bookmark of the hyperlink associated with the task.                |
| IgnoreResourceCalendar     | True if the task ignores the resource calendar.                                              |
| Notes                      | Gets or sets the text notes associated with the task.                                         |
| HideBar                    | True if the GANTT bar of the task is hidden when displayed in Microsoft Project.              |

## Notes
- The `CalendarUID` refers to a valid UID in the Calendars collection, indicating that the task is associated with a specific calendar.
- The leveling-related properties (`LevelAssignments`, `LevelingCanSplit`, `PreLevelStart`, etc.) are used to manage task scheduling when resource leveling is applied.
- The `Hyperlink` properties provide ways to associate URLs or document bookmarks with tasks for additional references or documentation.

### Related Properties and Methods
- **ACWP**: Actual Cost Work Performed
- **CV**: Cost Variance
- **ConstraintType**: Constraint types include Start No Earlier Than, Start No Later Than, etc.
- **PreLevelStart`, `PreLevelFinish`: These properties store the task's start and finish dates before leveling is applied.

## RAG Annotations

The document provides a detailed listing of properties related to task management and scheduling, particularly useful for understanding various attributes and functionalities within project management software like Microsoft Project.

<!-- tags: [Syncfusion, Winforms, TaskManagement, ProjectManagement] keywords: [task, resource leveling, GANTT bar, cost variance, calendar UID, hyperlink, deadline, overtime work] -->
```

---

<!-- 페이지 27 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_038.jpeg
document_name: ProjIO
page_number: 038
page_id: ProjIO#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:08Z
fidelity: lossless
-->

### 4.2.4 Creating Task links

**Creating Task links**

A task link is created using the default constructor of the `TaskLink` class. It accepts three parameters. The first parameter defines the predecessor `Task`, second parameter defines the successor `Task`, and the third parameter defines the task link type from values specified by the `TaskLinkType` enumeration type.

The following example illustrates how to create links between two tasks.

#### C#

```csharp
// Creating two tasks that are to be linked
Task task1 = new Task("Task1");
Task task2 = new Task("Task2");

// Link task1 and task2
TaskLink link = new TaskLink(task1, task2, TaskLinkType.FinishToStart);
```

#### VB

```vb
' Creating tasks that are to be linked
Dim task1 As Task = New Task("Task1")
Dim task2 As Task = New Task("Task2")

' Creating a link between task1 and task2
Dim link As TaskLink = New TaskLink(task1, task2, TaskLinkType.FinishToStart)
```

<!-- tags: [task, tasklink, tasklinktype, project management, syncfusion winforms, task dependency, finish to start, task links] keywords: [task, tasklink, tasklinktype, project, management, finish, start, dependency, tasklinks, tasklinkclass, enumeration, taskobject, successor, predecessor] -->
```

---

<!-- 페이지 28 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: ProjIO
page_number: 042
page_id: ProjIO#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:19Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Properties and descriptions related to resource management.
- Includes details on NTAccount, MaterialLabel, Code, Group, and WorkGroup.
- Focuses on resource allocation, hyperlink settings, and scheduling dates.

## Content

### Resource Properties Table

| Property              | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| name. For use with Japanese only. |          |
| NTAccount             | Gets or sets the NT account associated with the resource.               |
| MaterialLabel         | Gets or sets the unit of measure for the material resource.             |
| Code                  | Gets or sets the code or other information about the resource.          |
| Group                 | Gets or sets the group to which the resource belongs.                   |
| WorkGroup             | Gets or sets the type of workgroup to which the resource belongs.       |
| EmailAddress          | Gets or sets the email address of the resource.                         |
| Hyperlink             | Gets or sets the title of the hyperlink associated with the resource.   |
| HyperlinkAddress      | Gets or sets the hyperlink associated with the resource.               |
| HyperlinkSubAddress   | Gets or sets the document bookmark of the hyperlink associated with the resource. |
| MaxUnits              | Gets or sets the maximum number of units that the resource is available. |
| PeakUnits             | Gets or sets the largest number of units assigned to the resource at any time. |
| OverAllocated         | True if the resource is over allocated.                                  |
| AvailableFrom         | Gets or sets the first date that the resource is available.             |
| AvailableTo           | Gets or sets the last date the resource is available.                   |
| Start                 | Gets or sets the scheduled start date of the resource.                  |
| Finish                | Gets or sets the scheduled finish date of the resource.                 |
| CanLevel              | True if the resource can be leveled.                                     |

## API Reference

### Namespace: Syncfusion.Windows.Forms.Utilities.ResourceComponents

#### Properties

- **name**: For use with Japanese only.
- **NTAccount**: Gets or sets the NT account associated with the resource.
- **MaterialLabel**: Gets or sets the unit of measure for the material resource.
- **Code**: Gets or sets the code or other information about the resource.
- **Group**: Gets or sets the group to which the resource belongs.
- **WorkGroup**: Gets or sets the type of workgroup to which the resource belongs.
- **EmailAddress**: Gets or sets the email address of the resource.
- **Hyperlink**: Gets or sets the title of the hyperlink associated with the resource.
- **HyperlinkAddress**: Gets or sets the hyperlink associated with the resource.
- **HyperlinkSubAddress**: Gets or sets the document bookmark of the hyperlink associated with the resource.
- **MaxUnits**: Gets or sets the maximum number of units that the resource is available.
- **PeakUnits**: Gets or sets the largest number of units assigned to the resource at any time.
- **OverAllocated**: True if the resource is over allocated.
- **AvailableFrom**: Gets or sets the first date that the resource is available.
- **AvailableTo**: Gets or sets the last date the resource is available.
- **Start**: Gets or sets the scheduled start date of the resource.
- **Finish**: Gets or sets the scheduled finish date of the resource.
- **CanLevel**: True if the resource can be leveled.

## Code Examples

```csharp
// Example: Setting resource properties
using Syncfusion.Windows.Forms.Utilities;

Syncfusion.Windows.Forms.Utilities.ResourceComponent resource = new Syncfusion.Windows.Forms.Utilities.ResourceComponent();
resource.NTAccount = "DOMAIN\\Username";
resource.Code = "Resource123";
resource.Group = "Engineering";
resource.MaxUnits = 10;
resource.Start = DateTime.Now;
resource.Finish = DateTime.Now.AddDays(14);
resource.CanLevel = true;
```

## Page-level Navigation/TOC
- [ ] [Resource Properties Overview](#resource-properties-table)

## Cross References
- See also: Documentation for `ResourceComponent` in the standard API reference.

<!-- tags: [resource, allocation, hyperlink, scheduling, Windows Forms] keywords: [NTAccount, MaterialLabel, Code, Group, WorkGroup, EmailAddress, Hyperlink, HyperlinkAddress, HyperlinkSubAddress, MaxUnits, PeakUnits, OverAllocated, AvailableFrom, AvailableTo, Start, Finish, CanLevel] -->
```

---

<!-- 페이지 29 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: ProjIO
page_number: 046
page_id: ProjIO#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:42Z
fidelity: lossless
-->

## 4.3.2 Adding Resources to a Project

The `Resources` property exposed by the `Project` class represents the list of all the `Resource` objects in a project. This property can be used to add resources.

The following code snippet illustrates adding resources to a project.

### Code Example: Adding Resources (C#)

```csharp
// Creating an instance of the Project
Project project = new Project();

// Creating resource
Resource resource = new Resource();
resource.Name = "Resource1";

// Adding resource to project
project.Resources.Add(resource);
```

### Code Example: Adding Resources (VB)

```vb
' Creating an instance of the Project
Dim project As Project = New Project()

' Creating resource
Dim resource As Resource = New Resource()
resource.Name = "Resource1"

' Adding resource to Project
project.Resources.Add(resource)
```

## 4.3.3 Writing Resources to a Project

The `Resources` property exposed by the `Project` class represents the list of all the `Resource` objects in a project. This property can be used to update resources in a project.

## API Reference

- **Method:** `ToString`
  - **Returns:** A string that represents the current object.

## Page-level Navigation/TOC (if applicable)

- 4.3.2 Adding Resources to a Project
- 4.3.3 Writing Resources to a Project

## Cross References

See also: Further details on managing resources in projects can be found in the synchronization with bucket and Advanced properties and attributes sections.

<!-- tags: [ProjIO, Project, Resources, C#, VB] keywords: [Adding, Writing, Resources, Project] -->
```

---

<!-- 페이지 30 -->

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

---

<!-- 페이지 31 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_054.jpeg
document_name: ProjIO
page_number: 054
page_id: ProjIO#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:13Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
project.Resources.Add(resource);
```

## API Reference

### Parameters
- `project`: The project object to which the resource is being added.
- `resource`: The resource object being added to the project's resources collection.

## Code Examples

### C# Example
```csharp
// Example usage of adding a resource to the project
project.Resources.Add(new Resource
{
    Name = "exampleResource",
    Path = @"C:\Path\To\Resource.txt"
});
```

## Cross References

See also:
- Handling Resources in Projects
- Project Resource Management

<!-- tags: [projio, resource management, project resources, syncfusion winforms] keywords: [project, resources, add, resource, management, Syncfusion, WinForms, version 11.4.0.26] -->
```

---

<!-- 페이지 32 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: ProjIO
page_number: 058
page_id: ProjIO#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:21Z
fidelity: lossless
-->

## Essential ProjIO

### 4.5.1.3 Methods

#### Table 18: Calendar Methods

| Method                           | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| Equals                           | Returns a value indicating whether this instance is equal to a specified object |
| GetHashCode                      | Serves as a hash function for Calendar type                                 |
| GetType                          | Gets the type of the current instance                                      |
| ToString                         | Returns a string that represents the current object                         |
| Calendar.StandardCalendar()      | Creates a standard calendar                                                |
| Calendar.StandardCalendar(string calendarName) | Creates a standard calendar                                               |

#### 4.5.2 Creating a Standard Calendar

The static method `StandardCalendar` is used to create a standard calendar and add it to the project.

This method contains two overloads namely:
- `StandardCalendar()` – Creates a standard calendar
- `StandardCalendar(string calendarName)` – Creates a standard calendar by passing the calendar name

The following code snippet shows how to make use of this method:

#### Code Examples

##### C#

```csharp
// Creating a standard calendar
Calendar calendar = Calendar.StandardCalendar();

// Creating a standard calendar by passing the calendar name
Calendar calendar1 = Calendar.StandardCalendar("Standard");
```

##### VB

```vb
' Creating a standard calendar
Dim calendar As Calendar = Calendar.StandardCalendar()
```

## Page-level Navigation/TOC (if applicable)
- 4.5.1.3 Methods
- 4.5.2 Creating a Standard Calendar

### RAG Annotations
<!-- tags: [Syncfusion, Winforms, Calendar, StandardCalendar, Creating Calendars] keywords: [calendar, StandardCalendar, methods, static method] -->
```

---

<!-- 페이지 33 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: ProjIO
page_number: 062
page_id: ProjIO#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:33Z
fidelity: lossless
-->

# Essential ProjIO

[VB]

```vb
' Opening the project file
Dim project As Project = ProjectReader.Open("ProjectWithResources.xml")

' Retrieving a resource by UID
Dim resource As Resource = project.GetResourceByUID(1)

' Viewing retrieved resource information
Console.WriteLine("Resource Name: " + resource.Name)
Console.WriteLine("Type: " + resource.Type)
Console.WriteLine("Work: " + resource.Work)
Console.WriteLine("Remaining Work: " + resource.RemainingWork)
Console.WriteLine("Resource Calendar ID: " + resource.CalendarUID)
```

## How to retrieve resource assignments from a project?

The resource assignments present in a project can be retrieved using the `GetAssignmentByUID` method.

The following code snippet shows how to use this method:

[C#]

```csharp
// Opening the project file
Project project = ProjectReader.Open("SampleProject.xml");

// Retrieving an assignment by UID
Assignment assignment = project.GetAssignmentByUID(1);

// Viewing retrieved assignment information
Console.WriteLine("Resource: " + assignment.Resource.Name);
Console.WriteLine("Assigned to: " + assignment.Task.Name);
Console.WriteLine("Booking Type: " + assignment.BookingType);
Console.WriteLine("Cost: $" + assignment.Cost);
```
```

---

<!-- 페이지 34 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: ProjIO
page_number: 003
page_id: ProjIO#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:58Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Provides details on fiscal year properties, week day properties, task handling, resource management, assignment addition, and calendar creation.
- Focuses on properties, methods, and events for tasks, resources, and assignments.
- Includes steps to add tasks, create summary tasks, and manage task links.
- Explains resource addition, assignments, and standard calendar creation.

## Content

###财政年属性
- **4.1.7.1 Retrieving Fiscal Year Properties** ..... 27
- **4.1.7.2 Setting Fiscal Year Properties** ..... 27

###周日属性
- **4.1.8 Week Day Properties** ..... 28
  - **4.1.8.1 Retrieving Week Day Properties** ..... 28
  - **4.1.8.2 Setting Week Day Properties** ..... 29

###任务
- **4.2 Task** ..... 30
  - **4.2.1 Properties, Methods, and Events Tables for Task** ..... 30
    - **4.2.1.1 Constructors** ..... 30
    - **4.2.1.2 Properties** ..... 31
    - **4.2.1.3 Methods** ..... 36
  - **4.2.2 Adding Tasks to a Project** ..... 36
  - **4.2.3 Creating a summary task** ..... 37
  - **4.2.4 Creating Task links** ..... 38
  - **4.2.5 Writing Tasks to Projects** ..... 39

###资源
- **4.3 Resource** ..... 41
  - **4.3.1 Properties, Methods, and Events Tables for Task** ..... 41
    - **4.3.1.1 Constructors** ..... 41
    - **4.3.1.2 Properties** ..... 41
    - **4.3.1.3 Methods** ..... 45
  - **4.3.2 Adding Resources to a Project** ..... 46
  - **4.3.3 Writing Resources to a Project** ..... 46

###分配
- **4.4 Assignment** ..... 48
  - **4.4.1 Properties, Methods, and Events Tables for Task** ..... 48
    - **4.4.1.1 Constructors** ..... 48
    - **4.4.1.2 Properties** ..... 48
    - **4.4.1.3 Methods** ..... 52
  - **4.4.2 Adding Assignments to a Project** ..... 52

###日历
- **4.5 Calendar** ..... 57
  - **4.5.1 Properties, Methods, and Events Tables for Task** ..... 57
    - **4.5.1.1 Constructors** ..... 57
    - **4.5.1.2 Properties** ..... 57
    - **4.5.1.3 Methods** ..... 58
  - **4.5.2 Creating a Standard Calendar** ..... 58

###如何操作
- **5 How To** ..... 60

## Conclusion
- Covers all steps and methods required to manipulate fiscal years, week days, tasks, resources, assignments, and calendars.
- Offers detailed tables and instructions for handling various aspects of project elements in Syncfusion Winforms.

<!-- tags: [winforms, projio, fiscal years, week day properties, task management, resource allocation, assignment, calendar creation, api reference] keywords: [retrieving properties, setting properties, constructors, properties, methods, adding tasks, creating summary tasks, task links, writing tasks, adding resources, assignments, creating calendars, standard calendar] -->
```

---

<!-- 페이지 35 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: ProjIO
page_number: 007
page_id: ProjIO#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:20Z
fidelity: lossless
-->

# Essential ProjIO

## 2 Installation and Deployment

### 2.1 Installation

For step-by-step installation procedure for the installation of Essential Studio, refer to the Installation topic under Installation and Deployment in the Common UG.

### 2.2 Where to Find Samples?

This section covers the location of the installed samples and describes the procedure to run the samples through the sample browser and online. It also lists the location of utilities, assemblies, and source code.

#### 2.2.1 Sample Installation Location

Sample install locations for different platforms are listed below:

- **Windows Forms** – The Windows Forms samples are installed in the following location:

  ```
  ...\MyDocuments\Syncfusion\EssentialStudio\VersionNumber\Windows\ProjIO.Windows\Samples\2.0
  ```

- **WPF** – The WPF samples are installed in the following location:

  ```
  ...\MyDocuments\Syncfusion\EssentialStudio\VersionNumber\WPF\ProjIO.WPF\Samples\3.5
  ```

#### 2.2.2 Viewing Samples

The samples can be viewed in any of the following three ways:

- **Run Samples** – Click to view the locally installed samples.
- **Online Samples** – Click to view online samples.
- **Explore Samples** – Explore samples on disk.

To view the samples:

1. Click Start → All Programs → Syncfusion → Essential Studio <x.x.x.x> → Dashboard.
   The UI samples are displayed by default.
2. Select **Reporting**.

<!-- tags: [Essential Studio, Installation, Samples, WinForms, WPF, Reporting, Version11.4.0.26] keywords: [installation, samples, project location, viewing samples, reporting] -->
```

---

<!-- 페이지 36 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: ProjIO
page_number: 011
page_id: ProjIO#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:32Z
fidelity: lossless
-->

## Overview

- This section outlines the usage and features of the Essential Studio Reporting WPF and ProjIO components, showcasing their capabilities through sample screenshots and explanations.

### Essential Studio Reporting

#### WPF

##### Documentation

Essential DocIO is a .NET library that can read and write Microsoft Word files. It features a full-fledged object model similar to the Microsoft Office COM libraries. It does not use COM interop and is built from scratch in C#. It can even be used on systems that do not have Microsoft Word installed.

##### Featured Samples
- **Sales Invoice**: A sample invoice document demonstrating table and content styling.
- **Table Insertion**: Showing how to insert and manipulate tables within a document.
- **Employee Report**: An example of generating employee reports.
- **Forms**: Displaying form fields that can be interacted with.
- **Clone and Merge**: Illustrating the cloning and merging of documents.
- **Update Fields**: Demonstrating the ability to update fields dynamically.

#### Figure: Essential Studio Reporting WPF Dashboard

![Figure 5: Essential Studio Reporting WPF Dashboard](image_url)

##### Navigation
- **Left Pane**: Contains navigation links for various features such as Product Showcase, Getting Started, Insert Content, Editing, Mail Merge, View, Security, and Import and Export.
- **Top Bar**: Features a search function to quickly find content.

##### Footer
- **Copyright Notice**: Copyright © 2001-2012 Syncfusion Inc.
- **Links**: Quick access links to forum, documentation, support, and sales.

### ProjIO

#### WPF

##### Documentation

Essential ProjIO is a .NET class library that can read and write Microsoft Project xml files. It does not use COM interop and is built from scratch in C#.

##### Featured Samples
- **Inserting Resources**: A visual representation of inserting resources into a Microsoft Project file.

#### Figure: Essential Studio Reporting ProjIO Samples

![Figure 6: Essential Studio Reporting ProjIO Samples](image_url)

##### Navigation
- **Left Pane**: Contains links for Getting Started, Resources, and Tasks.
- **Top Bar**: Same as in the WPF Dashboard.

#### Footer
- **Copyright Notice**: Copyright © 2001-2012 Syncfusion Inc.
- **Links**: Similar access links to forum, documentation, support, and sales.

## Content

1. **Overview**
   - Explains the core functionalities of Essential DocIO and ProjIO.
   - Both libraries operate without the need for COM interop and are built using C#.

2. **Essential DocIO**
   - **Primary Use Case**: The library is designed for working with Microsoft Word files.
   - **Detailed Features**:
     - Object model similar to Microsoft Office COM libraries.
     - Can operate on systems without Microsoft Word installed.

3. **ProjIO**
   - **Primary Use Case**: The library is designed for working with Microsoft Project xml files.
   - **Detailed Features**:
     - Built from scratch in C#.
     - Focuses on reading and writing Microsoft Project xml files without COM interop.

### Instructions

5. **Click ProjIO form the bottom-left pane and browse through the features.**

## Code Examples

- **Snippet for Inserting Resources using ProjIO**:
```csharp
using Syncfusion.DocIO.Process;

// Code example for inserting resources into a project file
```

## API Reference

### Essential DocIO

- **Namespace**: Syncfusion.DocIO
- **Classes**: Document, Section, Table, etc.

### ProjIO

- **Namespace**: Syncfusion.ProjIO
- **Classes**: ProjectDocument, Task, Resource, etc.
- **Methods**: InsertResource(), UpdateTask(), ExportToXml(), etc.

## RAG Annotations

<!-- tags: [DocIO, ProjIO, Winforms, Reporting, WPF, Syncfusion, EssentialStudio, workspace, microsoft, project] keywords: [DocIO features, ProjIO features, WPF, C#, COM interop, Object model, XML files, forums, documentation, support, sales] -->
```

---

<!-- 페이지 37 -->

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

---

<!-- 페이지 38 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: ProjIO
page_number: 019
page_id: ProjIO#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:31Z
fidelity: lossless
-->

## Content

### 4.1.3 Reading a project file

The **Read** method of the **ProjectReader** class is used to read the project files. The **Read** method has two overloads, namely:

- **Read(string filename)** — opens the file specified by the given file name.
- **Read(Stream stream)** — opens the file specified by the **Stream**.

The **Read** method returns a **Project** object, which can then be used to retrieve or manipulate project information.

The following code illustrates the use of the **Read** method:

```csharp
// Assigning the Project object returned by the Read method
Project P = ProjectReader.Open("SimpleProject.xml");
```

## API Reference

### ProjectReader Class Methods

#### Open(string filename)

- **Parameters**:
  - **filename**: A string representing the path to the project file to be opened.
  
- **Returns**: A **Project** object that represents the loaded project.

#### Open(Stream stream)

- **Parameters**:
  - **stream**: A **Stream** object representing the input stream for the project file.
  
- **Returns**: A **Project** object that represents the loaded project.

## Code Examples

### Reading a Project using a File Path

```csharp
using Syncfusion.Windows.Formsプロジェクト管理;

// Specify the file path to the project
string filePath = "C:\\Projects\\SimpleProject.xml";

// Open the project file using the ProjectReader
Project project = ProjectReader.Open(filePath);

// Now, 'project' contains the loaded project information
```

### Reading a Project using a Stream

```csharp
using Syncfusion.Windows.Formsプロジェクト管理;
using System.IO;

// Specify the file path to the project
string filePath = "C:\\Projects\\SimpleProject.xml";

// Create a stream from the file
FileStream fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read);

// Open the project file using the ProjectReader with the stream
Project project = ProjectReader.Open(fileStream);

// Now, 'project' contains the loaded project information
fileStream.Close();
```

## RAG Annotations

<!-- tags: [ProjIO, project management, project reader, reading files, Syncfusion Winforms] keywords: [ProjectReader, Read method, Project object, filename parameter, Stream parameter] -->
```

---

<!-- 페이지 39 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_023.jpeg
document_name: ProjIO
page_number: 023
page_id: ProjIO#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:48Z
fidelity: lossless
-->

## Essential ProjIO

### Retrieving Project Information

```csharp
Console.WriteLine("Default Finish Time: " + project.DefaultFinishTime);
Console.WriteLine("Default Standard Rate: " +
project.DefaultStandardRate);
Console.WriteLine("Default Overtime Rate: " +
project.DefaultOvertimeRate);
Console.WriteLine("Default Task EV Method: " +
project.DefaultTaskEVMethod);
Console.WriteLine("Default Cost Accrual: " +
project.DefaultFixedCostAccrual);
```

### [VB]

```vb
' Creating an instance of Project
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Retrieving Project information
Console.WriteLine("Default Start Time: " & project.DefaultStartTime.ToString())
Console.WriteLine("Default Finish Time: " & project.DefaultFinishTime.ToString())
Console.WriteLine("Default Standard Rate: " & project.DefaultStandardRate)
Console.WriteLine("Default Overtime Rate: " & project.DefaultOvertimeRate)
Console.WriteLine("Default Task EV Method: " & project.DefaultTaskEVMethod)
Console.WriteLine("Default Cost Accrual: " & project.DefaultFixedCostAccrual)
```

### 4.1.5.2 Setting Default Project Properties

The following example shows how to set the default project properties.

---

<!-- tags: [projio, project, information, retrieval, vb, setting, properties] keywords: [project, default finish time, standard rate, overtime rate, task ev method, cost accrual, projectreader, sample project] -->
```

---

<!-- 페이지 40 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: ProjIO
page_number: 027
page_id: ProjIO#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:58Z
fidelity: lossless
-->

# Essential ProjIO

## Retrieving Fiscal Year Properties

The following code snippets retrieve Fiscal year properties from a project:

### C#
```csharp
// Calling Open method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Retrieving Fiscal Year information
Console.WriteLine("Fiscal Year Start Month: " + project.FYStartDate);

Console.WriteLine(project.FiscalYearStart ? "Fiscal Year Numbering is used in the Project" : "Fiscal Year Numbering is not used in the Project");
```

### VB
```vbnet
' Calling Read method of ProjectReader to get the Project object
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Retrieving Fiscal Year information
Console.WriteLine("Fiscal Year Start Month: " + project.FYStartDate)

Console.WriteLine(If(project.FiscalYearStart, "Fiscal Year Numbering is used in the Project", "Fiscal Year Numbering is not used in the Project"))
```

## Setting Fiscal Year Properties

The following code sets the Fiscal year properties for a project.

### C#
```csharp
// Creating a new instance of Project object
Project project = new Syncfusion.ProjIO.Project();
```

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

<!-- tags: [ProjIO, Fiscal Year, Project Properties, Retrieving, Setting, C#, VB, ProjectReader, Syncfusion, Essentials] keywords: [FiscalYearStart, FYStartDate, ProjectReader, ProjectReader.Open, If, Console.WriteLine, Syncfusion.ProjIO.Project] -->
```

---

<!-- 페이지 41 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: ProjIO
page_number: 031
page_id: ProjIO#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:12Z
fidelity: lossless
-->

## 4.2.1.2 Properties

### Table 8: Task Properties

| Property        | Description                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------|
| UID             | Gets or sets the unique ID of the task.                                                          |
| ID              | Gets or sets the position identifier of the task within the list of tasks.                     |
| Name            | Gets or sets the name of the task.                                                               |
| Type            | Gets or sets the type of task.                                                                  |
| IsNull          | True if the task is null.                                                                       |
| CreateDate      | Gets or sets the date the task was created.                                                    |
| Contact         | Gets or sets the contact person for the task.                                                  |
| WBS             | Gets or sets the work breakdown structure code of the task.                                    |
| WBSLevel        | Gets or sets the rightmost WBS level of the task.                                              |
| OutlineNumber   | Gets or sets the outline number of the task.                                                   |
| OutlineLevel    | Gets or sets the outline level of the task.                                                    |
| Priority        | Gets or sets the priority of the task from 0 to 1000.                                          |
| Start           | Gets or sets the scheduled start date of the task.                                             |
| Finish          | Gets or sets the scheduled finish date of the task.                                            |
| Duration        | Gets or sets the planned duration of the task.                                                 |
| DurationFormat  | Gets or sets the format for expressing the Duration of the Task.                               |
| Work            | Gets or sets the amount of scheduled work for the task.                                        |
| Stop            | Gets or sets the date that the task was stopped.                                               |
| Resume          | Gets or sets the date that the task resumed.                                                   |
| ResumeValid     | True if the task can be resumed.                                                                |
| EffortDriven    | True if the task is effort-driven.                                                              |
| Recurring       | True if the task is a recurring task.                                                           |

<!-- tags: [task properties, unique ID, position identifier, name, task type, task creation date, contact person, WBS, outline number, outline level, priority, start date, finish date, duration, duration format, scheduled work, stop date, resume date, resume validity, effort-driven tasks, recurring tasks] keywords: [task properties, UID, ID, task name, task type, creation date, work breakdown structure, WBS, outline number, outline level, priority, start, finish, duration, duration format, scheduled work, stop, resume, resume valid, effort-driven, recurring] -->
```

---

<!-- 페이지 42 -->

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

---

<!-- 페이지 43 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: ProjIO
page_number: 039
page_id: ProjIO#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:48Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Describes the process of writing tasks to projects using the `RootTask` property of the `Project` class.
- Demonstrates how to update tasks using the `Children` property.
- Provides a code snippet to illustrate adding and linking tasks to a project.

## Content

### Writing Tasks to Projects

The `RootTask` property of the `Project` class contains the `Children` property, which returns the list of `Task` objects. The `Children` property is used to update the tasks. The following code snippet demonstrates writing tasks to a project.

#### Code Example

```csharp
[C#]

// Creating an instance of the Project
Project P = new Project();

// Creating two tasks to be added to the project
Task task1 = new Task("Task1");
task1.Duration = new TimeSpan(8, 0, 0);
Task task2 = new Task("Task2");
task2.Duration = new TimeSpan(8, 0, 0);

// Adding the tasks to the RootTask of project
P.RootTask.Children.Add(task1);
P.RootTask.Children.Add(task2);

// Calculating Task IDs and UIDs
P.CalculateTaskIDs();

// Link "Task1" and "Task2"
TaskLink link = new TaskLink(task1, task2, TaskLinkType.FinishToStart);

// Saving the project
P.Save("ProjectWithTasks.xml");
```

### Explanation

1. **Creating the Project Instance**:
   - An instance of the `Project` class is created using `new Project()`.

2. **Creating Tasks**:
   - Two task objects (`task1` and `task2`) are created with specified names and durations using `new Task("TaskName")` and `new TimeSpan(8, 0, 0)`.

3. **Adding Tasks to the Project**:
   - The tasks are added to the `RootTask.Children` collection of the project using the `Add` method.

4. **Calculating Task IDs and UIDs**:
   - The `CalculateTaskIDs` method is called to assign unique IDs and UIDs to the tasks.

5. **Linking Tasks**:
   - A `TaskLink` object is created to link `task1` and `task2` using the `FinishToStart` link type.

6. **Saving the Project**:
   - The project is saved to an XML file named `"ProjectWithTasks.xml"` using the `Save` method.

## RAG Annotations
<!-- tags: [syncfusion-winforms, projio, task-management, project-class, roottask, children-property, tasklink, timestamp-2025-08-09T07:58:48Z] keywords: [project, task, children, roottask, tasklink, finishtostart, calculateTaskIDs, save, csharp] -->
```

---

<!-- 페이지 44 -->

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

---

<!-- 페이지 45 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: ProjIO
page_number: 047
page_id: ProjIO#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:27Z
fidelity: lossless
-->

## Essential ProjIO

### Overview

- Demonstrates how to write resources to a project.
- Explains steps using C# and VB code snippets.

### Content

The following code shows how to write resources to a project.

#### C# Code Example

```csharp
// Creating an instance of the Project
Project project = new Project();

// Creating resource
Resource resource = new Resource();
resource.Name = "Resource1";

// Adding resource to project
project.Resources.Add(resource);

// Calculating Resource IDs and UIDs
project.CalculateResourceIDs();

// Saving the project
project.Save("Project With Resources.xml");
```

#### VB Code Example

```vb
' Creating an instance of the Project
Dim project As Project = New Project()

' Creating resource
Dim resource As Resource = New Resource()
resource.Name = "Resource1"

' Adding resource to Project
project.Resources.Add(resource)

' Calculating Resource IDs and UIDs
project.CalculateResourceIDs()
```

### API Reference

#### Methods Used
- `Project()`  
  - **Description**: Creates a new instance of the Project class.
- `Resource()`  
  - **Description**: Creates a new instance of the Resource class.
- `Resource.Name`  
  - **Description**: Sets the name of the resource.
- `Project.Resources.Add(resource)`  
  - **Description**: Adds the specified resource to the project's resource collection.
- `Project.CalculateResourceIDs()`  
  - **Description**: Calculates and assigns IDs and UIDs to the resources in the project.
- `Project.Save(filename)`  
  - **Description**: Saves the project to the specified file.

### Code Examples

#### C# Example
```csharp
Project project = new Project();
Resource resource = new Resource();
resource.Name = "Resource1";
project.Resources.Add(resource);
project.CalculateResourceIDs();
project.Save("Project With Resources.xml");
```

#### VB Example
```vb
Dim project As Project = New Project()
Dim resource As Resource = New Resource()
resource.Name = "Resource1"
project.Resources.Add(resource)
project.CalculateResourceIDs()
```

### Licensing
© 2013 Syncfusion. All rights reserved.

<!-- tags: [Essential ProjIO, resource management, project class, saving project, IDs, UIDs, C#, VB, Syncfusion Winforms, version 11.4.0.26] keywords: [ProjIO, resource, project, calculateResourceIDs, save, C#, VB, Syncfusion, Winforms] -->
```

---

<!-- 페이지 46 -->

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

---

<!-- 페이지 47 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: ProjIO
page_number: 055
page_id: ProjIO#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:04Z
fidelity: lossless
-->

## ProjIO

### VB Code Example

```vb
' Creating an instance of Project
Dim project As Project = New Project()

' Creating an instance of Task
Dim task As Task = New Task()
task.Name = "Task1"

' Adding the task to project
project.RootTask.Children.Add(task)

' Calculating Task ID
project.CalculateTaskIDs()

' Creating an instance of Resource
Dim resource As Resource = New Resource()
resource.Name = "Resource1"

' Adding resource to project
project.Resources.Add(resource)

' Calculating Resource ID
project.CalculateResourceIDs()

' Creating an instance of Assignment
Dim assignment As Assignment = New Assignment()
assignment.UID = 1

' Assigning tasks and resource to assignment
assignment.Task = task
assignment.Resource = resource

' Adding an assignment to a project
```

### Summary

- This code example demonstrates how to create a project instance and manage tasks, resources, and assignments within it. The steps include:
  - Creating a `Project` object.
  - Adding a `Task` to the project.
  - Calculating Task IDs.
  - Creating a `Resource` and adding it to the project.
  - Calculating Resource IDs.
  - Creating an `Assignment` with a specified UID, linking it to a specific task and resource, and adding it to the project.

### Code Explanation

- **Project Instance**: The `Project` object is the core container for tasks, resources, and assignments.
- **Task Management**: A `Task` object is created, named "Task1," and added to the project's root task children. Task IDs are then recalculated using `CalculateTaskIDs`.
- **Resource Management**: A `Resource` object is created, named "Resource1," and added to the project's resource collection. Resource IDs are recalculated using `CalculateResourceIDs`.
- **Assignment Management**: An `Assignment` object is created with a UID of 1, and it is linked to the previously created `Task` and `Resource`. The assignment is then added to the project.

### Usage Scenario

This code snippet can be used in applications that require project management functionalities, such as scheduling, resource allocation, and task assignment. It demonstrates how to programmatically manipulate project components using the Syncfusion WinForms library.

## API Reference

### Namespace: Syncfusion.ProjectManagement

#### Class: Project
- **Method**: `RootTask.Children.Add(Task)`
  - Adds a task to the root task's children.
- **Method**: `CalculateTaskIDs()`
  - Recalculates the IDs of all tasks within the project.
- **Method**: `Resources.Add(Resource)`
  - Adds a resource to the project's resource collection.
- **Method**: `CalculateResourceIDs()`
  - Recalculates the IDs of all resources within the project.
- **Property**: `Resources`
  - Collection of resources associated with the project.
- **Property**: `RootTask`
  - The root task of the project.

#### Class: Task
- **Property**: `Name`
  - Gets or sets the name of the task.

#### Class: Resource
- **Property**: `Name`
  - Gets or sets the name of the resource.

#### Class: Assignment
- **Property**: `UID`
  - Gets or sets the unique identifier of the assignment.
- **Property**: `Task`
  - Gets or sets the task associated with the assignment.
- **Property**: `Resource`
  - Gets or sets the resource associated with the assignment.

## Cross References

See also:
- "Adding Tasks to a Project"
- "Managing Resources in Project"
- "Assigning Resources to Tasks"

<!-- tags: [Syncfusion, WinForms, Project Management, Tasks, Resources, Assignments, Version 11.4.0.26] keywords: [project, task, resource, assignment, calculate IDs, root task, resource collection, task management] -->
```


---

<!-- 페이지 48 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: ProjIO
page_number: 059
page_id: ProjIO#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:24Z
fidelity: lossless
-->

## Creating a Standard Calendar

To create a standard calendar, you can use the `Calendar.StandardCalendar` method by passing the calendar name. Below is an example of how to create a standard calendar:

```vb
Dim calendar1 As Calendar = Calendar.StandardCalendar("Standard")
```

### Overview

- Creates a standard calendar using the `Calendar.StandardCalendar` method.
- The `Standard` calendar name is passed as a parameter to the method.

### Description

The `Calendar.StandardCalendar` method is used to create a calendar instance based on the specified calendar name. In this example, the "Standard" calendar is being created. This is useful in applications where you need to work with different calendar systems, such as the Gregorian calendar, Islamic calendar, or other custom calendar systems.

### Code Example

```vb
' Creating a standard calendar by passing the calendar name
Dim calendar1 As Calendar = Calendar.StandardCalendar("Standard")
```

### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Method**: `Calendar.StandardCalendar(name As String)`
  - **Parameters**:
    - `name` (String): The name of the calendar to create.
  - **Returns**: A `Calendar` object representing the specified calendar.

### Notes

- Ensure that the calendar system supports the specified calendar name to avoid errors.
- The "Standard" calendar typically refers to the Gregorian calendar.

### Cross References

- For more information on different calendar systems and their usage, refer to the [Syncfusion documentation on calendars](https://www.syncfusion.com/documentation/windows-forms/calendars).

<!-- tags: [syncfusion, winforms, calendar, standardcalendar, api, 11.4.0.26] keywords: [calendar, standard, calendar creation, standardcalendar method, winforms controls] -->
```

---

<!-- 페이지 49 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: ProjIO
page_number: 063
page_id: ProjIO#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:36Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Demonstrates how to open a project file using the `ProjectReader`.
- Retrieves an assignment by its unique identifier (UID).
- Displays detailed information about the retrieved assignment, including resource name, task assignment, booking type, and cost.

## Content

### Retrieving and Displaying Assignment Information

The following example demonstrates how to open a project file, retrieve an assignment by its UID, and display its details using the `ProjIO` library.

#### Code Example: Retrieving and Displaying Assignment Information

```vb
' Opening the project file
Dim project As Project = ProjectReader.Open("SampleProject.xml")

' Retrieving a resource by UID
Dim assignment As Assignment = project.GetAssignmentByUID(1)

' Viewing retrieved assignment information
Console.WriteLine("Resource: " + assignment.Resource.Name)
Console.WriteLine("Assigned to: " + assignment.Task.Name)
Console.WriteLine("Booking Type: " + assignment.BookingType)
Console.WriteLine("Cost: $" + assignment.Cost)
```

### Explanation

1. **Opening the Project File**:
   - The `ProjectReader.Open` method is used to load the project file named `SampleProject.xml`. This file contains the project data, including assignments and resources.

2. **Retrieving an Assignment by UID**:
   - The `GetAssignmentByUID` method is called on the project object to fetch the assignment associated with the specified UID (in this case, UID 1).

3. **Displaying Assignment Details**:
   - The retrieved assignment's details are then printed to the console, including:
     - **Resource Name**: The name of the resource associated with the assignment.
     - **Task Name**: The name of the task to which the resource is assigned.
     - **Booking Type**: The type of booking for the resource (e.g., Fixed Units, Fixed Work, etc.).
     - **Cost**: The cost associated with the assignment.

## API Reference

### `ProjectReader.Open`
- **Namespace**: `Essential.ProjIO`
- **Parameters**: 
  - `filePath`: `String` - The path to the project file.
- **Returns**: `Project` - The loaded project object.

### `Project.GetAssignmentByUID`
- **Namespace**: `Essential.ProjIO`
- **Parameters**:
  - `uid`: `Integer` - The unique identifier of the assignment.
- **Returns**: `Assignment` - The assignment object associated with the specified UID.

### `Assignment`
- **Properties**:
  - `Resource.Name`: `String` - The name of the resource.
  - `Task.Name`: `String` - The name of the task.
  - `BookingType`: `String` - The booking type of the assignment.
  - `Cost`: `Decimal` - The cost of the assignment.

## Code Examples

The above example demonstrates the complete process of loading a project, retrieving a specific assignment, and displaying its details. This can be particularly useful for custom reporting or advanced resource and task management in project scheduling applications.

## Conclusion

This section provides a straightforward example of how to interact with project assignments using the `ProjIO` library. By leveraging the provided APIs, developers can efficiently retrieve and display assignment details, facilitating enhanced project management workflows.

<!-- tags: projectmanagement, projio, syncfusion, vb, assignment, resource, task, cost, bookingtype keywords: projectreader, getassignmentbyuid, assignmentdetails, resource, task, cost -->
```

---

<!-- 페이지 50 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_004.jpeg
document_name: ProjIO
page_number: 004
page_id: ProjIO#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:55:58Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- 1. Does ProjIO require MS Project to be installed on the machine?
- 2. Will it be possible to view the generated project (`.xml` file) using ProjIO?
- 3. Can Essential ProjIO be used to read MS Project files?
- 4. How to retrieve tasks from a project?

### Detailed Questions
- **5.1 Does ProjIO require MS Project to be installed on the machine?** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\

---

<!-- 페이지 51 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: ProjIO
page_number: 008
page_id: ProjIO#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:32Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Discusses the Essential Studio Reporting Dashboard.
- Explains the steps to view ProjIO samples for various platforms.
- Focuses specifically on the Windows platform for reporting.

## Content

### Essential Studio Reporting Dashboard

![Essential Studio Reporting Dashboard](#)

**Figure 1: Essential Studio Reporting Dashboard**

The steps to view the ProjIO samples in various platforms are discussed below.

#### Windows

1. **In the Dashboard window, click Run Samples for Windows Forms under Reporting Edition Panel.** The Windows Forms Sample Browser window is displayed.

## API Reference (if applicable)
Coming soon.

## Code Examples (multi-language supported)
Coming soon.

## Cross References
- Refer to related sections or resources for more detailed information on ProjIO and Syncfusion Winforms.

<!-- tags: [essential studio, reporting, projio, winforms, samples, dashboard] keywords: [essential studio, reporting dashboard, reporting edition, projio samples, winforms, asp.net, silverlight, windows forms, sample browser] -->
```

---

<!-- 페이지 52 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: ProjIO
page_number: 012
page_id: ProjIO#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:41Z
fidelity: lossless
-->

## Deployment Procedures

### DLLs
The following assemblies need to be referenced in your application for the usage of ProjIO:
- Syncfusion.Core.dll
- Syncfusion.ProjIO.Base.dll

```markdown
<!-- tags: [product: Syncfusion Winforms, module: ProjIO, control: deployment, api: referenced assemblies, version:] keywords: [deployment procedures, dlls, Syncfusion.Core.dll, Syncfusion.ProjIO.Base.dll] -->
``` 
```

---

<!-- 페이지 53 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: ProjIO
page_number: 016
page_id: ProjIO#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:48Z
fidelity: lossless
-->

## Essential ProjIO

### Properties and Descriptions

| Property                      | Description                                                                                                                                                                   |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InsertedProjectsLikeSummary   | True if subtasks are calculated as summary tasks.                                                                                                                            |
| MultipleCriticalPaths         | True if multiple critical paths are calculated.                                                                                                                              |
| NewTasksEffortDriven          | True if new tasks are effort-driven.                                                                                                                                         |
| NewTasksEstimated             | True to show the estimated duration by default.                                                                                                                              |
| SplitsInProgressTasks         | True if in-progress tasks can be split.                                                                                                                                      |
| SpreadActualCost               | True if actual costs are spread to the status date.                                                                                                                         |
| SpreadPercentComplete         | True if percent complete is spread to the status date.                                                                                                                      |
| TaskUpdatesResource           | True if updates to tasks update resources.                                                                                                                                   |
| FiscalYearStart               | True to use fiscal year numbering.                                                                                                                                           |
| WeekStartDay                  | Gets or sets the Start day of the week.                                                                                                                                      |
| MoveCompletedEndsBack         | True if the end of completed portions of tasks scheduled to begin after the status date but begun early should be moved back to the status date.                           |
| MoveRemainingStartsBack       | True if the beginning of remaining portions of tasks scheduled to begin after the status date but began early should be moved back to the status date.                       |
| MoveRemainingStartsForward    | True if the beginning of remaining portions of tasks scheduled to begin late should be moved up to the status date.                                                          |
| MoveCompleteEndsForward       | True if the end of completed portions of tasks scheduled to get completed before the status date but began late should be moved up to the status date.                        |
| BaselineForEarnedValue        | Gets or sets the specific baseline used to calculate Variance values.                                                                                                       |
| AutoAddNewResourcesAndTasks   | True to automatically add new resources to the resource pool.                                                                                                                |
| StatusDate                    | Gets or sets the date used for calculation and reporting.                                                                                                                   |
| CurrentDate                   | Gets or sets the system date that the XML was generated.                                                                                                                    |
| MicrosoftProjectServerURL     | True if the project was created by a Project Server user as opposed to an NT user.                                                                                           |
| Autolink                      | True to auto-link inserted or moved tasks.                                                                                                                                   |

### API Reference

For detailed API information related to the properties listed above, refer to the Syncfusion Winforms documentation for version 11.4.0.26. The properties listed in this section are part of the `ProjIO` module, which provides essential functionality for managing project schedules and task dependencies within the WinForms framework.

## Code Examples

Example of setting and retrieving the `StatusDate` property in C#:

```csharp
// Setting the StatusDate
project.StatusDate = new DateTime(2023, 10, 5);

// Retrieving the StatusDate
DateTime statusDate = project.StatusDate;
```

### RAG Annotations

- **Tags:** Essential ProjIO, properties, task scheduling, cost estimation
- **Keywords:** status date, critical paths, effort-driven tasks, fiscal year, project server, auto-link
```

---

<!-- 페이지 54 -->

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

---

<!-- 페이지 55 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_024.jpeg
document_name: ProjIO
page_number: 024
page_id: ProjIO#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:35Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
[C#]

// Creating a new instance of the Project object
Project project = new Project();

// Setting Project Default information
project.DefaultStartTime = new TimeSpan(8, 0, 0);
project.DefaultFinishTime = new TimeSpan(17, 0, 0);
project.DefaultStandardRate = 0f;
project.DefaultOvertimeRate = 0f;
project.DefaultTaskEVMethod = EarnedValueMethod.PercentComplete;
project.DefaultFixedCostAccrual = DefaultFixedCostAccrual.Prorated;

// Saving the Project
project.Save("DefaultProjectProperties.xml");
```

```vb
[VB]

' Creating an instance of a Project
Dim project As Project = New Project()

' Setting Project information
project.DefaultStartTime = New TimeSpan(8, 0, 0)
project.DefaultFinishTime = New TimeSpan(17, 0, 0)
project.DefaultStandardRate = 0.0F
project.DefaultOvertimeRate = 0.0F
project.DefaultTaskEVMethod = EarnedValueMethod.PercentComplete
project.DefaultFixedCostAccrual = DefaultFixedCostAccrual.Prorated

' Saving the Project
project.Save("DefaultProjectProperties.xml")
```

## API Reference (if applicable)
### WinForms-specific conventions
- Prefer C# samples when language is ambiguous; if VB is explicitly shown, keep both.
- Treat control names, namespaces, and types exactly (e.g., Syncfusion.Windows.Forms.Tools.TabControlAdv, Syncfusion.Windows.Forms.Grid).
- Distinguish design-time vs runtime features; preserve property grids, designer steps, and menu paths as regular text or ordered lists.
- When API elements are listed (Properties/Methods/Events/Enums) in subsections.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

### RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
- Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: ProjIO#page_024#getting-started -->. Do not add if the heading text is unclear.
```

---

<!-- 페이지 56 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_028.jpeg
document_name: ProjIO
page_number: 028
page_id: ProjIO#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:50Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
// Setting Fiscal Year information
project.FYStartDate = FYStartDate.April;
project.FiscalYearStart = true;

// Saving the Project
project.Save("FiscalProperties.xml");
```

```vb
' Creating an instance of Project
Dim project As Project = New Project()

' Setting Fiscal Year information
project.FYStartDate = FYStartDate.April
project.FiscalYearStart = True

' Saving the Project
project.Save("FiscalProperties.xml")
```

## 4.1.8 Week Day Properties

The Project class contains properties `WeekStartDay`, `DaysPerMonth`, `MinutesPerDay`, `MinutesPerWeek` that can be used to get or set Week day properties of a project.

### 4.1.8.1 Retrieving Week Day Properties

The following code snippets illustrate how to retrieve the Week day properties of a project.

```csharp
// Opening the project file
Project project = Syncfusion.ProjIO.ProjectReader.Open("Sample Project.xml");

// Retrieving Week day properties
```

## Footer
© 2013 Syncfusion. All rights reserved.
```

---

<!-- 페이지 57 -->

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

---

<!-- 페이지 58 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: ProjIO
page_number: 036
page_id: ProjIO#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:21Z
fidelity: lossless
-->

## 4.2.1.3 Methods

### Table 9: Task Methods

| **Method**     | **Description**                                          |
|----------------|----------------------------------------------------------|
| GetHashCode    | Serves as a hash function for Task type.                |
| GetType        | Gets the type of the current instance.                  |
| ToString       | Returns a string that represents the current object.    |

---

## 4.2.2 Adding Tasks to a Project

### Overview
- Tasks can be created in one or more ways as given below.

### By a default constructor
Creating a task instance without using any parameter as shown in the following code snippet:

#### C#
```csharp
Task task1 = new Task();
task1.Name = "Main Task";
task1.Start = DateTime.Now;
task1.Finish = DateTime.Now;
```

#### VB
```vb
Dim task1 As Task = New Task()
task1.Name = "Main Task"
task1.Start = DateTime.Now
task1.Finish = DateTime.Now
```

### By name
Creating a task instance by passing the task name as shown in the following code snippet:

---

## Code Examples

### C#
```csharp
Task task1 = new Task();
task1.Name = "Main Task";
task1.Start = DateTime.Now;
task1.Finish = DateTime.Now;
```

### VB
```vb
Dim task1 As Task = New Task()
task1.Name = "Main Task"
task1.Start = DateTime.Now
task1.Finish = DateTime.Now
```

---

<!-- tags: [Syncfusion, Winforms, Task, Methods, DefaultConstructor, NameParameter, DateTime, TaskCreation] keywords: [Task, CreateTask, TaskMethods, DateTime, CSharp, VB, TaskInstance, TaskName] -->
```

---

<!-- 페이지 59 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: ProjIO
page_number: 040
page_id: ProjIO#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:33Z
fidelity: lossless
-->

# Essential ProjIO

```vb
' Creating an instance of the Project
Dim P As Project = New Project()

' Creating tasks that are to be linked
Dim task1 As Task = New Task("Task1")
task1.Duration = new TimeSpan(8, 0, 0)
Dim task2 As Task = New Task("Task2")
task2.Duration = new TimeSpan(8, 0, 0)

' Adding the tasks to the RootTask of the Project
P.RootTask.Children.Add(task1)
P.RootTask.Children.Add(task2)

' Calculating Task IDs and UIDs
P.CalculateTaskIDs()

' Creating a link between task1 and task2
Dim link As TaskLink = New TaskLink(task1, task2, TaskLinkType.FinishToStart)

' Saving the project
P.Save("ProjectWithTasks.xml")
```

The project file created using above code will look as shown in the following screenshot.

## API Reference

### WinForms-specific conventions
- This section can include details about any specific conventions or considerations for working with **ProjIO** in the context of Syncfusion WinForms.

### Methods

- `Save(fileName As String)`: Saves the project to the specified file path.

### Properties

- `RootTask`: The root task of the project.
- `TaskLinkType`: Enum representing the type of linkage between tasks.

## Code Examples

The provided VB code snippet demonstrates the creation, configuration, and saving of a project with tasks and their dependencies using **ProjIO**. This example showcases how to:
1. Create a new project.
2. Define tasks with specified durations.
3. Link tasks using various dependency types.
4. Save the created project to an XML file.

---

<!-- tags: [projio, syncfusion, winforms, projectmanagement, tasklink, xml, visualbasic] keywords: [projio, tasklinktype, finishtostart, project, task, duration, calculateids, savingproject] -->
```

---

<!-- 페이지 60 -->

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

---

<!-- 페이지 61 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_048.jpeg
document_name: ProjIO
page_number: 048
page_id: ProjIO#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:03Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
' Saving the project
project.Save(@"D:\Project With Resources.xml")
```

## Overview
- Discusses the Assignment class used to bind resources to tasks.
- Explains how to retrieve details of tasks and resources bound together.
- Provides an introduction to the properties, methods, and events of the Assignment class.

## Content

### 4.4 Assignment
Assignment class is used to bind resources to tasks. It can also be used to retrieve the details of the task and resource that are bound together.

#### 4.4.1 Properties, Methods, and Events Tables for Task

##### 4.4.1.1 Constructors

**Table 13: Assignment Constructor**

| Name                | Description                                     |
|---------------------|-------------------------------------------------|
| Assignment.Assignment() | Initializes a new instance of Assignment class. |

##### 4.4.1.2 Properties

**Table 14: Assignment Properties**

| Property        | Description                                    |
|-----------------|-----------------------------------------------|
| UID            | Gets or sets the unique identifier of the assignment. |
| TaskUID        | Gets or sets the unique identifier of the task. |
| ResourceUID    | Gets or sets the unique identifier of the resource. |
| PercentWorkComplete | Gets or sets the amount of work completed on the assignment. |
| ActualCost     | Gets or sets the actual cost incurred on the assignment. |

## API Reference (if applicable)
- **Namespace**: Likely related to Syncfusion.Windows.Forms or similar namespace.
- **Class**: Assignment
- **Properties**:
  - UID
  - TaskUID
  - ResourceUID
  - PercentWorkComplete
  - ActualCost
- **Methods**:
  - Assignment.Assignment()

## Code Examples (multi-language supported)
```csharp
// Example of creating and initializing an Assignment object
Assignment assignment = new Assignment();
assignment.UID = 1;
assignment.TaskUID = 2;
assignment.ResourceUID = 3;
assignment.PercentWorkComplete = 50;
assignment.ActualCost = 100.0;
```

## Cross References
- Referenced concepts include binding resources to tasks and managing project details.
- See also: Task class for details on task-specific properties and methods. 

<!-- tags: [syncfusion, winforms, projio, assignment, resource management] keywords: [task, resource, assignment class, binding, properties, methods, events] -->
```

---

<!-- 페이지 62 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: ProjIO
page_number: 052
page_id: ProjIO#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:18Z
fidelity: lossless
-->

## Overview
- This page discusses the properties and methods related to assignments in a project.
- It details how assignments bind tasks and resources and how to add assignments to a project using the Assignments collection.

## Content

### 4.4.1.3 Methods
Table 15: Assignment Methods

| Method         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Equals          | Returns a value indicating whether this instance is equal to a specified object. |
| GetHashCode     | Serves as a hash function for Assignment type.                              |
| GetType         | Gets the type of the current instance.                                     |
| ToString        | Returns a string that represents the current object.                       |

### 4.4.2 Adding Assignments to a Project

Assignments are used to bind the task and resources. The Project class exposes Assignments collection that represents the list of all the Assignment objects in a project. This property can be used to add assignments.

The code below shows adding assignments to a project:

## API Reference (if applicable)

### Properties
| Property           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| AssnOwner          | Gets or sets the name of the assignment owner.                            |
| AssnOwnerGuid      | Gets or sets the GUID of the assignment owner.                           |
| BudgetCost         | Gets or sets the budgeted amount for cost resources on this assignment.  |
| BudgetWork         | Gets or sets the budgeted work amount for work or material resources on this assignment. |
| ExtendedAttribute  | Gets or sets the value of an extended attribute.                         |
| Baseline           | Gets or sets the collection of baseline values associated with the assignment. |
| F404000 – F4040C8 | Gets or sets Project 2010 assignment enterprise custom field elements.      |
| TimePhasedData     | Gets or sets the time phased data associated with the assignment.         |

## Code Examples (multi-language supported)
- The section provides an overview of how to add assignments to a project using the Assignments collection.

<!-- tags: [syncfusion, winforms, projio, assignments, project, task, resource, method, property, sdk] keywords: [assignments, project class, bindings, add assignment, budget cost, budget work, baseline, extended attribute] -->
```

---

<!-- 페이지 63 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: ProjIO
page_number: 056
page_id: ProjIO#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:32Z
fidelity: lossless
-->

# Essential ProjIO

## Getting Started

- Demonstrates how to create a project using the ProjIO API.
- Explains the use of `Assignments` to define tasks within the project.

## Content

The project created using the following code will look as shown in the following Microsoft Project screenshot:

```csharp
project.Assignments.Add(assignment)
```

### Screenshot of the Created Project

| Task Mode | Task Name | Duration | Start | Finish | Predecessor | Resource Name | 25, '11  | Oct 2, '11 | Oct 9, '11 | Oct 12, '11 |
|-----------|-----------|----------|-------|--------|-------------|---------------|----------|-------------|-------------|--------------|
| 1         | Task1     | 1 day?   | Fri 10/7/11 | Fri 10/7/11 |               | Resource1[8] | M T W T F S S M T W T F S S M T W T F S |
|           |           |          |       |        |             |               |            |             |             |              |
|           |           |          |       |        |             |               |            |             |             |              |
|           |           |          |       |        |             |               |            |             |             |              |

The screenshot illustrates the task "Task1" scheduled for one day, starting and finishing on Friday, October 7, 2011. The task is assigned to "Resource1" with the specified start and finish dates.

## API Reference

### Namespaces and Classes

- **Namespace**: Syncfusion.ProjIO
- **Class**: Project

#### Methods

- `Assignments.Add(Assignment assignment)`
  - **Parameters**:
    - `assignment`: The assignment object representing the task to be added to the project.

## Code Examples

Here is a sample code snippet demonstrating how to create a project and add an assignment to it:

```csharp
// Create a new Project instance
Project project = new Project();

// Create an Assignment object
Assignment assignment = new Assignment();

// Set properties of the assignment
assignment.Task.Name = "Task1";
assignment.Start = new DateTime(2011, 10, 7);
assignment.Finish = new DateTime(2011, 10, 7);
assignment.Resource.Name = "Resource1";

// Add the assignment to the project
project.Assignments.Add(assignment);

// Save the project to a file
project.Save("output.mpp");
```

## Cross References

- For more detailed information on working with projects and assignments, refer to the ProjIO documentation.

<!-- tags: Microsoft Project, ProjIO, Assignments, Task Management, Resource Assignment keywords: project, assignments, code example, screenshot -->
```

---

<!-- 페이지 64 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_060.jpeg
document_name: ProjIO
page_number: 060
page_id: ProjIO#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:48Z
fidelity: lossless
-->

# Essential ProjIO

## 5 How To

### 5.1 Does ProjIO require MS Project to be installed on the machine?

No. ProjIO is a 100% Native .Net Library that does not depend on MS Project.

### 5.2 Will it be possible to view the generated project [`.xml` file] using ProjIO?

No. ProjIO does not have a Graphical User Interface to view the generated project files. MS Project is required to view the project files generated by using ProjIO.

### 5.3 Can Essential ProjIO be used to read MS Project files?

Essential ProjIO provides support for reading MS Project XML format files. Currently ProjIO does not support reading and writing files in `.mpp` or `.mpt` format.

### 5.4 How to retrieve tasks from a project?

The tasks present in a project can be retrieved using the `GetTaskByUID` method.  
The following code snippet illustrates retrieving tasks using this method:

```csharp
// Opening the project file
Project project = ProjectReader.Open(@"D:\ProjectWithTasks.xml");

// Retrieving a task by UID
Task task = project.GetTaskByUID(2);

// Viewing retrieved task information
Console.WriteLine("Task Name: " + task.Name);
Console.WriteLine("Task Start Date: " + task.Start);
Console.WriteLine("Task Finish Date: " + task.Finish);
Console.WriteLine("No. of Sub Tasks: " + task.Children.Count);
```

## API Reference

### Overview
- ProjIO allows retrieving tasks from a project by UID.
- The `ProjectReader` class is used to open the project file.
- Task details such as name, start date, finish date, and sub-task count can be accessed.

### Methods
- `GetTaskByUID(int uid)`
  - Retrieves a task from the project based on its unique identifier (UID).
  - **Parameters:**
    - `uid`: The unique identifier of the task to retrieve.
  - **Returns:**
    - `Task`: The task object corresponding to the provided UID.
  - **Example Usage:**
    ```csharp
    Task task = project.GetTaskByUID(2);
    ```

### Task Properties
- `Name`
  - The name of the task.
- `Start`
  - The start date of the task.
- `Finish`
  - The finish date of the task.
- `Children`
  - A collection of sub-tasks under the specified task.
    - `Count`: The number of sub-tasks.

## Code Examples

### Retrieving a Task by UID

```csharp
using System;
using Syncfusion.ProjectIO;

class Program
{
    static void Main()
    {
        // Open the project file
        Project project = ProjectReader.Open(@"D:\ProjectWithTasks.xml");

        // Retrieve a task by UID
        Task task = project.GetTaskByUID(2);

        // Display task details
        Console.WriteLine("Task Name: " + task.Name);
        Console.WriteLine("Task Start Date: " + task.Start);
        Console.WriteLine("Task Finish Date: " + task.Finish);
        Console.WriteLine("No. of Sub Tasks: " + task.Children.Count);
    }
}
```

### RAG Annotations
<!-- tags: ProjIO, MS Project, Project Reader, Task retrieval, Unique Identifier, Task Properties, C# code examples, Syncfusion Winforms, version: 11.4.0.26 -->
<!-- keywords: projio, task, uid, gettaskbyuid, ms project, projectreader, task properties, name, start date, finish date, sub tasks, csharp, code examples, essential toolkit -->

---

<!-- 페이지 65 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: ProjIO
page_number: 064
page_id: ProjIO#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:01:08Z
fidelity: lossless
-->

# Essential ProjIO

## Index

### A
- Adding Assignments to a Project 52
- Adding Resources to a Project 46
- Adding Tasks to a Project 36
- Assignment 48

### C
- Calendar 57
- Can Essential ProjIO be used to read MS Project files? 60
- Concepts and Features 14
- Constructors 14, 30, 41, 48, 57
- Creating a simple project 18
- Creating a Standard Calendar 58
- Creating a summary task 37
- Creating Task links 38

### D
- Default Project Properties 22
- Deployment Procedures 12
- DLLs 12
- Documentation 6
- Does ProjIO require MS Project to be installed on the machine? 60

### F
- Feature Summary 13
- Fiscal Year Properties 26

### G
- General Project Properties 20
- Getting Started 13

### H
- How To 60
- How to retrieve tasks from a project? 60

### I
- Installation 7
- Installation and Deployment 7
- Introduction to Essential ProjIO 5

### M
- Methods 17, 36, 45, 52, 58

### O
- Overview 5

### P
- Prerequisites and Compatibility 5
- Project 14
- Properties 14, 31, 41, 48, 57
- Properties, Methods, and Events Tables for Project 14
- Properties, Methods, and Events Tables for Task 30, 41, 48, 57

### R
- Reading a project file 19
- Resource 41
- Retrieving Default Project Properties 22
- Retrieving Fiscal Year Properties 27
- Retrieving Project Properties 20
- Retrieving Week Day Properties 28

### S
- Sample Installation Location 7
- Setting Default Project Properties 23
- Setting Fiscal Year Properties 27
- Setting Project Properties 21
- Setting Week Day Properties 29

### T
- Task 30

### U
- Use Case Scenario 5

### V
- Viewing Samples 7
```