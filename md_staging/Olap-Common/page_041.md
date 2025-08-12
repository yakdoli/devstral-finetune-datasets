```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: Olap Common
page_number: 041
page_id: Olap Common#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:33Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Demonstrates specifying excluded row elements in an OLAP report.
- Adding the date dimension element with fiscal year, month, fiscal quarter, and fiscal semester hierarchy levels.
- Creating column and measure elements.
- Adding row members to the report.

## Content

### Specifying Excluded Row Elements

The following code snippet demonstrates how to specify excluded row elements in an OLAP report:

```csharp
// Specifying the Excluded row elements
DimensionElement excludedRowElement = new DimensionElement();
excludedRowElement.Name = "Date";
excludedRowElement.AddLevel("Fiscal", "Fiscal Year");
excludedRowElement.AddLevel("Fiscal", "Month");
excludedRowElement.AddLevel("Fiscal", "Fiscal Quarter");
excludedRowElement.AddLevel("Fiscal", "Fiscal Semester");
excludedRowElement.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2002");
excludedRowElement.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2004");
excludedRowElement.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2005");
excludedRowElement.Hierarchy.LevelElements["Fiscal Semester"].Add("H2 FY 2003");
excludedRowElement.Hierarchy.LevelElements["Month"].Add("August 2002");
excludedRowElement.Hierarchy.LevelElements["Month"].Add("September 2002");
excludedRowElement.Hierarchy.LevelElements["Fiscal Quarter"].Add("Q2 FY 2003");
excludedRowElement.Hierarchy.LevelElements["Fiscal Quarter"].Add("Q2 FY 2003");

/// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn, excludedColumn);
/// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
/// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow, excludedRowElement);
```

### VB Example

The following Visual Basic code snippet demonstrates the configuration of an OLAP report, similar to the above example:

```vb
[VB]

Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
' Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")
```

## API Reference

### Methods
- `AddLevel(hierarchyName, levelName)`: Adds a level to the specified hierarchy.
- `Add`: Adds elements to the `CategoricalElements` or `SeriesElements` collections.

## Code Examples

### C# Example
```csharp
DimensionElement excludedRowElement = new DimensionElement();
excludedRowElement.Name = "Date";
excludedRowElement.AddLevel("Fiscal", "Fiscal Year");
excludedRowElement.AddLevel("Fiscal", "Month");
excludedRowElement.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2002");
// ... other level additions
olapReport.SeriesElements.Add(dimensionElementRow, excludedRowElement);
```

### VB Example
```vb
Dim olapReport As OlapReport = New OlapReport()
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")
```

## Cross References

- Refer to the main OLAP documentation for detailed explanations on hierarchy and element configurations.

<!-- tags: [Olap, OLAPReport, DimensionElement, Hierarchy, Level, MeasureElement, SeriesElements] keywords: [Fiscal Year, Month, Fiscal Quarter, Fiscal Semester, Customer Geography, Country, Customer, Report] -->
```