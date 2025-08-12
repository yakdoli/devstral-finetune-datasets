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