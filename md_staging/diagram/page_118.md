```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: diagram
page_number: 118
page_id: diagram#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:45Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Activates the Org line connector tool.
- Customizing nodes under the topics: Line Bridging.

## Content

### Line Bridging

#### 4.4 Customizing Nodes

This section discusses how to customize Diagram nodes, under the following topics:

##### 4.4.1 Line Bridging

Line bridging provides the visual effect such that the links jump over other links that are found in its way with lower ZOrder, thereby avoiding the links from intersecting each other and providing a hassle-free view to clearly state the various connections between the nodes. This is done by enabling the LineBridgingEnabled property. Default value is `false`.

### Code Example

```vb
'Activates the Org line connector tool.
diagram1.Controller.ActivateTool("OrgLineConnectorTool")
```

#### Figure 69: Org line Connector

![](https://via.placeholder.com/200x200?text=Org+line+Connector)

---

## API Reference

### Methods
- `ActivateTool(toolName As String)`

#### Parameters
- `toolName` - The name of the tool to be activated.

#### Returns
- No return value.

#### Exceptions
- If the specified tool does not exist.

## Code Examples

### VB.NET

```vb
' Activates the Org line connector tool.
diagram1.Controller.ActivateTool("OrgLineConnectorTool")
```

## Page-level Navigation/TOC (if applicable)
- 4.4 Customizing Nodes
  - 4.4.1 Line Bridging

## Cross References
- See also: LineBridgingEnabled property.

#### Figure: Org line Connector

![](https://via.placeholder.com/200x200?text=Org+line+Connector)

<!-- tags: [windows forms, diagram, line connector, org, line bridging, nodes customization, line bridgingenabled, tool activation] keywords: [diagram, line connector, org, line bridging, nodes, customization, line bridgingenabled, tool, activation, vb.net] -->
```