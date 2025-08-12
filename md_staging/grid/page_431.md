```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_431.jpeg
document_name: grid
page_number: 431
page_id: grid#page_431
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:33Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to apply different visual styles to the Essential Grid control.
- Explains the usage of visual style settings like Office2007Blue, Office2007Black, and others.
- Shows how to programmatically set the grid's visual style using C# and VB.NET examples.

## Grid Styles
### Figure 157: Grid Styles

The figure above displays various visual styles in the `VisualStyles` group box in the UI for the Essential Grid.

### Visual Style Settings
The figure illustrates the `VisualStyles` group box, which includes options for different grid styles such as:
- Windows Vista
- Office2007Blue
- Office2007Black
- Office2007Silver
- Office2003
- SystemTheme

Each style option affects the visual appearance of the grid, cell types, and UI elements.

### Cell Appearance and Behavior
The right section of the figure highlights specific properties like:
- `CellAppearance` (Flat)
- `CellTipText` (TextBox)
- `CharacterCasing` (Normal)
- `Font` settings
- `HorizontalAlignm` (Left)
- `Interior` (Solid; Window)
- `Behavior` properties (AllowEnter, AutoSize)

These settings allow for customization of the grid's appearance and behavior.

### Setting the Visual Style
Following code example illustrates how to set the visual style for the Grid control.

#### Code Examples
```csharp
// Sets an Office 2007 Blue skin theme to the Essential Grid control.
gridControl1.GridVisualStyles =
    Syncfusion.Windows.Forms.GridVisualStyles.Office2007Blue;
```

```vb
' Sets an Office 2007 Blue skin theme to the Essential Grid control.
gridControl1.GridVisualStyles =
    Syncfusion.Windows.Forms.GridVisualStyles.Office2007Blue
```

## RAG Annotations
This section describes how to set and customize the visual styles for the Essential Grid control using both C# and VB.NET. It includes examples and explanations of the visual style properties.

<!-- tags: [winforms, grid, visual styles, essential grid] keywords: [grid styles, visual styles, office themes, customization, c#, vb.net] -->
```