```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_028.jpeg
document_name: ProjIO
page_number: 028
page_id: ProjIO#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:50Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
// Setting Fiscal Year information
project.FYStartDate = FYStartDate.April;
project.FiscalYearStart = true;

// Saving the Project
project.Save("FiscalProperties.xml");
```

```vb
' Creating an instance of Project
Dim project As Project = New Project()

' Setting Fiscal Year information
project.FYStartDate = FYStartDate.April
project.FiscalYearStart = True

' Saving the Project
project.Save("FiscalProperties.xml")
```

## 4.1.8 Week Day Properties

The Project class contains properties `WeekStartDay`, `DaysPerMonth`, `MinutesPerDay`, `MinutesPerWeek` that can be used to get or set Week day properties of a project.

### 4.1.8.1 Retrieving Week Day Properties

The following code snippets illustrate how to retrieve the Week day properties of a project.

```csharp
// Opening the project file
Project project = Syncfusion.ProjIO.ProjectReader.Open("Sample Project.xml");

// Retrieving Week day properties
```

## Footer
© 2013 Syncfusion. All rights reserved.
```