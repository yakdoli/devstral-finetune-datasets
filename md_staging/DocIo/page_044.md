```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_044.jpeg
document_name: DocIo
page_number: 044
page_id: DocIo#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:55Z
fidelity: lossless
-->

Essential DocIO

```vb
' Save the file to stream.
Dim sfd As New SaveFileDialog()
sfd.DefaultExt = ".xls"
sfd.Filter = "Files(*.xls)|*.xls"
If sfd.ShowDialog() = True Then
    Using stream As Stream = sfd.OpenFile()
        document.Save(stream, FormatType.Doc)
    End Using
End If
```

**Note:** Here, initially Word document has no section and no paragraph. You should add sections and paragraphs to write text on it. Save method of the WordDocument is used to save the created document to disk or stream to browser.

The following screen shot shows the Word document that is generated.

![](https://via.placeholder.com/50)

<!-- tags: essential, docio, syncfusion, windowsforms, document saving, stream, winforms keywords: document, section, paragraph, save, stream, WordDocument, Office, toolbar, UI -->
```