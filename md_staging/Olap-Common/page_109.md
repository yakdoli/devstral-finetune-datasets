```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: Olap Common
page_number: 109
page_id: Olap Common#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:22:27Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim currentMdxQuery As String
'Invoke the service call to retrieve the MDX query from the Server based on current report.
_olapDataManager.GetMdxQuery(_olapDataManager.CurrentReport)
_olapDataManager.MdxQueryObtained += Function()
'MDX Query retrieved.
currentMdxQuery = _olapDataManager.CurrentReport.CurrentMdxQuery
End Function
```

## 5.23 Add UseWhereClauseForSlicing to an Application

The user can add the UseWhereClauseForSlicing property to an application by setting the property to a Boolean value. To perform the slicing operation using the ‘Where’ clause, set the property to `true`. To perform the slicing operation using the ‘Select’ clause, set the property to `false`. By default, the value of the UseWhereClauseForSlicing property is `true`.

### To perform slicing operation using ‘Where’ clause:

```csharp
OlapDataManager.UseWhereClauseForSlicing = true;
```

```vb
OlapDataManager.UseWhereClauseForSlicing = True
```

### To perform slicing operation using ‘Select’ clause:

```csharp
this.olapGridControl1.OlapDataManager.UseWhereClauseForSlicing = false;
```

```vb
Me.olapGridControl1.OlapDataManager.UseWhereClauseForSlicing = False
```

<!-- tags: [syncfusion, winforms, olap, slicing, mdx, where clause, select clause] keywords: [UseWhereClauseForSlicing, MDX query, slicing operation, boolean property, default value] -->
```