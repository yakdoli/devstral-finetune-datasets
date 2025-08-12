```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_271.jpeg
document_name: DocIo
page_number: 271
page_id: DocIo#page_271
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:16Z
fidelity: lossless
-->

# Essential DocIO

```vb
Dim table3 As DataTable = GetNestedDataTable("select * from Table3")
table3.TableName = "Table3"

Dim dataSet As DataSet = New DataSet("Test dataset")
dataSet.Tables.Add(table1)
dataSet.Tables.Add(table2)
dataSet.Tables.Add(table3)

' Arraylist contains the list of commands.
Dim commands As ArrayList = New ArrayList()
Dim enEntry As DictionaryEntry = New DictionaryEntry("Table1", String.Empty)
commands.Add(enEntry)

enEntry = New DictionaryEntry("table2", "sellerid = Decimal.Remainder(, table1.sellerid)%")
commands.Add(enEntry)

enEntry = New DictionaryEntry("Table3", "CustomerID = Decimal.Remainder(, Table2.CustomerID)%")
commands.Add(enEntry)

doc.MailMerge.RemoveEmptyParagraphs = True

' Execute NestedGroup by passing the DataSet.
doc.MailMerge.ExecuteNestedGroup(dataSet, commands)

doc.Save("NestedMailMerge.doc")
System.Diagnostics.Process.Start("NestedMailMerge.doc")
End Sub

' <summary>
' Get the table
' </summary>
' <param name="sqlQuery"></param>
' <returns></returns>
Private Function GetNestedDataTable(ByVal sqlQuery As String) As DataTable
    Dim conn As OleDbConnection = Nothing
    Try
        Dim connString As String = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + System.IO.Path.Combine(dataPath, "NestedMailMerge1.mdb")

        ' Get data from the database.
        conn = New OleDbConnection(connString)
        conn.Open()
        Dim cmd As OleDbCommand = New OleDbCommand(sqlQuery, conn)
    End Try
    ...
End Function
```

## API Reference

### Namespace: System.Data
- **Class**: DataSet
  - Members:
    - **Property**: Tables (As DataTableCollection)
    - **Property**: TableName (As String)
  
### Namespace: System.Collections
- **Class**: ArrayList
  - Members:
    - **Method**: Add(items As Object)

### Namespace: System.Collections.Generic
- **Class**: DictionaryEntry
  - Members:
    - **Property**: Key (As String)
    - **Property**: Value (As Object)

### Namespace: System.Diagnostics
- **Class**: Process
  - Members:
    - **Method**: Start(filename As String)

## Code Examples

```vb
' Example: Executing a nested group mail merge using a dataset and commands list.
Dim dataSet As DataSet = New DataSet("Test dataset")
dataSet.Tables.Add(table1)
dataSet.Tables.Add(table2)
dataSet.Tables.Add(table3)

Dim commands As ArrayList = New ArrayList()
commands.Add(New DictionaryEntry("Table1", String.Empty))
commands.Add(New DictionaryEntry("table2", "sellerid = Decimal.Remainder(, table1.sellerid)%"))
commands.Add(New DictionaryEntry("Table3", "CustomerID = Decimal.Remainder(, Table2.CustomerID)%"))

doc.MailMerge.ExecuteNestedGroup(dataSet, commands)
doc.Save("NestedMailMerge.doc")
System.Diagnostics.Process.Start("NestedMailMerge.doc")
```

## Related Topics

- [Mail Merge Overview in DocIO](#)
- [Executing Nested Groups in Mail Merge](#)
- [Data Merging in WinForms Applications](#)

<!-- tags: DocIO, WinForms, MailMerge, DataSet, ArrayList, DictionaryEntry, Process, System.Data, System.Collections, System.Collections.Generic, version: 11.4.0.26 -->
```