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