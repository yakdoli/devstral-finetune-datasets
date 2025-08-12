```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_933.jpeg
document_name: grid
page_number: 933
page_id: grid#page_933
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section demonstrates how to implement multi-record selection mechanisms in nested tables using the Syncfusion Grid.Grouping.Windows component.

## Content

### RecordSelection with NestedTables

When nested tables are used, you can extend the record selection mechanisms to each of the child table by accessing the SelectedRecords collection of the desired child table.

#### Example in C#

```csharp
// For Parent Table.
Record r1 = this.gridGroupingControl1.Table.Records[1];
Record r2 = this.gridGroupingControl1.Table.Records[2];

Table t = this.gridGroupingControl1.Table;
t.SelectedRecords.Add(r1);
t.SelectedRecords.Add(r2);
t.SelectedRecords.Add(r3);

// For Child Table.
Record cr1 = this.gridGroupingControl1.GetTable("Orders").Records[7];
Record cr2 = this.gridGroupingControl1.GetTable("Orders").Records[12];

this.gridGroupingControl1.GetTable("Orders").SelectedRecords.Add(cr1);
this.gridGroupingControl1.GetTable("Orders").SelectedRecords.Add(cr2);
```

#### Example in VB.NET

```vb.net
' For Parent Table.
Dim r1 As Record = Me.gridGroupingControl1.Table.Records(1)
Dim r2 As Record = Me.gridGroupingControl1.Table.Records(2)

Dim t As Table = Me.gridGroupingControl1.Table
t.SelectedRecords.Add(r1)
t.SelectedRecords.Add(r2)
t.SelectedRecords.Add(r3)

' For Child Table.
Dim cr1 As Record = 
Me.gridGroupingControl1.GetTable("Orders").Records(7)
Dim cr2 As Record = 
Me.gridGroupingControl1.GetTable("Orders").Records(12)
```

### Note: For more details, refer the following browser sample:
- `<Install Location>\Syncfusion\EssentialStudio[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Selection\Multi Record Selection Demo`

## API Reference

### Methods
- **GetTable(string tableName)**: Retrieves a table by its name.
- **SelectedRecords.Add(Record record)**: Adds a record to the selected records collection.

### Properties
- **Records**: Represents the collection of records in a table.

## Code Examples

The above examples demonstrate how to select records from both parent and child tables in a nested tabular structure.

### Cross References
- See also: [Multi Record Selection Demo](<Install Location>\Syncfusion\EssentialStudio[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Selection\Multi Record Selection Demo)

<!-- tags: [Syncfusion, Grid, NestedTables, RecordSelection, WinForms] keywords: [multi-record selection, nested tables, parent table, child table, SelectedRecords, GetTable, Records, C#, VB.NET] -->
```