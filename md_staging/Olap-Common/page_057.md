```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: Olap Common
page_number: 057
page_id: Olap Common#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:30Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview

- Adding calculated members in a collection using C# code.
- Demonstrating the configuration of categorical and series elements for reports.

## Content

### Adding Calculated Members in Calculated Member Collection

The following C# code snippet shows how to add calculated members to the `CalculatedRouteMembers` collection.

```csharp
//// Adding Calculated members in calculated member collection
olapReport.CalculatedMembers.Add(calculatedMeasure1);
olapReport.CalculatedMembers.Add(calculateDimension);
olapReport.CalculatedMembers.Add(calculatedMeasure2);

//// Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.Add(calculateDimension);
//// Adding Measure Element
olapReport.CategoricalElements.Add(measureElementColumn);
olapReport.CategoricalElements.Add(calculatedMeasure1);
olapReport.CategoricalElements.Add(calculatedMeasure2);

//// Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow);
```

### VB Code Implementation

The following VB code snippet provides details on configuring dimension elements and adding calculated measures.

```vb
[VB]

Dim dimensionElementColumn As DimensionElement = New DimensionElement()
' Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer"
dimensionElementColumn.HierarchyName = "Customer Geography"
dimensionElementColumn.AddLevel("Customer Geography", "Country")

Dim internalDimension As DimensionElement = New DimensionElement()
internalDimension.Name = "Product"
internalDimension.AddLevel("Product Categories", "Category")

' Calculated Measure
Dim calculatedMeasure1 As CalculatedMember = New CalculatedMember()
calculatedMeasure1.Name = "Oder on Discount"
calculatedMeasure1.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)"
calculatedMeasure1.AddElement(New MeasureElement With {.Name = "Order Quantity"})
```

### Explanation of the Code

- **DimensionElement Column**: Configures the dimension element for "Customer," specifying the hierarchy and level.
- **DimensionElement Row**: Configures the dimension element for "Product," specifying another hierarchy and level.
- **Calculated Measure**: Defines a calculated member named "Oder on Discount," calculating the order quantity plus 10% of the order quantity.

## API Reference

### Namespaces and Classes Used

- `DimensionElement`: Represents a dimension element for configuring categorical elements.
- `CalculatedMember`: Represents a calculated member for adding to the `CalculatedMembers` collection.

### Methods Used

- `Add(...)`:
  - Adds elements to the collection.
  - Parameters include `DimensionElement` or `CalculatedMember` objects based on context.

### Properties Set

- `Name`: Specifies the name of the dimension element or calculated member.
- `HierarchyName`: Specifies the hierarchy associated with the dimension element.
- `AddLevel(...)`: Associates a hierarchy level with the dimension element.
- `Expression`: Specifies the formula for calculating the value of a calculated member.

## Code Examples

### C# Example

```csharp
olapReport.CalculatedMembers.Add(calculatedMeasure1);
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.SeriesElements.Add(dimensionElementRow);
```

### VB Example

```vb
Dim dimensionElementColumn As DimensionElement = New DimensionElement()
internalDimension.Name = "Product"
calculatedMeasure1.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)"
calculatedMeasure1.AddElement(New MeasureElement With {.Name = "Order Quantity"})
```

---

<!-- tags: [OLAP, dimension elements, calculated members, VB, C#] keywords: [calculated members, dimension elements, hierarchy, level, expression, calculated measures] -->
```