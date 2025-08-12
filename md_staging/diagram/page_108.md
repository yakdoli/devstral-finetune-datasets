```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: diagram
page_number: 108
page_id: diagram#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:28Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- 1-3 bullets summarizing the page scope using only visible text.
- A list of various shapes and connectors available in the Diagram control for Windows Forms.
- Instructions on creating a node (Ellipse) in the Diagram control at runtime within a Windows Form.

## Content

### Available Shapes and Connectors
- Ellipse
- SemiCircle
- CircularArc
- PolylineNode
- CurveNode
- Line
- SplineNode
- Arc
- BezierCurve
- MeasureLine
- Polyline
- OrthogonalConnector
- LineConnector
- OrthogonalLine
- Link
- PolyLineConnector

#### Creating a Node in the Diagram Control at Run Time
To create a node in the Diagram control:

1. Drag the Diagram control to the windows form.
2. Press the F7 key to open the *.cs file and enter the following code in the `Page_Load` function.

##### Code Examples

- **C#**
```csharp
private void Form1_Load(object sender, EventArgs e)
{
    Syncfusion.Windows.Forms.Diagram.Ellipse ellipse = new Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 110, 70);
    diagram1.Model.AppendChild(ellipse);
}
```

- **VB**
```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    Dim ellipse As New Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 110, 70)
    diagram1.Model.AppendChild(ellipse)
End Sub
```

## API Reference
- Namespace: `Syncfusion.Windows.Forms.Diagram`
- Class: `Ellipse`
  - Methods
    - `Ellipse(int x, int y, int width, int height)`: Constructor to create an Ellipse.
  - Properties
    - `Model`: Definition reference for adding new shape to the Diagram.

## Code Examples
- Demonstrates how to programmatically add an Ellipse node to the Diagram control using C# and VB.NET.

<!-- tags: [syncfusion, winforms, diagram, shapes, connectors, runtime, windows forms] keywords: [essential diagram, ellipse, semi circle, circular arc, polyline node, curve node, line, spline node, arc, bezier curve, measure line, orthogonal connector, line connector, orthogonal line, link, poly line connector, runtime, programmatic creation] -->
```