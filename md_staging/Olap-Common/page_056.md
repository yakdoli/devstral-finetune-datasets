```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: Olap Common
page_number: 056
page_id: Olap Common#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:21Z
fidelity: lossless
-->

# Essential OlapCommon

## Content

### 4.3.11.1.10 Report with calculated member

```csharp
[C#]

olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

DimensionElement internalDimension = new DimensionElement();
internalDimension.Name = "Product";
internalDimension.AddLevel("Product Categories", "Category");

/// Calculated Measure
CalculatedMember calculatedMeasure1 = new CalculatedMember();
calculatedMeasure1.Name = "Order on Discount";
calculatedMeasure1.Expression = "[Measures].[Order Quantity] + ([Measures].[Order Quantity] * 0.10)";
calculatedMeasure1.AddElement(new MeasureElement { Name = "Order Quantity" });

/// Calculated Measure
CalculatedMember calculatedMeasure2 = new CalculatedMember();
calculatedMeasure2.Name = "Sales Range";
calculatedMeasure2.AddElement(new MeasureElement { Name = "Sales Amount" });
calculatedMeasure2.Expression = "IIF([Measures].[Sales Amount]>200000, \"High\", \"Low\")";

// Calculated Dimension
CalculatedMember calculateDimension = new CalculatedMember();
calculateDimension.Name = "Bikes & Components";
calculateDimension.Expression = "([Product].[Product Categories].[Category].[Bikes] + [Product].[Product Categories].[Category].[Components] )";
calculateDimension.AddElement(internalDimension);

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Sales Amount" });
measureElementColumn.Elements.Add(new MeasureElement { Name = "Order Quantity" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
```

## API Reference

### Namespaces and Classes

- **Namespace**: 
- **Class**: DimensionElement
- **Class**: CalculatedMember
- **Class**: MeasureElement
- **Class**: MeasureElements

### Methods

- AddElement
- AddLevel
- Add

### Properties

- Name
- HierarchyName

### Events

- None

## Code Examples

### C# Example

The provided C# code demonstrates how to create and configure a report with calculated members in an Olap report. It includes setting up dimension elements, calculated members, and measure elements. This example showcases how to define and compute derived metrics such as "Order on Discount" and "Sales Range," and how to handle calculated dimensions.

### Explanation

- **Setting Up Dimension Elements**: The code initializes dimension elements for the cube, specifying hierarchies and levels such as "Customer Geography" with the level "Country," and "Product Categories" with the level "Category."

- **Calculated Measures**: The code defines two calculated measures:
  - **Order on Discount**: Calculates the total order quantity with a 10% discount applied.
  - **Sales Range**: Categorizes sales amounts as "High" or "Low" based on a threshold of 200,000.

- **Calculated Dimension**: The code creates a calculated dimension combining two categories ("Bikes" and "Components") under the "Product Categories" dimension.

- **Measure Elements**: The example includes measure elements like "Sales Amount" and "Order Quantity," which are essential for populating the report.

## Summary

This section demonstrates the use of calculated members in an Olap report within Syncfusion WinForms. By defining dimension elements, measures, and calculated dimensions, users can create dynamic and flexible reports tailored to specific requirements.

---

<!-- tags: [olap, olapreport, calculatedmember, dimensionelement, measureelement, measureelements, syncfusionwinforms, v11.4.0.26] keywords: [calculated members, olap report, dimension elements, measures, calculated dimensions, olap cube, syncfusion winforms] -->
```