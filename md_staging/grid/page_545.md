```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_545.jpeg
document_name: grid
page_number: 545
page_id: grid#page_545
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Dim myDataTable As DataTable = New DataTable("MyDataTable")

' Declare the Data Column and Data Row variables.
Dim myDataColumn As DataColumn
Dim myDataRow As DataRow

' Create a new Data Column, set the Data Type and Column Name and add to the Data Table.
myDataColumn = New DataColumn()
myDataColumn.DataType = System.Type.GetType("System.Int32")
myDataColumn.ColumnName = "id"
myDataTable.Columns.Add(myDataColumn)

' Create a second column.
myDataColumn = New DataColumn()
myDataColumn.DataType = Type.GetType("System.String")
myDataColumn.ColumnName = "item"
myDataTable.Columns.Add(myDataColumn)

' Create new Data Row objects and add to the Data Table.
Dim i As Integer
For i = 0 To 10
    myDataRow = myDataTable.NewRow
    myDataRow("id") = i
    myDataRow("item") = "item " & i
    myDataTable.Rows.Add(myDataRow)
Next i

Me.gridDataBoundGrid1.DataSource = myDataTable

' Size the columns.
Me.gridDataBoundGrid1.Model.ColWidths(1) = 30
Me.gridDataBoundGrid1.Model.ColWidths(2) = 50
```

## 4.2.2 Concepts and Features

This section discusses the use cases for the Grid Data Bound Grid. The cases range from simple binding to a DataTable through Master-Detail and ends with some hierarchical binding samples. It also includes other topics like filtering, sorting, and accessing data in the grid.
```