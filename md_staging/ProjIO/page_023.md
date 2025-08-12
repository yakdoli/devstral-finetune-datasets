```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_023.jpeg
document_name: ProjIO
page_number: 023
page_id: ProjIO#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:57:48Z
fidelity: lossless
-->

## Essential ProjIO

### Retrieving Project Information

```csharp
Console.WriteLine("Default Finish Time: " + project.DefaultFinishTime);
Console.WriteLine("Default Standard Rate: " +
project.DefaultStandardRate);
Console.WriteLine("Default Overtime Rate: " +
project.DefaultOvertimeRate);
Console.WriteLine("Default Task EV Method: " +
project.DefaultTaskEVMethod);
Console.WriteLine("Default Cost Accrual: " +
project.DefaultFixedCostAccrual);
```

### [VB]

```vb
' Creating an instance of Project
Dim project As Project = ProjectReader.Open("Sample Project.xml")

' Retrieving Project information
Console.WriteLine("Default Start Time: " & project.DefaultStartTime.ToString())
Console.WriteLine("Default Finish Time: " & project.DefaultFinishTime.ToString())
Console.WriteLine("Default Standard Rate: " & project.DefaultStandardRate)
Console.WriteLine("Default Overtime Rate: " & project.DefaultOvertimeRate)
Console.WriteLine("Default Task EV Method: " & project.DefaultTaskEVMethod)
Console.WriteLine("Default Cost Accrual: " & project.DefaultFixedCostAccrual)
```

### 4.1.5.2 Setting Default Project Properties

The following example shows how to set the default project properties.

---

<!-- tags: [projio, project, information, retrieval, vb, setting, properties] keywords: [project, default finish time, standard rate, overtime rate, task ev method, cost accrual, projectreader, sample project] -->
```