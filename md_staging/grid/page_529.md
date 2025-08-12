```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_529.jpeg
document_name: grid
page_number: 529
page_id: grid#page_529
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:14Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

```csharp
{
    e.Count = this.numArrayCols;
    e.Handled = true;
}
```

### Using VB.NET

```vb
' Determine number of rows.
Private Me.gridControl1.QueryRowCount += New GridRowColCountEventHandler(AddressOf GridQueryRowCount)
Private Sub GridQueryRowCount(ByVal sender As Object, ByVal e As GridRowColCountEventArgs)
    e.Count = Me.numArrayRows
    e.Handled = True
End Sub

// Determine the number of columns.
Private Me.gridControl1.QueryColCount += New GridRowColCountEventHandler(AddressOf GridQueryColCount)
Private Sub GridQueryColCount(ByVal sender As Object, ByVal e As GridRowColCountEventArgs)
    e.Count = Me.numArrayCols
    e.Handled = True
End Sub

// Pass value to a cell from a given data source.
Private Me.gridControl1.QueryCellInfo += New 
```

### Copyright Information

© 2013 Syncfusion. All rights reserved. 529 | Page
```