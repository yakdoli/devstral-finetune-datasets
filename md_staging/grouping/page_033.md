<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: grouping
page_number: 033
page_id: grouping#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:58Z
fidelity: lossless
-->

# Essential Grouping

| SortedColumns | Holds sorted properties. |
| --- | --- |

## 4.2.2 Accessing a Particular Group

Grouping is a recursive process whereby a data source may be grouped several times. This leads to the recursive situation of groups having sub-groups and so on. In recursion, there is usually some primary node or initial starting point that you use, to work with the recursive objects. In Grouping, the initial starting point is `Engine.Table.TopLevelGroup`. This is the 'primary' Group object.

The `Grouping.Group` class has two properties that are used to recursively access nested groups and the `Record` objects contained in the terminal group. The properties are:

- `Group.Groups` and `Group.Records`.

1. `Group.Groups` is a collection of `Group` objects that are contained in the parent `Group`, and `Group.Records` is a collection of `Records` that are contained in the parent `Group`.

2. At most one of these collections will actually hold objects. If the `Groups` collection is populated, this implies that the Group has sub-groups and there are no records.

3. If the `Records` collection is populated, then it implies that this Group is a terminal group with records, but there are no sub-groups.

Your first task is to add a recursive method to either display records if the Group has records, or to recursively call itself to display any records of its child groups.

1. Add the following code below the `Main` method to implement a recursive method to display records in a Group.

```csharp
private static void ShowRecordsUnderGroup(Group g)
{
    if (g.Records != null && g.Records.Count > 0)
    {
        // Displaying the data for all the records in each group.
        foreach (Record rec in g.Records)
        {
            MyObject obj = rec.GetData() as MyObject;
            if (obj != null)
        }
    }
}
```

## Cross References
- See also: `Group`, `Record`, `Engine.Table.TopLevelGroup`.

<!-- tags: [Syncfusion Winforms, grouping, recursion, GroupRecord, TerminalGroup] keywords: [Grouping, Recursive Group, Nested Groups, Display Records, Group Object, Terminal Group, Records] -->