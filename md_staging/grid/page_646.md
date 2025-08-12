<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_646.jpeg
document_name: grid
page_number: 646
page_id: grid#page_646
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

```vb
End If
ElseIf TypeOf el Is GridSummaryRow Then

    ' You can get the column as follows.
    Dim column As GridColumnDescriptor =
Me.gridGroupingControl1.TableModel.GetHeaderColumnDescriptorAt(e.TableCellIdentity.ColIndex)
    If column IsNot Nothing AndAlso
table.TotalSummaries.IndexOf(column.MappingName) <> -1 Then
        Dim index As Integer =
column.TableDescriptor.Fields.IndexOf(column.FieldDescriptor)
        Dim tsa As IManualTotalSummaryArraySource =
TryCast((IIf(TypeOf el Is Group, el, el.ParentGroup)), IManualTotalSummaryArraySource)
        Dim tm As ManualTotalSummary =
tsa.GetManualTotalSummaryArray()(index)
        e.Style.CellValue = tm.Total
        e.Style.CellValueType = GetType(Double)
        e.Style.Format = "0.00"

        By using that column you could try and identify the summary that should be displayed in this cell.
        End If
    End If
End Sub
```

- Enable highlighting of the cells changed for all the columns.

### [C#]

```csharp
for (int c = 0; c < gridGroupingControl1.TableDescriptor.Columns.Count; c++)
    this.gridGroupingControl1.TableDescriptor.Columns[c].AllowBlink = true;
this.gridGroupingControl1.BlinkTime = 100;
```

### [VB.NET]

```vb
Do While c < gridGroupingControl1.TableDescriptor.Columns.Count
    Me.gridGroupingControl1.TableDescriptor.Columns(c).AllowBlink = True
    c += 1
Loop
Me.gridGroupingControl1.BlinkTime = 100
```

- To optimize the performance, the grid is updated manually (UpdateDisplayFrequency = 0) at regular intervals. A timer is used to keep track of the duration of the time periods. The code to track the changes in Freight and EmployeeID columns and to update the grid rows is written inside the timer_tick event handler where the update is done manually by

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridGroupingControl
- **Properties**:
  - `TableModel.GetHeaderColumnDescriptorAt()`
  - `TotalSummaries.IndexOf()`
  - `TableDescriptor.Fields.IndexOf()`
  - `GetManualTotalSummaryArray()`
  - `CellValue`
  - `CellValueType`
  - `Format`
  - `TableDescriptor.Columns`
  - `AllowBlink`
  - `BlinkTime`

## Code Examples

### VB.NET Example

```vb
Do While c < gridGroupingControl1.TableDescriptor.Columns.Count
    Me.gridGroupingControl1.TableDescriptor.Columns(c).AllowBlink = True
    c += 1
Loop
Me.gridGroupingControl1.BlinkTime = 100
```

### C# Example

```csharp
for (int c = 0; c < gridGroupingControl1.TableDescriptor.Columns.Count; c++)
    this.gridGroupingControl1.TableDescriptor.Columns[c].AllowBlink = true;
this.gridGroupingControl1.BlinkTime = 100;
```

## Cross References

- **Related Documentation**: Essential Grid for Windows Forms, GridGroupingControl, TotalSummaries

## RAG Annotations

<!-- tags: [syncfusion, windows.forms, gridgroupingcontrol, totalsummaries, performanceoptimization] keywords: [essential grid, windows forms, gridgroupingcontrol, total summaries, cell highlighting, update frequency, timer, performance] -->