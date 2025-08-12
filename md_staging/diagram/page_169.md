```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: diagram
page_number: 169
page_id: diagram#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:27Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

The point at which the connection should be established can be easily customized by setting the Position property to one of the options. This automatically associates the link to the desired position. Offset values can be specified through OffsetX and OffsetY properties, which will be inherited when the Position is set to Custom.

## Properties and Description

| Properties | Description |
|------------|-------------|
| OffsetX    | Specifies the position which takes the x value of the node. It positions the link with respect to the x value of the node. |
| OffsetY    | Specifies the Y offset value where the link should be aligned. It positions the link with respect to the Y value of the node. |
| Position   | Specifies the position where the links should be connected to the node. Default value is Center. The options included are as follows:<br><ul><li>Center</li><li>TopLeft</li><li>TopCenter</li><li>TopRight</li><li>MiddleLeft</li><li>MiddleRight</li><li>BottomLeft</li><li>BottomCenter</li><li>BottomRight</li><li>Custom</li></ul> |

## Code Snippet for Setting Position Values

### C#

```csharp
Syncfusion.Windows.Forms.Diagram.ConnectionPoint cp = new Syncfusion.Windows.Forms.Diagram.ConnectionPoint();
cp.Position = Position.BottomLeft;
cp.OffsetX = 50;
cp.OffsetY = 10;
```

### VB

```vb
Dim cp As New Syncfusion.Windows.Forms.Diagram.ConnectionPoint()
cp.Position = Position.BottomLeft
cp.OffsetX = 50
cp.OffsetY = 10
```

### Sample Diagram

Sample diagram is as follows,

<!-- tags: [Syncfusion Winforms, Diagram, Position Property, OffsetX, OffsetY, ConnectionPoint, Center, TopLeft, TopCenter, TopRight, MiddleLeft, MiddleRight, BottomLeft, BottomCenter, BottomRight, Custom, Code Example, C#, VB] -->
```