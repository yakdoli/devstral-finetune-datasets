```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: Olap Common
page_number: 028
page_id: Olap Common#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:23Z
fidelity: lossless
-->

# Essential OlapCommon

```vb
Dim dimensionElementSlicer As DimensionElement = New DimensionElement()
' Specifying the dimension Name
dimensionElementSlicer.Name = "Product"
' Adding the Level Name along with the Hierarchy Name
dimensionElementSlicer.AddLevel("Product Categories", "Category")
' Adding the Member Element
dimensionElementSlicer.Hierarchy.LevelElements("Category").Add("Bikes")
dimensionElementSlicer.Hierarchy.LevelElements("Category").IncludeAvailableMembers = True
```

## 4.3.3 Measure Element

In a cube, a measure is a set of values that are based on a column in the cube's **fact table** and are usually numeric. In addition, measures are the central values of a cube that are analyzed. That is, measures are the numeric data of primary interest to end users browsing a cube. The measures you select depend on the types of information end users request. Some common measures are sales, cost, expenditures, and production count.

We can create a measure element just by specifying its name. The following code will illustrate the creation of a measure element:

### C#

```csharp
MeasureElements measureElementColumn = new MeasureElements();
//Specifying the Measure Elements
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });
```

### VB

```vb
Dim measureElementColumn As MeasureElements = New MeasureElements()
' Specifying the Measure Elements
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

## API Reference

### Namespaces and Classes
- `MeasureElements`
- `MeasureElement`

### Properties
#### MeasureElement
- `Name` (Type: String)
  - Specifies the name of the measure element.

### Methods
#### MeasureElements
- `Add(MeasureElement element)`
  - Adds a new measure element to the collection.

### Example Usage

#### Creating a Measure Element
```csharp
MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });
```

```vb
Dim measureElementColumn As MeasureElements = New MeasureElements()
measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})
```

<!-- tags: [OlapCommon, MeasureElement, DimensionElement, Cube, FactTable] keywords: [measure, fact table, numeric data, end users, sales, cost, expenditures, production count, measure element, dimension element, cube, fact table] -->
```