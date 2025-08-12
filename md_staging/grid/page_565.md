<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_565.jpeg
document_name: grid
page_number: 565
page_id: grid#page_565
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates creating a grid with a foreign key column that uses a combo box for data binding.
- Shows how to configure the combo box in the grid to display values from a foreign key table while linking it to the primary table.

## Content

### Creating Primary and Foreign Key Tables

#### Primary Table Creation
```csharp
private DataTable PrimaryTable()
{
    DataTable dt = new DataTable("PrimaryTable");
    // Create columns for the primary table
    dt.Columns.Add(new DataColumn("ID", typeof(int)));
    dt.Columns.Add(new DataColumn("Address", typeof(string)));
    dt.Columns.Add(new DataColumn("City", typeof(string)));

    // Add rows with sample data
    for(int i = 0; i < 10; ++i)
    {
        DataRow dr = dt.NewRow();
        dr[0] = i;
        dr[1] = i % 4;
        dr[2] = string.Format("address{0}", i);
        dr[3] = string.Format("city{0}", i);
        dt.Rows.Add(dr);
    }
    return dt;
}
```

#### Foreign Key Table Creation
```csharp
private DataTable ForeignKeyTable()
{
    // Create a table with two columns: CustID (Value Member) and Name (Display Member).
    DataTable dt = new DataTable("ForeignKeyTable");
    dt.Columns.Add(new DataColumn("CustID", typeof(int)));
    dt.Columns.Add(new DataColumn("Name"));

    // Add sample data to the foreign key table
    for(int i = 0; i < 4; ++i)
    {
        DataRow dr = dt.NewRow();
        dr[0] = i;
        dr[1] = string.Format("Name{0}", i);
        dt.Rows.Add(dr);
    }
    return dt;
}
```

### Configuring the Grid with a Foreign Key Combo

#### VB.NET Implementation
```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.gridDataBoundGrid1.DataSource = PrimaryTable()
    Me.gridDataBoundGrid1.EnableAddNew = False

    ' Col 2 of the grid is the foreign key combo.
    Dim gbc As GridBoundColumn = Me.gridDataBoundGrid1.Binder.InternalColumns(1)
    gbc.StyleInfo.CellType = "ComboBox"
    gbc.StyleInfo.DataSource = ForeignKeyTable()
    gbc.StyleInfo.DisplayMember = "Name"
    gbc.StyleInfo.ValueMember = "CustID"
    gbc.StyleInfo.ShowButtons = GridShowButtons.ShowCurrentRow
    gbc.StyleInfo.HorizontalContentAlignment = GridHorizontalContentAlignment.Left

    ' Just display the primary table in a second grid without the foreign key column.
    Me.gridDataBoundGrid2.DataSource = Me.gridDataBoundGrid1.DataSource
    Me.gridDataBoundGrid2.EnableAddNew = False
End Sub
```

## API Reference

### Methods
- `PrimaryTable()`: Creates a primary data table with columns for ID, Address, and City.
- `ForeignKeyTable()`: Creates a foreign key data table with columns for CustID and Name.

### Properties
- `DataSource`: Binds the grid to the primary and foreign key tables.
- `EnableAddNew`: Disables the ability to add new rows manually.

### GridBoundColumn Options
- `CellType`: Sets the cell type as a combo box.
- `DataSource`: Specifies the data source for the combo box.
- `DisplayMember`: Defines the column used for displaying values.
- `ValueMember`: Defines the column used for storing actual values.
- `ShowButtons`: Configures the visibility of buttons for the combo box.
- `HorizontalContentAlignment`: Aligns the content horizontally in the grid cell.

### See also:
- [Data Binding in Essential Grid](#data-binding-in-essential-grid)
- [Using Iterative Methods for Tables](#using-iterative-methods-for-tables)

<!-- tags: [essential grid, windows forms, data binding, foreign key, combo box] keywords: [PrimaryTable, ForeignKeyTable, grid, datagrid, combo box cell type, foreign key table, display member, value member] -->