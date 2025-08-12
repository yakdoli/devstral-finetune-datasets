```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: Olap Common
page_number: 037
page_id: Olap Common#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:14Z
fidelity: lossless
-->

## Content

### 4.3.11.1.1 Simple Report

[C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
//Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
//Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

//// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
//// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
//// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

[VB]

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

---

## API Reference

### Namespaces and Classes

- **Namespace**: `OlapReport`
- **Class**: `OlapReport`
- **Properties**:
  - `Name`: Specifies the name of the report.
  - `CurrentCubeName`: Specifies the name of the current cube.
- **Methods**:
  - `AddLevel(hierarchyName, levelName)`: Adds a specific level to the dimension element.
  - `CategoricalElements.Add(dimensionElement)`: Adds column or measure elements to the report.
  - `SeriesElements.Add(dimensionElement)`: Adds row elements to the report.

### Parameters

- **Name**: 
  - **Type**: `string`
  - **Description**: The name of the report.
  - **Default**: None
  - **Required**: Yes
- **CurrentCubeName**: 
  - **Type**: `string`
  - **Description**: The name of the cube used in the report.
  - **Default**: None
  - **Required**: Yes

### Exceptions

- None explicitly listed. Ensure proper handling of null or invalid inputs.

---

## Code Examples (continued)

The above code samples demonstrate how to set up a simple report using the `OlapReport` class in both C# and VB. These examples illustrate how to specify the cube name, dimension elements, measure elements, and row/column configurations required for generating the report.

---

## Cross References

- For detailed information about OLAP concepts and terminology, refer to the official documentation or related sections in this guide.
- Additional examples and advanced configurations can be found in the API reference and examples provided with Syncfusion WinForms.

<!-- tags: [Syncfusion, Winforms, OLAP, Report, Dimension, Measure] keywords: [OlapReport, DimensionElement, MeasureElements, CurrentCubeName, AddLevel, CategoricalElements, SeriesElements] -->
```