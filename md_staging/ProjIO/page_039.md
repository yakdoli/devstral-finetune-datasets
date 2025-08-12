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