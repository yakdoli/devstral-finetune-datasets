```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_704.jpeg
document_name: grid
page_number: 704
page_id: grid#page_704
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:13Z
fidelity: lossless
-->

## Grouping - Nested Tables and Multi-Column Grouping

### Overview
- Demonstrates the process of grouping data in tables using the `ListSortDirection` in both C# and VB.NET.
- Highlights the nested grouping functionality in tables.
- Shows how to perform multi-column grouping.

### Content

#### Nested Tables Grouping

The following sections demonstrate how to group data in a nested table using both C# and VB.NET.

##### Code Examples

[C#]
```csharp
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Title", ListSortDirection.Descending);
```

[VB.NET]
```vb
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Title", ListSortDirection.Descending)
```

The below screenshot reflects this process:

![](screenshot.png)

**Figure 278: Nested Tables Grouping**

When multiple tables are used in a nested manner, a child table can also be grouped by getting access to the `GroupedColumns` property of the desired `ChildTableDescriptor`. The code below shows this process.

##### Child Table Grouping

[C#]
```csharp
this.gridGroupingControl1.TableDescriptor.Relations[0].ChildTableDescriptor.GroupedColumns.Add("CategoryName", ListSortDirection.Descending);
```

[VB.NET]
```vb
Me.gridGroupingControl1.TableDescriptor.Relations(0).ChildTableDescriptor.GroupedColumns.Add("CategoryName", ListSortDirection.Descending)
```

#### Note

For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping\Grouping Demo
```

### Multi Column Grouping

Currently, this section is a placeholder for further details related to multi-column grouping.

## Page-Level Navigation/TOC

- Grouping
  - Nested Tables Grouping
  - Multi Column Grouping

## Cross References

See also:
- [Syncfusion Grid Grouping Documentation](https://docs.syncfusion.com/windowsforms/grid/grouping/)

<!-- tags: [syncfusion, grid, grouping, nested tables, multi-column grouping, winforms] keywords: [grid grouping, nested tables, multi-column grouping, departments, employees, synchronization, Syncfusion, C#, VB.NET] -->
```