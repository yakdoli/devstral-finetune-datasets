```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: XlsIO
page_number: 050
page_id: XlsIO#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:51:06Z
fidelity: lossless
-->

## Workbook Management

### C#

```csharp
// Closing the workbook.
workbook.Close();

// Dispose the Excel Engine.
excelEngine.Dispose();
}
}
```

### VB.NET

```vbnet
' Save the file on to disk.
Dim sfd As SaveFileDialog = New SaveFileDialog()
sfd.DefaultExt = ".xls"
sfd.Filter = "Files(*.xls)|*.xls"
If sfd.ShowDialog() = True Then
    Using stream As Stream = sfd.OpenFile()
        workbook.SaveAs(stream)

        ' Closing the workbook.
        workbook.Close()

        ' Dispose the Excel Engine.
        excelEngine.Dispose()
    End Using
End If
```

The Workbook is saved and closed and the Excel engine is disposed.

### Note:
This is a very basic usage scenario where "Hello World" is inserted into the cell "A1" of the spreadsheet. The more advanced usage scenarios of creating complex spreadsheets from scratch are explained in detail in this user guide.
```


<!-- tags: [Syncfusion Winforms, XlsIO, Workbook Management, C# examples, VB.NET examples] keywords: [workbook, dispose, Excel Engine, file dialog, save, close, user guide, complex spreadsheets] -->
```