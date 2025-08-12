```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_952.jpeg
document_name: grid
page_number: 952
page_id: grid#page_952
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:34Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
// Add relation to parent table.
gridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor);

// Register any DataTable/IList with SourceListSet, so that
// RelationDescriptor can resolve the name
this.gridGroupingControl1.Engine.SourceListSet.Add("MyParentTable", parentTable);
this.gridGroupingControl1.Engine.SourceListSet.Add("MyChildTable", childTable);

this.gridGroupingControl.DataSource = parentTable;
this.gridGroupingControl.ShowGroupDropArea = true;
this.gridGroupingControl.AddGroupDropArea("MyChildTable");

// The TrackWidthOfParentColumn property of a column descriptor ensures that
// columns are aligned and synchronized.

this.gridGroupingControl.TableDescriptor.Columns[0].Width = 200;
this.gridGroupingControl.TableDescriptor.Columns[1].Width = 150;
this.gridGroupingControl.TableDescriptor.Columns[2].Width = 150;

// Synchronize width of columns in child record with width of column in
// parent record.
for (int n = 0; n < 3; n++)
    parentToChildRelationDescriptor.ChildTableDescriptor.Columns[n].TrackWidthOfParentColumn =
        gridGroupingControl1.TableDescriptor.Columns[n].Name;

this.gridGroupingControl.TableDescriptor.GroupedColumns.Add("GroupID");
this.gridGroupingControl.TableOptions.ShowRecordPreviewRow = true;
this.gridGroupingControl.ChildGroupOptions.ShowGroupPreview = true;

this.gridGroupingControl.TableDescriptor.Columns["GroupID"].Appearance.AnyHeaderCell.HorizontalAlignment = GridHorizontalAlignment.Right;
this.gridGroupingControl.TableDescriptor.Columns["GroupID"].Appearance.AnyHeaderCell.VerticalAlignment = GridVerticalAlignment.Bottom;
this.gridGroupingControl.Appearance.AnySummaryCell.Interior = new BrushInfo(Color.FromArgb(255, 231, 162));

// Hook up this event to handle preview rows.
this.gridGroupingControl.QueryCellStyleInfo += new GridTableCellStyleInfoEventHandler(gridGroupingControl1_QueryCellStyleInfo);

private Sub gridGroupingControl1_QueryCellStyleInfo(ByVal sender As
```

## API Reference

### WinForms-Events
- **gridGroupingControl1_QueryCellStyleInfo**
  - Parameters:
    - **sender**: The object that raised the event.
    - **e**: Event data containing information about the cell styles.
  - Returns: None.
  - Description: Customizes the appearance of the grid cells.

## Code Examples

### Example: Customizing Grid Appearance

```csharp
// Event handler for customizing cell styles
private void gridGroupingControl1_QueryCellStyleInfo(object sender, GridTableCellStyleInfoEventArgs e)
{
    // Custom logic to modify cell appearance as needed
    // Example: Changing background color for specific rows or cells
    // e.Style.BackColor = Color.LightYellow;
}
```

### Example: Synchronizing Column Widths

```csharp
// Synchronize column widths across parent and child tables
for (int n = 0; n < 3; n++)
{
    parentToChildRelationDescriptor.ChildTableDescriptor.Columns[n].TrackWidthOfParentColumn =
        gridGroupingControl1.TableDescriptor.Columns[n].Name;
}
```

## Cross References

- Refer to the "Table Descriptor and Relations" section for more information on managing relationships between tables.
- For further details on styling grid controls, see the "GridCellCustomization" documentation.

<!-- tags: [syncfusion, winforms, grid, tabledescriptor, relationdescriptor, querycellstyleinfo] keywords: [syncfusion, grid, table, column, alignment, styling, customevent, width, relation, previewrow, groupdroparea] -->
```