```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_954.jpeg
document_name: grid
page_number: 954
page_id: grid#page_954
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:35Z
fidelity: lossless
-->

## Content

### Example of SummaryRow and Grouped Grid in Windows Forms

Below is an example demonstrating how to use the `GridSummaryRowDescriptor` and `GridGroupingControl` in a Windows Forms application using the Syncfusion library. The code snippet shows how to set up a summary row, define relationships between tables, register tables, and customize the appearance of the grid.

```vb
gridSummaryColumnDescriptor.SummaryType = SummaryType.Count
parentToChildRelationDescriptor.ChildTableDescriptor.SummaryRows.Add(New Syncfusion.Windows.Forms.Grid.Grouping.GridSummaryRowDescriptor("SummaryRow", New Syncfusion.Windows.Forms.Grid.Grouping.GridSummaryColumnDescriptor(gridSummaryColumnDescriptor)))

' Add relation to parent table.
gridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor)

' Register any DataTable/IList with SourceListSet, so that RelationDescriptor can resolve the name
Me.gridGroupingControl1.Engine.SourceListSet.Add("MyParentTable", parentTable)
Me.gridGroupingControl1.Engine.SourceListSet.Add("MyChildTable", childTable)

Me.gridGroupingControl1.DataSource = parentTable
Me.gridGroupingControl1.ShowGroupDropArea = True
Me.gridGroupingControl1.AddGroupDropArea("MyChildTable")

' The TrackWidthOfParentColumn property of a column descriptor ensures that columns are aligned and synchronized.
Me.gridGroupingControl1.TableDescriptor.Columns(0).Width = 200
Me.gridGroupingControl1.TableDescriptor.Columns(1).Width = 150
Me.gridGroupingControl1.TableDescriptor.Columns(2).Width = 150

' Synchronize width of columns in child record with width of column in parent record.
For n As Integer = 0 To 2
    parentToChildRelationDescriptor.ChildTableDescriptor.Columns(n).TrackWidthOfParentColumn = _
        gridGroupingControl1.TableDescriptor.Columns(n).Name
Next n

Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("GroupID")
Me.gridGroupingControl1.TableOptions.ShowRecordPreviewRow = True
Me.gridGroupingControl1.ChildGroupOptions.ShowGroupPreview = True

Me.gridGroupingControl1.TableDescriptor.Columns("GroupID").Appearance.AnyHeaderCell.HorizontalAlignment = GridHorizontalAlignment.Right
Me.gridGroupingControl1.TableDescriptor.Columns("GroupID").Appearance.AnyHeaderCell.VerticalAlignment = GridVerticalAlignment.Bottom
Me.gridGroupingControl1.Appearance.AnySummaryCell.Interior = New BrushInfo(Color.FromArgb(255, 231, 162))
```

### Explanation of Key Features

1. **SummaryRow**: A summary row is added to the grid to display aggregated data, such as a count of records. The `SummaryType` is set to `Count` to show the number of rows.

2. **Relations Between Tables**: The `parentToChildRelationDescriptor` establishes a parent-child relationship between two tables, `MyParentTable` and `MyChildTable`.

3. **SourceListSet**: The tables are registered in the `SourceListSet` to ensure that the `RelationDescriptor` can resolve the table names.

4. **Grouped Grid**: The `GridGroupingControl` is configured to display grouped data. The `GroupedColumns` property is used to specify which column should be used for grouping.

5. **Column Width Synchronization**: The `TrackWidthOfParentColumn` property ensures that the width of columns in the child record is synchronized with the width of the corresponding column in the parent record.

6. **Appearance Customization**: The appearance of specific columns and cells is customized using the `Appearance` property. For example, the alignment and background color of the summary row are set.

## Summary

This example demonstrates how to use the Syncfusion GridGroupingControl in a Windows Forms application to create a grouped grid with a summary row. By defining relationships between tables, registering them in the `SourceListSet`, and customizing the appearance of the grid, you can create a more user-friendly and functional data display.

<!-- tags: [Syncfusion, GridGroupingControl, Windows Forms, SummaryRow, Grouped Grid, Customization, Parent-Child Relation, Appearance, C#] keywords: [summaryrow, groupedgrid, windowsforms, appearance, relations, customalignment, parentchild] -->
```