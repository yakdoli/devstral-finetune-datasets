```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: Olap Common
page_number: 051
page_id: Olap Common#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:42Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

'Creating Measure Element
Dim olapReport As OlapReport = New OlapReport()
olapReport.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
'Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"

Dim olapReport As OlapReport = New OlapReport()
olapReport.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
'Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
'Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.HierarchyName = "Fiscal"
```

## Page-level Navigation/TOC (if applicable)

- \[No TOC visible on this page\]

## Cross References

- Refer to related sections or pages in the documentation for additional details.

## RAG Annotations

<!-- tags: [OlapReport, DimensionElement, MeasureElements, Adventure Works, Customer Geography, Fiscal, Internet Sales Amount] keywords: [dimension, hierarchy, levels, measure elements, data reporting, olap] -->
```