<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: grid
page_number: 104
page_id: grid#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:25:44Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
_GGridQueryCellInfoEventHandler(AddressOf GridQueryCellInfo)
AddHandler gridControl1.QueryRowCount, New _GridRowColCountEventHandler(AddressOf GridQueryRowColCount)
_GGridQueryCellInfoEventHandler(AddressOf GridQueryCellInfo)
AddHandler gridControl1.QueryColCount, New _GridRowColCountEventHandler(AddressOf GridQueryColCount)
End Sub
```

## 3.1.5.4 Style Properties

In your `GridQueryCellInfo` handler, it is possible to set the style properties other than the `CellValue`. For example, the code that follows will color any value that is divisible by three.

To set properties other than the `CellValue`, change your `QueryCellInfo` event handler as shown below.

### C#

```csharp
void GridQueryCellInfo(object sender, GridQueryCellInfoEventArgs e)
{
    if (e.RowIndex > 0 && e.ColIndex > 0)
    {
        // Set Cell Value.
        e.Style.CellValue = this._extData[e.RowIndex - 1, e.ColIndex - 1];

        // Apply conditional formatting.
        if (this._extData[e.RowIndex - 1, e.ColIndex - 1] % 3 == 0)
            e.Style.BackColor = Color.LightPink;
        e.Handled = true;
    }
}
```

### VB.NET

```vb
Private Sub GridQueryCellInfo(ByVal sender As Object, ByVal e As GridQueryCellInfoEventArgs)
    If ((e.RowIndex > 0) AndAlso (e.ColIndex > 0)) Then

        ' Set Cell Value.
        e.Style.CellValue = Me._extData(e.RowIndex - 1, e.ColIndex - 1)

        ' Apply conditional formatting.
    End If
End Sub
```

---

<!-- tags: [syncfusion, winforms, essential grid, style properties, c#, vb.net, cell formatting, grid query cellinfo, grid element] keywords: [divisible by three, conditional formatting, cell value, event handler, style property] -->