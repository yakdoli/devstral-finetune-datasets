```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: grid
page_number: 076
page_id: grid#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the grouping feature in Essential Grid.
- Explains how to group data by the "CompanyName" column.
- Describes the structure of grouped values, including "Caption" rows and "AddNew" rows.

## Content

### WinForms Grouping by CompanyName Column

#### Figure 42: Grouping by the CompanyName Column

![](./image.png)

**Description:**
This image illustrates the grouping functionality in the Essential Grid component. The grid displays a list of suppliers, with each supplier having a unique `SupplierID`, `CompanyName`, and `ContactName`. The grouping is achieved by dragging the "Company Name" column header, which organizes the data into groups based on the company names.

Each group has the following features:

- **Caption Row:** A row that summarizes the grouped values, providing visibility into the grouped data.
- **AddNew Row (*):** A row that allows users to add new entries within the group.
- **Expand/Collapse Control:** Each group includes a PlusMinus cell, allowing users to expand or collapse the group to view or hide the detailed entries.

Notice that each set of grouped values has its own **"Caption"** row and its own **"AddNew"** row (*). Each group has its own **PlusMinus** cell that will let you expand/collapse the group.

## API Reference

### Properties

- **CompanyName:** Represents the name of the company.
- **ContactName:** Represents the contact person associated with the company.
- **SupplierID:** Unique identifier for each supplier.

### Methods

- **GroupByColumn:** Method to group data by a specific column (e.g., "CompanyName").
- **ExpandGroup:** Expands a specific group to view all its contents.
- **CollapseGroup:** Collapses a specific group to hide its contents.

### Events

- **GroupedEventArgs:** Event fired when data is grouped.
- **ExpandedEventArgs:** Event fired when a group is expanded.
- **CollapsedEventArgs:** Event fired when a group is collapsed.

## Code Examples

### C# Example

```csharp
private void GroupByCompany()
{
    // Assuming grid is an instance of Essential Grid
    grid.GroupByColumn("CompanyName");

    // Add event handlers for Grouped, Expanded, and Collapsed events
    grid.Grouped += Grid_Grouped;
    grid.Expanded += Grid_Expanded;
    grid.Collapsed += Grid_Collapsed;
}

private void Grid_Grouped(object sender, GroupedEventArgs e)
{
    // Handle when data is grouped
    MessageBox.Show("Data grouped by " + e.GroupColumnName);
}

private void Grid_Expanded(object sender, ExpandedEventArgs e)
{
    // Handle when a group is expanded
    MessageBox.Show("Group expanded: " + e.Group.GroupName);
}

private void Grid_Collapsed(object sender, CollapsedEventArgs e)
{
    // Handle when a group is collapsed
    MessageBox.Show("Group collapsed: " + e.Group.GroupName);
}
```

## Page-level Navigation/TOC
- Figure 42: Grouping by the CompanyName Column

## Cross References
- See also: GroupingOperations, GridGrouping, GridDataSource

## RAG Annotations
<!-- tags: [grid, windows forms, grouping, company name, caption row, addnew row, expand-collapse, Syncfusion Winforms] keywords: [grouping, company name, caption row, addnew row, plus minus cell, expand, collapse, grid, windows forms, Syncfusion] -->
```