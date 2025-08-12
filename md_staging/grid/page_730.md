<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_730.jpeg
document_name: grid
page_number: 730
page_id: grid#page_730
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
' Collapse the group with index 4.
Me.gridGroupingControl1.Table.TopLevelGroup.Groups(4).IsExpanded = False
```

## Accessing a Given Group

The `Table.TopLevelGroup.Groups` collection maintains the details of the individual groups in this collection, which can be used to retrieve the details of any group.

Below code lets you access the details of a group with the category `Sport`. It also defines a method named `IterateGroup` that is used to iterate through the records and also the nested groups in a given group. It provides you with the group details such as the level of the group, number of items in that group, its category, and so on.

## Accessing all the groups

`Table.TopLevelGroup` is the main topmost group in a grouping grid. It forms the root node of the group hierarchy where its categorized records and the nested groups form the child nodes. To access all the groups, you can make use of the same `IterateThrough` method by passing the `TopLevelGroup` as the method parameter. Then this method will loop through the categorized records and nested groups of the top-level group and will print the details of all the groups.

```csharp
// Call IterateThrough method for a given group.
Group g = this.gridGroupingControl1.Table.TopLevelGroup.Groups["Sport"];
IterateGroup(g);

// Call IterateThrough method for all the groups in a grid table.
IterateGroup(this.gridGroupingControl1.Table.TopLevelGroup);

// IterateThrough method iterates through the records and the nested groups.
public void IterateThrough(Group g)
{
    System.Diagnostics.Trace.WriteLine("GroupLevel = "+g.GroupLevel);
    System.Diagnostics.Trace.WriteLine(g.Info);
    foreach (Record r in g.Records)
    {
        System.Diagnostics.Trace.WriteLine(r.Info);
    }
}
```

---

<!-- tags: [Essential Grid, Windows Forms, Grouping, Table, TopLevelGroup, Grid Group, Records] keywords: [group, category, iteration, nested groups, records, top-level group, iterate, records] -->