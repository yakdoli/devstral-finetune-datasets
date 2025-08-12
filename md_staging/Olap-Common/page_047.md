```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: Olap Common
page_number: 047
page_id: Olap Common#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:29Z
fidelity: lossless
-->

# Essential OlapCommon

```vbnet
' Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim filterElement As FilterElement = New FilterElement(AxisPosition.Categorical)
filterElement.Elements.Add(measureElementColumn)
filterElement.Elements.Add(dimensionElementColumn)
filterElement.FilterCase = FilterCase.GreaterThan

filterElement.FilterValue.Add(New MeasureElement With {.Name = "Internet Sales Amount", .Visible = True})

filterElement.FilterValue.Add(New FilterValue With {.Filter_Value = 2700000.00})
filterElement.IsFilterCondition = True
olapReport.CategoricalElements.Add(New Item With {.ElementValue = dimensionElementColumn})
olapReport.CategoricalElements.IsFilterOrSortOn = True
olapReport.FilterElements.Add(New Item With {.ElementValue = filterElement})
```

## 4.3.11.1.6 Report with subset

### C#

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";
DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet
```


*Note*: It appears there is an incomplete line at the end. This may need further clarification.

## Page-level Navigation/TOC (if applicable)
- Local Table of Contents: Chapter or section headings as specified in the page image.

<!-- tags: [Syncfusion, Winforms, OlapCommon, Report, Filter, C#] keywords: [dimension, hierarchy, filter, internet sales, customer, country, measure element] -->
``` 
