```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: diagram
page_number: 074
page_id: diagram#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:10Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Properties

| Property         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| TailDecorator    | Sets the Tail Decorator applied to the created node.                          |
| InAction         | Sets the distance from the start of the line to the dash pattern. It accepts Float value. |
| Name             | Sets the Name for the Tool.                                                  |
| Preceding Tool   | Gets the Preceding Tool.                                                    |

```csharp
diagram1.Controller.ActivateTool("LineLinkTool");

Tool t = diagram1.Controller.ActiveTool;
if (t is Syncfusion.Windows.Forms.Diagram.LineConnectorTool)
{
    LineConnectorTool l = (LineConnectorTool)t;
    l.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
    l.TailDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
}
```

## Orthogonal Connector Tool

### Overview

- Orthogonal Connector Tool is used to connect nodes in an orthogonal manner by providing its start point and end point.
- It creates the Orthogonal Line Shape node.
- The name of the Orthogonal Connector Tool is `OrthogonalLinkTool`.

### Properties

| Property         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| HeadDecorator    | Sets the Head Decorator applied to the created node.                         |
| TailDecorator    | Sets the Tail Decorator applied to the created node.                          |
| InAction         | Sets the distance from the start of the line to the dash pattern. It accepts Float value. |
| Name             | Sets the Name for the Tool.                                                  |
| Preceding Tool   | Gets the Preceding Tool.                                                    |

```csharp
```

### Code Example

```csharp
diagram1.Controller.ActivateTool("OrthogonalLinkTool");

Tool t = diagram1.Controller.ActiveTool;
if (t is Syncfusion.Windows.Forms.Diagram.OrthogonalLinkTool)
{
    OrthogonalLinkTool l = (OrthogonalLinkTool)t;
    l.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
    l.TailDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;
}
```

## Page-specific Notes
- The section discusses properties and usage of the LineConnectorTool and OrthogonalConnectorTool in Syncfusion Diagram for Windows Forms.
- Key points include setting decorators, additional properties like `InAction`, and tool names.
- The C# code examples demonstrate how to use these tools and modify their properties.

<!-- tags: [diagram, winforms, lineconnectortool, orthogonalconnectortool] keywords: [linelinktool, orthogonallinktool, headdecorator, taildecorator, inaction, name, precedingtool, orthogonalconnector, decoratorshape, filled45arrow] -->
```