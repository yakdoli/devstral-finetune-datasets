```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_151.jpeg
document_name: diagram
page_number: 151
page_id: diagram#page_151
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:23Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This section provides an introduction to the Subgraph Layout Manager used in Windows Forms, focusing on enabling distinct orientations for subgraph nodes.
- Describes the implementation and functionality of the `SubgraphTreeLayoutManager` to manage layout positioning.

## Content

### 4.5.1.7 Subgraph Layout Manager

The SubgraphTreeLayoutManager enables the sub nodes of a diagram layout tree to have an orientation that is distinct from the parent node. The subgraph orientation is specified using a SubgraphPreferredLayout event that the layout manager raises before positioning each set of sub nodes in the graph.

The event of the SubgraphLayoutManager class is as follows:

| Event                     | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| SubgraphPreferredLayout   | Event that the layout manager raises before positioning each set of sub nodes in the graph. |

Programmatically, it is implemented as follows.

#### Code Implementation

##### C#
```csharp
SubgraphTreeLayoutManager st = new SubgraphTreeLayoutManager(this.diagram1.Model, 0, 20, 20);
st.SubgraphPreferredLayout += new SubgraphPreferredLayoutEventHandler(st_SubgraphPreferredLayout);
this.diagram1.LayoutManager = st;
this.diagram1.LayoutManager.UpdateLayout(null);
this.diagram1.UpdateView();

private void st_SubgraphPreferredLayout(object sender, SubgraphPreferredLayoutEventArgs evtArgs)
{
    evtArgs.ResizeSubgraphNodes = false;
    evtArgs.RotationDegree = 0;
}
```

##### VB
```vb
Dim st As New SubgraphTreeLayoutManager(Me.diagram1.Model, 0, 20, 20)
AddHandler st.SubgraphPreferredLayout, AddressOf st_SubgraphPreferredLayout
Me.diagram1.LayoutManager = st
Me.diagram1.LayoutManager.UpdateLayout(Nothing)
Me.diagram1.UpdateView()

Private Sub st_SubgraphPreferredLayout(ByVal sender As Object, ByVal evtArgs As SubgraphPreferredLayoutEventArgs)
    evtArgs.ResizeSubgraphNodes = False
End Sub
```

## Page-level Navigation/TOC (if applicable)
- This section is part of the Essential Diagram for Windows Forms documentation, focusing specifically on advanced layout management features.

## Cross References
- See also: diagrams, layout managers, orientation settings, event handling.

<!-- tags: [syncfusion, windows forms, diagram, layout manager, subgraph layout, event handling] keywords: [SubgraphTreeLayoutManager, SubgraphPreferredLayout, orientation, layout positioning, event handler, diagrams, windows forms] -->
```
