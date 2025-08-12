```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_489.jpeg
document_name: grid
page_number: 489
page_id: grid#page_489
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:44Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.1.4.17 Floating Cells

Floating cells are those cells whose content floats over empty, adjacent cells. You can enable floating cells at the grid level by setting the `GridControl.FloatCellsMode`.

Setting this property to the `GridFloatCellsMode.BeforeDisplayCalculation` will force the floating cells to always be calculated just prior to being displayed. Setting the property to the `GridFloatCellsMode.OnDemandCalculation` will calculate the floating cells only if the cell contents or size changes. This latter option is more efficient.

You can control a cell whether or not it floats over adjacent cells through the `FloatCell` property in the cell's `GridStyleInfo` object. You can also prevent a cell from being flooded by using its `GridStyleInfo.FloodCell` property. In the code given below, all three lines `(1, 3, 5)` hold the same text in column one. But, the floating cells in lines three and five are stopped short; line three by an occupied cell and line five by a `FloodCell` false settings.

```csharp
[C#]

// Enable Float Cells.
this.gridControl1.FloatCellsMode = 
GridFloatCellsMode.OnDemandCalculation;

// Specify Cell Text.
this.gridControl1[1, 1].Text = "This is a text that floats over several cells.";
this.gridControl1[3, 1].Text = "This is a text that floats over several cells.";
this.gridControl1[5, 1].Text = "This is a text that floats over several cells.";
this.gridControl1[3, 3].Text = "3.14159";

// Code to prevent cell(5,2) from being flooded.
this.gridControl1[5, 2].FloodCell = false;
```

## API Reference

### Parameters
| Name         | Type     | Description                                                                 |
|--------------|----------|-----------------------------------------------------------------------------|
| FloatCell    | Boolean  | Controls whether the cell floats over adjacent cells.                     |
| FloodCell    | Boolean  | Prevents the cell from being flooded by adjacent floating cells.           |

### Methods
- **FloatCellsMode**: Sets the mode for calculating floating cells.
  - Parameters:
    - `GridFloatCellsMode`: Specifies the calculation mode.
  - Returns: void

### Events
- **OnDemandCalculation**: Triggered when floating cells are calculated on demand.

## Code Examples

### Example: Enabling and Controlling Floating Cells

```csharp
// Enable floating cells on demand.
gridControl1.FloatCellsMode = GridFloatCellsMode.OnDemandCalculation;

// Set text for floating cells.
gridControl1[1, 1].Text = "This is a text that floats over several cells.";
gridControl1[3, 1].Text = "This is a text that floats over several cells.";

// Prevent cell (5,2) from being flooded.
gridControl1[5, 2].FloodCell = false;
```

<!-- tags: [grid, windows forms, Syncfusion] keywords: [floating cells, FloatCellsMode, GridFloatCellsMode, FloodCell, OnDemandCalculation] -->
```