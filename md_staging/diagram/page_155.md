```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_155.jpeg
document_name: diagram
page_number: 155
page_id: diagram#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:38Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Introduced ability to set margins for diagrams using layout managers, except for Symmetric and Table Layout Manager.
- Improved performance of layout managers by reducing the time taken to lay out a diagram.

## Content

### Setting Margins for Diagrams

For all the Layout Managers supported by Essential Diagram, except **Symmetric and Table Layout Manager**, it is now possible to set the left and right margins for the graph that can be laid out by the layout manager. The two new properties, i.e., **TopMargin** and **LeftMargin** of the Layout Manager will set the margin for the graph using the following code snippet.

- **C#**
```csharp
OrgChartLayoutManager manager = new OrgChartLayoutManager(this.diagram.Model, RotateDirection.TopToBottom, 20, 50);
manager.LeftMargin = 50;
manager.TopMargin = 50;
```

- **VB**
```vb
Dim manager As New OrgChartLayoutManager(Me.diagram.Model, RotateDirection.TopToBottom, 20, 50)
manager.LeftMargin = 50
manager.TopMargin = 50
```

### Improving performance

The performance of most of the Essential Diagram Layout Managers is now improved to a great extent. The time taken for laying out a diagram, using a Layout Manager can now be reduced by setting the **ImprovePerformance** property to **true**.

- **C#**
```csharp
OrgChartLayoutManager manager = new OrgChartLayoutManager(this.diagram.Model, RotateDirection.TopToBottom, 20, 50);
manager.ImprovePerformance = true;
```

- **VB**
```vb
Dim manager As New OrgChartLayoutManager(Me.diagram.Model, RotateDirection.TopToBottom, 20, 50)
manager.ImprovePerformance = True
```

## API Reference (if applicable)
- Namespace: EssentialDiagram.LayoutManagers
- Class: LayoutManager
- Members:
  - **TopMargin**: Sets the top margin for the graph.
  - **LeftMargin**: Sets the left margin for the graph.
  - **ImprovePerformance**: Improves the performance of the layout manager by reducing the time taken to lay out the diagram.

## Code Examples (multi-language supported)
- The provided code snippets demonstrate how to set margins and improve performance using the **OrgChartLayoutManager** class in both C# and VB.NET.

## Page-level Navigation/TOC (if applicable)
- This page introduces new features for setting margins and improving performance in Layout Managers.

## Cross References
- Refer to the **Layout Manager** section in the main documentation for a comprehensive understanding of all available layout managers and their configurations.

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```