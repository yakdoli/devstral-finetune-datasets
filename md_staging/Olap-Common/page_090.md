```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: Olap Common
page_number: 090
page_id: Olap Common#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:21Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim dimensionElementRow As DimensionElement = New DimensionElement()
'Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

'Adding Column Members
olapReport1.CategoricalElements.Add(dimensionElementColumn)
'Adding Measure Element
olapReport1.CategoricalElements.Add(measureElementColumn)
'Adding Row Members
olapReport1.SeriesElements.Add(dimensionElementRow)
```

## 5.8.1 CurrentReport

Once the OlapReport is created by assigning the report to the **CurrentReport** property of the OlapDataManager, you can bind the OlapReport to the OlapDataManager.

The following code snippet explains the assigning of an OlapReport to CurrentReport property:

### C#
```csharp
OlapDataManager.CurrentReport = olapReport;
```

### VB
```vb
OlapDataManager.CurrentReport = olapReport
```

## 5.8.2 SetCurrentReport

The following code snippet explains setting an OlapReport to CurrentReport of an OlapDataManager using SetCurrentReport method:

### C#
```csharp
OlapDataManager.SetCurrentReport(olapReport);
```

### VB
```vb
OlapDataManager.SetCurrentReport(olapReport)
```

## 5.8.3 LoadOlapDataManager

The following code snippet explains loading an OlapReport to CurrentReport property of an OlapDataManager using LoadOlapDataManager method:

### C#
```csharp
```

<!-- tags: [Olap, OlapCommon, OlapReport, OlapDataManager, CurrentReport, SetCurrentReport, LoadOlapDataManager, WinForms] keywords: [OlapReport, OlapDataManager, CurrentReport, SetCurrentReport, LoadOlapDataManager] -->
```