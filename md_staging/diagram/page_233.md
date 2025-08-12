```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_233.jpeg
document_name: diagram
page_number: 233
page_id: diagram#page_233
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:09Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Flowchart representation of the "Port Changed Event."
- Illustrates the sequence of steps involving "START," "PROCESS," "CHECK," and "END."
- Highlighted an event handling mechanism in a Windows Forms application.

## Content

### WinForms Diagram Example

#### Port Changed Event

**Figure 145: Port Changed Event**

- **START**: Initiates the process flow.
- **PROCESS**: Handles the main logic or operations.
- **CHECK**: Performs validation or status check.
- **END**: Provides a termination condition.

![Figure illustrating the Port Changed Event](image-of-diagram.png)  
*(Note: An image of the diagram is available as a visual reference for the event handling process.)*

### 4.6.8.2.6 Property Events

Each node has different properties (Name, Color, Size, etc.). The below events are handled when changing these properties:

**Property Events** are as follows:

| DocumentEventSink               | Description                                           |
|----------------------------------|-------------------------------------------------------|
| PropertyChanged                 | Triggered after the property of any node is changed. |
| PropertyChanging                | Triggered when the property value is changed.        |

### Summary

This section explains how property events are handled in a Windows Forms application, focusing on the changes to node properties like Name, Color, and Size. The diagram visually demonstrates the flow of operations and event handling in such an application.

### API Reference

#### Events

1. **PropertyChanged**
   - Triggered after the property of any node is changed.
2. **PropertyChanging**
   - Triggered when the property value is changed.

### Code Examples

```csharp
// Example handling the PropertyChanging event
class Node {
    public string Name { get; set; }

    public event EventHandler PropertyChanging;

    protected virtual void OnPropertyChanging(PropertyChangedEventArgs e) {
        PropertyChanging?.Invoke(this, e);
    }
}
```

## RAG Annotations

<!-- tags: [property events, windows forms, port changed event, diagram, node properties, event handling] keywords: [PropertyChanged, PropertyChanging, Windows Forms, Syncfusion Winforms, Process Flowchart] -->
```