```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_803.jpeg
document_name: grid
page_number: 803
page_id: grid#page_803
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:27Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

```csharp
dr(1) = String.Format("GrandChildName({0})", i)
dr(2) = (i Mod numberChildRows).ToString()
dt.Rows.Add(dr)
Next i

Return dt
End Function
```

### Relationship Setup Between Tables

2. Manually set up relationships between the tables and add the relation to the parent and child tables.

#### Example in C#

```csharp
GridRelationDescriptor parentToChildRelationDescriptor = new GridRelationDescriptor();

// Same as SourceListSetEntry.Name for Child Table.
parentToChildRelationDescriptor.ChildTableName = "MyChildTable";
parentToChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails;
parentToChildRelationDescriptor.RelationKeys.Add("parentID", "ParentID");

// Add relation to Parent Table.
gridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor);

GridRelationDescriptor childToGrandChildRelationDescriptor = new GridRelationDescriptor();

// Same as SourceListSetEntry.Name for Grand Child Table.
childToGrandChildRelationDescriptor.ChildTableName = "MyGrandChildTable";
childToGrandChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails;
childToGrandChildRelationDescriptor.RelationKeys.Add("childID", "ChildID");

// Add relation to Child Table.
parentToChildRelationDescriptor.ChildTableDescriptor.Relations.Add(childToGrandChildRelationDescriptor);
```

#### Example in VB.NET

```vb
Dim parentToChildRelationDescriptor As New GridRelationDescriptor()

' Same as SourceListSetEntry.Name for Child Table.
```

---

```html
<!-- tags: [Syncfusion, Winforms, Essential Grid, Grid Relation, Table Relationship] keywords: [GridRelationDescriptor, RelationKind, RelatedMasterDetails, RelationKeys, TableDescriptor, relations, child table, parent table, grandchild table] -->
```