<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_038.jpeg
document_name: diagram
page_number: 038
page_id: diagram#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:48Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Introduces the use of `PaletteGroupBar` in a Windows Forms application.
- Demonstrates how to configure and load palettes for the `Diagram` control.

## Content

### C# Example

```csharp
// Imports the Diagram control's namespace
using Syncfusion.Windows.Forms.Diagram.Controls;

// Creates a PaletteGroupBar instance
PaletteGroupBar paletteBar = new PaletteGroupBar();
paletteBar.Dock = DockStyle.Fill;
paletteBar.Font = new Font("Arial", 9);
paletteBar.BorderStyle = BorderStyle.None;

// Apply visual styles
paletteBar.VisualStudio = Syncfusion.Windows.Forms.VisualStyle.Office2007;
paletteBar.TextAlign = Syncfusion.Windows.Forms.Tools.ContentAlignment.Left;

// Load palettes to paletteBar
paletteBar.LoadPalette("../../../../Basic Shapes.edp");
paletteBar.LoadPalette("../../../../Flowchart Symbols.edp");

// Add paletteBar to the form
this.Controls.Add(paletteBar);
```

### VB Example

```vb
' Imports the Diagram control's namespace
Imports Syncfusion.Windows.Forms.Diagram.Controls

' Creates a PaletteGroupBar instance
Dim paletteBar As New PaletteGroupBar()
paletteBar.Dock = DockStyle.Fill
paletteBar.Font = New Font("Arial", 9)
paletteBar.BorderStyle = BorderStyle.None
```

## API Reference

### Namespace
- `Syncfusion.Windows.Forms.Diagram.Controls`

### Members
- **Properties**
  - `Dock`: Determines how the control is docked.
  - `Font`: Specifies the font used by the control.
  - `BorderStyle`: Defines the border style of the control.
  - `VisualStyle`: Sets the visual style of the control.
  - `TextAlign`: Specifies the text alignment in the control.

- **Methods**
  - `LoadPalette`: Loads a palette from a specified file.

## Code Examples

The above examples demonstrate creating and configuring a `PaletteGroupBar` control in both C# and VB, highlighting the loading of palettes and applying visual styles.

## Cross References

See also:
- Documentation on `Diagram` control in the Syncfusion WinForms SDK
- Additional resources on `PaletteGroupBar` customization

<!-- tags: [Syncfusion Winforms, Diagram, PaletteGroupBar, Visual Studio 2007, Office2007, shapes, symbols, fonts, BorderStyle] keywords: [palette, visual style, text alignment, load, configure, DockStyle, Font, control, PaletteGroupBar, Syncfusion Windows Forms] -->