```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: Olap Common
page_number: 061
page_id: Olap Common#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:53Z
fidelity: lossless
-->

# Essential OlapCommon

## Code Examples

```csharp
' Adding Column Members
olapReport.CategoricalElements.Add(dimensionElementColumn)
olapReport.CategoricalElements.Add(kpiElement)
' Adding Measure Elements
olapReport.CategoricalElements.Add(measureElementColumn)
' Adding Row Members
olapReport.SeriesElements.Add(dimensionElementRow)
```

## Content

### Report with member properties

```csharp
[C#]

OlapReport olapReport = new OlapReport();
olapReport.Name = "Employee Sales Report";
// Specifying the current cube name
olapReport.CurrentCubeName = "Adventure Works";

MeasureElements measureElementColumn = new MeasureElements();
// Specifying the Name for the Measure Element
measureElementColumn.Elements.Add(new MeasureElement { Name = "Sales Amount Quota" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Dimension Name
dimensionElementRow.Name = "Employee";
// Specifying the Hierarchy and level name for the Dimension Element
dimensionElementRow.AddLevel("Employees", "Employee Level 02");
dimensionElementRow.Hierarchy.LevelElements["Employee Level 02"].IncludeAvailableMembers = true;

// Adding the Member properties to the Dimension Element
dimensionElementRow.MemberProperties.Add(new MemberProperty("Title", "[Employee].[Employees].[Title]"));
dimensionElementRow.MemberProperties.Add(new MemberProperty("Phone", "[Employee].[Employees].[Phone]"));
dimensionElementRow.MemberProperties.Add(new MemberProperty("Email Address",
```

## Page-level Navigation/TOC (if applicable)

- **Report with member properties**

## Cross References

- See also: [previous section on adding column, measure, and row members]

<!-- tags: [OlapReport, DimensionElement, MeasureElements, MemberProperty, Syncfusion Winforms] keywords: [OlapReport properties, DimensionElementRow, IncludeAvailableMembers, MemberProperties, Employee Sales Report] -->
```