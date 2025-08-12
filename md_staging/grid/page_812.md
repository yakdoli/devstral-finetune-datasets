```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_812.jpeg
document_name: grid
page_number: 812
page_id: grid#page_812
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

### Code Examples

```csharp
usStatesRd.RelationKind = RelationKind.ForeignKeyReference;

// SourceListSet name for look up.
usStatesRd.ChildTableName = "USStates";
usStatesRd.RelationKeys.Add("State", "Key");

// Format ChildList.
usStatesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 245, 227);

// To hide the Key column.
usStatesRd.ChildTableDescriptor.VisibleColumns.Add("Name");
usStatesRd.ChildTableDescriptor.SortedColumns.Add("Name");
usStatesRd.ChildTableDescriptor.AllowEdit = false;

// Disallow users to modify states.
usStatesRd.ChildTableDescriptor.AllowNew = false;

mainTd.Relations.Add(usStatesRd);

// Assign data source.
this.gridGroupingControl1.DataSource = table;
mainTd.Name = "ForeignKeyReference";
```

```vb
[VB.NET]

Dim mainTd As GridTableDescriptor = 
Me.gridGroupingControl1.TableDescriptor

Dim usStatesRd As New GridRelationDescriptor()
usStatesRd.Name = "State"
usStatesRd.RelationKind = RelationKind.ForeignKeyReference

' SourceListSet name for look up.
usStatesRd.ChildTableName = "USStates"
usStatesRd.RelationKeys.Add("State", "Key")

' Format ChildList.
usStatesRd.ChildTableDescriptor.Appearance.AlternateRecordFieldCell.BackColor = Color.FromArgb(255, 245, 227)

' To hide the Key Column.
usStatesRd.ChildTableDescriptor.VisibleColumns.Add("Name")
usStatesRd.ChildTableDescriptor.SortedColumns.Add("Name")
usStatesRd.ChildTableDescriptor.AllowEdit = False
```

## Page-level Navigation/TOC (if applicable)
- None

## Cross References
- None

### RAG Annotations
- <!-- tags: [Essential Grid, Windows Forms, RelationKind, GridRelationDescriptor, GridTableDescriptor, GridView, ForeignKeyReference, SourceListSet, ChildTableName, RelationKeys, VisibleColumns, SortedColumns, AllowEdit, AllowNew, VB.NET, C#] keywords: [RelationKind, GridRelationDescriptor, GridTableDescriptor, GridView, ChildTableName, RelationKeys, VisibleColumns, SortedColumns, AllowEdit, AllowNew, allowedit, alllownew, ChildTableDescriptor, USStates, State, Key, AlternateRecordFieldCell, BackColor] -->
```