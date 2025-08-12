```html
<!--[START OF METADATA] 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_136.jpeg
document_name: diagram
page_number: 136
page_id: diagram#page_136
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:07Z
fidelity: lossless
[END OF METADATA]-->

# Essential Diagram for Windows Forms

<figure>
 <img src="image.png" alt="Vertical Orientation Diagram" />
 <figcaption>Figure 76: Vertical Orientation</figcaption>
</figure>

## 4.5.1.2 Directed Tree Layout Manager

### Overview
- Implements a layout manager for arranging nodes in a tree-like structure.
- Can be applied to any directed tree graph with a unique root and child nodes.
- Allows orientation around the root in various directions.
- Supports arrangements such as vertical, horizontal, and angular trees.

### Content

#### DirectedTreeLayoutManager Class
- Subclass of `GraphLayoutManager`.
- Layout manager for arranging nodes in a tree-like structure.
- Applicable to directed tree graphs with a unique root and child nodes.
- Enables orientation of the tree in any direction around the root.
- Supports vertical and horizontal orientations, including top-to-bottom, bottom-to-top, right-to-left, and left-to-right arrangements.

#### Graph Orientation Determination
- Orientation is determined by the rotation degree parameter during initialization.
- A rotation degree of \(0^\circ\) specifies a top-to-bottom vertical tree.
- A rotation degree of \(270^\circ\) results in a left-to-right horizontal tree layout.

#### Parameters
- The parameters for the `DirectedTreeLayoutManager` class are listed in the following table.

### API Reference
- Classes:
  - `DirectedTreeLayoutManager`
  - `GraphLayoutManager`

#### Parameters for DirectedTreeLayoutManager
| Parameter            | Type      | Description                   | Default | Required |
|----------------------|-----------|-------------------------------|---------|----------|
| rotation degree      | Degree    | Specifies the orientation.   | \(0^\circ\) | Yes     |

### Code Examples
```csharp
// Example: Creating a DirectedTreeLayoutManager with a specific rotation degree
var layoutManager = new DirectedTreeLayoutManager();
layoutManager.RotationDegree = 270; // Left-to-right horizontal tree
```

### Cross References
- See also: [Layout Managers](#layout-managers)
- [Graph Layout Management](#graph-layout-management)

<!-- tags: directed_tree_layout_manager, layout_managers, tree_graphs, graph_orientation, rotation_degree -->
```