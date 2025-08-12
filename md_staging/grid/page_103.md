```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_103.jpeg
document_name: grid
page_number: 103
page_id: grid#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:24:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
' Add an external data member.
Private _extData As ExternalData
```

## Initialization and Event Handling

3. Then, in your `Form1_Load` handler, add the following code to initialize the external data source and hook up the Grid control events, so that the grid can use the external data source to get the data which is in demand. The events of interest are `GridControl.QueryRowCount`, `GridControl.QueryColCount`, and `GridControl.QueryCellInfo`. The call to `ResetVolatileData` tells the grid that it needs to reset properties like the `RowCount` and `ColCount` the next time they are needed. This will allow the event handlers to set these values.

### C#

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    // Create a new external data source with 100 rows and 20 columns.
    this._extData = new ExternalData(100, 20);

    // Prepare the grid for virtual data.
    gridControl.ResetVolatileData();

    // Hook up the events needed for the virtual grid.
    gridControl.QueryCellInfo += new GridQueryCellInfoEventHandler(GridQueryCellInfo);
    gridControl.QueryRowCount += new GridRowColCountEventHandler(GridQueryRowCount);
    gridControl.QueryColCount += new GridRowColCountEventHandler(GridQueryColCount);
}
```

### VB.NET

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    ' Create a new external data source with 100 rows and 20 columns.
    Me._extData = New ExternalData(100, 20)

    ' Prepare the grid for virtual data.
    gridControl.ResetVolatileData()

    ' Hook up the events needed for the virtual grid.
    ' While only the QueryCellInfo is absolutely required, it would be unusual not to handle at least one of the count events.
    AddHandler gridControl.QueryCellInfo, New
```

## API Reference

### Namespaces and Classes
- `GridQueryCellInfoEventHandler`
- `GridRowColCountEventHandler`

### Methods and Events
- `GridControl.ResetVolatileData()`
- `GridControl.QueryCellInfo`
- `GridControl.QueryRowCount`
- `GridControl.QueryColCount`

### Parameters
- `RowCount`: The number of rows in the grid.
- `ColCount`: The number of columns in the grid.

## Code Examples

### C# Example

```csharp
// Example demonstrating initialization and event handling for virtual grid.
private void Form1_Load(object sender, System.EventArgs e)
{
    this._extData = new ExternalData(100, 20);
    gridControl.ResetVolatileData();

    gridControl.QueryCellInfo += new GridQueryCellInfoEventHandler(GridQueryCellInfo);
    gridControl.QueryRowCount += new GridRowColCountEventHandler(GridQueryRowCount);
    gridControl.QueryColCount += new GridRowColCountEventHandler(GridQueryColCount);
}
```

### VB.NET Example

```vb
' Example demonstrating initialization and event handling for virtual grid.
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    Me._extData = New ExternalData(100, 20)
    gridControl.ResetVolatileData()

    AddHandler gridControl.QueryCellInfo, New GridQueryCellInfoEventHandler(AddressOf GridQueryCellInfo)
    AddHandler gridControl.QueryRowCount, New GridRowColCountEventHandler(AddressOf GridQueryRowCount)
    AddHandler gridControl.QueryColCount, New GridRowColCountEventHandler(AddressOf GridQueryColCount)
End Sub
```

## See also
- [Virtual Grid Documentation](#)
- [External Data Management](#)
<!-- tags: [VirtualGrid, Syncfusion, GridControl, EventHandling, WinForms] keywords: [VirtualData, RowCount, ColCount, QueryCellInfo, QueryRowCount, QueryColCount, ExternalData] -->
```