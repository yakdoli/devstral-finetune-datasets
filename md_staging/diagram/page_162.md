```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: diagram
page_number: 162
page_id: diagram#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:51Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to create a rectangle node with custom ports using Syncfusion.Windows.Forms.Diagram.Rectangle.
- Explains the use of `ConnectionPoint` to define ports on a node.
- Describes how to customize port shapes using the `VisualType` property.

## Content

### Example Code

[C#]

```csharp
Syncfusion.Windows.Forms.Diagram.Rectangle rect = new
Syncfusion.Windows.Forms.Diagram.Rectangle(100, 100, 100, 50);
rect.DrawPorts = true;
Syncfusion.Windows.Forms.Diagram.ConnectionPoint cp = new
Syncfusion.Windows.Forms.Diagram.ConnectionPoint();
rect.Ports.Add(cp);
```

[VB]

```vb
Dim rect As New Syncfusion.Windows.Forms.Diagram.Rectangle(100, 100, 100, 50)
rect.DrawPorts = True
Dim cp As New Syncfusion.Windows.Forms.Diagram.ConnectionPoint()
rect.Ports.Add(cp)
```

#### Sample diagram is as follows.

![Rectangle Node with Four Custom Ports](images/rectangle_node_with_ports.jpg)

**Figure 96: Rectangle Node with Four Custom Ports**

### Port Shapes

The `VisualType` property available for the port can be used for customizing the shape of the port. There are several types of ports available for customizing the port's shape, each of which differs depending on how they are positioned within the symbol and how they are rendered. For example, a `CirclePort` can be positioned anywhere within the bounds of a symbol and renders itself as a circle containing cross hairs. Another example is a `CenterPort`, which always positions itself in the center of the symbol and has no visual representation.

#### Properties and Descriptions

| Property       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| VisualType     | Used for customizing the shape of the port. Various types of ports can be used. |

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Diagram`
- **Members**:
  - `ConnectionPoint`: Represents a port that can be added to a node.
  - `Rectangle`: A class representing a rectangle node.
  - `Ports`: A collection of ports associated with a node.

## Code Examples

The provided code examples demonstrate how to create a rectangle node and add custom ports using both C# and VB.NET.

## Page-level Navigation/TOC

- Port Shapes
- Properties and Descriptions
- Overview
- Example Code

## Cross References

For more information on the diagram control, refer to the [Syncfusion Diagram documentation](https://www.syncfusion.com/products/windowsforms/diagram).

<!-- tags: [syncfusion, windowsforms, diagram, ports, node, rectangle, visualtype] keywords: [ports, node, rectangle, visualtype, connectionpoint, centerport, circleport] -->
```
