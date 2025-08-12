```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_731.jpeg
document_name: grid
page_number: 731
page_id: grid#page_731
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:36Z
fidelity: lossless
--> 

# Essential Grid for Windows Forms

```csharp
foreach (Group gr in g.Groups)
{
    IterateGroup(gr);
}
```

### [VB.NET]

```vb.net
' Call IterateThrough method for a given group.
Dim g As Group
g = Me.gridGroupingControl1.Table.TopLevelGroup.Groups("Sport")
IterateThrough(g)

' Call IterateThrough method for all the groups in a grid table.
IterateThrough(Me.gridGroupingControl1.Table.TopLevelGroup)

' IterateThrough method iterates through the records and the nested groups.
Public Sub IterateThrough(ByVal g As Group)
    System.Diagnostics.Trace.WriteLine("GroupLevel = " + g.GroupLevel.ToString())
    System.Diagnostics.Trace.WriteLine(g.Info)
    For Each r As Record In g.Records
        System.Diagnostics.Trace.WriteLine(r.Info)
    Next r
    For Each gr As Group In g.Groups
        IterateThrough(gr)
    Next gr
End Sub
```

## Accessing the group for a given record

It is the grid.Table object that provides access to the records and the grouped elements. The Table.Records collection returns a read-only collection of the data records. The following code can be used to get access to the group for a particular record. Record.ParentGroup property is used to obtain the group that a record belongs to.

### [C#]

```csharp
System.Diagnostics.Trace.WriteLine(this.gridGroupingControl1.Table.Records[3].ParentGroup.Info);
```

### [VB.NET]

```vb.net
System.Diagnostics.Trace.WriteLine(Me.gridGroupingControl1.Table.Record
```

<!-- tags: [Syncfusion Winforms, Essential Grid, Table, Records, Groups, IterateThrough, ParentGroup, Accessing Groups, Version 11.4.0.26] keywords: [grid, windows forms, iterate through, grouped elements, table, records, parent group, accessing groups for records, gridgroupingcontrol, trace] -->
```