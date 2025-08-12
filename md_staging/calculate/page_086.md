```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: calculate
page_number: 086
page_id: calculate#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:18Z
fidelity: lossless
-->

# Essential Calculate

```csharp
// e1.RowIndex, e1.ColIndex needs to be one-based.
Syncfusion.Calculate.ValueChangedEventArgs e1 = new
    ValueChangedEventArgs(pos + 1, field + 1, val);
ValueChanged(this, e1);
}

// 3) Returns the value at the one-based row and col.
public object GetValueRowCol(int row, int col)
{
    // Row, col are one-based.
    return this[row - 1, col - 1];
}

// 4) Sets the value at the one-based row and col.
public void SetValueRowCol(object value, int row, int col)
{
    // Row, col are one-based.
    DataTable dt = this.DataSource as DataTable;
    dt.Rows[row - 1][col - 1] = value;
}

// 5) Required ICalcData event.
public event ValueChangedEventHandler ValueChanged;
}
```

### [VB]

```vb
Public Class CalcDataGrid
    Inherits DataGrid
    Implements Syncfusion.Calculate.ICalcData

    Public Sub New()
        ' Avoids the complexity of sorting.
        Me.AllowSorting = False
    End Sub

    ' 1) Used to subscribe to the DataTable.ColumnChanged event. This event will
    ' raise the required ValueChanged event. Without this ValueChanged
    ' event, the CalcEngine would have no knowledge of the data.
    Public Sub WireParentObject() Implements ICalcData.WireParentObject
        ' Assumes the grid's datasource is a DataTable.
        Dim dt As DataTable = Me.DataSource
        AddHandler dt.ColumnChanged, AddressOf dt_ColumnChanged

        ' Avoids the complexity of a new row.
    End Sub
```

<!-- tags: [Syncfusion Winforms, Calculate, ICalcData, ValueChangedEventArgs, DataTable, ColumnChanged event] keywords: [calculate, data grid, data source, value changed, column changed event, event handling, one-based index, VB, CSharp] -->
```