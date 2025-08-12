```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: ProjIO
page_number: 063
page_id: ProjIO#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:36Z
fidelity: lossless
-->

# Essential ProjIO

## Overview
- Demonstrates how to open a project file using the `ProjectReader`.
- Retrieves an assignment by its unique identifier (UID).
- Displays detailed information about the retrieved assignment, including resource name, task assignment, booking type, and cost.

## Content

### Retrieving and Displaying Assignment Information

The following example demonstrates how to open a project file, retrieve an assignment by its UID, and display its details using the `ProjIO` library.

#### Code Example: Retrieving and Displaying Assignment Information

```vb
' Opening the project file
Dim project As Project = ProjectReader.Open("SampleProject.xml")

' Retrieving a resource by UID
Dim assignment As Assignment = project.GetAssignmentByUID(1)

' Viewing retrieved assignment information
Console.WriteLine("Resource: " + assignment.Resource.Name)
Console.WriteLine("Assigned to: " + assignment.Task.Name)
Console.WriteLine("Booking Type: " + assignment.BookingType)
Console.WriteLine("Cost: $" + assignment.Cost)
```

### Explanation

1. **Opening the Project File**:
   - The `ProjectReader.Open` method is used to load the project file named `SampleProject.xml`. This file contains the project data, including assignments and resources.

2. **Retrieving an Assignment by UID**:
   - The `GetAssignmentByUID` method is called on the project object to fetch the assignment associated with the specified UID (in this case, UID 1).

3. **Displaying Assignment Details**:
   - The retrieved assignment's details are then printed to the console, including:
     - **Resource Name**: The name of the resource associated with the assignment.
     - **Task Name**: The name of the task to which the resource is assigned.
     - **Booking Type**: The type of booking for the resource (e.g., Fixed Units, Fixed Work, etc.).
     - **Cost**: The cost associated with the assignment.

## API Reference

### `ProjectReader.Open`
- **Namespace**: `Essential.ProjIO`
- **Parameters**: 
  - `filePath`: `String` - The path to the project file.
- **Returns**: `Project` - The loaded project object.

### `Project.GetAssignmentByUID`
- **Namespace**: `Essential.ProjIO`
- **Parameters**:
  - `uid`: `Integer` - The unique identifier of the assignment.
- **Returns**: `Assignment` - The assignment object associated with the specified UID.

### `Assignment`
- **Properties**:
  - `Resource.Name`: `String` - The name of the resource.
  - `Task.Name`: `String` - The name of the task.
  - `BookingType`: `String` - The booking type of the assignment.
  - `Cost`: `Decimal` - The cost of the assignment.

## Code Examples

The above example demonstrates the complete process of loading a project, retrieving a specific assignment, and displaying its details. This can be particularly useful for custom reporting or advanced resource and task management in project scheduling applications.

## Conclusion

This section provides a straightforward example of how to interact with project assignments using the `ProjIO` library. By leveraging the provided APIs, developers can efficiently retrieve and display assignment details, facilitating enhanced project management workflows.

<!-- tags: projectmanagement, projio, syncfusion, vb, assignment, resource, task, cost, bookingtype keywords: projectreader, getassignmentbyuid, assignmentdetails, resource, task, cost -->
```