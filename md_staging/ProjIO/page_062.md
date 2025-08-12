```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: ProjIO
page_number: 062
page_id: ProjIO#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:59:33Z
fidelity: lossless
-->

# Essential ProjIO

[VB]

```vb
' Opening the project file
Dim project As Project = ProjectReader.Open("ProjectWithResources.xml")

' Retrieving a resource by UID
Dim resource As Resource = project.GetResourceByUID(1)

' Viewing retrieved resource information
Console.WriteLine("Resource Name: " + resource.Name)
Console.WriteLine("Type: " + resource.Type)
Console.WriteLine("Work: " + resource.Work)
Console.WriteLine("Remaining Work: " + resource.RemainingWork)
Console.WriteLine("Resource Calendar ID: " + resource.CalendarUID)
```

## How to retrieve resource assignments from a project?

The resource assignments present in a project can be retrieved using the `GetAssignmentByUID` method.

The following code snippet shows how to use this method:

[C#]

```csharp
// Opening the project file
Project project = ProjectReader.Open("SampleProject.xml");

// Retrieving an assignment by UID
Assignment assignment = project.GetAssignmentByUID(1);

// Viewing retrieved assignment information
Console.WriteLine("Resource: " + assignment.Resource.Name);
Console.WriteLine("Assigned to: " + assignment.Task.Name);
Console.WriteLine("Booking Type: " + assignment.BookingType);
Console.WriteLine("Cost: $" + assignment.Cost);
```
```