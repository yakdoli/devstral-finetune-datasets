```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: tools
page_number: 130
page_id: tools#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:41:35Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Tab the docked controls
- Use the docking manager to manage control docking styles (Left, Right, Top, Bottom).
- Select docking style at runtime using the context menu.

## Content

### Docking Controls Example

```vb
 ' Tab the docked controls
 Me.dockingManager.DockControl(Me.listBox1, Me.listBox2, Syncfusion.Windows.Forms.Tools.DockStyle.Left, 200, True)
```

#### Figure Caption: Controls docked to Left, Right, Top and Bottom

<figure>
  <img src="Docking_Examples.png" alt="Docking Styles" />
  <figcaption>Figure 49: Controls docked to Left, Right, Top and Bottom</figcaption>
</figure>

**At runtime, docking style can be selected easily using the context menu.**

## API Reference

### Methods

#### DockControl
- **Signature:** `DockControl(Control Control, DockStyle DockStyle, Integer Width, Boolean AllowSize)`
- **Parameters:**
  - `Control`: The control to dock.
  - `DockStyle`: The style of docking (e.g., Left, Right, Top, Bottom).
  - `Width`: Width of the docked control.
  - `AllowSize`: Whether the control can be resized.

## Code Examples

The provided VB.NET code snippet demonstrates how to use the `DockControl` method to dock a control to the left with a specified width.

## Cross References
- For more information on docking styles and their usage, refer to the Syncfusion WinForms documentation.

## RAG Annotations
<!-- tags: [windows forms, docking, controls, syncfusion] keywords: [dockcontrol, dockstyle, runtime, context menu, listbox, width, allowsize] -->
```
```