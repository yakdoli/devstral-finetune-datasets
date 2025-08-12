```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: Olap Common
page_number: 026
page_id: Olap Common#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:20Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Explains the hierarchical structure of a dimension.
- Demonstrates the creation of simple dimension elements using code.
- Illustrates the relationship between dimension elements, hierarchy elements, and level elements.

## Content

### Hierarchical Structure of a Dimension

![Figure 5: Hierarchical structure of a dimension](#)  
Figure 5: Hierarchical structure of a dimension

The following code will illustrate the creation of different types of dimensions:

#### Creating Simple Dimension Element

[C#]

```csharp
DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for Column Dimension Element
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy and Level Element Name
dimensionElementColumn.AddLevel("Customer Geography", "Country");
```

## API Reference (if applicable)
- Methods such as `AddLevel()` are used to define the hierarchy and levels within a dimension.

## Code Examples (multi-language supported)
- Provided C# code snippet for creating a simple dimension element.

## Page-level Navigation/TOC (if applicable)
- Refer to the "Hierarchical structure of a dimension" for visual representation.

## Cross References
- See also: Documentation for `DimensionElement`, `AddLevel()` method, and other relevant classes and methods.

<!-- tags: [Olap Common, dimension structure, dimension element, hierarchy, level element, code example, Winforms, version: 11.4.0.26] keywords: [dimension, hierarchy, level, element, structure, creation, code example, C#] -->
```