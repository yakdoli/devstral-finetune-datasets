```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_649.jpeg
document_name: grid
page_number: 649
page_id: grid#page_649
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:53Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
}
}
```

[VB.NET]

```vb
Private Sub timer_tick(ByVal sender As Object, ByVal e As EventArgs)
    Dim td As GridTableDescriptor = 
        Me.gridGroupingControl1.TableDescriptor
    Dim tb As ManualTotalSummaryTable = 
        CType(Me.gridGroupingControl1.Table, ManualTotalSummaryTable)
    Dim i As Integer = 0

    MeasureTime.Measure("Form1.timer_tick")
    Try
        Dim count As Integer = 1000

        If gridGroupingControl1.SortPositionChangedBehavior = 
           GridListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate Then
            If sortedByFreight OrElse
               gridGroupingControl1.TestDeleteRecords OrElse
               gridGroupingControl1.TestInsertRecords OrElse
               gridGroupingControl1.TestChangeGroup Then

                ' When sort position is changed, this is much more
                ' demanding, let's do less records then.
                count = 200
            End If

            If sortedByEmployeeID Then

                ' Each update will cause records being shifted around, so
                ' let's do even less records. You can also check out
                ' InvalidateAll option instead above.
                count = 50
            End If
        End If

        i = 0
        Do While i < count
            Dim dr As ManualTotalSummaries.DataSet1.OrdersRow

            ' Insert Records.
            If gridGroupingControl1.TestInsertRecords Then
                If i Mod 10 = 0 Then
                    dr = northwindDataSet1.Orders.NewOrdersRow()
                    dr.CustomerID = i.ToString() & (j += 1).ToString()
                End If
            End If
        Loop
    Catch ex As Exception
        Trace.WriteLine("Exception in timer_tick: " & ex.Message)
    Finally
        MeasureTime.StopMeasure("Form1.timer_tick")
    End Try
End Sub
```

## API Reference (if applicable)

### Namespaces and Classes
- `GridListChangedInsertRemoveBehavior`
- `MeasureTime`
- `GridTableDescriptor`
- `ManualTotalSummaryTable`
- `GridGroupingControl`

## Code Examples

The provided VB.NET code demonstrates a timer tick event handler that performs operations on a `GridGroupingControl` with a `ManualTotalSummaryTable`. It measures the performance of certain operations and adjusts the number of records to process based on the current sorting and testing conditions.

## Cross References

See also:
- [Syncfusion Grid Documentation](https://www.syncfusion.com/documentation/windows-forms)
- [Timer Events in Windows Forms](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.timer?view=netframework-4.8)

<!-- tags: [Grid, Timer, Windows Forms, ManualTotalSummaryTable, GridListChangedInsertRemoveBehavior, MeasureTime] keywords: [timer_tick, GridGroupingControl, manual total summary, sort position changed, performance measurement] -->
```