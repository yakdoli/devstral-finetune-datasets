```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_648.jpeg
document_name: grid
page_number: 648
page_id: grid#page_648
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
dr.Table.Rows.Add(dr);
continue;
}
}
if (northwindDataSet1.Orders.Rows.Count == 0)
{
    this.gridGroupingControl1.Update();
    return;
}
int newIndex = rnd.Next(northwindDataSet1.Orders.Rows.Count);
dr = northwindDataSet1.Orders[newIndex];

// Delete Records.
if (gridGroupingControl1.TestDeleteRecords)
{
    if (i % 12 == 0)
    {
        dr.Delete();
        continue;
    }
}

// Change Records.
// Freight
decimal freight = (decimal)dr.Freight +
    Math.Round((decimal)rnd.Next(-100, 100) / 10000, 2);
int employeeID = (int)(rnd.NextDouble() * 1000);
dr.BeginEdit();
decimal oldFreight = dr.Freight;
dr.Freight = freight;
dr.EmployeeID = employeeID;
if (gridGroupingControl1.TestChangeGroup)
{
    // Change Group Category.
    if (i == 10)
    {
        tb.AddChangedField(new ChangedFieldInfo(td, "ShipVia",
            dr.ShipVia, 0));
        dr.ShipVia = 0;
    }
}
// Fires ListChanged event.
dr.EndEdit();
}
// Optionally manually flush changes.
if (this.gridGroupingControl1.UpdateDisplayFrequency == 0)
this.gridGroupingControl1.Update();
```

## API Reference (if applicable)

This section is related to the use of the `Syncfusion GridGroupingControl` in Windows Forms applications. The following elements are highlighted:

- **gridGroupingControl1**: The Syncfusion `GridGroupingControl` instance used for displaying and manipulating data.

- **northwindDataSet1**: The data source for the `GridGroupingControl`.

- **rd** (Random Object): Used for generating random values for modifications to the dataset.

- **dr (DataRow)**: Represents a row in the `northwindDataSet1`.

- **freight (decimal)**: Variable used to adjust shipping costs.

- **employeeID (int)**: Variable used to adjust employee ID values.

- **oldFreight (decimal)**: Tracks the original freight value for reference.

- **ShipVia (int)**: Used to change the shipping method category.

## Code Examples

The provided code includes methods for modifying data within a `GridGroupingControl`:

- **Adding Rows**: Uses `dr.Table.Rows.Add(dr)` to add a new row.

- **Deleting Rows**: Uses `dr.Delete()` to remove a randomly selected row.

- **Modifying Rows**: Updates the `Freight` and `EmployeeID` fields with random values.

- **Changing Group Categories**: Modifies the `ShipVia` field to change group categories conditionally.

- **Manual Update**: Calls `this.gridGroupingControl1.Update()` to manually refresh the grid display.

## RAG Annotations

<!-- tags: [Syncfusion, Windows Forms, GridGroupingControl, Data Manipulation, CRUD Operations] keywords: [gridgroupingcontrol1, northwinddataset1, dr, freight, employeeID, shipvia, testdeleterecords, testchangegroup, updatdisplayfrequency, addchangedfield] -->
```