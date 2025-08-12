```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_530.jpeg
document_name: grid
page_number: 530
page_id: grid#page_530
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:43Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
GridQueryCellInfoEventHandler(AddressOf QueryCellInfoHandler)
Private Sub GridQueryCellInfo(ByVal sender As Object, ByVal e As GridQueryCellInfoEventArgs)
    If e.ColIndex > 0 AndAlso e.RowIndex > 0 Then

        '// By using indexers, pass value to a cell from a given data source.
        e.Style.CellValue = Me.intArray(e.RowIndex - 1, e.ColIndex - 1)
        e.Handled = True
    End If
End Sub
```

**Figure 204: Grid Population**

A sample demonstrating this feature is available under the following sample installation path.

```bash
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Performance\Trader Grid Test Demo
```

## Page-level Navigation/TOC (if applicable)

- **Grid Population Demonstration**
  - Overview of Grid Population
  - Code Sample for Grid Querycellinfo Event Handler
  - Grid Interactions and Performance

## API Reference (if applicable)

- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridQueryCellInfoEventArgs
- **Event:** QueryCellInfo
- **Properties:**
  - **ColIndex:** Gets or sets the column index of the current cell.
  - **RowIndex:** Gets or sets the row index of the current cell.
  - **Handled:** Gets or sets a value indicating whether the event should be handled.
  - **Style:** Represents the style of the current cell.
- **Parameters:**
  - **sender:** The source of the event.
  - **e:** An instance of GridQueryCellInfoEventArgs containing event data.
- **Returns:** None (Event)
- **Exceptions:** None

## Code Examples (multi-language supported)

```vb
Private Sub GridQueryCellInfo(ByVal sender As Object, ByVal e As GridQueryCellInfoEventArgs)
    If e.ColIndex > 0 AndAlso e.RowIndex > 0 Then
        e.Style.CellValue = Me.intArray(e.RowIndex - 1, e.ColIndex - 1)
        e.Handled = True
    End If
End Sub
```

## Cross References

See also:
- [Grid Data Binding](#grid-data-binding)
- [Virtual Grid Mode](#virtual-grid-mode)
- [Events and Event Handling](#events-and-event-handling)

<!-- tags: [winforms, grid, virtualmode, performance, gridquerycellinfoeventhandler, tradergridtestdemo, syncfusion, windowsforms] keywords: [grid population, essential grid, windows forms, querycellinfo, handler, cellvalue, handled, rowindex, colindex, indexers, sample installation path, trader grid test demo] -->
```