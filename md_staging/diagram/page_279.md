```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_279.jpeg
document_name: diagram
page_number: 279
page_id: diagram#page_279
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:43Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

```vb
' Nearest grid point
Dim ptGridNearestPoint As PointF =
    diagram1.View.Grid.GetNearestGridPoint(ptMouse, rulerHeight)
```

### 5.20 How To Hide Handles Completely From the Nodes

We can hide the handles completely by setting the `HandleColor` and `HandleOutlineColor` properties to `'Transparent'` as follows.

#### Implementation

```csharp
[C#]
this.diagram1.View.HandleColor = Color.Transparent;
this.diagram1.View.HandleOutlineColor = Color.Transparent;
```

```vb
[VB.NET]
Me.diagram1.View.HandleColor = Color.Transparent
Me.diagram1.View.HandleOutlineColor = Color.Transparent
```

Figure 157: Illustrates Hiding Handles
![Figure 157: Illustrates Hiding Handles](https://i.imgur.com/gAMVsuL.png)

### 5.21 How To Highlight a Particular Node At Run-time

A diagram node can be highlighted at run time using the mouse move actions. Using the `Controller.GetNodeUnderMouseMove` method, we can get the corresponding node under mouse move. By changing the node's `LineStyle` and `FillStyle` effects, we can highlight the respective nodes.
```html
```