```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: Olap Common
page_number: 052
page_id: Olap Common#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:18:04Z
fidelity: lossless
-->

# Essential OlapCommon

```csharp
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").Add("FY 2002")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ShowChildMembers = True
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).Add("H1 FY 2002")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).ShowChildMembers = True
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).Add("Q1 FY 2002")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).ChildMemberElements(0).ShowChildMembers = True
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).ChildMemberElements(0).ChildMemberElements(0).Add("July 2001")
dimensionElementRow.Hierarchy.LevelElements("Fiscal Year").MemberElements(0).ChildMemberElements(0).ChildMemberElements(0).ChildMemberElements(0).ShowChildMembers = True
```

## 4.3.11.1.8 Report with Top count Filter

### [C#]

```csharp
OlapReport olapReport = new OlapReport();
olapReport.Name = "Customer Report";
olapReport.CurrentCubeName = "Adventure Works";

DimensionElement dimensionElementColumn = new DimensionElement();
//Specifying the Name for the Dimension Element
dimensionElementColumn.Name = "Customer";
dimensionElementColumn.AddLevel("Customer Geography", "Country");

//Creating Measure Element
MeasureElements measureElementColumn = new MeasureElements();
measureElementColumn.Elements.Add(new MeasureElement { Name = "Internet Sales Amount" });

DimensionElement dimensionElementRow = new DimensionElement();
//Specifying the Dimension Name
dimensionElementRow.Name = "Date";
dimensionElementRow.AddLevel("Fiscal", "Fiscal Year");
```

<!-- tags: [Syncfusion Winforms, Olap Common, Report Filter] keywords: [OlapReport, DimensionElement, MeasureElements, Customer, Date, Fiscal Year, Internet Sales Amount] -->
```