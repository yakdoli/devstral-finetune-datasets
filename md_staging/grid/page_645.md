```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_645.jpeg
document_name: grid
page_number: 645
page_id: grid#page_645
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:38Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
Dim tb As ManualTotalSummaryTable = DirectCast(Me.gridGroupingControl1.Table, ManualTotalSummaryTable)
tb.TotalSummaries.Add("Freight")
tb.TotalSummaries.Add("EmployeeID")
tb.TableDirty = True

AddHandler Me.gridGroupingControl1.QueryCellStyleInfo, AddressOf gridGroupingControl1_QueryCellStyleInfo

Private Sub gridGroupingControl1_QueryCellStyleInfo(ByVal sender As Object, ByVal e As GridTableCellStyleEventArgs)
    Dim el As Element = e.TableCellIdentity.DisplayElement
    Dim table As ManualTotalSummaryTable = TryCast(el.ParentTable, ManualTotalSummaryTable)

    If table Is Nothing Then
        Return
    End If

    If Element.IsCaption(el) Then
        If e.Style.TableCellIdentity.ColIndex > 3 Then

            ' You need to provide manually, the code to look up the summaries you want to display here.
            ' e.TableCellIdentity.Column and e.TableCellIdentity.SummaryColumn will be null.
            ' You can get the column as follows.
            Dim column As GridColumnDescriptor = 
            gridGroupingControl1.TableModel.GetHeaderColumnDescriptorAt(e.TableCellIdentity.ColIndex)

            If column IsNot Nothing AndAlso table.TotalSummaries.IndexOf(column.MappingName) <> -1 Then
                Dim index As Integer = column.TableDescriptor.Fields.IndexOf(column.FieldDescriptor)
                Dim tsa As IManualTotalSummaryArraySource = TryCast((IIf(TypeOf el Is Group, el, el.ParentGroup)), IManualTotalSummaryArraySource)
                Dim tm As ManualTotalSummary = tsa.GetManualTotalSummaryArray()(index)
                e.Style.CellValue = tm.Total
                e.Style.CellValueType = GetType(Double)
                e.Style.Format = "0.00"

                ' By using that column you could try and identify the summary that should be displayed in this cell.
            End If
        End If
    End If
End Sub
```

---

© 2013 Syncfusion. All rights reserved. 645 | Page

<!-- tags: [Syncfusion Winforms, grid, Table Summary, ManualTotalSummaryTable, QueryCellStyleInfo] keywords: [Table Summary, Manual Total Summary, gridGroupingControl, TotalSummaries, QueryCellStyleInfo, Element, DisplayElement, TableCellIdentity, GridColumnDescriptor, IManualTotalSummaryArraySource, ManualTotalSummaryArray] -->
```