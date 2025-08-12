```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_185.jpeg
document_name: grid
page_number: 185
page_id: grid#page_185
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains the usage of `GridControl.ChangeCells` method for modifying cell styles in the grid using `GridStyleInfo` objects.
- It also covers the `ActivateCurrentCellBehavior` property and the `GridCellActivateAction` enumeration for controlling cell activation behavior.

## Content

### 4.1.4.2.4 The GridControl.ChangeCells Method
The GridControl.ChangeCells method is used to modify GridStyleInfo objects. This overloaded method accepts GridRangeInfo and GridStyleInfo objects. The ChangeCells method depends upon the value of the **ModifyType** parameter. The current GridStyleInfo settings are modified by using the new GridStyleInfo settings that are present in the **CellInfo** parameter, according to the value of the ModifyType parameter.

```csharp
// Apply an array of styles to the specified range in grid.
public bool ChangeCells(GridRangeInfo range, GridStyleInfo cellInfo,
    StyleModifyType modifyType);
```

```vb.net
' Apply an array of styles to the specified range in grid.
Public Function ChangeCells(range As GridRangeInfo, cellInfo As GridStyleInfo, 
    modifyType As StyleModifyType) As Boolean
```

### 4.1.4.2.5 Activating Current Cell Behavior
When moving the current cell or clicking inside a cell, you can control the current cell's activation behavior by using the `ActivateCurrentCellBehavior` property. The `GridCellActivateAction` enumeration defines when to set the focus on the cell or toggle to edit mode for the current cell.

Here is the list of options under the `GridCellActivateAction` enumeration:

- **ClickOnCell**: Setting `ActivateCurrentCellBehavior` to this option sets the cell to editing mode or sets focus on the cell after user clicks the cell.
- **DblClickOnCell**: Setting `ActivateCurrentCellBehavior` to this option sets the cell to editing mode or sets focus on the cell when user double clicks the cell.
- **None**: Setting `ActivateCurrentCellBehavior` to this option deactivates the cell, even if the user clicks it.
- **PositionCaret**: Setting `ActivateCurrentCellBehavior` to this option sets the caret to be positioned at the character where the user clicks.
- **SelectAll**: Setting `ActivateCurrentCellBehavior` to this option sets the cell to editing mode or sets focus on the cell and keeps the entire text in the cell selected whenever it becomes the current cell irrespective of the click on the cell or movement over it using arrow keys.
- **SetCurrent**: Setting `ActivateCurrentCellBehavior` to this option sets the cell to editing mode or sets focus on the cell whenever it becomes the current cell irrespective of the click on the cell or movement over it using arrow keys.

## Cross References
- [SEE ALSO] Related topics: Customizing Cell Appearance and Behavior.

<!-- tags: [syncfusion sdk, windows forms, grid control, cell activation, style modification] keywords: [GridControl, ChangeCells, ActivateCurrentCellBehavior, GridCellActivateAction, GridStyleInfo, ModifyType, CellInfo, ClickOnCell, DblClickOnCell, None, PositionCaret, SelectAll, SetCurrent] -->
```
