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
