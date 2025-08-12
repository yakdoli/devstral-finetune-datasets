```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_277.jpeg
document_name: DocIo
page_number: 277
page_id: DocIo#page_277
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:45Z
fidelity: lossless
-->



### Essential DocIO

Here is the code snippet demonstrating the use of a mail merge event handler for image fields.

```vb
' Using Merge events handler for image fields. AddHandler
document.MailMerge.MergeImageField, AddressOf MergeField_ProductImage
document.MailMerge.Execute (GetDataTable());

    ' Save the document
    document.Save("sample.doc")
End Sub

''' <summary>
''' This is called when mail merge engine encounters Image:XXX merge field in
the document.
'''
''' You have a chance to return an Image object, file name or a stream that
contains the image.
'''
''' </summary>
Private Sub MergeField_ProductImage(ByVal sender As Object, ByVal args As MergeImageFieldEventArgs)

    ' Get the image from disk during Merge.
    If args.FieldName = "ProductImage" Then
        Dim ProductFileName As String = args.FieldValue.ToString()
        args.Image = Image.FromFile (ProductFileName)
    End If
End Sub

'''<summary>
''' Create DataTable and fill it with data.
'''
'</summary>
Private Shared Function GetDataTable() As DataTable

    Dim dataTable As DataTable = New DataTable("Employee")

    dataTable.Columns.Add("EmpName")
    dataTable.Columns.Add("EmpNumber")

    For i As Integer = 0 To 19
```

## Notes

- The code snippet demonstrates the use of a mail merge event handler to handle image fields in a document. It saves the document as `sample.doc` after executing the merge operation with data from a `DataTable`.

## Created DataTable Example
- The `GetDataTable` function creates a `DataTable` named "Employee" with columns "EmpName" and "EmpNumber". It populates the table with data using a loop.

**Usage:**
- This example shows how to integrate image handling during a mail merge operation in a .NET application using the Syncfusion DocIO library.

### Related Documentation
- For more information on mail merge capabilities and event handling in Syncfusion DocIO, refer to the official documentation on Syncfusion's website.

---

### RAG Annotations
- <!-- tags: [product, module, control, api, version?] keywords: ["mail merge", "image handler", "merge field", "document", "DataTable", "Syncfusion DocIO", "Winforms", "C#", "VB.NET", "software development", "data handling"] -->
```