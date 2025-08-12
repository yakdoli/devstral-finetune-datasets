```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_508.jpeg
document_name: grid
page_number: 508
page_id: grid#page_508
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:54Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- The document covers specific selection modes and banner cells functionality in the Essential Grid control for Windows Forms.
- Selection of cells can be customized using `GridSelectionFlags` options or by selecting checkboxes under the Selection Modes group box.
- Examples provided for setting specific selection modes using C# and VB.NET.

### Content

#### Selection of Multiple Ranges of Cells
- **Using the Ctrl Key:**
  - Selection of multiple ranges of cells can be achieved by using `GridSelectionFlags.Multiple` or selecting the "Multiple" check box under the Selection Modes group box in the UI.
- **Extending Existing Selection:**
  - An existing selection can be extended using the `SHIFT` key or by using `GridSelectionFlags.Shift` or selecting the "Shift" check box under the Selection Modes group box.
- **Disabling Selection:**
  - Selection of cells using the `CTRL` key can be disabled by using `GridSelectionFlags.None` or selecting the "Cell" check box under the Selection Modes group box.

#### Setting Specific Selection Mode

**Specific selection modes can be set by using the following code examples:**

1. **Using C#:**
   ```csharp
   this.gridControl1.AllowSelection = GridSelectionFlags.Row;
   ```

2. **Using VB.NET:**
   ```vb
   Me.gridControl1.AllowSelection = GridSelectionFlags.Row
   ```

#### 4.1.4.25 Banner Cells

**Banner cells are multiple cells spanning a single background image.** An image to be displayed in the cell can be loaded on disk by changing the `BackgroundImage` property for a cell in the Property Grid and applying a Banner for the cell area, displaying the image. For a cell background color, a Gradient style can be set. Custom cell backgrounds can be drawn by handling the `DrawCellBackground` event. The Banner cells can also be defined through a recurring pattern by handling the `QueryBanneredRange` event.

**The following screenshot shows an example of how multiple cells span a single background image to form banner cells.**

### Screen Shot Example
*Note: The screenshot image is not included in the text content and should be referenced separately.*

### API Reference

#### Properties
- **BackgroundImage**: Used to display an image in a cell.

#### Events
- **DrawCellBackground**: Handles custom drawing of cell backgrounds.
- **QueryBanneredRange**: Used to define recurring patterns for banner cells.

### Code Examples
#### C#
```csharp
this.gridControl1.AllowSelection = GridSelectionFlags.Row;
```

#### VB.NET
```vb
Me.gridControl1.AllowSelection = GridSelectionFlags.Row
```

### RAG Annotations
<!-- tags: [Essential Grid, Selection Modes, Windows Forms, GridSelectionFlags, Banner Cells, Custom Cell Backgrounds, DrawCellBackground, QueryBanneredRange] keywords: [multi-range selection, banner cells, background image, gradient style, custom background, recurring pattern] -->
```