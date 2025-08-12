```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_416.jpeg
document_name: grid
page_number: 416
page_id: grid#page_416
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The GridQueryCellInfoEventArgs members, e.ColIndex and e.RowIndex, specify the column and row of the requested style. The e.Style member holds the GridStyleInfo object whose value this event should set provided it is a cell that you want to populate. It is possible that e.ColIndex and / or e.RowIndex may have the value of -1. A -1 indicating that a **rowstyle** or **columnstyle** is being requested. So, e.ColIndex = -1 and e.RowIndex = 4 indicates that the rowstyle for row 4 is being requested (GridControl.RowStyle[4]). Similarly, a positive column value with the row value = -1 would be a request for that particular columnstyle. If both values are -1, then the **TableStyle** property is being requested.

One last comment before we look at the code. Header rows and columns in an Essential Grid are treated the same as other rows and columns with respect to QueryCellInfo. If you have a single header row, then anytime e.ColIndex is 0, a row header is being requested. Similarly, if you have a single column header row, e.RowIndex = 0 is a request for the column header.

### C#

```csharp
private void GridQueryCellInfo(object sender, GridQueryCellInfoEventArgs e)
{
    if (e.ColIndex > 0 && e.RowIndex > 0)
    {
        // Using indexers, pass value to a cell from a given data source.
        e.Style.CellValue = this.intArray[e.RowIndex - 1, e.ColIndex - 1];
        e.Handled = true;
    }
}
```

### VB.NET

```vb.net
Private Sub GridQueryCellInfo(ByVal sender As Object, ByVal e As GridQueryCellInfoEventArgs)
    If ((e.ColIndex > 0) AndAlso (e.RowIndex > 0)) Then
        ' Using indexers, pass value to a cell from a given data source.
        e.Style.CellValue = Me.intArray(e.RowIndex - 1, e.ColIndex - 1)
        e.Handled = True
    End If
End Sub
```
```