```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: diagram
page_number: 075
page_id: diagram#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:21Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### DirectedLineConnector Tool

#### Overview
- **Purpose**: Connects nodes in a directed line.
- **Shape Creation**: Creates a directed line shape node.
- **Tool Name**: DirectedLineLinkTool.

#### Properties

| Property           | Description                                                                       |
|--------------------|-----------------------------------------------------------------------------------|
| HeadDecorator      | Sets the Head Decorator applied to the created node.                              |
| TailDecorator      | Sets the Tail Decorator applied to the created node.                              |
| InAction           | Sets the distance from the start of the line to the dash pattern. Accepts Float value. |
| Name               | Sets the Name for the Tool.                                                         |
| Preceding Tool     | Gets the Preceding Tool.                                                              |

#### Code Example

```csharp
diagram1.Controller.ActivateTool("DirectedLineLinkTool");
Tool t = diagram1.Controller.ActiveTool;
if (t is Syncfusion.Windows.Forms.Diagram.DirectedLineConnectorTool)
{
    DirectedLineConnectorTool l = (DirectedLineConnectorTool)t;
    l.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
    l.TailDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
}
```

### PolyLineConnector Tool

#### Summary

- **Purpose**: Describes the functionality and usage of the PolyLineConnector Tool.

<!-- tags: [syncfusion, winforms, directedlineconnectortool, polylineconnectortool, version: 11.4.0.26] keywords: [directedlineconnector, polylineconnector, decorator, decoratorshape, directedline, dashpattern, name, tool, precedence, filled45arrow, connector, tool] -->
```html
```