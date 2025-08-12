```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_176.jpeg
document_name: diagram
page_number: 176
page_id: diagram#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:17:20Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Explains how to manage layers in Windows Forms.
- Describes the properties and functionalities associated with adding and managing layers.
- Highlights the process of adding objects to specific layers and controlling object visibility.

## Content

### Adding Layers
Layers can be added to the model through **LayersCollectionEditor**, which can be opened by selecting the **Layers Collection** property.

| Properties | Description |
|------------|-------------|
| Enabled    | Indicates whether the layer should be active or not. Default value is `False`. |
| Name       | Indicates whether the unit should be inherited. |
| Visible    | Indicates whether the objects on the layer should be visible. |

#### Adding Objects to a Layer
- To add objects to a layer, that layer must be active. If an object is added to the model, it will be automatically added to that active layer.
- The layer can be made active only by setting the **Enabled** property of that layer.
- Objects can be added to more than one layer by setting the **Enabled** property of all the layers to which it is added.
- To add an object only to a single layer, make sure that only a single layer is enabled at a time.

#### Object Visibility
- Controls the visibility of objects on specific layers.

## API Reference

## Code Examples

## Page-level Navigation/TOC

## Cross References

See also: [Unclear]

<!-- tags: [Syncfusion Winforms, Diagram, Layers, LayersCollectionEditor, Windows Forms, Object Visibility] keywords: [Layers, LayersCollectionEditor, Enabled, Name, Visible, Object Visibility, Active Layer] -->
```