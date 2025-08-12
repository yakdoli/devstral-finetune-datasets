```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: grid
page_number: 111
page_id: grid#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:30:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Code Examples

```csharp
// Provide the col widths on demand - optional...
void GridQueryColWidth(object sender, GridRowColSizeEventArgs e)
{
    if (e.Index % 3 == 0)
    {
        e.Size = 40;
        e.Handled = true;
    }
}

// Provide covered range on demand - optional...
void GridQueryCoveredRange(object sender, GridQueryCellRangeEventArgs e)
{
    // Cover odd rows, columns 1 through 3.
    if (e.RowIndex % 2 == 1 && e.ColIndex >= 1 && e.ColIndex <= 3)
    {
        e.Range = GridRangeInfo.Cells(e.RowIndex, 1, e.RowIndex, 3);
        e.Handled = true;
    }

    // Cover column 6 with odd-even row pairs.
    if (e.RowIndex > 0 && e.ColIndex == 6)
    {
        int row = (e.RowIndex - 1) / 2 * 2 + 1;
        int col = e.ColIndex;
        e.Range = GridRangeInfo.Cells(row, col, row + 1, col);
        e.Handled = true;
    }
}
```

### [VB.NET]

```vb
Private Sub GridQueryRowHeight(ByVal sender As Object, ByVal e As _GridRowColSizeEventArgs)
    If (e.Index Mod 2) = 0 Then
        e.Size = 20
        e.Handled = True
    End If
End Sub

Private Sub GridQueryColWidth(ByVal sender As Object, ByVal e As _GridRowColSizeEventArgs)
    If ((e.Index Mod 3) = 0) Then
        e.Size = 40
    End If
End Sub
```

## API Reference

### Events
- **GridRowColSizeEventArgs**
  - **Index**: The index of the row or column.
  - **Size**: The size of the row or column.
  - **Handled**: A flag indicating whether the event has been handled.

### Methods
- **Cells**: Determines the range of cells based on the given row and column indices.

### Classes
- **GridRangeInfo**: Represents a range of cells in the grid.

## See also
- GridRowColSizeEventArgs
- GridQueryCellRangeEventArgs
- GridRangeInfo

<!-- tags: [Syncfusion, Winforms, Grid, EventHandling, Version: 11.4.0.26] keywords: [GridQueryColWidth, GridQueryCoveredRange, GridRowColSizeEventArgs, GridQueryCellRangeEventArgs, GridRangeInfo, covered range, covered rows, covered columns, row size, column size] -->
```