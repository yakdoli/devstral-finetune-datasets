```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_112.jpeg
document_name: grid
page_number: 112
page_id: grid#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:30:47Z
fidelity: lossless
-->

## Customizing Grid Cell Coverage

### Handling Grid Events

Customizing the behavior of grid cells can be achieved by handling specific events. Below is an example demonstrating how to handle the `GridQueryCoveredRange` event to cover certain cells dynamically based on row and column conditions.

#### Code Example

```vb
Private Sub GridQueryCoveredRange(ByVal sender As Object, ByVal e As _GridQueryCellRangeEventArgs)

    ' Cover odd rows, columns 1 through 3.
    ' Cover column 6 with odd-even row pairs.
    If (((e.RowIndex Mod 2) = 1) AndAlso (e.ColIndex >= 1)) _AndAlso (e.ColIndex <= 3) Then
        e.Range = GridRangeInfo.Cells(e.RowIndex, 1, e.RowIndex, 3)
        e.Handled = True
    End If

    If ((e.RowIndex > 0) AndAlso (e.ColIndex = 6)) Then
        Dim row As Integer
        row = (((e.RowIndex - 1) / 2) * 2) + 1
        Dim col As Integer
        col = e.ColIndex
        e.Range = GridRangeInfo.Cells(row, col, (row + 1), col)
        e.Handled = True
    End If

End Sub
```

#### Explanation
- The `GridQueryCoveredRange` event is used to determine which cells in the grid should be covered.
- The logic splits the coverage conditions into two parts:
  1. Cover odd rows for columns 1 through 3.
  2. Cover column 6 with alternating (odd-even) row pairs.

### Visual Representation

The following figure illustrates a grid where column widths, row heights, and covered cells are dynamically provided based on the implemented logic.

#### Figure Description
- **Figure Caption**: Grid with Column Widths, Row Heights and Covered Cells Provided Dynamically.
- **Visual Elements**: The grid shows a dynamic layout where certain cells are highlighted, indicating they are covered based on the specified conditions. Odd rows in columns 1 to 3 are covered, and every alternate pair of rows in column 6 is also covered.

#### Illustration

![Grid with Covered Cells](image_link_here)

### Summary
This section explains how to dynamically customize the coverage of grid cells in Windows Forms using the `GridQueryCoveredRange` event. By leveraging conditions based on row and column indices, developers can enhance the appearance and functionality of the grid to meet specific requirements.

---

### References
- [Syncfusion WinForms Documentation on Grid Events](https://www.syncfusion.com/products/windowsforms)
- For complete details on event handling, refer to the [Syncfusion WinForms Grid API Reference](https://help.syncfusion.com/windowsforms/grid).

<!-- tags: grid, winforms, events, customization, cell coverage, even-odd rows, column conditions keywords: gridcustomization, eventhandling, cellcoverage, rowcolumnconditions -->
```