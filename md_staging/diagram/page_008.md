```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: diagram
page_number: 008
page_id: diagram#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:07:31Z
fidelity: lossless
-->

## Overview

This page provides an essential diagram for understanding the flow of a wireless network in Windows Forms, showcasing various key features of Essential Diagram. The diagram illustrates the interaction between servers, workstations, modems, remote workstations, and control logic components, using specific network communication protocols such as Ethernet and Control Net. Key features highlighted include support for matrix transformations, custom shape drawing tools, and connector decorators.

---

### WIRELESS NETWORK FLOW DIAGRAM

The flow diagram (Figure 1) illustrates the seamless integration of wireless and wired network components, emphasizing the network pathways and communication protocols used to connect various devices.

#### Diagram Components
- **Servers**: Two server blocks at the top of the diagram.
- **WorkStations**: Stations connected to servers via Ethernet.
- **Modems**: Modems labeled Modem1, Modem2, Modem3, and Modem4, connected to different parts of the network.
- **Remote WorkStations**: Remote workstations connected via wireless modems to the network.
- **Portable WorkStation**: A workstation that is portable and communicates wirelessly.
- **HMI (Human Machine Interface)**: An interface device connected to the control logic.
- **Control Logic**: The main control logic block connected through a control network.

#### Connections and Protocols
- **Ethernet**: Directly connects servers to workstations.
- **Control Net**: Connects devices under the control logic.
- **Modems**: Facilitate wireless communication between devices.

---

### Key Features

Some of the key features of Essential Diagram are listed below:

- **Matrix Transformations**: Essential Diagram supports transformations like Translate (Move), Rotate, and Scale.
- **Shape Nodes**: Graphical objects can be drawn using tools such as RectangleTool, RoundRectTool, EllipseTool, LineTool, PolylineTool, OrthogonallineTool, BezierTool, CurveTool, ArcTool, and PolygonTool.
- **DecoratorShape**: Decorator shapes such as arrows, circles, diamonds, crosses, squares, and custom decorators can be added to connectors.

---

## API Reference

### Namespaces and Classes
- **Namespace**: EssentialDiagram
  - Provides the diagramming functionality essential for implementing graphical network flows.
  
### Methods and Properties
- **Matrix Transformations**:
  - Translate
  - Rotate
  - Scale
- **Shape Tools**:
  - RectangleTool
  - RoundRectTool
  - EllipseTool
  - LineTool
  - PolylineTool
  - OrthogonallineTool
  - BezierTool
  - CurveTool
  - ArcTool
  - PolygonTool
- **Decorator Shapes**:
  - Add shape decorators to connectors.

---

## Code Examples

```csharp
// Example for adding a new shape with custom decorators
using Syncfusion.Diagram.Controls;
using Syncfusion.Diagram.Core;

Diagrams diagram = new Diagrams();
Shape shape = new Shape();
shape.Bounds = new RectangleF(100, 100, 100, 100);
shape.DecoratorShape = DecoratorShape.Arrow;
diagram.Nodes.Add(shape);
```

---

## Figures
**Figure 1: Wireless Network flow**

This figure provides a comprehensive view of the wireless network layout, detailing how different components interact to form a cohesive network system.

---

## Cross References

See also:
- Essential Diagram documentation for specific control logic components and connectivity protocols.
- Syncfusion Winforms user guides covering advanced diagramming and network visualization features.

---

<!-- tags: [diagram, network-flow, wireless, workstations, modems, control_logic, essentialdiagram, winforms] keywords: [matrix_transformations, shape_nodes, decorator_shapes, wireless_network, control_net] -->
```