```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: Olap Common
page_number: 102
page_id: Olap Common#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:00Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

FilterElement filterElement = new FilterElement(AxisPosition.Categorical);
filterElement.Elements.Add(measureElementColumn);
filterElement.Elements.Add(dimensionElementColumn);
filterElement.FilterCase = FilterCase.GreaterThan;
filterElement.FilterValue.Add(new MeasureElement { Name = "Internet Sales Amount", Visible = true });
filterElement.FilterValue.Add(new FilterValue { Filter_Value = 2700000.0 });
filterElement.IsFilterCondition = true;
/// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.IsFilterOrSortOn = true;
/// Adding Measure Element
olapReport.FilterElements.Add(filterElement);
```

### [VB]

```vb
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim filterElement As FilterElement = New FilterElement(AxisPosition.Categorical)
filterElement.Elements.Add(measureElementColumn)
filterElement.Elements.Add(dimensionElementColumn)
filterElement.FilterCase = FilterCase.GreaterThan

filterElement.FilterValue.Add(New MeasureElement With {.Name = "Internet Sales Amount", .Visible = True})

filterElement.FilterValue.Add(New FilterValue With {.Filter_Value =
```

---  
© 2013 Syncfusion. All rights reserved.  
```  
<!-- tags: [Syncfusion Winforms, Olap Common, MeasureElements, FilterElement, DimensionElement, FilterCase, FilterValue, CSharp, VB, API Reference, Code Examples] keywords: [Olap Common, Essential Features, MeasureElements, FilterElement, DimensionElement, FilterCase, FilterValue, CSharp, VB, API, Code Examples, WinForms] -->
``` 
``` 
