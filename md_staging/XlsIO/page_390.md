```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_390.jpeg
document_name: XlsIO
page_number: 390
page_id: XlsIO#page_390
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:37Z
fidelity: lossless
-->

# XlsIO

## Overview
- Demonstrates how to use the `IsSummaryRowBelow` and `IsSummaryColumnRight` properties in XlsIO for summary settings.
- Explains features to check the existence and level of groups using properties like `IsGroupedByColumn`, `IsGroupedByRow`, `RowGroupLevel`, and `ColumnGroupLevel`.
- Describes the Expand/Collapse functionality for groups in XlsIO.

## Content

### Summary Settings in XlsIO
In XlsIO, the summary settings can be adjusted using the `IsSummaryRowBelow` and `IsSummaryColumnRight` properties of the `IPageSetup` class. These settings allow customization of where summaries appear in the worksheet.

#### Disabled State of Summary Settings
The following screenshot shows the disabled state of summary settings.

![Figure 140: Summary Settings Disabled](https://i.imgur.com/GenericScreenshot.png)
*Figure 140: Summary Settings Disabled*

### Group Existence and Level Checking
XlsIO provides options to check the existence of a group and the level at which it exists. This can be done through the `IsGroupedByColumn/IsGroupedByRow` and `RowGroupLevel/ColumnGroupLevel` properties of `IRange`.

### Expand/Collapse Groups
Essential XlsIO supports Expand and Collapse features for existing groups. The Expand feature includes overloads that allow expanding the entire parent, including child groups. The Expand and Collapse features are available for both Column and Row groups.

#### Code Examples: Expanding and Collapsing Groups

[C#]
```csharp
// Expand group with flag set to expand parent.
worksheet.Range["A1:A19"].ExpandGroup(ExcelGroupBy.ByRows, ExpandCollapseFlags.ExpandParent);

// Collapse group.
worksheet.Range["A61:A114"].CollapseGroup(ExcelGroupBy.ByRows);
```

## API Reference

### Properties
- **IsSummaryRowBelow**: Specifies whether the summary row is placed below the data.
- **IsSummaryColumnRight**: Specifies whether the summary column is placed to the right of the data.
- **IsGroupedByColumn**: Indicates if the range is grouped by columns.
- **IsGroupedByRow**: Indicates if the range is grouped by rows.
- **RowGroupLevel**: Specifies the group level for rows.
- **ColumnGroupLevel**: Specifies the group level for columns.

### Methods
- **ExpandGroup**: Expands the specified group.
- **CollapseGroup**: Collapses the specified group.

## Code Examples

### C#
```csharp
// Example: Expanding a group with parent expansion.
worksheet.Range["A1:A19"].ExpandGroup(ExcelGroupBy.ByRows, ExpandCollapseFlags.ExpandParent);
```

### VB.NET
```vbnet
' Example: Collapsing a group.
worksheet.Range("A61:A114").CollapseGroup(ExcelGroupBy.ByRows)
```

## Cross References
- Refer to the documentation on Grouping Data for more details on group settings and properties.
- See also: Row and Column Grouping in Excel.

<!-- tags: [XlsIO, Grouping, Summary Settings, Expand/Collapse, WinForms, C#, VB.NET] keywords: [IsSummaryRowBelow, IsSummaryColumnRight, IPageSetup, IsGroupedByColumn, IsGroupedByRow, RowGroupLevel, ColumnGroupLevel, ExpandFlags, CollapseGroup] -->
```