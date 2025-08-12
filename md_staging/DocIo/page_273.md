```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_273.jpeg
document_name: DocIo
page_number: 273
page_id: DocIo#page_273
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:32Z
fidelity: lossless
-->

# Essential DocLO

```
/// Called for every merge field encountered in the document.
/// We can either return some data to the mail merge engine or do something
/// else with the document. In this case we modify cell formatting.
/// </summary>
```

## Content

### C#

```csharp
private void AlternateRows_MergeField(object sender, MergeFieldEventArgs args)
{
    // Conditionally format data during Merge.
    if (args.RowIndex % 2 == 0)
    {
        args.CharacterFormat.TextColor = Color.FromArgb(255, 102, 0);
    }
}

/// <summary>
/// Create DataTable and fill it with data.
/// </summary>
private static DataTable GetDataTable()
{
    DataTable dataTable = new DataTable("Employee");
    dataTable.Columns.Add("EmpName");
    dataTable.Columns.Add("EmpNumber");
    for (int i = 0; i < 20; i++)
    {
        DataRow datarow = dataTable.NewRow();
        dataTable.Rows.Add(datarow);
        datarow[0] = "Emp" + i.ToString();
        datarow[1] = "Emp" + i.ToString();
    }
    return dataTable;
}
```

### [VB.NET]

```vb
Public Sub MailMerge()
    ' Load the template.
    Dim document As WordDocument = New WordDocument("Template.doc")

    ' Using Merge events to do conditional formatting during runtime.
    AddHandler document.MailMerge.MergeField, AddressOf AlternateRows_MergeField
    document.MailMerge.Execute(GetDataTable())

    ' Save the document.
End Sub
```

## Page-level Navigation/TOC (if applicable)
- This page discusses methods to modify cell formatting during a mail merge using events to conditionally format the data.

## Cross References
- Refer to the documentation on `MergeFieldEventArgs` for more information on how to handle merge fields.

<!-- tags: DocIO, mail merge, merge events, cell formatting, data manipulation keywords: [mail merge, merge events, cell formatting, data manipulation, AlternateRows_MergeField, GetDataTable] -->
```