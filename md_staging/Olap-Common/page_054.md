```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: Olap Common
page_number: 054
page_id: Olap Common#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:17Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim topCountElement As TopCountElement = New TopCountElement(AxisPosition.Categorical, 5)
topCountElement.MeasureName = "Internet Sales Amount"

'' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)

'' Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn)

'' Adding Measure Element
olapReport.CategoricalElements.Add(topCountElement)

'' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

### 4.3.11.1.9 Report with Named set

#### [C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the dimension Name
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
// Specifying the measure elements
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

// Specifying the NamedSet Element
NamedSetElement dimensionElementRow = new NamedSetElement();
// Specifying the dimension name
dimensionElementRow.Name = "Core Product Group";

/// Adding the Column members
olapReport.CategoricalElements.Add(dimensionElementColumn);
/// Adding the Measure elements
olapReport.CategoricalElements.Add(measureElementColumn);
/// Adding the Row members
```

<!-- tags: [product, module, control, api, version?] keywords: [OlapReport, DimensionElement, MeasureElements, NamedSetElement, AxisPosition, Categorical, TopCountElement, Customer Geography, Core Product Group, Internet Sales Amount] -->
```