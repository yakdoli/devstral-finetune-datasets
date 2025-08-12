```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: Olap Common
page_number: 027
page_id: Olap Common#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:04Z
fidelity: lossless
-->

## Essential OlapCommon

### Creating Sliced Dimension

#### [VB]

```vb
Dim dimensionElementRow As DimensionElement = New DimensionElement()
' Specifying the Name for Row Dimension Element
dimensionElementRow.Name = "Date"
' Specifying the Hierarchy and Level Element Name
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")
```

#### [C#]

```csharp
DimensionElement dimensionElementSlicer = new DimensionElement();
// Specifying the dimension Name
dimensionElementSlicer.Name = "Product";
// Adding the Level Name along with the Hierarchy Name
dimensionElementSlicer.AddLevel("Product Categories", "Category");
// Adding the Member Element
dimensionElementSlicer.Hierarchy.LevelElements["Category"].Add("Bikes");
dimensionElementSlicer.Hierarchy.LevelElements["Category"].IncludeAvailableMembers = true;
```

<!-- tags: [Olap, Dimension, Slicer, Hierarchy, Level, Element, Product, Category, Row, DimensionElement] keywords: [dimension, slicer, hierarchy, level, element, product, category, row, DimensionElement, OlapCommon] -->
```