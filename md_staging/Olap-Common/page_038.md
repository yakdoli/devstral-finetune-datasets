```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_038.jpeg
document_name: Olap Common
page_number: 038
page_id: Olap Common#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:01Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
ernet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
// Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

''' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
''' Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)
''' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

## 4.3.11.1.2 Report with slicing operation

[C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the dimension Name
dimensionElementColumn.Name = "Customer";
// Adding the Level Name along with the Hierarchy Name
dimensionElementColumn.AddLevel("Customer Geography", "Country");

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the dimension Name
dimensionElementRow.Name = "Date";
// Adding the Level Name along with the Hierarchy Name
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

DimensionElement dimensionElementSlicer = new DimensionElement();
dimensionElementSlicer.Name = "Sales Channel";
dimensionElementSlicer.AddLevel("Sales Channel", "Sales Channel");

MeasureElements measureElementRow = new MeasureElements();
measureElementRow.Elements.Add(new MeasureElement { Name = "Internet Sa les Amount" });
```

## API Reference (if applicable)
- Refer to the relevant namespaces and classes pertaining to `OlapReport`, `DimensionElement`, `MeasureElement`, and related methods used in the examples above.

## Code Examples (straddle user context controls)
- Ensure that any code examples provided in this section integrate properly with the Syncfusion.Winforms framework and comply with the specified configurations and version constraints.

<!-- tags: [Olap, Report, Slicing, DimensionElement, MeasureElement, WinForms, Syncfusion] keywords: [OlapReport, DimensionElement, MeasureElements, Fiscal, Customer Report, Adventure Works, Sales Channel] -->
```