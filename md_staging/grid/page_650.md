```html
<!--source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_650.jpeg
document_name: grid
page_number: 650
page_id: grid#page_650
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:42Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the manipulation of records in a GridGroupingControl.
- Includes adding, updating, deleting, and modifying records.
- Handles events related to data changes and operations.

## Content

### Example Code for Record Manipulation

The following code snippet illustrates the process of adding, updating, deleting, and modifying records in a `GridGroupingControl` based on a dataset.

```vb
dr.EmployeeID = i
dr.Freight = i / 10
dr.ShipVia = 0
dr.Table.Rows.Add(dr)
GoTo Continue1
End If
End If

If northwindDataSet1.Orders.Rows.Count = 0 Then
    Me.gridGroupingControl1.Update()
    Return
End If

Dim newIndex As Integer = rnd.Next(northwindDataSet1.Orders.Rows.Count)
dr = northwindDataSet1.Orders(newIndex)

' Delete Records.
If gridGroupingControl1.TestDeleteRecords Then
    If i Mod 12 = 0 Then
        dr.Delete()
        GoTo Continue1
    End If
End If

' Change Records.
' Freight
Dim freight As Decimal = CDec(dr.Freight) + Math.Round(CDec(rnd.Next(-100, 100)) / 10000, 2)
Dim employeeID As Integer = CInt(rnd.NextDouble() * 1000)
dr.BeginEdit()

Dim oldFreight As Decimal = dr.Freight
dr.Freight = freight
dr.EmployeeID = employeeID

If gridGroupingControl1.TestChangeGroup Then
    ' Change Group Category.
    If i = 10 Then
        tb.AddChangedField(New ChangedFieldInfo(td, "ShipVia", dr.ShipVia, 0))
        dr.ShipVia = 0
    End If
End If

' Fires ListChanged event.
```

### Explanation

1. **Adding Records**:
   - Sets the `EmployeeID`, `Freight`, and `ShipVia` properties of a new row.
   - Adds the new row to the dataset's table using `dr.Table.Rows.Add(dr)`.

2. **Handling Record Updates**:
   - Updates the `GridGroupingControl` if the dataset's `Orders` table has no rows.

3. **Deleting Records**:
   - Randomly selects a record for deletion based on a condition (`i Mod 12 = 0`).
   - Deletes the selected record using `dr.Delete()`.

4. **Changing Records**:
   - Modifies the `Freight` and `EmployeeID` fields of a record.
   - Begins editing the record using `dr.BeginEdit()`.

5. **Handling Group Category Changes**:
   - If a specific condition is met (`i = 10`), changes the group category by setting `ShipVia` to `0`.

6. **Fires `ListChanged` Event**:
   - Indicates that the changes made to the record trigger the `ListChanged` event.

## API Reference

### Methods and Properties Used
- `dr.Table.Rows.Add(dr)` - Adds a new row to the dataset's table.
- `dr.Delete()` - Deletes a specific record.
- `dr.BeginEdit()` - Begins editing a record.
- `gridGroupingControl1.TestDeleteRecords` - Tests whether records can be deleted.
- `gridGroupingControl1.TestChangeGroup` - Tests whether group categories can be changed.
- `tb.AddChangedField` - Adds a changed field to the transaction buffer.

### Event Triggers
- `ListChanged` event - Indicates that the dataset has been modified.

## Code Examples

The provided code snippet demonstrates the various operations that can be performed on records within a `GridGroupingControl`, including adding, updating, deleting, and modifying records.

## Cross References

See also:
- [GridGroupingControl Documentation](https://help.syncfusion.com/windowsforms/gridgrouping)
- [Data Manipulation in Windows Forms](https://help.syncfusion.com/windowsforms/gridgrouping/data-manipulation)

<!-- tags: [GridGroupingControl, WindowsForms, DataManipulation, Syncfusion Winforms, version: 11.4.0.26] keywords: [dr.EmployeeID, dr.Freight, dr.ShipVia, GoTo Continue1, northwindDataSet1.Orders.Rows.Count, gridGroupingControl1.TestDeleteRecords, gridGroupingControl1.TestChangeGroup, ListChanged event] -->
```