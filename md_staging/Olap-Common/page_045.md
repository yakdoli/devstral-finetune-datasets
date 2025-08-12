```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: Olap Common
page_number: 045
page_id: Olap Common#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:54Z
fidelity: lossless
-->

## Essential OlapCommon

```vb
' Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim sortElement As SortElement = New SortElement(AxisPosition.Categorical, SortOrder.BDESC, True)
sortElement.Element.UniqueName = "[Measures].[Internet Sales Amount]"

''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)

''' Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)

' Adding Sort Element
olapReport.CategoricalElements.Add(sortElement)

''' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

## 4.3.11.1.5 Report with Filter

### [C#]

```csharp
OlapReport olapReport = new OlapReport();

olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

// Creating Measure Element
MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Dimension Name
```
```