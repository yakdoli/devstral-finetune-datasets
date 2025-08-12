```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_255.jpeg
document_name: diagram
page_number: 255
page_id: diagram#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:04Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the inclusion of CirclePorts in a symbol's constructor for both C# and VB.NET.
- Explains how to change the color of a LineConnector when activating the LineTool using the `LineTool` and `LineBase` classes.

## Content

### Adding Ports to a Symbol
The following code snippets show how to add CirclePorts to a symbol in both C# and VB.NET.

#### C#
```csharp
// Add these lines to MySymbol's Constructor
// Port locations
leftport = new CirclePort(new PointF(0, this.Height / 2));
rightport = new CirclePort(new PointF(this.Width, this.Height / 2));

// Append CirclePorts to MySymbol
AppendChild(leftport);
AppendChild(rightport);

// Make CenterPort visible
this.CenterPort.Visible = true;
```

#### VB.NET
```vbnet
[VB.NET]

Private leftport As CirclePort
Private rightport As CirclePort

' Add these lines to MySymbol's Constructor
' Port locations
leftport = New CirclePort(New PointF(0, Me.Height / 2))
rightport = New CirclePort(New PointF(Me.Width, Me.Height / 2))

' Append CirclePorts to MySymbol
AppendChild(leftport)
AppendChild(rightport)

' Make CenterPort visible
Me.CenterPort.Visible = True
```

### How To Change the Color Of the LineConnector When Activating the LineTool

```markdown
## 5.3 How To Change the Color Of the LineConnector When Activating the LineTool

We can change the color of the LineConnector while activating the LineTool using the `LineTool` and `LineBase` class. In the Mouse up event of the LineTool class, change the color of the link.

Refer to the following code snippet in CustomLineConnector class.
```

#### VB.NET Code Snippet
```vbnet
[C#]
```

## Page-level Navigation/TOC (if applicable)
- [unclear]

## Cross References
- Refer to the `CustomLineConnector` class for additional details on implementing the code snippet.
- See the `LineTool` and `LineBase` classes for more information on customizing the LineConnector behavior.

<!-- tags: [Syncfusion Winforms, CustomLineConnector, LineTool, LineBase, C#, VB.NET] keywords: [Diagram, CirclePorts, Color Change, LineConnector, Mouse up event, CustomLineConnector, LineTool, LineBase] -->
```