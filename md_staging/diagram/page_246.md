```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_246.jpeg
document_name: diagram
page_number: 246
page_id: diagram#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:47Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

Following code example illustrates how to enable preview support:

### Code Example: Enabling and Showing Dragged Node Cue (C#)

```csharp
[C#]
// enable dragged node cue
paletteGroupBar1.DragNodeCueEnabled = true;
paletteGroupView1.DragNodeCueEnabled = true;

// show dragged node cue
paletteGroupBar1.ShowDragNodeCue = true;
paletteGroupView1.ShowDragNodeCue = true;
```

### Code Example: Enabling and Showing Dragged Node Cue (VB)

```vb
[VB]
' enable dragged node cue
paletteGroupBar1.DragNodeCueEnabled = True
paletteGroupView1.DragNodeCueEnabled = True

' show dragged node cue
paletteGroupBar1.ShowDragNodeCue = True
paletteGroupView1.ShowDragNodeCue = True
```

## API Reference

### Properties

- `DragNodeCueEnabled`:
  - Type: `bool`
  - Purpose: Enables or disables the dragged node cue feature.
  - Default: `false`

- `ShowDragNodeCue`:
  - Type: `bool`
  - Purpose: Controls the visibility of the dragged node cue.
  - Default: `false`

## Code Examples Explanation

These code examples demonstrate how to enable and show the dragged node cue for `paletteGroupBar1` and `paletteGroupView1` in both C# and VB.NET. By setting the `DragNodeCueEnabled` property to `true`, the dragged node cue feature is enabled. Additionally, setting the `ShowDragNodeCue` property to `true` ensures that the dragged node cue is visibly displayed during node dragging operations.

## See also

- [Syncfusion Diagram Documentation](https://help.syncfusion.com/windowsforms/diagram)

<!-- tags: [Syncfusion, WinForms, Diagram, DragNodeCue, DragNodeCueEnabled, ShowDragNodeCue] keywords: [diagram, windows forms, dragged node cue, enable, show, drag node cue, paletteGroupBar, paletteGroupView] -->
```