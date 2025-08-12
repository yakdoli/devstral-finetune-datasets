<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: Olap Common
page_number: 060
page_id: Olap Common#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:45Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
// Adding Measure Elements
olapReport.CategoricalElements.Add(measureElementColumn);
// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

### [VB]

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Products Sales Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the name for Dimension Element for Column
dimensionElementColumn.Name = "Product"
dimensionElementColumn.AddLevel("Product Categories", "Category")
dimensionElementColumn.Hierarchy.LevelElements("Category").Add(Me.productName)
dimensionElementColumn.Hierarchy.LevelElements("Category").IncludeAvailableMembers = True

Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the name for Measure Element
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Gross Profit"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Name for Row Dimension Element
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim kpiElement As KpiElements = New KpiElements()
kpiElement.Elements.Add(New KpiElement With {.Name = "Revenue",
                                             .ShowKPIStatus = True,
                                             .ShowKPIGoal = False,
                                             .ShowKPI Trend = True,
                                             .ShowKPIValue = True})
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

<!-- tags: [olapcommon, essentialolapcommon, syncfusion, winforms, olapreport, dimensionelement, measureelements, kpielements] keywords: [OlapReport, DimensionElement, MeasureElements, KpiElements, Products Sales Report, Adventure Works, Product, Gross Profit, Date, Fiscal, Revenue] -->