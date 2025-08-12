```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: ProjIO
page_number: 056
page_id: ProjIO#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:00:32Z
fidelity: lossless
-->

# Essential ProjIO

## Getting Started

- Demonstrates how to create a project using the ProjIO API.
- Explains the use of `Assignments` to define tasks within the project.

## Content

The project created using the following code will look as shown in the following Microsoft Project screenshot:

```csharp
project.Assignments.Add(assignment)
```

### Screenshot of the Created Project

| Task Mode | Task Name | Duration | Start | Finish | Predecessor | Resource Name | 25, '11  | Oct 2, '11 | Oct 9, '11 | Oct 12, '11 |
|-----------|-----------|----------|-------|--------|-------------|---------------|----------|-------------|-------------|--------------|
| 1         | Task1     | 1 day?   | Fri 10/7/11 | Fri 10/7/11 |               | Resource1[8] | M T W T F S S M T W T F S S M T W T F S |
|           |           |          |       |        |             |               |            |             |             |              |
|           |           |          |       |        |             |               |            |             |             |              |
|           |           |          |       |        |             |               |            |             |             |              |

The screenshot illustrates the task "Task1" scheduled for one day, starting and finishing on Friday, October 7, 2011. The task is assigned to "Resource1" with the specified start and finish dates.

## API Reference

### Namespaces and Classes

- **Namespace**: Syncfusion.ProjIO
- **Class**: Project

#### Methods

- `Assignments.Add(Assignment assignment)`
  - **Parameters**:
    - `assignment`: The assignment object representing the task to be added to the project.

## Code Examples

Here is a sample code snippet demonstrating how to create a project and add an assignment to it:

```csharp
// Create a new Project instance
Project project = new Project();

// Create an Assignment object
Assignment assignment = new Assignment();

// Set properties of the assignment
assignment.Task.Name = "Task1";
assignment.Start = new DateTime(2011, 10, 7);
assignment.Finish = new DateTime(2011, 10, 7);
assignment.Resource.Name = "Resource1";

// Add the assignment to the project
project.Assignments.Add(assignment);

// Save the project to a file
project.Save("output.mpp");
```

## Cross References

- For more detailed information on working with projects and assignments, refer to the ProjIO documentation.

<!-- tags: Microsoft Project, ProjIO, Assignments, Task Management, Resource Assignment keywords: project, assignments, code example, screenshot -->
```