```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_449.jpeg
document_name: XlsIO
page_number: 449
page_id: XlsIO#page_449
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:19:05Z
fidelity: lossless
-->

### Code Example for Zipping Files

```vb
' Zip and save the file.
Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)
    SubFoldersFiles(Me.textBox1.Text)
    
    If Directory.Exists(Me.textBox1.Text) Then
        AddRootFiles()
        
        AddSubFoldersFiles()
        
        ' Saving zipped file.
        Dim saveDialog As New SaveFileDialog()
        saveDialog.Filter = "Zip Files | *.zip"
        If saveDialog.ShowDialog() = Windows.Forms.DialogResult.OK Then
            zipArchive.Save(saveDialog.FileName)
        End If
        
        zipArchive.Close()
        label1.Text = "Files Zipped successfully!"
        button1.Enabled = False
    End If
End Sub

Private Sub AddRootFiles()
    For Each rootfiles As String In Directory.GetFiles(Me.textBox1.Text)
        stream = New FileStream(rootfiles, FileMode.Open, FileAccess.Read)
        att = File.GetAttributes(rootfiles)
        item = New ZipArchiveItem(rootfiles, stream, True, att)
        zipArchive.AddItem(item)
    Next
End Sub

Private Sub AddSubFoldersFiles()
    For Each dInfo As IO.DirectoryInfo In arr
        Dim fInfo As FileInfo() = dInfo.GetFiles()
        For Each file As FileInfo In fInfo
            Dim str As String = file.FullName
            stream = New FileStream(str, FileMode.Open, FileAccess.Read)
            Dim att As FileAttributes = file.GetAttributes(str)
            zipArchive.AddItem(New Syncfusion.Compression.Zip.ZipArchiveItem(str, stream, True, att))
        Next
        Next
End Sub
```

<!-- tags: [Syncfusion Winforms, XlsIO, CodeExample, ZippingFiles] keywords: [zip, save, file, directory, AddRootFiles, AddSubFoldersFiles, SaveFileDialog, FileStream, ZipArchiveItem] -->
```