```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: grid
page_number: 109
page_id: grid#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:28:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates handling virtual data in a grid control.
- Implements data source management and synchronization between grid and external data.
- Utilizes event handlers for grid cell and row operations.

## Content

### Setting Up Virtual Data in the Grid

The following code snippet shows how to prepare and manage a grid control for handling virtual data using VB.NET. It includes creating an external data source, configuring the grid for virtual mode, and hooking up necessary event handlers to manage data retrieval and saving.

```vb
[VB.NET]

Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)

    ' Create a new external data source with 100 rows and 20 columns.
    Me._extData = New ExternalData(100, 20)

    ' Prepare the grid for virtual data.
    gridControl1.ResetVolatileData()

    ' Hook up the events needed for the virtual grid.
    ' While only the QueryCellInfo is absolutely required, it would be
    ' unusual not to handle at least one of the count events.
    AddHandler gridControl1.QueryCellInfo, New _
               _GridQueryCellInfoEventHandler(AddressOf GridQueryCellInfo)
    AddHandler gridControl1.QueryRowCount, New _
               _GridRowColCountEventHandler(AddressOf GridQueryRowCount)
    AddHandler gridControl1.QueryColCount, New _
               _GridRowColCountEventHandler(AddressOf GridQueryColCount)

    ' Handle saving data back to the data source.
    AddHandler gridControl1.SaveCellInfo, New _
               _GridSaveCellInfoEventHandler(AddressOf GridSaveCellInfo)
End Sub

Private Sub GridSaveCellInfo(ByVal sender As Object, ByVal e _As
                GridSaveCellInfoEventArgs)
    Try

        ' Move the changes back to the external data object.
        If ((e.ColIndex > 0) AndAlso (e.RowIndex > 0)) Then
            Me._extData((e.RowIndex - 1), (e.ColIndex - 1)) = _
             _System.Int32.Parse(e.Style.CellValue.ToString)
        End If
    Catch ex As System.Exception
    End Try
    e.Handled = True
End Sub
```

### Explanation

- **Data Source Creation**: 
  - An `ExternalData` object is created with 100 rows and 20 columns. This represents the external data source for the grid.

- **Grid Configuration**:
  - The `ResetVolatileData` method is called on the grid control to prepare it for handling virtual data.

- **Event Handlers**:
  - **QueryCellInfo**:
    - Handles the retrieval of cell information based on the row and column indices.
  - **QueryRowCount** and **QueryColCount**:
    - Determine the number of rows and columns in the grid.
  - **SaveCellInfo**:
    - Saves changes made in the grid back to the external data source.

### Saving Changes

The `GridSaveCellInfo` method ensures that any changes made in the grid are reflected in the external data source. It includes error handling to safely parse and store cell values.

## API Reference

### Methods

- **ResetVolatileData**:
  - Resets the volatile data for the grid, preparing it for virtual mode.

- **AddHandler**:
  - Registers event handlers for grid-specific events such as `QueryCellInfo`, `QueryRowCount`, and `SaveCellInfo`.

### Parameters

- **e.RowIndex**: The row index of the cell being queried or modified.
- **e.ColIndex**: The column index of the cell being queried or modified.
- **e.Style.CellValue**: The value of the cell being modified.

## Code Examples

The provided code examples demonstrate the setup and usage of virtual data in a grid control, including data retrieval, modification, and synchronization with an external data source.

## Cross References

See also:
- Documentation on Grid Control for Windows Forms
- Handling Data Virtualization
- Event Handling in Grid Controls

<!-- tags: [grid, windows forms, virtual data, event handling, data synchronization] keywords: [form1_load, querycellinfo, queryrowcount, querycolcount, savecellinfo, externaldata, gridcontrol1] -->
```