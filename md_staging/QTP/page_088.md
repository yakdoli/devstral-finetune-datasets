```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_088.jpeg
document_name: QTP
page_number: 088
page_id: QTP#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:56Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Guides you through scheduling control using essential diagrams for quick test.
- Demonstrates methods for changing node positions and connecting nodes in essential diagrams.
- Focuses on `MoveNode` method usage for node repositioning.

## Content

### 7.6 Essential Diagram

#### 7.6.1 How to change the node to a new position

**Supported method to change the node to a new position**

The `MoveNode` method is used to change the node to the new position.

**Use Case Scenarios**

This feature enables you to change the node to the new position of the chart control in QTP testing.

**Methods Table**

| Method   | Description                                       | Parameters                                       | Return Type |
|----------|---------------------------------------------------|---------------------------------------------------|-------------|
| MoveNode | Changes the node to the new position.            | public void MoveNode(string name, float offsetX, float offsetY) | void        |

**Applying MoveNode in QTP**

The following code examples illustrate how to change the node to a new position in the chart control.

```csharp
[For Diagram Control]
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").SelectNode "EllipseStart"
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").MoveNode "EllipseStart", 130.000000, 35.000000
```

#### 7.6.2 How to connect the specified nodes using connectors

**Supported method to connect the specified nodes using connectors**

(Note: Content for connecting nodes using connectors is partially visible; further information may be needed to complete this section.)

### WinForms-specific conventions
- Control manipulation in QTP using Syncfusion Winforms.
- Methods such as `MoveNode` for adjusting node positions in diagrams.

## API Reference (if applicable)

No explicit API reference is provided in the visible scope. However, the `MoveNode` method is detailed above.

## Code Examples (multi-language supported)

The code examples provided demonstrate the use of the `MoveNode` method in QTP.

```csharp
[For Diagram Control]
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").SelectNode "EllipseStart"
SwfWindow("Simple Flow Diagram").SwfObject("diagram1").MoveNode "EllipseStart", 130.000000, 35.000000
```

### Cross References

- Refer to the section on using connectors for connecting nodes, which may be detailed in subsequent pages.

## RAG Annotations

<!-- tags: [essential-diagram, qtp, node-positioning, syncfusion-winform] keywords: [MoveNode, chart control, node, diagram, QTP, test automation, version 11.4.0.26, scheduling control] -->
```