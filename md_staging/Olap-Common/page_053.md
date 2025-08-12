```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: Olap Common
page_number: 053
page_id: Olap Common#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:17Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Demonstrates filtering the top 5 elements of "Internet Sales Amount" in an OLAP report.
- Constructs a report with categorized elements and series elements for specific dimensions and measures.

## Content

### Example Code in C#

```csharp
//Filter the top 5 elements of "Internet Sales Amount".
TopCountElement topCountElement = new TopCountElement(AxisPosition.Categorical, 5);
topCountElement.MeasureName = "Internet Sales Amount";

//// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
////Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
////Adding Measure Element
olapReport.CategoricalElements.Add(topCountElement);
////Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

### Example Code in VB

```vb
[VB]

Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

' Creating Measure Element
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

' Filter the top 5 elements of "Internet Sales Amount".
```

## Page-level Navigation/TOC (if applicable)
- This page focuses on using `TopCountElement` to filter elements in an OLAP report.

<!-- tags: [product, module, control, api, version?] keywords: [Olap Common, TopCountElement, OLAP report, filtering, VB, C#] -->
```