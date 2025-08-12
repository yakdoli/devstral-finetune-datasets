```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_147.jpeg
document_name: diagram
page_number: 147
page_id: diagram#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:10Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes the configuration and usage of a hierarchical layout manager in a Diagram control.
- Includes details on properties like HorizontalSpacing and VerticalSpacing.
- Provides examples in C# and VB for creating and updating the layout manager.

## Content

### Layout Manager Properties

| Property           | Description                                                                             |
|--------------------|-----------------------------------------------------------------------------------------|
| HorizontalSpacing  | Holds the value for the horizontal offset between adjacent nodes (float value).        |
| VerticalSpacing    | Holds the value for the vertical offset between adjacent nodes (float value).          |

Programmatically, the hierarchical layout manager instance should be created with the respective arguments, assigned to the Layout Manager, and updated as follows.

### Creating and Updating the Hierarchical Layout Manager

#### C# Example
```csharp
HierarchicLayoutManager hierarchyLayout = new HierarchicLayoutManager(diagram1.Model, 0, 10, 20);
this.diagram1.LayoutManager = hierarchyLayout;
this.diagram1.LayoutManager.UpdateLayout(null);
```

#### VB Example
```vb
Dim hierarchyLayout As New HierarchicLayoutManager(diagram1.Model, 0, 10, 20)
Me.diagram1.LayoutManager = hierarchyLayout
Me.diagram1.LayoutManager.UpdateLayout(Nothing)
```

### Sample Diagrams

Sample diagrams are as follows:

![Hierarchical Layout Diagram](https://via.placeholder.com/800x600?text=Hierarchical+Layout+Diagram)

---

## Page-level Navigation/TOC (if applicable)
- [unclear]

## Cross References
- See also: [unclear]

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [HierarchicLayoutManager, HorizontalSpacing, VerticalSpacing, UpdateLayout, Diagram, layout manager, hierarchical layout] -->
```