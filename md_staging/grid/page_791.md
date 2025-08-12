```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_791.jpeg
document_name: grid
page_number: 791
page_id: grid#page_791
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

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

    For Each el As Element In Me.gridGroupingControl1.Table.DisplayElements
        If el.IsFilterBar() AndAlso Not colName Is Nothing Then
            style = gridGroupingControl1.Table.GetTableCellStyle(el, colName)
            row = style.TableCellIdentity.RowIndex
            col = style.TableCellIdentity.ColIndex
        End If
    Next el

    ' By using the calculated row and column indices, get the filter bar string of the record filter.
    Dim cr As GridTableFilterBarCellRenderer = TryCast(Me.gridGroupingControl1.TableControl.CellRenderers("FilterBarCell"), GridTableFilterBarCellRenderer)
    If Not cr Is Nothing AndAlso row <> 0 Then
        Console.WriteLine(cr.GetFilterBarText(Me.gridGroupingControl1.TableModel(row, col)))
    End If
End Sub
```

## 4.3.4.3.4.2.4 Filter By DisplayMember

Grid Grouping control filters the data records by the value member of the columns by default. This behavior can be customized to get the filters work with display member of the columns. This is accomplished in the Filter By DisplayMember feature.

### Implementation

---

© 2013 Syncfusion. All rights reserved.
- **791** | Page
<!-- tags: [Syncfusion Winforms, Grid Grouping Control, Filter BarString, RecordFilters, DisplayElements, Filter By DisplayMember] keywords: [Filter BarString, RecordFilters, DisplayElements, Filter By DisplayMember, Grid Grouping Control, Customization, Display Member] -->
```