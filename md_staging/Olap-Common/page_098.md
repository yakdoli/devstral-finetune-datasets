```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_098.jpeg
document_name: Olap Common
page_number: 098
page_id: Olap Common#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:49Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
olapDataManager.LoadReport(@"C:\SampleReport\RevenueAnalysis.xml");
```

```vb
olapDataManager.LoadReport("C:\SampleReport\RevenueAnalysis.xml")
```

## For Silverlight:

The saved report file can be used with `OlapDataManager` by serializing it to type `OlapReport` with `XmlSerializer`.

The following code snippet will illustrate the loading of a saved XML report file:

### C#

```csharp
private void LoadReport()
{
    OpenFileDialog dlg = new OpenFileDialog();
    dlg.Filter = "XML files (*.xml)|*.xml";
    bool? b = dlg.ShowDialog();

    if (b.HasValue && b.Value)
    {
        OlapReport report = null;

        using (FileStream stream = dlg.File.OpenRead())
        {
            System.Xml.Serialization.XmlSerializer serializer = new System.Xml.Serialization.XmlSerializer(typeof(OlapReportCollection));
            OlapReportCollection olapReportCollection = serializer.Deserialize(stream) as OlapReportCollection;
            report = olapReportCollection[0];
        }
        olapDataManager.SetCurrentReport(report);
    }
}
```

### VB

```vb
Private Sub LoadReport()
    Dim dlg As OpenFileDialog = New OpenFileDialog()
```

---

``` 
© 2013 Syncfusion. All rights reserved.
Page 98
```
