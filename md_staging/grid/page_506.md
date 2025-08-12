```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_506.jpeg
document_name: grid
page_number: 506
page_id: grid#page_506
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:01Z
fidelity: lossless
-->

## Overview
- Demonstrates handling drag-and-drop operations in a Grid control.
- Explains enabling drag-and-drop functionality using the `GridControl` class.
- Provides examples in C# and VB.NET for managing drag-over events and setting the drag effect.

## Content

### Drag-and-Drop Operations

#### C# Example
```csharp
e.Effect = DragDropEffects.Copy;
}
```

#### Using VB.NET
```vb
[VB.NET]

gridControl1.AllowDrop = True
gridControl2.AllowDrop = True

private void gridControl1_DragOver(Object sender, DragEventArgs e)
e.Effect = DragDropEffects.Copy

private void gridControl2_DragOver(Object sender, DragEventArgs e)
e.Effect = DragDropEffects.Copy
```

### 4.1.4.24 Selection Modes

Essential Grid supports different selection modes for grid cells. A specific selection behavior can be set through the `GridControl.AllowSelection` property.

The following screen shot shows a window with a list of selection modes.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms
- **Class:** GridControl
- **Properties:**
  - `AllowDrop`: Enables or disables drag-and-drop functionality.
  - `AllowSelection`: Configures the selection behavior of grid cells.

## Code Examples
- **C# Example:** Implementing drag-and-drop functionality for a Grid control.
- **VB.NET Example:** Configuring drag-over event handling for different grid controls.

## Cross References
- See also: Drag-and-Drop Handling in the Grid Control.

<!-- tags: [Syncfusion, Winforms, GridControl, DragDrop, SelectionModes, C#, VB.NET] keywords: [AllowDrop, AllowSelection, DragDropEffects, DragOver, Grid cells, selection behavior, drag-and-drop] -->
```