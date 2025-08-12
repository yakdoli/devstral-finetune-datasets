```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_333.jpeg
document_name: DocIo
page_number: 333
page_id: DocIo#page_333
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:22Z
fidelity: lossless
-->

# Essential DocIO

```vb
'[VB]

Dim dataBase As String = "Northwind.mdb"

' Open the word document
Dim doc As WordDocument = New WordDocument("EmployeesReportDemo.doc")

' Create database connection
Dim conn As OleDbConnection = New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + dataBase)
conn.Open()

' Populate data table
Dim table As DataTable = New DataTable()
Dim adapter As OleDbDataAdapter = New OleDbDataAdapter("select * from employees", conn)
adapter.Fill(table)
adapter.Dispose()

' Perform Mail Merge
doc.MailMerge.Execute(table)

' Save the document
doc.Save("MailMerge.doc", FormatType.Doc)

' Close the document
doc.Close()
```

**Note:** For more information on performing the mail merge using DocIO, you can refer to the online documentation link given below:

[http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/46mailmerge.htm](http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/46mailmerge.htm)

## 5.12.2 Find and Replace

This section illustrates how to perform simple find and replace operations in a word document using MS Office Interop and DocIO.

### Using MS Office Interop

The following code example shows how to search a word in a word document, replace it with another word, and save the document in a new name.

<!-- tags: [docio, mail merge, find and replace, ms office interop] -->
```json
{
  "keywords": [
    "mail merge",
    "find and replace",
    "docio",
    "ole db connection",
    "mail merge execute",
    "save document",
    "document close",
    "ms office interop"
  ]
}
```
```