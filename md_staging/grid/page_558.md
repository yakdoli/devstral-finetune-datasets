```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_558.jpeg
document_name: grid
page_number: 558
page_id: grid#page_558
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
[C#]

private void Form1_Load(object sender, System.EventArgs e)
{
    this.gridDataBoundGrid1.DataSource = ReturnATable();
    this.gridDataBoundGrid1.EnableAddNew = false;
    this.gridDataBoundGrid1.BackColor = Color.FromArgb(0xcc, 0xd4, 0xe6);

    // Create a GridBoundColumn for each displayed column.
    GridBoundColumn gbc = new GridBoundColumn();
    gbc.MappingName = "FirstName";

    // Must set to column mapping name.
    gbc.HeaderText = "Name";

    // Set some style properties.
    gbc.StyleInfo.BackColor = Color.FromArgb(0xC0, 0xC9, 0xdb);
    gbc.StyleInfo.TextColor = Color.Blue;

    // Add the column to the GridBoundColumns collection.
    this.gridDataBoundGrid1.GridBoundColumns.Add(gbc);

    // Repeat for each column.
    gbc = new GridBoundColumn();
    gbc.MappingName = "LastName";
    gbc.HeaderText = "FamilyName";
    gbc.StyleInfo.Font.Bold = true;
    this.gridDataBoundGrid1.GridBoundColumns.Add(gbc);

    gbc = new GridBoundColumn();
    gbc.MappingName = "City";
    gbc.HeaderText = "City";
    this.gridDataBoundGrid1.GridBoundColumns.Add(gbc);

    // Need to initialize the GridBoundColumns so that their settings
    // will replace the currently set values.
    this.gridDataBoundGrid1.Binder.InitializeColumns();

    // Resize the column headers.
    this.gridDataBoundGrid1.Model.ColWidths.ResizeToFit(GridRangeInfo.Row(0), GridResizeToFitOptions.NoShrinkSize);
}
```

## API Reference

- **Namespace:** Not explicitly mentioned in the code but typically resides in `Syncfusion.Windows.Forms`.
- **Class:** GridDataBoundGrid
- **Methods/Properties:**
  - `DataSource`: Gets or sets the data source for the grid control.
  - `EnableAddNew`: Enables or disables the ability to add new rows.
  - `BackColor`: Gets or sets the background color of the grid.
  - `GridBoundColumns`: Collection of GridBoundColumn items for mapping columns.
  - `Binder.InitializeColumns()`: Initializes the grid columns based on the settings.
  - `Model.ColWidths.ResizeToFit()`: Resizes the column widths to fit the content with the specified options.

## Code Examples

The provided code snippet demonstrates the process of configuring a `GridDataBoundGrid` control in a Windows Forms application. It includes setting the data source, disabling the ability to add new rows, customizing the background color, creating and customizing GridBoundColumns, and initializing the columns to apply the custom settings.

## Page-level Navigation/TOC

- Essential Grid for Windows Forms
  - Configuring GridDataBoundGrid
  - Customizing Column Properties
  - Initializing Grid Bound Columns
  - Resizing Columns Dynamically

## Cross References

See also:
- Documentation for `GridDataBoundGrid` in Syncfusion WinForms.
- Additional customization options for GridBoundColumn.
- More advanced scenarios involving dynamic data binding and column resizing.

<!-- tags: [Essential Grid, Windows Forms, Syncfusion, GridDataBoundGrid, GridBoundColumn, Grid Resize] keywords: [Grid, Windows Forms, Data Binding, Column Properties, Custom Styling, ResizeToFit] -->
```