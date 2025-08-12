```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: diagram
page_number: 042
page_id: diagram#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:11:03Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## PaletteView Configuration in WinForms

### Overview
- Demonstrates the creation and configuration of a PaletteView control in Windows Forms.
- Includes setting properties such as Dock, FlatLook, BackgroundColor, and Font.
- Loads a palette from an edp file and adds the PaletteView to the form.

### Content

```csharp
// Creates a PaletteGroupView instance
PaletteGroupView paletteView = new PaletteGroupView();

// paletteView settings
paletteView.Dock = DockStyle.Fill;
paletteView.FlatLook = true;
paletteView.BackColor = Color.White;
paletteView.Font = new System.Drawing.Font("Arial", 9);

// Load palette to paletteView
paletteView.LoadPalette("..///Basic Shapes.edp");

// Add the paletteView to the form
this.Controls.Add(paletteView);
```

### [VB]

```vb
' Imports the Diagram control's namespace
Imports Syncfusion.Windows.Forms.Diagram.Controls

' Creates a PaletteGroupView instance
Dim paletteView As New PaletteGroupView()

' paletteView settings
paletteView.Dock = DockStyle.Fill
paletteView.FlatLook = True
paletteView.BackColor = Color.White
paletteView.Font = New System.Drawing.Font("Arial", 9)

' Load palette to paletteView
paletteView.LoadPalette("..///Basic Shapes.edp")

' Add the paletteView to the form
```

## API Reference

### Syncfusion.Windows.Forms.Diagram.Controls.PaletteGroupView
- **Properties:**
  - **Dock:** Determines how the control is docked within its container.
  - **FlatLook:** Indicates whether the control should have a flat appearance.
  - **BackColor:** Sets the background color of the control.
  - **Font:** Specifies the font used for rendering text in the control.

- **Methods:**
  - **LoadPalette(String path):** Loads a palette from the specified file path.

## Code Examples

### C# Example
```csharp
// Creates a PaletteGroupView instance
var paletteView = new PaletteGroupView();

// Configure paletteView settings
paletteView.Dock = DockStyle.Fill;
paletteView.FlatLook = true;
paletteView.BackColor = Color.White;
paletteView.Font = new System.Drawing.Font("Arial", 9);

// Load the palette from a file
paletteView.LoadPalette("..///Basic Shapes.edp");

// Add the PaletteView to the form
this.Controls.Add(paletteView);
```

### VB Example
```vb
' Imports the Diagram control's namespace
Imports Syncfusion.Windows.Forms.Diagram.Controls

' Creates a PaletteGroupView instance
Dim paletteView As New PaletteGroupView()

' Configure paletteView settings
paletteView.Dock = DockStyle.Fill
paletteView.FlatLook = True
paletteView.BackColor = Color.White
paletteView.Font = New System.Drawing.Font("Arial", 9)

' Load the palette from a file
paletteView.LoadPalette("..///Basic Shapes.edp")

' Add the PaletteView to the form
```

### Cross References
- See also: WinForms Designer, Control Properties, Diagramming API, Palette Management

### Notes
- Ensure that the path to the palette file is correct and accessible.
- The font specification can be adjusted based on UI requirements.

<!-- tags: [Syncfusion, WinForms, Diagramming, PaletteView, Control] keywords: [PaletteGroupView, DockStyle, FlatLook, BackgroundColor, Font, LoadPalette] -->
```