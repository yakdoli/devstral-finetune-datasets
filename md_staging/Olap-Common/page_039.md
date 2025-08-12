```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: Olap Common
page_number: 039
page_id: Olap Common#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:45Z
fidelity: lossless
-->

## Overview
- Demonstrates how to configure categorical elements, series elements, slicer elements, and measure elements for a report in an OLAP environment using C# and VB.NET.

## Content

### Example Code

#### C#
The following C# code demonstrates how to configure categorical elements, series elements, slicer elements, and measure elements for an OLAP report:

```csharp
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.SeriesElements.Add(dimensionElementRow);
olapReport.SlicerElements.Add(dimensionElementSlicer);
olapReport.SeriesElements.Add(measureElementRow);
```

#### VB.NET
The following VB.NET code demonstrates the same configuration for an OLAP report:

```vb
Dim olapReport As OlapReport = New OlapReport()

olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()

' Specifying the dimension Name
dimensionElementColumn.Name = "Customer"

' Adding the Level Name along with the Hierarchy Name
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim dimensionElementRow As DimensionElement = New DimensionElement()

' Specifying the dimension Name
dimensionElementRow.Name = "Date"

' Adding the Level Name along with the Hierarchy Name
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim dimensionElementSlicer As DimensionElement = New DimensionElement()
dimensionElementSlicer.Name = "Sales Channel"
dimensionElementSlicer.AddLevel("Sales Channel", "Sales Channel")

Dim measureElementRow As MeasureElements = New MeasureElements()
measureElementRow.Elements.Add(New MeasureElement() { Name = "Internet Sales Amount" });
```

## API Reference

### OlapReport
- **Namespace**: Syncfusion.Olap
- **Description**: Represents an OLAP report with configurable elements.

#### Properties
- **CategoricalElements**: Collection of categorical elements.
- **SeriesElements**: Collection of series elements.
- **SlicerElements**: Collection of slicer elements.

#### Methods
- **Add(dimensionElement)**: Adds a dimension element to the collection.

### DimensionElement
- **Namespace**: Syncfusion.Olap
- **Description**: Represents a dimension element.

#### Properties
- **Name**: Specifies the name of the dimension.
- **Levels**: Collection of level names associated with the hierarchy.

#### Methods
- **AddLevel(hierarchyName, levelName)**: Adds a level to the dimension element.

### MeasureElement
- **Namespace**: Syncfusion.Olap
- **Description**: Represents a measure element.

#### Properties
- **Name**: The name of the measure.

## Code Examples

### C#
```csharp
// Example configuration for an OLAP report
OlapReport olapReport = new OlapReport();

olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

DimensionElement dimensionElementRow = new DimensionElement();
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

DimensionElement dimensionElementSlicer = new DimensionElement();
dimensionElementSlicer.Name = "Sales Channel";
dimensionElementSlicer.AddLevel("Sales Channel", "Sales Channel");

MeasureElements measureElementRow = new MeasureElements();
measureElementRow.Elements.Add(new MeasureElement() { Name = "Internet Sales Amount" });

// Adding elements to the report
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.SeriesElements.Add(dimensionElementRow);
olapReport.SlicerElements.Add(dimensionElementSlicer);
olapReport.SeriesElements.Add(measureElementRow);
```

### VB.NET
```vb
Dim olapReport As OlapReport = New OlapReport()

olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim dimensionElementRow As DimensionElement = New DimensionElement()
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

Dim dimensionElementSlicer As DimensionElement = New DimensionElement()
dimensionElementSlicer.Name = "Sales Channel"
dimensionElementSlicer.AddLevel("Sales Channel", "Sales Channel")

Dim measureElementRow As MeasureElements = New MeasureElements()
measureElementRow.Elements.Add(New MeasureElement() { Name = "Internet Sales Amount" })

' Adding elements to the report
olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.SeriesElements.Add(dimensionElementRow)
olapReport.SlicerElements.Add(dimensionElementSlicer)
olapReport.SeriesElements.Add(measureElementRow)
```

### Example: Configuring Elements
The examples above demonstrate how to:
1. Create an `OlapReport` instance.
2. Specify the report name and current cube.
3. Configure categorical, series, and slicer dimensions.
4. Add measure elements for specific data analysis.

<!-- tags: OlapReport, DimensionElement, MeasureElement, C#, VB.NET, OLAP, Syncfusion Winforms, version: 11.4.0.26 -->
```