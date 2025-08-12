```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: QTP
page_number: 089
page_id: QTP#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:07:28Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- How to connect nodes using the `ConnectNodes` method in QTP testing.
- Use of the `ResizeNode` method to adjust node size in diagram controls.

## Content

### The ConnectNodes Method

#### Overview of ConnectNodes
The `ConnectNodes` method is used to connect the specified nodes using connectors.

#### Use Case Scenarios
This feature enables you to connect the specified nodes using connectors in the chart control in QTP testing.

#### Methods Table
| Method         | Description                                      | Parameters                                                                 | Return Type |
|-----------------|--------------------------------------------------|---------------------------------------------------------------------------|--------------|
| `ConnectNodes` | Connects the specified nodes using connectors.  | `public void ConnectNodes(string startNode, string endNode, string connector)` | `void`       |

#### Applying ConnectNodes in QTP
The following code examples illustrate how to connect the specified nodes using connectors in the chart control.

##### Code Example
```csharp
[For Diagram Control]
SwfWindow("Simple Flow Diagram").SwfObject("diagram").SelectNode "EllipseStart"
SwfWindow("Simple Flow Diagram").SwfObject("diagram").ConnectNodes "RectangleProcess", "RectangleProcess", "LineConnector"
```

### 7.6.3 How to resize the node

#### Overview of Resizing Nodes
The `ResizeNode` method is used to resize the node size in diagram control.

#### Use Case Scenarios
This feature enables you to resize the node in the diagram control.

#### Methods Table
| Method       | Description                                | Parameters | Return Type |
|--------------|--------------------------------------------|------------|--------------|
| `ResizeNode` | Resizes the node size in diagram control. |            |              |

## API Reference (if applicable)
- **Namespace**: `Syncfusion.WinForms.Diagram.Controls`
- **Class**: DiagramControl
  - **Methods**:
    - `public void ConnectNodes(string startNode, string endNode, string connector)`
      - **Parameters**:
        - `startNode`: The identifier of the starting node.
        - `endNode`: The identifier of the ending node.
        - `connector`: The type of connector to use.
      - **Return Type**: `void`
    - `public void ResizeNode(SIZE size)`
      - **Parameters**:
        - `size`: The new size for the node.
      - **Return Type**: `void`

## Code Examples (multi-language supported)

#### C# Example for Connecting Nodes
```csharp
SwfWindow("Simple Flow Diagram").SwfObject("diagram").ConnectNodes("Node1", "Node2", "LineConnector");
```

#### C# Example for Resizing Nodes
```csharp
SwfWindow("Simple Flow Diagram").SwfObject("diagram").ResizeNode(new System.Drawing.Size(100, 50));
```

## RAG Annotations
<!-- tags: QTP, Syncfusion Winforms, DiagramControl, ConnectNodes, ResizeNode version: 11.4.0.26 -->
<!-- keywords: QTP, ConnectNodes, ResizeNode, node resizing, node connection, chart control, diagram control -->
```