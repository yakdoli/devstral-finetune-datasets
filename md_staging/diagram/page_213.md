```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_213.jpeg
document_name: diagram
page_number: 213
page_id: diagram#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:53Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Introduction to the `Simple Flow Diagram` feature in Windows Forms.
- Demonstrates the use of the `Magnification Factor` during zooming in.

## Content

### Diagram Example
The image below illustrates a simple flow diagram with zoom-related functionality:

```markdown
### Simple Flow Diagram
- **Start**
- **Process**
- **Check**
- **End**
```

#### Magnification Factor Pop-up
A pop-up window displays magnification factors:

- **Magnification Factors:**
  - Old = 75
  - New = 50

### Figure 132: Magnification Factor while Zoom In
The figure below shows the magnification factor dialog box:

```markdown
Figure 132: Magnification Factor while Zoom In
```

### Visual Description
The flow diagram includes:
1. **Start** (Oval shape)
2. **Process** (Rectangle shape)
3. **Check** (Diamond shape)
4. **End** (Oval shape)

The pop-up window is labeled as:
- **Magnification Factors: Old = 75 New = 50**
- This dialog appears when the user zooms in on the diagram.

## API Reference

### Namespaces
- **Syncfusion.Windows.Forms.Diagram**

### Methods
- **MagnificationFactor**:
  - Updates the zoom level of the diagram.
  - Parameters:
    - **Old**: Current magnification factor.
    - **New**: Desired magnification factor.

### Events
- **ZoomChanged**:
  - Triggered when the magnification factor changes.
  - Listener should update the view or redraw elements as needed.

## Code Examples

### C# Example
Here’s an example of how to adjust the magnification factor:

```csharp
// Assume 'diagram' is the instance of your diagram control
diagram.MagnificationFactor = new MagnificationFactor(75, 50);
diagram.OnZoomChanged();
```

### VB.NET Example
```vb
' Assume 'diagram' is the instance of your diagram control
diagram.MagnificationFactor = New MagnificationFactor(75, 50)
diagram.OnZoomChanged()
```

### Tip:
Ensure that the diagram control handles the `ZoomChanged` event to update the view appropriately when the magnification factor changes.

## RAG Annotations
<!-- tags: [diagram, windows forms, magnification factor, zoom in, flow diagram] keywords: [Simple Flow Diagram, Magnification Factor, zoom, diagram control, pop-up, magnification, Windows Forms, Syncfusion] -->
```