```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_818.jpeg
document_name: grid
page_number: 818
page_id: grid#page_818
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- This page explains how to create a `ForeignKeyKeyWords` relation in the `GridGroupingControl`. It demonstrates the setup using C# and VB.NET code examples.
- The final output includes a GridView with a master-detail relationship between `Customers` and `Items`.
- The code allows for dynamic addition and editing of items within a customer's grid view.

## Content

### Configuring ForeignKeyKeyWords Relation

#### Code Examples

##### C#

```csharp
GridRelationDescriptor childRelation = new GridRelationDescriptor();
childRelation.RelationKind = RelationKind.ForeignKeyKeyWords;

// SourceListSet name for look up.
childRelation.ChildTableName = "Items";
childRelation.RelationKeys.Add("customerID", "CustomerID");
childRelation.ChildTableDescriptor.AllowEdit = true;
childRelation.ChildTableDescriptor.AllowNew = true;
this.gridGroupingControl.TableDescriptor.Relations.Add(childRelation);
```

##### VB.NET

```vb
Dim childRelation As GridRelationDescriptor = New 
GridRelationDescriptor()
childRelation.RelationKind = RelationKind.ForeignKeyKeyWords

' SourceListSet name for look up.
childRelation.ChildTableName = "Items"
childRelation.RelationKeys.Add("customerID", "CustomerID")
childRelation.ChildTableDescriptor.AllowEdit = True
childRelation.ChildTableDescriptor.AllowNew = True
Me.gridGroupingControl1.TableDescriptor.Relations.Add(childRelation)
```

### Sample Output

#### GridView with ForeignKeyKeyWords Relation

Refer to Figure 323展示了Foreign Key KeyWords关系的示例输出:

- The GridView is split into two levels: the master table for `Customers` and a detail table for `Items`.
- The detail table is nested within the master table and shows items associated with each customer via the `CustomerID` foreign key.

**Figure 323: ForeignKeyKeyWords Relation**

![](https://placehold.it/600x400)

### Explanation of Output

- The GridView displays six customers, each with associated items listed in a detailed subtable.
- The items for each customer are dynamically populated and linked via the foreign key relationship.
- Newly added items or edits to existing items are reflected in the GridView, as set by the `AllowEdit` and `AllowNew` properties.

---

<!-- tags: [grid, foreignkeykeywords, relation, gridgroupingcontrol, windowsforms, master-detail] keywords: [customers, items, foreign key, items, customerid, allowedit, allownew] -->
```