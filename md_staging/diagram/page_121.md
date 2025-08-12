```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: diagram
page_number: 121
page_id: diagram#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:24Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
this.diagram1.Model.LineRoutingEnabled = true;
```

```csharp
// enabling for link object
link.LineRoutingEnabled = true;
```

```vb
' enabling for model
Me.diagram1.Model.LineRoutingEnabled = True

' enabling for link object
link.LineRoutingEnabled = True.Model.LineBridgeSize = 5
```

> Note:  
> In the above code snippet, `link` refers to the instance of the `Link` node.

Only when `LineRoutingEnabled` property is set to `true`, `LineRouter` properties will be enabled.

## Distance and Routing mode settings

To customize the distance between the connectors and the obstacles, and the type of routing to use, the `LineRouter` collection property should be handled. The below properties are available for the `LineRouter` Collection property.

| Line Router Property   | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| DistanceToObstacle     | Specifies the distance from routing connector to the obstacle.             |
| RoutingMode            | Specifies the type of LineRouting engine routing mode to be used. The default value is 'Inactive'. The options include,   <br> <br> Inactive, <br> Automatic and <br> SemiAutomatic. |

Programmatically it can be set as follows.

```csharp
[C#]
```

## API Reference

### Properties
- **LineRoutingEnabled**: Enables or disables line routing for links.
- **DistanceToObstacle**: Specifies the distance from routing connector to the obstacle.
- **RoutingMode**: Specifies the type of LineRouting engine routing mode to be used. The default value is `Inactive`. The options include:
  - `Inactive`
  - `Automatic`
  - `SemiAutomatic`

## Code Examples

```csharp
// Example of enabling line routing for a link
this.diagram1.Model.LineRoutingEnabled = true;
link.LineRoutingEnabled = true;
link.LineRoutingMode = DiagramLineRoutingMode.Automatic;
```

<!-- tags: [Syncfusion, Winforms, Diagram, LineRouting, Link, DistanceToObstacle, RoutingMode] keywords: [line routing, links, obstacles, distance, automatic routing, semif-automatic routing] -->
```