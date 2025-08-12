```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: diagram
page_number: 073
page_id: diagram#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:21Z
fidelity: lossless
-->

## Overview
- Describes the functionality of essential diagram tools for Windows Forms.
- Highlights the use of various tools like BitmapTool, ConnectionPointTool, and Diagram Connector Tools.
- Explains the properties and usage of LineConnectorTool in detail.

## Content

| Tool Name             | Description                                                                 | Code Example                                                                |
|-----------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
|                       | double-click events. If the user double-clicks a rich text node, this tool opens a text editor allowing the user to edit the text.                                          |                                                                 |
| BitmapTool            | Interactive tool for inserting bitmaps into a diagram.                       | `diagram1.Controller.ActivateTool("BitmapTool");`                       |
| ConnectionPointTool   | The connection point tool is an interactive tool for inserting and deleting connection points on diagram nodes. You can insert a connection point by clicking the node and delete a connection point by holding CTRL and clicking the node. | `diagram1.Controller.ActivateTool("ConnectionPointTool");`              |

### Diagram Connector Tools

The following screenshot illustrates the Diagram Connector tools.

![Diagram Connector Tools](image.png)

**Figure 43: Diagram Connector Tools**

#### LineConnectorTool

Line Connector Tool is used to connect nodes in a straight line. It creates line shape nodes. The name of the LineConnectorTool is LineLinkTool.

The below table lists the properties of the tool.

### WinForms-specific conventions

#### Tools Overview
- **BitmapTool**: Allows the insertion of bitmaps into a diagram.
- **ConnectionPointTool**: Facilitates the insertion and deletion of connection points on diagram nodes.

#### LineConnectorTool Properties
- **HeadDecorator**: Sets the Head Decorator applied to the created node.

## API Reference

### Namespace: Syncfusion.Windows.Forms.Diagram

#### Classes
- **LineConnectorTool**
  - **Description**: Used to connect nodes in a straight line.

##### Properties
- **HeadDecorator**
  - **Type**: DecoratorCollection
  - **Description**: Sets the Head Decorator applied to the created node.
  - **Default**: None
  - **Required**: Yes

## Code Examples

```csharp
// Activating the BitmapTool
diagram1.Controller.ActivateTool("BitmapTool");

// Activating the ConnectionPointTool
diagram1.Controller.ActivateTool("ConnectionPointTool");

// Example usage of LineConnectorTool
LineConnectorTool lineTool = new LineConnectorTool();

// Setting the Head Decorator
lineTool.HeadDecorator = new DecoratorCollection();
lineTool.HeadDecorator.Add(new ArrowHeadDecorator());
```

## RAG Annotations

<!-- tags: [diagram, windows forms, LineConnectorTool, BitmapTool, ConnectionPointTool, ConnectorTools] keywords: [essential diagram, rich text node, text editor, interactive tool, bitmap insertion, connection points, straight line connection, Head Decorator, LineLinkTool] -->
```