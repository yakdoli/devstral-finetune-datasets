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