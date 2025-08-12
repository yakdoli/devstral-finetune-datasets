```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_790.jpeg
document_name: grid
page_number: 790
page_id: grid#page_790
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

To get access to the FilteredString, you can use the GetFilterBarText of the FilterBarCellRenderer. Following code example illustrates how to print the filter bar string for a given column.

## WinForms-specific Example

The following C# code demonstrates how to retrieve and print the filter bar string for a specific column in a `GridGroupingControl`.

```csharp
private void GetFilterBarString()
{
    int row = 0, col = 0;
    string colName = null;
    GridTableCellStyleInfo style;
    
    // Ensure the filter bar is visible and RecordFilters collection is not empty,
    // and get the filter bar row index and index of the field, by using the value with which
    // the grid records are filtered.
    if (gridGroupingControl1.TableDescriptor.RecordFilters.Count > 0)
        colName = gridGroupingControl1.TableDescriptor.RecordFilters[0].MappingName;
    
    foreach (Element el in this.gridGroupingControl1.Table.DisplayElements)
    {
        if (el.IsFilterBar() && colName != null)
        {
            style = gridGroupingControl1.Table.GetTableCellStyle(el, colName);
            row = style.TableCellIdentity.RowIndex;
            col = style.TableCellIdentity.ColIndex;
        }
    }
    
    // By using the calculated row and column indices, get the filter bar string of the record filter.
    GridTableFilterBarCellRenderer cr = this.gridGroupingControl1.TableControl.CellRenderers["FilterBarCell"] as GridTableFilterBarCellRenderer;
    if (cr != null && row != 0)
    {
        Console.WriteLine(cr.GetFilterBarText(this.gridGroupingControl1.TableModel[row, col]));
    }
}
```

## Code Examples

### C#

The C# example above utilizes the `GridTableFilterBarCellRenderer` to retrieve and print the filter bar string for a specific column in a grid. The example assumes the existence of a `GridGroupingControl` named `gridGroupingControl1`.

### VB.NET

To provide a similar example in VB.NET, the following code can be used:

```vb
Private Sub GetFilterBarString()
    Dim row As Integer = 0, col As Integer = 0
    Dim colName As String = Nothing
    Dim style As GridTableCellStyleInfo
    
    ' Ensure the filter bar is visible and RecordFilters collection is not empty,
    ' and get the filter bar row index and index of the field, by using the value with which
    ' the grid records are filtered.
    If gridGroupingControl1.TableDescriptor.RecordFilters.Count > 0 Then
        colName = gridGroupingControl1.TableDescriptor.RecordFilters(0).MappingName
    End If

    For Each el As Element In gridGroupingControl1.Table.DisplayElements
        If el.IsFilterBar() AndAlso colName IsNot Nothing Then
            style = gridGroupingControl1.Table.GetTableCellStyle(el, colName)
            row = style.TableCellIdentity.RowIndex
            col = style.TableCellIdentity.ColIndex
        End If
    Next

    ' By using the calculated row and column indices, get the filter bar string of the record filter.
    Dim cr As GridTableFilterBarCellRenderer = TryCast(gridGroupingControl1.TableControl.CellRenderers("FilterBarCell"), GridTableFilterBarCellRenderer)
    If cr IsNot Nothing AndAlso row <> 0 Then
        Console.WriteLine(cr.GetFilterBarText(gridGroupingControl1.TableModel(row, col)))
    End If
End Sub
```

This example mirrors the functionality of the C# example, demonstrating how to retrieve and print the filter bar string in a VB.NET context.

## API Reference

### GridTableFilterBarCellRenderer

- **Method**: `GetFilterBarText(model As SGridTableModel)`
  - **Parameters**:
    - `model`: The grid model object.
  - **Returns**: A string containing the filter bar text.

### GridGroupingControl

- **Property**: `TableDescriptor`
  - Contains the `RecordFilters` collection.

- **Property**: `TableControl`
  - Provides access to cells and their renderers.

## Cross References

See also:
- `GridTableFilterBarCellRenderer`
- `GridGroupingControl`
- `RecordFilters`
- `MappingName`

<!-- tags: [syncfusion, windows forms, grid, filter, gridgroupingcontrol, filterbarcellrenderer] keywords: [filteredstring, getfilterbartext, RecordFilters, MappingName, filter bar, filter bar string] -->
```
