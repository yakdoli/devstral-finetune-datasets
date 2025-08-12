```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_994.jpeg
document_name: grid
page_number: 994
page_id: grid#page_994
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:57:23Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

```csharp
for (int j = 0; j < nCols; j++)
{
    dr[j] = r.Next(100).ToString();
    dt.Rows.Add(dr);
}
return dt;
}

// Set up a grouping grid.
this.gridGroupingControl1.DataSource = GetDataTable();
this.gridGroupingControl1.ShowGroupDropArea = true;
```

### [VB.NET]

```vb
' Create the data source.
Private Function GetDataTable() As DataTable

    Dim dt As New DataTable("MyTable")

    Dim nCols As Integer = 4
    Dim nRows As Integer = 50

    Dim i As Integer
    For i = 0 To nCols - 1
        dt.Columns.Add(New DataColumn(String.Format("Col{0}", i)))
    Next i
    Dim r As New Random()

    i = 0
    While i < nRows
        Dim dr As DataRow = dt.NewRow()
        Dim j As Integer
        For j = 0 To nCols - 1
            dr(j) = r.Next(100).ToString()
        Next j
        dt.Rows.Add(dr)
        i += 1
    End While

    Return dt
End Function

' Set up a grouping grid.
Me.gridGroupingControl1.DataSource = GetDataTable()
Me.gridGroupingControl1.ShowGroupDropArea = True
```
```html
<!-- tags: [Essential Grid, Windows Forms, group grid, grouping grid, DataSource, gridGroupingControl, ShowGroupDropArea] keywords: [syncfusion, windows forms, grid, grouping, grid control] -->
```