```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: Olap Common
page_number: 032
page_id: Olap Common#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:38Z
fidelity: lossless
-->

# Essential OlapCommon

## Calculated Dimension

```csharp
[C#]
DimensionElement internalDimension = new DimensionElement();
internalDimension.Name = "Product";
internalDimension.AddLevel("Product Categories", "Category");
// Calculated Dimension
CalculatedMember calculateDimension = new CalculatedMember();
calculateDimension.Name = "Bikes & Components";
calculateDimension.Expression = "([Product].[Product Categories].[Category].[Bikes] + [Product].[Product Categories].[Category].[Components] )";
calculateDimension.AddElement(internalDimension);
olapReport.CalculatedMembers.Add(calculateDimension)
```

```vb
[VB]
Dim internalDimension As DimensionElement = New DimensionElement()
internalDimension.Name = "Product"
internalDimension.AddLevel("Product Categories", "Category")
' Calculated Dimension
Dim calculateDimension As CalculatedMember = New CalculatedMember()
calculateDimension.Expression = "Bikes & Components"
calculateDimension.Expression = "([Product].[Product Categories].[Category].[Bikes] + [Product].[Product Categories].[Category].[Components] )"
calculateDimension.AddElement(internalDimension)
olapReport.CalculatedMembers.Add(calculateDimension)
```

### 4.3.8 Subset Element

Subset Elements are used to filter the result set by their count. It will just filter the number records and number of fields in the result set.

The following codes will illustrate the creation of a Subset Element:

```csharp
[C#]
SubsetElement subSetElementColumn = new SubsetElement(5);
subSetElementColumn.Name = "Top 5 Elements";
```

## API Reference

## Code Examples

<!-- tags: [product, module, control, api, version?] keywords: [calculated dimension, subset element, OlapCommon, Syncfusion Winforms] -->
```