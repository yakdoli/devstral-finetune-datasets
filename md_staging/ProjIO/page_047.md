```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: ProjIO
page_number: 047
page_id: ProjIO#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:27Z
fidelity: lossless
-->

## Essential ProjIO

### Overview

- Demonstrates how to write resources to a project.
- Explains steps using C# and VB code snippets.

### Content

The following code shows how to write resources to a project.

#### C# Code Example

```csharp
// Creating an instance of the Project
Project project = new Project();

// Creating resource
Resource resource = new Resource();
resource.Name = "Resource1";

// Adding resource to project
project.Resources.Add(resource);

// Calculating Resource IDs and UIDs
project.CalculateResourceIDs();

// Saving the project
project.Save("Project With Resources.xml");
```

#### VB Code Example

```vb
' Creating an instance of the Project
Dim project As Project = New Project()

' Creating resource
Dim resource As Resource = New Resource()
resource.Name = "Resource1"

' Adding resource to Project
project.Resources.Add(resource)

' Calculating Resource IDs and UIDs
project.CalculateResourceIDs()
```

### API Reference

#### Methods Used
- `Project()`  
  - **Description**: Creates a new instance of the Project class.
- `Resource()`  
  - **Description**: Creates a new instance of the Resource class.
- `Resource.Name`  
  - **Description**: Sets the name of the resource.
- `Project.Resources.Add(resource)`  
  - **Description**: Adds the specified resource to the project's resource collection.
- `Project.CalculateResourceIDs()`  
  - **Description**: Calculates and assigns IDs and UIDs to the resources in the project.
- `Project.Save(filename)`  
  - **Description**: Saves the project to the specified file.

### Code Examples

#### C# Example
```csharp
Project project = new Project();
Resource resource = new Resource();
resource.Name = "Resource1";
project.Resources.Add(resource);
project.CalculateResourceIDs();
project.Save("Project With Resources.xml");
```

#### VB Example
```vb
Dim project As Project = New Project()
Dim resource As Resource = New Resource()
resource.Name = "Resource1"
project.Resources.Add(resource)
project.CalculateResourceIDs()
```

### Licensing
© 2013 Syncfusion. All rights reserved.

<!-- tags: [Essential ProjIO, resource management, project class, saving project, IDs, UIDs, C#, VB, Syncfusion Winforms, version 11.4.0.26] keywords: [ProjIO, resource, project, calculateResourceIDs, save, C#, VB, Syncfusion, Winforms] -->
```