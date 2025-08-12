```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_932.jpeg
document_name: grid
page_number: 932
page_id: grid#page_932
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Multiple records can be selected at a time by adding the desired record specifications into the `SelectedRecords` collection. The following code example illustrates this process. It selects the records with indexes 2, 4, and 0 by adding them into the `SelectedRecords` collection.

## Selecting Multiple Records

### Code Examples

#### C#
```csharp
Record r1 = this.gridGroupingControl1.Table.Records[2];
Record r2 = this.gridGroupingControl1.Table.Records[4];
Record r3 = this.gridGroupingControl1.Table.Records[0];

Table t = this.gridGroupingControl1.Table;
t.SelectedRecords.Add(r1);
t.SelectedRecords.Add(r2);
t.SelectedRecords.Add(r3);
```

#### VB.NET
```vb
Dim r1 As Record = Me.gridGroupingControl1.Table.Records(2)
Dim r2 As Record = Me.gridGroupingControl1.Table.Records(4)
Dim r3 As Record = Me.gridGroupingControl1.Table.Records(0)

Dim t As Table = Me.gridGroupingControl1.Table
t.SelectedRecords.Add(r1)
t.SelectedRecords.Add(r2)
t.SelectedRecords.Add(r3)
```

### Figure 345: Selecting Multiple Records

![Figure 345: Selecting Multiple Records](#)

<!-- tags: [Syncfusion, Winforms, Essential Grid, Record Selection, API Reference, C#, VB.NET, Multiple Records, SelectedRecords] keywords: [UNCLEAR, records, selection, index, add, collection, process, specify, desired, illustration] -->
```