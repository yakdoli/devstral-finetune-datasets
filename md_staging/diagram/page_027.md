```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: diagram
page_number: 027
page_id: diagram#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:08:33Z
fidelity: lossless
-->

## Overview
- This page discusses the process of adding nodes to a model using the Diagram control in Syncfusion Winforms.
- It explains how to create predefined basic shapes and customize them using the Essential Diagram package.
- Demonstrates how to add a rectangular node to the model.

## Content

### Adding Nodes to the Model

#### Figure 12: Diagram Control Created using Code

![Figure 12: Diagram Control Created using Code](attachment:figure_12_image.png)

**3.2.1.3 Adding Nodes to the Model**

The Diagram control has a list of predefined basic shapes (nodes) which help you to draw diagrams according to your requirement. You can create your own shapes by inheriting the existing shape’s class and the Symbol Designer utility tool which is shipped with the Essential Diagram package.

The following code creates a rectangular node and adds it to the model.

#### Code Example

```csharp
[C#]
// Enable diagram rulers
diagram.ShowRulers = true;

// Create a rectangular node
```

## API Reference (if applicable)
- *Namespace*: Syncfusion.Windows.Forms.Diagram
- *Class*: Diagram
- *Properties*: 
  - ShowRulers
- *Methods*: None in this context

## Code Examples (multi-language supported)
- The example provided in this section demonstrates enabling rulers and creating a rectangular node programmatically.

## Cross References
- Refer to the Symbol Designer utility tool documentation for more information on customizing shapes.

<!-- tags: [essential-diagram, windows-forms, diagram-control, nodes, shapes, csharp] keywords: [diagram, nodes, shapes, rulers, symbol designer, custom shapes, inheritance, Essential Diagram package] -->
```