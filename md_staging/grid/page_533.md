```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_533.jpeg
document_name: grid
page_number: 533
page_id: grid#page_533
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:23Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
this.gridControl1.BeginUpdate();
currentPercent = percent;
for (int i = 0; i <= gridControl1.ColCount; i++)
{
    for (int j = 0; j <= gridControl1.RowCount; j++)
        this.gridControl1[j, i].Font.Size = fontSize * currentPercent;
    this.gridControl.Model.ColWidths[i] = (int)(percent * defColWidth);
}
this.gridControl1.ColWidths[0] = (int)(percent * headerColWd);
this.gridControl.DefaultColWidth = (int)(percent * defColWidth);
this.gridControl.DefaultRowHeight = (int)(percent * defRowHeight);
this.gridControl1.RowHeights[0] = (int)(percent * headerRowHt);
this.gridControl1.EndUpdate();
this.gridControl1.Refresh();
```

### [VB.NET]

```vb
Private Sub zoomGrid(ByVal percent As Single)
    Me.label1.Text = Me.trackBar1.Value.ToString() & "%" 
    Me.label1.Refresh()

    Me.gridControl1.BeginUpdate()
    currentPercent = percent
    For i As Integer = 0 To gridControl1.ColCount
        For j As Integer = 0 To gridControl1.RowCount
            Me.gridControl1(j, i).Font.Size = fontSize * currentPercent
        Next j
        Me.gridControl1.Model.ColWidths(i) = CInt(Fix(percent * defColWidth))
    Next i

    Me.gridControl1.ColWidths(0) = CInt(Fix(percent * headerColWd))
    Me.gridControl.DefaultColWidth = CInt(Fix(percent * defColWidth))
    Me.gridControl.DefaultRowHeight = CInt(Fix(percent * defRowHeight))
    Me.gridControl1.RowHeights(0) = CInt(Fix(percent * headerRowHt))
    Me.gridControl1.EndUpdate()
    Me.gridControl1.Refresh()
End Sub
```

The preceding code sets the font and cell size using the percent parameter.

<!-- tags: [winforms, grid, zooming, font size, cell size, percent parameter] keywords: [gridcontrol, font size, colwidths, rowheights, defaultcolwidth, defaultrowheight, percent parameter] -->
``` 
