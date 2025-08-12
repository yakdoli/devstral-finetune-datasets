```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_163.jpeg
document_name: diagram
page_number: 163
page_id: diagram#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:17:12Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes the visual types for ports in the Essential Diagram for Windows Forms.
- Explains how to define the visual types using code snippets.
- Provides examples of different port shapes.

## Content

### VisualType
The **VisualType** property determines the visual representation of a port. The default value is `XPort`. The options included are as follows:

- **CirclePort**
- **XPort**
- **TrianglePort**
- **SquarePort**
- **RhombPort**
- **Custom**

#### Defining Visual Types
The visual types for a port can be defined using the following code snippet.

- **C#**
```csharp
port.VisualType = PortVisualType.RhombPort;
```

- **VB**
```vb
port.VisualType = PortVisualType.RhombPort
```

#### Sample Diagram
The sample diagram illustrates different port shapes as follows:

- **X Port**: A pentagonal shape with an "X" in the center.
- **Triangle**: A triangular shape.
- **Square**: A square shape with dotted edges.
- **Circle**: A circular shape with three plus signs at the cardinal points.

![Figure 97: Different Port Shapes](https://example.com/figure97_image_url)

**Figure 97: Different Port Shapes**

## API Reference
- **Namespace**: EssentialDiagram
- **Class**: Port
- **Property**:
  - **Name**: VisualType
  - **Type**: PortVisualType
  - **Description**: Defines the visual representation of the port.
  - **Default**: XPort
  - **Options**: CirclePort, XPort, TrianglePort, SquarePort, RhombPort, Custom

## Code Examples
### C#
```csharp
port.VisualType = PortVisualType.RhombPort;
```

### VB
```vb
port.VisualType = PortVisualType.RhombPort
```

## See also
- [Syncfusion Winforms Documentation](https://example.com/winforms-docs)
- [Diagram Control Overview](https://example.com/diagram-control-overview)

<!-- tags: [syncfusion, winforms, diagram, port, visualtype, version:11.4.0.26] keywords: [visual types, xport, triangleport, squareport, rhombport, custom, code snippets, diagram control, port shapes] -->
```