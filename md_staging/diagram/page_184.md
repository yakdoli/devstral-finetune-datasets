```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_184.jpeg
document_name: diagram
page_number: 184
page_id: diagram#page_184
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:17:47Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes special methods available when working with Groups in Diagram forms.
- Explains how to manage child nodes, including adding, removing, and positioning them.
- Discusses child count properties and methods to interact with Group nodes.

## Content

### Group Node Methods and Properties

If the node is a Group, the following are some special methods:

```csharp
public Node GetChild(int childIndex);
public Node GetChildByName(string childName);
public void RemoveAllChildren();
public bool RemoveChild(int childIndex);
public bool RemoveChild(Node nodeToRemove);
public void InsertChild(Node child, int childIndex);
```

Also, Group has an `int ChildCount` property, which returns the child count in a Group. To delete the first element in a Group, use the below code:

```csharp
foreach (Node node in Diagraml.Model.Nodes)
{
    if (node is Group) // Check for Group
    {
        Group groupNode = (Group)node;
        if (groupNode.ChildCount > 0) // Group has sub nodes
        {
            Node nodeToRemove = groupNode.GetChild(0);
            groupNode.RemoveChild(nodeToRemove);
        }
    }
}
```

### Group Node

![Group Node](https://i.imgur.com/EkNa2n.png)
**Figure 113: Group Node**

### Positioning nodes in Group

#### Positioning support
Diagram Group node supports absolute and relative positioning.

#### Positioning Group node’s Child

## Page-level Navigation/TOC
- 4.6.6.1 Positioning nodes in Group

## Cross References
- Refer to other sections related to Group nodes and child management in Diagrams.

<!-- tags: [diagram, group node, child node, positioning, windows forms] keywords: [child count, remove child, insert child, Group node, positioning support, absolute positioning, relative positioning] -->
```