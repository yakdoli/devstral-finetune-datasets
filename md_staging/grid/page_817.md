```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_817.jpeg
document_name: grid
page_number: 817
page_id: grid#page_817
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
dt.Columns.Add(New DataColumn("ItemName"))
dt.Columns.Add(New DataColumn("CustomerID"))
dt.Columns.Add(New DataColumn("Price"))
Dim rand As Random = New Random()
Dim i As Integer = 0
Do While i < numberChildRows
    Dim dr As DataRow = dt.NewRow()
    dr(0) = i.ToString()
    dr(1) = String.Format("ItemName{0}", i)
    dr(2) = (i Mod numberParentRows).ToString()
    dr(3) = rand.Next(500).ToString()
    dt.Rows.Add(dr)
    i += 1
Loop
Return dt
End Function
```

## 2. Register the child table (Items) into the SourceListSet of the grouping engine.

### [C#]

```csharp
DataTable parentTable = GetParentTable();
DataTable childTable = GetChildTable();

this.gridGroupingControl.Engine.SourceListSet.Add("Items", childTable);
```

### [VB.NET]

```vb
Dim parentTable As DataTable = GetParentTable()
Dim childTable As DataTable = GetChildTable()

Me.gridGroupingControl.Engine.SourceListSet.Add("Items", childTable)
```

## 3. Assign the datasource to the grid.

### [C#]

```csharp
this.gridGroupingControl.DataSource = parentTable;
```

### [VB.NET]

```vb
Me.gridGroupingControl.DataSource = parentTable
```

## 4. Establish ForeignKeyKeywords relationship between the tables.

<!-- tags: [grid, syncfusion winforms, essential grid, source list set, foreign key, data source, control table] keywords: [child table, parent table, items, grouping engine, datasource, foreign key relationship, vb.net, c#] -->
```