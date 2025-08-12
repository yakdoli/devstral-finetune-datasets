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