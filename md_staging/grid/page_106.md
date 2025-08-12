```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_106.jpeg
document_name: grid
page_number: 106
page_id: grid#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:26:34Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
e.Handled = true;
}

// Set number of columns from external data source.
void GridQueryColCount(object sender, GridRowColCountEventArgs e)
{
    e.Count = this._extData.ColCount;
    e.Handled = true;
}
```

## [VB.NET]

```vb
' Set number of rows from external data source.
Private Sub GridQueryRowCount(ByVal sender As Object, ByVal e As GridRowColCountEventArgs)
    e.Count = Me._extData.RowCount
    e.Handled = True
End Sub

' Set number of columns from external data source.
Private Sub GridQueryColCount(ByVal sender As Object, ByVal e As GridRowColCountEventArgs)
    e.Count = Me._extData.ColCount
    e.Handled = True
End Sub
```

### Add a `QueryCellInfo` event handler.

The `GridQueryCellInfo` is the event handler where the grid expects the external data source to provide the cell values that are in demand. Here is how it can be implemented with the external data source. Recall that row 0 and column 0 are usually the header columns in a grid. In the `GridQueryCellInfo`, do not provide these values and use the default headers. If you need to provide special header values, you can do so.

```csharp
[C#]

void GridQueryCellInfo(object sender, GridQueryCellInfoEventArgs e)
{
    if (e.RowIndex > 0 && e.ColIndex > 0)
    {
        e.Style.CellValue = this._extData[e.RowIndex - 1, e.ColIndex - 1];
        e.Handled = true;
    }
}
```
```