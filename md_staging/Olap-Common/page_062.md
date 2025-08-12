```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: Olap Common
page_number: 062
page_id: Olap Common#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:41Z
fidelity: lossless
-->

# Essential OlapCommon

```cs
"[Employee].[Employees].[Email Address]"
);

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Dimension Name
dimensionElementColumn.Name = "Product";
// Specifying the Hierarchy and level name for the Dimension Element
dimensionElementColumn.AddLevel("Product Categories", "Category");
dimensionElementColumn.MemberProperties.Add(new MemberProperty("Dealer Price", "[Product].[Product Categories].[Dealer Price]"));
dimensionElementColumn.MemberProperties.Add(new MemberProperty("Standard Cost", "[Product].[Product Categories].[Standard Cost]"));

// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);

///Adding Column Members
olapReport.CategoricalElements.Add(measureElementColumn);
```

### VB

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Employee Sales Report"
' Specifying the current cube name
olapReport.CurrentCubeName = "Adventure Works"

Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the Name for the Measure Element
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Sales Amount Quota"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimensionElementRow.Name = "Employee"
' Specifying the Hierarchy and level name for the Dimension Element
dimensionElementRow.AddLevel("Employees", "Employee Level 02")
dimensionElementRow.Hierarchy.LevelElements("Employee Level 02").
```

## API Reference (if applicable)
- None specific to this page.

## Code Examples (multi-language supported)
- C# Example:
```cs
"[Employee].[Employees].[Email Address]"
);
DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Dimension Name
dimensionElementColumn.Name = "Product";
// Specifying the Hierarchy and level name for the Dimension Element
dimensionElementColumn.AddLevel("Product Categories", "Category");
dimensionElementColumn.MemberProperties.Add(new MemberProperty("Dealer Price", "[Product].[Product Categories].[Dealer Price]"));
dimensionElementColumn.MemberProperties.Add(new MemberProperty("Standard Cost", "[Product].[Product Categories].[Standard Cost]"));

// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);

///Adding Column Members
olapReport.CategoricalElements.Add(measureElementColumn);
```

- VB Example:
```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Employee Sales Report"
' Specifying the current cube name
olapReport.CurrentCubeName = "Adventure Works"

Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the Name for the Measure Element
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Sales Amount Quota"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Dimension Name
dimensionElementRow.Name = "Employee"
' Specifying the Hierarchy and level name for the Dimension Element
dimensionElementRow.AddLevel("Employees", "Employee Level 02")
dimensionElementRow.Hierarchy.LevelElements("Employee Level 02").
```

<!-- tags: [product, olap, syncfusion, winforms, reporting, dimension, hierarchy, elements, measure, element, property] keywords: [OlapReport, DimensionElement, MeasureElements, SeriesElements, CategoricalElements, MemberProperty, LevelElements] -->
```