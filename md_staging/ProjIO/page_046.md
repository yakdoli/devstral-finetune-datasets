```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: ProjIO
page_number: 046
page_id: ProjIO#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:42Z
fidelity: lossless
-->

## 4.3.2 Adding Resources to a Project

The `Resources` property exposed by the `Project` class represents the list of all the `Resource` objects in a project. This property can be used to add resources.

The following code snippet illustrates adding resources to a project.

### Code Example: Adding Resources (C#)

```csharp
// Creating an instance of the Project
Project project = new Project();

// Creating resource
Resource resource = new Resource();
resource.Name = "Resource1";

// Adding resource to project
project.Resources.Add(resource);
```

### Code Example: Adding Resources (VB)

```vb
' Creating an instance of the Project
Dim project As Project = New Project()

' Creating resource
Dim resource As Resource = New Resource()
resource.Name = "Resource1"

' Adding resource to Project
project.Resources.Add(resource)
```

## 4.3.3 Writing Resources to a Project

The `Resources` property exposed by the `Project` class represents the list of all the `Resource` objects in a project. This property can be used to update resources in a project.

## API Reference

- **Method:** `ToString`
  - **Returns:** A string that represents the current object.

## Page-level Navigation/TOC (if applicable)

- 4.3.2 Adding Resources to a Project
- 4.3.3 Writing Resources to a Project

## Cross References

See also: Further details on managing resources in projects can be found in the synchronization with bucket and Advanced properties and attributes sections.

<!-- tags: [ProjIO, Project, Resources, C#, VB] keywords: [Adding, Writing, Resources, Project] -->
```