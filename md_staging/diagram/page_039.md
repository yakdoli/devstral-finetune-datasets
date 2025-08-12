```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_039.jpeg
document_name: diagram
page_number: 039
page_id: diagram#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:09:22Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates applying visual styles to a `PaletteBar` control in a Windows Forms application.
- Combines essential shapes and flowchart symbols using `LoadPalette` methods.

## Content

### Code Example

```vb
' Apply visual styles
paletteBar.VisualStyle = Syncfusion.Windows.Forms.VisualStudio.Office2007
paletteBar.TextAlign = Syncfusion.Windows.Forms.Tools.ContentAlignment.Left

' Load palettes to paletteBar
paletteBar.LoadPalette("...//...//Basic Shapes.edp")
paletteBar.LoadPalette("...//...//Flowchart Symbols.edp")

' Add paletteBar to the form
Me.Controls.Add(paletteBar)
```

### Figure: PaletteGroupBar Control Created using Code
![Figure 17: PaletteGroupBar Control Created using Code](https://example.com/path/to/image)

## API Reference

### Namespace: Syncfusion.Windows.Forms
- **Class**: PaletteBar
  - **Properties**:
    - **VisualStyle**: Gets or sets the visual style of the control.
    - **TextAlign**: Gets or sets the text alignment of the control.

- **Methods**:
  - **LoadPalette(fileName As String)**: Loads a palette from the specified file.

## Code Examples
The code snippet demonstrates:
1. Applying an Office 2007 visual style to the `paletteBar`.
2. Aligning the text in the `paletteBar` to the left.
3. Loading two palettes: "Basic Shapes" and "Flowchart Symbols."
4. Adding the `paletteBar` to the form.

### Visual Representation
The figure shows the `PaletteGroupBar` control with:
- **Basic Shapes** group:
  - Rectangle
  - Rounded Rectangle
  - Square
  - Shadowed Box
  - Circle
  - Ellipse
- **Flowchart Symbols** group (partially visible).

## Cross References
See also:
- "Visual Styles in Syncfusion Windows Forms"
- "Loading Palettes in Diagram Controls"

## RAG Annotations
<!-- tags: [diagram, palettebar, windows-forms, visual-styles, palettes] keywords: [Syncfusion, PaletteBar, Windows Forms, visual style, align text, load palette, Basic Shapes, Flowchart Symbols, PaletteGroupBar, Office2007] -->
```