```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: Olap Common
page_number: 058
page_id: Olap Common#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:29Z
fidelity: lossless
-->

Essential OlapCommon

```vb
'// Calculated Measure
Dim calculatedMeasure2 As CalculatedMember = New CalculatedMember()
calculatedMeasure2.Name = "Sales Range"
calculatedMeasure2.AddElement(New MeasureElement With {.Name = "Sales Amount"})
calculatedMeasure2.Expression = "IIF([Measures].[Sales Amount]>200000,""High"",""Low"")"

' Calculated Dimension
Dim calculateDimension As CalculatedMember = New CalculatedMember()
calculateDimension.Name = "Bikes & Components"
calculateDimension.Expression = "([Product].[Product Categories].[Category].[Bikes] + [Product].[Product Categories].[Category].[Components] )"
calculateDimension.AddElement(internalDimension)

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Sales Amount"})
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Order Quantity"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
'Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

'// Adding Calculated members in calculated member collection
olapReport.CalculatedMembers.Add(calculatedMeasure1)
olapReport.CalculatedMembers.Add(calculateDimension)
olapReport.CalculatedMembers.Add(calculatedMeasure2)

''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.CategoricalElements.Add(calculateDimension)
```

---

© 2013 Syncfusion. All rights reserved.  
```