```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_935.jpeg
document_name: grid
page_number: 935
page_id: grid#page_935
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:56Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Dim rec As Record = Me.gridGroupingControl1.Table.Records(2)

' Search for the record 'rec'.
Dim index As Integer =
Me.gridGroupingControl1.Table.SelectedRecords.FindRecord(rec)

' Search for the record with index 2.
Dim index2 As Integer =
Me.gridGroupingControl1.Table.SelectedRecords.FindRecord(2)
```

## Removing a RecordSelection

A record can be removed from the `SelectedRecords` collection by using the methods `Remove()` and `RemoveAt()`. A call to `Remove()` requires you to specify the whole record itself as a parameter. In case if you know only the record index, you could then make use of `RemoveAt()`. Both the methods remove the specified record from the collection and mark it as deselected.

### [C#]

```csharp
Record rec = this.gridGroupingControl1.Table.Records[2];

// Remove the record 'rec'.
this.gridGroupingControl1.Table.SelectedRecords.Remove(rec);

// Remove the record at the index 2.
this.gridGroupingControl1.Table.SelectedRecords.RemoveAt(2);
```

### [VB.NET]

```vb
Dim rec As Record = Me.gridGroupingControl1.Table.Records(2)

' Remove the record 'rec'.
Me.gridGroupingControl1.Table.SelectedRecords.Remove(rec)

' Remove the record at the index 2.
Me.gridGroupingControl1.Table.SelectedRecords.RemoveAt(2)
```

## Clear Selection

To remove all the selections from the grid, you can call `SelectedRecords.Clear()` method that removes all the elements from the collection and mark them as deselected.

### [C#]

```csharp
this.gridGroupingControl1.Table.SelectedRecords.Clear();
```

<!-- tags: [grid, windows forms, essential grid, selected records, deselection, version 11.4.0.26] keywords: [records, collection, deselect, remove, clear, gridGroupingControl, findRecord, removeAt] -->
```