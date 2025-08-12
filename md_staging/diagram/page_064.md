```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: diagram
page_number: 064
page_id: diagram#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:51Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Overview of pan and zoom tools in the Essential Diagram for Windows Forms.
- Describes the functionality of various tools and their corresponding code snippets.

## Pan and Zoom Tools

### Tools Overview
The following section details the tools used for interacting with the diagram, including their descriptions and code snippets for implementation.

#### Figure 35: Pan&Zoom Tool
![](./page_064_image.svg)

| Tool Name       | Description                                                                                             | Code Snippet                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Pan Tool       | Pan tool allows the user to drag the diagram and hence scroll it in any direction.                     | `diagram1.Controller.ActivateTool("PanTool");`                                                   |
| Zoom Tool       | Zoom tool allows the user to zoom the diagram with minimum and maximum magnification.                 | `diagram1.Controller.ActivateTool("ZoomTool");`                                                   |
| Magnification   | This value is used to zoom the view in and out. The x and y axes can be scaled independently. Normally, the x and y axes will have the same magnification value. | ```csharp<br>int magVal = 30;<br>diagram1.View.Magnification = magVal;<br>``` |
| ShowGrid       | This will show/hide the diagram view grid.                                                              | `Diagraml.View.Grid.Visible = true;`                                                           |
| SnapToGrid     | Specifies whether the snap to grid feature is enabled.                                                  | `Diagram1.View.Grid.SnapToGrid = true;`                                                        |
| Rulers         | Diagram control supports rulers similar to that in Microsoft Word. For details see Rulers.            | `Diagraml.ShowRulers = true;`                                                                  |

## Alignment Tool
The following screenshot illustrates the Alignment tools.

```html
<!-- tags: [Syncfusion, Windows Forms, Diagram, Pan and Zoom, Alignment, Tools, Magnification, SnapToGrid, Rulers] keywords: [Pan Tool, Zoom Tool, Magnification, ShowGrid, SnapToGrid, Rulers, Diagram control, alignment, zoom, pan, grid, UI] -->
```
```