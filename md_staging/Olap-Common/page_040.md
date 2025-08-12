```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: Olap Common
page_number: 040
page_id: Olap Common#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:07Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
measureElementRow.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.SeriesElements.Add(dimensionElementRow)
olapReport.SlicerElements.Add(dimensionElementSlicer)
olapReport.SeriesElements.Add(measureElementRow)
```

## 4.3.11.1.3 Report with dicing operation

```csharp
[C#]

OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";
DimensionElement dimensionElementColumn = new DimensionElement();
//Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
//Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
//Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.HierarchyName = "Fiscal";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

//Specifying Excluded column elements
DimensionElement excludedColumnElement = new DimensionElement();
excludedColumnElement.Name = "Customer";
excludedColumnElement.HierarchyName = "Customer Geography";
excludedColumnElement.AddLevel("Customer Geography", "Country");
excludedColumnElement.Hierarchy.LevelElements["Country"].Add("Canada");
excludedColumnElement.Hierarchy.LevelElements["Country"].Add("France");
excludedColumnElement.Hierarchy.LevelElements["Country"].Add("United Kingdom");
excludedColumnElement.Hierarchy.LevelElements["Country"].Add("United States");
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [olap, report, dice operation, customer report, date hierarchy, excluded elements] keywords: [C#, dimensionElement, measureElements, hierarchy, fiscal year, customer geography, excluded column, United States] -->

<!-- tags: [olap, report, dice operation, customer report, date hierarchy, excluded elements] keywords: [C#, dimensionElement, measureElements, hierarchy, fiscal year, customer geography, excluded column, United States] -->
```
