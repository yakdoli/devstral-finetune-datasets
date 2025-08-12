```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: ProjIO
page_number: 022
page_id: ProjIO#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:12Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
project.CurrentDate = new DateTime(2011, 7, 9);
project.StatusDate = new DateTime(2011, 7, 9);

// Saving the Project
project.Save("ProjectProperties.xml");
```

```vb
' Creating an instance of Project
Dim project As Project = New Project()

' Setting Project information
project.ScheduleFromStart = True
project.StartDate = New DateTime(2011, 7, 9)
project.CurrentDate = New DateTime(2011, 7, 9)
project.StatusDate = New DateTime(2011, 7, 9)

' Saving the Project
project.Save("ProjectProperties.xml")
```

## 4.1.5 Default Project Properties

The Project class is used to get/set Project Default Properties. The default properties of a project can be viewed using the **Tools – Options** menu in MS Project.

### 4.1.5.1 Retrieving Default Project Properties

The following example illustrates how to retrieve default project properties.

```csharp
// Calling Open method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Retrieving Project Default information
Console.WriteLine("Default Start Time: " + project.DefaultStartTime);
```

## 4.1.5 Default Project Properties (Continued)

The `Project` class is used to get/set Project Default Properties. The default properties of a project can be viewed using the **Tools – Options** menu in MS Project.

### Code Example: Retrieving Default Project Properties

```csharp
// Calling Open method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Retrieving Project Default information
Console.WriteLine("Default Start Time: " + project.DefaultStartTime);
```

<!-- tags: [prodjio, project properties, retrieval, default properties, user guide, winforms] keywords: [project class, default start time, retrieving properties, tools options menu, project default properties, sample project, project reader] -->
```