```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: diagram
page_number: 217
page_id: diagram#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:08Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the usage of flow diagrams in Windows Forms.
- Highlights the sequence of operations from Start to End.
- Includes a Vertex Changing Event notification.

## Content

### Diagram Overview
The following diagram illustrates a simple flow process:

```markdown
Simple Flow Diagram

1. **START** - Marks the beginning of the process.
2. **PROCESS** - Indicates the main action or task.
3. **CHECK** - Represents a decision point or verification step.
4. **END** - Denotes the completion of the process.
5. **Vertex Changing Event** - A notification dialog that appears during the process.
```

#### Figure: Diagram with Vertex Changing Event

![](image.png)

**Figure 134: Diagram with Vertex Changing Event**

This diagram includes the following components:
- **Start** symbol: An oval shape indicating the initiation of the process.
- **Process** symbol: A rectangle representing the main processing steps.
- **Check** symbol: A diamond shape for decision-making or verification.
- **End** symbol: An oval shape signifying the conclusion of the process.
- **Vertex Changing Event**: A dialog box that appears as part of the process, indicating a notification or action.

## API Reference

### Methods
- **VertexChangingEvent**: Triggered when the vertex of a node is changed.
  - **Parameters**: None.
  - **Returns**: None.
  - **Usage**: Used to handle events related to vertex changes in the diagram.

## Code Examples

### C# Example

```csharp
// Example code for handling VertexChanging event
private void Diagram_VertexChanging(object sender, EventArgs e)
{
    MessageBox.Show("VertexChanging fired");
}
```

### VB.NET Example

```vb
' Example code for handling VertexChanging event
Private Sub Diagram_VertexChanging(ByVal sender As Object, ByVal e As EventArgs)
    MessageBox.Show("VertexChanging fired")
End Sub
```

## Cross References
- For more details on handling events in diagrams, refer to the Events section in the Syncfusion documentation.
- For an overview of flow diagrams and their components, see the Flowcharting Basics guide.

<!-- tags: [diagram, winforms, event handling, flowchart, vertexchanging, syncfusion] keywords: [simple flow diagram, start, process, check, end, vertex changing event, c#, vb.net] -->
```