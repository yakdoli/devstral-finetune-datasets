```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: ProjIO
page_number: 029
page_id: ProjIO#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:51Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
Console.WriteLine("Weeks starts on: " + project.WeekStartDay);
Console.WriteLine("No. of working days per month: " + 
project.DaysPerMonth);
Console.WriteLine("No.of minutes per day: " + project.MinutesPerDay);
Console.WriteLine("No. of minutes per week: " + 
project.MinutesPerWeek);
```

### VB
```vb
' Opening the project file
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Retrieving Week day properties
Console.WriteLine("Weeks starts on: " + project.WeekStartDay)
Console.WriteLine("No. of working days per month: " + 
project.DaysPerMonth)
Console.WriteLine("No.of minutes per day: " + project.MinutesPerDay)
Console.WriteLine("No. of minutes per week: " + project.MinutesPerWeek)
```

### 4.1.8.2 Setting Week Day Properties
The following code snippet illustrates how to set the Week day properties of a project.

#### C#
```csharp
// Creating a new Project instance
Project project = new Project();

// Setting week day properties
project.WeekStartDay = WeekStartDay.Monday;
project.DaysPerMonth = 24;
project.MinutesPerDay = 480;
project.MinutesPerWeek = 2880;
```

## Page-level Navigation/TOC (if applicable)
- 
```html
<!-- tags: [project file, project properties, week start day, working days, minutes per day, minutes per week, setting properties, syncfusion winforms, projectReader, sample project] keywords: [work day properties, start day, working days per month, minutes per day, minutes per week, project properties, projectReader, sample project.xml] -->
``` 
```