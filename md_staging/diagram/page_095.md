```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: diagram
page_number: 095
page_id: diagram#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:12:35Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates how to integrate a palette group bar with symbol palettes in Windows Forms.
- The code shows configuration of a `paletteGroupBar` to display different symbol categories.
- Includes loading predefined palettes for "Basic Shapes" and "Electrical Symbols."

## Content

This section focuses on implementing a `paletteGroupBar` in a Windows Forms application. The objective is to create a user interface that provides access to different symbol categories in a structured manner.

### Code Example: C#
```csharp
paletteGroupBar1.Location = new System.Drawing.Point(0, 0);
paletteGroupBar1.Name = "paletteGroupBar1";
paletteGroupBar1.SelectedItem = 1;
paletteGroupBar1.Size = new System.Drawing.Size(114, 477);
paletteGroupBar1.TabIndex = 1;
paletteGroupBar1.Text = "Symbol Palette";

groupBarItem1.Client = paletteGroupView1;
groupBarItem1.Text = "Basic Shapes";
groupBarItem2.Client = paletteGroupView2;
groupBarItem2.Text = "ElectricalSymbols";
paletteGroupView1.ButtonView = true;
paletteGroupView1.Location = new System.Drawing.Point(2, 24);
paletteGroupView1.Name = "paletteGroupView1";
paletteGroupView1.Size = new System.Drawing.Size(71, 0);
paletteGroupView1.TabIndex = 0;

paletteGroupView1.Text = "paletteGroupView1";

paletteGroupView1.LoadPalette
(@"......\..\..\..\..\Common\Data\Diagram\BasicShapes.edp");

paletteGroupView2.LoadPalette
(@"......\..\..\..\..\Common\Data\Diagram\ElectricalSymbols.edp");
```

### Code Example: VB
```vb
paletteGroupBar1.AllowDrop = True
paletteGroupBar1.Controls.Add(paletteGroupView1)
paletteGroupBar1.Controls.Add(paletteGroupView2)
paletteGroupBar1.Dock = System.Windows.Forms.DockStyle.Left
paletteGroupBar1.EditMode = False
paletteGroupBar1.GroupBarItems.AddRange(New 
Syncfusion.Windows.Forms.Tools.GroupBarItem() {groupBarItem1, 
groupBarItem2})

paletteGroupBar1.Location = New System.Drawing.Point(0, 0)
paletteGroupBar1.Name = "paletteGroupBar1"
paletteGroupBar1.SelectedItem = 1
paletteGroupBar1.Size = New System.Drawing.Size(114, 477)
paletteGroupBar1.TabIndex = 1
paletteGroupBar1.Text = "Symbol Palette"
```

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: PaletteGroupBar, PaletteGroupView
- **Members**:
  - `Location`: Sets the position of the control.
  - `Name`: Provides a unique name for the control.
  - `SelectedItem`: Specifies the currently selected item in the palette group bar.
  - `Size`: Defines the dimensions of the control.
  - `TabIndex`: Indicates the tab order for the control.
  - `Text`: Displays the caption for the control.
  - `Client`: Associates a client control with a group bar item.
  - `Text`: Specifies the text displayed for each group bar item.
  - `ButtonView`: Configures display options for the palette group view.
  - `LoadPalette`: Loads a predefined palette file.

## Code Examples (multi-language)
The provided examples show how to configure a `paletteGroupBar` with two categories: "Basic Shapes" and "Electrical Symbols." These categories are loaded dynamically from external files using the `LoadPalette` method.

## Page-level Navigation/TOC (if applicable)
- This page focuses solely on the `paletteGroupBar` implementation and its properties, with no additional navigation elements.

<!-- tags: [syncfusion, windowsforms, palettegroupbar, diagram, control, version:11.4.0.26] keywords: [palette, group bar, symbol, shapes, electrical symbols, windows forms, loadpalette, configuration, controls, properties] -->
```