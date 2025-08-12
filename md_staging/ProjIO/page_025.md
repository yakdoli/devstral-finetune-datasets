```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: ProjIO
page_number: 025
page_id: ProjIO#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:31Z
fidelity: lossless
-->

## 4.1.6 Writing Project Summary Information

Project class contains properties that can get or set the summary information of a project file in XML format. Using this class, the summary information can be updated and the file can be written back in XML format. The following code shows how this can be done.

```csharp
// C#

// Calling Read method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Setting Project Default information
project.SaveVersion = 14;
project.Author = "Sam Anderson";
project.Manager = "John Henson";
project.Company = "Syncfusion";
project.CreationDate = new DateTime(2011, 10, 8);
project.Subject = "Essential ProjIO";
project.Title = "Sample Project";

// Saving the Project
project.Save("Empty Project.xml");
```

```vb
' VB

' Calling Read method of ProjectReader to get the Project object
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Retrieving Project information
project.SaveVersion = 14
project.Author = "Sam Anderson"
project.Manager = "John Henson"
project.Company = "Syncfusion"
project.CreationDate = New DateTime(2011, 10, 8)
project.Subject = "Essential ProjIO"
```

## API Reference

### Namespace: Syncfusion.ProjIO

#### Class: Project
- Properties:
  - **SaveVersion**: Sets or gets the version number of the project file.
  - **Author**: Sets or gets the author name of the project. Type: string.
  - **Manager**: Sets or gets the manager name of the project. Type: string.
  - **Company**: Sets or gets the company name of the project. Type: string.
  - **CreationDate**: Sets or gets the date the project was created. Type: DateTime.
  - **Subject**: Sets or gets the subject of the project. Type: string.
  - **Title**: Sets or gets the title of the project. Type: string.
- Method:
  - **Save(string filename)**: Saves the project to the specified XML file path.

## Code Examples

The provided C# and VB.NET code examples demonstrate how to:

1. Open an existing project file using the `ProjectReader.Open` method.
2. Update the project properties such as `SaveVersion`, `Author`, `Manager`, `Company`, `CreationDate`, `Subject`, and `Title`.
3. Save the updated project to a new XML file using the `Save` method.

The code snippets provided illustrate the process of reading, modifying, and writing project summary information using the `Project` class from Syncfusion's ProjIO library.

## Cross References

- See also: [4.1 Basic Operations](#4.1-basic-operations)

<!-- tags: [projio, project, xml, summary information, winforms, syncfusion] keywords: [project class, project summary, xml format, project file, version number, author, manager, company, creation date, subject, title, project save] -->
```