```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_559.jpeg
document_name: grid
page_number: 559
page_id: grid#page_559
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:24:34Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Demonstrates how to configure and style GridBoundColumns in a Windows Forms application using VB.NET.
- Configures the grid with specific data bindings and column settings.
- Includes code for customizing column headers, background colors, and font styles.

## Content

### Configuring GridBindColumns

The following code snippet shows how to configure GridBindColumns for columns in a Windows Forms GridControl.

```vb
[VB.NET]

Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Set data source and grid properties
    Me.gridDataBoundGrid1.DataSource = ReturnATable()
    Me.gridDataBoundGrid1.EnableAddNew = False
    Me.gridDataBoundGrid1.BackColor = Color.FromArgb(&HCC, &HD4, &HE6)

    ' Create a GridBoundColumn for each displayed column.
    Dim gbc As New GridBoundColumn()
    gbc.MappingName = "FirstName"

    ' Must set to column mapping name.
    gbc.HeaderText = "Name"

    ' Set some style properties.
    gbc.StyleInfo.BackColor = Color.FromArgb(&HC0, &HC9, &HDB)
    gbc.StyleInfo.TextColor = Color.Blue

    ' Add the column to the GridBoundColumns collection.
    Me.gridDataBoundGrid1.GridBoundColumns.Add(gbc)

    ' Repeat for each column.
    gbc = New GridBoundColumn()
    gbc.MappingName = "LastName"
    gbc.HeaderText = "FamilyName"
    gbc.StyleInfo.Font.Bold = True
    Me.gridDataBoundGrid1.GridBoundColumns.Add(gbc)

    gbc = New GridBoundColumn()
    gbc.MappingName = "City"
    gbc.HeaderText = "City"
    Me.gridDataBoundGrid1.GridBoundColumns.Add(gbc)

    ' Need to initialize the GridBoundColumns so their settings will replace the currently set values.
    Me.gridDataBoundGrid1.Binder.InitializeColumns()

    ' Resize the column headers.
    Me.gridDataBoundGrid1.Model.ColWidths.ResizeToFit(GridRangeInfo.Row(0), GridResizeToFitOptions.NoShrinkSize)

    ' Form1_Load
End Sub
```

## API Reference

### Methods
- `ReturnATable()`: Returns a DataTable or similar data source for grid binding.
- `DataSource`: Sets the data source for the GridControl.
- `EnableAddNew`: Enables or disables the ability to add new rows in the grid.
- `BackColor`: Sets the background color for the grid.
- `MappingName`: Specifies the column name from the data source to bind to the GridBoundColumn.
- `HeaderText`: Sets the text displayed in the column header.
- `InitializeColumns()`: Initializes the GridBoundColumns with their custom settings.
- `ResizeToFit()`: Adjusts the column width to fit the content or other specified options.

## Code Examples

The above VB.NET code demonstrates how to:
1. Set up the grid with a data source.
2. Disable the ability to add new rows.
3. Configure specific styles and font properties for each column.
4. Add multiple GridBoundColumns to the GridControl.
5. Initialize the columns to apply custom settings.
6. Resize column headers to fit the content.

## Cross References

See also:
- [GridControl Documentation](#gridcontrol-documentation)
- [Data Binding in Windows Forms](#data-binding-in-windows-forms)
- [Customizing Grid Appearance](#customizing-grid-appearance)

<!-- tags: [Syncfusion WinForms, GridControl, GridBoundColumns, VB.NET, column configuration, Windows Forms] keywords: [GridControl, GridBoundColumns, DataSource, MappingName, HeaderText, Color, Font, InitializeColumns, ResizeToFit, Windows Forms, VB.NET] -->
```