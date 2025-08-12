```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_103.jpeg
document_name: diagram
page_number: 103
page_id: diagram#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:13:11Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes functionality related to handling nodes and selection in the Diagram control.
- Explains the use of the Document Explorer for managing diagram models and nodes.
- Discusses the Property Editor for editing node properties in the Windows Forms environment.

## Content

### Handling Node Selection and Editing

```csharp
{
    Node nodeTemp = e.Node.Tag as Node;
    if (nodeTemp != null)
    {
        if (nodeTemp.Visible &&
            nodeTemp.Root.Equals(this.diagram1.Model))
        {
            diagram1.View.SelectionList.Clear();
            diagram1.View.SelectionList.Add(e.Node.Tag as Node);
        }
        else
        {
            propertyEditor.PropertyGrid.SelectedObject = nodeTemp;
        }
    }
}
```

#### Explanation:
- **Node Handling**: The code snippet demonstrates how to handle mouse events (`e`) to select and edit nodes in the Diagram control.
- **Selection Logic**: If the node is visible and its root model matches the current `diagram1.Model`, it is added to the selection list.
- **Property Editing**: If the node does not belong to the current diagram, it is selected for property editing in the `propertyEditor.PropertyGrid`.

### Document Explorer

![Document Explorer](https://placehold.it/300x200?text=Figure%2060)

#### Figure 60: Document Explorer

- The Document Explorer window provides a hierarchical view of the diagram's structure, including:
  - **Models**: The root nodes of the diagram.
  - **Nodes**: Individual elements within the diagram.
  - **Layers**: Groupings of related nodes.

### Property Editor

#### 4.1.4 Property Editor

- The Property Editor allows users to edit properties of selected nodes directly.
- It integrates with the Diagram control to dynamically update the selected node's properties.

## API Reference (if applicable)
- **Namespace**: `Syncfusion.Windows.Forms.Diagram`
- **Classes**:
  - `Node`: Represents a node in the diagram.
  - `Diagram`: The main diagram control.
  - `PropertyGrid`: Component for editing properties.

### Methods/Properties
- `View.SelectionList`: Manages the current selection of nodes in the diagram.
- `PropertyGrid.SelectedObject`: Sets the current object for property editing.

### Events
- `Node.MouseClick`: Event triggered when a mouse button is clicked over a node.

## Code Examples (multi-language supported)

```csharp
// Example: Selecting a node in the Diagram
Node selectedNode = diagram1.View.SelectionList.FirstOrDefault();
if (selectedNode != null)
{
    propertyEditor.PropertyGrid.SelectedObject = selectedNode;
}
```

## References
- Refer to the official Syncfusion documentation for more details on the Diagram control and its components.

### Cross References
- See also: Diagram Control Overview, Node Properties, PropertyGrid Integration.

<!-- tags: [Syncfusion, WindowsForms, Diagram, NodeSelection, PropertyEditor, DocumentExplorer, DiagramControl, ModelNodes, Layers, Windows Forms, WinForms, WindowsFormsDiagram, EssentialDiagram, SelectionList, PropertyGrid] keywords: [selection, editing, node, property editor, diagram, windows forms, model, layers, DocumentExplorer, PropertyGrid, NodeSelection] -->
```