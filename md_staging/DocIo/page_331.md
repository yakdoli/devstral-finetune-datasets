```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_331.jpeg
document_name: DocIo
page_number: 331
page_id: DocIo#page_331
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:25Z
fidelity: lossless
-->

# Essential DocIO

```vb
Imports word = Microsoft.Office.Interop.Word
' Initialize objects
Dim nullobject As Object = Missing.Value
Dim dataBase As String = "Northwind.mdb"
Dim filePath As Object = "EmployeesReportDemo.doc"
Dim sqlStmt As String = "SELECT * FROM [Employees]"
Dim falseobj As Object = False

' Start the word application
Dim wordApp As word.Application = New word.Application()

' Open the word document
Dim doc As word.Document = wordApp.Documents.Open(filePath, _
    nullobject, nullobject, nullobject, nullobject, _
    nullobject, nullobject, nullobject, nullobject, falseobj, _
    nullobject, nullobject, nullobject, nullobject)

wordApp.Visible = False

' Perform Mail Merge
With doc.MailMerge
    .OpenDataSource(dataBase, nullobject, nullobject, _
        nullobject, nullobject, nullobject, nullobject, _
        nullobject, nullobject, sqlStmt, nullobject, nullobject, nullobject)
    .Execute(nullobject)
    .Destination = word.WdMailMergeDestination.wdSendToNewDocument
End With

' Close the document
doc.Close(nullobject, nullobject, nullobject)

' Quit the application
wordApp.Quit(nullobject, nullobject, nullobject)
```

## Using DocIO

DocIO performs the mail merge using the `Execute()` method as illustrated in the following example.
```html
<!-- tags: [DocIO, mail merge, Microsoft.Office.Interop.Word, Syncfusion Winforms, version: 11.4.0.26] keywords: [DocIO, mail merge, Execute, OpenDataSource, Microsoft.Office.Interop.Word, Word, Application, Document, wdMailMergeDestination, wdSendToNewDocument, nullobject, falseobj, EmployeesReportDemo.doc, Employees] -->
``` 
