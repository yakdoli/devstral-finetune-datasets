```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: Olap Common
page_number: 044
page_id: Olap Common#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:23Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Create and configure elements for OLAP reports using the Syncfusion WinForms library.
- Define columns, measures, dimensions, and sorting using `DimensionElement` and `MeasureElement`.
- Add row elements with hierarchical levels for categorizing data.

## Content

### Creating and Configuring OLAP Report Elements

Here, we are demonstrating how to configure various elements for creating an OLAP report.

```csharp
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet<br>Sales Amount" });
DimensionElement dimensionElementRow = new DimensionElement();

// Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

SortElement sortElement = new SortElement(AxisPosition.Categorical, SortOrder.BDESC, true);
sortElement.Element.UniqueName = "[Measures].[Internet Sales Amount]";

// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
// Adding Sort Element
olapReport.CategoricalElements.Add(sortElement);
// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

### Configuring Elements in VB.NET

The following VB.NET code snippet shows how to create and configure the same OLAP report elements:

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()

' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"

' Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

' Creating Measure Elements
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet<br>Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
```

## API Reference

### Namespaces and Classes
- **OlapReport**
  - Methods and Properties:
    - `Name` (String): Gets or sets the name of the report.
    - `CurrentCubeName` (String): Specifies the cube name to use for the report.
    - `CategoricalElements` (Collection): Contains elements configured for the categorical axis.
    - `SeriesElements` (Collection): Contains elements configured for the series axis.

### Methods
- **AddLevel**(String name, String levelName): Adds a hierarchical level to the dimension element.
- **SortElement**(AxisPosition position, SortOrder order, Boolean includeChildren): Creates a sort element for sorting data.

### Parameters
- **MeasureElement**:
  - Name (String): Name of the measure to display in the report.

## Code Examples

### C# Example

```csharp
var measureElementColumn = new DimensionElement();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });
var dimensionElementRow = new DimensionElement();
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

var sortElement = new SortElement(AxisPosition.Categorical, SortOrder.BDESC, true);
sortElement.Element.UniqueName = "[Measures].[Internet Sales Amount]";

olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.Add(measureElementColumn);
olapReport.CategoricalElements.Add(sortElement);
olapReport.SeriesElements.Add(dimensionElementRow);
```

### VB.NET Example

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()

dimensionElementColumn.Name = "Customer"
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
```

## RAG Annotations
<!-- tags: [syncfusion-sdk, winforms, olapreport, dimensionelement, measureelement, sortelement, version: 11.4.0.26] keywords: [olap report, dimension, measure, sorting, hierarchy, axes, categorization, data analysis, business intelligence, vb.net, c#, olap, cube] -->
```