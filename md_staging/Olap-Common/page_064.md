```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: Olap Common
page_number: 064
page_id: Olap Common#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:59Z
fidelity: lossless
-->

### Overview
- Configures dimension elements and hierarchy levels using `HierarchyElement` and `LevelElement`.
- Demonstrates adding row and column dimension elements with their respective hierarchies.
- Includes summary elements with specific columns and formatting.

### Content

#### Defining Dimensions and Hierarchies in C#
```csharp
dimensionElementRow.Name = "Geography";
dimensionElementRow.Hierarchy = new HierarchyElement() { Name = "Product Hierarchy" };

dimensionElementRow.Hierarchy.LevelElements.Add(new LevelElement() { Name = "Product" });
dimensionElementRow.Hierarchy.LevelElements.Add(new LevelElement() { Name = "Date" });

// Specifying the Column Dimension Element
DimensionElement dimensionElementColumn = new DimensionElement();
dimensionElementColumn.Name = "Geography";
dimensionElementColumn.Hierarchy = new HierarchyElement() { Name = "Geography Hierarchy" };

dimensionElementColumn.Hierarchy.LevelElements.Add(
    new LevelElement() { Name = "Country" });
dimensionElementColumn.Hierarchy.LevelElements.Add(
    new LevelElement() { Name = "State" });

// Specifying the Summary Elements
SummaryElements summaries = new SummaryElements();
summaries.Add(new SummaryInfo { Column = "Quantity", Key = "Quantity", Type = SummaryType.Sum });
summaries.Add(new SummaryInfo { Column = "Amount", Key = "Amount", Type = SummaryType.Sum, FormatString = "{0:c}" });

// Adding the Row Elements
olapReport.SeriesElements.Add(new Item { ElementValue = summaries });
```

#### Defining Dimensions and Hierarchies in VB.NET
```vb
Dim olapReport As OlapReport = New OlapReport()
olapReport.Name = "Sales Report"

' Specifying the Row Dimension Element
Dim dimensionElementRow As DimensionElement = New DimensionElement()
dimensionElementRow.Name = "Geography"
dimensionElementRow.Hierarchy = New HierarchyElement() With {.Name = "Product Hierarchy"}

dimensionElementRow.Hierarchy.LevelElements.Add(
    New LevelElement() With {.Name = "Product"})
dimensionElementRow.Hierarchy.LevelElements.Add(
    New LevelElement() With {.Name = "Time"})
```

### API Reference
#### Types Used
- **DimensionElement**: Represents a dimension element with hierarchy and levels.
- **HierarchyElement**: Represents a hierarchy within a dimension.
- **LevelElement**: Represents a level within a hierarchy.
- **SummaryElements**: Collection of summary elements.
- **SummaryInfo**: Represents information about a summary column.

### Code Examples

#### C#
The provided C# example shows how to create a row and column dimension element, define hierarchies and levels, add summary elements, and integrate them into an `OlapReport`.

#### VB.NET
The VB.NET example illustrates the creation of a dimension element, a hierarchy, and levels using the `With` keyword for object initialization. It provides a clearer way to define properties and relationships within the hierarchy structure.

### Cross References
- Additional resources on configuring dimension elements and summary elements can be found in the `OlapReport` documentation.

<!-- tags: [syncfusion, winforms, olapreport, dimensionelement, hierarchyelement, levelelement] keywords: [dimension, hierarchy, levels, summary elements, olap report, csharp, vb.net] -->
```