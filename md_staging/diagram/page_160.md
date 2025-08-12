<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_160.jpeg
document_name: diagram
page_number: 160
page_id: diagram#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:31Z
fidelity: lossless
-->

## Overview

- This page explains the use of pinpoint, rotation handles, ports, and central ports in Windows Forms.

## Content

### Ports and Connections

#### Overview

This section elaborates on the use of ports and connections.

#### Ports

- **Definition:** Port is an object used to establish a connection between the node and the link.

##### Central Port

By default, the central port for a diagram is enabled using the `EnableCentralPort` property available for the node.

| Property              | Description                  |
|-----------------------|-------------------------------|
| EnableCentralPort     | Used to enable or disable the CentralPort. |

The central port for a diagram node can be enabled by using the following code snippet:

```csharp
Ellipse ellipse = new Ellipse(100, 100, 200, 100);
ellipse.EnableCentralPort = true;
```

## Page-level Navigation/TOC (if applicable)

- **4.6.2 Ports And Connections**
  - **4.6.2.1 Ports**
    - Central Port

## Cross References

See also:

- Pinpoint and Rotation Handle
- Hide Point and Rotation Handle

<!-- tags: [syncfusion, winforms, diagram, ports, connections, central port, enablecentralport] keywords: [diagram, ports, connections, central port, enablecentralport, windows forms, code snippet] -->