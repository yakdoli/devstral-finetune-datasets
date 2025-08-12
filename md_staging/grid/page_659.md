```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_659.jpeg
document_name: grid
page_number: 659
page_id: grid#page_659
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains the functionality of inserting and removing rows within a grid using conditional logic based on an index counter (`icount`). The focus is on the data manipulation aspect of the grid's underlying data structure.

## Content

### Data Manipulation in Grid

The following code snippet demonstrates the process of inserting and removing rows in a grid, based on specific conditions and triggers. The functionality toggles between inserting and removing rows, controlled by the `shouldInsert` flag, which depends on the value of `icount`.

```vb
icount = icount Mod (toggleInsertRemove * 2)
shouldInsert = icount < toggleInsertRemove

If shouldInsert Then
    Dim ri As Integer = 0

    Do While ri < insertRemoveCount
        Dim recNum As Integer = 5

        Dim next_Renamed As Integer = rand.[next](100)
        Dim row As Object() = New Object()({
            "H" + ti.ToString("00000"), next_Renamed + 1, next_Renamed + 2,
            next_Renamed + 3, next_Renamed + 4, next_Renamed + 5, next_Renamed + 6,
            next_Renamed + 7, next_Renamed + 8, next_Renamed + 9, next_Renamed + 10,
            next_Renamed + 11, next_Renamed + 12, next_Renamed + 13, next_Renamed + 14,
            next_Renamed + 15, next_Renamed + 16, next_Renamed + 17,
            next_Renamed + 18, next_Renamed + 19, next_Renamed + 20
        })
        ti += 1
        Dim drow As DataRow = table.NewRow()
        drow.ItemArray = row
        table.Rows.InsertAt(drow, recNum)
        ri += 1
    Loop
Else
    Dim ri As Integer = 0

    Do While ri < insertRemoveCount
        Dim recNum As Integer = 5
        Dim rowNum As Integer = recNum + 1

        ' Underlying data structure (this could be a data table or whatever structure
        ' you use behind a virtual grid).

        If table.Rows.Count > 10 Then
            table.Rows.RemoveAt(recNum)
        End If
        ri += 1
    Loop
End If
End If

Finally
    End Try
End Sub
```

### Explanation

- **Insertion Logic**:
  - When `shouldInsert` is `True` (i.e., `icount < toggleInsertRemove`), rows are inserted into the grid.
  - The `Do While` loop iterates `insertRemoveCount` times, each iteration creating a new row with randomized data (`next_Renamed`).
  - The row data is stored in an `Object()` array, and a new `DataRow` is created.
  - This new row is then inserted into the grid at position `recNum` using `table.Rows.InsertAt`.

- **Removal Logic**:
  - When `shouldInsert` is `False`, rows are removed from the grid.
  - Similar to the insertion process, a `Do While` loop iterates `insertRemoveCount` times.
  - If the total number of rows in the grid exceeds 10, the row at position `recNum` is removed using `table.Rows.RemoveAt`.

### Benefits
- **Dynamic Row Management**: Allows for efficient and condition-based insertion and removal of rows in a grid.
- **Flexible Data Handling**: The code supports dynamic adjustments to the grid's data structure based on the application's needs.

<!-- tags: [WinForms, Grid, Insertion, Removal, DataManagement, Rows, ConditionalLogic, Essential Grid] keywords: [icount, toggleInsertRemove, shouldInsert, insertRemoveCount, rand.next, ti, table.Rows, recNum] -->
```