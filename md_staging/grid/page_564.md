<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_564.jpeg
document_name: grid
page_number: 564
page_id: grid#page_564
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

Essential Grid will handle this work for you and it can all be done through the designer. For the example discussed below we use code to handle most of the steps.

## Implementation

In the designer, drag two of the Grid Data Bound Grids onto a form. Use one grid to show the foreign key combobox and the other to show the raw data for the primary table. Once the grids are in place, the code, which is given below will create the tables for this sample and then the code in the Form_Load will hook up the foreign key combobox. In our sample, we have set the combobox button to display only the current row.

### Code Example

```csharp
[C#]

private void Form1_Load(object sender, System.EventArgs e)
{
    this.gridDataBoundGrid1.DataSource = PrimaryTable();
    this.gridDataBoundGrid1.EnableAddNew = false;

    // Column 2 of the grid is the foreign key combo.
    GridBoundColumn gbc = this.gridDataBoundGrid1.Binder.InternalColumns[1];
    gbc.StyleInfo.CellType = "ComboBox";
    gbc.StyleInfo.DataSource = ForeignKeyTable();
    gbc.StyleInfo.DisplayMember = "Name";
    gbc.StyleInfo.ValueMember = "CustID";
    gbc.StyleInfo.ShowButtons = GridShowButtons.ShowCurrentRow;
    gbc.StyleInfo.HorizontalAlignment = GridHorizontalAlignment.Left;

    // Display the primary table in a second grid without the foreign key column.
    this.gridDataBoundGrid2.DataSource = this.gridDataBoundGrid1.DataSource;
    this.gridDataBoundGrid2.EnableAddNew = false;
    this.gridDataBoundGrid2.Enabled = false;
}

private DataTable PrimaryTable()
{
    DataTable dt = new DataTable("PrimaryTable");
    dt.Columns.Add(new DataColumn("ID", typeof(int)));
    dt.Columns.Add(new DataColumn("CustID", typeof(int)));
    dt.Columns.Add(new DataColumn("Address"));
    dt.Columns.Add(new DataColumn("City"));
    for (int i = 0; i < 10; ++i)
    {
        DataRow dr = dt.NewRow();
        dr[0] = i;
```

## API Reference

### Namespace: `Syncfusion.Windows.Forms.Grid`

#### Methods:
- `PrimaryTable()`: Creates the primary table for the grid.
- `ForeignKeyTable()`: Creates the foreign key table for the grid.

#### Properties:
- `DataSource`: Sets the data source for the grid.
- `EnableAddNew`: Enables or disables adding new rows.
- `Enabled`: Enables or disables the grid.
- `CellType`: Sets the type of cell (e.g., ComboBox).
- `ShowButtons`: Determines the type of buttons to be displayed in the grid.
- `HorizontalAlignment`: Sets the horizontal alignment of the cell content.

## Code Examples

The provided code demonstrates:
1. Setting up two `GridDataBoundGrid` controls.
2. Configuring one grid to display a foreign key combobox.
3. Displaying the primary table in the second grid without the foreign key column.

## RAG Annotations

<!-- tags: [syncfusion, winforms, grid, data bound grid, foreign key combobox, table setup] keywords: [Essential Grid, GridDataBoundGrid, foreign key combobox, primary table, second grid, table setup] -->