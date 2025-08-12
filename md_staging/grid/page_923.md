```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_923.jpeg
document_name: grid
page_number: 923
page_id: grid#page_923
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### ListBoxSelectionCurrentCellOptions.None Enabled

- MoveCurrentCellWithMouse

    Used only with SelectionMode.MultiExtended. Moves current cell when user extends the selection with mouse. Below image well illustrates this mode. Here, the selection started with the cell {R2:C1} and is extended up to Row4 through a mouse drag that made the current cell to shift to the cell {R4:C1} by following the mouse.

#### Figure: ListBoxSelectionCurrentCellOptions: None Enabled

The figure depicts a table with the following structure:

- **Columns:** ID, losses, School, Sport, ties, wins, year.
- **Rows:** 1 to 5, where each row contains data for a basketball team.  
- The current cell is highlighted during mouse drag, shifting from {R2:C1} to {R4:C1}.

#### Figure 343: ListBoxSelectionCurrentCellOptions.MoveCurrentCellWithMouse Enabled

#### Note:

For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping Grid Options\Table Options Demo
```

#### 4.3.4.7.3 Focused Selection

Grouping Grid selection behavior can also be customized by handling appropriate events as required. Here is an example implementation that focuses the current selection onto the desired grid elements like only the Current Cell, only the entire Row that contains the current cell, only the entire column that contains the current cell or both the row and the column that contains the current cell. The focused grid element is highlighted to show the current selection.

#### Selection Options

| Name        | Description                            |
|-------------|-----------------------------------------|
| Cell Only   | Selects only the individual cells.    |
| Row Only    | Selects only the row.                 |
| Column Only | Selects only the column.              |

## API Reference

Relevant information about `ListBoxSelectionCurrentCellOptions` and its usage within the Grid component can be found in the Syncfusion documentation, particularly in the context of configuring grid element selection behaviors.

## Code Examples

This example demonstrates how to set `MoveCurrentCellWithMouse` and other selection options programmatically using C#:

```csharp
// Example: Configuring selection options
Grid.CurrentCellOptions.LBXCurrentCellOptions.MoveCurrentCellWithMouse = true;
Grid.CurrentCellOptions.LBXCurrentCellOptions.FocusedCell = CurrentCellOptions.SelectionOptions.RowOnly;
```

### Cross References

See also: [Grid.Grouping.Windows](https://www.syncfusion.com/products/windowsforms/grouping-grid) for comprehensive documentation on Grid.Grouping features.

## Page-level Navigation/TOC

- **ListBoxSelectionCurrentCellOptions.None Enabled**
    - Example use of MoveCurrentCellWithMouse
- **Focused Selection**
    - Customizing grid selection behavior
    - Highlighting focused grid elements
    - Selection Options

### RAG Annotations

<!-- tags: [grid, selection, currentcell, windowsforms, syncfusion] keywords: [selectionmode, multieextended, movewithmouse, focusedselection, grid.row, grid.column] -->
```