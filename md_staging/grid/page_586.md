```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_586.jpeg
document_name: grid
page_number: 586
page_id: grid#page_586
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:27Z
fidelity: lossless
-->

## Overview

This page provides an intricate overview of the events that occur in the `Essential Grid for Windows Forms` control, particularly focusing on the behaviors associated with the current cell. These events encompass a wide range of activities including cell movement, activation, deactivation, editing, validation, and various input sequences.

---

## Content

### Current Cell Events

- **CurrentCellMoved**: Triggered when the current cell is moved to a new position.
- **CurrentCellMoving**: Triggered when the current cell is about to be moved to a new position.
- **CurrentCellMoveFailed**: Triggered when the current cell movement to a new position fails.
- **CurrentCellActivating**: Triggered before the grid activates a specific cell as the current cell.
- **CurrentCellActivated**: Triggered after the grid activates the specified cell as the current cell.
- **CurrentCellActivateFailed**: Triggered after the grid fails to activate a specific cell as the current cell.
- **CurrentCellDeleting**: Triggered when the user presses the Delete key on an active current cell.
- **CurrentCellStartEditing**: Triggered before the current cell switches into editing mode.
- **CurrentCellChanging**: Triggered when the user wants to modify the contents of the current cell.
- **CurrentCellChanged**: Triggered when the user changes the contents of the current cell.
- **CurrentCellDeactivating**: Triggered before the grid deactivates the current cell.
- **CurrentCellShowedDropDown**: Triggered after the drop-down is displayed.
- **CurrentCellCloseDropDown**: Triggered when the drop-down in the current cell is closed.
- **CurrentCellShowingDropDown**: Triggered when the drop-down is about to be shown.
- **CurrentCellValidating**: Triggered when the grid validates the content of the active current cell.
- **CurrentCellValidated**: Triggered when the grid successfully validates the content of the active current cell.
- **CurrentCellAcceptedChanges**: Triggered when the grid accepted changes made to the active current cell.
- **CurrentCellConfirmChangesFailed**: Triggered when the grid could not save changes made to the active current cell.
- **CurrentCellRejectedChanges**: Triggered when the grid rejects changes made to the active current cell.
- **CurrentCellEditingComplete**: Triggered when the grid completes editing mode, i.e., when the active current cell exits the editing mode.
- **CurrentCellDeactivated**: Triggered after the grid deactivates the current cell.
- **CurrentCellDeactivateFailed**: Triggered after the grid fails to deactivate the current cell.
- **CurrentCellControlGotFocus**: Triggered when the current cell has switched to in-place editing, and the control associated with the current cell has received the focus.
- **CurrentCellControlLostFocus**: Triggered when the current cell has switched to in-place editing, and the control associated with the current cell has lost the focus.
- **CurrentCellKeyPress**: Triggered before `GridCellRendererBase.OnKeyPress` is called.
- **CurrentCellKeyDown**: Triggered before `GridCellRendererBase.OnKeyDown` is called.
- **CurrentCellKeyUp**: Triggered before `GridCellRendererBase.OnKeyUp` is called.

### Mouse Related Events

- **CellButtonClicked**: Triggered when the user has clicked on a button element inside a cell renderer.
- **CellClick**: Triggered when the user clicks inside a cell.
- **CellDoubleClick**: Triggered when the user double-clicks inside a cell.
- **CellMouseDown**: Triggered before the `OnMouseDown` method of a cell's renderer is called.
- **CellMouseUp**: Triggered before the `OnMouseUp` method of a cell's renderer is called.

---

## Tags and Keywords

<!-- tags: [Essential Grid, Windows Forms, Events, Current Cell, Mouse Events] keywords: [CurrentCellMoved, CurrentCellMoving, CurrentCellMoveFailed, CurrentCellActivating, CurrentCellActivated, CurrentCellActivateFailed, CurrentCellDeleting, CurrentCellStartEditing, CurrentCellChanging, CurrentCellChanged, CurrentCellDeactivating, CurrentCellShowedDropDown, CurrentCellCloseDropDown, CurrentCellShowingDropDown, CurrentCellValidating, CurrentCellValidated, CurrentCellAcceptedChanges, CurrentCellConfirmChangesFailed, CurrentCellRejectedChanges, CurrentCellEditingComplete, CurrentCellDeactivated, CurrentCellDeactivateFailed, CurrentCellControlGotFocus, CurrentCellControlLostFocus, CurrentCellKeyPress, CurrentCellKeyDown, CurrentCellKeyUp, CellButtonClicked, CellClick, CellDoubleClick, CellMouseDown, CellMouseUp] -->
```