```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: calculate
page_number: 087
page_id: calculate#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:44Z
fidelity: lossless
-->

# Essential Calculate

```vb
dt.DefaultView.AllowUser = False
End Sub

' 2) This event handler raises the required ICalcData.ValueChanged event when the data in the DataTable changes.
Private Sub dt_ColumnChanged(ByVal sender As Object, ByVal e As DataColumnChangeEventArgs)
    Dim cm As CurrencyManager = CType(Me.BindingContext(Me.DataSource, Me.DataMember), CurrencyManager)
    Dim dt As DataTable = Me.DataSource
    Dim pos As Integer = cm.Position
    Dim field As Integer = dt.Columns.IndexOf(e.Column)
    Dim val As String = Me(pos, field).ToString()

    ' el.RowIndex, el.COLIndex needs to be one-based.
    Dim el = New ValueChangedEventArgs(pos + 1, field + 1, val)
    ValueChanged(Me, el)
End Sub

' 3) Returns the value at the one-based row and col.
Public Function GetvalueRowCol(ByVal row As Integer, ByVal col As Integer) As Object Implements ICalcData.GetvalueRowCol
    ' Row, col are one-based.
    Return Me(row - 1, col - 1)
End Function

' 4) Sets the value at the one-based row and col.
Public Sub SetvalueRowCol(ByVal value As Object, ByVal row As Integer, ByVal col As Integer) Implements ICalcData.SetvalueRowCol
    ' Row, col are one-based.
    Dim dt As DataTable = Me.DataSource
    dt.Rows(row - 1)(col - 1) = value
End Sub

' 5) Required ICalcData event.
Public Event ValueChanged As ValueChangedEventHandler Implements ICalcData.ValueChanged
' CalcDataGrid
End Class
```

The following is an explanation of the preceding code.

## Content

### Explanation of the Preceding Code

1. **ICalcData.WireParentObject Implementation**
   - This is the implementation of the `ICalcData.WireParentObject`. One of the requirements of the `ICalcData` object is to inform the `CalcEngine` "when" values have changed. This notification is crucial for the `CalcEngine` to maintain the proper state of its data structures. The `ICalcData` object fulfills this task by raising the `ICalcData.ValueChanged` event.

<!-- tags: [syncfusion, winforms, icacldata, valuechanged, eventhandler] keywords: [CalcEngine, DataTable, CurrencyManager, ValueChangedEventArgs, ICalcData, DataTableColumnChangeEventArgs] -->
``` 
```