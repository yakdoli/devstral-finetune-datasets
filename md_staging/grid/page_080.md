```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: grid
page_number: 080
page_id: grid#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:08Z
fidelity: lossless
--> 

# Essential Grid for Windows Forms

## Overview
- This page covers the GridControl Designer, a tool for modifying grid properties.
- It explains how to select and modify ranges of cells.
- Instructions include highlighting and selecting multiple cells for property adjustments.

## Content

**Figure 46: GridControl Designer**

The GridControl Designer is a visual interface for configuring grid properties. It provides a property grid for selecting and modifying the appearance and behavior of grid elements.

### Grid Properties
- **Appearance**:
  - BackColor: Window
  - BorderStyle: None
  - Font: Tahoma, 8.25pt
  - ForeColor: ControlText
  - HighlightFrozenLine: True
  - Office2007ScrollBars: False
  - ThemesEnabled: False

- **Grid**:
  - ActivateCurrentCell: ClickOnCell
  - AllowDragSelected: False
  - AllowSelection: Any
  - AlphaBlendSelection: 64, 178, 180, 255 (Default)
  - ClickedOnDisabled: Default

### Selecting and Modifying Ranges
1. **Single Cells**: Individual cells can be modified using standard selection and editing tools.
2. **Ranges**: To modify a range of cells:
   - **Select the Range**: Click and drag to highlight a block of cells.
   - **View Properties**: Switch to the **Selected Range** tab to access the property grid for the selected range.

3. **Activation Behavior**:
   - The `ActivateCurrentCellBehavior` setting specifies how the grid reacts when the current cell is moved or clicked inside a cell. This property can be adjusted to control user interaction behavior.

## API Reference

### EssentialGrid Properties
- **ActivateCurrentCell**:
  - Type: `GridCellActivateAction`
  - Description: Specifies the behavior when moving the current cell or clicking inside a cell.
  - Values:
    - `ClickOnCell`
    - `FocusOnCell`
    - `None`
  - Default: `ClickOnCell`

### Syncfusion.Windows.Forms.Grid.GridCellActivateAction
- This enum defines the behavior of cell activation when interacting with the grid.

#### Code Example
```csharp
// Example of setting the ActivateCurrentCellBehavior
EssentialGrid grid = new EssentialGrid();
grid.ActivateCurrentCell = GridCellActivateAction.FocusOnCell;
```

## Cross References
- For more information on grid properties and their configurations, refer to the GridControl documentation.

## Page-level Navigation/TOC
- GridControl Designer
- Selecting and Modifying Ranges
- Grid Properties

<!-- tags: [Syncfusion, Winforms, GridControl, GridProperties, CellSelection, Ranges, Designer] keywords: [EssentialGrid, GridCellActivateAction, ClickOnCell, FocusOnCell, RangeSelection, PropertyGrid] -->
```