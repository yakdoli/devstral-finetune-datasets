```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_242.jpeg
document_name: diagram
page_number: 242
page_id: diagram#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:37Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to manage and customize the default context menu in a diagram component.
- Shows the structure of a simple flow diagram with start, check, and end nodes.
- Illustrates the code to disable the default context menu using C#.

## Content

### Simple Flow Diagram
The diagram below illustrates a basic flow with nodes labeled **START**, **CHECK**, and **END**, connected by default context menu UI elements for various actions like connecting shapes, aligning them, and modifying their properties.

![Simple Flow Diagram](#)
*Figure 149: Default Context Menu*

### Code Example: Disabling the Default Context Menu
The following C# code snippet demonstrates how to disable the default context menu in the diagram component:

```csharp
// hide default context menu
diagram1.DefaultContextMenuEnabled = false;
```

## References
- Refer to the Syncfusion documentation for more details on managing context menus in diagram components.

<!-- tags: [diagram, context menu, default context menu, windows forms, flow diagram, Syncfusion, C#] keywords: [diagram, context menu, default context menu, manage context menu, disable context menu, Windows Forms, C#, flow diagram] -->
```