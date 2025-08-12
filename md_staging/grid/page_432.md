```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_432.jpeg
document_name: grid
page_number: 432
page_id: grid#page_432
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:34Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Themes and Visual Styles

The `ThemesEnabled` property determines whether XP Themes (visual styles) can be used for this control or not, when available.

#### Code Example: Setting the Theme for Grid Control

Following code example illustrates how to set the theme for the Grid control.

```csharp
gridControl1.GridVisualStyles =
Syncfusion.Windows.Forms.GridVisualStyles.Office2007Blue
```

**C#:**
```csharp
this.gridControl1.ThemesEnabled = true;
```

**VB.NET:**
```vb
Me.gridControl1.ThemesEnabled = True
```

### 4.1.4.13.3 Grid Control Designer

#### Overview

This section elaborates upon Grid control's edit designer. Grid control has an excellent user-friendly design-time support. A Grid control's edit designer is added to the grid to ease the process of designing a Grid control on a cell level. Using the editor, the Grid can be modified, saved, and loaded to XML formatted files or to SOAP formatted templates.

#### Step-by-Step Procedure to Edit Grid Control's Cell Styles

1. **Right click the Grid control.** A context menu is displayed.
2. **Select Edit from the context menu drop-down.** The figure below illustrates this user-action:

   <!-- The figure is not specified here as it is not provided in the OCR text. -->

### API Reference

- **Namespace:** Syncfusion.Windows.Forms
- **Class:** GridControl
- **Properties:**
  - `GridVisualStyles`: Sets the visual style of the grid.
  - `ThemesEnabled`: Enables or disables the use of XP Themes for the grid.

### Code Examples

**C#:**
```csharp
gridControl1.GridVisualStyles = Syncfusion.Windows.Forms.GridVisualStyles.Office2007Blue;
gridControl1.ThemesEnabled = true;
```

**VB.NET:**
```vb
gridControl1.GridVisualStyles = Syncfusion.Windows.Forms.GridVisualStyles.Office2007Blue
gridControl1.ThemesEnabled = True
```

### RAG Annotations

<!-- tags: [Syncfusion Winforms, GridControl, ThemesEnabled, Grid Designer, Visual Styles] keywords: [grid, themes, design, visual styles, edit designer, xp themes, xml, soap, cell styles] -->
```