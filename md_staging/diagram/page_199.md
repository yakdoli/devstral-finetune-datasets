```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: diagram
page_number: 199
page_id: diagram#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:36Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
diagram1.Controller.ActivateTool("ZoomTool");
ZoomTool zoomTool = (ZoomTool)diagram1.Controller.ActiveTool;
zoomTool.MaximumMagnification = 100;
zoomTool.MinimumMagnification = 50;
zoomTool.ZoomIncrement = 10;
```

```vb
diagram1.Controller.ActivateTool("ZoomTool")
Dim zoomTool As ZoomTool = CType(diagram1.Controller.ActiveTool, ZoomTool)
zoomTool.MaximumMagnification = 100
zoomTool.MinimumMagnification = 50
zoomTool.ZoomIncrement = 10
```

### **Figure 123: ZoomTool Selection**

### **Figure 124: Zoomed in on the Selected Area**

### 4.6.7.3 Pan Support

The Pan tool allows the user to drag the diagram and hence scroll it in any direction.

Programmatically, it is implemented as follows.
```html

<!-- tags: [diagram, pan tool, zoom tool, windows forms, syncfusion, control, magnification] keywords: [pan support, zoom selection, scroll, drag, diagram, maximum magnification, minimum magnification, zoom increment] -->
```