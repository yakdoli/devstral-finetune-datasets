```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_974.jpeg
document_name: grid
page_number: 974
page_id: grid#page_974
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:55:57Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Using TableDescriptor.GroupedColumns property to add groups in the grid based on specified column names.
- Demonstrating grouping and sorting functionality in the grid view.
- Describing how to manage sorting by column headers and using properties for dynamic sorting.

## Content

### Grouping Columns

You can also use TableDescriptor.GroupedColumns property to add groups where you need to specify the column names based on which the table has to be grouped.

![Figure 366: Grouping Columns by adding Groups](https://.../gridGroupingControl1.png)

**Figure 366: Grouping Columns by adding Groups**

#### SortColumnDescriptor Collection Editor

The SortColumnDescriptor Collection Editor allows you to manage the sorting attributes of the columns. You can select the column you want to sort, specify the sort direction (Ascending or Descending), and fine-tune the sorting criteria.

### Sorting

Sorting can be done on the table data by simply clicking the desired column header by which the values need to be sorted. Once sorting is done, the grouping grid displays a ListSortIcon in the respective column header to indicate the Sort Direction.

You could also make use of the TableDescriptor.SortedColumns property to perform sorting on table data wherein you need to provide the column to be sorted and a sort order.

- **Sorting Logic**:
  - Click the desired column header to initiate sorting.
  - The grouping grid displays a ListSortIcon to indicate the sort direction.
  - Utilize the TableDescriptor.SortedColumns property for programmatically defining sorting order and criteria.

## API Reference

### Properties
- **TableDescriptor.GroupedColumns**
  - Purpose: Used to specify columns for grouping in the grid.
  - Behavior: Groups data based on specified column names.

- **TableDescriptor.SortedColumns**
  - Purpose: Used to specify columns for sorting.
  - Behavior: Accepts column names and sort orders to programmatically sort data.

## Code Examples

### C# Example for Sorting
```csharp
grid.Descriptor.SortedColumns.Add("ContactTitle", ListSortDirection.Descending);
```

### C# Example for Grouping
```csharp
grid.Descriptor.GroupedColumns.Add("ContactTitle");
```

## Related Concepts
- **Grid Sorting**: Learn more about different sorting options and configurations provided by the grid.
- **Grid Grouping**: Explore advanced grouping capabilities and customization options.

<!-- tags: [Syncfusion, WinForms, Grouping, Sorting, Grid, TableDescriptor, GroupedColumns, SortedColumns] keywords: [grouping, sorting, grid, TableDescriptor, GroupedColumns, SortedColumns, ListSortDirection, data sorting, custom grouping] -->
```