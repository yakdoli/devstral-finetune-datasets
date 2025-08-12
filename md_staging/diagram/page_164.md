```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: diagram
page_number: 164
page_id: diagram#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:41Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### 4.6.2.2 Connection Point Properties

**Overview**
- ConnectionPoint class provides points to connect to other nodes using a connector.
- Available in different custom appearances and sizes.
- ConnectionPointType and ConnectionsLimit properties define the nature of the ports.

**Content**

The ConnectionPointType and ConnectionsLimit properties are available for the ports to define their nature.

| Property               | Description                                                                                                                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ConnectionPointType   | Specifies the type of connection to be used. The values included are as follows:<br>• IncomingOutgoing (default)<br>• Outgoing<br>• Incoming                                                                           |
| ConnectionsLimit      | Specifies the number of connections to be allowed. Default value is 10.                                                                                                                                                     |

**Code Examples**

The following code snippet demonstrates their usage.

#### C#

```csharp
Syncfusion.Windows.Forms.Diagram.ConnectionPoint cp = new Syncfusion.Windows.Forms.Diagram.ConnectionPoint();
cp.ConnectionPointType = ConnectionPointType.Incoming;
cp.ConnectionsLimit = 12;
```

#### VB

```vb
Dim cp As New Syncfusion.Windows.Forms.Diagram.ConnectionPoint()
cp.ConnectionPointType = ConnectionPointType.Incoming
cp.ConnectionsLimit = 12
```

### Appendix

This section provides additional details related to diagramming features and Syncfusion controls, maintaining consistent reference to the 11.4.0.26 version.

#### See also:
- Syncfusion Diagram Documentation
- Other WinForms Controls

<!-- tags: [Syncfusion Winforms, Diagram, ConnectionPoint, ConnectionPointType, ConnectionsLimit, C#, VB, 11.4.0.26] keywords: [ConnectionPoint, ConnectionPointType, ConnectionsLimit, Syncfusion Diagram, WinForms, Windows Forms, essential diagram, C#, VB] -->
```
