```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_802.jpeg
document_name: grid
page_number: 802
page_id: grid#page_802
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:25Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Examples

#### Parent Table

```vb
dt.Columns.Add(New DataColumn("parentID"))
dt.Columns.Add(New DataColumn("ParentName"))
dt.Columns.Add(New DataColumn("ParentDec"))

Dim i As Integer
For i = 0 To numberParentRows - 1
    Dim dr As DataRow = dt.NewRow()
    dr(0) = i
    dr(1) = String.Format("parentName{0}", i)
    dr(2) = String.Format("parentName{0}", i)
    dt.Rows.Add(dr)
Next i

Return dt
End Function
```

#### Child Table

```vb
' Create Child Table.
Private Function GetChildTable() As DataTable
    Dim dt As New DataTable("ChildTable")

    dt.Columns.Add(New DataColumn("childID"))
    dt.Columns.Add(New DataColumn("Name"))
    dt.Columns.Add(New DataColumn("ParentID"))

    Dim i As Integer
    For i = 0 To numberChildRows - 1
        Dim dr As DataRow = dt.NewRow()
        dr(0) = i.ToString()
        dr(1) = String.Format("ChildName{0}", i)
        dr(2) = (i Mod numberParentRows).ToString()
        dt.Rows.Add(dr)
    Next i

    Return dt
End Function
```

#### Grand Child Table

```vb
' Create Grand Child Table.
Private Function GetGrandChildTable() As DataTable
    Dim dt As New DataTable("GrandChildTable")

    dt.Columns.Add(New DataColumn("GrandChildID"))
    dt.Columns.Add(New DataColumn("Name"))
    dt.Columns.Add(New DataColumn("ChildID"))

    Dim i As Integer
    For i = 0 To numberGrandChildRows - 1
        Dim dr As DataRow = dt.NewRow()
        dr(0) = i.ToString()
    Next i

End Function
```

<!-- tags: [windows-forms, essential-grid, table, data-bindings, synchronization, hierarchy] keywords: [parent table, child table, grandchild table, data binding, data table creation] -->
```