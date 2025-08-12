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