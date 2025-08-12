```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_729.jpeg
document_name: grid
page_number: 729
page_id: grid#page_729
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:35:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

This section best demonstrates how to work with the group rows and also shows how the groups are organized into a grouping grid. The Grouping Grid architecture can be viewed as a binary where the different grid elements like group rows, summary rows, filter rows, etc. form the nodes of the tree having the data records at the bottom as leaf nodes. A group can be a final node with records or it can be a node with nested groups rooting a sub tree.

This lesson will guide you the ways to access the individual groups in a collection, to retrieve all the groups, to expand/collapse groups and will discuss some of the properties and events used to process the groups.

## Expanding/Collapsing Groups

All the groups can be expanded as well as collapsed at once by calling the respective methods, Table.ExpandAllGroups and Table.CollapseAllGroups. To expand or collapse a specific group, set Group.IsExpanded property to true or false respectively. Following code example illustrates this.

### C#

```csharp
// Expands all groups.
this.gridGroupingControl1.Table.ExpandAllGroups();

// Collapse all groups.
this.gridGroupingControl1.Table.CollapseAllGroups();

// Expand the group with index 3.
this.gridGroupingControl1.Table.TopLevelGroup.Groups[3].IsExpanded = true;

// Collapse the group with index 4.
this.gridGroupingControl1.Table.TopLevelGroup.Groups[4].IsExpanded = false;
```

### VB.NET

```vbnet
' Expands all groups.
Me.gridGroupingControl1.Table.ExpandAllGroups()

' Collapse all groups.
Me.gridGroupingControl1.Table.CollapseAllGroups()

' Expand the group with index 3.
Me.gridGroupingControl1.Table.TopLevelGroup.Groups(3).IsExpanded = True
```

<!-- tags: [product, module, control, api, version?] keywords: [group rows, grouping grid, expand, collapse, Group.IsExpanded, Table.ExpandAllGroups, Table.CollapseAllGroups, tree] -->
```