```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_415.jpeg
document_name: grid
page_number: 415
page_id: grid#page_415
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:42Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

```vb
' Determine number of rows.
e.Count = Me.numArrayRows
e.Handled = True
End Sub
```

### 4.1.4.11.1.2 QueryColCount Event

#### Overview
- The `QueryColCount` event is used to return the column count on demand.
- Handling the event by assigning `e.Count` sets the `e.Handled` property to `True`.

#### Content
The `QueryColCount` event is used to return the column count on demand. Note that when you handle the event by assigning `e.Count`, you are setting the `e.Handled` property to `true`.

**C#**

```csharp
private void GridQueryColCount(object sender, GridRowColCountEventArgs e)
{
    // Determine the number of columns.
    e.Count = this.numArrayCols;
    e.Handled = true;
}
```

**VB.NET**

```vb
Private Sub GridQueryColCount(ByVal sender As Object, ByVal e As GridRowColCountEventArgs)

    ' Determine the number of columns.
    e.Count = Me.numArrayCols
    e.Handled = True
End Sub
```

### 4.1.4.11.1.3 QueryCellInfo Event

#### Overview
- `QueryCellInfo` is the core event for cell-specific configurations.
- Used to provide the `GridStyleInfo` object for a given cell.
- Handlers typically set the `CellValue` and can adjust other properties like `BackColor`.

#### Content
QueryCellInfo is the workhorse event. It is used to provide the `GridStyleInfo` object for a given cell. In your handler for this event, you would normally set the `CellValue` for the `GridStyleInfo` object passed in with the event arguments. But, you can also set other members of this `GridStyleInfo` object. For example, you can set the `BackColor` to change the cell background. All of this is done on a demand basis. The `BackColor` value is not stored in any grid storage. There is another event, `PreViewStyleInfo` that you can handle to make a transient adjustment to a style just before it is displayed. This event is discussed in more detail later in this section.

---

<!-- tags: [syncfusion, winforms, grid, event, querycolcount, querycellinfo] keywords: [essential grid, windows forms, QueryColCount, column count, QueryCellInfo, cell configuration, GridStyleInfo, CellValue, BackColor, PreViewStyleInfo] -->
```