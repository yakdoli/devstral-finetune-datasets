```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: diagram
page_number: 153
page_id: diagram#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:12Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates the programmatic creation and assignment of an organization layout manager instance.
- Explains the code snippets in C# and VB for setting up and updating the layout manager.
- Provides an example of a top-to-bottom direction organizational chart layout.

## Content

### Setting Up the Organization Layout Manager

Programmatically, the organization layout manager instance should be created with the respective arguments, assigned to the Layout Manager, and updated as follows.

#### C# Code Example
```csharp
OrgChartLayoutManager manager = new OrgChartLayoutManager(this.diagram.Model, RotateDirection.TopToBottom, 20, 50);
this.diagram1.LayoutManager = manager;
this.diagram1.LayoutManager.UpdateLayout(null);
```

#### VB Code Example
```vb
Dim manager As New OrgChartLayoutManager(Me.diagram.Model, RotateDirection.TopToBottom, 20, 50)
Me.diagram1.LayoutManager = manager
Me.diagram1.LayoutManager.UpdateLayout(Nothing)
```

### Sample Diagram

The sample diagram illustrating the top-to-bottom direction organizational chart layout is as follows.

![Top-to-Bottom Direction Organizational Chart Layout](https://image-url-here.com)

**Figure 89: Top-to-Bottom Direction Organizational Chart Layout**

## API Reference

### Namespace: Syncfusion.Windows.Forms.Diagram.Action
- `OrgChartLayoutManager`: The class responsible for managing the layout of organizational charts.

### Methods
- `UpdateLayout(null)`: Updates the layout of the organizational chart based on the configured settings.

## Code Examples

### Implementation

The code examples provided demonstrate how to programmatically create and assign the `OrgChartLayoutManager` to a diagram. The layout is then updated to reflect changes dynamically.

### Diagram Layout Configuration
```csharp
OrgChartLayoutManager manager = new OrgChartLayoutManager(this.diagram.Model, RotateDirection.TopToBottom, 20, 50);
this.diagram1.LayoutManager = manager;
this.diagram1.LayoutManager.UpdateLayout(null);
```

### Result
The resulting organizational chart layout is displayed in Figure 89, showcasing a hierarchical structure with top-to-bottom directionality.

## Conclusion

This section provides a concise guide to implementing an organizational chart layout manager programmatically using Syncfusion Windows Forms. The top-to-bottom direction layout is visually demonstrated, and the corresponding C# and VB code snippets ensure clarity and reusability for developers.

<!-- tags: [Windows Forms, organizational chart, layout manager, top-to-bottom direction] keywords: [Syncfusion, org chart, layout, diagram, C#, VB, rotation, manager] -->
```