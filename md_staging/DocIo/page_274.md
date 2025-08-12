```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_274.jpeg
document_name: DocIo
page_number: 274
page_id: DocIo#page_274
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:29Z
fidelity: lossless
-->

# Essential DocIO

```vb
document.Save("sample.doc")
End Sub

' <summary>
' Called for every merge field encountered in the document.
' We can either return some data to the mail merge engine or do something
' else with the document. In this case we modify cell formatting.
' </summary>
Private Sub AlternateRows_MergeField(ByVal sender As Object, ByVal args As MergeFieldEventArgs)

    ' Conditionally format data during Merge.
    If args.RowIndex Mod 2 = 0 Then
        args.CharacterFormat.TextColor = Color.FromArgb(255, 102, 0)
    End If
End Sub

'<summary>
' Create DataTable and fill it with data.
' </summary>
Private Shared Function GetDataTable() As DataTable
    Dim dataTable As DataTable = New DataTable("Employee")
    dataTable.Columns.Add("EmpName")
    dataTable.Columns.Add("EmpNumber")
    For i As Integer = 0 To 19
        Dim datarow As DataRow = dataTable.NewRow()
        dataTable.Rows.Add(datarow)
        datarow(0) = "Emp" & i.ToString()
        datarow(1) = "Emp" & i.ToString()
    Next i
    Return dataTable
End Function
```

## MergImageField Events

The MailMerge.MergeImageField occurs during mail merge when an image mail merge field is encountered in the document. Image mail merge field is a merge field, with format, Image:MyFieldName. You can respond to this event to return a file name, stream, or an Image object to the mail merge engine, so that it is inserted into the document.

Use the MergeImageFieldEventHandler delegate representing the method that will handle the MergeImageField event. The event handler receives an argument of type, MergeImageFieldEventArgs.

<!-- tags: [DocIo, mail merge, image merge field] keywords: [MergeImageField, MergeImageFieldEventHandler, mail merge engine, document, data, image, file, stream, object, merge field, event handler, DocIo] -->
```