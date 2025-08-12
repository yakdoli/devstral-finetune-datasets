<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: Olap Common
page_number: 097
page_id: Olap Common#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:43Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
dlg.Filter = "XML files (*.xml)|*.xml";

bool? b = dlg.ShowDialog();

if (b.HasValue && b.Value)
{
    using (Stream stream = dlg.OpenFile())
    {
        System.Xml.Serialization.XmlSerializer serializer = new System.Xml.Serialization.XmlSerializer(typeof(OlapReport));
        serializer.Serialize(stream, this.olapDataManager.CurrentReport);
    }
}
}
```

### [VB]

```vb
Private Sub SaveReport()
    Dim dlg As SaveFileDialog = New SaveFileDialog()
    dlg.Filter = "XML files (*.xml)|*.xml"

    Dim b As Nullable(Of Boolean) = dlg.ShowDialog()

    If b.HasValue AndAlso b.Value Then
        Using stream As Stream = dlg.OpenFile()
            Dim serializer As System.Xml.Serialization.XmlSerializer = New System.Xml.Serialization.XmlSerializer(GetType(OlapReport))
            serializer.Serialize(stream, Me.olapDataManager.CurrentReport)
        End Using
    End If
End Sub
```

## 5.12 Load xml report file

You can load the xml report set by using the `LoadReport` method.  
The following code snippet will illustrate the loading of the report:

---

<!-- tags: [syncfusion, winforms, olap, report, serialization, xml, load, save, api] keywords: [essential olapcommon, xml report, loadreport method, oleblob result, grid, table, size] -->