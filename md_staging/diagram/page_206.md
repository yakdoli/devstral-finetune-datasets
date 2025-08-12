```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_206.jpeg
document_name: diagram
page_number: 206
page_id: diagram#page_206
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:12Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page explains how to handle tool-activated events in Essential Diagram for Windows Forms.
- It features a simple flow diagram illustrating the sequence of operations during a tool-activated event.

## Content

### Tool Activated Event

#### Diagram Overview
The diagram below demonstrates the flow of actions taken when a tool is activated within a Windows Forms application.

![Simple Flow Diagram](#)
*FIGURE 128: Tool Activated Event*

**Figure 128: Tool Activated Event**

The flow diagram consists of four main components, illustrated as follows:

1. **START**: Denotes the beginning of the event sequence.
2. **PROCESS**: Represents the process where the tool activation is handled.
3. **CHECK**: Indicates a check operation to identify the activated tool and its status.
4. **END**: Marks the completion of the event sequence.

#### Explanation of the Diagram
- **START**: Initiates the sequence of operations.
- **PROCESS**: Refers to the handling of the activated tool within the application logic.
- **CHECK**: Validates the tool details such as the tool name (`ZoomTool`) and its status (`False`), as shown in the accompanying dialog box.
- **END**: Concludes the event handling process.

### Dialog Box Details
The dialog box in the diagram provides specific information:
- **Activated Tool Name**: ZoomTool
- **Status**: False

This indicates that the tool activation event is reported, even if the tool is not currently active.

### Summary
This flow diagram helps developers understand the sequence of operations related to tool activation in Windows Forms, ensuring they can appropriately handle such events within their applications.

## Code Examples
This section may include code examples demonstrating how to implement the identified process, check, and manage the tool activated events in Syncfusion Winforms. The code examples would likely involve handling events and validating tool states.

```csharp
// Example of handling the ToolActivated event in Syncfusion Winforms
diagram1.ToolActivated += (sender, e) => {
    MessageBox.Show(
        $"Activated Tool Name: {e.Tool.Name}\nStatus: {e.Tool.IsActivated}",
        "Tool Activated",
        MessageBoxButtons.OK,
        MessageBoxIcon.Information
    );
};
```

## Cross References
- Refer to the documentation for more details on handling UI events in Essential Diagram for Windows Forms.

<!-- tags: [Syncfusion Winforms, Diagram, ToolActivatedEvent, Workflow, WindowsForms] keywords: [Essential Diagram, Windows Forms, tool activation, flow diagram, check event, tool status, dialog box, ZoomTool, activated tool name, False status] -->
```