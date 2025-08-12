```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: Olap Common
page_number: 048
page_id: Olap Common#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:49Z
fidelity: lossless
-->

## Essential OlapCommon

### Code Example: C#

```csharp
"Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
//Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

//Specifying the SubsetElement
//Specify the start index and end index to retrieve the records.
SubsetElement subSetElementColumn = new SubsetElement(5);
subSetElementColumn.Name = "Top 5 Elements";

SubsetElement subSetElementRow = new SubsetElement(3);
subSetElementRow.Name = "Top 3 Elements";

///Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
///Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
olapReport.CategoricalElements.SubSetElement = subSetElementColumn;
///Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
olapReport.SeriesElements.SubSetElement = subSetElementRow;
```

### Code Example: VB

```vb
[VB]

Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

'Creating Measure Element
Dim olapReport As OlapReport = New OlapReport()
olapReport.CurrentCubeName = "Adventure Works"
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
```

### Summary: Key Points
- **DimensionElement** and **SubsetElement** are used to define the structure of the OLAP report.
- **DimensionElement** is used to specify the dimensions (e.g., "Date," "Fiscal Year," "Customer," "Country").
- **SubsetElement** is used to define the subset of elements to be retrieved (e.g., "Top 5 Elements").
- **MeasureElement** is also defined to specify the measure for the report.
- Both C# and VB examples are provided to illustrate the creation of an OLAP report using the Essential OlapCommon library.

---

<!-- tags: [syncfusion, olapcommon, dimensionelement, subsetelement, measelement, olapreport, winforms] keywords: [dimension, measure, subset, olap] -->
```