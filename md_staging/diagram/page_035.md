```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: diagram
page_number: 035
page_id: diagram#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:09:10Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to configure and connect nodes using the Essential Diagram controls in Windows Forms.
- Includes setting the head decorator styles for links and connecting nodes in the diagram.
- Provides a snippet code example for configuring a decorator and connecting nodes.

## Content

### Configuring Decorator Styles

The code snippet below shows how to configure the `HeadDecorator` for a link in the diagram.

```csharp
// Head decorator style
link.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow
link.HeadDecorator.Size = New SizeF(8, 8)
link.HeadDecorator.FillStyle.Color = Color.RosyBrown
link.HeadDecorator.LineStyle.LineColor = Color.RosyBrown

// Connect a tail node to a head node
process.CentralPort.TryConnect(link.TailEndPoint) 'process is tail node
decision.CentralPort.TryConnect(link.HeadEndPoint) 'decision is head node

// Add a link to the model
diagram.Model.AppendChild(link)
```

### Connecting Nodes

The example demonstrates connecting two nodes: a `Process` (tail node) and a `Decision` (head node) using the configured decorator style. The resulting diagram illustrates this connection.

![Figure 14: Connecting Nodes](https://example.com/figure14.png)

---

## Page-level Navigation/TOC (if applicable)
- Configuring Decorator Styles
- Connecting Nodes

## Cross References
- Refer to the documentation for more details on decorator styles and node connections.

<!-- tags: [Windows Forms, diagram, decorator, node connection, Syncfusion] keywords: [DecoratorShape, Filled45Arrow, RosyBrown, TryConnect, CentralPort] -->
```