```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_272.jpeg
document_name: DocIo
page_number: 272
page_id: DocIo#page_272
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:13Z
fidelity: lossless
-->

## Essential DocIO

```vb
Dim da As OleDbDataAdapter = New OleDbDataAdapter(cmd)
Dim table As DataTable = New DataTable()
da.Fill(table)
Return table
Finally
    If Not conn Is Nothing Then
        conn.Close()
    End If
End Try
End Function
}
```

### 4.6.2 Mail Merge Events

The MailMerge class provides two events to expand the mail merge capabilities. **MailMerge.MergeField** and **MailMerge.MergImageField** events are used to implement custom control logic over the mail merge process.

The MailMerge.MergeField event occurs during mail merge when a simple mail merge field is encountered in the document. This allows to implement further control over the mail merge and perform any actions when the event occurs. Use the **MergeFieldEventHandler** delegate to reference the method that will handle MergeField. This method should accept a MergeFieldEventArgs object that provides data for the MergeField event.

#### [C#]

```csharp
public void MailMerge()
{
    // Load the template.
    WordDocument document = new WordDocument(@"Template.doc");

    // Using Merge events to do conditional formatting during runtime.
    document.MailMerge.MergeField += new MergeFieldEventHandler(AlternateRows_MergeField);

    // Execute Mail Merge with groups.
    document.MailMerge.Execute(GetDataTable());

    // Save the document.
    document.Save("sample.doc");
}
```

#### Summary

<!-- tags: [MailMerge, EventHandling, DocIO] keywords: [mergefield, emailmerge, conditionalformatting, eventhandler, docio, winforms] -->
```