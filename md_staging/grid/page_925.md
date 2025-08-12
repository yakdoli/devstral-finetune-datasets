```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_925.jpeg
document_name: grid
page_number: 925
page_id: grid#page_925
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:56Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Provides code snippets for customizing row, cell, and column selection highlighting in the Syncfusion Windows Forms Grid.
- Demonstrates how to apply specific styles to the highlighting, such as using `SystemColors.Highlight` for the background color.
- Includes conditional logic based on radio button selections to determine the type of highlighting (row-only, cell-only, or column-only).

## Content

### Custom Highlighting Based on Selection

The following code snippet showcases how to handle grid view style events to apply custom highlighting for rows, cells, or columns depending on user input (radio button selections).

```csharp
Syncfusion.Windows.Forms.Grid.GridPrepViewStyleInfoEventArgs e)
{
    GridCurrentCell cc = gridGroupingControl1.TableControl.CurrentCell;
    GridControlBase grid = this.gridGroupingControl1.TableControl.CurrentCell.Grid;

    // Code for RowOnly.
    if (radioButton3.Checked)
    {
        // Highlight the current row with SystemColors.Highlight and Bold font.
        if (e.RowIndex > grid.Model.Rows.HeaderCount && e.ColIndex > grid.Model.Cols.HeaderCount
            && cc.HasCurrentCellAt(e.RowIndex))
        {
            e.Style.Interior = new BrushInfo(SystemColors.Highlight);
            e.Style.TextColor = SystemColors.HighlightText;
            e.Style.Font.Bold = true;
        }
    }

    // Code for CellOnly.
    else if (radioButton2.Checked)
    {
        // Highlight the current cell with SystemColors.Highlight and Bold font.
        if (e.RowIndex > grid.Model.Rows.HeaderCount && e.ColIndex > grid.Model.Cols.HeaderCount
            && cc.HasCurrentCellAt(e.RowIndex, e.ColIndex))
        {
            e.Style.Interior = new BrushInfo(SystemColors.Highlight);
            e.Style.TextColor = SystemColors.HighlightText;
            e.Style.Font.Bold = true;
        }
    }

    // Code for ColumnOnly.
    else if (radioButton4.Checked)
    {
        // Highlight the current column with SystemColors.Highlight and Bold font.
        if (e.RowIndex > grid.Model.Rows.HeaderCount && e.ColIndex > grid.Model.Cols.HeaderCount
            && cc.ColIndex == e.ColIndex)
        {
            e.Style.Interior = new BrushInfo(SystemColors.Highlight);
            e.Style.TextColor = SystemColors.HighlightText;
        }
    }
}
```

### Explanation
- **Row Highlighting**: 
  - When `radioButton3` is checked, the current row is highlighted if the row index is greater than the header count and the column index is greater than the header count.
  - The highlighting uses `SystemColors.Highlight` for the background and bold font style.

- **Cell Highlighting**: 
  - When `radioButton2` is checked, the current cell is highlighted if the row and column indices are greater than the header counts and the cell is marked as the current cell.
  - The highlighting uses `SystemColors.Highlight` for the background and bold font style.

- **Column Highlighting**: 
  - When `radioButton4` is checked, the current column is highlighted if the row index is greater than the header count and the column index is greater than the header count.
  - The highlighting uses `SystemColors.Highlight` for the background.

### Conclusion
This example demonstrates how to conditionally apply custom styling to specific rows, cells, or columns in a grid control based on user input. The use of `SystemColors.Highlight` ensures that the highlighting is consistent with the system's theme, and the bold font enhances the visibility of the highlighted elements.

## API Reference

- **Classes and Interfaces**
  - `Syncfusion.Windows.Forms.Grid.GridPrepViewStyleInfoEventArgs`: Event arguments for the grid style preparation event.
  - `GridCurrentCell`: Represents the current cell in the grid.
  - `GridControlBase`: Base class for grid controls.

- **Properties**
  - `TableControl.CurrentCell`: Gets or sets the current cell in the table control.
  - `Model.Rows.HeaderCount`: Gets the count of header rows.
  - `Model.Cols.HeaderCount`: Gets the count of header columns.
  - `Style.Interior`: Gets or sets the background color of the style.
  - `Style.TextColor`: Gets or sets the text color of the style.
  - `Style.Font.Bold`: Gets or sets the bold property of the font.

- **Methods**
  - `HasCurrentCellAt(int rowIndex, int colIndex)`: Checks if the current cell is at the specified row and column index.

## Code Examples

### Example: Highlighting Rows, Cells, or Columns

The provided code snippet above demonstrates how to implement row, cell, and column highlighting based on user selections using radio buttons. The logic ensures that only valid rows, columns, or cells (excluding header rows and columns) are highlighted.

## Cross References

- See also: [Grid Styling Documentation](https://docs.syncfusion.com/windowsforms/)

<!-- tags: [Syncfusion, WindowsForms, Grid, Styling, Highlighting] keywords: [GridPrepViewStyleInfoEventArgs, GridCurrentCell, GridControlBase, SystemColors.Highlight, HighlightText, BoldFont] -->
```