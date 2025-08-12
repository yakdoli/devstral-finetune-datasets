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