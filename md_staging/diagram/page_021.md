```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: diagram
page_number: 021
page_id: diagram#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:08:37Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

The PropertyEditor control displays and edits the properties of diagram models, and nodes on the diagram. It contains an embedded PropertyGrid control which is used to edit the properties of selected objects on the diagram. A combo box is added to this control for listing out the names of objects and selecting the objects on the diagram.

Figure 8: PropertyEditor Control
![](./assets/Page_8.png)

## Overview
- The PropertyEditor control manages diagram properties and nodes.
- Includes an embedded PropertyGrid for editing properties.
- Features a combo box for object selection.

### Key Features
- **PropertyGrid**: Used to edit properties of selected objects on the diagram.
- **Combo Box**: Allows listing and selection of object names on the diagram.
- **Visualization**: Clearly displays diagram properties in a structured format.

## Content

### PropertyGrid in PropertyEditor
- Displays structured properties of diagram models.
- Allows editing of various properties such as **BackgroundImageLayout**, **BackgroundStyle**, and more.
- Includes expandable/collapsible categories for properties like **Behavior**, **Header and Footer**, and **Logical Units**.

#### Example Properties
- **BackgroundImageLayout**: Tile
- **BackgroundStyle**: {Color [White], Type}
- **LineStyle**: {Width=0,Color [Black]}
- **RenderingStyle**: {HighQuality}
- **ShadowStyle**: {False, Color [A=128]}

#### Behavior Properties
- **BoundaryConstraintsEnabled**: True

#### Header and Footer Properties
- **HeaderFooterData**: Syncfusion.Windows.

#### Layers Properties
- **Layers**: (Collection)

#### Line Routing Properties
- **BridgeStyle**: Arc
- **LineBridgeSize**: 16
- **LineBridgingEnabled**: False
- **LineRoutingEnabled**: False
- **OptimizeLineBridging**: False

#### Logical Units Properties
- **DocumentScale**: 1 px = 1 px
- **DocumentSize**: 827 px; 600 px
- **MeasurementUnits**: Pixel

#### Miscellaneous Properties
- **BottomMargin**: 0
- **EnableSelectionListSubstitute**: True
- **LineRouter**

#### LogicalSize and MinimumSize
- **LogicalSize**: 827 px; 600 px
- **MinimumSize**: 396.8504 px; 566.9291

#### Document Name
- **Name**: Model

---

### DocumentExplorer
#### Overview
The DocumentExplorer control allows users to visualize the details of the various objects added to the diagram model. The layers are listed under the **Layers** node, and other objects like shapes, links, lines, and text editors are listed under the **Nodes** node.

#### Functionality
- **Layer Management**: Layers are organized under the **Layers** node.
- **Node Management**: Shapes, links, lines, and text editors are listed under the **Nodes** node.
- **Customization**: Nodes and layers can be renamed, deleted, hidden, and new layers can be added.

## API Reference
### Key Properties and Methods
- **PropertyGrid**: Handle for editing properties.
- **Combo Box**: Control for selecting object names.
- **DocumentExplorer**: Interface for managing layers and nodes.

### Example Usage
```csharp
// Accessing PropertyGrid and DocumentExplorer
PropertyGrid pg = new PropertyGrid();
DocumentExplorer de = new DocumentExplorer();

// Populate DocumentExplorer with details
de.AddLayer("Layer1");
de.AddObject("Node1", "Shape");
de.AddObject("Node2", "Link");
```

## Code Examples
#### C# Example for PropertyGrid Usage
```csharp
using Syncfusion.Windows.Forms.Diagram.Controls;

PropertyEditor propertyEditor = new PropertyEditor();
propertyEditor.PropertyGrid.Show();
propertyEditor.PropertyGrid.AddProperty("Name", "Model");
```

#### VB.NET Example for DocumentExplorer
```vb
Imports Syncfusion.Windows.Forms.Diagram.Controls

Dim propertyEditor As PropertyEditor = New PropertyEditor()
propertyEditor.PropertyGrid.Show()
propertyEditor.PropertyGrid.AddProperty("Name", "Model")
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Diagram Control, PropertyEditor, DocumentExplorer, PropertyGrid, C# Example, VB.NET Example, Version 11.4.0.26] keywords: [PropertyGrid, DocumentExplorer, Layer Management, Node Management, Shape, Link, Line, Text Editor, PropertyEditor Control] -->
```