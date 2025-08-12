```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_549.jpeg
document_name: grid
page_number: 549
page_id: grid#page_549
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:13Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the process of binding a `GridDataBoundGrid` to a `DataTable` in Windows Forms.
- Covers dynamically creating a `DataTable` and binding it to the grid.

## Content

### 4.2.2.2 Binding to a DataTable

Binding to a `DataTable` is a very simple and straightforward process. After defining a `DataTable`, you must set the `GridDataBoundGrid.DataSource` property to the table. Then you can easily use the Data Tab of your toolbox in Visual Studio to generate Data Tables. Here we will add a simple `People` table using the code to illustrate how you can dynamically create a `DataTable`.

Creating a `DataTable` from code is a two-step process. You must first add `DataColumn` objects to the `DataTable.Columns` collection and then you must add `DataRow` objects to the `DataTable.Rows` collection. Given below is the code that does this. The code will assume that you have dropped a `Grid Data Bound Grid` onto the form.

```csharp
[C#]

private void Form1_Load(object sender, System.EventArgs e)
{
    this.gridDataBoundGrid1.DataSource = ReturnATable();
}

private DataTable ReturnATable()
{
    DataTable table = new DataTable("People");

    // Add two columns.
    table.Columns.Add(new DataColumn("FirstName"));
    table.Columns.Add(new DataColumn("LastName"));

    // Add some rows.
    DataRow dr = table.NewRow();
    dr["FirstName"] = "John";
    dr["LastName"] = "Smith";
    table.Rows.Add(dr);

    dr = table.NewRow();
    dr["FirstName"] = "Mary";
    dr["LastName"] = "Tucker";
    table.Rows.Add(dr);

    dr = table.NewRow();
    dr["FirstName"] = "Sue";
    dr["LastName"] = "Gaskins";
    table.Rows.Add(dr);

    dr = table.NewRow();
    dr["FirstName"] = "John";
}
```

## API Reference (if applicable)

- **Class**: `DataTable`
- **Methods**:
  - `Add` (for columns)
  - `NewRow` (for rows)
  - `Rows.Add` (for adding rows to the `DataTable`)
- **Properties**:
  - `Columns`
  - `Rows`

## Code Examples (if applicable)

The provided code demonstrates the creation of a `DataTable` and its binding to a `GridDataBoundGrid`.

<!-- tags: [grid, datagrid, datatable, binding, windows forms, csharp] 
keywords: [GridDataBoundGrid, DataTable, DataColumn, DataRow, DataSource, People, Form1_Load, ReturnATable] -->
```