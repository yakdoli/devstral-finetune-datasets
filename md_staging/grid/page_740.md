```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_740.jpeg
document_name: grid
page_number: 740
page_id: grid#page_740
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:23Z
fidelity: lossless
-->

## Content

### Description
This section explains how to configure a foreign key reference relationship in a `GridGroupingControl` using both C# and VB.NET. It involves several steps to properly set up and manage the relations between tables.

#### Steps to Configure Foreign Key Reference

**1. Get the visible column's index:**

```csharp
// C#
int lookUpIndex = td.VisibleColumns.IndexOf("Customer");
```
```vbnet
' VB.NET
Dim td As GridTableDescriptor = Me.gridGroupingControl1.TableDescriptor
td.VisibleColumns.LoadDefault()
Dim lookUpIndex As Integer = td.VisibleColumns.IndexOf("Customer")
```

**2. Add the foreign table to the Engine's source list:**

```csharp
// C#
this.gridGroupingControl1.Engine.SourceListSet.Add(ForeignTableName,
ForeignTable.DefaultView);
```
```vbnet
' VB.NET
Me.gridGroupingControl1.Engine.SourceListSet.Add(ForeignTableName,
ForeignTable.DefaultView)
```

**3. Create and setup a RelationKind.ForeignKeyReference relation:**

```csharp
// C#
GridRelationDescriptor rd = new GridRelationDescriptor();
rd.Name = "CustomerColDisplay";
rd.RelationKind = RelationKind.ForeignKeyReference;
rd.ChildTableName = ForeignTableName;
```
```vbnet
' VB.NET
Dim rd As GridRelationDescriptor = New GridRelationDescriptor()
rd.Name = "CustomerColDisplay"
rd.RelationKind = RelationKind.ForeignKeyReference
rd.ChildTableName = ForeignTableName
```

**4. Set any optional properties on the relation:**

```csharp
// C#
// Display column.
rd.ChildTableDescriptor.VisibleColumns.Add("CustomerName");
// Sort it for dropdown display.
```

## API Reference

### Methods and Properties
- **GridRelationDescriptor**
  - **Name**: string - The name of the relation.
  - **RelationKind**: RelationKind - Specifies the kind of relation (e.g., ForeignKeyReference).
  - **ChildTableName**: string - The name of the child table.
- **GridTableDescriptor**
  - **VisibleColumns**: Collection - Handles visible columns.
  - **LoadDefault()**: Loads the default settings for visible columns.

## Code Examples

### Complete Example in C#
```csharp
GridRelationDescriptor rd = new GridRelationDescriptor();
rd.Name = "CustomerColDisplay";
rd.RelationKind = RelationKind.ForeignKeyReference;
rd.ChildTableName = "Customers";

GridTableDescriptor td = this.gridGroupingControl1.TableDescriptor;
td.VisibleColumns.LoadDefault();
int lookUpIndex = td.VisibleColumns.IndexOf("Customer");
this.gridGroupingControl1.Engine.SourceListSet.Add("Customers",
ForeignTable.DefaultView);

// Optional properties
rd.ChildTableDescriptor.VisibleColumns.Add("CustomerName");
```

### Complete Example in VB.NET
```vbnet
Dim rd As GridRelationDescriptor = New GridRelationDescriptor()
rd.Name = "CustomerColDisplay"
rd.RelationKind = RelationKind.ForeignKeyReference
rd.ChildTableName = "Customers"

Dim td As GridTableDescriptor = Me.gridGroupingControl1.TableDescriptor
td.VisibleColumns.LoadDefault()
Dim lookUpIndex As Integer = td.VisibleColumns.IndexOf("Customer")
Me.gridGroupingControl1.Engine.SourceListSet.Add("Customers",
ForeignTable.DefaultView)

' Optional properties
rd.ChildTableDescriptor.VisibleColumns.Add("CustomerName")
```

## See also
- [GridGroupingControl Documentation](https://help.syncfusion.com/windowsforms/datagrid)
- RelationKind Enumeration
- GridRelationDescriptor Class
- GridTableDescriptor Class

<!-- tags: [Syncfusion, WinForms, GridGroupingControl, foreign key reference, RelationKind] keywords: [GridGroupingControl, foreign table, relationKind, GridRelationDescriptor, GridTableDescriptor, visible columns, dropdown display, Windows Forms] -->
```
