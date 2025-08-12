```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: diagram
page_number: 076
page_id: diagram#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:37Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Interactive tool for drawing Polyline Connector named "PolyLineLinkTool."
- Lists the properties of the PolyLine tool.
- Demonstrates how to use the PolyLineLinkTool in C# with code examples.
- Procedures for creating a diagram using Diagram Builder.

## Content

### PolyLine Tool Properties

The following table lists the properties of the PolyLine tool:

| **Property**         | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| HeadDecorator        | Sets the Head Decorator applied to the created node.                          |
| TailDecorator        | Sets the Tail Decorator applied to the created node.                          |
| InAction             | Sets the distance from the start of the line to the dash pattern. It accepts Float value. |
| Name                 | Sets the Name for the Tool.                                                   |
| Preceding Tool       | Gets the Preceding Tool.                                                     |

### Code Example: Activating and Configuring PolyLineLinkTool

Here's an example in C# for activating and configuring the PolyLineLinkTool:

```csharp
diagram1.Controller.ActivateTool("PolyLineLinkTool");
Tool t = diagram1.Controller.ActiveTool;
if (t is Syncfusion.Windows.Forms.Diagram.PolyLineConnectorTool)
{
    PolyLineConnectorTool l = (PolyLineConnectorTool)t;
    l.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
    l.TailDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
}
```

### Creating a Diagram using Diagram Builder

To create your own diagram in the diagram builder, follow these steps:

#### Procedure for Creating a Diagram

1. **Go to the File menu and click New.**  
   The new window is displayed as shown below:

   ![Screen shot of new window](image.png)

### Notes on Using the PolyLineLinkTool

- The PolyLineLinkTool is an interactive tool designed for drawing polyline connectors.
- The tool can be customized using properties such as HeadDecorator, TailDecorator, and InAction.
- The provided C# example demonstrates how to configure the tool with filled 45-degree arrowheads.

### Additional References

For more information on using the PolyLineLinkTool or creating diagrams with the Diagram Builder, refer to the Syncfusion WinForms documentation.

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Diagram
- **Class:** PolyLineConnectorTool
- **Properties:**
  - HeadDecorator: Sets the Head Decorator applied to the created node.
  - TailDecorator: Sets the Tail Decorator applied to the created node.
  - InAction: Sets the distance from the start of the line to the dash pattern. Accepts Float value.
  - Name: Sets the Name for the Tool.
  - Preceding Tool: Gets the Preceding Tool.

## Code Examples

The provided C# example demonstrates how to activate and configure the PolyLineLinkTool, specifically setting the Head and Tail Decorator shapes to filled 45-degree arrows.

<!-- tags: [syncfusion, winforms, diagram, polylinelinktool, windows forms, property, decorator] keywords: [polyline connector, head decorator, tail decorator, inaction, polyline link tool, diagram builder, syncfusion] -->
```
