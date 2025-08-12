```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_836.jpeg
document_name: grid
page_number: 836
page_id: grid#page_836
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:36Z
fidelity: lossless
-->

# **Essential Grid for Windows Forms**

## Overview
- Demonstrates how to assign a collection to the data source of a grouping grid and establish a UniformChildList relation kind.
- Explains the process of configuring the GridGroupingControl to utilize grouping drop areas and manipulate grouped columns.

## Content

### Setting upDataSource for Grouping Grid
1. Define a collection (`childList`) to serve as the child data for the GridGroupingControl.
2. Populate this collection with appropriate data.

3. Iterate over the collection to establish the child relationships for the grouping grid.

```csharp
Do While j < (i * 5) + 5
    topList(i).Child.Add(childList(j))
    j += 1
Loop
Next i
```

4. Assign the above collection to the data source of the grouping grid.

#### Code Examples

##### C#
```csharp
gridGroupingControl1.DataSource = topList;
```

##### VB.NET
```vb
GridGroupingControl1.DataSource = topList
```

### Establishing UniformChildList Relation Kind
5. Establish the UniformChildList relation kind.

#### Code Examples

##### C#
```csharp
GridRelationDescriptor relation = new GridRelationDescriptor();
relation.RelationKind = RelationKind.UniformChildList;
relation.MappingName = "Child";
relation.Name = "Child";
relation.ChildTableName = "ChildTable";
gridGroupingControl1.TableDescriptor.Relations.Add(relation);

this.gridGroupingControl.ShowGroupDropArea = true;
GridTable chiltTable = gridGroupingControl1.GetTable("ChildTable");
this.gridGroupingControl.AddGroupDropArea(chiltTable);
chiltTable.TableDescriptor.GroupedColumns.Add("Field1");
```

##### VB.NET
```vb
Dim relation As GridRelationDescriptor = New GridRelationDescriptor()
relation.RelationKind = RelationKind.UniformChildList
relation.MappingName = "Child"
relation.Name = "Child"
relation.ChildTableName = "ChildTable"
gridGroupingControl1.TableDescriptor.Relations.Add(relation)

Me.gridGroupingControl1.ShowGroupDropArea = True
Dim chiltTable As GridTable = gridGroupingControl1.GetTable("ChildTable")
Me.gridGroupingControl1.AddGroupDropArea(chiltTable)
```

## API Reference
### GridRelationDescriptor
- **RelationKind**: Specifies the kind of relation. In this case, it is set to `RelationKind.UniformChildList`.
- **MappingName**: The name used for mapping the relation, here set to `"Child"`.
- **Name**: The relation's name, also set to `"Child"`.
- **ChildTableName**: The name of the table that acts as the child in the relation, defined as `"ChildTable"`.

### GridGroupingControl
- **TableDescriptor**: Contains properties and methods related to the table being displayed in the GridGroupingControl.
- **Relations**: A collection of relations defined for the table.
- **ShowGroupDropArea**: Property to enable or disable the display of the group drop area.
- **GetTable**: Method to retrieve the table descriptor corresponding to a specific table name.
- **GroupedColumns**: Collection to define the columns that are grouped in the grid.

## Code Examples
### Complete Example in C#
```csharp
using System;
using Syncfusion.Windows.Forms.Grid.Grouping;

class GridExample {
    public void SetupGroupingGrid() {
        // Assuming topList and childList are populated collections
        int j = 0;
        for (int i = 0; i < topList.Count; i++) {
            Do {
                topList[i].Child.Add(childList[j]);
                j++;
            } While (j < (i * 5) + 5);
        }

        gridGroupingControl1.DataSource = topList;

        GridRelationDescriptor relation = new GridRelationDescriptor();
        relation.RelationKind = RelationKind.UniformChildList;
        relation.MappingName = "Child";
        relation.Name = "Child";
        relation.ChildTableName = "ChildTable";
        gridGroupingControl1.TableDescriptor.Relations.Add(relation);

        this.gridGroupingControl.ShowGroupDropArea = true;
        GridTable chiltTable = gridGroupingControl1.GetTable("ChildTable");
        this.gridGroupingControl.AddGroupDropArea(chiltTable);
        chiltTable.TableDescriptor.GroupedColumns.Add("Field1");
    }
}
```

### Complete Example in VB.NET
```vb
Imports System
Imports Syncfusion.Windows.Forms.Grid.Grouping

Class GridExample
    Public Sub SetupGroupingGrid()
        ' Assuming topList and childList are populated collections
        Dim j As Integer = 0
        For i As Integer = 0 To topList.Count - 1
            Do
                topList(i).Child.Add(childList(j))
                j += 1
            Loop While j < (i * 5) + 5
        Next

        GridGroupingControl1.DataSource = topList

        Dim relation As GridRelationDescriptor = New GridRelationDescriptor()
        relation.RelationKind = RelationKind.UniformChildList
        relation.MappingName = "Child"
        relation.Name = "Child"
        relation.ChildTableName = "ChildTable"
        gridGroupingControl1.TableDescriptor.Relations.Add(relation)

        Me.gridGroupingControl1.ShowGroupDropArea = True
        Dim chiltTable As GridTable = gridGroupingControl1.GetTable("ChildTable")
        Me.gridGroupingControl1.AddGroupDropArea(chiltTable)
        chiltTable.TableDescriptor.GroupedColumns.Add("Field1")
    End Sub
End Class
```

## Cross References
See also:
- Documentation on GridGroupingControl properties and methods.
- Examples of using grouping and relation descriptors in the GridGroupingControl.

<!-- tags: [grid, grouping grid, relation descriptor, uniform child list, data source] keywords: [GridGroupingControl, GridRelationDescriptor, RelationKind, UniformChildList, DataSource, GroupDropArea, GroupedColumns] -->
```
