<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_590.jpeg
document_name: grid
page_number: 590
page_id: grid#page_590
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:50Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Events

| Event Name      | Event Trigger                | Description                                    |
|------------------|------------------------------|------------------------------------------------|
| RowsRemoved      | Model.RowsRemoved           | Occurs when a row/rows are deleted.            |
| SelectionChanged | Model.SelectionChanged      | Occurs when current selection changes.         |
| SelectionChanged | Model.RowHeightsChanged     | Occurs when row height changes.                |

### Methods

| .Net Grid               | Essential Grid                    | Description                                                                 |
|--------------------------|------------------------------------|-----------------------------------------------------------------------------|
| ClearSelection()        | Selections.Clear()              | Clears the current selection by unselecting all selected cells.              |
| InvalidateCell()        | Model.InvalidateRange()          | Invalidates the specified cell forcing it to be repainted.                   |
| InvalidateColumn()      | Model.InvalidateRange()          | Invalidates the specified column forcing it to be repainted.                 |
| InvalidateRow           | Model.InvalidateRange()          | Invalidates the specified row forcing it to be repainted.                    |
| RefreshEdit             | CurrentCell.Refresh()            | Refreshes the value of the current cell.                                     |

## 4.2.2.19 Field Chooser for Grid Data Bound Grid

### Overview
- This feature enables you to customize the view of the grid without modifying the database.
- The FieldChooser class of a GridDataBoundGrid has been implemented to add or remove columns from a grid.

### Use Case Scenarios
- This feature will be useful when you want to remove certain columns (which cannot be deleted) from the grid.

### Methods

| Table 9: Methods Table |
|-------------------------|

## API Reference

### Events

- **RowsRemoved**
  - **Trigger**: Model.RowsRemoved
  - **Description**: Occurs when a row/rows are deleted.
  
- **SelectionChanged**
  - **Trigger**: Model.SelectionChanged
  - **Description**: Occurs when the current selection changes.
  
- **SelectionChanged**
  - **Trigger**: Model.RowHeightsChanged
  - **Description**: Occurs when the row height changes.

### Methods

- **ClearSelection()**
  - **Essential Grid Equivalent**: Selections.Clear()
  - **Description**: Clears the current selection by unselecting all selected cells.

- **InvalidateCell()**
  - **Essential Grid Equivalent**: Model.InvalidateRange()
  - **Description**: Invalidates the specified cell, forcing it to be repainted.

- **InvalidateColumn()**
  - **Essential Grid Equivalent**: Model.InvalidateRange()
  - **Description**: Invalidates the specified column, forcing it to be repainted.

- **InvalidateRow**
  - **Essential Grid Equivalent**: Model.InvalidateRange()
  - **Description**: Invalidates the specified row, forcing it to be repainted.

- **RefreshEdit**
  - **Essential Grid Equivalent**: CurrentCell.Refresh()
  - **Description**: Refreshes the value of the current cell.

## Code Examples

### Example: Clear Selection in Essential Grid

```csharp
// Clear selection in Essential Grid
gridControl.Selections.Clear();
```

### Example: Invalidate Cell in Essential Grid

```csharp
// Invalidate a specific cell in Essential Grid
gridControl.Model.InvalidateRange(rowIndex, colIndex);
```

### Example: Refresh Current Cell in Essential Grid

```csharp
// Refresh the current cell in Essential Grid
gridControl.CurrentCell.Refresh();
```

## Page-level Navigation/TOC

- **4.2.2.19 Field Chooser for Grid Data Bound Grid**
  - Overview
  - Use Case Scenarios
  - Methods

## Cross References

- Refer to "[4.2.2.19 Field Chooser for Grid Data Bound Grid](#4.2.2.19-field-chooser-for-grid-data-bound-grid)" for more details.

<!-- tags: [winforms, essentialgrid, grid, events, methods, fieldchooser] keywords: [selection, grid, invalidate, refresh, rowremoved, selectionchanged, rowheightschanged] -->