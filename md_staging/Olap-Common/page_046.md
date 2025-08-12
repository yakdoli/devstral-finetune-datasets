```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_046.jpeg
document_name: Olap Common
page_number: 046
page_id: Olap Common#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:38Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");

FilterElement filterElement = new FilterElement(AxisPosition.Categorical);
filterElement.Elements.Add(measureElementColumn);
filterElement.Elements.Add(dimensionElementColumn);
filterElement.FilterCase = FilterCase.GreaterThan;
filterElement.FilterValue.Add(new MeasureElement { Name = "Internet Sales Amount", Visible = true });
filterElement.FilterValue.Add(new FilterValue { Filter_Value = 2700000.00 });
filterElement.IsFilterCondition = true;
// Adding Column Members
olapReport.CategoricalElements.Add(new Item { ElementValue = dimensionElementColumn });
olapReport.CategoricalElements.IsFilterOrSortOn = true;
olapReport.FilterElements.Add(new Item { ElementValue = filterElement });

olapReport.SeriesElements.Add(dimensionElementRow);
```

### VB

```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Customer Report"
olapReport.CurrentCubeName = "Adventure Works"

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
'Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

'Creating Measure Element
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
```

## API Reference (if applicable)
- **Namespace**: OlapCommon
- **Class**: OlapReport
  - **Properties**
    - `Name`: String
    - `CurrentCubeName`: String
    - `CategoricalElements`: ICollection(Of Item)
    - `FilterElements`: ICollection(Of Item)
    - `SeriesElements`: ICollection(Of DimensionElement)
  - **Methods**
    - `AddLevel(levelName, levelDescription)`: Adds a level to a dimension.
    - `AddItem(elementValue)`: Adds a categorical item.
    - `AddFilterElement(filterElement)`: Adds a filter condition.
  - **Events**
    - `FilterConditionChanged`: Triggered when the filter condition changes.
    - `SeriesElementAdded`: Triggered when a new series element is added.

## Code Examples (multi-language supported)

### C#
```csharp
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
```

### VB
```vb
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.AddLevel("Customer Geography", "Country")
```

<!-- tags: [OlapCommon, OlapReport, DimensionElement, MeasureElements, FilterElements, C#, VB] keywords: [dimension, level, filter, measure, series, addition, categorical, elements, report] -->
```