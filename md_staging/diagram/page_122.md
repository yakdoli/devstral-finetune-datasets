```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_122.jpeg
document_name: diagram
page_number: 122
page_id: diagram#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:58Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
this.diagram1.Model.LineRouter.DistanceToObstacles = 20;
this.diagram1.Model.LineRouter.RoutingMode = RoutingMode.Automatic;
```

```vb
Me.diagram1.Model.LineRouter.DistanceToObstacles = 20
Me.diagram1.Model.LineRouter.RoutingMode = RoutingMode.Automatic
```

The **LineBridgingEnabled**, **LineRoutingEnabled** properties can be set for the diagram, in which case it will be automatically applied to all the links added to the model. Else it can be enabled only for the required links individually.

## Node settings

When line routing is enabled, make sure to set the **TreatAsObstacle** property of the objects to `true`, to avoid the links running over them. If not set for an object, then that node will not be considered as an obstacle and the link will pass over it.

Programmatically it can be set as follows:

```csharp
circle.TreatAsObstacle = true;
```

```vb
circle.TreatAsObstacle = True
```

In the above code snippets, the **TreatAsObstacle** property is set to the circle object.

### 4.4.3 Grouping

A group is a node that acts as a transparent container for other nodes. A group is a composite node that controls a set of child nodes. The bounding rectangle of a group is the union of the bounds of its children. The group renders itself by iterating through its children and rendering them. Child nodes cannot be selected or manipulated individually. Members of the group are added and removed through the **ICompositeNode** interface.

The following code snippet creates a group with two nodes.

```csharp
```

``` 
© 2013 Syncfusion. All rights reserved.  
```
``` 
``` 
122 | Page  
```
``` 
``` 

<!-- tags: [WinForms, Syncfusion.Windows.Forms.Tools, Essential Diagram, LineRouting, ICompositeNode] keywords: [LineBridgingEnabled, LineRoutingEnabled, TreatAsObstacle, Obstacle, Child Nodes, ICompositeNode, Diagram, RoutingMode, Automatic] -->
``` 
