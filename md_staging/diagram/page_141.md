```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: diagram
page_number: 141
page_id: diagram#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:17:30Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

The Radial Tree Layout Manager is a specialization of the Directed Tree Layout Manager that employs a circular layout algorithm for locating the diagram nodes. The RadialTreeLayoutManager arranges nodes in a circular layout, positioning the root node at the center of the graph and the child nodes in a circular fashion around the root. Sub-trees formed by the branching of child nodes are located radially around the child nodes. This arrangement results in an ever-expanding concentric arrangement with radial proximity to the root node indicating the node level in the hierarchy.

The following parameters need should be specified for the RadialTreeLayoutManager.

| Property          | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Model             | Represents the model to be attached to the Layout Manager.                |
| RotationAngle     | Defines the Graph Rotation angle. It accepts only integer values between 0-360. |
| HorizontalSpacing | Defines the horizontal offset between adjacent nodes.                      |
| VerticalSpacing   | Defines the vertical offset between adjacent nodes.                       |

Programmatically, the radial tree layout manager instance is created with the respective arguments, assigned to the Layout Manager and updated as follows:

### C#

```csharp
RadialTreeLayoutManager radialLayout = new RadialTreeLayoutManager(model1, 0, 20, 20);
this.diagram1.LayoutManager = radialLayout;
this.diagram1.LayoutManager.UpdateLayout(null);
```

### VB

```vb
Dim radialLayout As New RadialTreeLayoutManager(model1, 0, 20, 20)
Me.diagram1.LayoutManager = radialLayout
Me.diagram1.LayoutManager.UpdateLayout(Nothing)
```

Sample Diagram is as follows.

<!-- tags: [product, windows forms, radial tree layout manager, directed tree layout manager, node layout algorithm, circular layout, concentric arrangement, graph rotation angle, horizontal spacing, vertical spacing, model, c#, vb, essential diagram] keywords: [radial tree layout manager, directed tree layout manager, node layout algorithm, circular layout, concentric arrangement, graph rotation angle, horizontal spacing, vertical spacing, model, essential diagram] -->
```