<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_825.jpeg
document_name: grid
page_number: 825
page_id: grid#page_825
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
for (int i = 0; i < 25; i++)
{
    table.Rows.Add(table.NewRow());
    table.Rows[i][0] = i;
    table.Rows[i][1] = countries[i % 8];
}
```

### [VB.NET]

```vb.net
Dim table As New DataTable()
table.Columns.Add("Id", GetType(String))
table.Columns.Add("Country", GetType(Country))

' Adding Rows.
Dim i As Integer
For i = 0 To 24
    table.Rows.Add(table.NewRow())
    table.Rows(i)(0) = i
    table.Rows(i)(1) = countries((i Mod 8))
Next i
```

## 4. Establish the ForeignKeyReference relationship.

### [C#]

```csharp
GridTableDescriptor mainTd = this.gridGroupingControl1.TableDescriptor;

GridRelationDescriptor countriesRd = new GridRelationDescriptor();
countriesRd.Name = "Country";
countriesRd.MappingName = "Country";
countriesRd.RelationKind = RelationKind.ListItemReference;

// SourceListSet name for look up.
countriesRd.ChildTableName = "Countries";

// Format ChildList.
countriesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 245, 227);

// To hide the Key column.
countriesRd.ChildTableDescriptor.VisibleColumns.Add("Name");
countriesRd.ChildTableDescriptor.SortedColumns.Add("Name");
countriesRd.ChildTableDescriptor.AllowEdit = true;

// Disallow users to modify states.
```

<!-- tags: [Syncfusion, Winforms, Grid, ForeignKeyReference, Version: 11.4.0.26] keywords: [GridTableDescriptor, GridRelationDescriptor, RelationKind, ListItemReference, ChildTableName, VisibleColumns, SortedColumns, AllowEdit] -->