```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_804.jpeg
document_name: grid
page_number: 804
page_id: grid#page_804
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:29Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Configures hierarchical relationships between tables
- Demonstrates setting up parent-child and grandchild relationships
- Explains registering DataTables with `Engine.SourceListSet`
- Describes the process of binding the hierarchical data source to a grouping grid

## Content

The following steps outline the process of configuring hierarchical data relationships and binding them to a grouping grid:

### Configuring Parent-Child Relationships

```csharp
parentToChildRelationDescriptor.ChildTableName = "MyChildTable"
parentToChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails
parentToChildRelationDescriptor.RelationKeys.Add("parentID", "ParentID")

' Add relation to Parent Table.
gridGroupingControl1.TableDescriptor.Relations.Add(parentToChildRelationDescriptor)
```

### Configuring Child-Grandchild Relationships

```csharp
Dim childToGrandChildRelationDescriptor As New GridRelationDescriptor()

' Same as SourceListSetEntry.Name for Grand Child Table.
childToGrandChildRelationDescriptor.ChildTableName = "MyGrandChildTable"
childToGrandChildRelationDescriptor.RelationKind = RelationKind.RelatedMasterDetails
childToGrandChildRelationDescriptor.RelationKeys.Add("childID", "ChildID")

' Add relation to Child Table.
parentToChildRelationDescriptor.ChildTableDescriptor.Relations.Add(childToGrandChildRelationDescriptor)
```

### Registering DataTables

To ensure the `RelationDescriptor` can resolve table names, register the DataTables with `Engine.SourceListSet`:

#### [C#]

```csharp
this.gridGroupingControl.Engine.SourceListSet.Add("MyParentTable", parentTable);
this.gridGroupingControl.Engine.SourceListSet.Add("MyChildTable", childTable);
this.gridGroupingControl.Engine.SourceListSet.Add("MyGrandChildTable", grandChildTable);
```

#### [VB.NET]

```vb
Me.gridGroupingControl.Engine.SourceListSet.Add("MyParentTable", parentTable)
Me.gridGroupingControl.Engine.SourceListSet.Add("MyChildTable", ChildTable)
Me.gridGroupingControl.Engine.SourceListSet.Add("MyGrandChildTable", grandChildTable)
```

### Binding Hierarchical Data Source

Finally, bind the hierarchical data source to the grouping grid by assigning the parent table to the `DataSource`.

---

## Cross References
- Refer to the main documentation for detailed information on the `GridRelationDescriptor` and `Engine.SourceListSet`.

<!-- tags: [product, module, control, api, version?] keywords: [Essential Grid, Windows Forms, hierarchical relationships, parent-child, grandchild, DataTable, Engine, SourceListSet, GridRelationDescriptor, hierarchy, grouping grid] -->
```