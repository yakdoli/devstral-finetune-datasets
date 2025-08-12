```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: Olap Common
page_number: 096
page_id: Olap Common#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:20Z
fidelity: lossless
-->

# Essential OlapCommon

The following sequential diagram shows the workflow of OlapBase when the input is a Non-OLAP data:

```plaintext
          User
            |
            v
        OlapDataManager
            |
            v
        DataProvider
            |
            v
        QuerySpecification
            |
            v
        QueryBuilder
            |
            v
        QueryBuilderHelper
            |
            v
        PivotEngine
```

**Figure 11: Olap base Sequential diagram**

## 5.11 Save the report as xml file

The user can save the current report set of OlapDataManager as an xml file for the future needs by using the SaveReport method.

The following code snippet will illustrate the saving of the current report set as an xml file:

### C#

```csharp
olapDataManager.SaveReport(@"C:\SampleReport\RevenueAnalysis.xml");
```

### VB

```vb
olapDataManager.SaveReport("C:\SampleReport\RevenueAnalysis.xml")
```

### For Silverlight:

You can save the current report of OlapDataManager as an xml file for their future use by serializing the report with `XmlSerializer`.

The following code snippet will illustrate the saving of the current report set as an xml file:

### C#

```csharp
private void SaveReport()
{
    SaveFileDialog dlg = new SaveFileDialog();
}
```

<footer>
© 2013 Syncfusion. All rights reserved.
106 | Page
</footer>
```