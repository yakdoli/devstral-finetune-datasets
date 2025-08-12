```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: diagram
page_number: 120
page_id: diagram#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:12Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Code Snippets

```csharp
this.diagram1.Model.LineBridgeSize = 5;

// enabling for model
this.diagram1.Model.LineBridgingEnabled = true;

// enabling for link object
link.LineBridgingEnabled = true;

this.diagram1.Model.BridgeStyle = BridgeStyle.Square;
```

```vb
Me.diagram1.Model.LineBridgeSize = 5

' enabling for model
Me.diagram1.Model.LineBridgingEnabled = True

' enabling for link object
link.LineBridgingEnabled = True

Me.diagram1.Model.BridgeStyle = BridgeStyle.Square
```

> **Note:** In the above code snippets, `link` refers to the instance of the Link node.

### 4.4.2 Line Routing

When a link is drawn between two nodes, by enabling the `LineRoutingEnabled` property of that link and the diagram view, and if any other node is found in between them, the line will be automatically re-routed around those nodes.

#### Properties

| Property            | Description                                                                                   |
|---------------------|-----------------------------------------------------------------------------------------------|
| LineRoutingEnabled  | Specifies whether the links must be re-routed when nodes are found in the path. Default value is false. |

#### Programmatic Setup

Programmatically it can be set as follows:

```csharp
// enabling for model
```

##### API Reference

```csharp
LineRoutingEnabled
```

#### Code Examples

```csharp
this.diagram1.Model.LineRoutingEnabled = true;
```

```vb
Me.diagram1.Model.LineRoutingEnabled = True
```

### Summary

- **Line Bridging**: Configures how bridges are displayed between links.
- **Line Routing**: Automatically re-routes links around obstacles (nodes) in the path.

<!-- tags: [diagram, line bridging, line routing, windows forms, Syncfusion] keywords: [line bridge size, LineBridgingEnabled, BridgeStyle, Link node, LineRoutingEnabled, automatic re-routing] -->
```