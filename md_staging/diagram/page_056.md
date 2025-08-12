```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: diagram
page_number: 056
page_id: diagram#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:12Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Overview Control provides a dynamic interface for diagram management, allowing users to pan and zoom.
- PaletteGroupBar and GroupView enable users to manage and drag symbols onto diagrams.
- Property Editor displays and modifies properties of diagram objects.
- Document Explorer visualizes details of objects added to the diagram at runtime.
- DiagramDocument encapsulates model and view data for diagrams.

## Content

### 1. Overview Control

Overview Control provides a perspective view of a diagram model, and allows users to dynamically pan and zoom the diagrams. The control features a view port window that can be moved and / or resized using the mouse to modify the diagrams' origin and magnification properties at run-time. The properties of this control is discussed in the **Overview Control** topic.

### 2. Palette GroupBar and GroupView

The PaletteGroupBar control provides a way for users to drag and drop symbols onto a diagram. It is based on the Syncfusion Essential Tools GroupBar control. Each symbol palette loaded in the PaletteGroupBar occupies a panel that can be selected by a bar button. The bar button is labeled with the name of the symbol palette. The symbols in the palette are shown as icons that can be dragged and dropped onto the diagram. This control allows users to add symbols to a palette, and save or load the palette whenever necessary. It provides a way to classify and maintain symbols.

The PaletteGroupView control provides an easy way to serialize a symbol palette to and from the resource file of a form. At design-time, users can attach a symbol palette to a PaletteGroupView control in the form. Selecting the PaletteGroupView and clicking the Palette property in the Visual Studio .NET Properties window will open a standard Open File dialog, which allows the user to select a symbol palette file that has been created with the Symbol Designer.

For more details about these diagram controls, refer to the **Palette GroupBar and GroupView** topic.

### 3. Property Editor

The Property Editor in Essential Diagram displays properties of the currently selected object(s) in the diagram. It is a Windows Forms control that can be added to the Visual Studio .NET Toolbox. It also allows users to set or modify various properties of the objects or the model. The Property Editor provides an easy interface to set and view the various property settings. To know about the control's properties see **Property Editor** topic.

### 4. Document Explorer

**Document Explorer** allows you to visualize the details of the various objects that are added onto the diagram control at run-time. The layers will be listed under the **Layers** node and other objects like shapes, links, lines and text editor will be listed under **Nodes** node.

### 5. Diagram Document

The DiagramDocument is a serializable document type that encapsulates the model and view data for the diagram. The grid area of the diagram document is the diagram view object area. The nodes dragged from the PaletteGroupBar will be dropped here.

## API Reference (if applicable)

## Code Examples (if applicable)

<!-- tags: [essential-diagram, windows-forms, overview-control, palette-groupbar, groupview, property-editor, document-explorer, diagramdocument, control-properties, syncfusion-winforms, 11.4.0.26] keywords: [overview, drag-drop, symbols, palette, designer, properties, layers, nodes, serialize, diagram] -->
```