```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_137.jpeg
document_name: diagram
page_number: 137
page_id: diagram#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:17:16Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- This page describes the usage of the Directed Tree Layout Manager in Syncfusion's Essential Diagram for Windows Forms. It covers properties such as Model, RotationAngle, HorizontalSpacing, and VerticalSpacing, along with code examples in C# and VB.
- The layout manager is used to programmatically create, assign, and update the layout for directed tree diagrams.
- Sample diagrams are also included to demonstrate the usage of the layout manager.

## Content

### Directed Tree Layout Properties
The following table outlines the key properties and their descriptions for the Directed Tree Layout Manager:

| Property          | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Model             | Represents the model of the diagram, which has to be displayed out as a directed tree. |
| RotationAngle     | Gets or sets the rotation angle for the graph. It accepts only integer values between 0-360. |
| HorizontalSpacing | Holds the value for the horizontal offset between adjacent nodes (float value). |
| VerticalSpacing   | Holds the value for the vertical offset between adjacent nodes (float value). |

### Programmatic Setup
Programmatically, the directed tree layout manager instance is created with the respective arguments, assigned to the Layout Manager, and updated as follows:

#### C# Code Example

```csharp
DirectedTreeLayoutManager directedLayout = new DirectedTreeLayoutManager(diagram1.Model, 0, 20, 20);
diagram1.LayoutManager = directedLayout;
diagram1.LayoutManager.UpdateLayout(null);
```

#### VB Code Example

```vb
DirectedTreeLayoutManager directedLayout = new DirectedTreeLayoutManager(diagram1.Model, 0, 20, 20)
diagram1.LayoutManager = directedLayout
diagram1.LayoutManager.UpdateLayout(null)
```

### Sample Diagrams
Sample Diagrams are as follows.

## Sample Diagrams
- Diagrams showcasing the Directed Tree Layout Manager in action are included below.

<!-- tags: [diagram, directed tree layout, windows forms, c#, vb, layout manager] keywords: [model, rotation angle, horizontal spacing, vertical spacing, directed tree, graph, layout, update layout, sample diagrams] -->
```