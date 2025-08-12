```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_550.jpeg
document_name: grid
page_number: 550
page_id: grid#page_550
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:57Z
fidelity: lossless
 -->

### Essential Grid for Windows Forms

```csharp
dr["LastName"] = "Jacobs";
table.Rows.Add(dr);
```
```csharp
dr = table.NewRow();
dr["FirstName"] = "Sam";
dr["LastName"] = "Garfunkel";
table.Rows.Add(dr);
```
```csharp
dr = table.NewRow();
dr["FirstName"] = "George";
dr["LastName"] = "Shepherd";
table.Rows.Add(dr);
```
```csharp
dr = table.NewRow();
dr["FirstName"] = "Becky";
dr["LastName"] = "Dunsford";
table.Rows.Add(dr);
```
```csharp
return table;
}
```

[VB.NET]

```vb
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    Me.GridDataBoundGrid1.DataSource = ReturnATable()
End Sub
```
```vb
Private Function ReturnATable() As DataTable
    Dim table As DataTable = New DataTable("People")

    ' Add two columns.
    table.Columns.Add(New DataColumn("FirstName"))
    table.Columns.Add(New DataColumn("LastName"))

    ' Add some rows.
    Dim dr As DataRow = table.NewRow()
    dr("FirstName") = "John"
    dr("LastName") = "Smith"
    table.Rows.Add(dr)

    dr = table.NewRow()
    dr("FirstName") = "Mary"
    dr("LastName") = "Tucker"
    table.Rows.Add(dr)
End Function
```
```