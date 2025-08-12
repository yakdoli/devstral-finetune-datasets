```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_662.jpeg
document_name: grid
page_number: 662
page_id: grid#page_662
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:44Z
fidelity: lossless
-->

## Overview

- Adds functionality to dynamically color cells based on the values of other cells.
- Enables or disables grouping, sorting, and filtering at runtime through event-handling mechanisms.
- Demonstrates how to programmatically adjust specific attributes of a grid control based on the state of checkboxes.

## Content

### Dynamic Coloring of Cells

The following VB.NET code snippet illustrates how to dynamically set the background color of grid cells contingent on the value of cell 1. It also ensures automatic repainting when changes occur to dependent columns.

```vb
Private Sub checkBoxColor_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles checkBoxColor.CheckedChanged
    If Me.checkBoxColor.Checked Then

        ' Callback for dynamically coloring cells.
        AddHandler gridGroupingControl1.QueryCellStyleInfo, AddressOf gridGroupingControl1_QueryCellStyleInfo

        ' The color of these cells depends on value of cell 1. If engines ListChanged handler detects a change to column 1, it should also automatically repaint the dependant columns.
        For i As Integer = 2 To 20
            gridGroupingControl1.TableDescriptor.Fields(i.ToString()).ReferencedFields = "1"
        Next i
    Else
        RemoveHandler gridGroupingControl1.QueryCellStyleInfo, AddressOf gridGroupingControl1_QueryCellStyleInfo
        gridGroupingControl1.TableDescriptor.Fields.LoadDefault()
    End If
    Me.gridGroupingControl1.Refresh()
End Sub
```

### Enabling Sorting at Runtime

The following C# example describes how to enable or disable sorting in a grid control based on the checked state of a checkbox.

```csharp
// Sorting Option.
private void checkBoxSorting_CheckedChanged(object sender, System.EventArgs e)
{
    if (this.checkBoxSorting.Checked)
    {
        gridGroupingControl1.TableDescriptor.SortedColumns.Clear();
        gridGroupingControl1.TableDescriptor.SortedColumns.Add("1");
        gridGroupingControl1.TableDescriptor.SortedColumns.Add("2");
    }
    else
    {
        gridGroupingControl1.TableDescriptor.SortedColumns.Clear();
    }
}
```

### Additional Checkboxes for Grouping, Filtering, and Other Options

In addition to the above functionality, you can add checkboxes to toggle options such as grouping, sorting, and filtering for the grid. When these checkboxes are checked or unchecked, corresponding code is triggered to enable or disable these features. For instance:

- **Grouping:** Enabling groups in the grid based on a selected column.
- **Filtering:** Applying filters to refine the visible data in the grid.

By handling the `CheckedChanged` event of three additional checkboxes, you can add or remove groups, sort records, or apply filters dynamically as per user interaction.

## API Reference

### Methods and Events Used

- **`gridGroupingControl1.QueryCellStyleInfo`**: Triggered to set the style (e.g., background color) of each cell dynamically.
- **`gridGroupingControl1.TableDescriptor.SortedColumns.Clear()`**: Clears all sorting information from the grid.
- **`gridGroupingControl1.TableDescriptor.SortedColumns.Add(columnIndex)`**: Adds the specified column index to the list of sorted columns.

### Event Handlers

- **`checkboxColor_CheckedChanged`**: Triggered when the checkbox for dynamic coloring is checked or unchecked.
- **`checkBoxSorting_CheckedChanged`**: Triggered when the checkbox for sorting functionality is checked or unchecked.

## Code Examples

### VB.NET Example for Dynamic Cell Coloring

```vb
Private Sub checkBoxColor_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles checkBoxColor.CheckedChanged
    ' ... Remainder of VB code as shown in provided snippet ...
End Sub
```

### C# Example for Sorting

```csharp
private void checkBoxSorting_CheckedChanged(object sender, System.EventArgs e)
{
    // ... Remainder of C# code as shown in provided snippet ...
}
```

## Page-level Navigation/TOC (if applicable)

- **Dynamic Coloring of Cells**
- **Enabling Sorting at Runtime**
- **Additional Checkboxes for Grouping, Filtering, etc.**

## Cross References

- [Grid Grouping Control Documentation](https://docs.syncfusion.com/windowsforms/groupingcontrol/)
- [Grid Sorting and Filtering Reference](https://docs.syncfusion.com/windowsforms/sorting-and-filtering/)

<!-- tags: [Syncfusion, WindowsForms, Grid, Grouping, Sorting, Filtering, Checkbox] keywords: [dynamic coloring, grid, checkbox, checked changed, event handling, runtime features, cell style, sorting columns] -->
```