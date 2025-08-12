```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_161.jpeg
document_name: diagram
page_number: 161
page_id: diagram#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:45Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Demonstrates enabling the Central Port for an Ellipse node in VB.NET.
- Explains the creation and use of custom ports in a diagram node.
- Describes how to manage connections to custom ports and避开 default ports.

## Content

### Central Port

[VB]
```vb
Dim ellips As New Ellipse(100, 100, 200, 100)
ellips.EnableCentralPort = True
```

In the above code snippets, the Central Port is enabled for an Ellipse node.

**Sample diagram is as follows:**

![Central Port](https://example.com/central_port_diagram.png)
*Figure 95: Central Port*

### Custom Ports

Custom ports can be defined at any position of the diagram node, thus allowing the creation of any number of connection ports at any position on the node. All the connections can be defined from the required point or port. Unlike the default port, the custom port when set, will be visible. The **DrawPorts** property must be enabled for custom ports to be created.

### Notes

**Note:** When a link is drawn to a node or another link and when the **EnableCentralPort** is set to **True**, the links cannot be connected to the custom port. Hence make sure to disable that property for the links and the nodes to connect the links to the custom ports.

#### Property Details

| Property     | Description                                                                 |
|--------------|------------------------------------------------------------------------------|
| DrawPorts    | Specifies whether creation of custom ports is enabled. Default value is True. |


The **Syncfusion.Windows.Forms.Diagram.ConnectionPoint** class is used to create custom ports and define their properties. For details, see **ConnectionPoint Properties**.

### Code Example

The following code snippet illustrate the Custom Ports,

## API Reference

### Syncfusion.Windows.Forms.Diagram.ConnectionPoint

- **DrawPorts**: Determines whether creation of custom ports is enabled. Default value is True.

## Code Examples

### VB.NET Example
The given code snippet is an example of enabling the Central Port for an Ellipse node.

## RAG Annotations

<!-- tags: [diagram, windows forms, central port, custom ports, VB.NET, connection point, ports, properties] keywords: [enablecentralport, drawports, connectionpoint, custom ports, syncfusion windows forms, ellipse node] -->
```