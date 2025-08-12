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