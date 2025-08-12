```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_222.jpeg
document_name: diagram
page_number: 222
page_id: diagram#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:14Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This section explains the behavior of Pinpoint Changed and Rotation Events in the Diagram component of Syncfusion WinForms.
- Provides details on event triggers and their corresponding actions.

## Content

### Pinpoint Changed Event

#### Overview
- **Figure 137: Pinpoint Changed Event** illustrates the scenario when the PinPointChanged event is triggered.

#### Description
- When the control is rotated horizontally or vertically, the rotation events will be fired, displaying the rotation offsets.

#### Available Rotation Events with Descriptions

| DocumentEventSink     | Description                                       |
|-----------------------|---------------------------------------------------|
| FlipChanged           | Triggered after the node is rotated using Flip property. |
| FlipChanging          | Triggered when the node is rotated using Flip property. |
| RotationChanged       | Triggered after the node is rotated. |
| RotationChanging      | Triggered on rotating the node in any direction. |

### Rotation Events

#### Overview
- Describes the behavior and details of rotation events in the Diagram control.

#### Data Access
- Data can be retrieved or set using the following members.

#### Rotation EventArgs Member | Description

| Rotation EventArgs Member | Description |
|---------------------------|-------------|
| (Members list to be added here) | (Descriptions corresponding to each member) |

### API Reference

- **FlipChanged**: Triggered after the node is rotated using the Flip property.
- **FlipChanging**: Triggered when the node is rotated using the Flip property.
- **RotationChanged**: Triggered after the node is rotated.
- **RotationChanging**: Triggered on rotating the node in any direction.

### Code Examples

#### Example 1: Handling FlipChanged Event (Sample C# code)
```csharp
DiagramNode myNode = new DiagramNode();
myNode.FlipChanged += (sender, args) =>
{
    // Handle FlipChanged event logic here
};
```

#### Example 2: Handling RotationChanged Event (Sample C# code)
```csharp
DiagramNode myNode = new DiagramNode();
myNode.RotationChanged += (sender, args) =>
{
    // Handle RotationChanged event logic here
};
```

## RAG Annotations

<!-- tags: [Syncfusion WinForms, Diagram, Rotation Events, Pinpoint Changed] keywords: [DiagramControl, FlipChanged, FlipChanging, RotationChanged, RotationChanging, EventHandling, RotationOffsets] -->
```