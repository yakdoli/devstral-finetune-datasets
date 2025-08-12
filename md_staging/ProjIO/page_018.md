```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: ProjIO
page_number: 018
page_id: ProjIO#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:59Z
fidelity: lossless
-->

# Essential ProjIO

| Method/Property       | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Save                 | Saves Project instance to disk                                              |
| CalculateResourceIDs | Recalculates UIDs and IDs of resources starting from 0                      |
| CalculateTaskIDs     | Recalculates UIDs and IDs of tasks starting from 0                          |
| Equals               | Returns a value indicating whether this instance is equal to a specified object |
| GetHashCode          | Serves as a hash function for Project type                                     |
| GetType              | Gets the type of the current instance                                          |
| ToString             | Returns a string that represents the current object                           |

## 4.1.2 Creating a simple project

**Project** is the main class of Essential ProjIO. We can only create project files in XML format. The following lines of code create a simple project.

### [C#]

```csharp
// Creating an instance of Project
Project project = new Project();

// Saving the project – Creates an empty project
project.Save("Empty Project.xml");
```

### [VB]

```vb
' Creating an instance of Project
Dim project As Project = New Project()

' Saving the Project – Creates an empty project
project.Save("Empty Project.xml")
```

The XML project file can be viewed in Microsoft Project using the option **File – Open** and then selecting the XML format (*.xml) option from the file types. Select ‘Project Information’ option from the **Projects** menu and the options will look as follows:

<!-- tags: [projio, essential projio, project class, xml project file, creating a simple project, c#, vb, code samples, api reference, microsoft project plugin, syncfusion winforms, version 11.4.0.26] keywords: [project, xml, creating projects, project class, essential projio, code examples, project information, file management, save method, calculate methods, equals method, project type, string representation] -->
```