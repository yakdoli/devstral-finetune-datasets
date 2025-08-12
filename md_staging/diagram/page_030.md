```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: diagram
page_number: 030
page_id: diagram#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:11Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This section provides a detailed explanation of the Diagram control in Windows Forms.
- Focuses on connecting nodes using the Diagram control's predefined links (connectors).
- Demonstrates how to create custom connectors by inheriting from the `ConnectorBase` class.

## Content

### 3.2.1.4 Connecting Nodes

The Diagram control has a set of predefined links (connectors) which help you to connect the nodes with each other. You can create your own connectors by inheriting the ConnectorBase class.

#### Example: Connecting Nodes
The following code illustrates how to connect a process node to a decision node by using the `OrthogonalConnector`.

#### Code Example

```csharp
// Create a process node
Syncfusion.Windows.Forms.Diagram.Rectangle process =
    new Syncfusion.Windows.Forms.Diagram.Rectangle(50, 50, 100, 70);

// Style the process node
process.FillStyle.Type = FillStyleType.LinearGradient;
process.FillStyle.Color = Color.FromArgb(128, 0, 0);
```

### Explanation of the Code
1. **Creating a Process Node**:
   - A `Rectangle` node is created using the `Diagram.Rectangle` class.
   - The `Rectangle` is initialized with its position (50, 50) and size (100, 70).

2. **Styling the Process Node**:
   - The `FillStyle.Type` property is set to `FillStyleType.LinearGradient` to apply a gradient fill.
   - The `FillStyle.Color` property is set to `Color.FromArgb(128, 0, 0)` to define the color of the fill.

#### Note
- This example focuses on creating and styling a process node. The connection between nodes is achieved using predefined or custom connectors.

#### Figure 13: Rectangular Node

![Rectangular Node](#)
*Figure 13: Rectangular Node*

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Diagram`
- **Class**: `Rectangle`
- **Properties**:
  - `FillStyle.Type`: Determines the type of fill applied to the node.
  - `FillStyle.Color`: Defines the color of the fill.

### Code Examples

The provided code example demonstrates the creation and styling of a process node. For more advanced usage, you can explore customizing connectors and integrating them into your application.

## Cross References

- Reference the documentation on inheritence and advanced customization for connectors.
- Refer to the section on `ConnectorBase` for creating custom connectors.

### RAG Annotations

<!-- tags: [diagram, windows forms, nodes, connectors, csharp, linear gradient] keywords: [Node, Connector, Diagram Control, Windows Forms, C#, LinearGradient, FillStyle, Color] -->
```