```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: Olap Common
page_number: 050
page_id: Olap Common#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:17:54Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Demonstrates creating an OLAP report with customized dimensions and measures.

## Content

### Creating an OLAP Report with Custom Dimension and Measure Elements

```csharp
[C#]

OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";
DimensionElement dimensionElementColumn = new DimensionElement();
// Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
// Specifying the Hierarchy Name
dimensionElementColumn.HierarchyName = "Customer Geography";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
// Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.HierarchyName = "Fiscal";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].Add("FY 2002");
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ShowChildMembers = true;
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].Add("H1 FY 2002");
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].ShowChildMembers = true;
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].Add("Q1 FY 2002");
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].ChildMemberElements[0].ShowChildMembers = true;
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].ChildMemberElements[0].ChildMemberElements[0].ShowChildMembers = true;
dimensionElementRow.Hierarchy.LevelElements["Fiscal Year"].MemberElements[0].ChildMemberElements[0].ChildMemberElements[0].ChildMemberElements[0].Add("July 2001");
``` 

### Sample Code Explanation
- **Creating a Report**: Initializes an `OlapReport` object, sets its name, and specifies the cube to use.
- **Customizing Dimensions**: Defines different dimensions such as "Customer" and "Date" with their respective hierarchies and levels.
- **Adding Measures**: Specifies a measure column with a single measure, "Internet Sales Amount".
- **Hierarchy and Levels**: Configures the "Date" dimension with a fiscal hierarchy, adding fiscal years, half-years, and quarters, and setting flags for showing child members.

### Custom Dimension and Measure Setup
- **DimensionElement**: Represents a dimension in the OLAP report.
- **HierarchyName**: Specifies the hierarchy name for that dimension.
- **AddLevel**: Adds levels to the hierarchy, defining the granularity of the dimension.
- **MeasureElements**: Defines columns for measures in the report.
- **ShowChildMembers**: Controls whether child members of a level are shown in the report.

## Code Examples

```csharp
[C#]
OlapReport olapReport = new OlapReport();
// Additional code as shown above...

[VB]
```

## Cross References
- Refer to the OLAP Report documentation for more details on hierarchy and level configurations.

<!-- tags: [olapreport, dimensionelement, measureelements, fiscalhierarchy, customergeography] keywords: [olap report, dimension, measure, hierarchy, level] -->
```