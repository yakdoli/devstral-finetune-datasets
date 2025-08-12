```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: ProjIO
page_number: 027
page_id: ProjIO#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:58Z
fidelity: lossless
-->

# Essential ProjIO

## Retrieving Fiscal Year Properties

The following code snippets retrieve Fiscal year properties from a project:

### C#
```csharp
// Calling Open method of ProjectReader to get the Project object
Project project = ProjectReader.Open("Sample Project.xml");

// Retrieving Fiscal Year information
Console.WriteLine("Fiscal Year Start Month: " + project.FYStartDate);

Console.WriteLine(project.FiscalYearStart ? "Fiscal Year Numbering is used in the Project" : "Fiscal Year Numbering is not used in the Project");
```

### VB
```vbnet
' Calling Read method of ProjectReader to get the Project object
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Retrieving Fiscal Year information
Console.WriteLine("Fiscal Year Start Month: " + project.FYStartDate)

Console.WriteLine(If(project.FiscalYearStart, "Fiscal Year Numbering is used in the Project", "Fiscal Year Numbering is not used in the Project"))
```

## Setting Fiscal Year Properties

The following code sets the Fiscal year properties for a project.

### C#
```csharp
// Creating a new instance of Project object
Project project = new Syncfusion.ProjIO.Project();
```

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

<!-- tags: [ProjIO, Fiscal Year, Project Properties, Retrieving, Setting, C#, VB, ProjectReader, Syncfusion, Essentials] keywords: [FiscalYearStart, FYStartDate, ProjectReader, ProjectReader.Open, If, Console.WriteLine, Syncfusion.ProjIO.Project] -->
```