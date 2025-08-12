<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: diagram
page_number: 174
page_id: diagram#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:26Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Layers organize graphical objects into groups that share common properties and Z-order.
- Users can add multiple layers to a model and adjust object visibility with respect to other layers.
- Layers help separate text and links from other nodes, and nodes can be assigned to multiple layers.

## Content

### Understanding Layers in Diagrams
Layers arrange graphical objects into groups that share default properties and Z-order. Users have the freedom to add any number of layers and move objects between them. Objects in a single layer are rendered with the same Z-order, allowing relative control over visibility compared to other layers. 

#### Use Case: Separating Text and Links
Layers enable grouping nodes, such as text and links, separately from other nodes. For example, nodes created for text and links can be added to their respective layers. The following code snippet demonstrates the creation of three layers and assigning them to various nodes.

#### Use Case: Grouping Nodes in Collections
Layers can group nodes in collections, allowing users to show or hide entire groups of nodes by toggling the visibility of their parent layers. A single node can be assigned to multiple layers, but it will only be visible if all its assigned layers are visible. If any layer is hidden, the node will not be drawn.

#### Implementation
Programmatically, layers can be implemented as follows:

```csharp
// Layer 1

PointF[] pts1 = { new PointF(50, 25), new PointF(75, 75), new PointF(100, 25), new PointF(125, 75), new PointF(150, 25), new PointF(175, 75), new PointF(200, 25) };
CurveNode cn = new CurveNode(pts1);
diagram1.Model.AppendChild(cn);
Layer layer1 = new Layer();
cn.Layers.Add(layer1);

// Layer 2

PointF[] pts = { new PointF(10, 100), new PointF(50, 25), new PointF(34, 78), new PointF(100, 78) };
ClosedCurveNode ccn = new ClosedCurveNode(pts);
diagram1.Model.AppendChild(ccn);
Layer layer2 = new Layer();
ccn.Layers.Add(layer2);

// Layer 3

PointF pt = new PointF(50F, 200F);
PointF pt1 = new PointF(200F, 100F);
BezierCurve bc = new BezierCurve(pt, pt1);
diagram1.Model.AppendChild(bc);
SplineNode sp = new SplineNode(new PointF(130, 200), new PointF(200, 200), new PointF(120, 40));
diagram1.Model.AppendChild(sp);
```

### Key Insights
- **Layer Assignment:** Nodes are added to specific layers to control their visibility and organization within the diagram.
- **Multiple Layer Assignments:** A single node can be assigned to multiple layers, ensuring consistent visibility across all assigned layers.
- **Programmatic Layer Creation:** Using methods like `Layer`, `CurveNode`, `ClosedCurveNode`, and others, layers can be programmatically created and assigned to nodes.

#### Cross References
- Refer to the relevant sections on `Layer`, `CurveNode`, `ClosedCurveNode`, and `BezierCurve` for more details on implementation.

<!-- tags: [Syncfusion, WinForms, Diagram, Layers, CurveNode, ClosedCurveNode, BezierCurve, SplineNode] keywords: [layers, grouping, visibility, nodes, Z-order, CurveNode, ClosedCurveNode, BezierCurve, SplineNode] -->