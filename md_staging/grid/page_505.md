```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_505.jpeg
document_name: grid
page_number: 505
page_id: grid#page_505
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates OLE Drag-and-Drop functionality between grids in Windows Forms using Syncfusion's Essential Grid.
- Illustrates how to enable drag-and-drop operations for grids, allowing users to transfer data between them or other applications.

## Content

![Figure: OLE Drag-and-Drop](#)
*Figure 1: OLE Drag-and-Drop*

### Explanation
- The image showcases two grids (`gridControl1` and `gridControl2`) where data can be dragged and dropped between them.
- Data can also be copied or pasted between grids or other applications using OLE (Object Linking and Embedding) drag-and-drop functionality.
- The sample data in the grids provides an example of how users can manipulate data using this feature.

#### Using C#

1. **Enable Drag-and-Drop for Grids**
   The following code example enables drag-and-drop functionality for `gridControl1` and `gridControl2`.

   ```csharp
   gridControl1.AllowDrop = true;
   gridControl2.AllowDrop = true;
   ```

2. **Handle Drag-and-Drop Events**
   The event handlers for the `DragOver` event determine the effect of the drag-and-drop operation.

   ```csharp
   private void gridControl1_DragOver(object sender, DragEventArgs e)
   {
       e.Effect = DragDropEffects.Copy;
   }

   private void gridControl2_DragOver(object sender, DragEventArgs e)
   {
   }
   ```

## API Reference

### Members
- `gridControl1.AllowDrop`: A property to enable dragging and dropping onto the grid.
- `gridControl2.AllowDrop`: Similar property for another grid control.
- `DragEventArgs.Effect`: Property to set the effect of the drag-and-drop operation.

## Code Examples

### C# Example
The following code demonstrates how to enable and handle drag-and-drop operations for grid controls.

```csharp
// Enable drag-and-drop for grid control
gridControl1.AllowDrop = true;
gridControl2.AllowDrop = true;

// Handle drag-over event for gridControl1
private void gridControl1_DragOver(object sender, DragEventArgs e)
{
    e.Effect = DragDropEffects.Copy;
}

// Handle drag-over event for gridControl2
private void gridControl2_DragOver(object sender, DragEventArgs e)
{
}
```

### Explanation of Code
- `gridControl1.AllowDrop = true;`: Enables drag-and-drop functionality for `gridControl1`.
- `gridControl2.AllowDrop = true;`: Enables drag-and-drop functionality for `gridControl2`.
- `e.Effect = DragDropEffects.Copy;`: Sets the effect of the drag-and-drop operation to "Copy".

## Cross References
See also:
- Documentation on OLE Drag-and-Drop in Syncfusion's Essential Grid for Windows Forms.
- Additional examples of data manipulation and transfer between grid controls.

<!-- tags: [windows-forms, grid, drag-and-drop, synchronization, ole, clipboard, data-transfer, syncfusion] keywords: [gridcontrol, dragover, draganddrop, datamanipulation, windowsforms, usersguide] -->
```