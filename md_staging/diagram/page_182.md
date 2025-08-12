```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_182.jpeg
document_name: diagram
page_number: 182
page_id: diagram#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:58Z
fidelity: lossless
-->

## Overview
This page discusses grouping in diagrams within Syncfusion Winforms. It covers the concept of groups as transparent containers for child nodes and explains how groups are added and manipulated using the `ICompositeNode` interface. The section includes code examples for creating a group with child nodes.

## Content

### Horizontal Ruler Property Settings
**Figure 112: Horizontal Ruler Property Settings**

The figure illustrates the use of the horizontal ruler in property settings within the diagram control. The ruler is marked with measurement units at intervals, and a yellow rectangle indicates a selected object or area with manipulation handles.

### 4.6.6 Grouping
A group is a node that acts as a transparent container for other nodes. It is a composite node that controls a set of child nodes. The bounding rectangle of a group is the union of the bounds of its children. The group renders itself by iterating through its children and rendering them. Child nodes cannot be selected or manipulated individually. Members of the group are added and removed through the `ICompositeNode` interface.

There are two ways available to add a Group in diagram control:

1. **Add the children to the group manually with the help of Group class methods.** The below code snippet creates a group with two nodes.

```csharp
[C#]
```

## API Reference (if applicable)
This section provides references to relevant APIs used in grouping within the diagram control, such as methods and interfaces like `ICompositeNode`.

## Code Examples (multi-language supported)
Example of creating a group with two nodes in C#:
```csharp
[C#]
```

## Cross References
See also: related documentation sections on node manipulation, rendering, and the use of `ICompositeNode`.

## RAG Annotations
- Tags: [Syncfusion Winforms, Diagram Control, Groups, ICompositeNode, Group Methods]
- Keywords: [Group, Child Nodes, Transparent Container, Composite Node, Bounding Rectangle, Rendering, ICompositeNode, Group Class Methods, C# Code Example]

```