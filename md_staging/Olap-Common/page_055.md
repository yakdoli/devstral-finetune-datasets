```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: Olap Common
page_number: 055
page_id: Olap Common#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:55Z
fidelity: lossless
-->

## Essential OlapCommon

### Overview
- This section demonstrates the use of dimension elements in an OLAP report. It includes examples in both C# and VB.
- The process involves specifying dimensions, hierarchies, measures, and named sets to create a comprehensive OLAP report.
- This example utilizes the "Adventure Works" cube and includes elements such as "Customer," "Customer Geography," "Core Product Group," and "Internet Sales Amount."

### WinForms-specific conventions
```csharp
olapReport.SeriesElements.Add(dimensionElementRow);
```

### Content

#### VB Code
```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the dimension Name
dimensionElementColumn.Name = "Customer"
' Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the measure elements
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

' Specifying the NamedSet Element
Dim dimensionElementRow As NamedSetElement = New NamedSetElement()
' Specifying the dimension name
dimensionElementRow.Name = "Core Product Group"

'''Adding the Column members
olapReport.CategoricalElements.Add(dimensionElementColumn)
'''Adding the Measure elements
olapReport.CategoricalElements.Add(measureElementColumn)
'''Adding the Row members
olapReport.SeriesElements.Add(dimensionElementRow)
```

### Page-level Navigation/TOC (if applicable)
- Refer to the "Olap Common" section for more details on dimension elements and OLAP report configurations.

### Cross References
- See also: "Adventure Works" cube documentation, "DimensionElement" class reference, "MeasureElements" class reference, "NamedSetElement" class reference.

### Tags and Keywords
<!-- tags: [OlapReport, DimensionElement, MeasureElements, NamedSetElement, Adventure Works, Customer Geography, Core Product Group, Internet Sales Amount] keywords: [OLAP, dimension elements, report configurations, WinForms, Syncfusion OLAP, Adventure Works cube, Customer geography, named sets] -->
```