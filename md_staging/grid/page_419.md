```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_419.jpeg
document_name: grid
page_number: 419
page_id: grid#page_419
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:57Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Example: GridQueryColWidth in VB.NET

```vb
Private Sub GridQueryColWidth(ByVal sender As Object, ByVal e As GridRowColSizeEventArgs)
    If ((e.Index Mod 3) = 0) Then
        ' Assign Column Width.
        e.Size = 40
        e.Handled = True
    End If
End Sub
```

### 4.1.4.11.2.4 QueryCoveredRange

**Overview:**
- Used to provide covered ranges on demand.
- Ideal for scenarios where a specific pattern of cell coverage is required.

### Code Example: GridQueryCoveredRange in C#

```csharp
void GridQueryCoveredRange(object sender, GridQueryCoveredRangeEventArgs e)
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

### Code Example: GridQueryCoveredRange in VB.NET

```vb
Private Sub GridQueryCoveredRange(ByVal sender As Object, ByVal e As GridQueryCoveredRangeEventArgs)
    ' Code for GridQueryCoveredRange in VB.NET
End Sub
```

## Footer

© 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, Grid, Range, Coverage] keywords: [GridQueryColWidth, GridQueryCoveredRange, Cell Coverage, Range Handling, Odd-Even Rows] -->
```