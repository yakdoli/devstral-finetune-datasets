<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_171.jpeg
document_name: diagram
page_number: 171
page_id: diagram#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:17:39Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### ConnectionPoint in Specified X & Y Offset

![Figure 106: ConnectionPoint in Specified X & Y Offset](https://i.imgur.com/anonymous.png "Figure 106: ConnectionPoint in Specified X & Y Offset")

### Reject Connections

**4.6.2.2.1 Reject Connections**

This feature allows the ConnectionPoint to discard the incoming or outgoing connections to or from that point by setting the ConnectionPointType as Reject. The prohibition sign will be shown when users attempt to connect a line connector to it.

The following code sample illustrates how to reject the incoming and outgoing connections from the ConnectionPoint:

#### C#

```csharp
ConnectionPoint port = new ConnectionPoint();
port.Position = Position.MiddleLeft;
// Sets the ConnectionPointType as Reject, which rejects the incoming and outgoing connections.
port.ConnectionPointType = ConnectionPointType.Reject;
rect1.Ports.Add(port);
```

#### VB

```vb
Dim port As New ConnectionPoint()
port.Position = Position.MiddleLeft
' Sets the ConnectionPointType as Reject, which rejects the incoming and outgoing connections.
port.ConnectionPointType = ConnectionPointType.Reject
rect1.Ports.Add(port)
```

## Page-level Navigation/TOC (if applicable)
- Essential Diagram for Windows Forms
  - ConnectionPoint in Specified X & Y Offset
  - Reject Connections
    - 4.6.2.2.1 Reject Connections

## Cross References
- See also:
  - Windows Forms

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
- Essential Diagram
- Windows Forms
- ConnectionPoint
- ConnectionPointType
- Reject
- Prohibition Sign
- Line Connector
- ConnectionPoint in Specified X & Y Offset
- Reject Connections