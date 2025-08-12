```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: Olap Common
page_number: 049
page_id: Olap Common#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:05Z
fidelity: lossless
-->

## Essential OlapCommon

```vb
dimensionElementColumn.Name = "Customer"

' Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

' Specifying the SubsetElement
' Specify the start index and end index to retrieve the records.
Dim subSetElementColumn As SubsetElement = New SubsetElement(5)
subSetElementColumn.Name = "Top 5 Elements"

Dim subSetElementRow As SubsetElement = New SubsetElement(3)
subSetElementRow.Name = "Top 3 Elements"

''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
''' Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)
olapReport.CategoricalElements.SubSetElement = subSetElementColumn
''' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
olapReport.SeriesElements.SubSetElement = subSetElementRow
```

## 4.3.11.1.7 Drill down report

---

```html
© 2013 Syncfusion. All rights reserved. | Page 49
```

<!-- tags: [OlapCommon, WinForms, Version 11.4.0.26] keywords: [dimensionElementColumn, measureElementColumn, subsetElementColumn, subsetElementRow, olapReport, categorical elements, series elements, drill down report] -->
```