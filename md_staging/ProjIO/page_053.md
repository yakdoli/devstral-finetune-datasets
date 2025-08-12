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