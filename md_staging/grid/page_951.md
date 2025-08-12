```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_951.jpeg
document_name: grid
page_number: 951
page_id: grid#page_951
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
    dr(3) = r.Next(994, 1006)
    dt.Rows.Add(dr)
    i += 1
    Loop
    Return dt
End Function
```

### WinForms-specific Conventions

- Using `GridGroupingControl` for setting up grouping grids.
- Adding preview rows, groups, and summary rows using descriptors.

## Content

### Setting Up a Grouping Grid

1. **Load Data from a Data Source:**
   - Retrieve parent and child data tables.
   - Example: `parentTable = GetParentTable();`
     - `childTable = GetChildTable();`

2. **Adding Summary Rows to the Parent Table:**
   - Create a `GridSummaryColumnDescriptor`.
   - Add a summary row descriptor to the table.
   - Example:
     ```vb
     gridSummaryColumnDescriptor.DisplayColumn = "GroupID"
     gridSummaryColumnDescriptor.Format = "{Count} Records."
     gridSummaryColumnDescriptor.Name = "SummaryColumn"
     gridSummaryColumnDescriptor.SummaryType = SummaryType.Count
     this.gridGroupingControl.TableDescriptor.SummaryRows.Add(new GridSummaryRowDescriptor("SummaryRow", new GridSummaryColumnDescriptor[] { gridSummaryColumnDescriptor }))
     ```

3. **Defining Parent-Child Relationships:**
   - Create a `GridRelationDescriptor` to specify the relationship.
   - Add relation keys for parent and child tables.
   - Example:
     ```vb
     parentToChildRelationDescriptor.ChildTableName = "MyChildTable"
     parentToChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails
     parentToChildRelationDescriptor.RelationKeys.Add("parentID", "ParentID")
     ```

4. **Adding Summary Rows to the Child Table:**
   - Use a similar approach as for the parent table.
   - Example:
     ```vb
     gridSummaryColumnDescriptor.DisplayColumn = "ChildGroupID"
     gridSummaryColumnDescriptor.Format = "{Count} Records."
     gridSummaryColumnDescriptor.Name = "SummaryColumn"
     gridSummaryColumnDescriptor.SummaryType = SummaryType.Count
     parentToChildRelationDescriptor.ChildTableDescriptor.SummaryRows.Add(new GridSummaryRowDescriptor("SummaryRow", new Syncfusion.Windows.Forms.Grid.Grouping.GridSummaryColumnDescriptor[] { gridSummaryColumnDescriptor }))
     ```

## Code Examples

### Example: Setup Grouping Grid with Summary Rows

```csharp
DataTable parentTable = GetParentTable();
DataTable childTable = GetChildTable();

// Add Summary row to parent table.
GridSummaryColumnDescriptor gridSummaryColumnDescriptor = new GridSummaryColumnDescriptor();
gridSummaryColumnDescriptor.DisplayColumn = "GroupID";
gridSummaryColumnDescriptor.Format = "{Count} Records.";
gridSummaryColumnDescriptor.Name = "SummaryColumn";
gridSummaryColumnDescriptor.SummaryType = SummaryType.Count;
this.gridGroupingControl.TableDescriptor.SummaryRows.Add(new GridSummaryRowDescriptor("SummaryRow", new GridSummaryColumnDescriptor[] { gridSummaryColumnDescriptor }));

// Manually specify relations in grouping engine.
GridRelationDescriptor parentToChildRelationDescriptor = new GridRelationDescriptor();
parentToChildRelationDescriptor.ChildTableName = "MyChildTable"; // same as SourceListSetEntry.Name for childTable
parentToChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails;
parentToChildRelationDescriptor.RelationKeys.Add("parentID", "ParentID");

// Add Summary Row to child table.
gridSummaryColumnDescriptor = new GridSummaryColumnDescriptor();
gridSummaryColumnDescriptor.DisplayColumn = "ChildGroupID";
gridSummaryColumnDescriptor.Format = "{Count} Records.";
gridSummaryColumnDescriptor.Name = "SummaryColumn";
gridSummaryColumnDescriptor.SummaryType = SummaryType.Count;
parentToChildRelationDescriptor.ChildTableDescriptor.SummaryRows.Add(new GridSummaryRowDescriptor("SummaryRow", new Syncfusion.Windows.Forms.Grid.Grouping.GridSummaryColumnDescriptor[] { gridSummaryColumnDescriptor }));
```

## RAG Annotations

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```