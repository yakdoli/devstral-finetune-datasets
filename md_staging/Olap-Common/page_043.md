```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: Olap Common
page_number: 043
page_id: Olap Common#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:14Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY 2004")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY 2005")
excludedRowElement.Hierarchy.LevelElements("Fiscal Semester").Add("H2 FY 2003")
excludedRowElement.Hierarchy.LevelElements("Month").Add("August 2002")
excludedRowElement.Hierarchy.LevelElements("Month").Add("September 2002")
excludedRowElement.Hierarchy.LevelElements("Fiscal Quarter").Add("Q2 FY 2003")
excludedRowElement.Hierarchy.LevelElements("Fiscal Quarter").Add("Q2 FY 2003")
```

#### Adding Column Members
```csharp
olapReport.CategoricalElements.Add(dimensionElementColumn, excludedColumn)
```

#### Adding Measure Element
```csharp
olapReport.CategoricalElements.Add(measureElementColumn)
```

#### Adding Row Members
```csharp
olapReport.SeriesElements.Add(dimensionElementRow, excludedRowElement)
```

## 4.3.11.1.4 Ordered Report

```csharp
[C#]

OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";
DimensionElement dimensionElementColumn = new DimensionElement();

// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

// Creating Measure Elements
MeasureElements measureElementColumn = new MeasureElements();
```

## Page-level Navigation/TOC (if applicable)
- This section provides examples of Ordered Reports
- Demonstrates how to specify dimensions, hierarchies, and measures

### Cross References
- Refer to Chapter 4 for more on OlapReport configurations
- See also: Related topics in the user guide

<!-- tags: [OlapReport, Ordered Report, Dimension, Hierarchy, Measure, Syncfusion Winforms, 11.4.0.26] keywords: [OlapCommon, Ordered Report, DimensionElement, Customer Geography, MeasureElements, C#, Syncfusion] -->
```