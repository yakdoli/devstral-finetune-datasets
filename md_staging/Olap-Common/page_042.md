```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: Olap Common
page_number: 042
page_id: Olap Common#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:16Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement { Name = "Internet Sales Amount" })
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})

Dim dimensionElementRow As DimensionElement = New DimensionElement()
'Specifying the Dimension Name
dimensionElementRow.Name = "Date"
dimensionElementRow.HierarchyName = "Fiscal"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")

'Specifying Excluded column elements
Dim excludedColumnElement As DimensionElement = New DimensionElement()
excludedColumnElement.Name = "Customer"
excludedColumnElement.HierarchyName = "Customer Geography"
excludedColumnElement.AddLevel("Customer Geography", "Country")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("Canada")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("France")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("United Kingdom")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("United States")

'Specifying the Excluded row elements
Dim excludedRowElement As DimensionElement = New DimensionElement()
excludedRowElement.Name = "Date"
excludedRowElement.AddLevel("Fiscal", "Fiscal Year")
excludedRowElement.AddLevel("Fiscal", "Month")
excludedRowElement.AddLevel("Fiscal", "Fiscal Quarter")
excludedRowElement.AddLevel("Fiscal", "Fiscal Semester")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY 2002")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY
```

## API Reference (if applicable)

```vb
Namespace:
- MeasureElements
- MeasureElement
- DimensionElement
- Hierarchy
- LevelElements
```

## Code Examples

### Example 1: Defining Measure Elements

```vb
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement { Name = "Internet Sales Amount" })
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

### Example 2: Specifying a Dimension Row

```vb
Dim dimensionElementRow As DimensionElement = New DimensionElement()
dimensionElementRow.Name = "Date"
dimensionElementRow.HierarchyName = "Fiscal"
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")
```

### Example 3: Specifying Excluded Column Elements

```vb
Dim excludedColumnElement As DimensionElement = New DimensionElement()
excludedColumnElement.Name = "Customer"
excludedColumnElement.HierarchyName = "Customer Geography"
excludedColumnElement.AddLevel("Customer Geography", "Country")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("Canada")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("France")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("United Kingdom")
excludedColumnElement.Hierarchy.LevelElements("Country").Add("United States")
```

### Example 4: Specifying Excluded Row Elements

```vb
Dim excludedRowElement As DimensionElement = New DimensionElement()
excludedRowElement.Name = "Date"
excludedRowElement.AddLevel("Fiscal", "Fiscal Year")
excludedRowElement.AddLevel("Fiscal", "Month")
excludedRowElement.AddLevel("Fiscal", "Fiscal Quarter")
excludedRowElement.AddLevel("Fiscal", "Fiscal Semester")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY 2002")
excludedRowElement.Hierarchy.LevelElements("Fiscal Year").Add("FY")
```

### Notes
- The code examples demonstrate how to define various elements in an OLAP context, such as Measure Elements, Dimension Elements, and specifying excluded elements for both rows and columns.
- The examples use VB.NET, which is consistent with Syncfusion WinForms development.
- The Hierarchy and LevelElements are used to specify the structure and levels within dimensions.

<!-- tags: [OlapCommon, WinForms, MeasureElements, DimensionElement, Hierarchy, LevelElements, UserGuide] keywords: [MeasureElement, DimensionElement, Hierarchy, LevelElements, excluded elements, OLAP context, VB.NET] -->
```