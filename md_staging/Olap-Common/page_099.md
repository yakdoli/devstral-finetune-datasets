```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: Olap Common
page_number: 099
page_id: Olap Common#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:45Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
dlg.Filter = "XML files (*.xml)|*.xml"
Dim b As Nullable(Of Boolean) = dlg.ShowDialog()

If b.HasValue AndAlso b.Value Then
    Dim report As OlapReport = Nothing

    Using stream As FileStream = dlg.File.OpenRead()
        Dim serializer As System.Xml.Serialization.XmlSerializer = New System.Xml.Serialization.XmlSerializer(GetType(OlapReportCollection))
        Dim olapReportCollection As OlapReportCollection = TryCast(serializer.Deserialize(stream), OlapReportCollection)
        report = olapReportCollection(0)
    End Using
    olapDataManager.SetCurrentReport(report)
End If
End Sub
```

## 5.13 Rename and remove a report

Once the report collection is loaded with reports, you can rename or remove any reports in that collection by using the RenameReport and RemoveReport methods.

### 5.13.1 RenameReport

A report in the report collection of OlapDataManager can be renamed by invoking RenameReport method with arguments such as, index of the report and new name for the report or with old name and new name of the report. The following code snippet will illustrate this:

#### [C#]

```csharp
olapDataManager.RenameReport(2, "SalesAnalysisOn2003");
olapDataManager.RenameReport("RevenueAnalysis", "RevenueAnalysisOn2003");
```

#### [VB]

```vb
olapDataManager.RenameReport(2, "SalesAnalysisOn2003")
olapDataManager.RenameReport("RevenueAnalysis", "RevenueAnalysisOn2003")
```
```